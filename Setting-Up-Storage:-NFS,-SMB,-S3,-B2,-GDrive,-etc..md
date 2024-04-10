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

> [!SUCCESS]
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

### BTRFS

> [!WARNING]
> Likely supported on Linux, but not officially tested.

- https://docs.docker.com/storage/storagedriver/btrfs-driver/

### EXT4

> [!SUCCESS]
> This is supported by ArchiveBox on Linux systems.

### APFS

> [!SUCCESS]
> This is supported by ArchiveBox on macOS systems.

### HFS+

> [!WARNING]
> Likely supported on macOS, but not officially tested.

### NTFS

> [!WARNING]
> Likely supported on Windows through Docker and/or WSL2, but not officially tested.

### EXT2 / EXT3

> [!DANGER]
> Not recommended. Cannot store more than 31,998 Snapshot entries due to directory entry limit.

### FAT32 / exFAT

> [!DANGER]
> Not recommended. Cannot store more than 65,536 Snapshot entries due to directory entry limit.

<br/><hr/><br/>

## Supported Remote Filesystems

ArchiveBox supports most common types of remote filesystems using NFS and the `rclone` Docker volume plugin.


### NFS

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

### SMB / CIFS / Ceph

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

### Other Docker Volume Plugin Filesystems

- [IPFS](https://github.com/djdv/go-filesystem-utils/pull/40) / [Peergos](https://github.com/peergos/peergos)
- [GlusterFS](https://github.com/calavera/docker-volume-glusterfs) / 
- DigitalOcean Block Storage Volumes: https://github.com/djmaze/dobs-volume-plugin
- Linode Block Storage Volumes: https://github.com/linode/docker-volume-linode
- More volume plugins: https://docs.docker.com/engine/extend/legacy_plugins/#volume-plugins


### RClone: Amazon S3 / Backblaze B2 / Google Drive / Storj / etc.

```bash
# easier: create your storage config using the RClone Web GUI
rclone rcd --rc-web-gui
```
```bash
# harder: create your storage config manually in ~/.config/rclone/rclone.conf:
```ini
# Example using Amazon S3 for storage
[archivebox-s3]
type = s3
provider = AWS
access_key_id = XXX
secret_access_key = YYY
region = us-east-1
```
**Examples:**

- [SMB](https://rclone.org/smb/) / [Ceph](https://rclone.org/s3/#ceph) / [SFTP](https://rclone.org/sftp/) / [FTP](https://rclone.org/ftp/) / [WebDAV (e.g. Nextcloud)](https://rclone.org/webdav/)
- [Google Drive](https://rclone.org/drive/) / [Dropbox](https://rclone.org/dropbox/) / [OneDrive](https://rclone.org/onedrive/)
- [Amazon S3](https://rclone.org/s3/#configuration) / [Backblaze B2](https://rclone.org/b2/) / [Cloudflare R2](https://rclone.org/s3/#cloudflare-r2) / [DigitalOcean Spaces](https://rclone.org/s3/#digitalocean-spaces)
- [Google Cloud Storage](https://rclone.org/s3/#google-cloud-storage) / [Azure Blob](https://rclone.org/azureblob/) / [Azure Files](https://rclone.org/azurefiles/)
- [Storj](https://rclone.org/s3/#storj) / [Sia](https://rclone.org/sia/) / [Archive.org Storage](https://rclone.org/internetarchive/)
- And many more...
  - https://rclone.org/s3/
  - https://rclone.org/overview/

*Bonus features:*
- Transparent gzip compression: https://rclone.org/compress/
- Transparent file encryption: https://rclone.org/crypt/
- Hasher for other filesystems: https://rclone.org/hasher/

#### Setup

```bash
apt install rclone     # or brew install rclone
nano ~/.config/rclone/rclone.conf

# for Docker, install the volume plugin for your CPU architecture
docker plugin install rclone/docker-volume-rclone:amd64 --grant-all-permissions --alias rclone
ln -sf ~/.config/rclone/rclone.conf /var/lib/docker-plugins/rclone/config/rclone.conf

# for bare-metal, run this to mount the remote volume
rclone mount --allow-other --uid 911 --gid 911 --vfs-cache-mode=full --transfers=16 --checkers=4 archivebox-s3:/mnt/archivebox-s3
```
See the full [Rclone + Docker Documentation](https://rclone.org/docker/) for more help and examples...

Then you can start the container and verify the filesystem is accessible within it:
```bash
docker compose run archivebox /bin/bash 'ls -lah /data/archive/'
```