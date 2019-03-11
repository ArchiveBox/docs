## Roadmap

▶️ *Comment here to discuss the contribution roadmap: [Official Roadmap Discussion](https://github.com/pirate/ArchiveBox/issues/120).*

If you feel like contributing a PR, some of these tasks are pretty easy.  Feel free to open an issue if you need help getting started in any way!

**IMPORTANT**: *Please don't work on any of these major long-term tasks without [contacting me first](https://nicksweeting.com/blog#Contact-Me), work is already in progress for many of these, and I may have to reject your PR if it doesn't align with the existing work!*

---

### Major long-term changes
 - release `pip`, `apt`, and `brew` packaged distributions for installing ArchiveBox
 - switch to django + sqlite db with migrations system & json/html export for managing archive schema changes and persistence
 - finalize python packaging to allow installing via pip and importing individual components
 - add an optional web GUI for managing sources, adding new links, and viewing the archive
 - switch to sha256 of URL as unique link ID
 - support storing multiple snapshots of pages over time
 - support customer user puppeteer scripts to run while archiving (e.g. for expanding reddit threads, scrolling thread on twitter, etc)
 - support named collections of archived content with different user access permissions
 - support sharing archived assets via DHT + torrent / ipfs / ZeroNet / other sharing system

### Smaller planned features
 - support pushing pages to multiple 3rd party services using ArchiveNow instead of just archive.org
 - body text extraction to markdown (using [fathom](https://hacks.mozilla.org/2017/04/fathom-a-framework-for-understanding-web-pages/)?)
 - featured image / thumbnail extraction
 - auto-tagging links based on important/frequent keywords in extracted text (like pocket)
 - automatic article summary paragraphs from extracted text with nlp summarization library
 - full-text search of extracted text with elasticsearch/elasticlunr/ag
 - download closed-caption subtitles from Youtube and other video sites for full-text indexing of video content
 - try pulling dead sites from archive.org and other sources if original is down (https://github.com/hartator/wayback-machine-downloader)
 - And more in the [issues list](https://github.com/pirate/ArchiveBox/issues/)...