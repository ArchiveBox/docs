# Upgrading Versions

```bash
# cd /path/to/your/archivebox/data
cd ~/archivebox/data

pip install --upgrade --ignore-installed archivebox
# or
docker pull archivebox/archivebox:latest

# upgrade the collection to a new version
archivebox init
```


**✅ Upgrading checklist:**

1. Find the version you want to upgrade to on https://github.com/ArchiveBox/ArchiveBox/releases
2. **Read the release notes carefully** for any instructions or extra steps around upgrading for each release you're skipping or installing
3. **Make a full backup** of your `index.sqlite3` and `archive/` content before upgrading!  
`gzip -9 < index.sqlite3 > "index.sqlite3.$(date +%s).bak"`
4. Follow the steps below depending on your setup to run `archivebox init` (repeating as necessary for each major version if upgrading across multiple major versions)
5. Confirm the upgrade succeeded and check for any orphan/corrupted snapshots with `archivebox status`

💬 [Open an issue](https://github.com/ArchiveBox/ArchiveBox/issues/new/choose) in our bug tracker if you experience any problems with upgrading/merging/modifying collections.

---

*Note: It's recommended to only upgrade one major version at a time. e.g. if you're on `v0.4.14`, upgrade to `v0.5.6` next, then `v0.6.3`, and finally `v0.7.1` (as 3 separate steps).
You can specify exact versions with pip like so: `pip install archivebox==0.6.3` or with docker `docker pull archivebox/archivebox:0.6.3`. Upgrading directly across multiple major versions may work in some cases, but is not recommended for maximum data safety.*


---
---

**ℹ️ How it works internally:**

The same command is used for initializing a new archive and upgrading an existing one. `archivebox init` is indempotent and safely be run multiple times. Running it will ensure your collection is on the latest version and all the files are in their correct locations. `archivebox status` can be used to check for orphan/corrupted snapshots or invalid index data.

There are three main areas on disk that ArchiveBox modifies during upgrades:
- `index.sqlite3` contains the SQLite3 DB index that gets upgraded automatically by Django based on the changes in [`archivebox/core/models.py`](https://github.com/ArchiveBox/ArchiveBox/blob/dev/archivebox/core/models.py).
- `archive/*/index.json` these files are redundant json exports of the data for each Snapshot in `index.sqlite3`, these files are overwritten on every `archivebox update` run or anytime the Snapshot is modified from the GUI or CLI. These files will be [lazily updated](https://github.com/ArchiveBox/ArchiveBox/issues/962) to the latest schema versions as ArchiveBox accesses them, but are usually not modified in bulk during `archivebox init` when upgrading.
- `archive/*` the Snapshot output files may be moved or renamed by future upgrades (so far they have remained unchanged since v0.1, but future versions reserve the right to change their locations)

The `ArchiveBox.conf` file is not modified by upgrades and should remain forward-compatible across future versions (even when config options are renamed, we check the old names internally to maintain compatibility).

As of v0.4 and above, ArchiveBox uses the Django migrations system for deterministic, atomic, safe upgrades, so your DB should always be left in a consistent state in the event of a failure or power outage. If you need help fixing a corrupted collection, open an issue using the link above.

More info:
- https://docs.djangoproject.com/en/4.0/topics/migrations/
- https://github.com/ArchiveBox/ArchiveBox/wiki/Upgrading-or-Merging-Archives#database-migrations-errors-or-upgrade-issues
- https://github.com/ArchiveBox/ArchiveBox/wiki/Troubleshooting

---

### Upgrading with Docker Compose ⭐️

Using Docker Compose is recommended because it makes upgrading a breeze! ✨  
Pulling and running the latest version automatically upgrades the ArchiveBox collection and all of ArchiveBox's internal dependencies.

```bash
cd ~/archivebox        # or wherever your folder containing docker-compose.yml is
docker-compose down    # stop the currently running archivebox containers
docker-compose down    # run twice to clear stopped containers
docker-compose pull    # pull the latest image version from Docker Hub
docker-compose up      # collection will be automatically upgraded as it starts
```

More info:
- https://github.com/ArchiveBox/ArchiveBox#%EF%B8%8F-easy-setup
- https://github.com/ArchiveBox/ArchiveBox/wiki/Docker#docker-compose
- https://github.com/ArchiveBox/ArchiveBox/wiki/Docker#setup

### Upgrading with plain Docker

Upgrading with plain Docker is similar to the process with Docker Compose, but you have to run `archivebox init` manually at the end to finish the process.

```bash
docker ps -a -q  --filter ancestor=archivebox/archivebox  # find any currently running archivebox containers
docker kill <image>    # stop any currently running archivebox versions

docker pull archivebox/archivebox
docker run -v $PWD:/data -it archivebox/archivebox init  # upgrade the collection to the latest version

# restart the archivebox server container if needed
docker run -v $PWD:/data -it -p 8000:8000 archivebox/archivebox server 0.0.0.0:8000
```

More info:
- https://github.com/ArchiveBox/ArchiveBox#%EF%B8%8F-easy-setup
- https://github.com/ArchiveBox/ArchiveBox/wiki/Docker#docker
- https://github.com/ArchiveBox/ArchiveBox/wiki/Docker#setup-1

### Upgrading with a package manager

Package manager releases take a lot of effort to maintain ([contributions welcome!](https://github.com/ArchiveBox/ArchiveBox/wiki/Donations)) and sometimes lag behind the Docker releases. We make a best effort to have the latest release available through all channels within a reasonable timeframe.

```bash
cd ~/archivebox/data   # or wherever your data folder is
killall archivebox     # stop the currently running archivebox version

# upgrade ArchiveBox using the package manager you originally used to install it
pip install --upgrade --ignore-installed archivebox
# or
apt install --upgrade archivebox
# or with the optional auto-installer script
curl -sSL 'https://get.archivebox.io' | sh

archivebox init        # run init to upgrade the collection to the latest version

archivebox update --index-only  # optionally force an update of the snapshot index files (normally done lazily, see issue #962 for more info)

archivebox status      # check that everything succeeded
```

More info:
- https://github.com/ArchiveBox/ArchiveBox#-package-manager-setup
- https://github.com/ArchiveBox/ArchiveBox/wiki/Install#manual-setup
- https://github.com/ArchiveBox/pip-archivebox
- https://github.com/ArchiveBox/homebrew-archivebox
- https://github.com/ArchiveBox/docker-archivebox
- https://github.com/ArchiveBox/debian-archivebox
- https://github.com/ArchiveBox/electron-archivebox
- https://aur.archlinux.org/packages/archivebox
- https://github.com/NixOS/nixpkgs/blob/master/pkgs/applications/misc/archivebox/default.nix

<hr/>

## Merge two or more existing archives

See [[Merging Collections]]...

<br/>

<hr/>

## Related Documents

- https://github.com/ArchiveBox/ArchiveBox/wiki/Troubleshooting#database
- https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#disk-layout
- https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#large-archives
- https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview#output-folder
- https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#python-shell-usage
- https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#sql-shell-usage
