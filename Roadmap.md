## Roadmap

▶️ *Comment here to discuss the contribution roadmap: [Official Roadmap Discussion](https://github.com/pirate/ArchiveBox/issues/120).*

If you feel like contributing a PR, some of these tasks are pretty easy.  Feel free to open an issue if you need help getting started in any way!

### Major upcoming changes
 - switch to django + sqlite db with migrations system & json/html export for managing archive schema changes and persistence
 - finalize python packaging to allow installing via pip and importing individual components
 - add an optional web GUI for managing sources, adding new links, and viewing the archive
 - switch to sha256 of URL as unique link ID
 - support storing multiple snapshots of pages over time
 - support customer user puppeteer scripts to run while archiving (e.g. for expanding reddit threads, scrolling thread on twitter, etc)

### Minor upcoming changes
 - support pushing pages to multiple 3rd party services using ArchiveNow instead of just archive.org
 - body text extraction using [fathom](https://hacks.mozilla.org/2017/04/fathom-a-framework-for-understanding-web-pages/)
 - auto-tagging based on important extracted words
 - full-text indexing with elasticsearch/elasticlunr/ag
 - video closed-caption downloading on Youtube for full-text indexing of video content
 - automatic text summaries of article with nlp summarization library
 - featured image extraction
 - try wgetting dead sites from archive.org (https://github.com/hartator/wayback-machine-downloader)
 - And more in the [issues list](https://github.com/pirate/ArchiveBox/issues/)...