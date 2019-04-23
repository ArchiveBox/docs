## Roadmap

<img src="https://i.imgur.com/es97GGV.png" width="20%" align="right"/>

▶️ *Comment here to discuss the contribution roadmap:  
[Official Roadmap Discussion](https://github.com/pirate/ArchiveBox/issues/120).*

If you feel like contributing a PR, some of these tasks are pretty easy.  Feel free to open an issue if you need help getting started in any way!

**IMPORTANT**: *Please don't work on any of these major long-term tasks without [contacting me first](https://nicksweeting.com/blog#Contact-Me), work is already in progress for many of these, and I may have to reject your PR if it doesn't align with the existing work!*

---

# Planned Specification

ArchiveBox is going to migrate towards this design spec over the next 3 months bit by bit as functionality gets implemented and refactors are released.

To see how much of this spec is scheduled / implemented / released so far, read these pull requests:
 - [v0.3.0](https://github.com/pirate/ArchiveBox/pull/197)
 - [v0.4.0](https://github.com/pirate/ArchiveBox/pull/207)

**API:**
 - [`pip install archivebox`](#-pip-install-archivebox)
 - [`archivebox version`](#-archivebox-version--version)
 - [`archivebox help`](#-archivebox-help-h--help)
 - [`archivebox init`](#-archivebox-init)
 - [`archivebox info`](#-archivebox-info)
 - [`archivebox add`](#-archivebox-add)
 - [`archivebox remove`](#-archivebox-remove)
 - [`archivebox schedule`](#-archivebox-schedule)
 - [`archivebox config`](#-archivebox-config)
 - [`archivebox update`](#-archivebox-update)
 - [`archivebox list`](#-archivebox-list)
 - [`archivebox oneshot`](#-archivebox-oneshot)
 - [`archivebox server`](#-archivebox-server)
 - [`archivebox proxy`](#-archivebox-proxy)
 - [`archivebox shell`](#-archivebox-shell)
 - [`archivebox manage`](#-archivebox-manage)
 - [`from archivebox import ...`](#api-for-normal-archivebox-usage)
 - [`from archivebox.component import ...`](#api-for-all-useful-subcomponents)

**Design:**
 - [Overview](#design)
 - [Dependencies](#dependencies)
 - [Dependencies](#dependencies)
 - [Code Layout](#code-folder-layout)
 - [Data Layout](#collection-data-folder-layout)
 - [Export Layout](#exported-folder-layout)

## CLI Usage

*Note, these ways to run ArchiveBox are all equivalent:*

 - `archivebox [subcommand] [...args]`
 - `python3 -m archivebox [subcommand] [...args]`
 - `python3 archivebox/__main__.py [subcommand] [...args]`
 - `python3 archivebox/manage.py archivebox [subcommand] [...args]`

### `$ pip install archivebox`
```bash
...
Installing collected packages: archivebox
  Running setup.py install for archivebox ... done
Successfully installed archivebox-0.4.0
```

Developers who are working on the ArchiveBox codebase should install the project in "linked" mode for development using: `pipenv install; pip install -e .`.

### `$ archivebox [version|--version]`
```bash
ArchiveBox v0.4.0

[i] Dependency versions:
 √  PYTHON_BINARY            /optArchiveBox/.venv/bin/python3.7            v3.7            valid
 √  DJANGO_BINARY            /optArchiveBox/.venv/lib/python3.7/site-packages/django/bin/django-admin.py v2.2.0          valid
 √  CURL_BINARY              /usr/bin/curl                                                          v7.54.0         valid
 √  WGET_BINARY              /usr/local/bin/wget                                                    v1.20.1         valid
 √  GIT_BINARY               /usr/local/bin/git                                                     v2.20.1         valid
 √  YOUTUBEDL_BINARY         /optArchiveBox/.venv/bin/youtube-dl           v2019.04.17     valid
 √  CHROME_BINARY            /Applications/Google Chrome.app/Contents/MacOS/Google Chrome           v74.0.3729.91   valid

[i] Folder locations:
 √  REPO_DIR                 /optArchiveBox                                28 files        valid
 √  PYTHON_DIR               /optArchiveBox/archivebox                     14 files        valid
 √  LEGACY_DIR               /optArchiveBox/archivebox/legacy              15 files        valid
 √  TEMPLATES_DIR            /optArchiveBox/archivebox/legacy/templates    7 files         valid
 √  OUTPUT_DIR               /optArchiveBox/archivebox/data                10 files        valid
 √  SOURCES_DIR              /optArchiveBox/archivebox/data/sources        1 files         valid
 √  LOGS_DIR                 /optArchiveBox/archivebox/data/logs           0 files         valid
 √  ARCHIVE_DIR              /optArchiveBox/archivebox/data/archive        2 files         valid
 √  CHROME_USER_DATA_DIR     /Users/squash/Library/Application Support/Chromium                     2 files         valid
 -  COOKIES_FILE                                                                                    -               disabled                                                                                   -               disabled
```

### `$ archivebox [help|-h|--help]`
```bash
ArchiveBox: The self-hosted internet archive.

Documentation:
    https://github.com/pirate/ArchiveBox/wiki

UI Usage:
    Open output/index.html to view your archive.

CLI Usage:
    mkdir data; cd data/
    archivebox init

    echo 'https://example.com/some/page' | archivebox add
    archivebox add https://example.com/some/other/page
    archivebox add --depth=1 ~/Downloads/bookmarks_export.html
    archivebox add --depth=1 https://example.com/feed.rss
    archivebox update --resume=15109948213.123
```

### `$ archivebox init`

Initialize a new "collection" folder, aka a complete archive containing an ArchiveBox.conf config file, an index of all the archived pages, and the archived content for each page.

```bash
$ mkdir ~/new/data/folder && cd ~/new/data/folder
$ archivebox init
[+] Initializing new archive directory: /Users/squash/Documents/Code/ArchiveBox/archivebox/data
----------------------------------------------------------------
    > /Users/squash/Documents/Code/ArchiveBox/archivebox/data/sources
    > /Users/squash/Documents/Code/ArchiveBox/archivebox/data/archive
    > /Users/squash/Documents/Code/ArchiveBox/archivebox/data/logs

[+] Running Django migrations...
    /Users/squash/Documents/Code/ArchiveBox/archivebox/data/index.sqlite3
No changes detected
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, core, sessions
Running migrations:
  ...

[*] [2019-04-23 01:53:41] Updating 0 links in main index...
    √ /Users/squash/Documents/Code/ArchiveBox/archivebox/data/index.sqlite3
    √ /Users/squash/Documents/Code/ArchiveBox/archivebox/data/index.json
    √ /Users/squash/Documents/Code/ArchiveBox/archivebox/data/index.html

----------------------------------------------------------------
[√] Done. ArchiveBox collection is set up in the current folder.
    To add new links, you can run:
        archivebox add 'https://example.com'

    For more usage and examples, run:
        archivebox help
```

### `$ archivebox info`

Print out some info and statistics about the archive collection.

```bash
$ archivebox info
*] Scanning archive collection main index with 1 links:
    /Users/squash/Documents/Code/ArchiveBox/archivebox/data
    > Index Size: 190.0KB across 6 files

[*] Scanning archive collection data directory with 1 entries:
    /Users/squash/Documents/Code/ArchiveBox/archivebox/data/archive
    > Total Size: 2.3MB across 26 files in 15 directories

    > 1 valid archive data directories (valid directories matched to links in the index)
    > 0 missing data directories (directories missing for links in the index)
    > 0 invalid data directories (directories present that don't contain an index file)
    > 0 orphaned data directories (directories present for links that don't exist in the index)
```

### `$ archivebox add`

#### `--only-new`
Controls whether to only add new links or also retry previously failed/skipped links.

#### `--mirror`
Archive an entire site (finding all linked pages below it on the same domain)

#### `--depth`
Controls how far to follow links from the given url. `0` sets it to only archive the page, and not follow any outlinks. `1` sets it to archive the page and follow one link outwards and archive those pages. `2` sets it to follow a maximum of two hops outwards, and so on...

#### `--crawler=[type]`
Controls which crawler to use in order to find outlinks in a given page. 

#### `url`
Is the page you want to archive

#### `< stdin`
URLs to be added can also be piped in via stdin instead of passed as an argument

```bash
$ archivebox add --depth=1 https://example.com
[+] [2019-03-30 18:36:41] Adding 1 new url and all pages 1 hop out: https://example.com
[*] [2019-03-30 18:36:42] Saving main index files...
    √ ./index.json
    √ ./index.html
[▶] [2019-03-30 18:36:42] Updating archive content...
[+] [2019-03-30 18:36:42] "Using Geolocation Data to Understand Consumer Behavior During Severe Weather Events"
    https://orbitalinsight.com/using-geolocation-data-understand-consumer-behavior-severe-weather-events
    > ./archive/1553789823
        > wget
        > warc
        > media
        > screenshot
[√] [2019-03-30 18:39:00] Update of 37 pages complete (2.08 sec)
    - 35 links skipped
    - 0 links updated
    - 2 links had errors
[*] [2019-03-30 18:39:00] Saving main index files...
    √ ./index.json
    √ ./index.html

    To view your archive, open:
        /Users/example/ArchiveBox/index.html
```

### `$ archivebox schedule`
Use `python-crontab` to add, remove, and edit regularly scheduled archive update jobs.

#### `--run-all`

Run all the scheduled jobs once immediately, independent of their configured schedules

#### `--foreground`

Launch ArchiveBox as a long-running foreground task instead of using cron.

#### `--show`

Print a list of currently active ArchiveBox cron jobs

#### `--clear`

Stop all ArchiveBox scheduled runs, clear it completely from cron

#### `--add`

Add a new scheduled ArchiveBox update job to cron

#### `--quiet`

Don't warn about many jobs potentially using up storage space.

#### `--every=[schedule]`

The schedule to run the command can be either: 
 - `minute`/`hour`/`day`/`week`/`month`/`year`
 - or a cron-formatted schedule like `"0/2 * * * *"`/`"* 0/10 * * * *"`/...

#### `import_path`
Specify the path as the path to a local file or remote URL to check for new links.


```bash
$ archivebox schedule --show
@hourly cd /optArchiveBox/data && /opt/ArchiveBox/.venv/bin/archivebox add "https://getpocket.com/users/nikisweeting/feed/all" 2>&1 > /opt/ArchiveBox/data/logs/archivebox.log # archivebox_schedule
```
```bash
$ archivebox schedule --add --every=hour https://getpocket.com/users/nikisweeting/feed/all

[√] Scheduled new ArchiveBox cron job for user: squash (1 jobs are active).
  > @hourly cd /Users/squash/Documents/Code/ArchiveBox/data && /Users/squash/Documents/Code/ArchiveBox/.venv/bin/archivebox add "https://getpocket.com/users/nikisweeting/feed/all" 2>&1 > /Users/squash/Documents/Code/ArchiveBox/data/logs/archivebox.log # archivebox_schedule

[!] With the current cron config, ArchiveBox is estimated to run >365 times per year.
    Congrats on being an enthusiastic internet archiver! 👌

    Make sure you have enough storage space available to hold all the data.
    Using a compressed/deduped filesystem like ZFS is recommended if you plan on archiving a lot.
```

### `$ archivebox config`

#### `(no args)`
Print the entire config to stdout.

#### `--get KEY`
Get the given config key:value and print it to stdout.

#### `--set KEY=VALUE`
Set the given config key:value in the current collection's config file.

#### `< stdin`

```bash
$ archviebox config
OUTPUT_DIR="output"
OUTPUT_PERMISSIONS=755
ONLY_NEW=False
...
```
```bash
$ archviebox --get CHROME_VERSION
Google Chrome 74.0.3729.40 beta
```
```bash
$ archviebox --set USE_CHROME=False
USE_CHROME=False
```

### `$ archivebox update`
**Check all subscribed feeds for new links, archive them and retry any previously failed pages.**

#### `(no args)`
Update the index and go through each page, retrying any that failed previously.

#### `--only-new`
By default it always retries previously failed/skipped pages, pass this flag to only archive newly added links without going through the whole archive and attempting to fix previously failed links.

#### `--resume=[timestamp]`
Resume the update process from a specific URL timestamp.

#### `--snapshot`
[TODO] by default ArchiveBox never re-archives pages after the first successful archive, if you want to take a new snapshot of every page even if there's an existing version, pass this option.

### `$ archivebox list`

#### `--csv=COLUMNS`

Print the output in CSV format, with the specified columns, e.g. `--csv=timestamp,base_url,is_archived`

#### `--json`

Print the output in JSON format (with all the link attributes included in the JSON output).

#### `--filter=REGEX`

Print only URLs matching a specified regex, e.g. `--filter='.*github.com.*'`

#### `--before=TIMESTAMP` / `--after=TIMESTAMP`

Print only URLs before or after a given timestamp, e.g. `--before=1554263415.2` or `--after=1554260000`

```bash
$ archivebox list --sort=timestamp
http://www.iana.org/domains/example
https://github.com/pirate/ArchiveBox/wiki
https://github.com/pirate/ArchiveBox/commit/0.4.0
https://github.com/pirate/ArchiveBox
https://archivebox.io
```
```bash
$ archivebox list --sort=timestamp --csv=timestamp,url
timestamp,url
1554260947,http://www.iana.org/domains/example
1554263415,https://github.com/pirate/ArchiveBox/wiki
1554263415.0,https://github.com/pirate/ArchiveBox/commit/0.4.0
1554263415.1,https://github.com/pirate/ArchiveBox
1554263415.2,https://archivebox.io
```
```bash
$ archivebox list --sort=timestamp --csv=timestamp,url --after=1554263415.0
timestamp,url
1554263415,https://github.com/pirate/ArchiveBox/wiki
1554263415.0,https://github.com/pirate/ArchiveBox/commit/0.4.0
1554263415.1,https://github.com/pirate/ArchiveBox
1554263415.2,https://archivebox.io
```

### `$ archivebox remove`

#### `--yes`

Proceed with removal without prompting the user for confirmation.

#### `--delete`

Also delete all the matching links snapshot data folders and content files.

#### `--filter-type`

Defaults to `exact`, but can be set to any of `exact`, `substring`, `domain`, or `regex`.

#### `pattern`

The filter pattern used to match links in the index.  Matching links are removed.

#### `--before=TIMESTAMP` / `--after=TIMESTAMP`

Remove any URLs bookmarked before/after the given timestamp, e.g. `--before=1554263415.2` or `--after=1554260000`.

```bash
$ archivebox remove --delete --filter-type=regex 'http(s)?:\\/\\/(.+)?(demo\\.dev|example\\.com)\\/?.*'
[*] Finding links in the archive index matching these regex patterns:
    http(s)?:\/\/(.+)?(youtube\.com|example\.com)\/?.*

---------------------------------------------------------------------------------------------------
timestamp        | is_archived      | num_outputs      | url
"1554984695"     | true             | 7                | "https://example.com"
---------------------------------------------------------------------------------------------------

[i] Found 1 matching URLs to remove.
    1 Links will be de-listed from the main index, and their archived content folders will be deleted from disk.
    (1 data folders with 7 archived files will be deleted!)

[?] Do you want to proceed with removing these 1 links?
    y/[n]: y

[*] [2019-04-11 08:11:57] Saving main index files...
    √ /opt/ArchiveBox/data/index.json
    √ /opt/ArchiveBox/data/index.html

[√] Removed 1 out of 1 links from the archive index.
    Index now contains 0 links.
```
```bash
$ archivebox remove --yes --delete --filter-type=domain example.com
...
```

### `$ archivebox manage`

Run a Django management command in the context of the current archivebox data directory.

#### `[command] [...args]`
The name of the management command to run, e.g.: `help`, `migrate`, `changepassword`, `createsuperuser`, etc.

```bash
$ archivebox manage help
Type 'archivebox manage help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[core]
    archivebox

...
```

### `$ archivebox server`

#### `[ip:port]`
The address:port combo to run the server on, defaults to `127.0.0.1:8000`.

```bash
$ archivebox server
[+] Starting ArchiveBox webserver...
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 23, 2019 - 01:40:52
Django version 2.2, using settings 'core.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### `$ archivebox proxy`

Run a live HTTP/HTTPS proxy for recording and replaying WARCs using pywb.

#### `--bind=[ip:port]`
The address:port combo to run the proxy on, defaults to `127.0.0.1:8010`.

#### `--record`
Save all traffic visited through the proxy to the archive.

#### `--replay`
Attempt to serve all pages visited through the proxy from the archive.

### `$ archivebox shell`

Drop into an ArchiveBox Django shell with access to all models and data.

```bash
$ archivebox shell                                                                                                                                                          
Loaded archive data folder ~/example_collection...
Python 3.7.2 (default, Feb 12 2019, 08:15:36)

In [1]: url_to_archive = Link.objects.filter(is_archived=True).values_list('url', flat=True)
...
```

### `$ archivebox oneshot`
Create a single URL archive folder with an index.json and index.html, and all the archive method outputs.  You can run this to archive single pages without needing to create a whole collection with `archivebox init`.

#### `--out-dir=[path]`
Path to save the single archive folder to, e.g. `./example.com_archive`.

#### `[--all|--media|--wget|...]`
Which archive methods to use when saving the URL.

## Python Usage

### API for normal ArchiveBox usage
```python
from archivebox import add, subscribe, update

add('https://example.com', depth=2)
subscribe('https://example.com/some/feed.rss')
update(only_new=True)
```

### API for All Useful Subcomponents
```python
from archivebox import oneshot
from archivebox.crawl import rss
from archivebox.extract import media

links = crawl_rss(open('feed.rss', 'r').read())
assets = media.extract('https://youtube.com/watch?v=example')
oneshot('https://example.com', depth=2, out_dir='~/Desktop/example.com_archive')
```

---

## Design

As of v0.4.0 ArchiveBox also writes the index to a `sqlite3` file using the Django ORM (in addition to the usual `json` and `html` formats, those aren't going away).  To an end user, it will still appear to be a single CLI application, and none of the django complexity will be exposed.  Django is used primarily because it allows for safe migrations of a sqlite database. As the schema gets updated in the future I don't want to break people's archives with every new version.  It also allows us to have the GUI server start with many safe defaults and share much of the same codebase with the CLI and library components, including maintaining the archive database and managing a worker pool.

There will be 3 primary use cases for archivebox, and all three will be served by the pip package:

 - simple CLI operation:
   `archivebox.cli import add --depth=1 ./path/to/export.html` (similar to current `archivebox` CLI)
 - use of individual components as a library: 
  `from archivebox.extract import screenshot` or `archivebox oneshot --screenshot ...`
 - usage in server mode with a GUI to add/remove links and create exports:
   `archivebox server`

## Dependencies:
 * django (required)
 * sqlite (required)
 * headless chrome (required)
 * wget (required)
 * redis (optional, for web GUI only)
 * dramatiq (optinal, for web GUI only)

When launched in webserver mode, archivebox will automatically spawn a pool of workers (dramatiq) as big as the number of CPUs available to use for crawling, archiving, and publishing.

When launched in CLI mode it will use normal subprocesses to do multithreading without redis/dramatiq.

## Code Folder Layout

* archivebox/
    * core/
        * models.py
            Archive = Dict[Page, Dict[Archiver, List[Asset]]]   # A collection of archived pages
            Crawl = List[Page]                                                      # list of links to add to an archive
            Page                                                   # an archived page with unique url
            Asset                                              # a file archived from a page

        * util.py
        * settings.py
    
    * crawl/
        impl:
            detect_crawlable(Import) -> bool
            crawl(Import) -> List[Page]
            
        * txt.py
        * rss.py
        * netscape.py
        * pocket.py
        * pinboard.py
        * html.py

    * extract/
        impl:
            detect_extractable(Page) -> bool
            extract(Page) -> List[Asset]

        * wget.py
        * screenshot.py
        * pdf.py
        * dom.py
        * youtubedl.py
        * waybackmachine.py
        * solana.py

    * publish/
        impl:
            publish(Archive, output_format)

        * html.py
        * json.py
        * csv.py
        * sql.py


## Collection Data Folder Layout

* ArchiveBox.conf
* database/
    * sqlite.db
* archive
    * assets/\<hash>/
* logs/
    * server.log
    * crawl.log
    * archive.log

## Exported Folder Layout

For publishing the archive as static html/json/csv/sql.

* index.html,json,csv,sql
* archive/
    * \<timestamp>/
        * index.html
        * \<url>/
            * index.html,json,csv,sql
        * assets/
            * hash.mp4
            * hash.txt
            * hash.mp3

---

The server will be runnable with docker / docker-compose as well:

```yaml
version: '3'

services:
    archivebox:
        image: archivebox
        ports:
            - '8098:80'
        volumes:
            - ./data/:/data
```

---

### Major long-term changes
 - release **`pip`, `apt`, `pkg`, and `brew` packaged distributions** for installing ArchiveBox
 - add an **optional web GUI** for managing sources, adding new links, and viewing the archive
 - switch to django + **sqlite db with migrations system** & json/html export for managing archive schema changes and persistence
 - modularize internals to allow importing individual components
 - switch to sha256 of URL as unique link ID
 - support **storing multiple snapshots** of pages over time
 - support **custom user puppeteer scripts to run while archiving** (e.g. for expanding reddit threads, scrolling thread on twitter, etc)
 - support named collections of archived content with different user access permissions
 - support sharing archived assets via DHT + torrent / ipfs / ZeroNet / other sharing system

### Smaller planned features
 - support pushing pages to multiple 3rd party services using ArchiveNow instead of just archive.org
 - body text extraction to markdown (using [fathom](https://hacks.mozilla.org/2017/04/fathom-a-framework-for-understanding-web-pages/)?)
 - featured image / thumbnail extraction
 - auto-tagging links based on important/frequent keywords in extracted text (like pocket)
 - automatic article summary paragraphs from extracted text with nlp summarization library
 - full-text search of extracted text with elasticsearch/elasticlunr/ag
 - download closed-caption subtitles from Youtube and other video sites for full-text indexing of video content
 - try pulling dead sites from archive.org and other sources if original is down (https://github.com/hartator/wayback-machine-downloader)
 - And more in the [issues list](https://github.com/pirate/ArchiveBox/issues/)...

---

**IMPORTANT**: *Please don't work on any of these major long-term tasks without [contacting me first](https://nicksweeting.com/blog#Contact-Me), work is already in progress for many of these, and I may have to reject your PR if it doesn't align with the existing work!*