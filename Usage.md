▶️ *Make sure you have ArchiveBox [fully installed](https://github.com/pirate/ArchiveBox/wiki/Install) before running any of the commands below.*

# CLI Usage

`./archive` refers to the executable shortcut in the root of the project, but you can also call ArchiveBox via `./bin/archivebox`.  If you add `/path/to/ArchiveBox/bin` to your shell `$PATH` then you can call `archivebox` from anywhere on your system.

If you're using Docker, the CLI interface is similar but needs to be prefixed by `docker-compose exec ...` or `docker run ...`, for examples see the [[Docker]] page.

<div align="center">
<img src="https://i.imgur.com/biVfFYr.png" width="50%"><br/>
</div>

## Run ArchiveBox with configuration options
You can set environment variables in your shell profile, a config file, or by using the `env` command.

```bash
env FETCH_MEDIA=True MEDIA_TIMEOUT=500 ./archive ...
```
See [[Configuration]] page for more details about the available options and ways to pass config.  
If you're using Docker, also make sure to read the Configuration section on the [[Docker]] page.

## Import a single URL or list of URLs via stdin
```bash
echo 'https://example.com' | ./archive
# or
cat urls_to_archive.txt | ./archive
```
You can also pipe in RSS, XML, Netscape, or any of the other supported import formats via stdin.

## Import list of links exported from browser or another service

```bash
./archive ~/Downloads/browser_bookmarks_export.html
# or
./archive ~/Downloads/pinboard_bookmarks.json
# or
./archive ~/Downloads/other_links.txt
```

Passing a file as an argument here does not archive the file, it parses it as a list of URLs and archives the links *inside of it*, so only use it for *lists of links* to archive, not HTML files or other content you want added directy to the archive.

## Import list of URLs from a remote RSS feed or file
ArchiveBox will download the URL to a local file in `output/sources/` and attempt to autodetect the format and import any URLs found. Currently, Netscape HTML, JSON, RSS, and plain text links lists are supported.

```bash
./archive https://example.com/feed.rss
# or
./archive https://example.com/links.txt
```

Passing a URL as an argument here does not archive the specified URL, it downloads it and archives the links *inside* of it, so only use it for RSS feeds or other *lists of links* you want to add.  To add an individual link use the instruction above and pass the URL via stdin instead of as an argument.

## Import list of links from browser history
```bash
./bin/archivebox-export-browser-history --chrome
./archive output/sources/chrome_history.json
# or
./bin/archivebox-export-browser-history --firefox
./archive output/sources/firefox_history.json
```

# UI Usage

To access your archive, open `output/index.html` in a browser.  You should see something [like this](https://archive.sweeting.me).

You can sort by column, search using the box in the upper right, and see the total number of links at the bottom.

Click the Favicon under the "Files" column to go to the details page for each link. 

<img src="https://i.imgur.com/52RjhUM.png" width="45%">
<img src="https://i.imgur.com/Gg9sTyq.png" width="45%">


# More

 - Read [[Docker]] to learn about ArchiveBox usage with Docker and Docker Compose
 - Read [[Configuration]] to learn about the various archive method options
 - Read [[Scheduled Archiving]] to learn how to set up automatic daily archiving
 - Read [[Publishing Your Archive]] if you want to host your archive for others to access online
 - Read [[Troubleshooting]] if you encounter any problems