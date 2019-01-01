Configuration is done through environment variables.  You can pass in settings using all the usual environment variable methods: e.g. by using the `env` command, settings variables in your shell profile, or sourcing a `.env` file before running the command.

You can also modify the defaults in `archiver/config.py` directly, but that's not recommended as your custom settings will be erased whenever you update ArchiveBox.

Example configuration using `env` command:
```bash
env CHROME_BINARY=google-chrome-stable RESOLUTION=1440,900 FETCH_PDF=False ./archive ~/Downloads/bookmarks_export.html
```

**Shell Options:**
 - colorize console ouput: `USE_COLOR` value: [`True`]/`False`
 - show progress bar: `SHOW_PROGRESS` value: [`True`]/`False`
 - archive permissions: `OUTPUT_PERMISSIONS` values: [`755`]/`644`/`...`

**Dependency Options:**
 - path to Chrome: `CHROME_BINARY` values: [`chromium-browser`]/`/usr/local/bin/google-chrome`/`...`
 - path to wget: `WGET_BINARY` values: [`wget`]/`/usr/local/bin/wget`/`...`

**Archive Options:**
 - maximum allowed download time per link: `TIMEOUT` values: [`60`]/`30`/`...`
 - import only new links: `ONLY_NEW` values `True`/[`False`]
 - archive methods (values: [`True`]/`False`):
   - fetch page with wget: `FETCH_WGET`
   - fetch images/css/js with wget: `FETCH_WGET_REQUISITES` (True is highly recommended)
   - print page as PDF: `FETCH_PDF`
   - fetch a screenshot of the page: `FETCH_SCREENSHOT`
   - fetch a DOM dump of the page: `FETCH_DOM`
   - fetch a favicon for the page: `FETCH_FAVICON`
   - submit the page to archive.org: `SUBMIT_ARCHIVE_DOT_ORG` 
 - screenshot: `RESOLUTION` values: [`1440,900`]/`1024,768`/`...`
 - user agent: `WGET_USER_AGENT` values: [`Wget/1.19.1`]/`"Mozilla/5.0 ..."`/`...`
 - chrome profile: `CHROME_USER_DATA_DIR` values: [`~/Library/Application\ Support/Google/Chrome/Default`]/`/tmp/chrome-profile`/`...`
    To capture sites that require a user to be logged in, you must specify a path to a chrome profile (which loads the cookies needed for the user to be logged in).  If you don't have an existing chrome profile, create one with `chromium-browser --disable-gpu --user-data-dir=/tmp/chrome-profile`, and log into the sites you need.  Then set `CHROME_USER_DATA_DIR=/tmp/chrome-profile` to make ArchiveBox use that profile.
 - output directory: `OUTPUT_DIR` values: [`$REPO_DIR/output`]/`/srv/www/bookmarks`/`...` Optionally output the archives to an alternative directory.

 (See defaults & more at the top of `config.py`)

To tweak the outputted html index file's look and feel, just edit the HTML files in `archiver/templates/`.

The chrome/chromium dependency is _optional_ and only required for screenshots, PDF, and DOM dump output, it can be safely ignored if those three methods are disabled.