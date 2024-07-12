## Merging two or more existing archives

Two or more existing ArchiveBox collection dirs can be merged together by simply combining the contents of `archive/*` and re-running `archivebox init` to pull the new Snapshots into the index.

> [!WARNING]
> Snapshot folders are identified by their timestamp (in milliseconds), this is normally not a problem for archives collected on one machine, but when merging archives from two different instances that ran at the same time it means there is a small chance of conflicts. Check the contents of `archive/` before merging, and backup any directories that may conflict before proceeding.

1. Upgrade both old collections to the most recent ArchiveBox version (following instructions above)
  ```bash
  pip install --upgrade archivebox   # or follow instructions above for upgrading w/ Docker

  cd /path/to/archivebox1/data
  archivebox init
  archivebox status

  cd /path/to/archivebox2/data
  archivebox init
  archivebox status

  # ... repeat the same for each collection if merging more than two
  ```

2. Create a new empty archivebox collection in a new folder somewhere, this will hold the new merged collection
  ```bash
  mkdir /path/to/archivebox_new
  cd /path/to/archivebox_new
  archivebox init
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
  archivebox init
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
cd ~/archivebox/data    # cd into your archivebox collection dir
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
cd ~/archivebox/data    # cd into your archivebox collection dir
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

These errors can also be encountered when there are permissions, network, or filesystem issues preventing writes to `index.sqlite3`.

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
cd ~/archivebox/data
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