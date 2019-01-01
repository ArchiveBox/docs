### (Recently [renamed](https://github.com/pirate/ArchiveBox/issues/108) from `Bookmark Archiver`)


    "Your own personal Way-Back Machine"

---

Save an archived copy of the websites you visit (the actual *content* of each site, not just the list of links).  Can archive entire browsing history, or just links matching a filter or bookmarks list.

ArchiveBox can import links from:

 - <img src="https://nicksweeting.com/images/bookmarks.png" height="22px"/> Browser history or bookmarks (Chrome, Firefox, Safari, IE, Opera)
 - <img src="https://getpocket.com/favicon.ico" height="22px"/> Pocket
 - <img src="https://pinboard.in/favicon.ico" height="22px"/> Pinboard
 - <img src="https://nicksweeting.com/images/rss.svg" height="22px"/> RSS or plain text lists
 - Shaarli, Delicious, Instapaper, Reddit Saved Posts, Wallabag, Unmark.it, and more!

For each site, it outputs (configurable):

- Browsable static HTML archive (wget)
- PDF (Chrome headless)
- Screenshot (Chrome headless)
- HTML after 2s of JS running (Chrome headless)
- Favicon
- Submits URL to archive.org
- Index summary pages: index.html & index.json

The archiving is additive, so you can schedule `./archive` to run regularly and pull new links into the index.
All the saved content is static and indexed with json files, so it lives forever & is easily parseable, it requires no always-running backend.

[DEMO: archive.sweeting.me](https://archive.sweeting.me)

[![](https://img.shields.io/badge/Donate-Patreon-%23DD5D76.svg)](https://www.patreon.com/theSquashSH)

<img src="https://i.imgur.com/q3Oz9wN.png" width="75%" alt="Desktop Screenshot" align="top"><img src="https://i.imgur.com/TG0fGVo.png" width="25%" alt="Mobile Screenshot" align="top"><br/>