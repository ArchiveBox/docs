## System Support

ArchiveBox officially supports the following operating systems:

* Linux: e.g. Ubuntu, Debian, etc
* BSD: FreeBSD, OpenBSD, NetBSD etc
* macOS

You can run it on Windows and other systems via Docker containers or Vagrant VMs if they have support for those technologies.  I haven't tested it on distros like Fedora, SUSE, Arch, CentOS, etc but you can probably get it working on those as well.

The most important dependency is Chrome headless, so if you can figure out how to get Chrome headless and Python 3 running on your system, then ArchiveBox is likely to work just fine.

## Automatic Setup

Run `./bin/setup` to install all dependencies automatically on Linux (with `apt`) or macOS (with `brew`).

BSD and Windows users should follow the manual setup and Docker instructions respectively.

## Docker Setup

Docker support for ArchiveBox is in beta, I'll update it as we improve the ergonomics and add an example `docker-compose.yml` file for serving the archive with nginx.

Currently, you can run ArchiveBox with Docker like this:

```bash
docker build github.com/pirate/ArchiveBox -t ArchiveBox
docker volume create archivebox-data
docker run -v archivebox-data:/home/chromeuser/app/archivebox/output ArchiveBox 'https://example.com/some/rss/feed.xml'
```

It's not perfect yet, I still have to improve the system for passing in link files to parse, right now you have to put them in the data volume and then reference them by their path inside the container to get ArchiveBox to find them:

```bash
docker run -v archivebox-data:/home/chromeuser/app/archiver/output ArchiveBox /home/chromeuser/app/archivebox/output/downloads/path-to-links.json
```

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

Follow the instruction in the "Quickstart" section to download your bookmarks export file containing a list of links to archive.

**3. Run the archive script:**

1. Clone this repo `git clone https://github.com/pirate/ArchiveBox`
2. `cd ArchiveBox/`
3. `./archive ~/Downloads/links_list.html`

You may optionally specify a second argument to `archive.py export.html 153242424324` to resume the archive update at a specific timestamp.

If you have any trouble, see the [Troubleshooting](#troubleshooting) section at the bottom.