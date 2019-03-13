<div align="center">

<img src="https://i.imgur.com/4nkFjdv.png" height="35px"/>

<h2>ArchiveBox Documentation</h2>

*(Previously [named](https://github.com/pirate/ArchiveBox/issues/108) `Bookmark Archiver`)*

▶️ *If you need help or have a question, you can open an [issue](https://github.com/pirate/ArchiveBox/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc) or reach out on [Twitter](https://github.com/theSquashSH).*


**Use the sidebar on the right to browse documentation topics ->**

</div>

---

### Can import links from:

 - <img src="https://getpocket.com/favicon.ico" height="22px"/> Pocket, Pinboard, Instapaper
 - <img src="https://nicksweeting.com/images/rss.svg" height="22px"/> RSS, XML, JSON, HTML, Markdown, or plain text lists
 - <img src="https://nicksweeting.com/images/bookmarks.png" height="22px"/> Browser history or bookmarks (Chrome, Firefox, Safari, IE, Opera, and more)
 - *Shaarli, Delicious, Reddit Saved Posts, Wallabag, Unmark.it, and any other text with links in it!*

### Can save these things for each site:

 - **Index:** `index.html` & `index.json` HTML and JSON index files containing metadata and details
 - **Title:** `title` title of the site
 - **Favicon:** `favicon.ico` favicon of the site
 - **WGET Clone:** `example.com/page-name.html` wget clone of the site, with .html appended if not present
 - **WARC:** `warc/` for the html + gzipped warc file `<timestamp>.gz`
 - **PDF:** `output.pdf` Printed PDF of site using headless chrome
 - **Screenshot:** `screenshot.png` 1440x900 screenshot of site using headless chrome
 - **DOM Dump:** `output.html` DOM Dump of the HTML after rendering using headless chrome
 - **URL to Archive.org:** `archive.org.txt` A link to the saved site on archive.org
 - **Audio & Video:** `media/` all audio/video files + playlists, including subtitles & metadata with youtube-dl
 - **Source Code:** `git/` clone of any repository found on github, bitbucket, or gitlab links

 By default it does everything, visit the [Configuration](https://github.com/pirate/ArchiveBox/wiki/Configuration) page for details on how to disable or fine-tune certain methods.

The archiving is additive, so you can schedule `./archive` to run regularly and pull new links into the index.
All the saved content is static and indexed with JSON files, so it lives forever & is easily parseable, it requires no always-running backend.

---

<div align="center">

[![](https://img.shields.io/badge/Donate-Patreon-%23DD5D76.svg)](https://www.patreon.com/theSquashSH)

</div>