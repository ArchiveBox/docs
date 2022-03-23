## Upgrade your ArchiveBox collection to a new version

*Note: It's recommended to only upgrade one major version at a time. e.g. if you're on `v0.4.14`, upgrade to `v0.4.2`, then to `v0.5.6` (the latest available minor version for each major version), then from there to `v0.6.3`, not straight from `v0.4.14` -> `v0.6.3`.
You can specify exact versions with pip like so: `pip install archivebox==0.6.3` or with docker `docker pull archivebox/archivebox:0.6.3`. Upgrading directly across multiple major versions may work in some cases, but is not recommended for maximum data safety.*

**✅ Upgrading checklist:**

1. Find the version you want to upgrade to on https://github.com/ArchiveBox/ArchiveBox/releases
2. **Read the release notes carefully** for any instructions or extra steps around upgrading for each release you're skipping or installing
3. **Make a full backup** of your `index.sqlite3` and `archive/` content before upgrading!  
`gzip -9 < index.sqlite3 > "index.sqlite3.$(date +%s).bak"`
4. Follow the steps below depending on your setup to run `archivebox init` (repeating as necessary for each major version if upgrading across multiple major versions)
5. Confirm the upgrade succeeded and check for any orphan/corrupted snapshots with `archivebox status`

**ℹ️ How it works internally:**

The same command is used for initializing a new archive and upgrading an existing one. `archivebox init` is indempotent and safely be run multiple times. Running it will ensure your collection is on the latest version and all the files are in their correct locations. `archivebox status` can be used to check for orphan/corrupted snapshots or invalid index data.

