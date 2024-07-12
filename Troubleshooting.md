# Troubleshooting

▶️ *If you need help or have a question, you can open an [issue](https://github.com/ArchiveBox/ArchiveBox/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc) or reach out on [Twitter](https://twitter.com/theSquashSH).*

What are you having an issue with?:

- [Installing ArchiveBox](#Installing)
- [Upgrading ArchiveBox](https://github.com/ArchiveBox/ArchiveBox/wiki/Upgrading-or-Merging-Archives)
- [Configuring ArchiveBox](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration)
- [Archiving content with ArchiveBox](#Archiving)
- [Hosting your collection publicly](#Hosting-the-Archive)
- [Database and filesystem issues](https://github.com/ArchiveBox/ArchiveBox/wiki/Upgrading-or-Merging-Archives#database-troubleshooting)

---

## Installing

If using `archivebox` without Docker, make sure you've followed the full guide in the [[Install]] instructions first.  Then check here for help depending on what component you need help with.

Then make sure `archivebox` is installed available in your `$PATH`.
```bash
apt show archivebox      # show info about the apt-installed version of archivebox
brew info archivebox     # show info about the brew-installed version of archivebox
pip show archivebox      # show info about the pip-installed version of archivebox

echo $PATH               # show the directories your system is searching for binaries
which -a archivebox      # show all installed archivebox binaries available
which archivebox         # show which archivebox binary is being called
```
**⭐️ Show the full archivebox version info + info about all installed dependencies:**
```bash
archivebox version       # shows lots of useful info about installed dependencies and more
```
(ensure the version shown is the most recent available from [Releases](https://github.com/ArchiveBox/ArchiveBox/releases))



### Python

Make sure you have at least Python 3.9 installed on your system.

```bash
python3 --version
pip --version
pip install --upgrade pip setuptools
```

If you still need help getting Python installed, [the official Python docs](https://docs.python.org/3.9/using/unix.html) are a good place to start.

### Chromium/Google Chrome

For more info, see the [[Chromium Install]] page.

ArchiveBox depends on being able to access a `chromium-browser`/`google-chrome` executable.  The executable used
defaults to `chromium-browser` but can be manually specified with the environment variable `CHROME_BINARY`:

```bash
env CHROME_BINARY=/usr/local/bin/chromium-browser archivebox add ~/Downloads/bookmarks_export.html
```

1. Test to make sure you have Chrome on your `$PATH` with:

```bash
which chromium-browser || which google-chrome
```
If no executable is displayed, follow the setup instructions to install and link one of them.

2. If a path is displayed, the next step is to check that it's runnable:

```bash
chromium-browser --version || google-chrome --version
```
If no version is displayed, try the setup instructions again, or confirm that you have permission to access chrome.

3. If a version is displayed and it's `<111`, upgrade it:

```bash
apt upgrade chromium-browser -y
# OR
brew cask upgrade chromium-browser
```

4. If a version is displayed and it's `>=111`, make sure ArchiveBox is running the right one:

```bash
env CHROME_BINARY=/path/from/step/1/chromium-browser archivebox version   # replace the path with the one you got from step 1
```


### Wget & Curl

If you're missing `wget` or `curl`, simply install them using `apt` or your package manager of choice.
See the "Manual Setup" instructions for more details.

If wget times out or randomly fails to download some sites that you have confirmed are online,
upgrade wget to the most recent version with `brew upgrade wget` or `apt upgrade wget`.  There is
a bug in versions `<=1.19.1_1` that caused wget to fail for perfectly valid sites.

### NPM Dependencies

NPM packages like `readability`, `singlefile`, etc. are auto-installed by `archivebox setup` into `data/node_modules`.

Make sure you have installed NodeJS + NPM first, here are their [official install docs](https://nodejs.org/en/download/package-manager/).

```bash
node --version         # make sure you have node >=19 installed
npm --version          # make sure you have npm installed

cd ~/archivebox/data   # go into your data directory
archivebox setup       # auto-installs all JS dependencies into ./node_modules
# equivalent to:
# curl -fsSL 'https://raw.githubusercontent.com/ArchiveBox/ArchiveBox/stable/archivebox/package.json' > package.json
# npm install

# install npm dependencies should then be present in ~/archivebox/data/node_modules/.bin
archivebox version     # show version full info to make sure they're loaded correctly
```

---

## Archiving

### No links parsed from export file

Please open an [issue](https://github.com/ArchiveBox/ArchiveBox/issues) with a description of where you got the export, and
preferrably your export file attached (you can redact the links).  We'll fix the parser to support your format.

### Lots of skipped sites

If you ran the archiver once, it wont re-download sites subsequent times, it will only download new links.
If you haven't already run it, make sure you have a working internet connection and that the parsed URLs look correct.
You can check the ArchiveBox stdout logs or the Web UI to see what links it's downloading.

If you're still having issues, try deleting or moving the `./archive` folder (back it up first!) and running `archivebox init` again.

### Lots of errors

Make sure you have all the dependencies installed and that you're able to visit the links from your browser normally.
Open an [issue](https://github.com/ArchiveBox/ArchiveBox/issues) with a description of the errors if you're still having problems.

### Lots of broken links from the index

Not all sites can be effectively archived with each method, that's why it's best to use a combination of `wget`, PDFs, and screenshots.
If it seems like more than 10-20% of sites in the archive are broken, open an [issue](https://github.com/ArchiveBox/ArchiveBox/issues)
with some of the URLs that failed to be archived and I'll investigate.

### Removing unwanted links from the index

`archivebox remove --help`

## Hosting the Archive

If you're having issues trying to host the archive via nginx, make sure you already have nginx running with SSL.
If you don't, google around, there are plenty of tutorials to help get that set up.  Open an [issue](https://github.com/ArchiveBox/ArchiveBox/issues)
if you have problem with a particular nginx config.

### Other database or filesystem issues

#### Docker Permissions issues

Try Setting `PUID` & `PGID`: https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#puid--pgid

Try using [`bindfs`](https://github.com/clecherbauer/docker-volume-bindfs) to work around issues by remapping permissions, for example to remap `uid:33 gid:33` on the host to `911:911` inside the container:
`docker-compose.yml`:
```yaml
services:
  archivebox:
    volumes:
      - archivebox-data:/data

volumes:
  archivebox-data:
    driver: lebokus/bindfs:latest
    driver_opts:
      sourcePath: "${EXTERNAL_MOUNT_PARENT}/external-parent/external/archivebox"
      map: "33/911:@33/@911"
```

<br/>

---

<br/>

## Database

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

See here for more info:

- https://github.com/ArchiveBox/ArchiveBox/wiki/Upgrading
- https://github.com/ArchiveBox/ArchiveBox/wiki/Merging-Collections
- https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#python-shell-usage
- https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#sql-shell-usage
- https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview#do-not-run-as-root
- https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview#output-folder
