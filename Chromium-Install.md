# Chromium Install

By default, ArchiveBox looks for any existing installed version of Chrome/Chromium and uses it if found.  You can optionally install a specific version and set the environment variable `CHROME_BINARY` to force ArchiveBox to use that one, e.g.:  

 - `CHROME_BINARY=google-chrome-beta`
 - `CHROME_BINARY=/usr/bin/chromium-browser`
 - `CHROME_BINARY='/Applications/Chromium.app/Contents/MacOS/Chromium'`
 - `CHROME_BINARY='~/Library/Caches/ms-playwright/chromium-857950/chrome-mac/Chromium.app/Contents/MacOS/Chromium'`

If you don't already have Chrome installed, I recommend installing Chromium instead of Google Chrome, as it's the open-source fork of Chrome that doesn't send as much tracking data to Google.

**Check for existing Chrome/Chromium install:**

<img src="https://imgur.zervice.io/FxFoIMH.jpg" width="25%" align="right"/> 

```bash
google-chrome --version | chromium-browser --version
Google Chrome 122.0.6261.49 beta     # should be >v111
```

## Installing Chromium

### ⭐️ Any OS (recommended)

[`playwright`](https://playwright.dev/python/docs/browsers) (by the Microsoft team) and [`puppeteer`](https://github.com/puppeteer/puppeteer) (by the Google team) are two options to get stable, repeatable Chromium distributions on many OSs.
```bash
pip install --upgrade --ignore-installed playwright
playwright install --with-deps chromium

# alternatively use puppeteer to get Chromium instead of playwright:
npm install puppeteer
```

### macOS

If you already have a Chrome app installed like `/Applications/Chromium.app`, you don't need to run this.
```bash
brew install --cask chromium
```

### Ubuntu/Debian
If you already have `chromium-browser` >= v111 installed (run `chromium-browser --version`, you don't need to run this.
```bash
sudo apt update
sudo apt install chromium-browser
# or on some systems:
sudo apt install chromium
```

## Installing Google Chrome

### macOS
If you already have `/Applications/Google Chrome.app`, you don't need to run this.
```bash
brew install --cask google-chrome
```
### Ubuntu/Debian
If you already have `google-chrome` >= v111 installed (run `google-chrome --version`, you don't need to run this.
```bash
wget -q -O - 'https://dl-ssl.google.com/linux/linux_signing_key.pub' | sudo apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt update
sudo apt install -y google-chrome
```

## Troubleshooting Chromium Install

If you encounter problems setting up Google Chrome or Chromium, see the [Troubleshooting](https://github.com/ArchiveBox/ArchiveBox/wiki/Troubleshooting#chromiumgoogle-chrome) page.

---

# Setting Up a Chromium User Profile

You may choose to set up a Chrome/Chromium user profile in order to use your cookies/sessions to log into sites behind authentication/paywall during archiving.

*Note: not all extractors use Chrome (e.g. `wget`, `mercury`, `media`), so [`COOKIES_FILE`](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration/#cookies_file) should be set up as well after this.*

> [!WARNING]
> **Make sure you use separate burner credentials dedicated to archiving,** e.g. don't log in with your normal daily Facebook/Instagram/Google/etc. accounts as server responses and page content will often contain your name/email/PII, session cookies, private tokens, etc. which then get preserved in your snapshots.
>  
> Future viewers of your archive may be able to use any reflected archived session tokens to log in as you, or at the very least, associate the content with your real identity. Even if this tradeoff seems acceptable now or you plan to keep your archive data private, you may want to share a snapshot with others in the future, and snapshots are very hard to sanitize/anonymize after-the-fact!
>
> For this reason, it's best to set up dedicated fake profile accounts for each site you want to archive, and consider them burned if you ever share any of your archived snapshots of those sites with untrusted people.

### Docker Setup

If using ArchiveBox in Docker, the easiest way to set up session credentials is by attaching the ArchiveBox browser to a virtual window server in a sidecar container, and logging in to your sites over VNC (less complicated than it sounds).

1. Add a `novnc` container and these settings to your `docker-compose.yml`.  
   ([`novnc`](https://github.com/theasp/docker-novnc) runs an [Xvfb](https://www.x.org/releases/X11R7.6/doc/man/man1/Xvfb.1.xhtml) + [Fluxbox](http://www.fluxbox.org/) desktop environment that lets you remote-control ArchiveBox's Chrome via VNC)

`docker-compose.yml`:
```yaml
services:
    archivebox:
        ...
        volumes:
            ...
            - ./chrome_profile:/home/archivebox/chrome_profile
        environment:
            - CHROME_USER_DATA_DIR=/home/archivebox/chrome_profile
            - DISPLAY=novnc:0.0
            
    novnc:
        image: theasp/novnc:latest
        environment:
            - DISPLAY_WIDTH=1920
            - DISPLAY_HEIGHT=1080
            - RUN_XTERM=no
        ports:
            - "8080:8080"
```

2. Start the `novnc` window server container
```bash
docker compose up -d novnc
# wait a few seconds for novnc to start...
```

3. Start ArchiveBox's Chrome inside Docker
```bash
docker compose run archivebox /usr/bin/chromium-browser --user-data-dir=/home/archivebox/chrome_profile --profile-directory=Default --disable-gpu --disable-features=dbus --disable-dev-shm-usage --start-maximized --no-sandbox --no-zygote --disable-sync --no-first-run
```
<small>(make sure you set `DISPLAY` & `CHROME_USER_DATA_DIR` and added the line to `volumes:` above first!)</small>

4. Open [`http://localhost:8080/vnc.html`](http://localhost:8080/vnc.html) in your browser. You should see a remote linux desktop shown with Chrome open, allowing you to remote-control ArchiveBox's browser. Use it to log into any sites where you want to save credentials.

5. ✅ Close the browser, stop & remove novnc, and then run archivebox normally. It will use the profile stored in `CHROME_USER_DATA_DIR=/home/archivebox/chrome_profile` going forward, you should now be able to archive sites as if you were logged in!

```bash
# stop the archivebox and novnc containers
docker compose down
docker compose down --remove-orphans
# edit docker-compose.yml to remove/comment out the novnc: section

# test it all out by archiving something hosted on one of the domains you logged in to
docker compose run archivebox add 'https://private.example.com/some/site/requiring/login.html'
# check the SingleFile, Screenshot, DOM, or PDF snapshot output (only these use the Chrome profile)
# make sure the content appears as your logged-in user would see it
```

<br/>

### Non-Docker Setup (Local Host)

If running ArchiveBox on your local machine without Docker, this process is fairly easy.

First, tell archivebox where you want to store your Chrome profile.

```bash
# replace /Users/alice/.archivebox_chrome with a path to store your profile in
archivebox config --set CHROME_USER_DATA_DIR=/Users/alice/.archivebox_chrome
```

Then run Chrome (with that profile dir) to open a visible browser window where you can log into things, e.g.:

```bash
# find your CHROME_BINARY path by running
archivebox version | grep CHROME_BINARY

# macOS example (using Google Chrome.app)
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --user-data-dir=/Users/alice/.archivebox_chrome

# Linux example (using Playwright Chromium)
/root/.cache/ms-playwright/chromium-1105/chrome-linux/chrome --user-data-dir=/Users/alice/.archivebox_chrome
```

Once it's open, log in to all the sites you want to be logged in to for archiving, then close/quit Chrome.

✅ All ArchiveBox extractors that use Chrome (e.g. Screenshot, PDF, DOM, Singlefile) should now use that profile.  
*Don't forget to set up [`COOKIES_FILE`](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration/#cookies_file) for the rest!*

<br/>

### Non-Docker Setup (Remote Host)

You must set up the profile using the exact same version of chrome that ArchiveBox is running (which can be found with `archivebox version`).
You can download the latest chromium with `pip install playwright && playwright install --with-deps chromium`, or get older versions of Chrome from https://chromium.cypress.io.

**General steps:**

1. Make sure you are running the same OS and have the same version of Chrome installed as the host running ArchiveBox
2. Follow the `Non-Docker Setup (Local Host)` setups above to create a Chrome profile locally
3. Rsync your chrome profile from your local machine to the remote archivebox host  
   `rsync --archive /path/to/profile remotehost:/path/to/profile/on/remote/host`
4. Configure ArchiveBox on the remote host to use the `rsync`'ed Chrome profile  
   `archivebox config --set CHROME_USER_DATA_DIR=/path/to/profile/on/remote/host`

You may need to run `chown -R archivebox /path/to/profile/on/remote/host` on the remote host to make the profile editable by the `archivebox` user on that machine.

✅ All ArchiveBox extractors that use Chrome (e.g. Screenshot, PDF, DOM, Singlefile) should now use that profile.  
*Don't forget to set up [`COOKIES_FILE`](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration/#cookies_file) for the rest!*

---

## More Info & Troubleshooting

- https://github.com/ArchiveBox/ArchiveBox/issues/952
- https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview#archiving-private-content
- https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview#%EF%B8%8F-things-to-watch-out-for-%EF%B8%8F
- https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview#publishing
- https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#chrome_user_data_dir
- https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#chrome_binary
- https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#cookies_file