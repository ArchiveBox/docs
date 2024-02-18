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
 - [Archive Method Toggles:](#archive-method-toggles) On/off switches for methods.
 - [Archive Method Options:](#archive-method-options) Method tunables and parameters.
 - [Shell Options:](#shell-options) Format & behavior of CLI output.
 - [Dependency Options:](#dependency-options) Specify exact paths to dependencies. 

<br/>

---

<img src="https://imgur.zervice.io/iTYT7Ip.png" width="100%"/>
<p align="center">
<i>In case this document is ever out of date, it's recommended to read the code that loads the config directly: <a href="https://github.com/ArchiveBox/ArchiveBox/blob/master/archivebox/config.py#L27"><code>archivebox/config.py</code></a> ➡️</i>
</p>

## General Settings

*General options around the archiving process, output format, and timing.*

---
#### `OUTPUT_PERMISSIONS`
**Possible Values:** [`755`]/`644`/...  
Permissions to set the output directory and file contents to.  

This is useful when running ArchiveBox inside Docker as root and you need to explicitly set the permissions to something that the users on the host can access.

*Related options:*  
[`PUID` / `PGID`](#puid--pgid)

---

<a name="puid--pgid"/>
<a name="puid"/>
<a name="pgid"/>

#### `PUID` / `PGID`

**Possible Values:** [`911`]/`1000`/...

User and Group ownership to set the output directory and file contents to.  **Only settable as environment variables** when using ArchiveBox in Docker.

This is useful on some Docker setups when you want the data dir to be owned by the same UID/GID on the host and inside the container.

`PUID=0` is not allowed ([do not run as root](https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview#do-not-run-as-root)), and `PGID=0` is allowed but not recommended.  
Make sure if using NFS/SMB/FUSE that the volume allows setting ownership on files (e.g. don't set `root_squash` or `all_squash` on NFS shares).

*Learn more:*  
- https://docs.linuxserver.io/general/understanding-puid-and-pgid/
- https://github.com/ArchiveBox/ArchiveBox/issues/1304
- https://github.com/ArchiveBox/ArchiveBox/blob/main/bin/docker_entrypoint.sh

*Related options:*  
[`OUTPUT_PERMISSIONS`](#output_permissions)

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

<a name="admin_username"/>
<a name="admin_password"/>

#### `ADMIN_USERNAME` / `ADMIN_PASSWORD`

**Possible Values:** [`None`]/`"admin"`/...  

Only used on first run / initial setup in Docker. ArchiveBox will create an admin user with the specified username and password when these options are found in the environment.
Useful for setting up a Docker instance of ArchiveBox without needing to run a shell command to create the admin user.

Equivalent to:
```bash
$ archivebox manage createsuperuser
Username: <ADMIN_USERNAME>
Password: <ADMIN_PASSWORD>
Password (again): <ADMIN_PASSWORD>
```

*Related options:*  
[`PUBLIC_INDEX / PUBLIC_SNAPSHOTS / PUBLIC_ADD_VIEW`](#public_index)

---

<a name="public_index"/>
<a name="public_snapshots"/>
<a name="public_add_view"/>

#### `PUBLIC_INDEX` / `PUBLIC_SNAPSHOTS` / `PUBLIC_ADD_VIEW`

**Possible Values:** [`False`]/`True`
Configure whether or not login is required to use each area of ArchiveBox.

```python3
archivebox manage createsuperuser  # set a password before disabling public access

archivebox config --set PUBLIC_INDEX=False       # True = allow users to view main snapshots list without logging in
archivebox config --set PUBLIC_SNAPSHOTS=False   # True = allow users to view snapshot content without logging in
archivebox config --set PUBLIC_ADD_VIEW=False    # True = allow users to submit new URLs to archive without logging in
```
https://github.com/ArchiveBox/ArchiveBox#-web-ui-usage

---
#### `CUSTOM_TEMPLATES_DIR`
**Possible Values:** [`None`]/`/path/to/custom_templates`/...  

Path to a directory containing custom html/css/images for overriding the default UI styling.  Files found in the folder at the specified path can override any of the defaults in the [`TEMPLATES_DIR`](https://github.com/ArchiveBox/ArchiveBox/tree/dev/archivebox/templates) directory (copy files from that default dir into your custom dir to get started making a custom theme).

If you've used `django` before, this works exactly the same way that `django` template overrides work (because it uses `django` under the hood).

```bash
$ pip show -f archivebox | grep Location: | awk '{print $2}'
/opt/homebrew/lib/python3.11/site-packages
$ pip show -f archivebox | grep archivebox/templates
archivebox/templates/admin/app_index.html
archivebox/templates/admin/base.html
archivebox/templates/admin/login.html
...
# copy default templates into a directory somewhere, edit as needed, then point archivebox to it
$ cp -r /opt/homebrew/lib/python3.11/site-packages/archivebox/templates ~/archivebox/custom_templates
$ archivebox config --set CUSTOM_TEMPLATES_DIR=~/archivebox/custom_templates
```

*Related options:*  
[`FOOTER_INFO`](#footer_info)

---
#### `REVERSE_PROXY_USER_HEADER`
**Possible Values:** [`Remote-User`]/`X-Remote-User`/...

HTTP header containing user name from authenticated proxy.

More info: https://github.com/ArchiveBox/ArchiveBox/pull/866

*Related options:*
[`REVERSE_PROXY_WHITELIST`](#REVERSE_PROXY_WHITELIST), [`LOGOUT_REDIRECT_URL`](#LOGOUT_REDIRECT_URL)

---
#### `REVERSE_PROXY_WHITELIST`
**Possible Values:** [`<empty string>`],`172.16.0.0/16`,`2001:d80::/26`/...

Comma separated list of IP CIDRs which are allowed to use reverse proxy authentication. Both IPv4 and IPv6 IPs can be used next to each other. Empty string means "deny all".

More info: https://github.com/ArchiveBox/ArchiveBox/pull/866

*Related options:*
[`REVERSE_PROXY_USER_HEADER`](#REVERSE_PROXY_USER_HEADER), [`LOGOUT_REDIRECT_URL`](#LOGOUT_REDIRECT_URL)

---
#### `LOGOUT_REDIRECT_URL`
**Possible Values:** [`/`]/`https://example.com/some/other/app`/...

URL to redirect users back to on logout when using reverse proxy authentication.

More info: https://github.com/ArchiveBox/ArchiveBox/pull/866

*Related options:*
[`REVERSE_PROXY_USER_HEADER`](#REVERSE_PROXY_USER_HEADER), [`REVERSE_PROXY_WHITELIST`](#REVERSE_PROXY_WHITELIST)

---
#### `LDAP`
**Possible Values:** [`False`]/`True`

Whether to use an external [LDAP](https://jumpcloud.com/blog/what-is-ldap-authentication) server for authentication (e.g. OpenLDAP, MS Active Directory, OpenDJ, etc.).

```bash
# first, install optional ldap addon to use this feature
pip install archivebox[ldap]
```

Then set these configuration values to finish configuring LDAP:
```yaml
LDAP: True
LDAP_SERVER_URI: "ldap://ldap.example.com:3389"
LDAP_BIND_DN: "ou=archivebox,ou=services,dc=ldap.example.com"
LDAP_BIND_PASSWORD: "secret-bind-user-password"
LDAP_USER_BASE: "ou=users,ou=archivebox,ou=services,dc=ldap.example.com"
LDAP_USER_FILTER: "(objectClass=user)"

LDAP_USERNAME_ATTR: "uid"
LDAP_FIRSTNAME_ATTR: "givenName"
LDAP_LASTNAME_ATTR: "sn"
LDAP_EMAIL_ATTR: "mail"
```

More info:
- https://github.com/ArchiveBox/ArchiveBox/pull/1214
- https://github.com/django-auth-ldap/django-auth-ldap#example-configuration
- https://jumpcloud.com/blog/what-is-ldap-authentication

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

<a name="url_blacklist"/>

#### `URL_DENYLIST`
**Possible Values:** [`\.(css|js|otf|ttf|woff|woff2|gstatic\.com|googleapis\.com/css)(\?.*)?$`]/`.+\.exe$`/`http(s)?:\/\/(.+)?example.com\/.*`/...  

A regex expression used to exclude certain URLs from archiving.  You can use if there are certain domains, extensions, or other URL patterns that you want to ignore whenever they get imported.  Blacklisted URLs wont be included in the index, and their page content wont be archived.

When building your exclusion list, you can check whether a given URL matches your regex expression in `python` like so:
```python
>>> import re
>>> URL_DENYLIST = r'^http(s)?:\/\/(.+\.)?(youtube\.com)|(amazon\.com)\/.*$'  # replace this with your regex to test
>>> URL_DENYLIST_PTN = re.compile(URL_DENYLIST, re.IGNORECASE | re.UNICODE | re.MULTILINE)

>>> bool(URL_DENYLIST_PTN.search('https://test.youtube.com/example.php?abc=123'))  # replace this with the URL to test
True   # this URL would not be archived because it matches the exclusion pattern
```

*Note: all assets required to render each page are still archived, `URL_DENYLIST`/`URL_ALLOWLIST` do not apply to images, css, video, etc. visible inline within the page.*

<b>Note 2:</b> These options used to be called <a href="#url_whitelist"><code>URL_WHITELIST</code></a> & <a href="#url_blacklist"><code>URL_BLACKLIST</code></a> before <a href="https://github.com/ArchiveBox/ArchiveBox/releases"><code>v0.7.1</code></a>.

*Related options:*  
[`URL_ALLOWLIST`](#URL_ALLOWLIST), [`SAVE_MEDIA`](#SAVE_MEDIA), [`SAVE_GIT`](#SAVE_GIT), [`GIT_DOMAINS`](#GIT_DOMAINS)

---

<a name="url_whitelist"/>

#### `URL_ALLOWLIST`
**Possible Values:** [`None`]/`^http(s)?:\/\/(.+)?example\.com\/?.*$`/...  

A regex expression used to exclude all URLs that don't match the given pattern from archiving.  You can use if there are certain domains, extensions, or other URL patterns that you want to restrict the scope of archiving to (e.g. to only archive a single domain, subdirectory, or filetype, etc..

When building your whitelist, you can check whether a given URL matches your regex expression in `python` like so:
```python
>>> import re
>>> URL_ALLOWLIST = r'^http(s)?:\/\/(.+)?example\.com\/?.*$'  # replace this with your regex to test
>>> URL_ALLOWLIST_PTN = re.compile(URL_ALLOWLIST, re.IGNORECASE | re.UNICODE | re.MULTILINE)

>>> bool(URL_ALLOWLIST_PTN.search('https://test.example.com/example.php?abc=123'))
True      # this URL would be archived

>>> bool(URL_ALLOWLIST_PTN.search('https://test.youtube.com/example.php?abc=123'))
False     # this URL would be excluded from archiving
```

This option is useful for **recursive archiving** of all the pages under a given domain or subfolder (aka crawling/spidering), without following links to external domains / parent folders.
```bash
# temporarily enforce a whitelist by setting the option as an environment variable
export URL_ALLOWLIST='^http(s)?:\/\/(.+)?example\.com\/?.*$'

# then run your archivebox commands in the same shell
archivebox add --depth=1 'https://example.com'
archivebox list https://example.com | archivebox add --depth=1
archivebox list https://example.com | archivebox add --depth=1
archivebox list https://example.com | archivebox add --depth=1   # repeat up to desired depth
...
# all URLs that don't match *.example.com will be excluded, e.g. a link to youtube.com would not be followed
```

*Note: all assets required to render each page are still archived, `URL_DENYLIST`/`URL_ALLOWLIST` do not apply to images, css, video, etc. visible inline within the page.*

*Related options:*  
[`URL_DENYLIST`](#URL_DENYLIST), [`SAVE_MEDIA`](#SAVE_MEDIA), [`SAVE_GIT`](#SAVE_GIT), [`GIT_DOMAINS`](#GIT_DOMAINS)

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
Unlike the other methods, this does not download any additional files, so it's practically free from a disk usage perspective. It works by using any existing downloaded HTML version (e.g. wget, DOM dump, singlefile) and piping it into Mercury.

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
**Possible Values:** [`github.com,bitbucket.org,gitlab.com,gist.github.com,codeberg.org,gitea.com,git.sr.ht`]/`git.example.com`/...  
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

<img src="https://imgur.zervice.io/BDPfWxk.png" width="48%"/>
<img src="https://imgur.zervice.io/kIL8zSD.png" width="48%"/>

---
#### `SHOW_PROGRESS`
**Possible Values:** [`True`]/`False`  
Show real-time progress bar in console output. Defaults to `True` if stdin is a TTY (interactive session), otherwise `False` (e.g. if run in a script or piped into a file).

*Note: We use [asymptotic progress bars](https://gist.github.com/pirate/c89b7d42be148e9180d8c7cf81e734c8) because most tasks complete quickly! ✨*

<img src="https://imgur.zervice.io/XY2E7AR.png" width="99%"/>

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

---
#### `SINGLEFILE_ARGS`
**Possible Values:** [`["--back-end=playwright-firefox","--load-deferred-images-dispatch-scroll-event=true"]`]/..

Arguments that are passed to the SingleFile binary. The values should be a valid JSON string.

*Related options:*  
[`SINGLEFILE_BINARY`](#singlefile_binary)

---
#### `CURL_ARGS`
**Possible Values:** [`["--tlsv1.3","--http2"]`]/..

Arguments that are passed to the curl binary. The values should be a valid JSON string.

*Related options:*  
[`CURL_BINARY`](#curl_binary)

---
#### `WGET_ARGS`
**Possible Values:** [`["--https-only"]`]/..

Arguments that are passed to the wget binary. The values should be a valid JSON string.

*Related options:*  
[`WGET_BINARY`](#wget_binary)

---
#### `YOUTUBEDL_ARGS`
**Possible Values:** [`["--limit-rate=10M"]`]/..

Arguments that are passed to the [youtube-dl](https://github.com/rg3/youtube-dl) binary. The values should be a valid JSON string.

*Related options:*  
[`YOUTUBEDL_BINARY`](#youtubedl_binary)

---
#### `GIT_ARGS`
**Possible Values:** [`["--depth=1"]`]

Arguments that are passed to the `git clone` subcommand. The values should be a valid JSON string.

*Related options:*  
[`GIT_BINARY`](#git_binary)


<img src="https://github.com/ArchiveBox/ArchiveBox/assets/511499/5a4dd576-387a-4a1f-9dfa-407eac87078c" width="100%"/>

▶️ *Looking for more? Sometimes this document is out of date. Check the source code for extra undocumented options: [`archivebox/config.py`](https://github.com/ArchiveBox/ArchiveBox/blob/master/archivebox/config.py#L27).*