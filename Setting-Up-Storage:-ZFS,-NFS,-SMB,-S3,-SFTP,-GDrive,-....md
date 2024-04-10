ArchiveBox supports a wide range of local and remote filesystems, both in Docker and on bare metal. The examples below use [Docker Compose bind mounts](https://docs.docker.com/storage/bind-mounts/) to demonstrate the concepts, you can adapt them to your OS and environment needs.

Example [`docker-compose.yml`](https://github.com/ArchiveBox/ArchiveBox/blob/dev/docker-compose.yml) storage setup:
```yaml
services:
    archivebox:
        ...
        volumes:
            # your index db, config, logs, etc. should be stored on a local SSD (usually <10Gb)
            - ./data:/data

            # but bulk archive/ content can be located on an HDD or remote filesystem
            - /mnt/archivebox/data/archive:/data/archive
```

## Supported Local Filesystems

### ZFS ⭐️

> [!TIP]
> This is the recommended filesystem for ArchiveBox. 

- https://openzfs.github.io/openzfs-docs/
- https://openzfs.github.io/openzfs-docs/man/v2.2/8/zpool-create.8.html
- https://openzfs.github.io/openzfs-docs/man/v2.2/8/zfs-create.8.html
- https://docs.docker.com/storage/storagedriver/zfs-driver/
- https://www.ixsystems.com/blog/fast-dedup-is-a-valentines-gift-to-the-openzfs-and-truenas-communities/

```bash
# create a new archivebox pool to hold your dataset
zpool create -f \
    -O mountpoint=/mnt/archivebox \
    -O sync=standard \
    -O compression=lz4 \
    -O recordsize=128K \
    -O dnodesize=auto \
    -O atime=off \
    -O xattr=sa \
    -O acltype=posixacl \
    -O aclinherit=passthrough \
    -O utf8only=on \
    -O normalization=formD \
    -O casesensitivity=sensitive \
    archivebox /dev/disk/by-uuid/disk1... /dev/disk/by-uuid/disk2...

# create the archivebox/data ZFS dataset
zfs create \
    -o mountpoint=/mnt/archivebox/data \
    archivebox/data

# optional: add encryption
    -o encryption=on \
    -o keysource=passphrase,prompt \
```


### EXT4, APFS

> [!TIP]
> These filesystems are fully supported by ArchiveBox.

### NTFS, HFS+, BTRFS

> [!WARNING]
> Likely supported, but not officially tested.

### EXT2, EXT3, FAT32, exFAT

> [!CAUTION]
> Not recommended. Cannot store more than 31k ~ 65k Snapshot entries due to directory entry limits.

<br/>

---

<br/>

## Supported Remote Filesystems

ArchiveBox supports most common types of remote filesystems using NFS and the `rclone` Docker volume plugin.


### NFS (Docker Driver)

`docker-compose.yml`:
```yaml
services:
    archivebox:
        volumes:
            - ./data:/data
            - archivebox-archive:/data/archive

volumes:
    archivebox-archive:
        driver_opts:
            type: "nfs"
            o: "addr=some-remote-server.example.com,nolock,soft,rw,nfsvers=4"
            device: ":/archivebox-archive"
```

### SMB / Ceph (Docker CIFS Driver)

`docker-compose.yml`:
```yaml
services:
    archivebox:
        volumes:
            - ./data:/data
            - archivebox-archive:/data/archive

volumes:
    archivebox-archive:
        driver: local
        driver_opts:
            type: cifs
            device: "//some-remote-server.example.com/archivebox-archive"
            o: "username=XXX,password=YYY,uid=911,gid=911"
```

### Amazon S3 / Backblaze B2 / Google Drive / etc. (RClone)

```bash
# whether or not you're using Docker, you must first install rclone on your host system
apt install rclone fuse     # or brew install

# allow sharing FUSE volumes between Docker and Host
echo 'user_allow_other' >> /etc/fuse.conf
```

Then define your remote storage config `~/.config/rclone/rclone.conf`:

> [!TIP]
> You can also create your config using the RClone Web GUI:  
> `rclone rcd --rc-web-gui`

```ini
# Example rclone.conf using Amazon S3 for storage:
[archivebox-s3]
type = s3
provider = AWS
access_key_id = XXX
secret_access_key = YYY
region = us-east-1
```

#### RClone Config Examples

- [SMB](https://rclone.org/smb/) / [Ceph](https://rclone.org/s3/#ceph) / [SFTP](https://rclone.org/sftp/) / [FTP](https://rclone.org/ftp/) / [WebDAV (e.g. Nextcloud)](https://rclone.org/webdav/)
- [Google Drive](https://rclone.org/drive/) / [Dropbox](https://rclone.org/dropbox/) / [OneDrive](https://rclone.org/onedrive/)
- [Amazon S3](https://rclone.org/s3/#configuration) / [Backblaze B2](https://rclone.org/b2/) / [Cloudflare R2](https://rclone.org/s3/#cloudflare-r2) / [DigitalOcean Spaces](https://rclone.org/s3/#digitalocean-spaces)
- [Google Cloud Storage](https://rclone.org/s3/#google-cloud-storage) / [Azure Blob](https://rclone.org/azureblob/) / [Azure Files](https://rclone.org/azurefiles/)
- [Storj](https://rclone.org/s3/#storj) / [Sia](https://rclone.org/sia/) / [Archive.org Storage](https://rclone.org/internetarchive/)
- And many more...
  - https://rclone.org/s3/
  - https://rclone.org/overview/

*Bonus:*
- Set up gzip compression: https://rclone.org/compress/
- Set up file encryption: https://rclone.org/crypt/
- Set up hashing engine: https://rclone.org/hasher/


#### Running RClone on Bare Metal host

See here for full instructions: https://rclone.org/commands/rclone_mount/

```bash
# run this long-running command to mount the remote volume containing data/archive
rclone mount --allow-other --uid 911 --gid 911 \
             --vfs-cache-mode=full --transfers=16 --checkers=4 \
             archivebox-s3/data/archive:/opt/archivebox/data/archive
```

> [!TIP]
> You can also pass an Rclone mount created on the host as a normal bind mount volume to Docker containers (without needing the storage plugin below).  
> (just make sure it's mounted with `--allow-other`)

#### Running RClone with Docker Storage Plugin

See here for full instructions: https://rclone.org/docker/

First, install the [Rclone Docker Volume Plugin](https://rclone.org/docker/#installing-as-managed-plugin) for your CPU architecture:
```bash
docker plugin install rclone/docker-volume-rclone:amd64 --grant-all-permissions --alias rclone
ln -sf ~/.config/rclone/rclone.conf /var/lib/docker-plugins/rclone/config/rclone.conf
```

Then, [create a volume using the Docker CLI](https://rclone.org/docker/#creating-volumes-via-cli) or [define one using Docker Compose / Swarm](https://rclone.org/docker/#using-with-swarm-or-compose):

`docker-compose.yml`:
```yaml
services:
    archivebox:
        volumes:
            - ./data:/data
            - archivebox-s3:/data/archive

volumes:
    archivebox-s3:
        driver: rclone
        driver_opts:
            remote: 'archivebox-s3/data/archive'
            allow_other: 'true'
            vfs_cache_mode: full
            poll_interval: 0
            uid: 911
            gid: 911
            transfers: 16
            checkers: 4
```


To start the container and verify the filesystem is accessible within it:
```bash
docker compose run archivebox /bin/bash 'ls -lah /data/archive/'
```

<br/>
---
<br/>

### More Docker Storage Plugins

- [IPFS](https://github.com/djdv/go-filesystem-utils/pull/40) / [Peergos](https://github.com/peergos/peergos)
- [GlusterFS](https://github.com/calavera/docker-volume-glusterfs) / 
- DigitalOcean Block Storage Volumes: https://github.com/djmaze/dobs-volume-plugin
- Linode Block Storage Volumes: https://github.com/linode/docker-volume-linode
- More volume plugins: https://docs.docker.com/engine/extend/legacy_plugins/#volume-plugins