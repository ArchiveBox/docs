## Roadmap

<img src="https://i.imgur.com/es97GGV.png" width="20%" align="right"/>

▶️ *Comment here to discuss the contribution roadmap:  
[Official Roadmap Discussion](https://github.com/pirate/ArchiveBox/issues/120).*

If you feel like contributing a PR, some of these tasks are pretty easy.  Feel free to open an issue if you need help getting started in any way!

**IMPORTANT**: *Please don't work on any of these major long-term tasks without [contacting me first](https://nicksweeting.com/blog#Contact-Me), work is already in progress for many of these, and I may have to reject your PR if it doesn't align with the existing work!*

---

# Planned Specification

ArchiveBox is going to migrate towards this design spec over the next 6 months bit by bit as functionality gets implemented and refactors are released.

**API:**
 - [`pip install archivebox`](#-pip-install-archivebox)
 - [`archivebox --version`](#-archivebox-version--version)
 - [`archivebox --help`](#-archivebox-help-h--help)
 - [`archivebox init`](#-archivebox-init)
 - [`archivebox add`](#-archivebox-add)
 - [`archivebox subscribe`](#-archivebox-subscribe)
 - [`archivebox config`](#-archivebox-config)
 - [`archivebox update`](#-archivebox-update)
 - [`archivebox oneshot`](#-archivebox-oneshot)
 - [`archivebox server`](#-archivebox-server)
 - [`archivebox proxy`](#-archivebox-proxy)
 - [`archivebox shell`](#-archivebox-shell)
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

### `$ pip install archivebox`
```bash
...
Installing collected packages: archivebox
  Running setup.py install for archivebox ... done
Successfully installed archivebox-0.3.0+03047e428
```

### `$ archivebox [version|--version]`
```bash
ArchiveBox v0.3.0+03047e428

[√] CURL:      /usr/bin/curl --version
               curl 7.54.0 (x86_64-apple-darwin18.0) libcurl/7.54.0 LibreSSL/2.6.5 zlib/1.2.11 nghttp2/1.24.1

[√] GIT:       /usr/local/bin/git --version
               git version 2.20.1

[√] WGET:      /usr/local/bin/wget --version
               GNU Wget 1.20.1 built on darwin18.2.0.

[√] YOUTUBEDL: /usr/local/bin/youtube-dl --version
               2019.03.09

[√] CHROME:    /Applications/Google Chrome.app/Contents/MacOS/Google Chrome --version
               Google Chrome 74.0.3729.40 beta
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

#### `(no args)`
With no arguments, it interactively prompts the user to set up the collection, similar to `npm init`.

####  `< stdin`
You can optionally pipe in config as `KEY=VALUE` pairs in python/.env format to setup the project (if you don't want to use the interactive prompt)

```bash
$ mkdir ~/my_archive; cd ~/my_archive
$ archivebox init
Welcome to ArchiveBox v0.30+03047e428!
[+] Creating a new archive collection in the current folder...
    > ~/Documents/my_collection

[1/3] What do you want to call this collection? [main]: main
[2/3] Do you want to retry previously failed pages after checking for new pages to add? [y]/n: y
[3/3] Do you want to automatically submit added URLs to archive.org and other online services? [y]/n: y 

[√] Done! Your archive collection has been created.
    > ./ArchiveBox.conf contains your configuration

Visit https://ArchiveBox.io to see documentation, or run:
   archivebox help

To get started, you can add individual pages or import lists or feeds of URLs:
   archivebox add https://example.com
   archivebox add --depth=1 ~/Downloads/firefox_bookmarks.html
   archivebox add --depth=1 https://blog.example.com/some/rss/feed.xml

You can also watch certain file files or URLs and import add links automatically on every update:
   archivebox subscribe https://getpocket.com/users/example/feed/all
   archivebox subscribe ~/Documents/my_favorite_sites.txt
   archivebox update
```

Initialize a new "collection" folder, aka a complete archive containing an ArchiveBox.conf config file, an index of all the archived pages, and the archived content for each page.

### `$ archivebox add`

#### `--skip=[existing|none]`
Controls whether to skip links that have been previously archived. To re-archive links and take a new snapshot every time they're added, pass `none`.

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

### `$ archivebox subscribe`
Download a remote feed or check a remote file path for new links every time
`archivebox update` is run.

#### `path`
Specify the path as the path to a local file or remote URL to check for new links.

```bash
[+] Adding new subscription: https://getpocket.com/users/example/feed/all
    > data/subscriptions.txt

[√] New subscription added.
    Check your subscribed local paths and remote feeds
    for any new links, and archive them by running:
        archivebox update
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

#### `--skip=[none|existing]`
By default it always retries previously failed pages, set this to `existing` to only archive newly added links.

#### `--resume=[timestamp]`
Resume the update process from a specific URL timestamp.

#### `--snapshot`
[TODO] by default ArchiveBox never re-archives pages after the first successful archive, if you want to take a new snapshot of every page even if there's an existing version, pass this option.


### `$ archivebox server [--bind=0.0.0.0:8000]`
```bash
# WIP
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

The new design is based on a django app with management commands that perform each function above.  To an end user, it will appear to be a single cli application, and none of the django complexity will be exposed.  Django is used primarily because it allows for safe migrations of a sqlite database. As the schema gets updated in the future I don't want to break people's archives with every new version.  It also allows us to have the GUI server start with many safe defaults and share much of the same codebase with the CLI and library components, including maintaining the archive database and managing a worker pool.

There will be 3 primary use cases for archivebox, and all three will be served by the pip package:

 - simple CLI operation:
   `archivebox add --depth=1 ./path/to/export.html` (similar to current `archivebox` CLI)
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