## Roadmap

▶️ *Comment here to discuss the contribution roadmap: [Official Roadmap Discussion](https://github.com/pirate/ArchiveBox/issues/120).*

If you feel like contributing a PR, some of these tasks are pretty easy.  Feel free to open an issue if you need help getting started in any way!

**Major upcoming changes:**

 - finalize python packaging to allow installing via pip and importing individual componenets
 - add an optional web GUI for managing sources, adding new links, and viewing the archive

**Minor upcoming changes:**
 - download closed-captions text from youtube videos
 - body text extraction using [fathom](https://hacks.mozilla.org/2017/04/fathom-a-framework-for-understanding-web-pages/)
 - auto-tagging based on important extracted words
 - audio & video archiving with `youtube-dl`
 - full-text indexing with elasticsearch/elasticlunr/ag
 - video closed-caption downloading on Youtube for full-text indexing of video content
 - automatic text summaries of article with nlp summarization library
 - featured image extraction
 - http support (from my https-only domain)
 - try wgetting dead sites from archive.org (https://github.com/hartator/wayback-machine-downloader)