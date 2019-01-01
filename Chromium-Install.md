### Google Chrome Instructions:

I recommend Chromium instead of Google Chrome, since it's open source and doesn't send your data to Google.
Chromium may have some issues rendering some sites though, so you're welcome to try Google-chrome instead.
It's also easier to use Google Chrome if you already have it installed, rather than downloading Chromium all over.

1. Install & link google-chrome
```bash
# On Mac:
# If you already have Google Chrome in /Applications/, skip this brew command
brew cask install google-chrome
brew install wget python3

echo -e '#!/bin/bash\n/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome "$@"' > /usr/local/bin/google-chrome
chmod +x /usr/local/bin/google-chrome
```

```bash
# On Linux:
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
apt update; apt install google-chrome-beta python3 wget
```

2. Set the environment variable `CHROME_BINARY` to `google-chrome` before running:

```bash
env CHROME_BINARY=google-chrome ./archive ~/Downloads/bookmarks_export.html
```
If you're having any trouble trying to set up Google Chrome or Chromium, see the Troubleshooting section below.