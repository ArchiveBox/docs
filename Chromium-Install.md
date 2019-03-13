By default, ArchiveBox looks for any existing installed version of Chrome/Chromium and uses it if found, but you can optionally install a specific version and set the environment variable `CHROME_BINARY` to force ArchiveBox to that one (e.g. `CHROME_BINARY=google-chrome-beta`).

If you don't already have Chrome installed, I recommend installing Chromium instead of Google Chrome, as it's the open-source fork of Chrome that doesn't send as much tracking data to Google.

#### Check for existing Chrome install
```bash
google-chrome --version
Google Chrome 73.0.3683.75 beta     # should be >v59
```
(Replace `google-chrome` with `chromium-browser` or path to your preferred binary)

## Installing Chromium

### macOS
If you already have `/Applications/Chromium.app`, you don't need to run this.
```bash
brew cask install chromium-browser
```

### Ubuntu/Debian
If you already have `chromium-browser` >= v59 installed (run `chromium-browser --version`, you don't need to run this.
```bash
apt update
apt install chromium-browser
```

## Installing Google Chrome

### macOS
If you already have `/Applications/Google Chrome.app`, you don't need to run this.
```bash
brew cask install google-chrome
```
### Ubuntu/Debian
If you already have `google-chrome` >= v59 installed (run `google-chrome --version`, you don't need to run this.
```bash
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
apt update
apt install google-chrome-beta
```

## Troubleshooting

If you encounter problems setting up Google Chrome or Chromium, see the [Troubleshooting](https://github.com/pirate/ArchiveBox/wiki/Troubleshooting#chromiumgoogle-chrome) page.