# Quickstart

<div align="center">
<img src="https://i.imgur.com/ZbHpEf8.jpg" width="40%"/>
</div>

▶️ *It only takes about 5 minutes to get up and running with ArchiveBox.*

ArchiveBox [officially supports](https://github.com/pirate/ArchiveBox/wiki/Install#supported-systems) **macOS**, **Ubuntu/Debian**, and **BSD**, but likely runs on many other systems.  You can run it on any system that supports **Docker**, including Windows.

If you want to use Docker or Docker Compose to run ArchiveBox, see the [[Docker]] page.

---

First, we install the ArchiveBox [dependencies](./Install#dependencies), then we create a folder to [store the archive data](https://github.com/pirate/ArchiveBox/wiki/Usage#Disk-Layout), and finally, we [import the list of links](https://github.com/pirate/ArchiveBox/wiki/Usage#CLI-Usage) to the archive by running `archivebox add < [links_file]`.

## 1. Set up ArchiveBox

Clone the ArchiveBox repo and install its dependencies:

```bash
git clone https://github.com/pirate/ArchiveBox
cd ArchiveBox/
./bin/setup.sh  # script prompts for user confirmation before installing anything
```

(The above are shell commands to run. If you're not used to those, consult your operating system's manual for how to run a terminal emulator.)

<img src="https://i.imgur.com/VMTzm0G.png" width="99%"/>

For more detail, including the manual setup and docker instructions, see the [[Install]] page.

## 2. Get your list of URLs to archive

Follow the links here to find instructions for exporting a list of URLs from each service.

 - [Pocket](https://getpocket.com/export)
 - [Pinboard](https://pinboard.in/export/)
 - [Instapaper](https://www.instapaper.com/user/export)
 - [Reddit Saved Posts](https://github.com/csu/export-saved-reddit)
 - [Shaarli](https://shaarli.readthedocs.io/en/master/guides/backup-restore-import-export/#export-links-as)
 - [Unmark.it](http://help.unmark.it/import-export)
 - [Wallabag](https://doc.wallabag.org/en/user/import/wallabagv2.html)
 - [Chrome Bookmarks](https://support.google.com/chrome/answer/96816?hl=en)
 - [Firefox Bookmarks](https://support.mozilla.org/en-US/kb/export-firefox-bookmarks-to-backup-or-transfer)
 - [Safari Bookmarks](http://i.imgur.com/AtcvUZA.png)
 - [Opera Bookmarks](http://help.opera.com/Windows/12.10/en/importexport.html)
 - [Internet Explorer Bookmarks](https://support.microsoft.com/en-us/help/211089/how-to-import-and-export-the-internet-explorer-favorites-folder-to-a-32-bit-version-of-windows)
 - Chrome History: `./bin/archivebox-export-browser-history --chrome`
 - Firefox History: `./bin/archivebox-export-browser-history --firefox`
 - Other File or URL: (e.g. RSS feed url, text file path) pass as second argument in the next step

 (If any of these links are broken, please submit an issue and I'll fix it)

## 3. Add your URLs to the archive

Pass in URLs directly, import a list of links from a file, or import from a feed URL. All via stdin:
```bash
echo 'https://example.com' | archivebox add
# or
archivebox add < ~/Downloads/example_bookmarks_export.html
# or
curl https://getpocket.com/users/example/feed/all | archivebox add
```

## ✅ Done!

Open `output/index.html` to view your archive.  (favicons will appear next to each title once they have finished downloading)

---

**Next Steps:**

 - Read [[Usage]] to learn about the various CLI and web UI functions
 - Read [[Configuration]] to learn about the various archive method options
 - Read [[Scheduled Archiving]] to learn how to set up automatic daily archiving
 - Read [[Publishing Your Archive]] if you want to host your archive for others to access online
 - Read [[Troubleshooting]] if you encounter any problems
