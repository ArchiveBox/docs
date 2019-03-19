## Security Model

ArchiveBox has three recommended usage modes.

#### Public Mode [Default]

This is the default (lax) mode, intended for archiving public (non-secret) URLs without authenticating the headless browser.  This is the mode used if you're archiving news articles, audio, video, etc. browser bookmarks to a folder published on your webserver. This allows you to access and link to content on `http://your.archive.com/archive...` after the originals go down.

This mode should not be used for archiving entire browser history or authenticated private content like Google Docs, paywalled content, invite-only subreddits, etc.

#### Private Mode

If you're importing private links or authenticated content, you definitely don't want to share your archive folder publicly on a webserver.  You can set [`CHROME_USER_DATA_DIR`](https://github.com/pirate/ArchiveBox/wiki/Configuration#chrome_user_data_dir) and [`COOKIES_FILE`](https://github.com/pirate/ArchiveBox/wiki/Configuration#COOKIES_FILE) to enable authenticated Chrome and wget archiving respectively, and then point ArchiveBox to a safe output folder with conservative permissions.  You may also wish to encrypt the archive using an encrypted disk image or filesystem like ZFS as it will contain all requests and response data, including session keys, user data, usernames, etc.

#### Extra Private Mode

Two 3rd-party API endpoints are hit during normal archiving:

 - `https://www.google.com/s2/favicons?domain={domain}` when [`FETCH_FAVICON`](https://github.com/pirate/ArchiveBox/wiki/Configuration#fetch_favicon) is `True`, the domains for each link are shared in order to get the favicon, but not the full URL
 - `https://web.archive.org/save/{url}` when [`SUBMIT_ARCHIVE_DOT_ORG`](https://github.com/pirate/ArchiveBox/wiki/Configuration#submit_archive_dot_org) is `True`, full URLs are submitted to the Wayback Machine for archiving, but no cookies or content from the local authenticated archive are shared

If you are not comfortable using 3rd-party endpoints during archiving, you should disable the archive methods above.  Disabling these are highly recommended if you plan on archiving sites that use unique slugs access private content, e.g. Google docs, codimd notepads, etc.


## Archive Data Storage

How much are you planning to archive?  Only a few bookmarked articles, or thousands of pages of browsing history a day?  If it's only 1-50 pages a day, you can probably just stick it in a normal folder on your hard drive, but if you want to go over 100 pages a day, you will likely want to put your archive on a compressed/deduplicated filesystem like ZFS or inside a compressed disk image.

What are the permissions on the archive folder? Limit access to the fewest possible users by checking folder ownership and setting [`OUTPUT_PERMISSIONS`](https://github.com/pirate/ArchiveBox/wiki/Configuration#OUTPUT_PERMISSIONS) accordingly.

Are you publishing your archive? If so, make sure you're only serving it as HTML and not accidentally running it as php or cgi, and put it on its own domain not shared with other services.  This is done in order to avoid cookies leaking between your main domain and domains hosting content you don't control.  Many companies put user provided files on separate domains like googleusercontent.com and github.io to avoid this problem.

### Are the URLs private, the content, or both??
