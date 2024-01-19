# Install

ArchiveBox only has a few main dependencies apart from `python3`, and they can all be installed using your normal package manager.  It usually takes 1min to get up and running if you use the [helper script](#automatic-setup), or about 5min if you install everything [manually](#manual-setup).

<img src="https://lh4.googleusercontent.com/KWaqSJ_J9nSaGZugZWGR_mC18xxbGj2pVScriSzP8hX7KiUSw6L3VVL8rhDxQKIwxaCsfSFUO1B2pipEM4h7L-HJOGXo7yZK8a3DBVERwqfEZ8GxpeHPwh8P4LSkqVjPGRx5XYs" width="20%" align="right"/>

 - [Supported Systems](#supported-systems)
 - [Dependencies](#dependencies)
 - [Automatic Setup](#automatic-setup)
 - [Manual Setup](#manual-setup)
 - **[Docker Setup](#docker-setup)**

## Supported Systems

ArchiveBox officially supports the following operating systems:

<img src="https://lh4.googleusercontent.com/KWaqSJ_J9nSaGZugZWGR_mC18xxbGj2pVScriSzP8hX7KiUSw6L3VVL8rhDxQKIwxaCsfSFUO1B2pipEM4h7L-HJOGXo7yZK8a3DBVERwqfEZ8GxpeHPwh8P4LSkqVjPGRx5XYs" width="20%" align="right"/>

<img src="https://cdn0.iconfinder.com/data/icons/flat-round-system/512/freebsd-512.png" width="5%" align="right"/>
<img src="https://assets.ubuntu.com/v1/c5cb0f8e-picto-ubuntu.svg" width="5%" align="right"/>
<img src="https://i.imgur.com/Ue9BI7n.png" width="5%" align="right"/>

* [**macOS:**](#macos) >=10.12 (with homebrew)
* [**Linux:**](#ubuntudebian) Ubuntu, Debian, etc (with apt)
* [**BSD:**](#bsd) FreeBSD, OpenBSD, NetBSD etc (with pkg)

Other systems that are not officially supported but probably work to varying degrees:

<img src="https://i.imgur.com/WYSb96z.png" width="6%" align="right"/>
<img src="http://files.softicons.com/download/system-icons/web0.2ama-icons-by-chrfb/png/256x256/Operating%20System%20-%20Windows.png" width="5%" align="right"/>


 * Windows: Via [[Docker]], Docker in WSL2, bare WSL/WSL2, or even directly in batch/powershell with `pip` (if you're adventurous)
 * Other Linux distros: Fedora, SUSE, Arch, CentOS, etc.

<br/>

Platforms other than Linux, BSD, and macOS are untested, but you can probably get it working on them without too much effort.

It's recommended to use a filesystem with compression and/or deduplication abilities (e.g. ZFS or BTRFS) for maximum archive storage efficiency.

You will also need 500MB of RAM (bare minimum), though 2GB or greater recommended. You may be able to reduce the RAM requirements if you disable all the chrome-based archiving methods with `USE_CHROME=False`.

## Dependencies

Not all the dependencies are required for all modes. If you disable some archive methods you can avoid those dependencies, for example, if you set `FETCH_MEDIA=False` you don't need to install `youtube-dl`, and if you set `FETCH_[PDF,SCREENSHOT,DOM]=False` you don't need `chromium`.

<img src="https://avatars0.githubusercontent.com/u/1503512?s=200&v=4" width="10%" align="right"/>

 - `python3 >= 3.7`
 - `wget >= 1.16`
 - `chromium >= 59` (`google-chrome >= v59` works fine as well)
 - `youtube-dl`
 - `curl` (usually already on most systems)
 - `git` (usually already on most systems)

**More info:**
 - For help installing these, see the [Manual Setup](#manual-setup), [[Troubleshooting]] and [[Chromium Install]] pages.
 - To use specific binaries for dependencies, see the [Configuration: Dependencies](Configuration#dependency-options) page.
 - To disable unwanted dependencies, see the [Configuration: Archive Method Toggles](Configuration#archive-method-toggles) page.  

## Automatic Setup

If you're on Linux with `apt`, or macOS with `brew` there is an automatic setup script provided to install all the dependencies.
BSD, Windows, and other OS users should follow the [Manual Setup](#manual-setup) or [[Docker]] instructions.

```bash
# docker or the manual setup are preferred on all platforms now, if you want to use the old install script you can run:
curl https://raw.githubusercontent.com/pirate/ArchiveBox/master/bin/setup.sh | sh
``` 
The script explains what it installs beforehand, and will prompt for user confirmation before making any changes to your system.

<img src="https://i.imgur.com/VMTzm0G.png" width="99%"/>

After running the setup script, continue with the [[Quickstart]] guide...

## Manual Setup

If you don't like running random setup scripts off the internet (:+1:), you can follow these manual setup instructions.

### 1. Install dependencies

#### macOS
```bash
brew tap homebrew-ffmpeg/ffmpeg
brew install homebrew-ffmpeg/ffmpeg/ffmpeg --with-fdk-aac
brew install python3 git wget curl youtube-dl
brew install --cask chromium  # Skip this if you already have Google Chrome/Chromium installed in /Applications/
```

#### Ubuntu/Debian
```bash
apt install python3 python3-pip python3-distutils git wget curl youtube-dl
apt install chromium-browser  # Skip this if you already have Google Chrome/Chromium installed
```

#### BSD

FreeBSD:

```bash
pkg install python git wget curl youtube-dl 
pkg install chromium-browser  # Skip this if you already have Google Chrome/Chromium installed
```

OpenBSD:

```bash
pkg_add python3 git wget curl youtube-dl chromium
```

#### Install ArchiveBox using pip
```bash
python3 -m pip install --upgrade archivebox
```

#### Check that everything worked and the versions are high enough.
```bash
python3 --version | head -n 1 && 
git --version | head -n 1 && 
wget --version | head -n 1 && 
curl --version | head -n 1 && 
youtube-dl --version | head -n 1 && 
echo "[√] All dependencies installed."

archivebox version
```

If you have issues setting up Chromium / Google Chrome, see the [[Chromium Install]] page for more detailed setup instructions.

### 2. Get your bookmark export file

Follow the [[Quickstart]] guide to download your bookmarks export file containing a list of links to archive.

### 3. Run archivebox

```bash
# create a new folder to hold your data and cd into it
mkdir data && cd data
archivebox init
archivebox version
archivebox add < ~/Downloads/bookmarks_export.html
```

You can also use the `update` subcommand to resume the archive update at a specific timestamp `archivebox update --resume=153242424324.123`.

### Next Steps

 - Read [[Usage]] to learn how to use the ArchiveBox CLI and HTML output
 - Read [[Configuration]] to learn about the various archive method options
 - Read [[Scheduled Archiving]] to learn how to set up automatic daily archiving
 - Read [[Publishing Your Archive]] if you want to host your archive for others to access online
 - Read [[Troubleshooting]] if you encounter any problems


## Docker Setup

First, if you don't already have docker installed, follow the official install instructions for Linux, macOS, or Windows https://docs.docker.com/install/#supported-platforms.


Then see the [[Docker]] page for next steps.
