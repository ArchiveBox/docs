# Security Overview

## Usage Modes

ArchiveBox has three common usage modes outlined below.

<img src="https://i.imgur.com/K3dZcjG.png" width="50px" align="right"/>

#### Public Content Mode [Default]

This is the default (lax) mode, intended for archiving public (non-secret) URLs without authenticating the headless browser.  This is the mode used if you're archiving news articles, audio, video, etc. browser bookmarks to a folder published on your webserver. This allows you to access and link to content on `http://your.archive.com/archive...` after the originals go down.

This mode should not be used for archiving entire browser history or authenticated private content like Google Docs, paywalled content, invite-only subreddits, private photo share urls, etc.

#### Archiving Private Content

`WARNING! Advanced users only`

ArchiveBox is able to archive content that requires authentication or cookies, but it comes with some caveats. Create dedicated logins for archiving to access paywalled content, private forums, LAN-only content, etc. then share them with ArchiveBox via Chrome profile + cookies.txt file.

To get started, set [`CHROME_USER_DATA_DIR`](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#chrome_user_data_dir) and [`COOKIES_FILE`](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#COOKIES_FILE) to point to a Chrome user folder that has your sessions and a wget `cookies.txt` file respectively.

If you're importing private links or authenticated content, you probably don't want to share your archive folder publicly on a webserver, so don't follow the [[Publishing Your Archive]] instructions unless you are only serving it on a trusted LAN or have some sort of authentication in front of it.  Make sure to point ArchiveBox to an output folder with conservative permissions, as it may contain archived content with secret session tokens or pieces of your user data.  You may also wish to encrypt the archive using an encrypted disk image or filesystem like ZFS as it will contain all requests and response data, including session keys, user data, usernames, etc.

**Things to watch out for:**
- any cookies / secret state in this profile will be totally visible to anyone viewing the archives, don't use your personal Chrome profile
- any secret tokens in URLs are sent to `archive.org` (unless you set `SAVE_ARCHIVE_DOT_ORG = False`) 
- domain in URL is leaked to favicon service (unless you set `SAVE_FAVICON = False`)
- viewing malicious archived JS could allow an attacker to access your other archive items + the admin interface (it executes on the same domain right now, fix is pending)

<img src="https://i.imgur.com/Jszo4h2.png" width="400px"/>

*An example of a session cookie reflected in `headers.json` visible in the archive.*

<img src="https://i.imgur.com/DfyQUDV.png" width="50px" align="right"/>

## Do not run as root

<img src="https://i.imgur.com/yDqJc4I.jpg" width="150px" align="right">

Do not run ArchiveBox as root for a number of reasons:
 - Chrome will execute as root and fail immediately because Chrome sandboxing is pointless when the data directory is opened as root (do not set `CHROME_SANDBOX=False` just to bypass that error!)
 - All dependencies will be run as root, if any of them have a vulnerability that's exploited by sites you're archiving you're opening yourself up to full system compromise
 - ArchiveBox does lots of HTML parsing, filesystem access, and shell command execution.  A bug in any one of those subsystems could potentially lead to deleted/damaged data on your hard drive, or full system compromise unless restricted to a user that only has permissions to access the directories needed
 - Do you really trust a project created by a Github user called `@pirate` 😉? Why give a random program off the internet root access to your entire system? (I don't have malicious intent, I'm just saying in principle you should not be running random Github projects as root)

**Instead, you should run ArchiveBox as your normal user, or create a user with less privileged access:**
```bash
useradd -r -g archivebox -G audio,video archivebox  # the audio & video groups are used by chrome
mkdir -p /home/archivebox/data
chown -R archivebox:archivebox /home/archivebox
...
sudo -u archivebox archivebox add ...
```

~~If you absolutely must run it as root for some reason, a footgun is provided: you can set [`ALLOW_ROOT=True`](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#ALLOW_ROOT) via environment variable or in your ArchiveBox.conf file.~~ This footgun option was removed (I'm sorry, the support burden of helping people who messed up their systems by running this as root was too high).

<img src="https://i.imgur.com/ca1he6I.png" width="40px" align="right"/>

## Output Folder

### Permissions

What are the permissions on the archive folder? Limit access to the fewest possible users by checking folder ownership and setting [`OUTPUT_PERMISSIONS`](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#OUTPUT_PERMISSIONS) accordingly.

### Filesystem

How much are you planning to archive?  Only a few bookmarked articles, or thousands of pages of browsing history a day?  If it's only 1-50 pages a day, you can probably just stick it in a normal folder on your hard drive, but if you want to go over 100 pages a day, you will likely want to put your archive on a compressed/deduplicated/encrypted disk image or filesystem like ZFS.

### Publishing

Are you publishing your archive? If so, make sure you're only serving it as HTML and not accidentally running it as php or cgi, and put it on its own domain not shared with other services.  This is done in order to avoid cookies leaking between your main domain and domains hosting content you don't control.  Many companies put user provided files on separate domains like googleusercontent.com and github.io to avoid this problem.

Published archives automatically include a `robots.txt` `Dissallow: /` to block search engines from indexing them. You may still wish to publish your contact info in the index footer though using [`FOOTER_INFO`](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#FOOTER_INFO) so that you can respond to any DMCA and copyright takedown notices if you accidentally rehost copyrighted content.
