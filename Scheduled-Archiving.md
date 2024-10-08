# Scheduled Archiving

ArchiveBox contains a built-in scheduler that supports pulling in URLs regularly from the web or from the local filesystem.

```bash
$ cd ~/archivebox/data          # cd into your data directory first
$ archivebox schedule --help
[i] [2024-01-04 20:58:15] ArchiveBox v0.7.2: archivebox schedule --help
    > ~/archivebox/data

usage: archivebox schedule [-h] [--quiet] [--add] [--every EVERY] [--tag TAG] [--depth {0,1}] [--overwrite] [--update] [--clear] [--show] [--foreground] [--run-all] [import_path]

Set ArchiveBox to regularly import URLs at specific times using cron

positional arguments:
  import_path        Check this path and import any new links on every run (can be either local file or remote URL)

options:
  -h, --help         show this help message and exit
  --quiet, -q        Don't warn about storage space.
  --add              Add a new scheduled ArchiveBox update job to cron
  --every EVERY      Run ArchiveBox once every [timeperiod] (hour/day/month/year or cron format e.g. "0 0 * * *")
  --tag TAG, -t TAG  Tag the added URLs with the provided tags e.g. --tag=tag1,tag2,tag3
  --depth {0,1}      Depth to archive to [0] or 1, see "add" command help for more info
  --overwrite        Re-archive any URLs that have been previously archived, overwriting existing Snapshots
  --update           Re-pull any URLs that have been previously added, as needed to fill missing ArchiveResults
  --clear            Stop all ArchiveBox scheduled runs (remove cron jobs)
  --show             Print a list of currently active ArchiveBox cron jobs
  --foreground, -f   Launch ArchiveBox scheduler as a long-running foreground task instead of using cron.
  --run-all          Run all the scheduled jobs once immediately, independent of their configured schedules, can be used together with --foreground
```

