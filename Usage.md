# Usage

▶️ _Make sure the dependencies are [fully installed](https://github.com/pirate/ArchiveBox/wiki/Install) before running any ArchiveBox commands._

**ArchiveBox API Reference:**

<img src="https://i.imgur.com/aQZZcku.png" width="20%" align="right"/>

- [Overview](#Overview): Program structure and outline of basic archiving process.
- [CLI Usage](#CLI-Usage): Docs and examples for the ArchiveBox command line interface.
- [UI Usage](#UI-Usage): Docs and screenshots for the outputted HTML archive interface.
- [Disk Layout](#Disk-Layout): Description of the archive folder structure and contents.

**Related:**

- [[Docker]]: Learn about ArchiveBox usage with Docker and Docker Compose
- [[Configuration]]: Learn about the various archive method options
- [[Scheduled Archiving]]: Learn how to set up automatic daily archiving
- [[Publishing Your Archive]]: Learn how to host your archive for others to access
- [[Troubleshooting]]: Resources if you encounter any problems
- [Screenshots](https://github.com/pirate/ArchiveBox#Screenshots): See what the CLI and outputted HTML look like


## CLI Usage

<img src="https://i.imgur.com/biVfFYr.png" width="30%" align="right">

All three of these ways of running ArchiveBox are equivalent and interchangeable:

- `archivebox [subcommand] [...args]`  
  *Using the PyPI package via `pip install archivebox`*
- `archivebox run -v $PWD:/data nikisweeting/archivebox [subcommand] [...args]`  
  *Using the official Docker image*
- `docker-compose run archivebox [subcommand] [...args]`  
  *Using the official Docker image w/ Docker Compose*

You can share a single archivebox data directory between Docker and non-Docker instances as well, allowing you to run the server in a container but still execute CLI commands on the host for example.

For more examples see the [[Docker]] page.

- [Run ArchiveBox with configuration options](#Run-ArchiveBox-with-configuration-options)
- [Import a single URL or list of URLs via stdin](#Import-a-single-URL-or-list-of-URLs-via-stdin)
- [Import list of links exported from browser or another service](#Import-list-of-links-exported-from-browser-or-another-service)
- [Import list of URLs from a remote RSS feed or file](#Import-list-of-URLs-from-a-remote-RSS-feed-or-file)
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

### Import a list of URLs from a txt file

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

The `OUTPUT_DIR` folder (usually whatever folder you run `archivebox` in), contains the UI HTML and archived data with the structure outlined below.

```yaml
 - output/
   - index.sqlite3        # Main index of all archived URLs
   - index.json           # Redundant JSON version of the same main index
   - index.html           # Redundant static HTML version of the same main index

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

   - static/              # Staticfiles for the archive UI
   - robots.txt
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

## Python API Usage

```python
from archivebox.main import add, remove, server

... # load the archive directory first, see API docs below for more info

add('https://example.com', index_only=True, out_dir=out_dir)
remove(...)
server(...)
...
```

For more information see the [Python API Reference](https://docs.archivebox.io/en/latest/archivebox.html).
