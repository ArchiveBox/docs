# Usage

▶️ _Make sure the dependencies are [fully installed](https://github.com/ArchiveBox/ArchiveBox/wiki/Install) before running any ArchiveBox commands._

**ArchiveBox API Reference:**

<img src="https://i.imgur.com/aQZZcku.png" width="20%" align="right"/>

- [CLI Usage](#CLI-Usage): Docs and examples for the ArchiveBox command line interface.
- [UI Usage](#UI-Usage): Docs and screenshots for the outputted HTML archive interface.
- [Disk Layout](#Disk-Layout): Description of the archive folder structure and contents.

**Related:**

- [[Docker]]: Learn about ArchiveBox usage with Docker and Docker Compose
- [[Configuration]]: Learn about the various archive method options
- [[Scheduled Archiving]]: Learn how to set up automatic daily archiving
- [[Publishing Your Archive]]: Learn how to host your archive for others to access
- [[Troubleshooting]]: Resources if you encounter any problems

## CLI Usage

<img src="https://i.imgur.com/biVfFYr.png" width="30%" align="right">

All three of these ways of running ArchiveBox are equivalent and interchangeable:

- `archivebox [subcommand] [...args]`  
  *Using the PyPI package via `pip install archivebox`*
- `archivebox run -it -v $PWD:/data archivebox/archivebox [subcommand] [...args]`  
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
# via the CLI
archivebox config --set TIMEOUT=3600

# by modifying the config file
nano ArchiveBox.conf
# TIMEOUT=3600

# or by using environment variables
env TIMEOUT=3600 archivebox add 'https://example.com'
```

See [[Configuration]] page for more details about the available options and ways to pass config.  
If you're using Docker, also make sure to read the Configuration section on the [[Docker]] page.

---

### Import a single URL

```bash
archivebox add 'https://example.com'
# or
echo 'https://example.com' | archivebox add
```

You can also add `--depth=1` to any of these commands if you want to recursively archive the URLs and all URLs one hop away. (e.g. all the outlinks on a page + the page).

### Import a list of URLs from a text file

```bash
cat urls_to_archive.txt | archivebox add
# or
archivebox add < urls_to_archive.txt
# or
curl https://getpocket.com/users/USERNAME/feed/all | archivebox add
```

You can also pipe in RSS, XML, Netscape, or any of the other supported import formats via stdin.

```bash
archivebox add < ~/Downloads/browser_bookmarks_export.html
# or
archivebox add < ~/Downloads/pinboard_bookmarks.json
# or
archivebox add < ~/Downloads/other_links.txt
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
archivebox server
open http://127.0.0.1:8000
```

Or if you prefer to use the static HTML UI instead of the interactive UI provided by the server,
you can open `./index.html` in a browser.  You should see something [like this](https://archive.sweeting.me).

You can sort by column, search using the box in the upper right, and see the total number of links at the bottom.

Click the Favicon under the "Files" column to go to the details page for each link.

<div align="center">
<img src="https://i.imgur.com/52RjhUM.png" width="45%">
<img src="https://i.imgur.com/Gg9sTyq.png" width="45%">
</div>

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

### Large Archives

I've found it takes about an hour to download 1000 articles, and they'll take up roughly 1GB.  
Those numbers are from running it single-threaded on my i5 machine with 50mbps down. YMMV.

Storage requirements go up immensely if you're using `FETCH_MEDIA=True` and are archiving many pages with audio & video.

You can run it in parallel by manually splitting your URLs into separate chunks:
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

## Python Shell Usage

Explore the Python API a bit to see whats available using the archivebox shell:
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

    Hint: Example use:
        print(Snapshot.objects.filter(is_archived=True).count())
        Snapshot.objects.get(url="https://example.com").as_json()
        add("https://example.com/some/new/url")
```

## Python API Usage

```python
import os
DATA_DIR = '~/some/path/containing/your/archivebox/data'
os.chdir(DATA_DIR)


from archivebox.main import check_data_folder, setup_django, add, remove, server

check_data_folder(DATA_DIR)
setup_django(DATA_DIR)

add('https://example.com', index_only=True, out_dir=DATA_DIR)
remove(...)
server(...)
...
```

For more information see the [Python API Reference](https://docs.archivebox.io/en/latest/archivebox.html).
