# Troubleshooting

▶️ *If you need help or have a question, you can open an [issue](https://github.com/ArchiveBox/ArchiveBox/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc) or reach out on [Twitter](https://twitter.com/theSquashSH).*

What are you having an issue with?:

- [Installing ArchiveBox](#Installing)
- [Upgrading ArchiveBox](https://github.com/ArchiveBox/ArchiveBox/wiki/Upgrading-or-Merging-Archives)
- [Configuring ArchiveBox](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration)
- [Archiving content with ArchiveBox](#Archiving)
- [Hosting your collection publicly](#Hosting-the-Archive)
- [Database and filesystem issues](https://github.com/ArchiveBox/ArchiveBox/wiki/Upgrading-or-Merging-Archives#database-troubleshooting)

---

## Installing

If using `archivebox` without Docker, make sure you've followed the full guide in the [[Install]] instructions first.  Then check here for help depending on what component you need help with.

Then make sure `archivebox` is installed available in your `$PATH`.
```bash
brew info archivebox     # show info about the brew-installed version of archivebox
pip show archivebox      # show info about the pip-installed version of archivebox

echo $PATH               # show the directories your system is searching for binaries
which -a archivebox      # show all installed archivebox binaries available
which archivebox         # show which archivebox binary is being called
```
**⭐️ Show the full archivebox version info + info about all installed dependencies:**
```bash
archivebox version       # shows lots of useful info about installed dependencies and more
```
(ensure the version shown is the most recent available from [Releases](https://github.com/ArchiveBox/ArchiveBox/releases))



### Python

Make sure you have at least Python 3.9 installed on your system.

```bash
python3 --version
pip --version
pip install --upgrade pip setuptools
```

If you still need help getting Python installed, [the official Python docs](https://docs.python.org/3.9/using/unix.html) are a good place to start.

### Chromium/Google Chrome

For more info, see the [[Chromium Install]] page.

ArchiveBox depends on being able to access a `chromium-browser`/`google-chrome` executable.  The executable used
defaults to `chromium-browser` but can be manually specified with the environment variable `CHROME_BINARY`:

```bash
env CHROME_BINARY=/usr/local/bin/chromium-browser archivebox add ~/Downloads/bookmarks_export.html
```

1. Test to make sure you have Chrome on your `$PATH` with:

```bash
which chromium-browser || which google-chrome
```
If no executable is displayed, follow the setup instructions to install and link one of them.

2. If a path is displayed, the next step is to check that it's runnable:

```bash
chromium-browser --version || google-chrome --version
```
If no version is displayed, try the setup instructions again, or confirm that you have permission to access chrome.

3. If a version is displayed and it's `<111`, upgrade it:

```bash
apt upgrade chromium-browser -y
# OR
brew cask upgrade chromium-browser
```

4. If a version is displayed and it's `>=111`, make sure ArchiveBox is running the right one:

```bash
env CHROME_BINARY=/path/from/step/1/chromium-browser archivebox version   # replace the path with the one you got from step 1
```


### Wget & Curl

If you're missing `wget` or `curl`, simply install them using `apt` or your package manager of choice.
See the "Manual Setup" instructions for more details.

If wget times out or randomly fails to download some sites that you have confirmed are online,
upgrade wget to the most recent version with `brew upgrade wget` or `apt upgrade wget`.  There is
a bug in versions `<=1.19.1_1` that caused wget to fail for perfectly valid sites.

### NPM Dependencies

NPM dependencies like `readability`, `singlefile`, and `mercury` are installed in you data directory by `archivebox setup`.

Make sure you have installed NodeJS + NPM first, here are their [official install docs](https://nodejs.org/en/download/package-manager/).

```bash
node --version         # make sure you have node >=19 installed
npm --version          # make sure you have npm installed

cd ~/archivebox/data   # go into your data directory
archivebox setup       # install all runtime dependencies
# equivalent to:
# curl -fsSL 'https://raw.githubusercontent.com/ArchiveBox/ArchiveBox/main/archivebox/package.json' > package.json
# npm install

# install npm dependencies should then be present in ~/archivebox/data/node_modules/.bin
archivebox version     # show version full info to make sure they're loaded correctly
```

---

## Archiving

### No links parsed from export file

Please open an [issue](https://github.com/ArchiveBox/ArchiveBox/issues) with a description of where you got the export, and
preferrably your export file attached (you can redact the links).  We'll fix the parser to support your format.

### Lots of skipped sites

If you ran the archiver once, it wont re-download sites subsequent times, it will only download new links.
If you haven't already run it, make sure you have a working internet connection and that the parsed URLs look correct.
You can check the ArchiveBox stdout logs or the Web UI to see what links it's downloading.

If you're still having issues, try deleting or moving the `./archive` folder (back it up first!) and running `archivebox init` again.

### Lots of errors

Make sure you have all the dependencies installed and that you're able to visit the links from your browser normally.
Open an [issue](https://github.com/ArchiveBox/ArchiveBox/issues) with a description of the errors if you're still having problems.

### Lots of broken links from the index

Not all sites can be effectively archived with each method, that's why it's best to use a combination of `wget`, PDFs, and screenshots.
If it seems like more than 10-20% of sites in the archive are broken, open an [issue](https://github.com/ArchiveBox/ArchiveBox/issues)
with some of the URLs that failed to be archived and I'll investigate.

### Removing unwanted links from the index

`archivebox remove --help`

## Hosting the Archive

If you're having issues trying to host the archive via nginx, make sure you already have nginx running with SSL.
If you don't, google around, there are plenty of tutorials to help get that set up.  Open an [issue](https://github.com/ArchiveBox/ArchiveBox/issues)
if you have problem with a particular nginx config.

### Other database or filesystem issues

See here for more info:

- https://github.com/ArchiveBox/ArchiveBox/wiki/Upgrading-or-Merging-Archives
- https://github.com/ArchiveBox/ArchiveBox/wiki/Upgrading-or-Merging-Archives#database-troubleshooting
- https://github.com/ArchiveBox/ArchiveBox/wiki/Upgrading-or-Merging-Archives#repairing-a-corrupted-database
- https://github.com/ArchiveBox/ArchiveBox/wiki/Upgrading-or-Merging-Archives#modify-the-archivebox-sqlite3-db-directly
- https://github.com/ArchiveBox/ArchiveBox/wiki/Upgrading-or-Merging-Archives#merge-two-or-more-existing-archives
- https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#python-shell-usage
- https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#sql-shell-usage
- https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview#do-not-run-as-root
- https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview#output-folder