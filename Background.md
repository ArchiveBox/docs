## Details

`archive.py` is a script that takes a [Pocket-format](https://getpocket.com/export), [JSON-format](https://pinboard.in/export/), [Netscape-format](https://msdn.microsoft.com/en-us/library/aa753582(v=vs.85).aspx), or RSS-formatted list of links, and downloads a clone of each linked website to turn into a browsable archive that you can store locally or host online.

The archiver produces an output folder `output/` containing an `index.html`, `index.json`, and archived copies of all the sites,
organized by timestamp bookmarked.  It's Powered by [headless](https://developers.google.com/web/updates/2017/04/headless-chrome) Chromium and good 'ol `wget`.

For each sites it saves:

 - wget of site, e.g. `en.wikipedia.org/wiki/Example.html` with .html appended if not present
 - `output.pdf` Printed PDF of site using headless chrome
 - `screenshot.png` 1440x900 screenshot of site using headless chrome
 - `output.html` DOM Dump of the HTML after rendering using headless chrome
 - `archive.org.txt` A link to the saved site on archive.org
 - `audio/` and `video/` for sites like youtube, soundcloud, etc. (using youtube-dl) (WIP)
 - `code/` clone of any repository for github, bitbucket, or gitlab links (WIP)
 - `index.json` JSON index containing link info and archive details
 - `index.html` HTML index containing link info and archive details (optional fancy or simple index)

Wget doesn't work on sites you need to be logged into, but chrome headless does, see the [Configuration](#configuration)* section for `CHROME_USER_DATA_DIR`.

**Large Exports & Estimated Runtime:** 

I've found it takes about an hour to download 1000 articles, and they'll take up roughly 1GB.  
Those numbers are from running it single-threaded on my i5 machine with 50mbps down.  YMMV.  

You can run it in parallel by using the `resume` feature, or by manually splitting export.html into multiple files:
```bash
./archive export.html 1498800000 &  # second argument is timestamp to resume downloading from
./archive export.html 1498810000 &
./archive export.html 1498820000 &
./archive export.html 1498830000 &
```
Users have reported running it with 50k+ bookmarks with success (though it will take more RAM while running).

If you already imported a huge list of bookmarks and want to import only new
bookmarks, you can use the `ONLY_NEW` environment variable. This is useful if
you want to import a bookmark dump periodically and want to skip broken links
which are already in the index.

## Info & Motivation

This is basically an open-source version of [Pocket Premium](https://getpocket.com/premium) (which you should consider paying for!).
I got tired of sites I saved going offline or changing their URLS, so I started
archiving a copy of them locally now, similar to The Way-Back Machine provided
by [archive.org](https://archive.org).  Self hosting your own archive allows you to save
PDFs & Screenshots of dynamic sites in addition to static html, something archive.org doesn't do.

Now I can rest soundly knowing important articles and resources I like wont dissapear off the internet.

My published archive as an example: [archive.sweeting.me](https://archive.sweeting.me).