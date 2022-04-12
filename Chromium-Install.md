# Chromium Install

By default, ArchiveBox looks for any existing installed version of Chrome/Chromium and uses it if found.  You can optionally install a specific version and set the environment variable `CHROME_BINARY` to force ArchiveBox to use that one, e.g.:  

 - `CHROME_BINARY=google-chrome-beta`
 - `CHROME_BINARY=/usr/bin/chromium-browser`
 - `CHROME_BINARY='/Applications/Chromium.app/Contents/MacOS/Chromium'`

If you don't already have Chrome installed, I recommend installing Chromium instead of Google Chrome, as it's the open-source fork of Chrome that doesn't send as much tracking data to Google.

**Check for existing Chrome/Chromium install:**

<img src="https://i.imgur.com/FxFoIMH.jpg" width="25%" align="right"/> 

```bash
google-chrome --version | chromium-browser --version
Google Chrome 73.0.3683.75 beta     # should be >v59
```

## Installing Chromium

### macOS
If you already have `/Applications/Chromium.app`, you don't need to run this.
```bash
brew install chromium
```

### Ubuntu/Debian
If you already have `chromium-browser` >= v59 installed (run `chromium-browser --version`, you don't need to run this.
```bash
apt update
apt install chromium-browser
# or on some systems:
apt install chromium
```

## Installing Google Chrome

### macOS
If you already have `/Applications/Google Chrome.app`, you don't need to run this.
```bash
brew install google-chrome
```
### Ubuntu/Debian
If you already have `google-chrome` >= v59 installed (run `google-chrome --version`, you don't need to run this.
```bash
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
apt update
apt install google-chrome
```

## Troubleshooting Chromium Install

If you encounter problems setting up Google Chrome or Chromium, see the [Troubleshooting](https://github.com/ArchiveBox/ArchiveBox/wiki/Troubleshooting#chromiumgoogle-chrome) page.


---

# Setting Up a Chromium User Profile

You may choose to set up a Chrome/Chromium user profile in order to use your cookies/sessions to log into sites behind authentication/paywall during archiving.

You must set up the profile using the exact same version of chrome that ArchiveBox is running (which can be found with `archivebox version`).
You can download old versions of Chrome in order to match it from https://chromium.cypress.io.

**General steps:**

1. Install desired chromium version in new directory inside your data folder `./data/chromium` on the host (outside Docker)
2. Run [`vncserver`](https://linux.die.net/man/1/vncserver) as `archivebox` user and run chromium in VNC session to generate cookies, then close VNC session
3. Add the config to `docker-compose.yml` for the chromium data dir and binary mount and config  
  `docker-compose.yml`:  
  ```yaml
services:
    archivebox:
        ...
        environment:
            ...
            - CHROME_USER_DATA_DIR=/data/chromium/.config/chromium
            - CHROME_BINARY=/data/chromium/chrome
        volumes:
            - ./data:/data
            - ./data/chromium:/data/chromium
            ...
...
```

4. Set the permissions on the chromium dir  
  `chmod -R ugo+rwx ./data/chromium/.config/chromium`  
  `chown -R archivebox:archivebox /data/chromium/`  
  (may need to be done inside Docker with `docker-compose run --rm archivebox <command>`)

Now profile is now generated and used by same instance of chrome on docker host and container.

Each step is crucial, especially the permissions and matching the binary inside of Docker and outside.

More info and troubleshooting steps: https://github.com/ArchiveBox/ArchiveBox/issues/952