ArchiveBox ignores links that are imported multiple times (keeping the earliest version that it's seen).
This means you can add cron jobs that regularly poll the same file or URL for new links, adding only new
ones as necessary, or you can pass `--overwrite` to save a fresh copy each time the scheduled task runs.

The list of defined scheduled tasks can be inspected and cleared with `archivebox schedule --show` and `archivebox schedule --clear`.

⚠️ Many popular sites such as Twitter, Reddit, Facebook, etc. take efforts to block/ratelimit/lazy-load content to avoid being scraped by bots like ArchiveBox. It may be better to use an alternative frontend with minimal JS when archiving those sites:  
https://github.com/mendel5/alternative-front-ends

The scheduled interval can be passed easily using `--every={day,week,month,year}` or by passing a [cron-style schedule](https://crontab.guru/) e.g. `--every='5 4 * * *'` to run at 04:05 every day.

The scheduler can also be run in `--foreground` mode to avoid relying on your host system's cron scheduler to be running.  
In foreground mode, it will run all tasks previously added using `archivebox schedule` in a long-running foreground process.
This is useful for running scheduled tasks inside docker-compose or supervisord.

### Docker Usage

```bash
docker-compose run --rm archivebox schedule --every=week --depth=1 https://example.com
docker-compose run --rm archivebox schedule --every=day https://example.com
docker-compose run --rm archivebox schedule --show
docker-compose run --rm archivebox schedule --help

# restart the scheduler container to pick up any changes made
docker compose restart archivebox_scheduler
```

`docker-compose.yml`:
```yaml
services:
  archivebox:
    image: archivebox/archivebox:dev
    command: server --quick-init 0.0.0.0:8000
    ...
    volumes:
      - ./data:/data
      - ./etc/crontabs:/var/spool/cron/crontabs

  archivebox_scheduler:
    image: archivebox/archivebox:dev
    command: schedule --foreground
    ...
    volumes:
      - ./data:/data
      - ./etc/crontabs:/var/spool/cron/crontabs
```
For a full Docker Compose example config see here: https://github.com/ArchiveBox/ArchiveBox/blob/dev/docker-compose.yml#:~:text=schedule

For more examples of plain Docker and Docker Compose usage with scheduling, see: https://github.com/ArchiveBox/ArchiveBox/issues/1155#issuecomment-1590146616

---

### Example: Archive a Twitter user's Tweets and linked content within once a week

```bash
archivebox schedule --every=week --depth=1 'https://nitter.net/ArchiveBoxApp'
```

Nitter is an alternative frontends recommended Twitter that formats the content better for archiving/bots and avoids ratelimits.

### Example: Archive a Reddit subreddit and discussions for every post once a week

```bash
# optionally limit URLs to Teddit (aka Reddit) to capture discussion and user pages but not external outbound URLs
archivebox config --set URL_WHITELIST='^http(s)?:\/\/(.+)?teddit\.net\/?.*$'

archivebox schedule --every=week --overwrite --depth=1 'https://teddit.net/r/DataHoarder/'
```

Teddit is an alternative frontend recommended for Reddit that formats the content better for archiving/bots and avoids ratelimits.  
`--overwrite` is passed to save a fresh copy each week, otherwise the URL will be ignored as it's already present in the collection after the first time it's added.

### Example: Archive the HackerNews front page and some linked articles every 24 hours

```bash
# optional exclude some URLs you don't want to archive
archivebox config --set URL_BLACKLIST='^http(s)?:\/\/(.+\.)?(youtube\.com)|(amazon\.com)\/.*$'

archivebox schedule --every=day --depth=1 'https://news.ycombinator.com'
``` 

### Example: Archive all URLs in an RSS feed from Pocket every 12 hours

This example imports your Pocket bookmark feed and archives any new links every 12 hours:

First, set your Pocket RSS feed to "public" under https://getpocket.com/privacy_controls.

Then tell ArchiveBox to pull it regularly:
```bash
archivebox schedule --every=day --depth=1 https://getpocket.com/users/yourusernamegoeshere/feed/all
```

### Example: Archive a Github repository's source code only once a month

```bash
archivebox schedule --every=month --extract=git --overwrite 'https://github.com/ArchiveBox'
```
`--extract=git` tells it to only use the Git source extractor and skip saving the HTML/screenshot/etc. other extractor methods.

### Example: Archive a list of URLs pulled from the filesystem every 30 minutes

```bash
archivebox schedule --every='30 * * * *' /some/path/to/urls.txt
```

---

## Advanced Scheduling Using Cron

To schedule regular archiving you can also use any other task scheduler like `cron`, `at`, `systemd`, etc. aside from the built-in scheduler `archivebox schedule`.

For some example configs, see the [`etc/cron.d`](https://github.com/ArchiveBox/ArchiveBox/blob/master/etc/cron.d) and [`etc/supervisord`](https://github.com/ArchiveBox/ArchiveBox/blob/master/etc/supervisord) folders.

### Example: Export and archive Firefox browser history every 24 hours

This example exports your browser history and archives it once a day, saving a summary to disk:

First download the ArchiveBox helper script for browser history exporting https://github.com/ArchiveBox/ArchiveBox/blob/dev/bin/export_browser_history.sh to `./bin/export_browser_history.sh`

Then create `/home/ArchiveBox/archivebox/bin/scheduled_firefox_import.sh`:
```bash
#!/bin/bash

cd `/home/ArchiveBox/archivebox
bash ./bin/export_browser_history --firefox ./output/sources/firefox_history.json
archivebox add < ./output/sources/firefox_history.json >> /var/log/ArchiveBox.log
archivebox status >> /var/log/ArchiveBox.log
```

Then tell cron to run your script every 24 hours:
```bash
echo '0 24 * * * archivebox /home/ArchiveBox/archivebox/bin/scheduled_firefox_import.sh' > /etc/cron.d/archivebox_scheduled_firefox_import
```

### Example: Import an RSS feed from Pocket every 12 hours

If you need to customize the import process or archive a password-locked RSS feed, you can do it manually with a bash script + cron `/home/ArchiveBox/archivebox/bin/scheduled_imports.sh`:
```bash
#!/bin/bash

cd /home/ArchiveBox/archivebox
curl --silent https://getpocket.com/users/yourusernamegoeshere/feed/all | archivebox add >> /home/ArchiveBox/archivebox/logs/scheduled_imports.log
# you can add additional flags to curl here e.g. to authenticate with HTTP
# curl --silent -u username:password ... | archivebox add >> ...
```
Then create a cronjob telling your system to run the script on your chosen regular interval (e.g. every 12 hours):
```bash
echo '0 12 * * * archivebox /home/ArchiveBox/archivebox/bin/scheduled_imports.sh' > /etc/cron.d/archivebox_scheduled_imports
```
