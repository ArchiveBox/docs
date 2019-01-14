# CLI Usage

`./archive` refers to the executable shortcut in the root of the project, but you can also call ArchiveBox via `./bin/archivebox`.

Make sure to run `./setup` or follow the [[Install]] instructions before archiving anything.

## Import a single URL or list of URLs via stdin
```bash
echo 'https://example.com' | ./archive
# or
./archive < urls_to_archive.txt
```

## Import a bookmarks export from a browser
```bash
./archive ~/Downloads/bookmarks_export.html
```

## Archive URLs from a remote RSS feed or file
```bash
./archive https://example.com/feed.rss
# or
./archive https://example.com/links.txt
```