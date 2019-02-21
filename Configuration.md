## Intro

Configuration is done through environment variables.  You can pass in settings using all the usual environment variable methods: e.g. by using the `env` command, settings variables in your shell profile, or sourcing a `.env` file before running the command.

You can also modify the defaults in `archivebox/config.py` directly, but that's not recommended as your custom settings will be erased whenever you update ArchiveBox.

Example configuration using `env` command:
```bash
env CHROME_BINARY=google-chrome-stable RESOLUTION=1440,900 FETCH_PDF=False ./archive ~/Downloads/bookmarks_export.html
```

---

## Environment Variables

As defined in [`archivebox/config.py`](https://github.com/pirate/ArchiveBox/blob/master/archivebox/config.py) and [`etc/ArchiveBox.conf.default`](https://github.com/pirate/ArchiveBox/blob/master/etc/ArchiveBox.conf.default).

### Shell Options
 - colorize console ouput: `USE_COLOR` value: [`True`]/`False`
 - show progress bar: `SHOW_PROGRESS` value: [`True`]/`False`
 - archive permissions: `OUTPUT_PERMISSIONS` values: [`755`]/`644`/`...`

### Dependency Options
 - path to Chrome: `CHROME_BINARY` values: [`chromium-browser`]/`/usr/local/bin/google-chrome`/`...`
 - path to wget: `WGET_BINARY` values: [`wget`]/`/usr/local/bin/wget`/`...`

### Archive Settings
 - output directory: `OUTPUT_DIR` values: [`$REPO_DIR/output`]/`/srv/www/bookmarks`/`...` Optionally output the archives to an alternative directory.
 - maximum allowed download time per link: `TIMEOUT` values: [`60`]/`30`/`...`
 - maximum allowed download time per media file: `MEDIA_TIMEOUT` values: [`3600`]/`120`/`...`
 - import only new links: `ONLY_NEW` values `True`/[`False`]

### Archive Method Toggles
Possible values: [`True`]/`False`

   - fetch page with wget: `FETCH_WGET`
   - fetch images/css/js with wget: `FETCH_WGET_REQUISITES` (True is highly recommended)
   - print page as PDF: `FETCH_PDF`
   - fetch a screenshot of the page: `FETCH_SCREENSHOT`
   - fetch a DOM dump of the page: `FETCH_DOM`
   - fetch git repositories on the page: `FETCH_GIT`
   - fetch a WARC dump of the page: `FETCH_WARC`
   - fetch all audio and video on the page: `FETCH_MEDIA`
   - fetch a DOM dump of the page: `FETCH_DOM`
   - fetch a favicon for the page: `FETCH_FAVICON`
   - fetch and parse the title tag from html: `FETCH_TITLE`
   - submit the page to archive.org: `SUBMIT_ARCHIVE_DOT_ORG` 

### Archive Method Options
 - screenshot: `RESOLUTION` values: [`1440,900`]/`1024,768`/`...`
 - user agent: `WGET_USER_AGENT` values: [`Wget/1.19.1`]/`"Mozilla/5.0 ..."`/`...`
 - git domains: `GIT_DOMAINS` values: [`github.com,bitbucket.org,gitlab.com`]/`git.example.com`/`...`
 - cookies file: `COOKIES_FILE` values: [`None`]/`/path/to/cookies.txt`/`...`
    To capture sites that require a user to be logged in, you can specify a path to a [netscape-format](http://www.cookiecentral.com/faq/#3.5) `cookies.txt` file for wget to use.  You can generate this file by using a browser extension to export your cookies in this format, or by using wget with `--save-cookies`.
 - chrome profile: `CHROME_USER_DATA_DIR` values: [`~/Library/Application\ Support/Google/Chrome/Default`]/`/tmp/chrome-profile`/`...`
    To capture sites that require a user to be logged in, you can specify a path to a chrome user profile (which loads the cookies needed for the user to be logged in).  If you don't have an existing chrome profile, create one with `chromium-browser --disable-gpu --user-data-dir=/tmp/chrome-profile`, and log into the sites you need.  Then set `CHROME_USER_DATA_DIR=/tmp/chrome-profile` to make ArchiveBox use that profile.

 (See defaults & more at the top of `config.py`)

To tweak the outputted html index file's look and feel, just edit the HTML files in `archiver/templates/`.

The chrome/chromium dependency is _optional_ and only required for screenshots, PDF, and DOM dump output, it can be safely ignored if those three methods are disabled.

## Creating a Config File

*Note: if using Docker Compose you should set the config in the `docker-compose.yml` file or a `.env` file instead.*

To set up a persistent config:

1. Copy `etc/ArchiveBox.conf.default` to `~/.ArchiveBox.conf`
```bash
cp ArchiveBox/etc/ArchiveBox.conf.default ~/.ArchiveBox.conf
```

2. Edit your options inside `~/.ArchiveBox.conf`, e.g.:
```bash
CHROME_BINARY=google-chrome-stable
RESOLUTION=1440,900
FETCH_PDF=False
```

3. Source your config file when you run your archive script:
```bash
export "$(grep -v '^#' ~/.ArchiveBox.conf | xargs)"; ./archive https://example.com/rss/feed.xml
```

Improving this process is on the roadmap, in future versions you'll be able to pass a config file directly to the archive command.