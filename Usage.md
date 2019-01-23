# CLI Usage

`./archive` refers to the executable shortcut in the root of the project, but you can also call ArchiveBox via `./bin/archivebox`.  If you add `/path/to/ArchiveBox/bin` to your shell `$PATH` then you can call `archivebox` from anywhere on your system.

Make sure to run `./setup` or follow the [[Install]] instructions before archiving anything.

For instructions on how to configure ArchiveBox settings, see the [[Configuration]] page.

## Import a single URL or list of URLs via stdin
```bash
echo 'https://example.com' | ./archive
# or
./archive < urls_to_archive.txt
```

## Import links exported from browser or another service
```bash
./archive ~/Downloads/browser_bookmarks_export.html
# or
./archive ~/Downloads/pinboard_bookmarks.json
# or
./archive ~/Downloads/other_links.txt
```

## Archive URLs from a remote RSS feed or file
ArchiveBox will download the URL to a local file in `output/sources/` and attempt to autodetect the format and import any URLs found. Currently, Netscape HTML, JSON, RSS, and plain text links lists are supported.

```bash
./archive https://example.com/feed.rss
# or
./archive https://example.com/links.txt
```

# UI Usage

To access your archive, open `output/index.html` in a browser.  You should see something [like this](https://archive.sweeting.me).

You can sort by column, search using the box in the upper right, and see the total number of links at the bottom.

Click the Favicon under the "Files" column to go to the details page for each link. 

---

*Some alternatives that also work:*

Add a list of links from remote URL:
```bash
./archive "https://getpocket.com/users/yourusername/feed/all"  # url to an RSS, html, or json links file
```

Add a single URL or list of URLs to archive via stdin:
```bash
cat ./urls_to_archive.txt | ./archive
# or
echo 'https://example.com' | ./archive
```

Add all the links from your browser history:
```bash
./bin/archivebox-export-browser-history --chrome           # works with --firefox as well, can take path to SQLite history db
./archive output/sources/chrome_history.json
```

Or update the archive without adding new links:
```bash
./archive
```

---

