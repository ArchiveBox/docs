ArchiveBox only has a few main dependencies apart from `python3`, and they can all be installed using your normal package manager.  It usually takes 1min to get up and running if you use the [helper script](#automatic-setup), or about 5min if you install everything [manually](#manual-setup).

<img src="https://lh4.googleusercontent.com/KWaqSJ_J9nSaGZugZWGR_mC18xxbGj2pVScriSzP8hX7KiUSw6L3VVL8rhDxQKIwxaCsfSFUO1B2pipEM4h7L-HJOGXo7yZK8a3DBVERwqfEZ8GxpeHPwh8P4LSkqVjPGRx5XYs" width="20%" align="right"/>

 - [System Support](#system-support)
 - [Dependencies](#dependencies)
 - [Automatic Setup](#automatic-setup)
 - [Manual Setup](#manual-setup)
 - [Docker Setup](#docker-setup)

## System Support

ArchiveBox officially supports the following operating systems:

<img src="https://cdn0.iconfinder.com/data/icons/flat-round-system/512/freebsd-512.png" width="5%" align="right"/>
<img src="https://assets.ubuntu.com/v1/c5cb0f8e-picto-ubuntu.svg" width="5%" align="right"/>
<img src="https://i.imgur.com/Ue9BI7n.png" width="5%" align="right"/>

* **macOS:** >=10.12 (with homebrew)
* **Linux:** Ubuntu, Debian, etc (with apt)
* **BSD:** FreeBSD, OpenBSD, NetBSD etc (with pkg)

Other systems that are not officially supported but probably work to varying degrees:

<img src="https://camo.githubusercontent.com/fa6d5c12609ed8a3ba1163b96f9e9979b8f59b0d/687474703a2f2f7765732e696f2f566663732f636f6e74656e74" width="6%" align="right"/>
<img src="http://files.softicons.com/download/system-icons/web0.2ama-icons-by-chrfb/png/256x256/Operating%20System%20-%20Windows.png" width="5%" align="right"/>


 * Windows: Via [[Docker]] or WSL
 * Other Linux distros: Fedora, SUSE, Arch, CentOS, etc.

<br/>

Platforms other than Linux, BSD, and macOS are untested, but you can probably get it working on them without too much effort.

## Dependencies

Not all the dependencies are required for all modes. If you disable some archive methods you can avoid those dependencies, for example, if you set `FETCH_MEDIA=False` you don't need to install `youtube-dl`, and if you set `FETCH_[PDF,SCREENSHOT,DOM]=False` you don't need `chromium`.

 - `python3 >= 3.5`
 - `wget >= 1.16`
 - `chromium >= 59` (`google-chrome >= v59` works fine as well)
 - `youtube-dl`
 - `curl` (usually already on most systems)
 - `git` (usually already on most systems)

**More info:**
 - To use specific binaries for dependencies, see the [Configuration: Dependencies](Configuration#dependency-options) page.
 - To disable unwanted dependencies, see the [Configuration: Archive Method Toggles](Configuration#archive-method-toggles) page.  
 - For help installing dependencies, see the [[Troubleshooting]] and [[Chromium Install]] pages.

## Automatic Setup

If you're on Linux with `apt`, or macOS with `brew` there is an automatic setup script `./bin/setup` provided to install all the dependencies.

Running it will explain what it installs and will prompt you to continue before making any changes to your system.

After running `./bin/setup`, continue with the [[Quickstart]] guide...

BSD, Windows, and other users should follow the [Manual Setup](#manual-setup) or [[Docker]] instructions.

## Manual Setup

If you don't like running random setup scripts off the internet (:+1:), you can follow these manual setup instructions.

**1. Install dependencies:** 

```bash
# On Ubuntu/Debian:
apt install chromium-browser python3 wget curl youtube-dl git
```

```bash
# On Mac:
brew cask install chromium  # If you already have Google Chrome/Chromium in /Applications/, skip this command
brew install python3 wget curl youtube-dl git

echo -e '#!/bin/bash\n/Applications/Chromium.app/Contents/MacOS/Chromium "$@"' > /usr/local/bin/chromium-browser
chmod +x /usr/local/bin/chromium-browser
```

```bash
# Check that everything worked and the versions are high enough:
chromium-browser --version && which wget && which python3 && which curl && echo "[√] All dependencies installed."
```

If you have issues setting up Chromium / Google Chrome, see the [[Chromium Install]] page for more detailed setup instructions.

**2. Get your bookmark export file:**

Follow the [[Quickstart]] guide to download your bookmarks export file containing a list of links to archive.

**3. Run the archive script:**

1. Clone this repo `git clone https://github.com/pirate/ArchiveBox`
2. `cd ArchiveBox/`
3. `./archive ~/Downloads/links_list.html`

You may optionally specify a second argument to `archive.py export.html 153242424324` to resume the archive update at a specific timestamp.

**Next Steps:**

 - Read [[Configuration]] to learn about the various archive method options
 - Read [[Scheduled Archiving]] to learn how to set up automatic daily archiving
 - Read [[Publishing Your Archive]] if you want to host your archive for others to access online
 - Read [[Troubleshooting]] if you encounter any problems


## Docker Setup

First, if you don't already have docker installed, follow the official install instructions for Linux, macOS, or Windows https://docs.docker.com/install/#supported-platforms.


Then see the [[Docker]] page for next steps.