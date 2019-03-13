▶️ *Make sure the dependencies are [fully installed](https://github.com/pirate/ArchiveBox/wiki/Install) before running any ArchiveBox commands.*

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

## Overview

The `./archive` binary is a shortcut to `bin/archivebox`.  Piping RSS, JSON, [Netscape](https://msdn.microsoft.com/en-us/library/aa753582(v=vs.85).aspx), or TXT lists of links into the `./archive` command will add them to your archive folder, and create a locally-stored browsable archive for each new URL.

The archiver produces an [output folder](#Disk-Layout) `output/` containing `index.html`, `index.json`, and archived copies of all the sites organized by timestamp bookmarked.  It's powered by [Chrome headless](https://developers.google.com/web/updates/2017/04/headless-chrome), good 'ol `wget`, and a few other common Unix tools.

## CLI Usage

<img src="https://i.imgur.com/biVfFYr.png" width="30%" align="right">

`./archive` refers to the executable shortcut in the root of the project, but you can also call ArchiveBox via `./bin/archivebox`.  If you add `/path/to/ArchiveBox/bin` to your shell `$PATH` then you can call `archivebox` from anywhere on your system.

If you're using Docker, the CLI interface is similar but needs to be prefixed by `docker-compose exec ...` or `docker run ...`, for examples see the [[Docker]] page.

 - [Run ArchiveBox with configuration options](#Run-ArchiveBox-with-configuration-options)
 - [Import a single URL or list of URLs via stdin](#Import-a-single-URL-or-list-of-URLs-via-stdin)
 - [Import list of links exported from browser or another service](#Import-list-of-links-exported-from-browser-or-another-service)
 - [Import list of URLs from a remote RSS feed or file](#Import-list-of-URLs-from-a-remote-RSS-feed-or-file)
 - [Import list of links from browser history](#Import-list-of-links-from-browser-history)

---

### Run ArchiveBox with configuration options
You can set environment variables in your shell profile, a config file, or by using the `env` command.

```bash
env FETCH_MEDIA=True MEDIA_TIMEOUT=500 ./archive ...
```
See [[Configuration]] page for more details about the available options and ways to pass config.  
If you're using Docker, also make sure to read the Configuration section on the [[Docker]] page.

---

### Import a single URL or list of URLs via stdin
```bash
echo 'https://example.com' | ./archive
# or
cat urls_to_archive.txt | ./archive
```
You can also pipe in RSS, XML, Netscape, or any of the other supported import formats via stdin.

---

### Import list of links exported from browser or another service

```bash
./archive ~/Downloads/browser_bookmarks_export.html
# or
./archive ~/Downloads/pinboard_bookmarks.json
# or
./archive ~/Downloads/other_links.txt
```

Passing a file as an argument here does not archive the file, it parses it as a list of URLs and archives the links *inside of it*, so only use it for *lists of links* to archive, not HTML files or other content you want added directy to the archive.

---

### Import list of URLs from a remote RSS feed or file
ArchiveBox will download the URL to a local file in `output/sources/` and attempt to autodetect the format and import any URLs found. Currently, Netscape HTML, JSON, RSS, and plain text links lists are supported.

```bash
./archive https://example.com/feed.rss
# or
./archive https://example.com/links.txt
```

Passing a URL as an argument here does not archive the specified URL, it downloads it and archives the links *inside* of it, so only use it for RSS feeds or other *lists of links* you want to add.  To add an individual link use the instruction above and pass the URL via stdin instead of as an argument.

---

### Import list of links from browser history
```bash
./bin/archivebox-export-browser-history --chrome
./archive output/sources/chrome_history.json
# or
./bin/archivebox-export-browser-history --firefox
./archive output/sources/firefox_history.json
```

---

## UI Usage

To access your archive, open `output/index.html` in a browser.  You should see something [like this](https://archive.sweeting.me).

You can sort by column, search using the box in the upper right, and see the total number of links at the bottom.

Click the Favicon under the "Files" column to go to the details page for each link. 

<div align="center">
<img src="https://i.imgur.com/52RjhUM.png" width="45%">
<img src="https://i.imgur.com/Gg9sTyq.png" width="45%">
</div>

## Disk Layout

The `output/` folder containing the UI HTML and archived data has the structure outlined here.

```yaml
 - output/
   - index.json           # Main index of all archived URLs
   - index.html

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
Those numbers are from running it single-threaded on my i5 machine with 50mbps down.  YMMV.  

Storage requirements go up immensely if you're using `FETCH_MEDIA=True` and are archiving many pages with audio & video.

You can run it in parallel by using the `resume` feature, or by manually splitting export.html into multiple files:
```bash
./archive export.html 1498800000 &  # second argument is timestamp to resume downloading from
./archive export.html 1498810000 &
./archive export.html 1498820000 &
./archive export.html 1498830000 &
```
Users have reported running it with 50k+ bookmarks with success (though it will take more RAM while running).

If you already imported a huge list of bookmarks and want to import only new
bookmarks, you can use the `ONLY_NEW` environment variable. This is useful if
you want to import a bookmark dump periodically and want to skip broken links
which are already in the index.
