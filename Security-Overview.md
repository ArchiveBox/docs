<img src="https://i.imgur.com/ca1he6I.png" width="50px" align="right"/>

## Usage Modes

ArchiveBox has three common usage modes outlined below.

<img src="https://i.imgur.com/K3dZcjG.png" width="50px" align="right"/>

#### Public Mode [Default]

This is the default (lax) mode, intended for archiving public (non-secret) URLs without authenticating the headless browser.  This is the mode used if you're archiving news articles, audio, video, etc. browser bookmarks to a folder published on your webserver. This allows you to access and link to content on `http://your.archive.com/archive...` after the originals go down.

This mode should not be used for archiving entire browser history or authenticated private content like Google Docs, paywalled content, invite-only subreddits, etc.

<img src="https://i.imgur.com/xg6TxoK.png" width="50px" align="right"/>

#### Private Mode

ArchiveBox is designed to be able to archive content that requires authentication or cookies.  This includes paywalled content, private forums, LAN-only content, etc.

To get started, set [`CHROME_USER_DATA_DIR`](https://github.com/pirate/ArchiveBox/wiki/Configuration#chrome_user_data_dir) and [`COOKIES_FILE`](https://github.com/pirate/ArchiveBox/wiki/Configuration#COOKIES_FILE) to point to a Chrome user folder that has your sessions and a wget `cookies.txt` file respectively.

If you're importing private links or authenticated content, you probably don't want to share your archive folder publicly on a webserver, so don't follow the [[Publishing Your Archive]] instructions unless you are only serving it on a trusted LAN or have some sort of authentication in front of it.  Make sure to point ArchiveBox to an output folder with conservative permissions, as it may contain archived content with secret session tokens or pieces of your user data.  You may also wish to encrypt the archive using an encrypted disk image or filesystem like ZFS as it will contain all requests and response data, including session keys, user data, usernames, etc.

<img src="https://i.imgur.com/DfyQUDV.png" width="50px" align="right"/>

#### Stealth Mode

If you want ArchiveBox to be less noisy and avoid leaking any URLs to 3rd-party APIs during archiving, you can disable the options below.  Disabling these are recommended if you plan on archiving any sites that use secret tokens in the URL to grant access to private content without authentication, e.g. Google Docs, CodiDM notepads, etc.

 - `https://web.archive.org/save/{url}` when [`SUBMIT_ARCHIVE_DOT_ORG`](https://github.com/pirate/ArchiveBox/wiki/Configuration#submit_archive_dot_org) is `True`, full URLs are submitted to the Wayback Machine for archiving, but no cookies or content from the local authenticated archive are shared
 - `https://www.google.com/s2/favicons?domain={domain}` when [`FETCH_FAVICON`](https://github.com/pirate/ArchiveBox/wiki/Configuration#fetch_favicon) is `True`, the domains for each link are shared in order to get the favicon, but not the full URL

## Do not run as root

<img src="https://i.imgur.com/yDqJc4I.jpg" width="150px" align="right">

Do not run ArchiveBox as root for a number of reasons:
 - Chrome will execute as root and fail to run because Chrome sandboxing is not supported as root for good reason (do not set `CHROME_SANDBOX=False` just to bypass that error!)
 - All dependencies will be run as root, if any of them have a vulnerability that's exploited by sites you're archiving you're opening yourself up to full system compromise
 - ArchiveBox does lots of HTML parsing, filesystem access, and shell command execution.  A bug in any one of those subsystems could potentially lead to deleted/damaged data on your hard drive, or full system compromise unless restricted to a user that only has permissions to access the directories needed
 - Do you really trust a project created by a Github user called `@pirate` 😉? Why give a random program off the internet root access to your entire system? (I don't have malicious intent, I'm just saying in principle you should not be running random Github projects as root)

**Instead, you should run ArchiveBox as your normal user, or create a user with less privileged access:**
```bash
useradd -r -g archivebox -G audio,video archivebox
mkdir -p /home/archivebox/data
chown -R archivebox:archivebox /home/archivebox
...
sudo -u archivebox ./archive ...
```

## Output Folder

### Permissions

What are the permissions on the archive folder? Limit access to the fewest possible users by checking folder ownership and setting [`OUTPUT_PERMISSIONS`](https://github.com/pirate/ArchiveBox/wiki/Configuration#OUTPUT_PERMISSIONS) accordingly.

### Filesystem

How much are you planning to archive?  Only a few bookmarked articles, or thousands of pages of browsing history a day?  If it's only 1-50 pages a day, you can probably just stick it in a normal folder on your hard drive, but if you want to go over 100 pages a day, you will likely want to put your archive on a compressed/deduplicated/encrypted disk image or filesystem like ZFS.

### Publishing

Are you publishing your archive? If so, make sure you're only serving it as HTML and not accidentally running it as php or cgi, and put it on its own domain not shared with other services.  This is done in order to avoid cookies leaking between your main domain and domains hosting content you don't control.  Many companies put user provided files on separate domains like googleusercontent.com and github.io to avoid this problem.

Published archives automatically include a `robots.txt` `Dissallow: /` to block search engines from indexing them. You may still wish to publish your contact info in the index footer though using [`FOOTER_INFO`](https://github.com/pirate/ArchiveBox/wiki/Configuration#FOOTER_INFO) so that you can respond to any DMCA and copyright takedown notices if you accidentally rehost copyrighted content.