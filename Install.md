## Automatic Setup

Run `./bin/setup` to install all dependencies automatically.

## Manual Setup

If you don't like running random setup scripts off the internet (:+1:), you can follow these manual setup instructions.

**1. Install dependencies:** `chromium >= 59`,` wget >= 1.16`, `python3 >= 3.5`  (`google-chrome >= v59` works fine as well)

If you already have Google Chrome installed, or wish to use that instead of Chromium, follow the [Google Chrome Instructions](#google-chrome-instructions).

```bash
# On Mac:
brew cask install chromium  # If you already have Google Chrome/Chromium in /Applications/, skip this command
brew install wget python3

echo -e '#!/bin/bash\n/Applications/Chromium.app/Contents/MacOS/Chromium "$@"' > /usr/local/bin/chromium-browser  # see instructions for google-chrome below
chmod +x /usr/local/bin/chromium-browser
```

```bash
# On Ubuntu/Debian:
apt install chromium-browser python3 wget
```

```bash
# Check that everything worked:
chromium-browser --version && which wget && which python3 && which curl && echo "[√] All dependencies installed."
```

**2. Get your bookmark export file:**

Follow the instruction links above in the "Quickstart" section to download your bookmarks export file.

**3. Run the archive script:**

1. Clone this repo `git clone https://github.com/pirate/ArchiveBox`
2. Optionally clone the documentation locally as well `git clone https://github.com/pirate/ArchiveBox.wiki.git`
3. `cd ArchiveBox/`
4. `./archive ~/Downloads/bookmarks_export.html`

You may optionally specify a second argument to `archive.py export.html 153242424324` to resume the archive update at a specific timestamp.

If you have any trouble, see the [Troubleshooting](#troubleshooting) section at the bottom.