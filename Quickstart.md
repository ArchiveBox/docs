▶️ *It only takes 5 minutes to get up and running.*

ArchiveBox officially supports **Ubuntu**, **FreeBSD**, and **macOS**, but likely runs on many other systems.  You can run it on any system that supports **Docker**, including Windows.

First, we install the ArchiveBox dependencies, then we create a folder to store the archive data, and finally we import the list of links to the archive by running `./archive <links_file>`.

## 1. Create your archive

Create a folder to store your archive, and clone the ArchiveBox repo into it.
```bash
git clone https://github.com/pirate/ArchiveBox
cd ArchiveBox/
./setup   # installs all dependencies
```

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

## 3. Archive your list of URLs

To add a list of links from a file:
```bash
./archive ~/Downloads/bookmark_export.html      # replace with the path to your export file or URL from step 1
```

Or you can pass in URLs to archive via stdin:
```bash
echo 'https://example.com' | ./archive
```

## ✅ Done!

You can open `output/index.html` to view your archive.  (favicons will appear next to each title once it has finished downloading)

---

**Next Steps:**

 - Read [[Configuration]] to learn about the various archive method options
 - Read [[Scheduled Archiving]] to learn how to set up automatic daily archiving
 - Read [[Publishing Your Archive]] if you want to host your archive for others to access online
 - Read [[Troubleshooting]] if you encounter any problems