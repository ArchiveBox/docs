Configuration is done through environment variables.  You can pass in settings using all the usual environment variable methods: e.g. by using the `env` command, settings variables in your shell profile, or sourcing a `.env` file before running the command.

Example configuration using `env` command:
```bash
env CHROME_BINARY=google-chrome-stable RESOLUTION=1440,900 FETCH_PDF=False ./archive ~/Downloads/bookmarks_export.html
```

**Configuration Options:**
 - [General Settings](#general-settings)
 - [Archive Method Toggles](#archive-method-toggles)
 - [Archive Method Options](#archive-method-options)
 - [Shell Options](#shell-options)
 - [Dependency Options](#dependency-options)

All the available config options are described in this document below, but can also be found along with examples in [`etc/ArchiveBox.conf.default`](https://github.com/pirate/ArchiveBox/blob/master/etc/ArchiveBox.conf.default). The code that loads the config is in [`archivebox/config.py`](https://github.com/pirate/ArchiveBox/blob/master/archivebox/config.py), but don't modify the defaults in `config.py` directly, as your changes there will be erased whenever you update ArchiveBox.

To create a persistent config file, see the [Creating a Config File](#creating-a-config-file) section.  
To see details on how to do configuration when using Docker, see the [[Docker]] page.

---

Example config in: [`etc/ArchiveBox.conf.default`](https://github.com/pirate/ArchiveBox/blob/master/etc/ArchiveBox.conf.default).

## General Settings

*General options around the archiving process, output format, and timing.*

---
#### `OUTPUT_DIR`
**Possible Values:** [`$REPO_DIR/output`]/`/srv/www/bookmarks`/...  
Path to an output folder to store the archive in.  Defaults to `output/` in the root directory of the repository.

---
#### `OUTPUT_PERMISSIONS`
**Possible Values:** [`755`]/`644`/...  
Permissions to set the output directory and file contents to.

---
#### `ONLY_NEW`
**Possible Values:** [`False`]/`True`  
Download files for only newly added links when running the `./archive` command. By default ArchiveBox will go through all links in the index and download any missing files on every run, set this to `True` to only archive the fresh links added during this run without attempting to also update older archived links.

---
#### `TIMEOUT`
**Possible Values:** [`60`]/`120`/...  
Maximum allowed download time per archive method for each link in seconds.  If you have a slow network connection or are seeing frequent timeout errors, you can raise this value.

---
#### `MEDIA_TIMEOUT`
**Possible Values:** [`3600`]/`120`/...  
Maximum allowed download time for fetching media when `FETCH_MEDIA=True` in seconds.  This timeout is separate and usually much longer than `TIMEOUT` because media downloaded with `youtube-dl` can often be quite large and take many minutes/hours to download.  Tweak this setting based on your network speed and maximum media file size you plan on downloading.

*Related options:*  
[`FETCH_MEDIA`](#fetch_media)

---
#### `TEMPLATES_DIR`
**Possible Values:** [`$REPO_DIR/archivebox/templates`]/`/path/to/custom/templates`/...  
Path to a directory containing custom index html templates for themeing your archive output.  Folder at specified path must contain the following files:
 - `static/`
 - `index.html`
 - `link_index.html`
 - `index_row.html`

You can copy the files in `archivebox/templates` into your own directory to start developing a custom theme, then edit `TEMPLATES_DIR` to point to your new custom templates directory.

*Related options:*  
[`FOOTER_INFO`](#footer_info)

---
#### `FOOTER_INFO`
**Possible Values:** [`Content is hosted for personal archiving purposes only.  Contact server owner for any takedown requests.`]/`Operated by ACME Co.`/...  
Some text to display in the footer of the archive index.  Useful for providing server admin contact info to respond to takedown requests.

*Related options:*  
[`TEMPLATES_DIR`](#templates_dir)

---

## Archive Method Toggles

*High-level on/off switches for all the various methods used to archive URLs.*

---
#### `FETCH_TITLE`
**Possible Values:** [`True`]/`False`  
By default ArchiveBox uses the title provided by the import file, but not all types of imports provide titles (e.g. Plain texts lists of URLs).  When this is True, ArchiveBox downloads the page (and follows all redirects), then it attempts to parse the link's title from the first `<title></title>` tag found in the response.  It may be buggy or not work for certain sites that use JS to set the title, disabling it will lead to links imported without a title showing up with their URL as the title in the UI.

*Related options:*  
[`ONLY_NEW`](#only_new), [`CHECK_SSL_VALIDITY`](#check_ssl_validity)

---
#### `FETCH_FAVICON`
**Possible Values:** [`True`]/`False`  
Fetch and save favicon for the URL from Google's public favicon service: `https://www.google.com/s2/favicons?domain={domain}`.  Set this to `FALSE` if you don't need favicons, but be aware all the links may show with spinners next to them in the index as the favicon is used as the status icon to confirm the archive process is complete for that URL.

*Related options:*  
[`TEMPLATES_DIR`](#templates_dir), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`CURL_BINARY`](#curl_binary)

---
#### `FETCH_WGET`
**Possible Values:** [`True`]/`False`  
Fetch page with wget, and save responses into folders for each domain, e.g. `example.com/index.html`, with `.html` appended if not present.  For a full list of options used during the `wget` download process, see the `archivebox/archive_methods.py:fetch_wget(...)` function.

*Related options:*  
[`TIMEOUT`](#timeout), [`FETCH_WGET_REQUISITES`](#fetch_wget_requisites), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`COOKIES_FILE`](#cookies_file), [`WGET_USER_AGENT`](#wget_user_agent), [`FETCH_WARC`](#fetch_warc), [`WGET_BINARY`](#wget_binary)

---
#### `FETCH_WARC`
**Possible Values:** [`True`]/`False`  
Save a timestamped WARC archive of all the page requests and responses during the wget archive process.

*Related options:*  
[`TIMEOUT`](#timeout), [`FETCH_WGET_REQUISITES`](#fetch_wget_requisites), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`COOKIES_FILE`](#cookies_file), [`WGET_USER_AGENT`](#wget_user_agent), [`FETCH_WGET`](#fetch_wget), [`WGET_BINARY`](#wget_binary)

---
#### `FETCH_PDF`
**Possible Values:** [`True`]/`False`  
Print page as PDF.

*Related options:*  
[`TIMEOUT`](#timeout), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`CHROME_USER_DATA_DIR`](#chrome_user_data_dir), [`CHROME_BINARY`](#chrome_binary)

---
#### `FETCH_SCREENSHOT`
**Possible Values:** [`True`]/`False`  
Fetch a screenshot of the page.

*Related options:*  
[`RESOLUTION`](#resolution), [`TIMEOUT`](#timeout), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`CHROME_USER_DATA_DIR`](#chrome_user_data_dir), [`CHROME_BINARY`](#chrome_binary)

---
#### `FETCH_DOM`
**Possible Values:** [`True`]/`False`  
Fetch a DOM dump of the page.

*Related options:*  
[`TIMEOUT`](#timeout), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`CHROME_USER_DATA_DIR`](#chrome_user_data_dir), [`CHROME_BINARY`](#chrome_binary)

---
#### `FETCH_GIT`
**Possible Values:** [`True`]/`False`  
Fetch any git repositories on the page.

*Related options:*  
[`TIMEOUT`](#timeout), [`GIT_DOMAINS`](#git_domains), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`GIT_BINARY`](#git_binary)

---
#### `FETCH_MEDIA`
**Possible Values:** [`True`]/`False`  
Fetch all audio, video, annotations, and media metadata on the page using `youtube-dl`.  Warning, this can use up *a lot* of storage very quickly.

*Related options:*  
[`MEDIA_TIMEOUT`](#media_timeout), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`YOUTUBEDL_BINARY`](#youtubedl_binary)

---
#### `SUBMIT_ARCHIVE_DOT_ORG`
**Possible Values:** [`True`]/`False`  
Submit the page's URL to be archived on Archive.org. (The Internet Archive) 

*Related options:*  
[`TIMEOUT`](#timeout), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`CURL_BINARY`](#curl_binary)

---

## Archive Method Options

*Specific options for individual archive methods above. Some of these are shared between multiple archive methods, others are specific to a single method.*

---
#### `CHECK_SSL_VALIDITY`
**Possible Values:** [`True`]/`False`  
Whether to enforce HTTPS certificate and HSTS chain of trust when archiving sites.  Set this to `False` if you want to archive pages even if they have expired or invalid certificates.  Be aware that when `False` you cannot guarantee that you have not been man-in-the-middle'd while archiving content, so the content cannot be verified to be what's on the original site.

---
#### `FETCH_WGET_REQUISITES`
**Possible Values:** [`True`]/`False`  
Fetch images/css/js with wget. (True is highly recommended, otherwise your wont download many critical assets to render the page, like images, js, css, etc.)

*Related options:*  
[`TIMEOUT`](#timeout), [`FETCH_WGET`](#fetch_wget), [`FETCH_WARC`](#fetch_warc), [`WGET_BINARY`](#wget_binary)

---
#### `RESOLUTION`
**Possible Values:** [`1440,900`]/`1024,768`/...  
Screenshot resolution in pixels width,height.  

*Related options:*  
[`FETCH_SCREENSHOT`](#fetch_screenshot)

---
#### `WGET_USER_AGENT`
**Possible Values:** [`Wget/1.19.1`]/`"Mozilla/5.0 ..."`/...  
User agent to use during wget downloads.  You can set this to impersonate a more common browser like Chrome or Firefox if you're experiences pages blocking unknown user agents.

*Related options:*  
[`FETCH_WGET`](#fetch_wget), [`FETCH_WARC`](#fetch_warc), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`WGET_BINARY`](#wget_binary)

---
####  `GIT_DOMAINS`
**Possible Values:** [`github.com,bitbucket.org,gitlab.com`]/`git.example.com`/...  
Domains to attempt download of git repositories on using `git clone`.

*Related options:*  
[`FETCH_GIT`](#fetch_git), [`CHECK_SSL_VALIDITY`](#check_ssl_validity)

---
####  `COOKIES_FILE`
**Possible Values:** [`None`]/`/path/to/cookies.txt`/...  
Cookies file to pass to wget.  To capture sites that require a user to be logged in, you can specify a path to a [netscape-format](http://www.cookiecentral.com/faq/#3.5) `cookies.txt` file for wget to use.  You can generate this file by using a browser extension to export your cookies in this format, or by using wget with `--save-cookies`.

*Related options:*  
[`FETCH_WGET`](#fetch_wget), [`FETCH_WARC`](#fetch_warc), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`WGET_BINARY`](#wget_binary)

---
#### `CHROME_USER_DATA_DIR`
**Possible Values:** [`~/.config/google-chrome`]/`/tmp/chrome-profile`/...  
Path to a Chrome user profile directory.  To capture sites that require a user to be logged in, you can specify a path to a chrome user profile (which loads the cookies needed for the user to be logged in).  If you don't have an existing Chrome profile, create one with `chromium-browser --user-data-dir=/tmp/chrome-profile`, and log into the sites you need.  Then set `CHROME_USER_DATA_DIR=/tmp/chrome-profile` to make ArchiveBox use that profile.  

By default when set to `None`, ArchiveBox tries all the following User Data Dir paths in order:  
https://chromium.googlesource.com/chromium/src/+/HEAD/docs/user_data_dir.md

*Related options:*  
[`FETCH_PDF`](#fetch_pdf), [`FETCH_SCREENSHOT`](#fetch_screenshot), [`FETCH_DOM`](#fetch_dom), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`CHROME_HEADLESS`](#chrome_headless), [`CHROME_BINARY`](#chrome_binary)

---
#### `CHROME_HEADLESS`
**Possible Values:** [`True`]/`False`  
Whether or not to use Chrome/Chromium in `--headless` mode (no browser UI displayed).  When set to `False`, the full Chrome UI will be launched each time it's used to archive a page, which greatly slows down the process but allows you to watch in real-time as it saves each page.  

*Related options:*  
[`FETCH_PDF`](#fetch_pdf), [`FETCH_SCREENSHOT`](#fetch_screenshot), [`FETCH_DOM`](#fetch_dom), [`CHROME_USER_DATA_DIR`](#chrome_user_data_dir), [`CHROME_BINARY`](#chrome_binary)

---

## Shell Options

*Options around the format of the CLI output.*

---
#### `USE_COLOR`
**Possible Values:** [`True`]/`False`  
Colorize console output. Defaults to `True` if stdin is a TTY (interactive session), otherwise `False` (e.g. if run in a script or piped into a file).

<img src="https://i.imgur.com/BDPfWxk.png" width="48%"/>
<img src="https://i.imgur.com/kIL8zSD.png" width="48%"/>

---
#### `SHOW_PROGRESS`
**Possible Values:** [`True`]/`False`  
Show real-time progress bar in console output. Defaults to `True` if stdin is a TTY (interactive session), otherwise `False` (e.g. if run in a script or piped into a file).

<img src="https://i.imgur.com/XY2E7AR.png" width="99%"/>

---

## Dependency Options

*Options for defining which binaries to use for the various archive method dependencies.*

---
#### `CHROME_BINARY`
**Possible Values:** [`chromium-browser`]/`/usr/local/bin/google-chrome`/...  
Path or name of the Google Chrome / Chromium binary to use for all the headless browser archive methods.

Without setting this environment variable, ArchiveBox by default look for the following binaries in `$PATH` in this order:
 - `chromium-browser`
 - `chromium`
 - `google-chrome`
 - `google-chrome-stable`
 - `google-chrome-unstable`
 - `google-chrome-beta`
 - `google-chrome-canary`
 - `google-chrome-dev`

You can override the default behavior to search for any available bin by setting the environment variable to your preferred Chrome binary name or path.

The chrome/chromium dependency is _optional_ and only required for screenshots, PDF, and DOM dump output, it can be safely ignored if those three methods are disabled.

*Related options:*  
[`FETCH_PDF`](#fetch_pdf), [`FETCH_SCREENSHOT`](#fetch_screenshot), [`FETCH_DOM`](#fetch_dom)

---
#### `WGET_BINARY`
**Possible Values:** [`wget`]/`/usr/local/bin/wget`/...  
Path or name of the wget binary to use.

*Related options:*  
[`FETCH_WGET`](#fetch_wget), [`FETCH_WARC`](#fetch_warc)

---
#### `YOUTUBEDL_BINARY`
**Possible Values:** [`youtube-dl`]/`/usr/local/bin/youtube-dl`/...  
Path or name of the [youtube-dl](https://github.com/rg3/youtube-dl) binary to use.

*Related options:*  
[`FETCH_MEDIA`](#fetch_media)

---
#### `GIT_BINARY`
**Possible Values:** [`git`]/`/usr/local/bin/git`/...  
Path or name of the git binary to use.

*Related options:*  
[`FETCH_GIT`](#fetch_git)

---
#### `CURL_BINARY`
**Possible Values:** [`curl`]/`/usr/local/bin/curl`/...  
Path or name of the curl binary to use.

*Related options:*  
[`FETCH_FAVICON`](#fetch_favicon), [`SUBMIT_ARCHIVE_DOT_ORG`](#submit_archive_dot_org)

---
---

# Creating a Config File

*Note: If you're using Docker, see the [[Docker]] page for configuration instructions.*

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