# Scheduled Archiving

## Using Cron

To schedule regular archiving you can use any task scheduler like `cron`, `at`, `sytsemd`, etc.

ArchiveBox ignores links that are imported multiple times (keeping the earliest version that it's seen).
This means you can add cron jobs that regularly poll the same file or URL for new links, adding only new
ones as necessary.

For some example configs, see the [`etc/cron.d`](https://github.com/pirate/ArchiveBox/blob/master/etc/cron.d) and [`etc/supervisord`](https://github.com/pirate/ArchiveBox/blob/master/etc/supervisord) folders.

## Examples

### Example: Import Firefox browser history every 24 hours

This example exports your browser history and archives it once a day:

**Create `/opt/ArchiveBox/bin/firefox_custom.sh`:**
```bash
#!/bin/bash

cd /opt/ArchiveBox
./bin/archivebox-export-browser-history --firefox ./output/sources/firefox_history.json
archivebox add < ./output/sources/firefox_history.json  >> /var/log/ArchiveBox.log
```

**Then create a new file `/etc/cron.d/ArchiveBox-Firefox` to tell cron to run your script every 24 hours:**
```bash
0 24 * * * www-data /opt/ArchiveBox/bin/firefox_custom.sh
```

### Example: Import an RSS feed from Pocket every 12 hours

This example imports your Pocket bookmark feed and archives any new links every 12 hours:

First, set your Pocket RSS feed to "public" under https://getpocket.com/privacy_controls.

**Create `/opt/ArchiveBox/bin/pocket_custom.sh`:**
```bash
#!/bin/bash

cd /opt/ArchiveBox
curl https://getpocket.com/users/yourusernamegoeshere/feed/all | archivebox add  >> /var/log/ArchiveBox.log
```

**Then create a new file `/etc/cron.d/ArchiveBox-Pocket` to tell cron to run your script every 12 hours:**
```bash
0 12 * * * www-data /opt/ArchiveBox/bin/pocket_custom.sh
```