There are three main areas on disk that ArchiveBox modifies during upgrades:
- `index.sqlite3` contains the SQLite3 DB index that gets upgraded automatically by Django based on the changes in [`archivebox/core/models.py`](https://github.com/ArchiveBox/ArchiveBox/blob/dev/archivebox/core/models.py).
- `archive/*/index.json` these files are redundant json exports of the data for each Snapshot in `index.sqlite3`, these files are overwritten on every `archivebox update` run or anytime the Snapshot is modified from the GUI or CLI. These files will be lazily updated to the latest schema versions as ArchiveBox accesses them, but are usually not modified in bulk during `archivebox init` when upgrading.
- `archive/*` the Snapshot output files may be moved or renamed by future upgrades (so far they have remained unchanged since v0.1, but future versions reserve the right to change their locations)

The `ArchiveBox.conf` file is not modified by upgrades and should remain forward-compatible across future versions (even when config options are renamed, we check the old names internally to maintain compatibility).

As of v0.4 and above, ArchiveBox uses the Django migrations system for deterministic, atomic, safe upgrades, so your DB should always be left in a consistent state in the event of a failure or power outage. If you need help fixing a corrupted collection, open an issue using the link below.

💬 [Open an issue](https://github.com/ArchiveBox/ArchiveBox/issues/new/choose) in our bug tracker if you experience any problems with upgrading/merging/modifying collections.

### Upgrading with Docker Compose

```bash
cd ~/archivebox        # or wherever your data folder is
docker-compose down    # stop the currently running archivebox containers
docker-compose down    # run twice to clear stopped containers
docker-compose pull    # pull the latest image version from Docker Hub
docker-compose up      # collection will be automatically upgraded as it starts
```

### Upgrading with plain Docker

```bash
docker ps -a -q  --filter ancestor=archivebox/archivebox  # find any currently running archivebox containers
docker kill <image>    # stop any currently running archivebox versions

docker pull archivebox/archivebox
docker run -v $PWD:/data -it archivebox/archivebox init --setup  # upgrade the collection to the latest version
# restart archivebox server container if needed
docker run -v $PWD:/data -it -p 8000:8000 archivebox/archivebox server
```

### Upgrading with a package manager

```bash
cd ~/archivebox        # or wherever your data folder is
killall archivebox     # stop the currently running archivebox version

# upgrade ArchiveBox using the package manager you originally used to install it
pip install --upgrade archivebox
# or
brew upgrade archivebox
# or
apt install --upgrade archivebox
# or
curl -sSL 'https://get.archivebox.io' | sh

archivebox init        # run init to upgrade the collection to the latest version
```
*More detailed instructions here: https://github.com/ArchiveBox/ArchiveBox#-package-manager-setup*

---

## Merge two or more existing archives

Two or more existing ArchiveBox collection dirs can be merged together by simply combining the contents of `archive/*` and re-running `archivebox init` to pull the new Snapshots into the index.

1. Upgrade both old collections to the most recent ArchiveBox version (following instructions above)
  ```bash
  pip install --upgrade archivebox   # or follow instructions above for upgrading w/ Docker

  cd /path/to/archivebox1/data
  archivebox init --setup
  archivebox status

  cd /path/to/archivebox2/data
  archivebox init --setup
  archivebox status

  # ... repeat the same for each collection if merging more than two
  ```

2. Create a new empty archivebox collection in a new folder somewhere
  ```bash
  mkdir ~/archivebox_new
  cd ~/archivebox_new
  archivebox init --setup
  ```

3. Copy everything under `./archive/*` in each old collection into the new collection's `./archive/` folder
  ```bash
  rsync --archive --info=progress2 /path/to/archivebox1/data/archive/ ~/archivebox_new/archive
  rsync --archive --info=progress2 /path/to/archivebox2/data/archive/ ~/archivebox_new/archive
  # ...repeat the same for each collection if merging more than two
  ```

4. Run `archivebox init` in the new merged collection to regenerate the new index
  ```bash
  cd ~/archivebox_new
  archivebox init --setup
  ```

5. The new collection should now contain all the entries from the old collections combined
  ```bash
  cd ~/archivebox_new
  archivebox status
  ```

---

## Modify the ArchiveBox SQLite3 DB directly

If you need to automate changes to the ArchiveBox DB (for example adding a User from an Ansible script), you can modify the SQLite3 DB directly.

Note, this is often unnecessary for modifying ArchiveBox on a host that doesn't have the CLI installed, as you can also copy the `index.sqlite3` to a local machine that has it, do the modifications locally, then copy the modified db back into place on the host. (Docker/CLI/GUI/Web ArchiveBox all share the same DB schema/format)

```bash
cd ~/archivebox         # cd into your archivebox collection dir
sqlite3 index.sqlite3   # open the db with sqlite3 shell
```

#### Example: Modifying an existing user's email

```sql
UPDATE auth_user
SET email = 'someNewEmail@example.com', is_superuser = 1
WHERE username = 'someUsernameHere';
```

#### Example: Adding a new user with a hashed password

1. First, generate the hashed password in a Python shell using Django's `make_password` function.

This can be done on any machine with Python 3+, it doesn't have to have ArchiveBox installed.
  ```bash
pip3 install django==3.1.3   # install the django version used by ArchiveBox
python3                      # open any python shell with django available, doesn't have to be the archivebox shell
```
```python3
>>> from django.contrib.auth.hashers import make_password
>>> make_password('somePasswordHere', 'someSaltHere', 'pbkdf2_sha256')         # choose a password and a salt (can be anything 12 chars long)
'pbkdf2_sha256$216000$someSaltHere$styW1Uoy8SHp3zbSwGRp20C9mPjOHVjP9rl5a8/UOVE='
```
2. Use the generated hashed password to insert a new User row in the SQLite3 database directly:
  ```bash
cd ~/archivebox         # cd into your archivebox collection dir
sqlite3 index.sqlite3   # open the db with sqlite3 shell
```
```sql
INSERT INTO "auth_user" ("password", "last_login", "is_superuser", "username", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined")
VALUES ('pbkdf2_sha256$216000$someSaltHere$+2beZufc3JUXnmn0tG+2peJEBh7MjxPYmT3YfIFzEl0=', NULL, 0, 'someUsername', '', '', 'someEmail@example.com', 0, 1, '2022-03-22 23:34:02.333042')
```
  Replace the values above with the desired username, email, and password hash from python output^.

3. Log in using the new generated user to confirm it works
    https://localhost:8000/admin/login/ user: `someUsername` pass:`somePasswordHere`