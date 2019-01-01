Using ArchiveBox involves installing the ArchiveBox dependencies, creating a folder to store your archive data, and then importing a list of links to the archive by running the `./archive` binary.

**1. Get your list of URLs:**

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
 - Other File or URL: (e.g. RSS feed) pass as second argument in the next step

 (If any of these links are broken, please submit an issue and I'll fix it)

**2. Create your archive:**

```bash
git clone https://github.com/pirate/ArchiveBox
cd ArchiveBox/
./setup                                         # install all dependencies

# add a list of links from a file
./archive ~/Downloads/bookmark_export.html      # replace with the path to your export file or URL from step 1

# OR add a list of links from remote URL
./archive "https://getpocket.com/users/yourusername/feed/all"  # url to an RSS, html, or json links file

# OR add all the links from your browser history
./bin/archivebox-export-browser-history --chrome           # works with --firefox as well, can take path to SQLite history db
./archive output/sources/chrome_history.json

# OR just continue archiving the existing links in the index
./archive   # at any point if you just want to continue archiving where you left off, without adding any new links
```

**3. Done!**

You can open `output/index.html` to view your archive.  (favicons will appear next to each title once it has finished downloading)

If you want to host your archive somewhere to share it with other people, see the [Publishing Your Archive](#publishing-your-archive) section below.

**4. (Optional) Schedule it to run every day**

You can import links from any local file path or feed url by changing the second argument to `archive.py`.
ArchiveBox will ignore links that are imported multiple times, it will keep the earliest version that it's seen.
This means you can add multiple cron jobs to pull links from several different feeds or files each day,
it will keep the index up-to-date without duplicate links.

This example archives a pocket RSS feed and an export file every 24 hours, and saves the output to a logfile.
```bash
0 24 * * * yourusername /opt/ArchiveBox/archive https://getpocket.com/users/yourusername/feed/all > /var/log/archivebox_rss.log
0 24 * * * yourusername /opt/ArchiveBox/archive /home/darth-vader/Desktop/bookmarks.html > /var/log/archivebox_firefox.log
```
(Add the above lines to `/etc/crontab`)

**Next Steps**  
  
If you have any trouble, see the [Troubleshooting](#troubleshooting) section at the bottom.  
If you'd like to customize options, see the [Configuration](#configuration) section.  

If you want something easier than running programs in the command-line, take a look at [Pocket Premium](https://getpocket.com/premium) (yay Mozilla!) and [Pinboard Pro](https://pinboard.in/upgrade/) (yay independent developer!).  Both offer easy-to-use bookmark archiving with full-text-search and other features.