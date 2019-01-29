<div align="center">

<img src="https://i.imgur.com/4nkFjdv.png" height="35px"/>

<h2>ArchiveBox Documentation</h2>

*(Recently [renamed](https://github.com/pirate/ArchiveBox/issues/108) from `Bookmark Archiver`)*

▶️ *If you need help or have a question, you can open an [issue](https://github.com/pirate/ArchiveBox/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc) or reach out on [Twitter](https://github.com/theSquashSH).*


Use the sidebar on the right to browse documentation topics ->

</div>

---

### Can import links from:

 - <img src="https://nicksweeting.com/images/bookmarks.png" height="22px"/> Browser history or bookmarks (Chrome, Firefox, Safari, IE, Opera)
 - <img src="https://nicksweeting.com/images/rss.svg" height="22px"/> RSS or plain text lists
 - <img src="https://getpocket.com/favicon.ico" height="22px"/> Pocket, Pinboard, Instapaper
 - *Shaarli, Delicious, Reddit Saved Posts, Wallabag, Unmark.it, and any text with links in it!*

### Can save these things for each site:

 - `favicon.ico` favicon of the site
 - `example.com/page-name.html` wget clone of the site, with .html appended if not present
 - `output.pdf` Printed PDF of site using headless chrome
 - `screenshot.png` 1440x900 screenshot of site using headless chrome
 - `output.html` DOM Dump of the HTML after rendering using headless chrome
 - `archive.org.txt` A link to the saved site on archive.org
 - `warc/` for the html + gzipped warc file <timestamp>.gz
 - `media/` any mp4, mp3, subtitles, and metadata found using youtube-dl
 - `git/` clone of any repository for github, bitbucket, or gitlab links
 - `index.html` & `index.json` HTML and JSON index files containing metadata and details

 By default it does everything, visit the [Configuration](https://github.com/pirate/ArchiveBox/wiki/Configuration) page for details on how to disable or fine-tune certain methods.

The archiving is additive, so you can schedule `./archive` to run regularly and pull new links into the index.
All the saved content is static and indexed with JSON files, so it lives forever & is easily parseable, it requires no always-running backend.

[DEMO: archive.sweeting.me](https://archive.sweeting.me)

<img src="https://i.imgur.com/q3Oz9wN.png" width="75%" alt="Desktop Screenshot" align="top"><img src="https://i.imgur.com/TG0fGVo.png" width="25%" alt="Mobile Screenshot" align="top"><br/>

## Details

`ArchiveBox/archive` is the script that takes a [Pocket-format](https://getpocket.com/export), [JSON-format](https://pinboard.in/export/), [Netscape-format](https://msdn.microsoft.com/en-us/library/aa753582(v=vs.85).aspx), RSS, or plan-text-formatted list of links, and downloads a clone of each linked website to turn into a browsable archive that you can store locally or host online.

The archiver produces an output folder `output/` containing an `index.html`, `index.json`, and archived copies of all the sites,
organized by timestamp bookmarked.  It's Powered by [headless](https://developers.google.com/web/updates/2017/04/headless-chrome) Chromium and good 'ol `wget`.

Wget doesn't work on sites you need to be logged into, but chrome headless does, see the [Configuration](#configuration)* section for `CHROME_USER_DATA_DIR`.

**Large Exports & Estimated Runtime:** 

I've found it takes about an hour to download 1000 articles, and they'll take up roughly 1GB.  
Those numbers are from running it single-threaded on my i5 machine with 50mbps down.  YMMV.  

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

---

<div align="center">

[![](https://img.shields.io/badge/Donate-Patreon-%23DD5D76.svg)](https://www.patreon.com/theSquashSH)

</div>