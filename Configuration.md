# Configuration

Configuration of ArchiveBox is done by using the `archivebox config` command, modifying the `ArchiveBox.conf` file in the data folder, or by using environment variables. All three methods work equivalently when using Docker as well.

*Some equivalent examples of setting some configuration options:*
```bash
archivebox config --set CHROME_BINARY=google-chrome-stable
# OR
echo "CHROME_BINARY=google-chrome-stable" >> ArchiveBox.conf
# OR
env CHROME_BINARY=google-chrome-stable archivebox add ~/Downloads/bookmarks_export.html
```

Environment variables take precedence over the config file, which is useful if you only want to use a certain option temporarily during a single run. For more examples see [Usage: Configuration](Usage#run-archivebox-with-configuration-options)...

<br/>

<img src="https://imgur.zervice.io/EUeQbiZ.png" width="200px" align="right"/>

**Available Configuration Options:**
 - [General Settings:](#general-settings) Archiving process, output format, and timing.
 - [Server Settings:](#server-settings) Web UI, auth, and reverse proxy options.
 - [Storage Settings:](#storage-settings) File layout, permissions, and temp directories.
 - [Search Settings:](#search-settings) Full-text search backend configuration.
 - [Archive Method Toggles:](#archive-method-toggles) On/off switches for methods.
 - [Archive Method Options:](#archive-method-options) Method tunables and parameters.
 - [Shell Options:](#shell-options) Format & behavior of CLI output.
 - [Dependency Options:](#dependency-options) Specify exact paths to dependencies.
 - [LDAP Settings:](#ldap-settings) LDAP/Active Directory authentication.
 - [Plugin Settings:](#plugin-settings) Per-plugin configuration options.

<br/>

---

<img src="https://imgur.zervice.io/iTYT7Ip.png" width="100%"/>
<p align="center">
<i>In case this document is ever out of date, check the source code for config definitions: <a href="https://github.com/ArchiveBox/ArchiveBox/blob/dev/archivebox/config/common.py"><code>archivebox/config/common.py</code></a> ➡️</i>
</p>

## General Settings

*General options around the archiving process, output format, and timing.*

---
#### `ONLY_NEW`
**Possible Values:** [`True`]/`False`
Toggle whether or not to attempt rechecking old links when adding new ones, or leave old incomplete links alone and only archive the new links.

By default, ArchiveBox will only archive new links on each import. If you want it to go back through all links in the index and download any missing files on every run, set this to `False`.

*Note: Regardless of how this is set, ArchiveBox will never re-download sites that have already succeeded previously. When this is `False` it only attempts to fix previous pages have *missing* archive extractor outputs, it does not re-archive pages that have already been successfully archived.*

---
#### `OVERWRITE`
**Possible Values:** [`False`]/`True`
When set to `True`, ArchiveBox will re-archive URLs even if they have already been successfully archived before, overwriting any existing output.

---
#### `TIMEOUT`
**Possible Values:** [`60`]/`120`/...
Maximum allowed download time per archive method for each link in seconds.  If you have a slow network connection or are seeing frequent timeout errors, you can raise this value.

*Note: Do not set this to anything less than `5` seconds as it will cause Chrome to hang indefinitely and many sites to fail completely.*

---
#### `MAX_URL_ATTEMPTS`
**Possible Values:** [`50`]/`100`/...
Maximum number of times ArchiveBox will attempt to archive a URL before giving up. Useful for handling transient failures.

---
#### `RESOLUTION`
**Possible Values:** [`1440,2000`]/`1024,768`/...
Default screenshot/PDF resolution in pixels width,height. Used as the fallback for `SCREENSHOT_RESOLUTION`, `PDF_RESOLUTION`, and `CHROME_RESOLUTION`.

---
#### `CHECK_SSL_VALIDITY`
**Possible Values:** [`True`]/`False`
Whether to enforce HTTPS certificate and HSTS chain of trust when archiving sites.  Set this to `False` if you want to archive pages even if they have expired or invalid certificates.  Be aware that when `False` you cannot guarantee that you have not been man-in-the-middle'd while archiving content, so the content cannot be verified to be what's on the original site.

---
#### `USER_AGENT`
**Possible Values:** [`Mozilla/5.0 ... ArchiveBox/{VERSION} ...`]/`"Mozilla/5.0 ..."`/...
The default user agent string used during archiving. Individual extractors (wget, Chrome, curl, etc.) can override this with their own `*_USER_AGENT` settings, or fall back to this value.

---
#### `COOKIES_FILE`
**Possible Values:** [`None`]/`/path/to/cookies.txt`/...

Cookies file to pass to `wget`, `curl`, `yt-dlp` and other extractors that don't use Chrome (with its `CHROME_USER_DATA_DIR`) for authentication.  To capture sites that require a user to be logged in, you configure this option to point to a [netscape-format `cookies.txt`](http://www.cookiecentral.com/faq/#3.5) file containing all the cookies you want to use during archiving.

You can generate this `cookies.txt` file by using a number of different [browser extensions](https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc) that can export your cookies in this format, or by using `wget` on the command line with `--save-cookies` + `--user=... --password=...`.

Alternatively, you can create a persona and import cookies directly from your browser profile:

```bash
archivebox persona create --import=chrome personal
# supported: chrome/chromium/brave/edge (Chromium-based only)
# use --profile to target a specific profile (e.g. Default, Profile 1)
# re-running import merges/dedupes cookies.txt (by domain/path/name) but replaces chrome_user_data
```

> [!WARNING]
> **Make sure you use separate burner credentials dedicated to archiving,** e.g. don't re-use your normal daily Facebook/Instagram/Youtube/etc. account cookies as server responses often contain your name/email/PII, session tokens, etc. which then get preserved in your snapshots!

*Related options:*
[`CHROME_USER_DATA_DIR`](#chrome_user_data_dir), [`DEFAULT_PERSONA`](#default_persona)

---
#### `DEFAULT_PERSONA`
**Possible Values:** [`Default`]/`personal`/`work`/...
The persona profile to use by default when archiving. Personas allow you to have separate sets of cookies, Chrome profiles, and user agent strings for different archiving contexts.

```bash
archivebox persona create --import=chrome personal
archivebox config --set DEFAULT_PERSONA=personal
```

---

<a name="url_blacklist"/>

#### `URL_DENYLIST`
**Possible Values:** [`\.(css|js|otf|ttf|woff|woff2|gstatic\.com|googleapis\.com/css)(\?.*)?$`]/`.+\.exe$`/`http(s)?:\/\/(.+)?example.com\/.*`/...

A regex expression used to exclude certain URLs from archiving.  You can use if there are certain domains, extensions, or other URL patterns that you want to ignore whenever they get imported.  Blacklisted URLs wont be included in the index, and their page content wont be archived.

*Note: all assets required to render each page are still archived, `URL_DENYLIST`/`URL_ALLOWLIST` do not apply to images, css, video, etc. visible inline within the page.*

*Related options:*
[`URL_ALLOWLIST`](#URL_ALLOWLIST), [`SAVE_ALLOWLIST`](#SAVE_ALLOWLIST), [`SAVE_DENYLIST`](#SAVE_DENYLIST)

---

<a name="url_whitelist"/>

#### `URL_ALLOWLIST`
**Possible Values:** [`None`]/`^http(s)?:\/\/(.+)?example\.com\/?.*$`/...

A regex expression used to exclude all URLs that don't match the given pattern from archiving. Useful for **recursive archiving** of all the pages under a given domain or subfolder (aka crawling/spidering), without following links to external domains / parent folders.

```bash
export URL_ALLOWLIST='^http(s)?:\/\/(.+)?example\.com\/?.*$'
archivebox add --depth=1 'https://example.com'
```

*Related options:*
[`URL_DENYLIST`](#URL_DENYLIST), [`SAVE_ALLOWLIST`](#SAVE_ALLOWLIST), [`SAVE_DENYLIST`](#SAVE_DENYLIST)

---
#### `SAVE_ALLOWLIST`
**Possible Values:** [`{}`]/`{".*example\\.com.*": ["screenshot", "pdf"]}`/...
A JSON dictionary mapping URL regex patterns to lists of archive methods. Only the specified methods will be used for URLs matching each pattern. Useful for selectively archiving certain sites with only specific extractors.

---
#### `SAVE_DENYLIST`
**Possible Values:** [`{}`]/`{".*\\.pdf$": ["screenshot", "dom"]}`/...
A JSON dictionary mapping URL regex patterns to lists of archive methods to *skip*. Methods listed here will be skipped for URLs matching each pattern.

---
#### `TAG_SEPARATOR_PATTERN`
**Possible Values:** [`[,]`]/`[,;]`/...
Regex pattern used to split tag strings into individual tags. By default, only commas are used as tag separators.

---

## Server Settings

*Options for the web UI, authentication, and reverse proxy configuration.*

---

<a name="admin_username"/>
<a name="admin_password"/>

#### `ADMIN_USERNAME` / `ADMIN_PASSWORD`

**Possible Values:** [`None`]/`"admin"`/...

Only used on first run / initial setup in Docker. ArchiveBox will create an admin user with the specified username and password when these options are found in the environment.

Equivalent to:
```bash
$ archivebox manage createsuperuser
Username: <ADMIN_USERNAME>
Password: <ADMIN_PASSWORD>
```

More info:
- https://github.com/ArchiveBox/ArchiveBox/wiki/Setting-up-Authentication
- https://github.com/ArchiveBox/ArchiveBox/wiki/Docker#configuration

---

<a name="public_index"/>
<a name="public_snapshots"/>
<a name="public_add_view"/>

#### `PUBLIC_INDEX` / `PUBLIC_SNAPSHOTS` / `PUBLIC_ADD_VIEW`

**Possible Values:** [`True`]/`False`
Configure whether or not login is required to use each area of ArchiveBox.

```python3
archivebox manage createsuperuser  # set a password before disabling public access

# these are the default values
archivebox config --set PUBLIC_INDEX=True        # True = allow users to view main snapshots list without logging in
archivebox config --set PUBLIC_SNAPSHOTS=True    # True = allow users to view snapshot content without logging in
archivebox config --set PUBLIC_ADD_VIEW=False    # True = allow users to submit new URLs to archive without logging in
```

More info:
- https://github.com/ArchiveBox/ArchiveBox/wiki/Setting-up-Authentication

---
#### `SECRET_KEY`
**Possible Values:** *auto-generated random string*
Django's secret key for cryptographic signing (sessions, CSRF tokens, etc.). Automatically generated on first run. You should not need to change this unless you're running multiple ArchiveBox instances that need to share sessions.

---
#### `BIND_ADDR`
**Possible Values:** [`127.0.0.1:8000`]/`0.0.0.0:8000`/...
Address and port for the ArchiveBox web server to listen on.

```bash
archivebox config --set BIND_ADDR=0.0.0.0:8000    # listen on all interfaces
archivebox server                                   # starts on configured address
```

---
#### `LISTEN_HOST`
**Possible Values:** [`archivebox.localhost:8000`]/`archive.example.com:443`/...
The public hostname and port that ArchiveBox is accessible at. Used for generating absolute URLs in the web UI.

---
#### `ALLOWED_HOSTS`
**Possible Values:** [`*`]/`archive.example.com,localhost`/...
Comma-separated list of allowed HTTP Host header values. Set this to your domain name(s) in production for security. `*` allows all hosts (default, convenient for development).

---
#### `CSRF_TRUSTED_ORIGINS`
**Possible Values:** [`http://admin.archivebox.localhost:8000`]/`https://archive.example.com`/...
Comma-separated list of trusted origins for CSRF validation. Must include the scheme (http/https). Required when running behind a reverse proxy.

---
#### `ADMIN_BASE_URL`
**Possible Values:** [`""`]/`/admin/`/...
Base URL path for the Django admin interface. Leave empty to use the default.

---
#### `ARCHIVE_BASE_URL`
**Possible Values:** [`""`]/`/archive/`/...
Base URL path for serving archived content.

---
#### `SNAPSHOTS_PER_PAGE`
**Possible Values:** [`40`]/`100`/...
Maximum number of Snapshots to show per page on Snapshot list pages. Lower this value on slower machines to make the UI faster.

---
#### `PREVIEW_ORIGINALS`
**Possible Values:** [`True`]/`False`
Whether to show inline previews of the original URL on snapshot detail pages.

---
#### `FOOTER_INFO`
**Possible Values:** [`Content is hosted for personal archiving purposes only.  Contact server owner for any takedown requests.`]/`Operated by ACME Co.`/...
Some text to display in the footer of the archive index.  Useful for providing server admin contact info to respond to takedown requests.

---
#### `CUSTOM_TEMPLATES_DIR`
**Possible Values:** [`data/custom_templates`]/`/path/to/custom_templates`/...

Path to a directory containing custom html/css/images for overriding the default UI styling.  Files found in the folder at the specified path can override any of the defaults in the [`TEMPLATES_DIR`](https://github.com/ArchiveBox/ArchiveBox/tree/dev/archivebox/templates) directory.

If you've used `django` before, this works exactly the same way that `django` template overrides work.

---
#### `REVERSE_PROXY_USER_HEADER`
**Possible Values:** [`Remote-User`]/`X-Remote-User`/...

HTTP header containing user name from authenticated proxy.

More info:
- https://github.com/ArchiveBox/ArchiveBox/wiki/Setting-up-Authentication

*Related options:*
[`REVERSE_PROXY_WHITELIST`](#REVERSE_PROXY_WHITELIST), [`LOGOUT_REDIRECT_URL`](#LOGOUT_REDIRECT_URL)

---
#### `REVERSE_PROXY_WHITELIST`
**Possible Values:** [`<empty string>`],`172.16.0.0/16`,`2001:d80::/26`/...

Comma separated list of IP CIDRs which are allowed to use reverse proxy authentication. Both IPv4 and IPv6 IPs can be used next to each other. Empty string means "deny all".

*Related options:*
[`REVERSE_PROXY_USER_HEADER`](#REVERSE_PROXY_USER_HEADER), [`LOGOUT_REDIRECT_URL`](#LOGOUT_REDIRECT_URL)

---
#### `LOGOUT_REDIRECT_URL`
**Possible Values:** [`/`]/`https://example.com/some/other/app`/...

URL to redirect users back to on logout when using reverse proxy authentication.

---

## Storage Settings

*Options for file layout, permissions, and temp/lib directories.*

---
#### `OUTPUT_PERMISSIONS`
**Possible Values:** [`644`]/`755`/...
Permissions to set output files to. This is useful when running ArchiveBox inside Docker as root and you need to explicitly set the permissions to something that the users on the host can access.

*Related options:*
[`PUID` / `PGID`](#puid--pgid)

---

<a name="puid--pgid"/>
<a name="puid"/>
<a name="pgid"/>

#### `PUID` / `PGID`

**Possible Values:** [`911`]/`1000`/...

*Note: Only applicable for Docker users, settable via environment variables only.*
(not `ArchiveBox.conf` , `archivebox config --set ...`)

User and Group ID that the data directory should be owned by. We recommend leaving this as the default `911` and running `chown -R 911:$(id -g) ./data` outside Docker.

*Learn more:*
- https://docs.linuxserver.io/general/understanding-puid-and-pgid/
- https://github.com/ArchiveBox/ArchiveBox/wiki/Troubleshooting#docker-permissions-issues

---
#### `RESTRICT_FILE_NAMES`
**Possible Values:** [`windows`]/`unix`/`ascii`/...
Restrict output filenames to be compatible with the given filesystem type. `windows` (default) replaces characters that are invalid on Windows filesystems.

---
#### `ENFORCE_ATOMIC_WRITES`
**Possible Values:** [`True`]/`False`
Whether to use atomic writes when saving files. This ensures files are never left in a half-written state, but may be slower on some filesystems.

---
#### `TMP_DIR`
**Possible Values:** [`data/tmp/<machine_id>`]/`/tmp/archivebox/abc5d851`/...
Path for temporary files, unix sockets, and supervisor config. Must be a local, fast, readable/writable directory. Must have a short path due to unix socket path length restrictions (<100 chars). Must NOT be a network mount or FUSE filesystem.

ArchiveBox will try several fallback locations if the configured path is not usable.

---
#### `LIB_DIR`
**Possible Values:** [`data/lib/<arch>-<os>`]/`/usr/local/share/archivebox/abc5`/...
Path for installed binary dependencies (up to ~5GB). Must be local and fast for performance. Should not be a network mount.

---
#### `LIB_BIN_DIR`
**Possible Values:** [`LIB_DIR/bin`]
Path where installed binaries are symlinked for easy PATH management. Derived from `LIB_DIR / 'bin'`, prepended to PATH for all hook executions.

---

## Search Settings

*Options for full-text search backend configuration.*

---
#### `USE_INDEXING_BACKEND`
**Possible Values:** [`True`]/`False`
Enable the search indexing backend. When enabled, ArchiveBox will index archived content for full-text search.

---
#### `USE_SEARCHING_BACKEND`
**Possible Values:** [`True`]/`False`
Enable the search querying backend. When enabled, users can search through indexed content.

---
#### `SEARCH_BACKEND_ENGINE`
**Possible Values:** [`ripgrep`]/`sqlite`/`sonic`
Which search backend engine to use for full-text search.

- **`ripgrep`** (default): Uses ripgrep to search through files on disk. No extra setup required.
- **`sqlite`**: Uses SQLite FTS5 for full-text search. Stores index in a separate SQLite database.
- **`sonic`**: Uses a [Sonic](https://github.com/valeriansaliou/sonic) search server. Requires running a Sonic instance.

*Related options:*
[`RIPGREP_BINARY`](#ripgrep_binary), [`SEARCH_BACKEND_SONIC_*`](#search_backend_sonic_host_name)

---
#### `SEARCH_PROCESS_HTML`
**Possible Values:** [`True`]/`False`
Whether to strip HTML tags before indexing content for search. When `True`, only the text content is indexed.

---

## Archive Method Toggles

*High-level on/off switches for all the various methods used to archive URLs. In the new plugin architecture, each extractor has its own `*_ENABLED` toggle.*

---
#### `TITLE_ENABLED`
**Possible Values:** [`True`]/`False`
Extract the page title from the HTML `<title>` tag.

---
#### `FAVICON_ENABLED`
**Possible Values:** [`True`]/`False`
Fetch and save the favicon for each archived URL.

---
#### `WGET_ENABLED`
**Possible Values:** [`True`]/`False`
Fetch page with wget and save responses into folders for each domain, with support for page requisites (CSS, JS, images).

*Related options:*
[`WGET_WARC_ENABLED`](#wget_warc_enabled), [`WGET_TIMEOUT`](#wget_timeout), [`WGET_BINARY`](#wget_binary), [`WGET_ARGS`](#wget_args)

---
#### `WGET_WARC_ENABLED`
**Possible Values:** [`True`]/`False`
Save a timestamped WARC archive of all page requests and responses during the wget download.

---
#### `SCREENSHOT_ENABLED`
**Possible Values:** [`True`]/`False`
Capture a full-page screenshot using Chrome.

*Related options:*
[`SCREENSHOT_RESOLUTION`](#screenshot_resolution), [`SCREENSHOT_TIMEOUT`](#screenshot_timeout)

---
#### `PDF_ENABLED`
**Possible Values:** [`True`]/`False`
Print page as PDF using Chrome.

*Related options:*
[`PDF_RESOLUTION`](#pdf_resolution), [`PDF_TIMEOUT`](#pdf_timeout)

---
#### `DOM_ENABLED`
**Possible Values:** [`True`]/`False`
Capture a DOM snapshot of the page using Chrome.

---
#### `SINGLEFILE_ENABLED`
**Possible Values:** [`True`]/`False`
Fetch an HTML file with all assets embedded using [SingleFile](https://github.com/gildas-lormeau/SingleFile).

*Related options:*
[`SINGLEFILE_BINARY`](#singlefile_binary), [`SINGLEFILE_ARGS`](#singlefile_args), [`SINGLEFILE_TIMEOUT`](#singlefile_timeout)

---
#### `READABILITY_ENABLED`
**Possible Values:** [`True`]/`False`
Extract article text, summary, and byline using Mozilla's [Readability](https://github.com/mozilla/readability) library.

---
#### `MERCURY_ENABLED`
**Possible Values:** [`True`]/`False`
Extract article text, summary, and byline using the [Mercury](https://github.com/postlight/mercury-parser) parser.

---
#### `DEFUDDLE_ENABLED`
**Possible Values:** [`True`]/`False`
Extract article text using the [Defuddle](https://github.com/nicolo-ribaudo/defuddle) library, a newer alternative to Readability.

---
#### `HTMLTOTEXT_ENABLED`
**Possible Values:** [`True`]/`False`
Convert archived HTML pages to plain text.

---
#### `TRAFILATURA_ENABLED`
**Possible Values:** [`True`]/`False`
Extract article text using [Trafilatura](https://trafilatura.readthedocs.io/), a Python library for web text extraction. Can output in multiple formats (text, markdown, HTML, JSON, XML, CSV).

---
#### `GIT_ENABLED`
**Possible Values:** [`True`]/`False`
Clone any git repositories found on the page.

*Related options:*
[`GIT_DOMAINS`](#git_domains), [`GIT_BINARY`](#git_binary), [`GIT_ARGS`](#git_args)

---
#### `YTDLP_ENABLED`
**Possible Values:** [`True`]/`False`
Download audio, video, annotations, and media metadata using `yt-dlp`. Warning, this can use up *a lot* of storage very quickly.

*Related options:*
[`YTDLP_BINARY`](#ytdlp_binary), [`YTDLP_ARGS`](#ytdlp_args), [`YTDLP_MAX_SIZE`](#ytdlp_max_size)

---
#### `GALLERYDL_ENABLED`
**Possible Values:** [`True`]/`False`
Download image galleries using [gallery-dl](https://github.com/mikf/gallery-dl). Supports many image hosting sites.

---
#### `ARCHIVEDOTORG_ENABLED`
**Possible Values:** [`True`]/`False`
Submit the page's URL to be archived on Archive.org (The Internet Archive).

---
#### `CHROME_ENABLED`
**Possible Values:** [`True`]/`False`
Enable the Chrome/Chromium browser integration. This is required for screenshot, PDF, DOM, SingleFile, and many other extractors that depend on a browser.

---

#### Chrome Subextractor Toggles

These extractors run inside Chrome during the page load and capture additional metadata:

| Option | Default | Description |
|--------|---------|-------------|
| `DNS_ENABLED` | `True` | Record DNS queries during page load |
| `SSL_ENABLED` | `True` | Capture SSL certificate info |
| `HEADERS_ENABLED` | `True` | Capture HTTP response headers |
| `REDIRECTS_ENABLED` | `True` | Capture redirect chains |
| `RESPONSES_ENABLED` | `True` | Capture HTTP response bodies |
| `CONSOLELOG_ENABLED` | `True` | Capture browser console.log output |
| `ACCESSIBILITY_ENABLED` | `True` | Capture accessibility tree |
| `SEO_ENABLED` | `True` | Extract SEO metadata |
| `HASHES_ENABLED` | `True` | Generate merkle tree hashes of content |
| `STATICFILE_ENABLED` | `True` | Detect and directly download static file URLs |

#### Chrome Extension Toggles

| Option | Default | Description |
|--------|---------|-------------|
| `UBLOCK_ENABLED` | `True` | Enable uBlock Origin ad blocking extension |
| `ISTILLDONTCAREABOUTCOOKIES_ENABLED` | `True` | Enable cookie banner dismissal extension |
| `TWOCAPTCHA_ENABLED` | `True` | Enable 2captcha CAPTCHA solver extension |
| `MODALCLOSER_ENABLED` | `True` | Enable automatic modal/dialog closing |
| `INFINISCROLL_ENABLED` | `True` | Enable infinite scroll page expansion |

#### URL Parser Toggles

These post-process archived content to extract URLs for recursive crawling:

| Option | Default | Description |
|--------|---------|-------------|
| `PARSE_DOM_OUTLINKS_ENABLED` | `True` | Extract outlinks from DOM via CDP |
| `PARSE_HTML_URLS_ENABLED` | `True` | Parse URLs from HTML files |
| `PARSE_JSONL_URLS_ENABLED` | `True` | Parse URLs from JSONL files |
| `PARSE_NETSCAPE_URLS_ENABLED` | `True` | Parse Netscape bookmark format |
| `PARSE_TXT_URLS_ENABLED` | `True` | Parse URLs from plain text |
| `PARSE_RSS_URLS_ENABLED` | `True` | Parse URLs from RSS/Atom feeds |

---

## Archive Method Options

*Specific options for individual archive methods. Most extractors follow a naming convention: `PLUGINNAME_TIMEOUT`, `PLUGINNAME_ARGS`, `PLUGINNAME_BINARY`, etc.*

---

### Chrome Options

#### `CHROME_BINARY`
**Possible Values:** [`chromium`]/`/usr/local/bin/google-chrome`/...
Path or name of the Chrome/Chromium binary to use for all headless browser archive methods.

---
#### `CHROME_HEADLESS`
**Possible Values:** [`True`]/`False`
Whether to run Chrome in `--headless` mode. When `False`, the full Chrome UI will be launched each time.

---
#### `CHROME_SANDBOX`
**Possible Values:** [`True`]/`False`
Whether to use the Chrome sandbox. Only set to `False` if running inside a container or VM.

*Note: Do not run ArchiveBox as root! The solution is to create a non-root user, not to disable the sandbox.*

---
#### `CHROME_USER_DATA_DIR`
**Possible Values:** [`""`]/`~/.config/google-chrome`/`/tmp/chrome-profile`/...
Path to a Chrome user data directory for persistent sessions (cookies, logins). If not set, derived from the active persona's Chrome profile.

> [!WARNING]
> Use separate burner credentials dedicated to archiving. Don't re-use your normal daily accounts.

---
#### `CHROME_USER_AGENT`
**Possible Values:** [`""`] *(falls back to `USER_AGENT`)*
User agent string for Chrome. If empty, uses the global `USER_AGENT` setting.

---
#### `CHROME_TIMEOUT`
**Possible Values:** [`60`]/`120`/... *(falls back to `TIMEOUT`)*
Timeout for Chrome operations in seconds.

---
#### `CHROME_PAGELOAD_TIMEOUT`
**Possible Values:** [`60`]/`120`/... *(falls back to `CHROME_TIMEOUT`)*
Timeout specifically for page navigation/load in seconds.

---
#### `CHROME_RESOLUTION`
**Possible Values:** [`1440,2000`] *(falls back to `RESOLUTION`)*
Browser viewport resolution (width,height).

---
#### `CHROME_WAIT_FOR`
**Possible Values:** [`networkidle2`]/`domcontentloaded`/`load`/`networkidle0`
Puppeteer page load completion condition:
- `domcontentloaded`: Wait for DOMContentLoaded event
- `load`: Wait for load event
- `networkidle0`: No network connections for 500ms
- `networkidle2`: No more than 2 network connections for 500ms

---
#### `CHROME_DELAY_AFTER_LOAD`
**Possible Values:** [`0`]/`2`/`5`/...
Extra delay in seconds after page load completes before archiving. Useful for JS-heavy single page apps that need extra time to render.

---
#### `CHROME_ARGS`
**Possible Values:** *long list of default Chrome flags*
Default Chrome command-line arguments. These are carefully tuned for archiving — only override if you know what you're doing.

---
#### `CHROME_ARGS_EXTRA`
**Possible Values:** [`[]`]/`["--proxy-server=socks5://127.0.0.1:9050"]`/...
Extra arguments to append to the Chrome command. Use this instead of overriding `CHROME_ARGS` to add custom flags while keeping the defaults.

---

### Wget Options

#### `WGET_BINARY`
**Possible Values:** [`wget`]/`/usr/local/bin/wget`/...
Path or name of the wget binary.

---
#### `WGET_TIMEOUT`
**Possible Values:** [`60`] *(falls back to `TIMEOUT`)*
Timeout for wget operations in seconds.

---
#### `WGET_USER_AGENT`
**Possible Values:** [`""`] *(falls back to `USER_AGENT`)*
User agent string for wget.

---
#### `WGET_ARGS`
**Possible Values:** *default args for archiving*
Default wget arguments. Includes flags for page requisites, link conversion, and Windows-compatible filenames.

---
#### `WGET_ARGS_EXTRA`
**Possible Values:** [`[]`]/`["--limit-rate=1m"]`/...
Extra arguments to append to the wget command.

---

### SingleFile Options

#### `SINGLEFILE_BINARY`
**Possible Values:** [`single-file`]/`./node_modules/single-file/cli/single-file`/...
Path or name of the SingleFile binary.

---
#### `SINGLEFILE_TIMEOUT`
**Possible Values:** [`60`] *(falls back to `TIMEOUT`)*
Timeout for SingleFile in seconds.

---
#### `SINGLEFILE_ARGS` / `SINGLEFILE_ARGS_EXTRA`
**Possible Values:** [`["--browser-headless"]`]/...
Default and extra arguments for SingleFile.

---

### yt-dlp Options

#### `YTDLP_BINARY`
**Possible Values:** [`yt-dlp`]/`/usr/local/bin/yt-dlp`/...
Path or name of the yt-dlp binary (replacement for youtube-dl).

---
#### `YTDLP_TIMEOUT`
**Possible Values:** [`3600`] *(falls back to `TIMEOUT`)*
Timeout for yt-dlp downloads in seconds. Default is 1 hour since media downloads can be large.

---
#### `YTDLP_MAX_SIZE`
**Possible Values:** [`750m`]/`2g`/...
Maximum file size for yt-dlp downloads.

---
#### `YTDLP_ARGS` / `YTDLP_ARGS_EXTRA`
Default and extra arguments for yt-dlp. The defaults include options for subtitles, thumbnails, metadata, etc.

---

### Git Options

#### `GIT_BINARY`
**Possible Values:** [`git`]/`/usr/local/bin/git`/...
Path or name of the git binary.

---
#### `GIT_DOMAINS`
**Possible Values:** [`github.com,gitlab.com,bitbucket.org,gist.github.com,codeberg.org,gitea.com,git.sr.ht`]/`git.example.com`/...
Comma-separated list of domains to attempt `git clone` on.

---
#### `GIT_ARGS` / `GIT_ARGS_EXTRA`
**Possible Values:** [`["clone", "--depth=1", "--recursive"]`]/...
Default and extra arguments for git operations.

---

### Other Extractor Options

#### `READABILITY_BINARY`
**Possible Values:** [`readability-extractor`]/...
Path to the Readability extractor binary.

---
#### `MERCURY_BINARY`
**Possible Values:** [`postlight-parser`]/...
Path to the Mercury/Postlight parser binary.

---
#### `DEFUDDLE_BINARY`
**Possible Values:** [`defuddle`]/...
Path to the Defuddle binary.

---
#### `TRAFILATURA_BINARY`
**Possible Values:** [`trafilatura`]/...
Path to the Trafilatura binary.

---
#### `RIPGREP_BINARY`
**Possible Values:** [`rg`]/`rga`/...
Path or name of the ripgrep binary for full-text search.

---

### Search Backend Options

<a name="search_backend_sonic_host_name"/>

#### Sonic Search Backend

When using `SEARCH_BACKEND_ENGINE=sonic`:

| Option | Default | Description |
|--------|---------|-------------|
| `SEARCH_BACKEND_SONIC_HOST_NAME` | `127.0.0.1` | Sonic server hostname |
| `SEARCH_BACKEND_SONIC_PORT` | `1491` | Sonic server port |
| `SEARCH_BACKEND_SONIC_PASSWORD` | `SecretPassword` | Sonic server password |
| `SEARCH_BACKEND_SONIC_COLLECTION` | `archivebox` | Sonic collection name |
| `SEARCH_BACKEND_SONIC_BUCKET` | `snapshots` | Sonic bucket name |

#### SQLite FTS Search Backend

When using `SEARCH_BACKEND_ENGINE=sqlite`:

| Option | Default | Description |
|--------|---------|-------------|
| `SEARCH_BACKEND_SQLITE_DB` | `search.sqlite3` | FTS database filename |
| `SEARCH_BACKEND_SQLITE_SEPARATE_DATABASE` | `True` | Use separate DB file for FTS |
| `SEARCH_BACKEND_SQLITE_TOKENIZERS` | `porter unicode61 remove_diacritics 2` | FTS5 tokenizer config |

---

### Infinite Scroll Options

| Option | Default | Description |
|--------|---------|-------------|
| `INFINISCROLL_SCROLL_LIMIT` | `10` | Maximum number of scroll steps |
| `INFINISCROLL_SCROLL_DISTANCE` | `1600` | Distance per scroll step (px) |
| `INFINISCROLL_SCROLL_DELAY` | `2000` | Delay between scrolls (ms) |
| `INFINISCROLL_MIN_HEIGHT` | `16000` | Minimum page height to scroll to (px) |
| `INFINISCROLL_EXPAND_DETAILS` | `True` | Expand `<details>` elements and click "load more" buttons |
| `INFINISCROLL_TIMEOUT` | `120` | Maximum timeout (falls back to `TIMEOUT`) |

---

### 2captcha Options

| Option | Default | Description |
|--------|---------|-------------|
| `TWOCAPTCHA_API_KEY` | `""` | 2captcha API key (get from https://2captcha.com) |
| `TWOCAPTCHA_AUTO_SUBMIT` | `False` | Auto-submit forms after solving |
| `TWOCAPTCHA_RETRY_COUNT` | `3` | Number of solving retries |
| `TWOCAPTCHA_RETRY_DELAY` | `5` | Delay between retries (seconds) |
| `TWOCAPTCHA_TIMEOUT` | `60` | Solving timeout (falls back to `TIMEOUT`) |

---

### Modal Closer Options

| Option | Default | Description |
|--------|---------|-------------|
| `MODALCLOSER_POLL_INTERVAL` | `500` | How often to check for CSS modals (ms) |
| `MODALCLOSER_TIMEOUT` | `1250` | Delay before auto-closing dialogs (ms) |

---

## Shell Options

*Options around the format of the CLI output.*

---
#### `DEBUG`
**Possible Values:** [`False`]/`True`
Enable debug mode. Automatically set to `True` if `--debug` is passed on the command line.

---
#### `IS_TTY`
**Possible Values:** *auto-detected*
Whether stdout is a TTY (interactive terminal). Auto-detected, but can be overridden.

---
#### `USE_COLOR`
**Possible Values:** [`True`]/`False`
Colorize console output. Defaults to `True` if stdin is a TTY (interactive session), otherwise `False`.

---
#### `SHOW_PROGRESS`
**Possible Values:** [`True`]/`False`
Show real-time progress bar in console output. Defaults to `True` if stdin is a TTY (interactive session), otherwise `False`.

---
#### `IN_DOCKER`
**Possible Values:** [`False`]/`True`
Whether ArchiveBox is running inside a Docker container. Auto-detected from the `IN_DOCKER` environment variable.

---
#### `IN_QEMU`
**Possible Values:** [`False`]/`True`
Whether ArchiveBox is running inside QEMU emulation. This may affect performance expectations.

---

## LDAP Settings

*Options for LDAP/Active Directory authentication. Requires `pip install archivebox[ldap]`.*

---
#### `LDAP_ENABLED`
**Possible Values:** [`False`]/`True`

Whether to use an external [LDAP](https://jumpcloud.com/blog/what-is-ldap-authentication) server for authentication (e.g. OpenLDAP, MS Active Directory, OpenDJ, etc.).

```bash
pip install archivebox[ldap]
```

Then set these configuration values:
```yaml
LDAP_ENABLED: True
LDAP_SERVER_URI: "ldap://ldap.example.com:3389"
LDAP_BIND_DN: "ou=archivebox,ou=services,dc=ldap.example.com"
LDAP_BIND_PASSWORD: "secret-bind-user-password"
LDAP_USER_BASE: "ou=users,ou=archivebox,ou=services,dc=ldap.example.com"
LDAP_USER_FILTER: "(uid=%(user)s)"

LDAP_USERNAME_ATTR: "username"
LDAP_FIRSTNAME_ATTR: "givenName"
LDAP_LASTNAME_ATTR: "sn"
LDAP_EMAIL_ATTR: "mail"
LDAP_CREATE_SUPERUSER: False
```

| Option | Default | Description |
|--------|---------|-------------|
| `LDAP_ENABLED` | `False` | Enable LDAP authentication |
| `LDAP_SERVER_URI` | `None` | LDAP server URI (e.g. `ldap://ldap.example.com:389`) |
| `LDAP_BIND_DN` | `None` | DN to bind for searching |
| `LDAP_BIND_PASSWORD` | `None` | Password for bind DN |
| `LDAP_USER_BASE` | `None` | Base DN for user searches |
| `LDAP_USER_FILTER` | `(uid=%(user)s)` | LDAP search filter for users |
| `LDAP_USERNAME_ATTR` | `username` | LDAP attribute for username |
| `LDAP_FIRSTNAME_ATTR` | `givenName` | LDAP attribute for first name |
| `LDAP_LASTNAME_ATTR` | `sn` | LDAP attribute for last name |
| `LDAP_EMAIL_ATTR` | `mail` | LDAP attribute for email |
| `LDAP_CREATE_SUPERUSER` | `False` | Auto-create superuser accounts for LDAP users |

More info:
- https://github.com/ArchiveBox/ArchiveBox/wiki/Setting-up-Authentication
- https://github.com/django-auth-ldap/django-auth-ldap#example-configuration

---

## Plugin Settings

ArchiveBox uses a plugin system where each extractor defines its own configuration via `config.json` files. Plugin config options follow a consistent naming convention:

- **`PLUGINNAME_ENABLED`**: Enable/disable the plugin (`True`/`False`)
- **`PLUGINNAME_TIMEOUT`**: Timeout in seconds (usually falls back to global `TIMEOUT`)
- **`PLUGINNAME_BINARY`**: Path to the plugin's binary dependency
- **`PLUGINNAME_ARGS`**: Default command-line arguments (JSON array)
- **`PLUGINNAME_ARGS_EXTRA`**: Extra arguments to append (JSON array)

All plugin config options can be set the same way as core options — via environment variables, `ArchiveBox.conf`, or `archivebox config --set`.

To see all available plugin config options for your installation:
```bash
archivebox config
```

For the full list of plugins and their config schemas, see the [abx-plugins repository](https://github.com/ArchiveBox/abx-plugins).


<img src="https://github.com/ArchiveBox/ArchiveBox/assets/511499/5a4dd576-387a-4a1f-9dfa-407eac87078c" width="100%"/>
