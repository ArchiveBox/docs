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
 - [Server Settings:](#server-settings) Web UI, authentication, and reverse proxy options.
 - [Storage Settings:](#storage-settings) File layout, permissions, and temp directories.
 - [Search Settings:](#search-settings) Full-text search backend configuration.
 - [Shell Options:](#shell-options) Format & behavior of CLI output.
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
```

> [!WARNING]
> **Make sure you use separate burner credentials dedicated to archiving,** e.g. don't re-use your normal daily Facebook/Instagram/Youtube/etc. account cookies as server responses often contain your name/email/PII, session tokens, etc. which then get preserved in your snapshots!

*Related options:*
[`CHROME_USER_DATA_DIR`](#chrome_user_data_dir), [`DEFAULT_PERSONA`](#default_persona)

---
#### `DEFAULT_PERSONA`
**Possible Values:** [`Default`]/`personal`/`work`/...
The persona profile to use by default when archiving. Personas allow you to have separate sets of cookies, Chrome profiles, and user agent strings for different archiving contexts.

---
#### `URL_DENYLIST`
**Possible Values:** [`\.(css|js|otf|ttf|woff|woff2|gstatic\.com|googleapis\.com/css)(\?.*)?$`]/`.+\.exe$`/...

A regex expression used to exclude certain URLs from archiving.

*Related options:*
[`URL_ALLOWLIST`](#url_allowlist), [`SAVE_ALLOWLIST`](#save_allowlist), [`SAVE_DENYLIST`](#save_denylist)

---
#### `URL_ALLOWLIST`
**Possible Values:** [`None`]/`^http(s)?:\/\/(.+)?example\.com\/?.*$`/...

A regex expression used to exclude all URLs that don't match the given pattern from archiving. Useful for recursive crawling within a single domain.

---
#### `SAVE_ALLOWLIST`
**Possible Values:** [`{}`]/`{".*example\\.com.*": ["screenshot", "pdf"]}`/...
A JSON dictionary mapping URL regex patterns to lists of archive methods. Only the specified methods will be used for URLs matching each pattern.

---
#### `SAVE_DENYLIST`
**Possible Values:** [`{}`]/`{".*\\.pdf$": ["screenshot", "dom"]}`/...
A JSON dictionary mapping URL regex patterns to lists of archive methods to *skip*.

---
#### `TAG_SEPARATOR_PATTERN`
**Possible Values:** [`[,]`]/`[,;]`/...
Regex pattern used to split tag strings into individual tags.

---

## Server Settings

*Options for the web UI, authentication, and reverse proxy configuration.*

---
#### `ADMIN_USERNAME` / `ADMIN_PASSWORD`
**Possible Values:** [`None`]/`"admin"`/...

Only used on first run / initial setup in Docker. ArchiveBox will create an admin user with the specified username and password when these options are found in the environment.

More info:
- https://github.com/ArchiveBox/ArchiveBox/wiki/Setting-up-Authentication

---
#### `PUBLIC_INDEX` / `PUBLIC_SNAPSHOTS` / `PUBLIC_ADD_VIEW`
**Possible Values:** [`True`]/`False`
Configure whether or not login is required to use each area of ArchiveBox.

```bash
archivebox config --set PUBLIC_INDEX=True        # allow viewing snapshots list without login
archivebox config --set PUBLIC_SNAPSHOTS=True    # allow viewing snapshot content without login
archivebox config --set PUBLIC_ADD_VIEW=False    # allow submitting new URLs without login
```

---
#### `SECRET_KEY`
**Possible Values:** *auto-generated random string*
Django's secret key for cryptographic signing (sessions, CSRF tokens, etc.). Automatically generated on first run.

---
#### `BIND_ADDR`
**Possible Values:** [`127.0.0.1:8000`]/`0.0.0.0:8000`/...
Address and port for the ArchiveBox web server to listen on.

---
#### `LISTEN_HOST`
**Possible Values:** [`archivebox.localhost:8000`]/`archive.example.com:443`/...
The public hostname and port that ArchiveBox is accessible at.

---
#### `ALLOWED_HOSTS`
**Possible Values:** [`*`]/`archive.example.com,localhost`/...
Comma-separated list of allowed HTTP Host header values. Set this to your domain name(s) in production.

---
#### `CSRF_TRUSTED_ORIGINS`
**Possible Values:** [`http://admin.archivebox.localhost:8000`]/`https://archive.example.com`/...
Comma-separated list of trusted origins for CSRF validation. Must include the scheme (http/https).

---
#### `ADMIN_BASE_URL`
**Possible Values:** [`""`]/`/admin/`/...
Base URL path for the Django admin interface.

---
#### `ARCHIVE_BASE_URL`
**Possible Values:** [`""`]/`/archive/`/...
Base URL path for serving archived content.

---
#### `SNAPSHOTS_PER_PAGE`
**Possible Values:** [`40`]/`100`/...
Maximum number of Snapshots to show per page on Snapshot list pages.

---
#### `PREVIEW_ORIGINALS`
**Possible Values:** [`True`]/`False`
Whether to show inline previews of the original URL on snapshot detail pages.

---
#### `FOOTER_INFO`
**Possible Values:** [`Content is hosted for personal archiving purposes only.  Contact server owner for any takedown requests.`]/...
Text to display in the footer of the archive index.

---
#### `CUSTOM_TEMPLATES_DIR`
**Possible Values:** [`data/custom_templates`]/`/path/to/custom_templates`/...
Path to a directory containing custom html/css/images for overriding the default UI styling.

---
#### `REVERSE_PROXY_USER_HEADER`
**Possible Values:** [`Remote-User`]/`X-Remote-User`/...
HTTP header containing user name from authenticated proxy.

*Related options:*
[`REVERSE_PROXY_WHITELIST`](#reverse_proxy_whitelist), [`LOGOUT_REDIRECT_URL`](#logout_redirect_url)

---
#### `REVERSE_PROXY_WHITELIST`
**Possible Values:** [`<empty string>`]/`172.16.0.0/16`/...
Comma separated list of IP CIDRs which are allowed to use reverse proxy authentication.

---
#### `LOGOUT_REDIRECT_URL`
**Possible Values:** [`/`]/`https://example.com/some/other/app`/...
URL to redirect users back to on logout when using reverse proxy authentication.

---

### LDAP Settings

*Options for LDAP/Active Directory authentication. Requires `pip install archivebox[ldap]`.*

---
#### `LDAP_ENABLED`
**Possible Values:** [`False`]/`True`
Whether to use an external LDAP server for authentication.

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

More info:
- https://github.com/ArchiveBox/ArchiveBox/wiki/Setting-up-Authentication
- https://github.com/django-auth-ldap/django-auth-ldap#example-configuration

---
#### `LDAP_SERVER_URI`
**Default:** [`None`]
LDAP server URI (e.g. `ldap://ldap.example.com:389`).

---
#### `LDAP_BIND_DN`
**Default:** [`None`]
DN to bind for searching.

---
#### `LDAP_BIND_PASSWORD`
**Default:** [`None`]
Password for bind DN.

---
#### `LDAP_USER_BASE`
**Default:** [`None`]
Base DN for user searches.

---
#### `LDAP_USER_FILTER`
**Default:** [`(uid=%(user)s)`]
LDAP search filter for users.

---
#### `LDAP_USERNAME_ATTR`
**Default:** [`username`]
LDAP attribute for username.

---
#### `LDAP_FIRSTNAME_ATTR`
**Default:** [`givenName`]
LDAP attribute for first name.

---
#### `LDAP_LASTNAME_ATTR`
**Default:** [`sn`]
LDAP attribute for last name.

---
#### `LDAP_EMAIL_ATTR`
**Default:** [`mail`]
LDAP attribute for email.

---
#### `LDAP_CREATE_SUPERUSER`
**Default:** [`False`]
Auto-create superuser accounts for LDAP users.

---

## Storage Settings

*Options for file layout, permissions, and temp/lib directories.*

---
#### `OUTPUT_PERMISSIONS`
**Possible Values:** [`644`]/`755`/...
Permissions to set output files to.

*Related options:*
[`PUID` / `PGID`](#puid--pgid)

---
#### `PUID` / `PGID`
**Possible Values:** [`911`]/`1000`/...
*Note: Only applicable for Docker users, settable via environment variables only.*
User and Group ID that the data directory should be owned by.

*Learn more:*
- https://docs.linuxserver.io/general/understanding-puid-and-pgid/
- https://github.com/ArchiveBox/ArchiveBox/wiki/Troubleshooting#docker-permissions-issues

---
#### `RESTRICT_FILE_NAMES`
**Possible Values:** [`windows`]/`unix`/`ascii`/...
Restrict output filenames to be compatible with the given filesystem type.

---
#### `ENFORCE_ATOMIC_WRITES`
**Possible Values:** [`True`]/`False`
Whether to use atomic writes when saving files.

---
#### `TMP_DIR`
**Possible Values:** [`data/tmp/<machine_id>`]/`/tmp/archivebox/abc5d851`/...
Path for temporary files, unix sockets, and supervisor config. Must be a local, fast, short-path directory.

---
#### `LIB_DIR`
**Possible Values:** [`data/lib/<arch>-<os>`]/`/usr/local/share/archivebox/abc5`/...
Path for installed binary dependencies.

---
#### `LIB_BIN_DIR`
**Possible Values:** [`LIB_DIR/bin`]
Path where installed binaries are symlinked for easy PATH management.

---

## Search Settings

*Options for full-text search backend configuration.*

---
#### `USE_INDEXING_BACKEND`
**Possible Values:** [`True`]/`False`
Enable the search indexing backend.

---
#### `USE_SEARCHING_BACKEND`
**Possible Values:** [`True`]/`False`
Enable the search querying backend.

---
#### `SEARCH_BACKEND_ENGINE`
**Possible Values:** [`ripgrep`]/`sqlite`/`sonic`
Which search backend engine to use. `ripgrep` (default) requires no setup. `sqlite` uses FTS5. `sonic` requires a running Sonic instance.

---
#### `SEARCH_PROCESS_HTML`
**Possible Values:** [`True`]/`False`
Whether to strip HTML tags before indexing content for search.

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
Whether stdout is a TTY (interactive terminal).

---
#### `USE_COLOR`
**Possible Values:** [`True`]/`False`
Colorize console output. Defaults to `True` if stdin is a TTY.

---
#### `SHOW_PROGRESS`
**Possible Values:** [`True`]/`False`
Show real-time progress bar in console output. Defaults to `True` if stdin is a TTY.

---
#### `IN_DOCKER`
**Possible Values:** [`False`]/`True`
Whether ArchiveBox is running inside a Docker container.

---
#### `IN_QEMU`
**Possible Values:** [`False`]/`True`
Whether ArchiveBox is running inside QEMU emulation.

---

## Plugin Settings

ArchiveBox uses a plugin system where each extractor defines its own configuration via `config.json` files. All plugin config options can be set the same way as core options — via environment variables, `ArchiveBox.conf`, or `archivebox config --set`.

```bash
archivebox config                              # see all available config options
archivebox config --set SCREENSHOT_TIMEOUT=120  # set a plugin option
```

For the full list of plugins and their config schemas, see the [abx-plugins repository](https://github.com/ArchiveBox/abx-plugins).

### Title Settings

#### `TITLE_ENABLED`
**Default:** [`True`]
Enable title extraction

---
#### `TITLE_TIMEOUT`
**Default:** [`30`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for title extraction in seconds


### Favicon Settings

#### `FAVICON_ENABLED`
**Default:** [`True`]
Enable favicon downloading

---
#### `FAVICON_TIMEOUT`
**Default:** [`30`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for favicon fetch in seconds

---
#### `FAVICON_USER_AGENT`
**Default:** [`""`] *(falls back to [`USER_AGENT`](#user_agent))*
User agent string


### Wget Settings

#### `WGET_ARGS`
**Default:** [*see defaults*]
Default wget arguments

---
#### `WGET_ARGS_EXTRA`
**Default:** [`[]`]
Extra arguments to append to wget command

---
#### `WGET_BINARY`
**Default:** [`wget`]
Path to wget binary

---
#### `WGET_CHECK_SSL_VALIDITY`
**Default:** [`True`] *(falls back to [`CHECK_SSL_VALIDITY`](#check_ssl_validity))*
Whether to verify SSL certificates

---
#### `WGET_COOKIES_FILE`
**Default:** [`""`] *(falls back to [`COOKIES_FILE`](#cookies_file))*
Path to cookies file

---
#### `WGET_ENABLED`
**Default:** [`True`]
Enable wget archiving

---
#### `WGET_TIMEOUT`
**Default:** [`60`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for wget in seconds

---
#### `WGET_USER_AGENT`
**Default:** [`""`] *(falls back to [`USER_AGENT`](#user_agent))*
User agent string for wget

---
#### `WGET_WARC_ENABLED`
**Default:** [`True`]
Save WARC archive file


### Screenshot Settings

#### `SCREENSHOT_ENABLED`
**Default:** [`True`]
Enable screenshot capture

---
#### `SCREENSHOT_RESOLUTION`
**Default:** [`1440,2000`] *(falls back to [`RESOLUTION`](#resolution))*
Screenshot resolution (width,height)

---
#### `SCREENSHOT_TIMEOUT`
**Default:** [`60`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for screenshot capture in seconds


### PDF Settings

#### `PDF_ENABLED`
**Default:** [`True`]
Enable PDF generation

---
#### `PDF_RESOLUTION`
**Default:** [`1440,2000`] *(falls back to [`RESOLUTION`](#resolution))*
PDF page resolution (width,height)

---
#### `PDF_TIMEOUT`
**Default:** [`60`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for PDF generation in seconds


### DOM Settings

#### `DOM_ENABLED`
**Default:** [`True`]
Enable DOM capture

---
#### `DOM_TIMEOUT`
**Default:** [`60`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for DOM capture in seconds


### SingleFile Settings

#### `SINGLEFILE_ARGS`
**Default:** [`['--browser-headless']`]
Default single-file arguments

---
#### `SINGLEFILE_ARGS_EXTRA`
**Default:** [`[]`]
Extra arguments to append to single-file command

---
#### `SINGLEFILE_BINARY`
**Default:** [`single-file`]
Path to single-file binary

---
#### `SINGLEFILE_CHECK_SSL_VALIDITY`
**Default:** [`True`] *(falls back to [`CHECK_SSL_VALIDITY`](#check_ssl_validity))*
Whether to verify SSL certificates

---
#### `SINGLEFILE_CHROME_ARGS`
**Default:** [`[]`] *(falls back to [`CHROME_ARGS`](#chrome_args))*
Chrome command-line arguments for SingleFile

#### `SINGLEFILE_COOKIES_FILE`
**Default:** [`""`] *(falls back to [`COOKIES_FILE`](#cookies_file))*
Path to cookies file

---
#### `SINGLEFILE_ENABLED`
**Default:** [`True`]
Enable SingleFile archiving

#### `SINGLEFILE_TIMEOUT`
**Default:** [`60`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for SingleFile in seconds

---
#### `SINGLEFILE_USER_AGENT`
**Default:** [`""`] *(falls back to [`USER_AGENT`](#user_agent))*
User agent string


### Readability Settings

#### `READABILITY_ARGS`
**Default:** [`[]`]
Default Readability arguments

---
#### `READABILITY_ARGS_EXTRA`
**Default:** [`[]`]
Extra arguments to append to Readability command

---
#### `READABILITY_BINARY`
**Default:** [`readability-extractor`]
Path to readability-extractor binary

---
#### `READABILITY_ENABLED`
**Default:** [`True`]
Enable Readability text extraction

---
#### `READABILITY_TIMEOUT`
**Default:** [`30`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for Readability in seconds


### Mercury Settings

#### `MERCURY_ARGS`
**Default:** [`[]`]
Default Mercury parser arguments

---
#### `MERCURY_ARGS_EXTRA`
**Default:** [`[]`]
Extra arguments to append to Mercury parser command

---
#### `MERCURY_BINARY`
**Default:** [`postlight-parser`]
Path to Mercury/Postlight parser binary

---
#### `MERCURY_ENABLED`
**Default:** [`True`]
Enable Mercury text extraction

---
#### `MERCURY_TIMEOUT`
**Default:** [`30`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for Mercury in seconds


### Defuddle Settings

#### `DEFUDDLE_ARGS`
**Default:** [`[]`]
Default Defuddle arguments

---
#### `DEFUDDLE_ARGS_EXTRA`
**Default:** [`[]`]
Extra arguments to append to Defuddle command

---
#### `DEFUDDLE_BINARY`
**Default:** [`defuddle`]
Path to defuddle binary

---
#### `DEFUDDLE_ENABLED`
**Default:** [`True`]
Enable Defuddle text extraction

---
#### `DEFUDDLE_TIMEOUT`
**Default:** [`30`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for Defuddle in seconds


### HTML to Text Settings

#### `HTMLTOTEXT_ENABLED`
**Default:** [`True`]
Enable HTML to text conversion

---
#### `HTMLTOTEXT_TIMEOUT`
**Default:** [`30`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for HTML to text conversion in seconds


### Trafilatura Settings

#### `TRAFILATURA_BINARY`
**Default:** [`trafilatura`]
Path to trafilatura binary

---
#### `TRAFILATURA_ENABLED`
**Default:** [`True`]
Enable Trafilatura extraction

---
#### `TRAFILATURA_OUTPUT_CSV`
**Default:** [`False`]
Write CSV output (content.csv)

---
#### `TRAFILATURA_OUTPUT_HTML`
**Default:** [`True`]
Write HTML output (content.html)

---
#### `TRAFILATURA_OUTPUT_JSON`
**Default:** [`False`]
Write JSON output (content.json)

---
#### `TRAFILATURA_OUTPUT_MARKDOWN`
**Default:** [`True`]
Write markdown output (content.md)

---
#### `TRAFILATURA_OUTPUT_TXT`
**Default:** [`True`]
Write plain text output (content.txt)

---
#### `TRAFILATURA_OUTPUT_XML`
**Default:** [`False`]
Write XML output (content.xml)

---
#### `TRAFILATURA_OUTPUT_XMLTEI`
**Default:** [`False`]
Write XML TEI output (content.xmltei)

---
#### `TRAFILATURA_TIMEOUT`
**Default:** [`30`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for Trafilatura in seconds


### Git Settings

#### `GIT_ARGS`
**Default:** [`['clone', '--depth=1', '--recursive']`]
Default git arguments

---
#### `GIT_ARGS_EXTRA`
**Default:** [`[]`]
Extra arguments to append to git command

---
#### `GIT_BINARY`
**Default:** [`git`]
Path to git binary

---
#### `GIT_DOMAINS`
**Default:** [*see defaults*]
Comma-separated list of domains to treat as git repositories

---
#### `GIT_ENABLED`
**Default:** [`True`]
Enable git repository cloning

---
#### `GIT_TIMEOUT`
**Default:** [`120`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for git operations in seconds


### yt-dlp Settings

#### `YTDLP_ARGS`
**Default:** [*see defaults*]
Default yt-dlp arguments

---
#### `YTDLP_ARGS_EXTRA`
**Default:** [`[]`]
Extra arguments to append to yt-dlp command

---
#### `YTDLP_BINARY`
**Default:** [`yt-dlp`]
Path to yt-dlp binary

---
#### `YTDLP_CHECK_SSL_VALIDITY`
**Default:** [`True`] *(falls back to [`CHECK_SSL_VALIDITY`](#check_ssl_validity))*
Whether to verify SSL certificates

---
#### `YTDLP_COOKIES_FILE`
**Default:** [`""`] *(falls back to [`COOKIES_FILE`](#cookies_file))*
Path to cookies file

---
#### `YTDLP_ENABLED`
**Default:** [`True`]
Enable video/audio downloading with yt-dlp

---
#### `YTDLP_MAX_SIZE`
**Default:** [`750m`]
Maximum file size for yt-dlp downloads

#### `YTDLP_TIMEOUT`
**Default:** [`3600`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for yt-dlp downloads in seconds


### gallery-dl Settings

#### `GALLERYDL_ARGS`
**Default:** [`['--write-metadata', '--write-info-json']`]
Default gallery-dl arguments

---
#### `GALLERYDL_ARGS_EXTRA`
**Default:** [`[]`]
Extra arguments to append to gallery-dl command

---
#### `GALLERYDL_BINARY`
**Default:** [`gallery-dl`]
Path to gallery-dl binary

---
#### `GALLERYDL_CHECK_SSL_VALIDITY`
**Default:** [`True`] *(falls back to [`CHECK_SSL_VALIDITY`](#check_ssl_validity))*
Whether to verify SSL certificates

---
#### `GALLERYDL_COOKIES_FILE`
**Default:** [`""`] *(falls back to [`COOKIES_FILE`](#cookies_file))*
Path to cookies file

---
#### `GALLERYDL_ENABLED`
**Default:** [`True`]
Enable gallery downloading with gallery-dl

---
#### `GALLERYDL_TIMEOUT`
**Default:** [`3600`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for gallery downloads in seconds


### forum-dl Settings

#### `FORUMDL_ARGS`
**Default:** [`[]`]
Default forum-dl arguments

---
#### `FORUMDL_ARGS_EXTRA`
**Default:** [`[]`]
Extra arguments to append to forum-dl command

---
#### `FORUMDL_BINARY`
**Default:** [`forum-dl`]
Path to forum-dl binary

---
#### `FORUMDL_ENABLED`
**Default:** [`True`]
Enable forum downloading with forum-dl

---
#### `FORUMDL_OUTPUT_FORMAT`
**Default:** [`jsonl`]
Output format for forum downloads

---
#### `FORUMDL_TIMEOUT`
**Default:** [`3600`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for forum downloads in seconds


### papers-dl Settings

#### `PAPERSDL_ARGS`
**Default:** [`['fetch']`]
Default papers-dl arguments

---
#### `PAPERSDL_ARGS_EXTRA`
**Default:** [`[]`]
Extra arguments to append to papers-dl command

---
#### `PAPERSDL_BINARY`
**Default:** [`papers-dl`]
Path to papers-dl binary

---
#### `PAPERSDL_ENABLED`
**Default:** [`True`]
Enable paper downloading with papers-dl

---
#### `PAPERSDL_TIMEOUT`
**Default:** [`300`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for paper downloads in seconds


### Archive.org Settings

#### `ARCHIVEDOTORG_ENABLED`
**Default:** [`True`]
Submit URLs to archive.org Wayback Machine

---
#### `ARCHIVEDOTORG_TIMEOUT`
**Default:** [`60`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for archive.org submission in seconds

---
#### `ARCHIVEDOTORG_USER_AGENT`
**Default:** [`""`] *(falls back to [`USER_AGENT`](#user_agent))*
User agent string


### Chrome Settings

#### `CHROME_ARGS`
**Default:** [*see defaults*]
Default Chrome command-line arguments (static flags only, dynamic args like --user-data-dir are added at runtime)

---
#### `CHROME_ARGS_EXTRA`
**Default:** [`[]`]
Extra arguments to append to Chrome command (for user customization)

---
#### `CHROME_BINARY`
**Default:** [`chromium`]
Path to Chromium binary

---
#### `CHROME_CHECK_SSL_VALIDITY`
**Default:** [`True`] *(falls back to [`CHECK_SSL_VALIDITY`](#check_ssl_validity))*
Whether to verify SSL certificates (disable for self-signed certs)

---
#### `CHROME_DELAY_AFTER_LOAD`
**Default:** [`0`]
Extra delay in seconds after page load completes before archiving (useful for JS-heavy SPAs)

---
#### `CHROME_ENABLED`
**Default:** [`True`]
Enable Chromium browser integration for archiving

---
#### `CHROME_HEADLESS`
**Default:** [`True`]
Run Chrome in headless mode

#### `CHROME_PAGELOAD_TIMEOUT`
**Default:** [`60`] *(falls back to [`CHROME_TIMEOUT`](#chrome_timeout))*
Timeout for page navigation/load in seconds

---
#### `CHROME_RESOLUTION`
**Default:** [`1440,2000`] *(falls back to [`RESOLUTION`](#resolution))*
Browser viewport resolution (width,height)

---
#### `CHROME_SANDBOX`
**Default:** [`True`]
Enable Chrome sandbox (disable in Docker with --no-sandbox)

---
#### `CHROME_TIMEOUT`
**Default:** [`60`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for Chrome operations in seconds

---
#### `CHROME_USER_AGENT`
**Default:** [`""`] *(falls back to [`USER_AGENT`](#user_agent))*
User agent string for Chrome

---
#### `CHROME_USER_DATA_DIR`
**Default:** [`""`]
Path to Chrome user data directory for persistent sessions (derived from ACTIVE_PERSONA if not set)

---
#### `CHROME_WAIT_FOR`
**Default:** [`networkidle2`]
Page load completion condition (domcontentloaded, load, networkidle0, networkidle2)


### DNS Settings

#### `DNS_ENABLED`
**Default:** [`True`]
Enable DNS traffic recording during page load

---
#### `DNS_TIMEOUT`
**Default:** [`30`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for DNS recording in seconds


### SSL Settings

#### `SSL_ENABLED`
**Default:** [`True`]
Enable SSL certificate capture

---
#### `SSL_TIMEOUT`
**Default:** [`30`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for SSL capture in seconds


### Headers Settings

#### `HEADERS_ENABLED`
**Default:** [`True`]
Enable HTTP headers capture

---
#### `HEADERS_TIMEOUT`
**Default:** [`30`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for headers capture in seconds


### Redirects Settings

#### `REDIRECTS_ENABLED`
**Default:** [`True`]
Enable redirect chain capture

---
#### `REDIRECTS_TIMEOUT`
**Default:** [`30`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for redirect capture in seconds


### Responses Settings

#### `RESPONSES_ENABLED`
**Default:** [`True`]
Enable HTTP response capture

---
#### `RESPONSES_TIMEOUT`
**Default:** [`30`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for response capture in seconds


### Console Log Settings

#### `CONSOLELOG_ENABLED`
**Default:** [`True`]
Enable console log capture

---
#### `CONSOLELOG_TIMEOUT`
**Default:** [`30`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for console log capture in seconds


### Accessibility Settings

#### `ACCESSIBILITY_ENABLED`
**Default:** [`True`]
Enable accessibility tree capture

---
#### `ACCESSIBILITY_TIMEOUT`
**Default:** [`30`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for accessibility capture in seconds


### SEO Settings

#### `SEO_ENABLED`
**Default:** [`True`]
Enable SEO metadata capture

---
#### `SEO_TIMEOUT`
**Default:** [`30`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for SEO capture in seconds


### Hashes Settings

#### `HASHES_ENABLED`
**Default:** [`True`]
Enable merkle tree hash generation

---
#### `HASHES_TIMEOUT`
**Default:** [`30`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for merkle tree generation in seconds


### Static File Settings

#### `STATICFILE_ENABLED`
**Default:** [`True`]
Enable static file detection

---
#### `STATICFILE_TIMEOUT`
**Default:** [`30`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for static file detection in seconds


### uBlock Origin Settings

#### `UBLOCK_ENABLED`
**Default:** [`True`]
Enable uBlock Origin browser extension for ad blocking


### I Still Don't Care About Cookies Settings

#### `ISTILLDONTCAREABOUTCOOKIES_ENABLED`
**Default:** [`True`]
Enable I Still Don't Care About Cookies browser extension


### 2captcha Settings

#### `TWOCAPTCHA_API_KEY`
**Default:** [`""`]
2captcha API key for CAPTCHA solving service (get from https://2captcha.com)

---
#### `TWOCAPTCHA_AUTO_SUBMIT`
**Default:** [`False`]
Automatically submit forms after CAPTCHA is solved

---
#### `TWOCAPTCHA_ENABLED`
**Default:** [`True`]
Enable 2captcha browser extension for automatic CAPTCHA solving

---
#### `TWOCAPTCHA_RETRY_COUNT`
**Default:** [`3`]
Number of times to retry CAPTCHA solving on error

---
#### `TWOCAPTCHA_RETRY_DELAY`
**Default:** [`5`]
Delay in seconds between CAPTCHA solving retries

---
#### `TWOCAPTCHA_TIMEOUT`
**Default:** [`60`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for CAPTCHA solving in seconds


### Modal Closer Settings

#### `MODALCLOSER_ENABLED`
**Default:** [`True`]
Enable automatic modal and dialog closing

---
#### `MODALCLOSER_POLL_INTERVAL`
**Default:** [`500`]
How often to check for CSS modals (ms)

---
#### `MODALCLOSER_TIMEOUT`
**Default:** [`1250`]
Delay before auto-closing dialogs (ms)


### Infinite Scroll Settings

#### `INFINISCROLL_ENABLED`
**Default:** [`True`]
Enable infinite scroll page expansion

---
#### `INFINISCROLL_EXPAND_DETAILS`
**Default:** [`True`]
Expand <details> elements and click 'load more' buttons for comments

---
#### `INFINISCROLL_MIN_HEIGHT`
**Default:** [`16000`]
Minimum page height to scroll to in pixels

---
#### `INFINISCROLL_SCROLL_DELAY`
**Default:** [`2000`]
Delay between scrolls in milliseconds

---
#### `INFINISCROLL_SCROLL_DISTANCE`
**Default:** [`1600`]
Distance to scroll per step in pixels

---
#### `INFINISCROLL_SCROLL_LIMIT`
**Default:** [`10`]
Maximum number of scroll steps

---
#### `INFINISCROLL_TIMEOUT`
**Default:** [`120`] *(falls back to [`TIMEOUT`](#timeout))*
Maximum timeout for scrolling in seconds


### DOM Outlinks Parser Settings

#### `PARSE_DOM_OUTLINKS_ENABLED`
**Default:** [`True`]
Enable DOM outlinks parsing from archived pages

---
#### `PARSE_DOM_OUTLINKS_TIMEOUT`
**Default:** [`30`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for DOM outlinks parsing in seconds


### HTML URL Parser Settings

#### `PARSE_HTML_URLS_ENABLED`
**Default:** [`True`]
Enable HTML URL parsing


### JSONL URL Parser Settings

#### `PARSE_JSONL_URLS_ENABLED`
**Default:** [`True`]
Enable JSON Lines URL parsing


### Netscape URL Parser Settings

#### `PARSE_NETSCAPE_URLS_ENABLED`
**Default:** [`True`]
Enable Netscape bookmarks HTML URL parsing


### Text URL Parser Settings

#### `PARSE_TXT_URLS_ENABLED`
**Default:** [`True`]
Enable plain text URL parsing


### RSS URL Parser Settings

#### `PARSE_RSS_URLS_ENABLED`
**Default:** [`True`]
Enable RSS/Atom feed URL parsing


### Claude Code Settings

#### `ANTHROPIC_API_KEY`
**Default:** [`""`]
Anthropic API key for Claude Code authentication

---
#### `CLAUDECODE_BINARY`
**Default:** [`claude`]
Path to Claude Code CLI binary

---
#### `CLAUDECODE_ENABLED`
**Default:** [`False`]
Enable Claude Code AI agent integration. Controls whether the claudecode plugin participates in crawl-time extraction; child plugins still need the claudecode plugin installed and a working Claude binary.

---
#### `CLAUDECODE_MAX_TURNS`
**Default:** [`10`]
Maximum number of agentic turns per invocation

---
#### `CLAUDECODE_MODEL`
**Default:** [`sonnet`]
Claude model to use (e.g. sonnet, opus, haiku)

---
#### `CLAUDECODE_TIMEOUT`
**Default:** [`120`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for Claude Code operations in seconds


### Claude Chrome Settings

#### `CLAUDECHROME_ENABLED`
**Default:** [`False`]
Enable Claude for Chrome browser extension for AI-driven page interaction

---
#### `CLAUDECHROME_MAX_ACTIONS`
**Default:** [`15`]
Maximum number of agentic loop iterations (screenshots + actions) per page

---
#### `CLAUDECHROME_MODEL`
**Default:** [`sonnet`]
Claude model to use (e.g. sonnet, opus, haiku). Availability depends on your plan.

---
#### `CLAUDECHROME_PROMPT`
**Default:** [*see defaults*]
Prompt for Claude to execute on the page. Claude can click buttons, fill forms, download files, and interact with any page element.

---
#### `CLAUDECHROME_TIMEOUT`
**Default:** [`120`] *(falls back to [`TIMEOUT`](#timeout))*
Timeout for Claude for Chrome operations in seconds


### Claude Code Extract Settings

#### `CLAUDECODEEXTRACT_ENABLED`
**Default:** [`False`]
Enable Claude Code AI extraction

---
#### `CLAUDECODEEXTRACT_MAX_TURNS`
**Default:** [`10`] *(falls back to [`CLAUDECODE_MAX_TURNS`](#claudecode_max_turns))*
Maximum number of agentic turns for extraction

---
#### `CLAUDECODEEXTRACT_MODEL`
**Default:** [`sonnet`] *(falls back to [`CLAUDECODE_MODEL`](#claudecode_model))*
Claude model to use for extraction (e.g. sonnet, opus, haiku)

---
#### `CLAUDECODEEXTRACT_PROMPT`
**Default:** [*see defaults*]
Custom prompt for Claude Code extraction. Use this to define what Claude should extract or generate from the snapshot.

---
#### `CLAUDECODEEXTRACT_TIMEOUT`
**Default:** [`120`] *(falls back to [`CLAUDECODE_TIMEOUT`](#claudecode_timeout))*
Timeout for Claude Code extraction in seconds


### Claude Code Cleanup Settings

#### `CLAUDECODECLEANUP_ENABLED`
**Default:** [`False`]
Enable Claude Code AI cleanup of snapshot files

---
#### `CLAUDECODECLEANUP_MAX_TURNS`
**Default:** [`15`] *(falls back to [`CLAUDECODE_MAX_TURNS`](#claudecode_max_turns))*
Maximum number of agentic turns for cleanup

---
#### `CLAUDECODECLEANUP_MODEL`
**Default:** [`sonnet`] *(falls back to [`CLAUDECODE_MODEL`](#claudecode_model))*
Claude model to use for cleanup (e.g. sonnet, opus, haiku)

---
#### `CLAUDECODECLEANUP_PROMPT`
**Default:** [*see defaults*]
Custom prompt for Claude Code cleanup. Defines what Claude should clean up and how to determine which duplicates to keep.

---
#### `CLAUDECODECLEANUP_TIMEOUT`
**Default:** [`120`] *(falls back to [`CLAUDECODE_TIMEOUT`](#claudecode_timeout))*
Timeout for Claude Code cleanup in seconds


### Ripgrep Search Settings

#### `RIPGREP_ARGS`
**Default:** [`['--files-with-matches', '--no-messages', '--ignore-case']`]
Default ripgrep arguments

---
#### `RIPGREP_ARGS_EXTRA`
**Default:** [`[]`]
Extra arguments to append to ripgrep command

---
#### `RIPGREP_BINARY`
**Default:** [`rg`]
Path to ripgrep binary

---
#### `RIPGREP_TIMEOUT`
**Default:** [`90`] *(falls back to [`TIMEOUT`](#timeout))*
Search timeout in seconds


### Sonic Search Settings

#### `SEARCH_BACKEND_SONIC_BUCKET`
**Default:** [`snapshots`]
Sonic bucket name

---
#### `SEARCH_BACKEND_SONIC_COLLECTION`
**Default:** [`archivebox`]
Sonic collection name

---
#### `SEARCH_BACKEND_SONIC_HOST_NAME`
**Default:** [`127.0.0.1`]
Sonic server hostname

---
#### `SEARCH_BACKEND_SONIC_PASSWORD`
**Default:** [`SecretPassword`]
Sonic server password

---
#### `SEARCH_BACKEND_SONIC_PORT`
**Default:** [`1491`]
Sonic server port


### SQLite FTS Search Settings

#### `SEARCH_BACKEND_SQLITE_DB`
**Default:** [`search.sqlite3`]
SQLite FTS database filename

---
#### `SEARCH_BACKEND_SQLITE_SEPARATE_DATABASE`
**Default:** [`True`]
Use separate database file for FTS index

---
#### `SEARCH_BACKEND_SQLITE_TOKENIZERS`
**Default:** [`porter unicode61 remove_diacritics 2`]
FTS5 tokenizer configuration



<img src="https://github.com/ArchiveBox/ArchiveBox/assets/511499/5a4dd576-387a-4a1f-9dfa-407eac87078c" width="100%"/>
