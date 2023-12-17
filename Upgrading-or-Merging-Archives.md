## Upgrade your ArchiveBox collection to a new version


*Note: It's recommended to only upgrade one major version at a time. e.g. if you're on `v0.4.14`, upgrade to `v0.5.6` next, then `v0.6.3`, and finally `v0.7.1` (as 3 separate steps).
You can specify exact versions with pip like so: `pip install archivebox==0.6.3` or with docker `docker pull archivebox/archivebox:0.6.3`. Upgrading directly across multiple major versions may work in some cases, but is not recommended for maximum data safety.*

**✅ Upgrading checklist:**

1. Find the version you want to upgrade to on https://github.com/ArchiveBox/ArchiveBox/releases
2. **Read the release notes carefully** for any instructions or extra steps around upgrading for each release you're skipping or installing
3. **Make a full backup** of your `index.sqlite3` and `archive/` content before upgrading!  
`gzip -9 < index.sqlite3 > "index.sqlite3.$(date +%s).bak"`
4. Follow the steps below depending on your setup to run `archivebox init` (repeating as necessary for each major version if upgrading across multiple major versions)
5. Confirm the upgrade succeeded and check for any orphan/corrupted snapshots with `archivebox status`

💬 [Open an issue](https://github.com/ArchiveBox/ArchiveBox/issues/new/choose) in our bug tracker if you experience any problems with upgrading/merging/modifying collections.

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
cd ~/archivebox        # or wherever your data folder is
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
docker run -v $PWD:/data -it archivebox/archivebox init --setup  # upgrade the collection to the latest version

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
cd ~/archivebox        # or wherever your data folder is
killall archivebox     # stop the currently running archivebox version

# upgrade ArchiveBox using the package manager you originally used to install it
pip install --upgrade archivebox
# or
brew upgrade archivebox
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

2. Create a new empty archivebox collection in a new folder somewhere, this will hold the new merged collection
  ```bash
  mkdir /path/to/archivebox_new
  cd /path/to/archivebox_new
  archivebox init --setup
  ```

3. Copy everything under `./archive/*` in each old collection into the new collection's `./archive/` folder
  ```bash
  rsync --archive --info=progress2 /path/to/archivebox1/data/archive/ /path/to/archivebox_new/data/archive
  rsync --archive --info=progress2 /path/to/archivebox2/data/archive/ /path/to/archivebox_new/data/archive
  # ...repeat the same for each collection if merging more than two
  ```

4. Run `archivebox init` in the new merged collection to regenerate the new index
  ```bash
  cd /path/to/archivebox_new
  archivebox init --setup
  ```

5. The new collection should now contain all the entries from the old collections combined
  ```bash
  cd /path/to/archivebox_new
  archivebox status

  # optionally force an update of the snapshot index files (normally done lazily)
  archivebox update --index-only
  ```
  For more information about why Snapshot index files are usually updated lazily, see: https://github.com/ArchiveBox/ArchiveBox/issues/962

After you've confirmed your Snapshots are present in the new index, the old `index.sqlite3`, `index.json`, `index.html`, etc. main index files from the old archives can be safely deleted. You can optionally merge the contents of `ArchiveBox.conf` (your ArchiveBox config options), `sources/` (copies of all URLs imported in their original format), `logs/` (ArchiveBox error logs and debug info), and other root-level items yourself if that data is important to you.

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

*Note: this is just an example to demonstrate direct database usage. If you are trying to create a user on initial setup, use the [`ADMIN_USERNAME` & `ADMIN_PASSWORD`](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#admin_username--admin_password) configuration options.*

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

More info:
- https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#python-shell-usage
- https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#sql-shell-usage

---

## Database Troubleshooting

Database and filesystem issues are uncommon but do come up from time to time (especially when using networked storage, large archives, or multiple ArchiveBox processes for a single collection).  

*ℹ️ Generally, these commands can help you resolve most issues:*
```bash
archivebox init                 # upgrade the archivebox collection
archivebox init --setup         # upgrade the archivebox collection and all dependencies
archivebox update --index-only  # force an upgrade of some of the archivebox index/collection files
archivebox server --debug       # run the server with more verbose debug log output
archivebox shell                # access the Python API / Django management shell
sqlite3 index.sqlite3           # access the SQLite3 SQL database shell
```

Don't be scared by the volume of content here. Almost all of these issues linked below are duplicates or old resolved bugs, but they contain valuable context and troubleshooting steps if you're trying to figure out the cause of a problem with your setup.

#### Filesystem doesn't support FSYNC (e.g. network mounts)

The `index.sqlite3` file must be stored on a filesystem that supports FSYNC (most local filesystems) in order to ensure SQLite3 database integrity when multiple ArchiveBox processes may be accessing it simultaneously. However, the `./archive` folder can be on a NAS or other filesystem that does not support FSYNC.

- [Archivebox hangs when initializing collection on network drive that doesn't support FSYNC #742](https://github.com/ArchiveBox/ArchiveBox/issues/742)
- [Question: How to run AB on localhost but store data on NAS? #894](https://github.com/ArchiveBox/ArchiveBox/issues/894)
- [Question: Docker on Windows archiving to an SMB path that doesn't support FSYNC #722](https://github.com/ArchiveBox/ArchiveBox/issues/722)
- [Support for network drives or filesystems that don't implement FSYNC #456](https://github.com/ArchiveBox/ArchiveBox/issues/456)

More info:
- https://www.geeksforgeeks.org/python-os-fsync-method/
- https://man7.org/linux/man-pages/man2/fdatasync.2.html
- https://www.samba.org/samba/docs/current/man-html/smb.conf.5.html
- https://eclecticlight.co/2022/02/18/how-can-you-trust-a-disk-to-write-data/

#### Database and filesystem contention issues when running multiple ArchiveBox processes

ArchiveBox can sometimes struggle when archiving many links in parallel with multiple ArchiveBox processes trying to write to the database at the same time, leading to errors like this:
```bash
Unable to create the django_migrations table (database is locked)
```

These errors can also be encountered when there are permissions, network, or filesystem issues preventing writes to the `index.sqlite3` file.

- [Question: Unable to create the django_migrations table (database is locked) - When OUTPUT_DIR to SAMBA share #946](https://github.com/ArchiveBox/ArchiveBox/issues/946)
- [Question: ...Unable to create the django_migrations table (database is locked) #880](https://github.com/ArchiveBox/ArchiveBox/issues/880)
- [Database is locked and other weird behavior when doing simultaneous adds #781](https://github.com/ArchiveBox/ArchiveBox/issues/781)
- [Bugfix: Retry on "database locked" error (or add support for PostgreSQL/MySQL DB backend) #601](https://github.com/ArchiveBox/ArchiveBox/issues/601)
- [Architecture: Use multiple cores to run link archiving in parallel #91](https://github.com/ArchiveBox/ArchiveBox/issues/91)
- [ArchiveBox index corruption when running multiple import processes on v0.5.0 #454](https://github.com/ArchiveBox/ArchiveBox/issues/454)
- [Architecture: Concurrent runs accidentally delete each other's temp files, leaving the index broken #234](https://github.com/ArchiveBox/ArchiveBox/issues/234)
- [Database is locked and other weird behavior when doing simultaneous adds #781](https://github.com/ArchiveBox/ArchiveBox/issues/781)
- [Bugfix: Retry on "database locked" error (or add support for PostgreSQL/MySQL DB backend) #601](https://github.com/ArchiveBox/ArchiveBox/issues/601)

More info:
- https://www.sqlite.org/lockingv3.html
- https://charlesleifer.com/blog/going-fast-with-sqlite-and-python/
- https://victoria.dev/blog/sqlite-in-production-with-wal/
- https://code.djangoproject.com/ticket/29280
- https://stackoverflow.com/questions/47761570/how-can-i-avoid-database-is-locked-sqlite3-errors-in-django

#### Database migrations errors or upgrade issues

Migration or upgrade issues happen occasionally with some niche setups or when skipping major versions during archiving.  
Always backup your archive before upgrading, but know that migrations are deterministic and atomic using Django's migration system, so a failed migration does not mean your archive is unrecoverable, you just have to downgrade to the previous stable major version then continue upgrading.

```bash
archivebox init  # this usually applies any necesary migrations (atomically and indempotently, safe to run multiple times)
```

- [Bug: NOT NULL constraint failed: core_archiveresult.output when upgrading v0.4.24 archive to v0.6 #705](https://github.com/ArchiveBox/ArchiveBox/issues/705)
- [Bugfix: sqlite3.IntegrityError: NOT NULL constraint failed: core_archiveresult.cmd_version and .output #597](https://github.com/ArchiveBox/ArchiveBox/issues/597)
- [Error: django.db.utils.IntegrityError: UNIQUE constraint failed: core_tag.slug  #596](https://github.com/ArchiveBox/ArchiveBox/issues/596)
- [Bugfix: django.db.utils.IntegrityError: UNIQUE constraint failed: core_snapshot.timestamp #412](https://github.com/ArchiveBox/ArchiveBox/issues/412)
- [Best Practices for Backup/Restore #341](https://github.com/ArchiveBox/ArchiveBox/issues/341)
- [Bug: Running archivebox update --index-only doesn't upgrade Snapshot index.{html,json} files #962](https://github.com/ArchiveBox/ArchiveBox/issues/962)
- [Feature Request: Deduplicate files on archives #704](https://github.com/ArchiveBox/ArchiveBox/issues/704)

More info:
- https://docs.djangoproject.com/en/4.0/topics/migrations/
- https://realpython.com/django-migrations-a-primer/
- https://realpython.com/digging-deeper-into-migrations/
- https://www.kite.com/blog/python/django-database-migrations-overview/
- https://markusholtermann.eu/2021/06/writing-safe-database-migrations-in-django/


#### Repairing a corrupted SQLite3 database file

A corrupted database file can theoretically only happen if an external process or filesystem error corrupts the SQLite3 database (there has only been [one report](https://github.com/ArchiveBox/ArchiveBox/issues/955) of a user encountering this in real life). If you ever need to repair a corrupted ArchiveBox index you can run the following steps.

Note this is specific to this error, these steps do not apply to other migrations/db errors (see below for other issues):
```bash
sqlite3.DatabaseError: database disk image is malformed    
```

Generally all index issues should be fixable by running `archivebox init`.  
You can see the status of Snapshots and find any invalid/orphan/missing snapshots with `archivebox status`.

**Error output:**

```python3
[i] [2022-03-24 20:37:27] ArchiveBox v0.6.2: archivebox init                                                                                                                                  
    > /data                                                                                                                                                                                   
                                                                                                                                                                                              
[^] Verifying and updating existing ArchiveBox collection to v0.6.2...                                                                                                                        
----------------------------------------------------------------------                                                                                                                        
                                                                                                                                                                                              
[*] Verifying archive folder structure...                                                                                                                                                     
    + ./archive, ./sources, ./logs...                                                                                                                                                         
    + ./ArchiveBox.conf...                                                                                                                                                                    
                                                                                                                                                                                              
[*] Verifying main SQL index and running any migrations needed...                                                                                                                             
Traceback (most recent call last):                                                                                                                                                            
  File "/usr/local/lib/python3.9/site-packages/django/db/backends/utils.py", line 82, in _execute                                                                                             
    return self.cursor.execute(sql)                                                                                                                                                           
  File "/usr/local/lib/python3.9/site-packages/django/db/backends/sqlite3/base.py", line 411, in execute                                                                                      
    return Database.Cursor.execute(self, query)                                                                                                                                               
sqlite3.DatabaseError: database disk image is malformed    
```

**Steps to fix:**

```bash
cd ~/archivebox
echo '.dump' | sqlite3 index.sqlite3 | sqlite3 repaired_index.sqlite3
mv index.sqlite3 corrupt_index.sqlite3
mv repaired_index.sqlite3 index.sqlite3
```

More info:
- https://github.com/ArchiveBox/ArchiveBox/issues/955
- https://stackoverflow.com/questions/5274202/sqlite3-database-or-disk-is-full-the-database-disk-image-is-malformed


---

## Related Documents

- https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#disk-layout
- https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#large-archives
- https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview#output-folder
- https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#python-shell-usage
- https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#sql-shell-usage