# Troubleshooting

▶️ *If you need help or have a question, you can open an [issue](https://github.com/ArchiveBox/ArchiveBox/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc) or reach out on [Twitter](https://twitter.com/theSquashSH).*

What are you having an issue with?:

- [Installing](#Installing)
- [Configuration](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration)
- [Archiving Process](#Archiving)
- [Hosting the Archive](#Hosting-the-Archive)

---

## Installing

Make sure you've followed the Manual Setup guide in the [[Install]] instructions first.  Then check here for help depending on what component you need help with:

### Python

On some Linux distributions the python3 package might not be recent enough.
If this is the case for you, resort to installing a recent enough version manually.
```bash
add-apt-repository ppa:fkrull/deadsnakes && apt update && apt install python3.6
```
If you still need help, [the official Python docs](https://docs.python.org/3.6/using/unix.html) are a good place to start.

### Chromium/Google Chrome

For more info, see the [[Chromium Install]] page.

`archive.py` depends on being able to access a `chromium-browser`/`google-chrome` executable.  The executable used
defaults to `chromium-browser` but can be manually specified with the environment variable `CHROME_BINARY`:

```bash
env CHROME_BINARY=/usr/local/bin/chromium-browser ./archive ~/Downloads/bookmarks_export.html
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

3. If a version is displayed and it's `<59`, upgrade it:

```bash
apt upgrade chromium-browser -y
# OR
brew cask upgrade chromium-browser
```

4. If a version is displayed and it's `>=59`, make sure `archive.py` is running the right one:

```bash
env CHROME_BINARY=/path/from/step/1/chromium-browser ./archive bookmarks_export.html   # replace the path with the one you got from step 1
```


### Wget & Curl

If you're missing `wget` or `curl`, simply install them using `apt` or your package manager of choice.
See the "Manual Setup" instructions for more details.

If wget times out or randomly fails to download some sites that you have confirmed are online,
upgrade wget to the most recent version with `brew upgrade wget` or `apt upgrade wget`.  There is
a bug in versions `<=1.19.1_1` that caused wget to fail for perfectly valid sites.

## Archiving

### No links parsed from export file

Please open an [issue](https://github.com/ArchiveBox/ArchiveBox/issues) with a description of where you got the export, and
preferrably your export file attached (you can redact the links).  We'll fix the parser to support your format.

### Lots of skipped sites

If you ran the archiver once, it wont re-download sites subsequent times, it will only download new links.
If you haven't already run it, make sure you have a working internet connection and that the parsed URLs look correct.
You can check the `archive.py` output or `index.html` to see what links it's downloading.

If you're still having issues, try deleting or moving the `output/archive` folder (back it up first!) and running `./archive` again.

### Lots of errors

Make sure you have all the dependencies installed and that you're able to visit the links from your browser normally.
Open an [issue](https://github.com/ArchiveBox/ArchiveBox/issues) with a description of the errors if you're still having problems.

### Lots of broken links from the index

Not all sites can be effectively archived with each method, that's why it's best to use a combination of `wget`, PDFs, and screenshots.
If it seems like more than 10-20% of sites in the archive are broken, open an [issue](https://github.com/ArchiveBox/ArchiveBox/issues)
with some of the URLs that failed to be archived and I'll investigate.

### Removing unwanted links from the index

If you accidentally added lots of unwanted links into index and they slow down your archiving, you can use the `bin/purge` script to remove them from your index, which removes everything matching python regexes you pass into it. E.g: `bin/purge -r 'amazon\.com' -r 'google\.com'`. It would prompt before removing links from index, but for extra safety you might want to back up `index.json` first (or put in undex version control).

## Hosting the Archive

If you're having issues trying to host the archive via nginx, make sure you already have nginx running with SSL.
If you don't, google around, there are plenty of tutorials to help get that set up.  Open an [issue](https://github.com/ArchiveBox/ArchiveBox/issues)
if you have problem with a particular nginx config.
