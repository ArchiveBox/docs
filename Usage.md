# Usage

▶️ _Make sure the dependencies are [fully installed](https://github.com/ArchiveBox/ArchiveBox/wiki/Install) before running any ArchiveBox commands._

**ArchiveBox API Reference:**

<img src="https://imgur.zervice.io/aQZZcku.png" width="20%" align="right"/>

- [CLI Usage](#CLI-Usage): Docs and examples for the ArchiveBox command line interface.
- [Admin UI Usage](#UI-Usage): Docs and screenshots for the outputted HTML archive interface.
- [Browser Extension Usage](#Browser-Extension-Usage): Docs and screenshots for the outputted HTML archive interface.
- [Disk Layout](#Disk-Layout): Description of the archive folder structure and contents.

**Related:**

- [[Docker]]: Learn about ArchiveBox usage with Docker and Docker Compose
- [[Configuration]]: Learn about the various archive method options
- [[Scheduled Archiving]]: Learn how to set up automatic daily archiving
- [[Publishing Your Archive]]: Learn how to host your archive for others to access
- [[Troubleshooting]]: Resources if you encounter any problems

## CLI Usage

<img src="https://imgur.zervice.io/biVfFYr.png" width="30%" align="right"/>

All three of these ways of running ArchiveBox are equivalent and interchangeable:

- `archivebox [subcommand] [...args]`  
  *Using the PyPI package via `pip install archivebox`*
- `docker run ... archivebox/archivebox [subcommand] [...args]`  
  *Using the official Docker image*
- `docker-compose run archivebox [subcommand] [...args]`  
  *Using the official Docker image w/ Docker Compose*

You can share a single archivebox data directory between Docker and non-Docker instances as well, allowing you to run the server in a container but still execute CLI commands on the host for example.

For more examples see the [[Docker]] page.

- [Run ArchiveBox with configuration options](#Run-ArchiveBox-with-configuration-options)
- [Import a single URL](#Import-a-single-URL)
- [Import a list of URLs from a text file](#Import-a-list-of-URLs-from-a-text-file)
- [Import list of links from browser history](#Import-list-of-links-from-browser-history)

---

### Run ArchiveBox with configuration options

You can set environment variables in your shell profile, a config file, or by using the `env` command.

```bash
# set config via the CLI
archivebox config --set MEDIA_MAX_SIZE=750mb

# OR modify the config file directly
echo 'MEDIA_MAX_SIZE=750mb' >> ArchiveBox.conf

# OR use environment variables
env MEDIA_MAX_SIZE=750mb archivebox add 'https://example.com'
```

See [[Configuration]] page for more details about the available options and ways to pass config.  
If you're using Docker, also make sure to read the Configuration section on the [[Docker]] page.

> [!TIP]  
> You can run archivebox outside a data directory using:  
> `env chdir=/path/to/archivebox/data archivebox [subcommand] [args...]`

---

### Import a single URL

```bash
archivebox add 'https://example.com'
# OR
echo 'https://example.com' | archivebox add
```

You can also add `--depth=1` to any of these commands if you want to recursively archive the URLs and all URLs one hop away. (e.g. all the outlinks on a page + the page).

### Import a list of URLs from a text file

```bash
cat urls_to_archive.txt | archivebox add
# OR
archivebox add < urls_to_archive.txt
# OR
curl 'https://example.com/some/rss/feed.xml' | archivebox add
# OR
archivebox add --depth=1 'https://example.com/some/rss/feed.xml'
```

You can also pipe in RSS, XML, Netscape, or any of the other [supported import formats](https://github.com/ArchiveBox/ArchiveBox/wiki/Quickstart#2-get-your-list-of-urls-to-archive) via stdin.

```bash
archivebox add < ~/Downloads/browser_bookmarks_export.html
# OR
archivebox add < ~/Downloads/pinboard_bookmarks.json
# OR
archivebox add < ~/Downloads/any_text_containing_urls.txt
```

---

### Import list of links from browser history

Look in the `bin/` folder of this repo to find a script to parse your browser's SQLite history database for URLs.
Specify the type of the browser as the first argument, and optionally the path to the SQLite history file as the second argument.

```bash
./bin/export-browser-history --chrome
archivebox add < output/sources/chrome_history.json
# or
./bin/export-browser-history --firefox
archivebox add < output/sources/firefox_history.json
# or
./bin/export-browser-history --safari
archivebox add < output/sources/safari_history.json
```

---

## UI Usage

```bash
# configure which areas you want to require login to use vs make publicly available
archivebox config --set PUBLIC_INDEX=False
archivebox config --set PUBLIC_SNAPSHOTS=False
archivebox config --set PUBLIC_ADD_VIEW=False

archivebox manage createsuperuser  # set an admin password to use for any areas requiring login
archivebox server 0.0.0.0:8000     # start the archivebox web server

open http://127.0.0.1:8000         # open the admin UI in a browser to view your archive
```

*See the [Configuration Wiki](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#public_index--public_snapshots--public_add_view) and [Security Wiki](https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview#archiving-private-content) for more info...*

Or if you prefer to generate a [static HTML index](https://github.com/ArchiveBox/ArchiveBox#static-archive-exporting) instead of using the built-in web server, you can run `archivebox list --html --with-headers > ./index.html` and then open `./index.html` in a browser.  You should see something [like this](https://demo.archivebox.io).

You can sort by column, search using the box in the upper right, and see the total number of links at the bottom.

Click the Favicon under the "Files" column to go to the details page for each link.

<div align="center">
<img src="https://imgur.zervice.io/52RjhUM.png" width="45%"/>
<img src="https://imgur.zervice.io/Gg9sTyq.png" width="45%"/>
</div>

### Explanation of buttons in the web UI - admin snapshots list

<img src="https://imgur.zervice.io/4Sa76Ek.png" alt="Screenshot of buttons at top of Snapshot admin page"/>

A logged-in admin user may perform these operations on one or more snapshots:

- <kbd>Search</kbd> Search text in the Snapshot title, URL, tags, or archived content (supports regex with the default ripgrep search backend, or enable the [Sonic](https://github.com/ArchiveBox/ArchiveBox/blob/dev/docker-compose.yml#L35) full-text search backend in `docker-compose.yml` and set `SEARCH_BACKEND_ENGINE=sonic`, `SEARCH_BACKEND_HOST`, `SEARCH_BACKEND_PASSWORD` for full-text fuzzy searching) https://github.com/ArchiveBox/ArchiveBox/issues/956
- Tags - tag or un-tag snapshots
- <kbd>Title</kbd> Pull the title ( redownload if it was missing, or the title has changed )
- <kbd>Pull</kbd> Download missing/failed outputs/extractors methods ( pdf, wget... etc). Maybe because download failed or interrupted by a reboot or something. This is the default behavior when you add new URL, they will get pulled automatically. https://github.com/ArchiveBox/ArchiveBox#output-formats
- <kbd>Re-Snapshot</kbd> As the name suggests, re-download the page as a separated unique page. Not the same as pull, this one will create a separate entry, and the page is treated as a new URL ending with the date and time #2020-10-24-08:00 https://github.com/ArchiveBox/ArchiveBox#saving-multiple-snapshots-of-a-single-url
- <kbd>Reset</kbd> Delete all type of output and redownload them. In the contrary of snapshot, this will overwrite the files.
- <kbd>Delete</kbd> Delete a snapshot entirely. This action cannot be undone.

## Browser Extension Usage

Get the official [ArchiveBox Browser Extension](https://github.com/ArchiveBox/archivebox-browser-extension):

1. Set your Add page to allow non-logged-in access `archivebox config --set PUBLIC_ADD_VIEW=True`  
  (see [`PUBLIC_ADD_VIEW` in the wiki](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#public_index--public_snapshots--public_add_view))
2. Install the extension in your browser:
- [Chrome/Edge/Other Chromium](https://chrome.google.com/webstore/detail/habonpimjphpdnmcfkaockjnffodikoj)
- [Firefox](https://addons.mozilla.org/en-US/firefox/addon/archivebox-exporter/)
3. Set the `BASE_URL` in the extension to your ArchiveBox server's URL, e.g. `https://archivebox.example.com:3000`
4. Test it by archiving some pages from your browser and checking `data/logs/*` and `https://archivebox.example.com:3000/admin/core/archiveresult/`

<img width="400" align="top" alt="chrome web store screenshot" src="https://user-images.githubusercontent.com/511499/215699375-5c98c9bb-56fd-4a46-a990-e5745d46019c.png"/><img width="400" align="top" alt="browser extension config screen" src="https://user-images.githubusercontent.com/511499/215702958-4683af8f-7f1e-4b0e-a313-2466b9cf0276.png"/>

See https://github.com/ArchiveBox/ArchiveBox/issues/577 for more information.

## Disk Layout

The `OUTPUT_DIR` folder (usually whatever folder you run the `archivebox` command in), contains the UI HTML and archived data with the structure outlined below.

```yaml
 - data/
   - index.sqlite3        # Main index of all archived URLs
   - ArchiveBox.conf      # Main config file in ini format

   - archive/
      - 155243135/        # Archived links are stored in folders by timestamp
         - index.json     # Index/details page for individual archived link
         - index.html

         # Archive method outputs:
         - warc/
         - media/
         - git/
         ...

   - sources/             # Each imported URL list is saved as a copy here
      - getpocket.com-1552432264.txt
      - stdin-1552291774.txt
      ...
```

For more info about ArchiveBox's database/filesystem layout and troubleshooting steps:
- https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview#output-folder
- https://github.com/ArchiveBox/ArchiveBox/wiki/Upgrading-or-Merging-Archives
- https://github.com/ArchiveBox/ArchiveBox/wiki/Upgrading-or-Merging-Archives#modify-the-archivebox-sqlite3-db-directly
- https://github.com/ArchiveBox/ArchiveBox/wiki/Upgrading-or-Merging-Archives#database-troubleshooting

### Large Archives

I've found it takes about an hour to download 1000 articles, and they'll take up roughly 1GB.  
Those numbers are from running it single-threaded on my i5 machine with 50mbps down. YMMV.

Storage requirements go up immensely if you're using `FETCH_MEDIA=True` and are archiving many pages with audio & video.

You can try to run it in parallel by manually splitting your URLs into separate chunks (though this may not work with `database locked` errors on slower filesystems):
```bash
archivebox add < urls_chunk_1.txt &
archivebox add < urls_chunk_2.txt &
archivebox add < urls_chunk_3.txt &
```
(though this may not be faster if you have a very large collection/main index)

Users have reported running it with 50k+ bookmarks with success (though it will take more RAM while running).

If you already imported a huge list of bookmarks and want to import only new
bookmarks, you can use the `ONLY_NEW` environment variable. This is useful if
you want to import a bookmark dump periodically and want to skip broken links
which are already in the index.

For more info about troubleshooting filesystem permissions, performance, or issues when running on a NAS:
- https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview#output-folder
- https://github.com/ArchiveBox/ArchiveBox/wiki/Upgrading-or-Merging-Archives#database-troubleshooting

## SQL Shell Usage

Explore the SQLite3 DB a bit to see whats available using the SQLite3 shell:
```bash
cd ~/archivebox
sqlite3 index.sqlite3

# example usage:
SELECT * FROM snapshot;
UPDATE auth_user SET email = 'someNewEmail@example.com' WHERE username = 'someUsernameHere';
...
```

More info:
- https://github.com/ArchiveBox/ArchiveBox#-sqlpythonfilesystem-usage
- https://github.com/ArchiveBox/ArchiveBox/wiki/Upgrading-or-Merging-Archives#modify-the-archivebox-sqlite3-db-directly
- https://github.com/ArchiveBox/ArchiveBox/wiki/Upgrading-or-Merging-Archives#database-troubleshooting
- https://stackoverflow.com/questions/1074212/how-can-i-see-the-raw-sql-queries-django-is-running

## Python Shell Usage

Explore the Python API a bit to see whats available using the archivebox shell:

**Python API Documentation:** https://docs.archivebox.io/en/master/archivebox.html#module-archivebox.main

```bash
$ archivebox shell
[i] [2020-09-17 16:57:07] ArchiveBox v0.4.21: archivebox shell
    > /Users/squash/Documents/opt/ArchiveBox/data

# Shell Plus Model Imports
from core.models import Snapshot
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When
from django.utils import timezone
from django.urls import reverse
from django.db.models import Exists, OuterRef, Subquery
# ArchiveBox Imports
from archivebox.core.models import Snapshot, User
from archivebox import *
    help
    version
    init
    config
    add
    remove
    update
    list
    shell
    server
    status
    manage
    oneshot
    schedule

[i] Welcome to the ArchiveBox Shell!
    https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#Shell-Usage
    https://docs.archivebox.io/en/master/archivebox.html#module-archivebox.main

    Hint: Example use:
        print(Snapshot.objects.filter(is_archived=True).count())
        Snapshot.objects.get(url="https://example.com").as_json()
        add("https://example.com/some/new/url")

# run Python API queries/function calls directly
>>> print(Snapshot.objects.filter(is_archived=True).count())
24

# get help info on an object or function
>>> help(Snapshot)
...

# show raw SQL queries run
>>> from django.db import connection
>>> print(connection.queries)
```

For more info and example usage:
- https://github.com/ArchiveBox/ArchiveBox/wiki/Upgrading-or-Merging-Archives#example-adding-a-new-user-with-a-hashed-password
- https://github.com/ArchiveBox/ArchiveBox/blob/dev/archivebox/main.py
- https://github.com/ArchiveBox/ArchiveBox/blob/dev/archivebox/config.py
- https://github.com/ArchiveBox/ArchiveBox/blob/dev/archivebox/core/models.py
- https://stackoverflow.com/questions/1074212/how-can-i-see-the-raw-sql-queries-django-is-running


## Python API Usage

You can interact with ArchiveBox as a Python library from external scripts or programs.

This API is a *local* API, designed to be used on the same machine as the ArchiveBox collection.

For example you could create and a script `add_archivebox_url.py` like so:
```python
import os
DATA_DIR = '~/archivebox/data'
os.chdir(DATA_DIR)

# you must import and setup django first to establish a DB connection
from archivebox.config import setup_django
setup_django()

# then you can import all the main functions
from archivebox.main import add, remove, server

add('https://example.com', index_only=True, out_dir=DATA_DIR)
remove(...)
server(...)
...
```

For more information see:
- [ArchiveBox Python API Reference (ReadTheDocs)](https://docs.archivebox.io/en/latest/archivebox.html)
- [ArchiveBox Developer Documentation](https://github.com/ArchiveBox/ArchiveBox#archivebox-development)
- [ArchiveBox Python source code](https://github.com/ArchiveBox/ArchiveBox/blob/dev/archivebox/)
