# Configuration

▶️ *The full ArchiveBox config file definition with defaults can be found here: [`archivebox/config.py`](https://github.com/ArchiveBox/ArchiveBox/blob/master/archivebox/config.py#L27).*

Configuration of ArchiveBox is done by using the `archivebox config` command, modifying the `ArchiveBox.conf` file in the data folder, or by using environment variables. All three methods work equivalently when using Docker as well.

*Some equivalent examples of setting some configuration options:*
```bash[][]
archivebox config --set CHROME_BINARY=google-chrome-stable
# OR
echo "CHROME_BINARY=google-chrome-stable" >> ArchiveBox.conf
# OR
env CHROME_BINARY=google-chrome-stable archivebox add ~/Downloads/bookmarks_export.html
```

Environment variables take precedence over the config file, which is useful if you only want to use a certain option temporarily during a single run.

<br/>

<img src="https://i.imgur.com/EUeQbiZ.png" width="200px" align="right"/>

**Available Configuration Options:**
 - [General Settings:](#general-settings) Archiving process, output format, and timing.
 - [Archive Method Toggles:](#archive-method-toggles) On/off switches for methods.
 - [Archive Method Options:](#archive-method-options) Method tunables and parameters.
 - [Shell Options:](#shell-options) Format & behavior of CLI output.
 - [Dependency Options:](#dependency-options) Specify exact paths to dependencies. 

<br/>

In case this document is ever out of date, it's recommended to read the code that loads the config directly in [`archivebox/config.py`](https://github.com/ArchiveBox/ArchiveBox/blob/master/archivebox/config.py#L27).

---

<img src="https://i.imgur.com/iTYT7Ip.png" width="100%"/>


## General Settings

*General options around the archiving process, output format, and timing.*

---
#### `OUTPUT_PERMISSIONS`
**Possible Values:** [`755`]/`644`/...  
Permissions to set the output directory and file contents to.  

This is useful when running ArchiveBox inside Docker as root and you need to explicitly set the permissions to something that the users on the host can access.

---
#### `ONLY_NEW`
**Possible Values:** [`True`]/`False`  
Toggle whether or not to attempt rechecking old links when adding new ones, or leave old incomplete links alone and only archive the new links.

By default, ArchiveBox will only archive new links on each import. If you want it to go back through all links in the index and download any missing files on every run, set this to `False`.

*Note: Regardless of how this is set, ArchiveBox will never re-download sites that have already succeeded previously. When this is `False` it only attempts to fix previous pages have *missing* archive extractor outputs, it does not re-archive pages that have already been successfully archived.*

---
#### `TIMEOUT`
**Possible Values:** [`60`]/`120`/...  
Maximum allowed download time per archive method for each link in seconds.  If you have a slow network connection or are seeing frequent timeout errors, you can raise this value.

*Note: Do not set this to anything less than `15` seconds as it will cause Chrome to hang indefinitely and many sites to fail completely.*

---
#### `MEDIA_TIMEOUT`
**Possible Values:** [`3600`]/`120`/...  
Maximum allowed download time for fetching media when `SAVE_MEDIA=True` in seconds.  This timeout is separate and usually much longer than `TIMEOUT` because media downloaded with `youtube-dl` can often be quite large and take many minutes/hours to download.  Tweak this setting based on your network speed and maximum media file size you plan on downloading.

*Note: Do not set this to anything less than `10` seconds as it can often take 5-10 seconds for `youtube-dl` just to parse the page before it starts downloading media files.*

*Related options:*  
[`SAVE_MEDIA`](#save_media)

---
#### `CUSTOM_TEMPLATES_DIR`
**Possible Values:** [`None`]/`./path/to/custom_templates`/...  
Path to a directory containing custom html/css/images for overriding the default UI styling.  Files found in the folder at the specified path can override any of the defaults in the [`TEMPLATES_DIR`](https://github.com/ArchiveBox/ArchiveBox/tree/dev/archivebox/templates) directory (copy files from that default dir into your custom dir to get started making a custom theme).

If you've used `django` before, this works exactly the same way that `django` template overrides work (because it uses `django` under the hood).

*Related options:*  
[`FOOTER_INFO`](#footer_info)

---
#### `SNAPSHOTS_PER_PAGE`
**Possible Values:** [`40`]/`100`/...  

Maximum number of Snapshots to show per page on Snapshot list pages. Lower this value on slower machines to make the UI faster.

*Related options:*  
[`SEARCH_BACKEND_TIMEOUT`](#search_backend_timeout)

---
#### `FOOTER_INFO`
**Possible Values:** [`Content is hosted for personal archiving purposes only.  Contact server owner for any takedown requests.`]/`Operated by ACME Co.`/...  
Some text to display in the footer of the archive index.  Useful for providing server admin contact info to respond to takedown requests.

*Related options:*  
[`TEMPLATES_DIR`](#templates_dir)

---
#### `URL_BLACKLIST`
**Possible Values:** [`\.(css|js|otf|ttf|woff|woff2|gstatic\.com|googleapis\.com/css)(\?.*)?$`]/`.+\.exe$`/`http(s)?:\/\/(.+)?example.com\/.*'`/...  

A regex expression used to exclude certain URLs from archiving.  You can use if there are certain domains, extensions, or other URL patterns that you want to ignore whenever they get imported.  Blacklisted URLs wont be included in the index, and their page content wont be archived.

When building your exclusion list, you can check whether a given URL matches your regex expression in `python` like so:
```python
>>> import re
>>> URL_BLACKLIST = r'^http(s)?:\/\/(.+\.)?(youtube\.com)|(amazon\.com)\/.*$'  # replace this with your regex to test
>>> test_url = 'https://test.youtube.com/example.php?abc=123'
>>> bool(re.compile(URL_BLACKLIST, re.IGNORECASE | re.UNICODE | re.MULTILINE).search(test_url))
True   # this URL would not be archived because it matches the exclusion pattern
```

*Note: all assets required to render each page are still archived, `URL_BLACKLIST`/`URL_WHITELIST` do not apply to images, css, video, etc. visible inline within the page.*

*Related options:*  
[`URL_WHITELIST`](#URL_WHITELIST), [`SAVE_MEDIA`](#SAVE_MEDIA), [`SAVE_GIT`](#SAVE_GIT), [`GIT_DOMAINS`](#GIT_DOMAINS)

---
#### `URL_WHITELIST`
**Possible Values:** [`None`]/`^http(s)?:\/\/(.+)?example\.com\/?.*$`/...  

A regex expression used to exclude all URLs that don't match the given pattern from archiving.  You can use if there are certain domains, extensions, or other URL patterns that you want to ignore whenever they get imported.  Blacklisted URLs wont be included in the index, and their page content wont be archived.

When building your blacklist, you can check whether a given URL matches your regex expression in `python` like so:
```python
>>> import re
>>> URL_WHITELIST = r'^http(s)?:\/\/(.+)?example\.com\/?.*$'  # replace this with your regex to test
>>> test_url = 'https://test.example.com/example.php?abc=123'
>>> bool(re.compile(URL_BLACKLIST, re.IGNORECASE | re.UNICODE | re.MULTILINE).search(test_url))
True      # this URL would be archived

>>> test_url = 'https://test.youtube.com/example.php?abc=123'
>>> bool(re.compile(URL_BLACKLIST, re.IGNORECASE | re.UNICODE | re.MULTILINE).search(test_url))
False     # this URL would be excluded from archiving
```

This option is useful for **recursive archiving** of all the pages under a given domain or subfolder (aka crawling/spidering), without following links to external domains / parent folders.
```bash
# temporarily enforce a whitelist by setting the option as an environment variable
export URL_WHITELIST='^http(s)?:\/\/(.+)?example\.com\/?.*$'

# then run your archivebox commands in the same shell
archivebox add --depth=1 'https://example.com'
archivebox list https://example.com | archivebox add --depth=1
archivebox list https://example.com | archivebox add --depth=1
archivebox list https://example.com | archivebox add --depth=1   # repeat up to desired depth
...
# all URLs that don't match *.example.com will be excluded, e.g. a link to youtube.com would not be followed
```

*Note: all assets required to render each page are still archived, `URL_BLACKLIST`/`URL_WHITELIST` do not apply to images, css, video, etc. visible inline within the page.*

*Related options:*  
[`URL_BLACKLIST`](#URL_BLACKLIST), [`SAVE_MEDIA`](#SAVE_MEDIA), [`SAVE_GIT`](#SAVE_GIT), [`GIT_DOMAINS`](#GIT_DOMAINS)

---

## Archive Method Toggles

*High-level on/off switches for all the various methods used to archive URLs.*

---
#### `SAVE_TITLE`
**Possible Values:** [`True`]/`False`  
By default ArchiveBox uses the title provided by the import file, but not all types of imports provide titles (e.g. Plain texts lists of URLs).  When this is True, ArchiveBox downloads the page (and follows all redirects), then it attempts to parse the link's title from the first `<title></title>` tag found in the response.  It may be buggy or not work for certain sites that use JS to set the title, disabling it will lead to links imported without a title showing up with their URL as the title in the UI.

*Related options:*  
[`ONLY_NEW`](#only_new), [`CHECK_SSL_VALIDITY`](#check_ssl_validity)

---
#### `SAVE_FAVICON`
**Possible Values:** [`True`]/`False`  
Fetch and save favicon for the URL from Google's public favicon service: `https://www.google.com/s2/favicons?domain={domain}`.  Set this to `FALSE` if you don't need favicons.

*Related options:*  
[`TEMPLATES_DIR`](#templates_dir), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`CURL_BINARY`](#curl_binary)

---
#### `SAVE_WGET`
**Possible Values:** [`True`]/`False`  
Fetch page with wget, and save responses into folders for each domain, e.g. `example.com/index.html`, with `.html` appended if not present.  For a full list of options used during the `wget` download process, see the `archivebox/archive_methods.py:save_wget(...)` function.

*Related options:*  
[`TIMEOUT`](#timeout), [`SAVE_WGET_REQUISITES`](#save_wget_requisites), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`COOKIES_FILE`](#cookies_file), [`WGET_USER_AGENT`](#wget_user_agent), [`SAVE_WARC`](#save_warc), [`WGET_BINARY`](#wget_binary)

---
#### `SAVE_WARC`
**Possible Values:** [`True`]/`False`  
Save a timestamped WARC archive of all the page requests and responses during the wget archive process.

*Related options:*  
[`TIMEOUT`](#timeout), [`SAVE_WGET_REQUISITES`](#save_wget_requisites), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`COOKIES_FILE`](#cookies_file), [`WGET_USER_AGENT`](#wget_user_agent), [`SAVE_WGET`](#save_wget), [`WGET_BINARY`](#wget_binary)

---
#### `SAVE_PDF`
**Possible Values:** [`True`]/`False`  
Print page as PDF.

*Related options:*  
[`TIMEOUT`](#timeout), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`CHROME_USER_DATA_DIR`](#chrome_user_data_dir), [`CHROME_BINARY`](#chrome_binary)

---
#### `SAVE_SCREENSHOT`
**Possible Values:** [`True`]/`False`  
Fetch a screenshot of the page.

*Related options:*  
[`RESOLUTION`](#resolution), [`TIMEOUT`](#timeout), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`CHROME_USER_DATA_DIR`](#chrome_user_data_dir), [`CHROME_BINARY`](#chrome_binary)

---
#### `SAVE_DOM`
**Possible Values:** [`True`]/`False`  
Fetch a DOM dump of the page.

*Related options:*  
[`TIMEOUT`](#timeout), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`CHROME_USER_DATA_DIR`](#chrome_user_data_dir), [`CHROME_BINARY`](#chrome_binary)

---
#### `SAVE_SINGLEFILE`
**Possible Values:** [`True`]/`False`  
Fetch an HTML file with all assets embedded using [Single File](https://github.com/gildas-lormeau/SingleFile).

*Related options:*  
[`TIMEOUT`](#timeout), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`CHROME_USER_DATA_DIR`](#chrome_user_data_dir), [`CHROME_BINARY`](#chrome_binary), [`SINGLEFILE_BINARY`](#singlefile_binary)

---
#### `SAVE_READABILITY`
**Possible Values:** [`True`]/`False`  
Extract article text, summary, and byline using Mozilla's [Readability](https://github.com/mozilla/readability) library.
Unlike the other methods, this does not download any additional files, so it's practically free from a disk usage perspective. It works by using any existing downloaded HTML version (e.g. wget, DOM dump, singlefile) and piping it into readability.

*Related options:*  
[`TIMEOUT`](#timeout), [`SAVE_WGET`](#save_wget), [`SAVE_DOM`](#save_dom), [`SAVE_SINGLEFILE`](#save_singlefile), [`SAVE_MERCURY`](#save_mercury)

---
#### `SAVE_MERCURY`
**Possible Values:** [`True`]/`False`  
Extract article text, summary, and byline using the [Mercury](https://github.com/postlight/mercury-parser) library.
Unlike the other methods, this does not download any additional files, so it's practically free from a disk usage perspective. It works by using any existing downloaded HTML version (e.g. wget, DOM dump, singlefile) and piping it into readability.

*Related options:*  
[`TIMEOUT`](#timeout), [`SAVE_WGET`](#save_wget), [`SAVE_DOM`](#save_dom), [`SAVE_SINGLEFILE`](#save_singlefile), [`SAVE_READABILITY`](#save_readability)


---
#### `SAVE_GIT`
**Possible Values:** [`True`]/`False`  
Fetch any git repositories on the page.

*Related options:*  
[`TIMEOUT`](#timeout), [`GIT_DOMAINS`](#git_domains), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`GIT_BINARY`](#git_binary)

---
#### `SAVE_MEDIA`
**Possible Values:** [`True`]/`False`  
Fetch all audio, video, annotations, and media metadata on the page using `youtube-dl`.  Warning, this can use up *a lot* of storage very quickly.

*Related options:*  
[`MEDIA_TIMEOUT`](#media_timeout), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`YOUTUBEDL_BINARY`](#youtubedl_binary)

---
#### `SAVE_ARCHIVE_DOT_ORG`
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
#### `SAVE_WGET_REQUISITES`
**Possible Values:** [`True`]/`False`  
Fetch images/css/js with wget. (True is highly recommended, otherwise your won't download many critical assets to render the page, like images, js, css, etc.)

*Related options:*  
[`TIMEOUT`](#timeout), [`SAVE_WGET`](#save_wget), [`SAVE_WARC`](#save_warc), [`WGET_BINARY`](#wget_binary)

---
#### `RESOLUTION`
**Possible Values:** [`1440,2000`]/`1024,768`/...  
Screenshot resolution in pixels width,height.  

*Related options:*  
[`SAVE_SCREENSHOT`](#save_screenshot)

---
#### `CURL_USER_AGENT`
**Possible Values:** [`Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.61 Safari/537.36 ArchiveBox/{VERSION} (+https://github.com/ArchiveBox/ArchiveBox/) curl/{CURL_VERSION}`]/`"Mozilla/5.0 ..."`/...  
This is the user agent to use during curl archiving.  You can set this to impersonate a more common browser like Chrome or Firefox if you're getting blocked by servers for having an unknown/blacklisted user agent.

*Related options:*  
[`USE_CURL`](#use_curl), [`SAVE_TITLE`](#save_title), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`CURL_BINARY`](#curl_binary), [`WGET_USER_AGENT`](#wget_user_agent), [`CHROME_USER_AGENT`](#chrome_user_agent)

---
#### `WGET_USER_AGENT`
**Possible Values:** [`Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.61 Safari/537.36 ArchiveBox/{VERSION} (+https://github.com/ArchiveBox/ArchiveBox/) wget/{WGET_VERSION}`]/`"Mozilla/5.0 ..."`/...  
This is the user agent to use during wget archiving.  You can set this to impersonate a more common browser like Chrome or Firefox if you're getting blocked by servers for having an unknown/blacklisted user agent.

*Related options:*  
[`SAVE_WGET`](#save_wget), [`SAVE_WARC`](#save_warc), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`WGET_BINARY`](#wget_binary), [`CHROME_USER_AGENT`](#chrome_user_agent)

---
#### `CHROME_USER_AGENT`
**Possible Values:** [`Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.61 Safari/537.36 ArchiveBox/{VERSION} (+https://github.com/ArchiveBox/ArchiveBox/)`]/`"Mozilla/5.0 ..."`/...  

This is the user agent to use during Chrome headless archiving.  If you're experiencing being blocked by many sites, you can set this to hide the `Headless` string that reveals to servers that you're using a headless browser.

*Related options:*  
[`SAVE_PDF`](#save_pdf), [`SAVE_SCREENSHOT`](#save_screenshot), [`SAVE_DOM`](#save_dom), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`CHROME_USER_DATA_DIR`](#chrome_user_data_dir), [`CHROME_HEADLESS`](#chrome_headless), [`CHROME_BINARY`](#chrome_binary), [`WGET_USER_AGENT`](#wget_user_agent)


---
####  `GIT_DOMAINS`
**Possible Values:** [`github.com,bitbucket.org,gitlab.com`]/`git.example.com`/...  
Domains to attempt download of git repositories on using `git clone`.

*Related options:*  
[`SAVE_GIT`](#save_git), [`CHECK_SSL_VALIDITY`](#check_ssl_validity)

---
####  `COOKIES_FILE`
**Possible Values:** [`None`]/`/path/to/cookies.txt`/...  
Cookies file to pass to wget.  To capture sites that require a user to be logged in, you can specify a path to a [netscape-format](http://www.cookiecentral.com/faq/#3.5) `cookies.txt` file for wget to use.  You can generate this file by using a browser extension to export your cookies in this format, or by using wget with `--save-cookies`.

*Related options:*  
[`SAVE_WGET`](#save_wget), [`SAVE_WARC`](#save_warc), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`WGET_BINARY`](#wget_binary)

---
#### `CHROME_USER_DATA_DIR`
**Possible Values:** [`~/.config/google-chrome`]/`/tmp/chrome-profile`/...  
Path to a Chrome user profile directory.  To capture sites that require a user to be logged in, you can specify a path to a chrome user profile (which loads the cookies needed for the user to be logged in).  If you don't have an existing Chrome profile, create one with `chromium-browser --user-data-dir=/tmp/chrome-profile`, and log into the sites you need.  Then set `CHROME_USER_DATA_DIR=/tmp/chrome-profile` to make ArchiveBox use that profile.  

*Note: Make sure the path does not have `Default` at the end (it should the the parent folder of `Default`), e.g. set it to `CHROME_USER_DATA_DIR=~/.config/chromium` and not `CHROME_USER_DATA_DIR=~/.config/chromium/Default`.* 

By default when set to `None`, ArchiveBox tries all the following User Data Dir paths in order:  
https://chromium.googlesource.com/chromium/src/+/HEAD/docs/user_data_dir.md

*Related options:*  
[`SAVE_PDF`](#save_pdf), [`SAVE_SCREENSHOT`](#save_screenshot), [`SAVE_DOM`](#save_dom), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`CHROME_HEADLESS`](#chrome_headless), [`CHROME_BINARY`](#chrome_binary)

---
#### `CHROME_HEADLESS`
**Possible Values:** [`True`]/`False`  
Whether or not to use Chrome/Chromium in `--headless` mode (no browser UI displayed).  When set to `False`, the full Chrome UI will be launched each time it's used to archive a page, which greatly slows down the process but allows you to watch in real-time as it saves each page.  

*Related options:*  
[`SAVE_PDF`](#save_pdf), [`SAVE_SCREENSHOT`](#save_screenshot), [`SAVE_DOM`](#save_dom), [`CHROME_USER_DATA_DIR`](#chrome_user_data_dir), [`CHROME_BINARY`](#chrome_binary)

---
#### `CHROME_SANDBOX`
**Possible Values:** [`True`]/`False`  
Whether or not to use the Chrome sandbox when archiving.  

If you see an error message like this, it means you are trying to run ArchiveBox as root:  
```bash
:ERROR:zygote_host_impl_linux.cc(89)] Running as root without --no-sandbox is not supported. See https://crbug.com/638180
```

*Note: **Do not run ArchiveBox as root!** The solution to this error is not to override it by setting `CHROME_SANDBOX=False`, it's to use create another user (e.g. `www-data`) and run ArchiveBox under that new, less privileged user. This is a security-critical setting, only set this to `False` if you're running ArchiveBox inside a container or VM where it doesn't have access to the rest of your system!

*Related options:*  
[`SAVE_PDF`](#save_pdf), [`SAVE_SCREENSHOT`](#save_screenshot), [`SAVE_DOM`](#save_dom), [`CHECK_SSL_VALIDITY`](#check_ssl_validity), [`CHROME_USER_DATA_DIR`](#chrome_user_data_dir), [`CHROME_HEADLESS`](#chrome_headless), [`CHROME_BINARY`](#chrome_binary)


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
[`SAVE_PDF`](#save_pdf), [`SAVE_SCREENSHOT`](#save_screenshot), [`SAVE_DOM`](#save_dom), [`SAVE_SINGLEFILE`](#save_singlefile), [`CHROME_USER_DATA_DIR`](#chrome_user_data_dir), [`CHROME_HEADLESS`](#chrome_headless), [`CHROME_SANDBOX`](#chrome_sandbox)

---
#### `WGET_BINARY`
**Possible Values:** [`wget`]/`/usr/local/bin/wget`/...  
Path or name of the wget binary to use.

*Related options:*  
[`SAVE_WGET`](#save_wget), [`SAVE_WARC`](#save_warc)

---
#### `YOUTUBEDL_BINARY`
**Possible Values:** [`youtube-dl`]/`/usr/local/bin/youtube-dl`/...  
Path or name of the [youtube-dl](https://github.com/rg3/youtube-dl) binary to use.

*Related options:*  
[`SAVE_MEDIA`](#save_media)

---
#### `GIT_BINARY`
**Possible Values:** [`git`]/`/usr/local/bin/git`/...  
Path or name of the git binary to use.

*Related options:*  
[`SAVE_GIT`](#save_git)

---
#### `CURL_BINARY`
**Possible Values:** [`curl`]/`/usr/local/bin/curl`/...  
Path or name of the curl binary to use.

*Related options:*  
[`SAVE_FAVICON`](#save_favicon), [`SAVE_ARCHIVE_DOT_ORG`](#save_archive_dot_org)

---
#### `SINGLEFILE_BINARY`
**Possible Values:** [`single-file`]/`./node_modules/single-file/cli/single-file`/...  
Path or name of the SingleFile binary to use.

This can be installed using `npm install --no-audit --no-fund 'git+https://github.com/gildas-lormeau/SingleFile.git'`.

*Related options:*  
[`SAVE_SINGLEFILE`](#save_singlefile), [`CHROME_BINARY`](#chrome_binary), [`CHROME_USER_DATA_DIR`](#chrome_user_data_dir), [`CHROME_HEADLESS`](#chrome_headless), [`CHROME_SANDBOX`](#chrome_sandbox)

---
#### `READABILITY_BINARY`
**Possible Values:** [`readability-extractor`]/`./node_modules/readability-extractor/readability-extractor`/...  
Path or name of the Readability extrator binary to use.

This can be installed using `npm install --no-audit --no-fund 'git+https://github.com/ArchiveBox/readability-extractor.git'`.

*Related options:*  
[`SAVE_READABILITY`](#save_readability)

---
#### `MERCURY_BINARY`
**Possible Values:** [`mercury-parser`]/`./node_modules/@postlight/mercury-parser/cli.js`/...  
Path or name of the Mercury parser extractor binary to use.

This can be installed using `npm install --no-audit --no-fund '@postlight/mercury-parser'`.

*Related options:*  
[`SAVE_MERCURY`](#save_mercury)

---
#### `RIPGREP_BINARY`
**Possible Values:** [`rg`]/`rga`/...  

Path or name of the ripgrep binary to use for full text search.

This can be installed using your system package manager, e.g. `apt install ripgrep` or `brew install ripgrep`.

Optionally switch this to use `ripgrep-all` for full-text search support across more filetypes (e.g. PDF): https://github.com/phiresky/ripgrep-all.

*Related options:*  
[`SEARCH_BACKEND_ENGINE`](#search_backend_engine)


<img src="https://i.imgur.com/almAbwK.png" width="100%"/>
[]: 
