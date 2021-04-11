# Roadmap

<img src="https://i.imgur.com/es97GGV.png" width="20%" align="right"/>

▶️ *Comment here to discuss the contribution roadmap:  
[Official Roadmap Discussion](https://github.com/ArchiveBox/ArchiveBox/issues/120).*

---

## Planned Specification

(this is not set in stone, just a rough estimate)

### `v0.7: Schema improvements`
 - move config loading logic into settings.py
 - move all the extractors into "plugin" style folders that register their own config
 - right now, the paths of the extractor output are scattered all over the codebase, e.g. `output.pdf` (should be moved to constants at the top of the plugin config file)
 - make out_dir, link_dir, extractor_dir, naming consistent across codebase
 - remove `timestamps` as primary keys in favor of hashes, UUIDs, or some other slug
 - create a migration system for folder layout independent of the index (`mv` is atomic at the FS level, so we just need a `transaction.atomic(): move(oldpath, newpath); snap.data_dir = newpath; snap.save()`)
 - make `Tag` a real model `ManyToMany` with Snapshots
 - allow multiple Snapshots of the same site over time + CLI / UI to manage those, + migration from old style `#2020-01-01` hack to proper versioned snapshots
    
### `v0.8:  Security`
 - Add CSRF/CSP/XSS protection to rendered archive pages
 - Provide secure reverse proxy in front of archivebox server in docker-compose.yml
 - Create UX flow for users to setup session cookies / auth for archiving private sites
   - cookies for wget, curl, etc low-level commands
   - localstorage, cookies, indexedb setup for chrome archiving methods
        
### `v0.9:  Performance`
 - setup huey, break up archiving process into tasks on a queue that a worker pool executes
 - setup pyppeteer2 to wrap chrome so that it's not open/closed during each extractor

### `v1.0: Full headless browser control`
 - run user-scripts / extensions in the context of the page during archiving
 - community userscripts for unrolling twitter threads, reddit threads, youtube comment sections, etc.
 - pywb-based headless browser session recording and warc replay
 - archive proxy support
   - support sending upstream requests through an external proxy
   - support for exposing a proxy that archives all downstream traffic

...

### `v2.0 Federated or distributed archiving + paid hosted service offering`
 - ZFS / merkel tree for storing archive output subresource hashes
 - DHT for assigning merkel tree hash:file shards to nodes
 - tag system for tagging certain hashes with human-readable names, e.g. title, url, tags, filetype etc.
 - distributed tag lookup system




---

### Major long-term changes
 - ✅ release **`pip`, `apt`, `pkg`, and `brew` packaged distributions** for installing ArchiveBox
 - ✅ add an **optional web GUI** for managing sources, adding new links, and viewing the archive
 - ✅ switch to django + **sqlite db with migrations system** & json/html export for managing archive schema changes and persistence
 - modularize internals to allow importing individual components
 - switch to sha256 of URL as unique link ID
 - support **storing multiple snapshots** of pages over time
 - support **custom user puppeteer scripts to run while archiving** (e.g. for expanding reddit threads, scrolling thread on twitter, etc)
 - support named collections of archived content with different user access permissions
 - support sharing archived assets via DHT + torrent / ipfs / ZeroNet / other sharing system

### Smaller planned features
 - support pushing pages to multiple 3rd party services using ArchiveNow instead of just archive.org
 - ✅ body text extraction to markdown (using ~~[fathom](https://hacks.mozilla.org/2017/04/fathom-a-framework-for-understanding-web-pages/)~~ readability and mercury)
 - featured image / thumbnail extraction
 - auto-tagging links based on important/frequent keywords in extracted text (like pocket)
 - automatic article summary paragraphs from extracted text with nlp summarization library
 - ✅ full-text search of extracted text with ~~elasticsearch/elasticlunr/ag~~ sonic and ripgrep
 - ✅ download closed-caption subtitles from Youtube and other video sites (TODO: submit the subtitle files to the full-text search index)
 - try pulling dead sites from archive.org and other sources if original is down (https://github.com/hartator/wayback-machine-downloader)
 - And more in the [issues list](https://github.com/ArchiveBox/ArchiveBox/issues/)...

---

**IMPORTANT**: *Please don't work on any of these major long-term tasks without [contacting me first](https://nicksweeting.com/blog#Contact-Me), work is already in progress for many of these, and I may have to reject your PR if it doesn't align with the existing work!*


---

## Past Releases

To see how this spec has been scheduled / implemented / released so far, read these pull requests:
 - ✅ [v0.2.x](https://github.com/ArchiveBox/ArchiveBox/tree/483a3bef9e2b1a7b80611947a3be99b0cf4f9959) 
 - ✅ [v0.3.x](https://github.com/ArchiveBox/ArchiveBox/pull/197)
 - ✅ [v0.4.x](https://github.com/ArchiveBox/ArchiveBox/pull/207)
 - ✅ [v0.5.x](https://github.com/ArchiveBox/ArchiveBox/pull/552)
 - ✅ [v0.6.x](https://github.com/ArchiveBox/ArchiveBox/pull/680)
 - 🛠 v0.7.x next ...