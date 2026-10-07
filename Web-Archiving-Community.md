# Web Archiving Community

<div align="center" style="text-align: center">

💬 <i><b>Join us on our new ArchiveBox community chat server: https://Zulip.ArchiveBox.io</b></i>

🔢 **Just getting started and want to learn more about why Web Archiving is important? <br/>** &nbsp; &nbsp;&nbsp; Check out this article: [On the Importance of Web Archiving](https://items.ssrc.org/parameters/on-the-importance-of-web-archiving/).

</div>

---

The internet archiving community is surprisingly far-reaching and almost universally friendly! It has some overlap with the scraping and OSINT worlds, but it's also kinda its own thing.

Whether you want to learn which organizations are the big players in the web archiving space, want to find a specific open source tool for your web archiving need, or just want to see where archivists hang out online, this is my attempt at an index of the entire web archiving community. The alternatives and recent reading list were reviewed in October 2026; older resources are retained for historical context.

<img src="https://imgur.zervice.io/duS8Lm7.png" width="200px" align="right" style="float: right; margin: 5px"/>

<a id="contents"></a>

- [The Master Lists](#the-master-lists)
  *Community-maintained indexes of web archiving tools and groups by IIPC, COPTR, ArchiveTeam, Wikipedia, & the ASA.* 

- [Web Archiving Software](#web-archiving-projects)
  *Applications, services and tools grouped by purpose.*
  - [Personal archives & bookmarks](#personal-archives-and-bookmarks)
  - [Page capture & website crawling](#page-capture-and-website-crawling)
  - [Public archives & hosted services](#public-archives-and-hosted-services)
  - [Media, social & specialist archives](#media-social-and-specialist-archives)
  - [Replay, developer tools & integrations](#replay-developer-tools-and-integrations)

- [Reading List](#reading-list)
  *Articles, posts, and blogs relevant to ArchiveBox and web archiving in general.*
  - [Blogs](#blogs-friends-of-archivebox)
  - [Articles](#articles-we-like-about-internet-archiving)
  - [ArchiveBox-Specific Posts, Tutorials, and Guides](#archivebox-specific-posts-tutorials-and-guides)
  - [ArchiveBox Discussions in News & Social Media](#archivebox-discussions-in-news--social-media)

- [Articles in Other Languages](#articles-in-other-languages)
  [Chinese](#chinese) · [French](#french) · [German](#german) · [Italian](#italian) · [Japanese](#japanese) · [Polish](#polish) · [Portuguese](#portuguese) · [Russian](#russian) · [Spanish](#spanish)

- [Communities](#communities)
  *A collection of the most active internet archiving communities and initiatives.*
  - [Most Active Web-Archiving Communities](#most-active-communities)
  - [Other Web Archiving Communities](#web-archiving-communities)
  - [General Archiving Foundations, Coalitions, Initiatives, and Institutes](#general-archiving-foundations-coalitions-initiatives-and-institutes)

---

## The Master Lists

<img src="https://i.pinimg.com/originals/5d/8f/ae/5d8fae9a42210eb0320960b23e3fe236.jpg" width="230px" align="right" style="float: right; margin: 5px"/>

Indexes of archiving institutions and software maintained by other people.  If there's anything archivists love doing, it's making lists.

 - **[COPTR Wiki of Web Archiving Tools](http://coptr.digipres.org/Category:Tools) (COPTR)**  
 - **[Awesome Web Archiving Tools](https://github.com/iipc/awesome-web-archiving) (IIPC)**  
 - **[My up-to-date list of starred archiving github projects](https://github.com/stars/pirate/lists/internet-archiving)**
 - [Spreadsheet Comparison of Archiving Tools](https://github.com/datatogether/research/tree/master/web_archiving) (DataTogether)
 - [Awesome Web Crawling Tools](https://github.com/BruceDone/awesome-crawler)
 - [Awesome Web Scraping Tools](https://github.com/duyetdev/awesome-web-scraper)
 - [ArchiveTeam's List of Software](https://www.archiveteam.org/index.php?title=Software) (ArchiveTeam.org)  
 - [List of Web Archiving Initiatives](https://en.wikipedia.org/wiki/List_of_Web_archiving_initiatives) (Wikipedia.org)  
 - [Directory of Archiving Organizations](https://www2.archivists.org/assoc-orgs) (American Society of Archivists)  

---

## Web Archiving Projects

<div align="center">
<img src="https://github.com/Pocket.png" width="50px"/> &nbsp; &nbsp;
<img src="https://assets.ifttt.com/images/channels/23/icons/large.png" width="50px"/> &nbsp; &nbsp;
<img src="https://avatars1.githubusercontent.com/u/8275533?s=400&v=4" width="50px"/> &nbsp; &nbsp;
<img src="https://upload.wikimedia.org/wikipedia/commons/b/b8/Logo-wallabag-svg.svg" width="50px"/>
</div>

Browse by purpose: [personal archives](#personal-archives-and-bookmarks), [page capture and crawling](#page-capture-and-website-crawling), [public and hosted services](#public-archives-and-hosted-services), [media and social archives](#media-social-and-specialist-archives), or [replay and developer tools](#replay-developer-tools-and-integrations).

Open-source, self-hosted and commercial tools are grouped together by their main use. Each project has one primary entry; capture formats and capabilities vary, so check its documentation before choosing. Inclusion is not a personal endorsement of every tool.

> See also [my starred archiving projects](https://github.com/stars/pirate/lists/internet-archiving). This page selects relevant applications and utilities; the stars list also includes supporting infrastructure and experiments.

<a id="paid-alternatives"></a>
**Paid alternatives:** options include Muse among personal archives, StreamStash among media tools, Hunchly and Fossilo among capture tools, and the managed services below. Pricing notes stay with each project.

<a id="personal-archives-and-bookmarks"></a>
<a id="bookmarking-services"></a>

### Personal archives & bookmarks

Applications for saving, organizing, annotating and searching your own collections.

**Archive and bookmark managers**

- **[Linkwarden](https://github.com/linkwarden/linkwarden)** Modern bookmarking UI with singlefile archiving
- [Karakeep (formerly Hoarder)](https://github.com/karakeep-app/karakeep) Self-hosted bookmark manager for links, notes, images and PDFs, with saved page content, search and optional AI tagging.
- [Readeck](https://codeberg.org/readeck/readeck) Self-hosted read-later app preserving readable page content, with highlights, collections, full-text search and EPUB export.
- [Grimoire](https://github.com/goniszewski/grimoire) Local-first bookmark and content manager with readable content extraction, notes, tags and keyword/semantic search.
- [Django Link Archive](https://github.com/rumca-js/Django-link-archive) Self-hosted link database and RSS reader with public-archive integration and yt-dlp downloads.
- [Wallabag](https://wallabag.org) / [Wallabag.it](https://wallabag.it) Self-hostable web archiving server that can import via RSS
- [Shaarli](https://github.com/shaarli/Shaarli) Self-hostable bookmark tagging, archiving, and sharing service
- **[Reminiscence](https://github.com/kanishka-linux/reminiscence/) extremely similar to ArchiveBox, uses a Django backend + UI and provides auto-tagging and summary features with NLTK**
- **[Shaarchiver](https://github.com/nodiscc/shaarchiver) very similar project that archives Firefox, Shaarli, or Delicious bookmarks and all linked media, generating a markdown/HTML index**
- **[Archivy](https://github.com/archivy/archivy) Python-based self-hosted knowledge base embedded into your filesystem**
- [Shiori](https://github.com/go-shiori/shiori) Simple bookmark manager + readability archiver built with Go (like a clone of Pocket)
- [LinkAce](https://www.linkace.org/) A self-hosted bookmark management tool that saves snapshots to archive.org
- [LinkDing](https://github.com/sissbruecker/linkding) Self-hosted bookmark manager that is designed be to be minimal, fast, and easy to set up using Docker.
- [LinkWallet](https://github.com/tardisx/linkwallet) A self-hosted bookmark database with full-text page content search and limited archiving features
- [Espial](https://github.com/jonschoning/espial) Bookmark manager and search tool with limited archiving features
- [Herodotus](https://github.com/alaskanpuffin/herodotus-core) Django-based web archiving tool with a focus on collecting text-based content
- [Buku](https://github.com/jarun/buku) Browser-independent bookmark manager CLI written in Python3 and SQLite3
- [NeonLink](https://github.com/AlexSciFier/neonlink) Simple self-hosted bookmark management + [Benotes](https://noted.lol/benotes/) note-taking app with limited archiving features
- [Erised](https://github.com/marvelm/erised) Super simple CLI utility to bookmark and archive webpages
- **[Wayback](https://github.com/wabarc/wayback) Archiving in style like ArchiveBox, but with a chat.**

**Reading, notes and research**

- **[Gosuki](https://github.com/blob42/gosuki) A lightweight, open-source, privacy-first bookmark manager that unifies bookmarks across multiple browsers**; its [ArchiveBox integration](https://gosuki.net/docs/features/archiving/archive-box/) can automatically archive tagged bookmarks.
- **[Pinboard](https://pinboard.in) Bookmarking tool that provides archiving in a paid version, run by a single independent developer**
- **[Raindrop](https://raindrop.io) Bookmarking tool with archiving in their paid version, run by a company est. 2011**
- [Instapaper](https://www.instapaper.com) Bookmarking alternative to Pocket/Pinboard (with no archiving)
- [ReadWise](https://readwise.io/) A paid Pocket/Pinboard alternative that includes article snippet and highlight saving
- [Diigo](https://www.diigo.com/) Another brookmarking/annotation service with archiving as a paid feature
- **[Memex by Worldbrain.io](https://github.com/WorldBrain/Memex) a beautiful, user-friendly browser extension that archives all history with full-text search, annotation support, and more**
- **[Hypothes.is](https://web.hypothes.is/) a web/pdf/ebook annotation tool that also archives content**
- [Trilium Notes](https://github.com/TriliumNext/Trilium) Personal web UI based knowledge-base with web clipping and note-taking
- [Perkeep](https://perkeep.org/) "Perkeep lets you permanently keep your stuff, for life."
- [Zotero](https://www.zotero.org/) collect, organize, cite, and share research (mainly for technical/scientific papers & citations)
- [TiddlyWiki](https://tiddlywiki.com/) Non-linear bookmark and note-taking tool with archiving support
- [Joplin](https://joplinapp.org/) Desktop + mobile app for knowledge-base-style info collection and notes (w/ optional plugin for archiving)
- [Muse](https://www.theodorehq.com/muse/) Paid macOS visual bookmark and media manager with browser clipping, local files, OCR/search and on-device tagging; one-time purchase with a free trial.
- https://github.com/karlicoss/promnesia A browser extension that [collects and collates all the URLs you visit](https://beepb00p.xyz/promnesia.html) into a hierarchical/graph structure with metadata
- [Timelinize](https://github.com/timelinize/timelinize) Collect and browse personal data locally on a timeline; successor to the archived [Timeliner](https://github.com/mholt/timeliner).
- https://github.com/karlicoss/grasp capture webpages from Firefox and Chrome into Org-mode documents

**Historical bookmarking resources**

- ~[Pocket Premium](https://getpocket.com) Bookmarking tool that provides an archiving service in their paid version, run by Mozilla~
- [Sheetsee-Pocket](http://jlord.us/sheetsee-pocket/) project that provides a pretty auto-updating index of your Pocket links (without archiving them)
- [Pocket -> IFTTT -> Dropbox](https://christopher.su/2013/saving-pocket-links-file-day-dropbox-ifttt-launchd/) Post by Christopher Su on his Pocket saving IFTTT recipe
- https://en.wikipedia.org/wiki/Furl

---

<a id="page-capture-and-website-crawling"></a>
<a id="other-archivebox-alternatives"></a>
<a id="from-the-archiveorg--archive-it-teams"></a>
<a id="from-webrecorder"></a>
<a id="from-rhizomeorg-conifer"></a>
<a id="from-the-old-dominion-university-web-science-team"></a>

### Page capture & website crawling

Tools for capturing individual pages, recording browsing sessions and crawling entire websites.

**Browser capture and page saving**

- **[ArchiveWeb.page](https://webrecorder.net/archivewebpage)** Chrome extension for manual, interactive archiving of websites as you browse the web. Good for capturing high-fidelity complex interactions
- **[SingleFile](https://github.com/gildas-lormeau/SingleFile/) Web Extension / CLI util for Firefox and Chrome to save a web page as a single HTML file**
- [Hoardy-Web](https://github.com/Own-Data-Privateer/hoardy-web) Browser extension and local tools that capture HTTP requests/responses for offline replay, mirroring and indexing, including POST traffic.
- [WebScrapBook](https://github.com/danny0838/webscrapbook) Browser extension for saving, organizing, annotating and editing page captures locally or with a backend server.
- [Packrat](https://github.com/operating-function/packrat) Chromium extension for archiving browsing history using ArchiveWeb.page capture and ReplayWeb.page replay.
- [Diskernet](https://github.com/dosyago/DiskerNet) Archiving tool that uses the Chrome debugger protocol to save each page as-loaded in the browser (formerly 22120 by c0fe or i5ik)
- **[warcreate](https://github.com/machawk1/warcreate) a Chrome extension for creating WARCs from any webpage**
- [Monolith](https://github.com/Y2Z/monolith) CLI tool for saving complete web pages as a single HTML file
- [Obelisk](https://github.com/go-shiori/obelisk) Go package and CLI tool for saving web page as single HTML file
- [Percollate](https://github.com/danburzo/percollate) A command-line tool to turn web pages into beautiful, readable PDF, EPUB, or HTML docs.
- [Monolith of Web](https://github.com/rhysd/monolith-of-web) Chrome extension using Monolith compiled to WebAssembly to save a static page as one HTML file.
- https://github.com/vrtdev/save-page-state A Chrome extension for saving the state of a page in multiple formats

**Crawlers and collection platforms**

- **[Browsertrix](https://webrecorder.net/browsertrix)** Fully integrated (self hostable) SaaS web archiving platform
- **[Conifer by Rhizome.org](https://conifer.rhizome.org/)** **An open-source personal archiving server that uses pywb under the hood.** [Previously affiliated with Webrecorder](https://blog.conifer.rhizome.org/2020/06/11/webrecorder-conifer.html)
- [WAIL](https://machawk1.github.io/wail/) Web archiver GUI using Heritrix and OpenWayback
- [WAIL (Electron)](https://github.com/n0tan3rd/wail) Electron app version of the original [wail](https://github.com/machawk1/wail) for creating and interacting with web archives
- [Sosse](https://github.com/biolds/sosse) Self-hosted Selenium crawler and search engine with recurring crawls, authenticated browsing, locally rewritten HTML archives and downloaded assets.
- **[Heritrix](https://github.com/internetarchive/heritrix3) The king of internet archiving crawlers, powers the Wayback Machine**
- **[Brozzler](https://github.com/internetarchive/brozzler) chrome headless crawler + WARC archiver maintained by Archive.org**
- [Grab-Site](https://github.com/ArchiveTeam/grab-site) An easy preconfigured web crawler designed for backing up websites
- [Zeno](https://github.com/internetarchive/Zeno) Go crawler for broad crawls or individual pages, recording HTTP traffic to WARC.
- **[Browsertrix Crawler](https://github.com/webrecorder/browsertrix-crawler)** Command-line crawling application that powers Browsertrix's core crawling features
- [Squidwarc](https://github.com/N0taN3rd/Squidwarc) User-scriptable, archival crawler using Chrome
- **[Photon](https://github.com/s0md3v/Photon) a fast crawler with archiving and asset extraction support**
- **[Scoop](https://github.com/harvard-lil/scoop)** Create high-fidelity WARC/WACZ captures using a playwright browser, with support for signing, media extraction, PDFs, etc. ([by the Perma.cc team](https://lil.law.harvard.edu/blog/2023/04/13/scoop-witnessing-the-web/))
- [kage](https://github.com/tamnd/kage) CLI website mirror using headless Chrome to save static DOM snapshots and assets for offline viewing.
- [ReadableWebProxy](https://github.com/fake-name/ReadableWebProxy) A proxying archiver that downloads content from sites and can snapshot multiple versions of sites over time
- [Headless Chrome Crawler](https://github.com/yujiosaka/headless-chrome-crawler) distributed web crawler built on puppeteer with screenshots
- [WWWofle](http://www.gedanken.org.uk/software/wwwoffle/) old proxying recorder software similar to ArchiveBox
- [Hunchly](https://www.hunch.ly/) A paid web archiving / session recording tool designed for OSINT
- [Fossilo](https://www.fossilo.com/) A commercial archiving solution that appears to be very similar to ArchiveBox

---

<a id="public-archives-and-hosted-services"></a>
<a id="other-public-archiving-services"></a>

### Public archives & hosted services

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Archive.is.jpg/250px-Archive.is.jpg" width="150px" align="right" style="float: right; margin: 5px"/>

Find existing captures, submit pages to public archives, or use managed preservation and monitoring services.

**Public archives and historical lookup**

- **[Archive.org](https://archive.org) The O.G. Wayback Machine provided publicly by the Internet Archive (Archive.org)**
- https://archive.is / https://archive.today
- https://ghostarchive.org
- https://perma.cc
- [Arquivo.pt](https://arquivo.pt) Portuguese web archive with a [services catalog](https://sobre.arquivo.pt/en/about/services-catalog-by-arquivo-pt/) and [open-source tools](https://github.com/arquivo).
- https://archive.st
- https://theoldnet.com/
- https://timetravel.mementoweb.org/
- https://freezepage.com/
- https://webcitation.org/archive
- https://megalodon.jp/
- https://www.webarchive.org.uk/ukwa/
- Google, Bing, DuckDuckGo, and other [search engine caches](https://www.clickminded.com/google-cache-search/)

**Managed preservation and monitoring**

- **[Archive.it](https://archive-it.org) commercial Wayback Machine solution**
- https://www.pagefreezer.com
- https://www.smarsh.com
- https://www.stillio.com
- [SnapshotArchive](https://snapshotarchive.com/) Hosted scheduled screenshots and visual change monitoring, with PDF/HTML capture and archive retention depending on the plan.
- https://preservica.com/digital-archive-software-1/active-digital-preservation For-profit company offering a digital preservation software suite
- https://github.com/dgtlmoon/changedetection.io Change detection and monitoring of web page content changes

---

<a id="media-social-and-specialist-archives"></a>
<a id="specialist-media-and-social-archives"></a>

### Media, social & specialist archives

Tools for preserving videos, images, social accounts and conversations, plus specialist collections.

**Media and social capture**

- [StreamStash](https://www.streamstash.live/) Windows app for recording livestreams and collecting social-media content in a local library; free tier and paid one-time licenses. See the vendor’s [StreamStash vs ArchiveBox comparison](https://www.streamstash.live/blog/streamstash-vs-archivebox).
- [Auto Archiver](https://github.com/bellingcat/auto-archiver) Bellingcat's archiver for webpages, social posts, images and videos, with CLI/CSV/Google Sheets inputs and local or cloud storage.
- [Munin Archiver](https://github.com/peterk/munin-indexer) Social media archiver for Facebook, Instagram and VKontakte accounts.
- [Tube Archivist](https://github.com/tubearchivist/tubearchivist) Self-hosted YouTube archive with downloads, metadata search and playback.
- [TubeSync](https://github.com/meeb/tubesync) Synchronizes YouTube channels/playlists to local directories and media servers.
- [ytdl-sub](https://github.com/jmbannon/ytdl-sub) Automates yt-dlp subscription downloads and metadata generation for local media libraries.
- [gallery-dl](https://github.com/mikf/gallery-dl) Command-line downloader for image galleries and collections, with metadata support.
- [Slack Dumper](https://github.com/rusq/slackdump) Exports Slack messages, threads, files, channels and users to local storage.
- [tdl](https://github.com/iyear/tdl) Telegram toolkit with file downloads and JSON export of messages and member/subscriber lists.
- [forum-dl](https://github.com/mikwielgus/forum-dl) Alpha-stage forum and mailing-list archiver exporting threads/boards to JSONL, mailbox formats or WARC.
- [TwitchDownloader](https://github.com/lay295/TwitchDownloader) Downloads Twitch VODs, clips and chat, with chat replay rendering.
- [cobalt](https://github.com/imputnet/cobalt) Self-hostable multi-site media downloader with a web UI and API.

**Related collections and publishing networks**

- https://archiveofourown.org/
- https://github.com/HelloZeroNet/ZeroNet (super cool project)

---

<a id="replay-developer-tools-and-integrations"></a>
<a id="smaller-utilities"></a>
<a id="from-the-archives-unleashed-team"></a>
<a id="from-the-iipc-team"></a>
<a id="capture-crawling-and-content-extraction"></a>
<a id="warc-and-saved-collection-tools"></a>
<a id="archivebox-integrations"></a>
<a id="other-utilities-and-integrations"></a>

### Replay, developer tools & integrations

Tools for replaying and analyzing archives, building capture workflows, and connecting ArchiveBox to other services.

**Replay, search and collection analysis**

- **[ReplayWeb.page](https://webrecorder.net/replaywebpage)** Web archive viewer that runs entirely in the browser and doesn't require any server-hosted component to view WARC and WACZ files. Also available as a standalone electron app for local desktop use
- [pywb](https://github.com/webrecorder/pywb) aka *Python Wayback*, the open source toolkit forked from archive.org for self-hosting your own wayback machine among other web archiving tools
- **[ipwb](https://github.com/oduwsdl/ipwb) A distributed web archiving solution using pywb with IPFS for storage**
- **[OpenWayback](https://github.com/iipc/openwayback/wiki) Open source project developing core Wayback Machine components**
- [AUT](https://github.com/archivesunleashed/aut) Archives Unleashed Toolkit for analyzing web archives (formerly WarcBase)
- [Warclight](https://github.com/archivesunleashed/warclight) A Rails engine for finding and searching web archives
- [WarcDB](https://github.com/Florents-Tselai/WarcDB) Converts WARC crawl data into SQLite databases for querying.
- [WARC-GPT](https://github.com/harvard-lil/warc-gpt) Experimental retrieval-augmented generation pipeline and web UI for exploring WARC collections.
- [sist2](https://github.com/sist2app/sist2) Indexes saved file collections with text/metadata extraction, thumbnails, OCR and a search web interface; early development.
- [Archivematica](https://github.com/artefactual/archivematica) web GUI for institutional long-term archiving of web and other content

**Capture, extraction and conversion**

- [abx-dl](https://github.com/ArchiveBox/abx-dl) Standalone downloader using ArchiveBox plugins for webpage assets, media, PDFs, screenshots and other outputs.
- [Sliver](https://github.com/anjackson/sliver) Archives small URL collections or copies existing captures using shot-scraper through pywb, preserving WARC/WACZ provenance.
- [shot-scraper](https://github.com/simonw/shot-scraper) Browser screenshots, video recordings and JavaScript extraction from the command line.
- [WPull](https://github.com/ArchiveTeam/wpull) A pure python implementation of wget with WARC saving
- [Frozen Soup](https://github.com/jimwins/frozen-soup) Python library and CLI that inline resources into self-contained HTML pages.
- [singlepage](https://github.com/arp242/singlepage) Go library and CLI that bundle CSS, JavaScript and images into standalone HTML.
- [webarchive-to-singlefile](https://github.com/gonejack/webarchive-to-singlefile) Converts Safari .webarchive files into resource-embedded HTML; requires Chrome and is tested on macOS.
- [scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) Scrapy download handler for JavaScript-rendered pages using Playwright, retaining Scrapy scheduling and item processing.
- [Crawlee](https://github.com/apify/crawlee) JavaScript/TypeScript toolkit for browser-rendered and HTTP crawling, link discovery, file downloads and storing extracted results.
- [markdown-crawler](https://github.com/paulpierre/markdown-crawler) Recursively saves website content as Markdown, with depth/domain limits and resumable processing.
- [ExtractNet](https://github.com/currentslab/extractnet) Dragnet-based machine-learning extractor for article attributes such as author, headline, date and keywords; its README excludes boilerplate content extraction.
- [Inscriptis](https://github.com/weblyzard/inscriptis) HTML-to-text library, CLI and service preserving text layout, including nested tables and optional annotations.
- [htmldate](https://github.com/adbar/htmldate) Python library and CLI for identifying original and updated publication dates in webpages.
- [extruct](https://github.com/scrapinghub/extruct) Extracts embedded metadata including JSON-LD, Microdata, Microformats, Open Graph, RDFa and Dublin Core.
- [Defuddle](https://github.com/kepano/defuddle) Extracts primary content and metadata as cleaned HTML or Markdown; library/CLI developed for Obsidian Web Clipper, currently a work in progress.
- [Newspaper4k](https://github.com/AndyTheFactory/newspaper4k) Maintained Newspaper3k fork for article scraping, extraction and curation.
- [Courlan](https://github.com/adbar/courlan) Python library and CLI for crawl URL normalization, filtering, deduplication and scheduling.
- https://github.com/mozilla/readability tool for extracting article contents and text
- https://github.com/wkhtmltopdf/wkhtmltopdf Webkit HTML to PDF archiver/saver

**WARC/WACZ processing**

See also the [WACZ file format specification](https://specs.webrecorder.net/wacz/latest).

- [WarcProx](https://github.com/internetarchive/warcprox) WARC proxy recording and playback utility
- [WarcTools](https://github.com/internetarchive/warctools) utilities for dealing with WARCs
- [warcit](https://github.com/webrecorder/warcit) Create a WARC file out of a folder full of assets
- [warcio](https://github.com/webrecorder/warcio) fast streaming asynchronous WARC reader and writer
- [node-warc](https://github.com/N0taN3rd/node-warc) Parse And Create Web ARChive (WARC) files with node.js
- [JWARC](https://github.com/iipc/jwarc) A Java library for reading and writing WARC files.
- [warcat-rs](https://github.com/chfoo/warcat-rs) Rust WARC manipulation library and CLI; rewrite of the earlier Python [warcat](https://github.com/chfoo/warcat).
- [Warchaeology](https://github.com/NationalLibraryOfNorway/warchaeology) Command-line tools to inspect, manipulate and validate WARC files.
- [Waczerciser](https://github.com/harvard-lil/waczerciser) Experimental tool to inspect, edit, extract and repackage WARC/WACZ files.

**Discovery, recovery and supporting utilities**

- **[archivenow](https://github.com/oduwsdl/archivenow) tool that pushes urls into all the online archive services like Archive.is and Archive.org**
- [MemGator](https://github.com/oduwsdl/MemGator) Memento aggregator providing CLI and server access to captures across configured web archives.
- [Mink](https://github.com/machawk1/Mink) Chrome extension for finding archived versions of live pages and submitting pages to public archives.
- [LinkChecker](https://github.com/linkchecker/linkchecker) Recursively checks websites and local HTML for broken links, with filters and reports.
- https://github.com/jsvine/waybackpack command-line tool that lets you download the entire Wayback Machine archive for a given URL
- https://github.com/hartator/wayback-machine-downloader Download an entire website from the Internet Archive Wayback Machine.
- https://github.com/Lifesgood123/prevent-link-rot Replace any broken URLs in some content with Wayback machine URL equivalents
- https://en.archivarix.com download an archived page or entire site from the Wayback Machine
- https://proofofexistence.com prove that a certain file existed at a given time using the blockchain
- http://squidman.net/squidman/index.html
- https://wordpress.org/plugins/broken-link-checker/
- http://freedup.org/

**ArchiveBox integrations**

Third-party clients can target older ArchiveBox interfaces; check compatibility with your server version.

- [ArchiveBox QuickAdd](https://github.com/emschu/archivebox-quick-add) Desktop utility for submitting URLs to an existing ArchiveBox instance.
- [archivebox-reddit](https://github.com/FracturedCode/archivebox-reddit) Exports Reddit comments, posts, upvotes or saved items to ArchiveBox.
- [ArchiveboxTelegramBot](https://github.com/Gertje823/ArchiveboxTelegramBot) Telegram bot that submits URLs to ArchiveBox.
- https://github.com/TheCakeIsNaOH/xbs-to-archivebox A utility to sync xBrowserSync bookmarks with ArchiveBox

---

[More tools and indexes](#the-master-lists).

---

## Reading List

A collection of blog posts and articles about internet archiving, contact me / open an issue if you want to add a link here!

---

### Blogs Friends of ArchiveBox

<img src="https://media.npr.org/assets/img/2017/06/28/istock-506236357-5961b1f611e5136a7cd3fd5f74d97f4575f48c66-s800-c85.jpg" width="350px" align="right" style="float: right; margin: 5px"/>

- https://blog.archive.org
- https://webrecorder.net/blog
- https://netpreserveblog.wordpress.com
- https://blog.conifer.rhizome.org/
- https://ws-dl.blogspot.com
- https://siarchives.si.edu/blog
- https://parameters.ssrc.org
- https://sr.ithaka.org/publications
- https://ait.blog.archive.org
- https://brewster.kahle.org
- https://ianmilligan.ca
- https://medium.com/@giovannidamiola

---

### Articles We Like About Internet Archiving

- **2026-08-18 (updated) · English:** [Data Rescue Activist Tools](https://subjectguides.library.american.edu/data_rescue/tools) — American University Library; government-information preservation resources, including ArchiveBox's local capture use cases.
- **2025-05-19:** [Building a personal archive of the web](https://alexwlchan.net/2025/personal-archive-of-the-web/) — Alex Chan on manually saving and verifying a personal web archive.
- **2024-04 · English:** [Sprinter: Speeding Up High-Fidelity Crawling of the Modern Web](https://www.usenix.org/conference/nsdi24/presentation/goel) — USENIX; authors at University of Michigan, Princeton and USC; research on combining browser-based and browserless crawling while preserving fetched resources; compares ArchiveBox, Browsertrix and Brozzler when constructing its baseline.
- **2024-01-17 · English:** [Web Archiving](https://me.micahrl.com/blog/web-archiving/) — Micah R. Ledbetter; practical WARC/WACZ capture and embedded replay, with ArchiveBox among the alternative capture tools.
- **2022-07 · English:** [Jawa: Web Archival in the Era of JavaScript](https://www.usenix.org/conference/osdi22/presentation/goel) — USENIX; authors at University of Michigan and Princeton; research on JavaScript replay fidelity and archive storage; uses ArchiveBox as a measured crawling baseline.

- https://items.ssrc.org/parameters/on-the-importance-of-web-archiving/
- https://theconversation.com/your-internet-data-is-rotting-115891
- https://www.bbc.com/future/story/20190401-why-theres-so-little-left-of-the-early-internet
- https://sr.ithaka.org/publications/the-state-of-digital-preservation-in-2018/
- https://gizmodo.com/delete-never-the-digital-hoarders-who-collect-tumblrs-1832900423
- https://siarchives.si.edu/blog/we-are-not-alone-progress-digital-preservation-community
- https://www.gwern.net/Archiving-URLs
- http://brewster.kahle.org/2015/08/11/locking-the-web-open-a-call-for-a-distributed-web-2/
- https://lwn.net/Articles/766374/
- https://en.wikipedia.org/wiki/List_of_Web_archiving_initiatives
- https://medium.com/@giovannidamiola/making-the-internet-archives-full-text-search-faster-30fb11574ea9
- https://xkcd.com/1909/
- https://samsaffron.com/archive/2012/06/07/testing-3-million-hyperlinks-lessons-learned#comment-31366
- https://www.gwern.net/docs/linkrot/2011-muflax-backup.pdf
- https://thoughtstreams.io/higgins/permalinking-vs-transience/
- http://ait.blog.archive.org/files/2014/04/archiveit_life_cycle_model.pdf
- https://blog.archive.org/2016/05/26/web-archiving-with-national-libraries/
- https://blog.archive.org/2014/10/28/building-libraries-together/
- https://ianmilligan.ca/2018/03/27/ethics-and-the-archived-web-presentation-the-ethics-of-studying-geocities/
- https://ianmilligan.ca/2018/05/22/new-article-if-these-crawls-could-talk-studying-and-documenting-web-archives-provenance/
- https://ws-dl.blogspot.com/2019/02/2019-02-08-google-is-being-shuttered.html

If any of these links are dead, you can find an archived version on https://archive.sweeting.me or https://web.archive.org.

---


### ArchiveBox-Specific Posts, Tutorials, and Guides

*Tutorials describe the version available when written; use the current [installation](Install.md) and [usage](Usage.md) docs for setup. This list favors original articles, practical guides, interviews, and substantial reviews with meaningful ArchiveBox coverage. Brief listicle entries and passing mentions are omitted. Syndicated copies and translated editions of the same article are represented by the original source rather than counted separately.*

For other languages, see [Articles in Other Languages](#articles-in-other-languages) below.

<!-- Recent coverage is listed once per original work, with publication dates unless marked updated. -->

#### Recent English coverage (2022–2026)

- **2026-09-30 (updated) · English:** [How to Install ArchiveBox on Your Synology NAS](https://mariushosting.com/how-to-install-archivebox-on-your-synology-nas/) — Marius Hosting; illustrated Synology, Portainer and reverse-proxy setup.
- **2026-09-24 · English:** [ArchiveBox 0.9 brings desktop & mobile apps, redesigned viewers, and PostgreSQL support](https://alternativeto.net/news/2026/9/archivebox-0-9-brings-desktop-and-mobile-apps-redesigned-viewers-and-postgresql-support/) — AlternativeTo; dedicated release coverage of native apps, the archiving engine, scheduling, Personas and plugins.
- **2026-08-08 · English:** [I built my own Wayback Machine, and now I never lose web pages](https://www.makeuseof.com/i-built-my-own-wayback-machine-and-now-i-never-lose-web-pages/) — MakeUseOf; tests capture and offline access after removing the original page.
- **2026-06-27 · English:** [Build Your Own Wayback: Self-Hosting ArchiveBox for OSINT Evidence - Why and how](https://blog.osintph.info/build-your-own-wayback-self-hosting-archivebox-for-osint-evidence-why-and-how-2/) — OSINTPH; practitioner deployment and changedetection.io integration.
- **2026-04-21 · English:** [Wayback Machine vs SingleFile vs ArchiveBox: Which Preservation Tool Fits Which Job?](https://osint.dev/articles/wayback-machine-vs-singlefile-vs-archivebox) — OSINT.dev; detailed preservation-workflow comparison covering historical lookup, local capture, self-hosted archive management, repeated collection, metadata and custody.
- **2026-04-21 · English:** [Hunchly vs ArchiveBox: Evidence Packaging vs Archive Ownership](https://osint.dev/articles/hunchly-vs-archivebox-evidence-packaging-vs-archive-ownership) — OSINT.dev; detailed comparison of investigator case evidence and ongoing URL collections, including formats, recurring capture, local custody, backups and worked research scenarios.
- **2026-03-02 · English:** [The internet is disappearing, so I repurposed an old laptop to save it](https://www.howtogeek.com/the-internet-is-disappearing-so-i-repurposed-an-old-laptop-to-save-it/) — Jordan Gloor / How-To Geek; repurposes a Linux laptop, installs ArchiveBox and demonstrates browser-extension capture.
- **2025-12-02 · English:** [Best Tools to Archive Webpages and Websites in 2026](https://www.oscooshop.com/blogs/blogs/tools-to-archive-webpages-and-websites) — OSCOO; comparison with a dedicated ArchiveBox section on multi-format capture, organization and retrieval.
- **2025-09-24 (last updated) · English:** [Archiving Facebook, Instagram & LinkedIn](https://www.dpconline.org/blog/archiving-facebook-instagram-linkedin) — Digital Preservation Coalition; experiments importing social-media exports and preserving linked content.
- **2025-05-28 · English:** [How to set up your own article archiving service – and why I did (RIP, Pocket)](https://www.zdnet.com/article/how-to-set-up-your-own-article-archiving-service-and-why-i-did-rip-pocket/) — David Gewirtz / ZDNET; hands-on Docker/Portainer setup, browser-extension capture and inspecting the saved files.
- **2025-04-07 · English:** [Cookies for Capture: Using ArchiveBox’s –cookie Option for Authenticated Web Content in OSINT](https://www.argeliuslabs.com/cookies-for-capture-using-archiveboxs-cookie-option-for-authenticated-web-content-in-osint/) — Argelius Labs; cookie export and authenticated-capture workflows. See current [authentication documentation](Personas.md) for supported configuration.
- **2025-02-08 · English:** [Archiving websites with ArchiveBox and wget](https://www.claudinec.net/posts/2025-02-08-web-archiving/) — Claudine Chionh; personal preservation workflow using ArchiveBox and wget.
- **2025-02-03 · English:** [Offgrid internet-in-a-box project - Part four](https://blog.ctms.me/posts/2025-02-03-offgrid-build-part-4/) — Dom Corriveau; compares ArchiveBox, SingleFile, zimit and Kiwix for offline use.
- **2024-11-27 · English:** [Let's archive the web](https://changelog.com/podcast/619) — Changelog Interviews #619; interview with Nick Sweeting, with a full transcript, on ArchiveBox and distributed preservation.
- **2024-11-18 · English:** [How I Turned My Raspberry Pi Into a Private Internet Archive](https://maketecheasier.com/turn-raspberry-pi-into-private-internet-archive/) — David Morelo's Raspberry Pi/external-storage Docker walkthrough, initialization, resource settings and UI/CLI archiving.
- **2024-10-16 · English:** [Safeguarding Your Digital Heritage: A Guide to Archiving with ArchiveBox](https://dbtechreviews.com/2024/10/16/safeguarding-your-digital-heritage-a-guide-to-archiving-with-archivebox/) — DB Tech; guide and accompanying video walkthrough.
- **2024-06-30 · English:** [Archivebox – Your personal wayback machine](https://titor.dev/selfhosted/archivebox-your-personal-wayback-machine/) — Portainer installation and actual capture walkthrough covering privacy, cookies, user agents, URL deny filters and browser extension.
- **2024-06-13 · English:** [NixOS: Packaging a Python Application](https://valentinpratz.de/posts/2024-06-13-nixos-package-python-archivebox/) — Valentin Pratz's detailed walkthrough packaging ArchiveBox 0.8.1 and its Django 5 dependencies with Nix, including an overlay and complete derivation.
- **2024-03-02 · English:** [First setup of Archivebox](https://philippeloctaux.com/blog/archivebox-setup/) — Focused container setup note restricting public views, disabling Archive.org submission and creating an admin user.
- **2024-02-29 · English:** [Archiving Option Chain Data](https://avilpage.com/2024/02/historical-option-chain-india.html) — Anand Reddy Pandikunta's Indian option-chain archival workflow, URL generation, daily captures and multiple-version browsing limitation.
- **2024-02-25 · English:** [Grinding the ArchiveBox](https://trainedmonkey.com/2024/02/25/grinding_the_archivebox) — Jim Winstead's firsthand Pinboard RSS/JSON import investigation, feedparser contribution, and timestamp collision limitations.
- **2024-01-29 · English:** [Self-hosting an internet archive with ArchiveBox](https://cyb.org.uk/2024/01/29/self-hosted-archive.html) — CYB; firsthand deployment, search, capture formats, storage deduplication and authenticated-capture limitations.
- **2024-01-13 · English:** [ArchiveBox is Super Cool](https://mtlynch.io/notes/archivebox/) — Michael Lynch; firsthand review with Reddit and YouTube captures.
- **2023-03-18 · English:** [Install ArchiveBox Inside Docker Container in Linux](https://lindevs.com/install-archivebox-inside-docker-container-in-linux) — Lindevs; Docker installation and networking.
- **2023-01-05 · English:** [How To Self-host Your Own Internet Archive With ArchiveBox In Linux](https://ostechnix.com/self-host-internet-archive-with-archivebox/) — OSTechNix; installation methods and CLI/UI archiving.
- **2022-11-04 · English:** [How to Create a Web Archive With Archivebox](https://maketecheasier.com/create-web-archive-with-archivebox/) — Make Tech Easier; installation, nginx and capture walkthrough.
- **2022-10-26 · English:** [Building a webarchive with Archivebox](https://jeffmackinnon.com/building-a-personal-webarchive.html) — Firsthand move from a VM to Synology Docker/Portainer, configuring storage, permissions and the admin account.
- **2022-05 · English:** [Create your own VPS internet ArchiveBox](https://pocketmags.com/linux-format-magazine/may-2022/articles/create-your-own-vps-internet-archivebox) — David Rutland's Linux Format VPS/Docker Compose web-archiving tutorial. Magazine preview; full article requires purchase.
- **2022-02-26 · English:** [How to generate static website for an old ArchiveBox archive](https://sleeplessbeastie.eu/2022/02/26/how-to-generate-static-website-for-an-old-archivebox-archive/) — Recovering a legacy collection as a static site with an older pinned Docker image when its JSON cannot be imported.
- **2022-02-07 · English:** [k3s on a Raspberry Pi 4 at home, Part 6](https://darkstar.github.io/2022/02/07/k3s-on-raspberrypi-at-home-part6.html) — Darkstar; Kubernetes, persistent storage, ingress and full-text search.
- **2022-02-04 · English:** [ArchiveBox Linux Setup](https://danstechjourney.com/archivebox-linux-setup/) — Daniel Martin; Docker Compose setup and first captures.
- **2022-01-08 · English:** [Archivebox Helm Chart for the Raspberry Pi](https://mattscodecave.com/posts/archivebox-helm-chart-for-raspberry-pi.html) — Matt’s Codecave; Helm/K3s deployment on Raspberry Pi.
- **2022-01-04 · English:** [Bookmarking and Creating a Local Internet Archive](https://www.ecliptik.com/bookmarking-with-raindrop/) — Firsthand Raindrop/Dropbox export integration, converting bookmarks to tagged JSON, validating with jq, importing into ArchiveBox and running hourly cron.

#### Additional English articles and ongoing guides

- **English:** [ArchiveBox MCP Setup Guide](https://pragmar.github.io/mcp-server-webcrawl/guides/archivebox.html) — Original integration guide connecting multiple ArchiveBox collections to Claude Desktop through mcp-server-webcrawl, including installation, search and troubleshooting.
- **English:** [Media & Archives: ArchiveBox](https://cashewmade.com/lab/docker/media-archives/#archivebox) — Cashew Made; a complete Docker Compose stack and configuration tables covering ArchiveBox, Sonic, noVNC and pywb.
- "Install ArchiveBox on SaltBox.dev" https://docs.saltbox.dev/sandbox/apps/archivebox/#3-setup
- "ArchiveBox is an open-source self-hosted web archiving system for the web and the desktop" https://medevel.com/archivebox/
- "Install ArchiveBox on a One-Click Docker Application" https://www.vultr.com/docs/install-archivebox-on-a-oneclick-docker-application/
- "Preserve the Internet With ArchiveBox" https://www.cyberpunks.com/preserve-the-internet-with-archivebox/
- "How to Make Your Own Internet Archive With ArchiveBox" https://nixintel.info/osint-tools/make-your-own-internet-archive-with-archive-box/
- "How to install ArchiveBox to preserve websites you care about"
  https://blog.sleeplessbeastie.eu/2019/06/19/how-to-install-archivebox-to-preserve-websites-you-care-about/
- "How to remotely archive websites using ArchiveBox"
  https://blog.sleeplessbeastie.eu/2019/06/26/how-to-remotely-archive-websites-using-archivebox/
- "How to Create Your Own Private Self-Hosted Read-It-Later App" https://www.makeuseof.com/tag/self-hosted-read-later-app/
- "How to use CutyCapt inside ArchiveBox"
  https://blog.sleeplessbeastie.eu/2019/07/10/how-to-use-cutycapt-inside-archivebox/
- "Automate ArchiveBox with Google Spreadsheet to Backup your internet"
  https://manfred.life/archivebox
- https://metaxyntax.neocities.org/entries/7.html

<a id="archivebox-discussions-in-news--social-media"></a>

### ArchiveBox Discussions in News & Social Media

- **2024-02-14 · English:** [Web archiving with ArchiveBox](https://sanctum.geek.nz/presentations/web-archiving-with-archivebox.pdf) — Tom Ryder's 30-slide PLUG presentation and demonstration of ArchiveBox for personal daily archiving.

<img src="https://cdn.dribbble.com/users/896843/screenshots/2560608/news_media_icons-07.png" width="380px" align="right" style="float: right; margin: 5px"/>

- **2026-09-22:** [ArchiveBox v0.9 released with new native apps and 50 new plugins](https://news.ycombinator.com/item?id=49808008) — Hacker News discussion of the [official release announcement](https://docs.sweeting.me/s/archivebox-v0.9-announcement).

- **Aggregators:**  
  **[ProductHunt](https://www.producthunt.com/posts/archivebox)**, **[AlternativeTo](https://alternativeto.net/software/archivebox/)**, **[SaaSHub](https://www.saashub.com/archivebox)**, [Logiciels](https://www.logiciels.pro/logiciel-saas/archivebox/), [SteemHunt](https://steemhunt.com/@adnan556644/archivebox-the-open-source-self-hosted-internet-archiving-solution), [Recurse Center: The Joy of Computing](https://joy.recurse.com/posts/224-archivebox), [GitHub Changelog](https://changelog.com/news/archivebox-opensource-selfhosted-web-archive-6D0d), [Dev.To Ultra List](https://dev.to/teamxenox/-ultra-list-one-list-to-rule-them-all-march-19-4p4f), [O'Reilly 4 Short Links](https://www.oreilly.com/ideas/four-short-links-15-april-2019), [JaxEnter](https://jaxenter.com/github-trending-march-2019-157470.html)
- **Blog Posts & Podcasts:**  
  [Defining Desktop Linux Podcast #296 (0:55:00)](https://linuxunplugged.com/296), [Schrankmonster.de](https://www.schrankmonster.de/2019/04/10/archive-your-slice-of-the-web/)
- **Hacker News threads and comments:**  
  [#1](https://news.ycombinator.com/item?id=14272133), [#2](https://news.ycombinator.com/item?id=18728546), [#3](https://news.ycombinator.com/item?id=18876685), **[#4](https://news.ycombinator.com/item?id=19346985)**, [and many more...](https://www.google.com/search?q=site%3Anews.ycombinator.com+%22archivebox%22)
- **Reddit r/DataHoarder, r/SelfHosted, etc. posts and comments**:  
  [#1](https://www.reddit.com/r/DataHoarder/comments/69e6i9/archive_a_browseable_copy_of_your_saved_pocket/), [#2](https://www.reddit.com/r/DataHoarder/comments/6kepv6/bookmarkarchiver_now_supports_archiving_all_major/), [#3](https://www.reddit.com/r/DataHoarder/comments/apnud4/continually_archive_websites_and_keep_the_older/), [#4](https://www.reddit.com/r/DataHoarder/comments/azdhd9/archivebox_open_source_selfhosted_web_archive/), [#5](https://www.reddit.com/r/DataHoarder/comments/b0o10h/archivebox_self_hosting_clone_of_archiveorg/) , **[#6](https://www.reddit.com/r/DataHoarder/comments/b4nrlc/in_case_you_havent_seen_it_archivebox_has_a/)**, [#7](https://www.reddit.com/r/selfhosted/comments/69eoi3/pocket_stream_archive_your_own_personal_wayback/), [#8](https://www.reddit.com/r/selfhosted/comments/an2368/archivebox_the_opensource_selfhosted_web_archive/), [and many more...](https://www.google.com/search?q=site%3Areddit.com+%22archivebox%22)
- **Twitter:**  
  [Python Trending](https://twitter.com/pythontrending/status/1092492387182628865), [PyCoder's Weekly](https://twitter.com/pycoders/status/1105803699799105536), [Python Hub](https://twitter.com/PythonHub/status/1107601343395651589), [Smashing Magazine](https://twitter.com/smashingmag/status/1107990604774928386), <a href="https://twitter.com/search?q=archivebox.io%20OR%20archivebox%2Farchivebox%20OR%20archiveboxapp&src=typed_query&f=live">and many more...</a>


---

## Articles in Other Languages

Original articles, guides, videos and discussions grouped by language. Dated entries are newest first; older and undated resources follow. Translated editions of the same work remain together.

[Chinese](#chinese) · [French](#french) · [German](#german) · [Italian](#italian) · [Japanese](#japanese) · [Polish](#polish) · [Portuguese](#portuguese) · [Russian](#russian) · [Spanish](#spanish)

### Chinese

- **2026-09-29 · Chinese:** [ArchiveBox：把网页存进自己硬盘的自托管存档工具](https://zendot.org/posts/archivebox-archivebox) — Zendot; overview of formats, deployment, and uses for a personal archive. English edition is the same work.
- **2026-08-13 · Traditional Chinese / Cantonese:** [ArchiveBox：自架網頁存檔系統，永遠捕捉瀏覽記錄與書籤](https://www.techritual.com/2026/08/13/529168/) — Techritual; Hong Kong overview. Original Chinese edition; multilingual editions are the same work.
- **2025-08-11 · Chinese:** [本地部署开源网页存档工具 ArchiveBox 并实现外部访问](https://help.luyouxia.com/archivebox.html) — Illustrated Ubuntu Docker deployment and administrator setup followed by remote-access configuration using 路由侠.
- **2024-11-09 · Chinese:** [搭建自己的互联网档案馆：Archivebox](https://post.smzdm.com/p/admo7o5k/) — Illustrated DXP4800Plus NAS deployment with Docker Compose initialization and firsthand capture results for images, video and account-protected pages.
- **2024-01-16 · Chinese:** [搭一个网站存档库 ArchiveBox](https://blog.vcvit.me/2024/01/16/archive-box/) — Short dedicated Unraid/NAS installation walkthrough with administrator commands and Chrome Exporter setup.
- **2024-01-01 · Chinese:** [web.archive.org 自建开源替代品 ArchiveBox 试用](https://blog.lzc256.com/posts/archivebox-experience/) — Firsthand review of archive fidelity and disk usage, plus a concrete nginx subdirectory deployment configuration.
- **2023-08-03 · Chinese:** [MiniFlux Starred as Feed](https://wogong.net/blog/miniflux-starred/) — Practical integration exporting starred Miniflux entries as an RSS feed for ArchiveBox, with tested projects, reported issues and Docker Compose configuration.
- **2023-03-24 · Chinese:** [互联网存档系统：ArchiveBox安装使用](https://www.luxiyue.com/server/互联网存档系统：archivebox安装使用/) — Native Ubuntu installation, actual PATH troubleshooting, administrator setup, first capture, nginx reverse proxy and background operation.
- **2022-06-05 · Chinese:** [ArchiveBox 安装使用](https://networm.me/2022/06/05/archive-box-setup/) — networm; Synology setup experience and practical limitations.
- **2022-05-13 · Chinese:** [网站存档服务ArchiveBox](https://laosu.tech/2022/05/13/网站存档服务ArchiveBox/) — 老苏的博客; illustrated Synology Docker setup. Same-author CSDN repost counted here.
- "网页存档的开源工具ArchiveBox，可以将网页文字、图片、媒体文件等都保存下来，供日后查看。基于Python的开源项目，可搭建私人的网络存档服务。" https://www.bilibili.com/s/video/BV1ib4y1X7SL
- "使用存档盒制作自己的Internet存档" http://www.diglog.com/story/1045192.html
- "ArchiveBox：开源的WEB存档" https://zhen.bushini.de/14738.html / https://www.1fishsauce.com/?p=4206
- "两个基于爬虫的项目: Kiwix & ArchiveBox" https://blog.csdn.net/JackLang/article/details/108328791

### French

- **2024-01-25 · French:** [Installer ArchiveBox avec Docker](https://belginux.com/installer-archivebox-avec-docker/) — belginux; illustrated Docker setup and first captures.
- [Korben.info](https://korben.info/archivebox-un-clone-darchive-org-et-de-la-wayback-machine-a-auto-heberger.html)
- [La Ferme Du Web](https://www.lafermeduweb.net/veille/archivebox-archivez-des-copies-de-sites-en-local-avec-tous-les-medias-lies)

### German

- **2024-11-30 · German:** [Video: Dein eigenes Internetarchiv mit ArchiveBox](https://gnulinux.ch/dein-eigenes-internetarchiv-mit-archivebox) — GNU/Linux.ch; video and written guide to setup and URL/RSS archiving.
- **2024-11-30 · German:** [ArchiveBox – digitale Langzeitarchivierung mit Docker und Traefik installieren](https://goneuland.de/archivebox-digitale-langzeitarchivierung-mit-docker-und-traefik-installieren/) — goNeuland; Docker Compose and Traefik deployment.
- **2024-01-27 · German:** [ArchiveBox archiviert das Internet: Super Idee, leider sagen die Cookie-Banner nein...](https://u-labs.de/forum/internet-technik-136/archivebox-archiviert-das-internet-super-idee-leider-sagen-cookie-banner-nein-41320) — Substantial firsthand investigation of cookie-banner capture failures on five German news sites, Chromium extension timing, screenshot commands and Readability/workaround tradeoffs.
- **2023-08-22 · German:** [ArchiveBox](https://perron.de/archivebox/) — Illustrated firsthand Portainer installation on a Proxmox Ubuntu LXC, including storage mapping and administrator setup.
- "Mit ArchiveBox Webseiten auf der Festplatte archivieren" https://www.linux-community.de/ausgaben/linuxuser/2020/12/mit-archivebox-webseiten-auf-der-festplatte-archivieren/
- [WEB-ARCHIV TEIL 8: WALLABAG UND ARCHIVEBOX](http://webermartin.net/blog/web-archiv-teil-8-wallabag-und-archivebox/)
- [Binärgewitter Podcast #221](http://blog.binaergewitter.de/2019/01/18/binaergewitter-talk-number-221-vertieft-in-die-andere-richtung/)

### Italian

- **2026-09-23 · Italian:** [ArchiveBox crea la tua Wayback Machine privata: salva siti, login e cronologia](https://www.ilsoftware.it/focus/archivebox-wayback-machine-privata-salvare-pagine-web-login-cronologia/) — IlSoftware.it; v0.9 overview covering plugins, Personas and browser capture.
- **2025-10-07 · Italian:** [ArchiveBox l’archiviazione web open self-hosted](https://www.linuxeasy.org/archivebox-archiviazione-web-self-hosted/) — LinuxEasy; overview and Docker installation.
- **2024-01-15 · Italian:** [Salvare pagine Web e archiviarle con ArchiveBox: ecco il vostro Internet Archive](https://www.ilsoftware.it/focus/salvare-pagine-web-e-archiviarle-con-archivebox-ecco-il-vostro-internet-archive/) — IlSoftware.it; installation, capture formats, GUI and search.

### Japanese

- **2026-08-05 · Japanese:** [AIツールの調査結果をあとから証明できるか？CodexとOSSでつくるリサーチ証拠基盤](https://note.com/gtminami/n/n11b7ec48a970) — Proposed research-evidence architecture using ArchiveBox captures, snapshot metadata, asynchronous jobs and consistent backups.
- **2026-07-07 · Japanese:** [ArchiveBox のバックアップ](https://note.com/hitoshiarakawa/n/n398ac71f04a5) — Hitoshi Arakawa; personal backup and synchronization workflow.
- **2026-06-19 · Japanese:** [ArchiveBox を docker-compose でインストールする](https://note.com/hitoshiarakawa/n/ncb30c5a20b0d) — Hitoshi Arakawa; Docker Compose deployment on Proxmox/Ubuntu.
- **2025-12-13 · Japanese:** [ConoHa で容量無制限のマイ魚拓サービスを作成する](https://qiita.com/CloudRemix/items/0620706e33844d07a139) — Detailed illustrated VPS and S3 object-storage deployment for a personal ArchiveBox service, including API credentials, bucket configuration and storage mounting.
- **2024-01-14 · Japanese:** [ArchiveBoxをNginxリバースプロキシでhttpsにする](https://qiita.com/katori_m/items/1061e5b4a5798d809831) — Qiita; HTTPS setup with an Nginx reverse proxy.
- **2023-07-02 · Japanese:** [「ArchiveBox」使ってみたよレビュー](https://gigazine.net/news/20230702-archive-box/) — GIGAZINE; extensive hands-on review of Docker, CLI/UI and bookmark/history imports.
- "【デモ有♪】ConoHaのArchiveBoxアプリケーションを使ってみたよ"
  https://qiita.com/CloudRemix/items/691caf91efa3ef19a7ad

### Polish

- **2026-02-28 · Polish:** [Watcher: System strażniczy nad planowaniem przestrzennym w Łodzi](https://dadalo.pl/posts/watcher-system-strazniczy-planowanie-przestrzenne-lodz/) — Maciej Lesiak; civic monitoring case study using ArchiveBox to preserve planning pages and documents alongside a change-detection and alerting system. Also available in an [English edition](https://dadalo.pl/en/posts/watcher-urban-planning-guard-system-lodz/).

### Portuguese

- **2026-09-25 · Portuguese:** [ArchiveBox 0.9 chega com aplicações nativas e suporte para PostgreSQL](https://tugatech.com.pt/t91690-archivebox-0-9-chega-com-aplicacoes-nativas-e-suporte-para-postgresql) — Pedro Fernandes's dedicated Portuguese v0.9 coverage of native applications, rebuilt engine, PostgreSQL, scheduling, authenticated Personas and plugins.
- **2024-02-26 · Portuguese:** [ArchiveBox: Uma Ferramenta Poderosa para Segurança da Informação e Arquivologia](https://bruteforce.com.br/br/blog/archivebox-uma-ferramenta-poderosa-para-seguranca-da-informacao-e-arquivologia.html) — Dedicated practitioner essay on ArchiveBox's use in information-security evidence and archival institutions.

### Russian

- **2026-09-16 · Russian:** [10 полезных open-source проектов, которые стоит попробовать в 2026 году](https://slsrnko.ru/blog/10-poleznyh-open-source-proektov-kotorye-stoit-poprobovat-v-2026-godu/) — slsrnko.ru; includes ArchiveBox as a personal archive and knowledge-base component.
- **2025-01-10 · Russian:** [Как поднять на виртуальном сервере собственную интернет-машину времени с помощью ArchiveBox](https://habr.com/ru/companies/thehosting/articles/872836/) — THE.Hosting; VPS setup and CLI/UI tutorial.
- **2024-02-03 · Russian:** [Как архивировать Веб](https://causa-arcana.com/ru/blog/2024/02/03/web-archiving.html) — Firsthand web-preservation comparison with a substantial ArchiveBox evaluation: Docker deployment, static exports, measured archive size and limitations.
- "Персональный интернет-архив без боли" https://habr.com/ru/company/vdsina/blog/550180/
- "Сам себе архивариус. Изучаем возможности ArchiveBox" https://xakep.ru/2021/02/01/archivebox/

### Spanish

- **2026-09-09:** [Setting up a private ArchiveBox](https://x.com/edgaramist59014/status/2097593098045976921) — Spanish community post asking which websites to preserve locally.
- "ArchiveBox, una solución para crear nuestro propio Archive.org en miniatura y personalizado" https://www.genbeta.com/herramientas/archivebox-solucion-para-crear-nuestro-propio-archive-org-miniatura-personalizado

---

## Communities

### Most Active Communities

<p>
<a href="https://github.com/internetarchive"><img src="https://github.com/internetarchive.png" alt="Internet Archive" width="64"/></a> &nbsp;
<a href="https://github.com/webrecorder"><img src="https://github.com/webrecorder.png" alt="Webrecorder" width="64"/></a> &nbsp;
<a href="https://github.com/rhizome-conifer"><img src="https://github.com/rhizome-conifer.png" alt="Rhizome Conifer" width="64"/></a> &nbsp;
<a href="https://github.com/oduwsdl"><img src="https://github.com/oduwsdl.png" alt="ODU Web Science and Digital Libraries" width="64"/></a> &nbsp;
<a href="https://github.com/archivesunleashed"><img src="https://github.com/archivesunleashed.png" alt="Archives Unleashed" width="64"/></a> &nbsp;
<a href="https://github.com/iipc"><img src="https://github.com/iipc.png" alt="IIPC" width="64"/></a>
</p>

Project directories: [Internet Archive](https://github.com/internetarchive), [Webrecorder](https://github.com/webrecorder), [ODU WS-DL](https://github.com/oduwsdl), [Archives Unleashed](https://github.com/archivesunleashed), and [IIPC](https://github.com/iipc).

<img src="https://github.com/ArchiveTeam.png" width="230px" align="right" style="float: right; margin: 5px"/>

- **[The Internet Archive (Archive.org)](https://archive.org/iathreads/forums.php)** (USA)
- **[International Internet Preservation Consortium (IIPC)](http://netpreserve.org/)** (International)
- **[The Archive Team](https://www.archiveteam.org/), [URL Team](https://www.archiveteam.org/index.php?title=URLTeam), [r/ArchiveTeam](https://reddit.com/r/ArchiveTeam)** (International)
- **[Rhizome.org](http://archive.rhizome.org/)** The digital preservation group that works on [Conifer by Rhizome](https://conifer.rhizome.org/) formerly Webrecorder.io (USA)
- **[Webrecorder](https://webrecorder.net/)** (formerly known[¹](https://blog.conifer.rhizome.org/2020/06/11/webrecorder-conifer.html) as Webrecorder.io) is a company led by Ilya Kreymer, that researches and develops web archiving tools, widely used by the community.
- **[Old Dominion University: Web Science and Digital Libraries (WS-DL @ ODU)](https://ws-dl.cs.odu.edu)** (Virginia, USA)
- **[r/DataHoarder](https://www.reddit.com/r/DataHoarder), [r/Archivists](https://www.reddit.com/r/Archivists/), [r/DHExchange](https://www.reddit.com/r/DHExchange/)** (International)
- [The Eye](https://the-eye.eu) Non-profit working on content archival and long-term preservation (Europe)
- [Digital Preservation Coalition](https://www.dpconline.org/about) & their [Software Tool Registry (COPTR)](http://coptr.digipres.org/Main_Page) (UK & Wales)
- [Archives Unleashed Project](https://archivesunleashed.org/about-project/) and [UAP GitHub](https://github.com/archivesunleashed) (Canada)

---

### Web Archiving Communities

<img src="https://upload.wikimedia.org/wikipedia/commons/8/8d/Noun_project_community_icon_986427_cc.svg" width="230px" align="right" style="float: right; margin: 5px"/>

Follow these technological and organizational archiving hubs for the latest archiving news.

- [Canadian Web Archiving Coalition](https://www.carl-abrc.ca/advancing-research/digital-preservation/cwac/) (Canada)
- [Web Archives for Historical Research Group](https://uwaterloo.ca/web-archive-group/about) (Canada)
- [Smithsonian Institution Archives: Digital Curation](https://siarchives.si.edu/what-we-do/digital-curation) (Washington D.C., USA)
- [National Digital Stewardship Alliance (NDSA)](http://www.digitalpreservation.gov/ndsa/NDSAtoDLF.html) (USA)
- [Digital Library Federation (DLF)](https://www.diglib.org/about/) (USA)
- [Council on Library and Information Resources (CLIR)](http://www.clir.org/about) (USA)
- [Digital Curation Centre (DCC)](http://www.dcc.ac.uk/about-us) (UK)
- [ArchiveMatica](https://www.archivematica.org/en/) & their [Community Wiki](https://wiki.archivematica.org/Community) (International)
- [Professional Development Institutes for Digital Preservation (POWRR)](https://digitalpowrr.niu.edu/) (USA)
- [Institute of Museum and Library Services (IMLS)](https://www.imls.gov/about/mission) (USA)
- [Stanford Libraries Web Archiving](https://library.stanford.edu/projects/web-archiving) (USA)
- [Society of American Archivists: Electronic Records (SAA)](https://www2.archivists.org/groups/electronic-records-section) (USA)
- [BitCurator Consortium (BCC)](https://bitcuratorconsortium.org/mission) (USA)
- [Ethics & Archiving the Web Conference (Rhizome)](https://eaw.rhizome.org/) (USA)
- [Archivists Round Table of NYC](https://www.nycarchivists.org/) (USA)

---

### General Archiving Foundations, Coalitions, Initiatives, and Institutes

<details>
<summary>Browse archiving foundations, coalitions, initiatives, and institutes</summary>

<img src="https://us.123rf.com/450wm/drvector/drvector1510/drvector151000331/45755355-government-icons.jpg?ver=6" width="230px" align="right" style="float: right; margin: 5px"/>

Find your local archiving group in the list and see how you can contribute!

- [Community Archives and Heritage Group](https://www.communityarchives.org.uk/content/about/history-and-purpose) (UK & Ireland)
- [Open Preservation Foundation (OPF)](https://openpreservation.org/about/organisation/) (UK & Europe)
- [Software Preservation Network](https://www.softwarepreservationnetwork.org/about/) (International)
- [ITHAKA](https://www.ithaka.org/content/our-mission), [Portico](https://www.portico.org/why-portico/), [JSTOR](https://www.jstor.org/), [ARTSTOR](http://www.artstor.org/), [S+R](https://sr.ithaka.org/our-work/collections-and-preservation/) (USA)
- [Archives and Records Association](https://www2.archivists.org/assoc-orgs/archives-and-records-association-united-kingdom-ireland) (UK & Ireland)
- [Arkivrådet](http://www.arkivradet.se/) (Sweden)
- [Asociación Española de Archiveros, Bibliotecarios, Museologos y Documentalistas (ANABAD)](https://www2.archivists.org/assoc-orgs/asociaci%C3%B3n-espa%C3%B1ola-de-archiveros-bibliotecarios-museologos-y-documentalistas-anabad) (Spain)
- [Associação dos Arquivistas Brasileiros (AAB)](https://www2.archivists.org/assoc-orgs/associacao-dos-arquivistas-brasileiros-aab) (Brazil)
- [Associação Portuguesa de Bibliotecários, Archivistas e Documentalistas (BAD)](https://www2.archivists.org/assoc-orgs/associacao-portuguesa-de-bibliotecarios-archivistas-e-documentalistas-bad) (Portugal)
- [Association des archivistes français (AAF)](https://www2.archivists.org/assoc-orgs/association-des-archivistes-francais-aaf) (France)
- [Associazione Nazionale Archivistica Italiana (ANAI)](https://www2.archivists.org/assoc-orgs/associazione-nazionale-archivistica-italiana-anai) (Italy)
- [Australian Society of Archivists Inc.](https://www2.archivists.org/assoc-orgs/australian-society-of-archivists-inc) (Australia)
- [International Council on Archives (ICA)](https://www2.archivists.org/assoc-orgs/international-council-on-archives-ica) 
- [International Records Management Trust (IRMT)](https://www2.archivists.org/assoc-orgs/international-records-management-trust-irmt) 
- [Irish Society for Archives](https://www2.archivists.org/assoc-orgs/irish-society-for-archives) (Ireland)
- [Koninklijke Vereniging van Archivarissen in Nederland](https://www2.archivists.org/assoc-orgs/koninklijke-vereniging-van-archivarissen-in-nederland) (Netherlands)
- [State Archives Administration of the People's Republic of China](https://www2.archivists.org/assoc-orgs/state-archives-administration-of-the-peoples-republic-of-china) (China)
- [Academy of Certified Archivists](https://www2.archivists.org/assoc-orgs/academy-of-certified-archivists) 
- [Archivists and Librarians in the History of the Health Sciences](https://www2.archivists.org/assoc-orgs/archivists-and-librarians-in-the-history-of-the-health-sciences) 
- [Archivists for Congregations of Women Religious](https://www2.archivists.org/assoc-orgs/archivists-for-congregations-of-women-religious) 
- [Archivists of Religious Institutions](https://www2.archivists.org/assoc-orgs/archivists-of-religious-institutions) 
- [Association of Catholic Diocesan Archivists](https://www2.archivists.org/assoc-orgs/association-of-catholic-diocesan-archivists) 
- [Association of Moving Image Archivists](https://www2.archivists.org/assoc-orgs/association-of-moving-image-archivists) 
- [Council of State Archivists](https://www2.archivists.org/assoc-orgs/council-of-state-archivists) 
- [National Association of Government Archives and Records Administrators](https://www2.archivists.org/assoc-orgs/national-association-of-government-archives-and-records-administrators) 
- [National Episcopal Historians and Archivists](https://www2.archivists.org/assoc-orgs/national-episcopal-historians-and-archivists) 
- [Archival Education and Research Institute](https://www2.archivists.org/assoc-orgs/archival-education-and-research-institute) 
- [Archives Leadership Institute](https://www2.archivists.org/assoc-orgs/archives-leadership-institute) 
- [Georgia Archives Institute](https://www2.archivists.org/assoc-orgs/georgia-archives-institute) 
- [Modern Archives Institute](https://www2.archivists.org/assoc-orgs/modern-archives-institute) 
- [Western Archives Institute](https://www2.archivists.org/assoc-orgs/western-archives-institute) 
- [Association des archivistes du Québec](https://www2.archivists.org/assoc-orgs/association-des-archivistes-du-quebec) 
- [Association of Canadian Archivists](https://www2.archivists.org/assoc-orgs/association-of-canadian-archivists) 
- [Canadian Council of Archives/Conseil canadien des archives](https://www2.archivists.org/assoc-orgs/canadian-council-of-archivesconseil-canadien-des-archives) 
- [Archives Association of British Columbia](https://www2.archivists.org/assoc-orgs/archives-association-of-british-columbia) 
- [Archives Association of Ontario](https://www2.archivists.org/assoc-orgs/archives-association-of-ontario) 
- [Archives Council of Prince Edward Island](https://www2.archivists.org/assoc-orgs/archives-council-of-prince-edward-island) 
- [Archives Society of Alberta](https://www2.archivists.org/assoc-orgs/archives-society-of-alberta) 
- [Association for Manitoba Archives](https://www2.archivists.org/assoc-orgs/association-for-manitoba-archives) 
- [Association of Newfoundland and Labrador Archives](https://www2.archivists.org/assoc-orgs/association-of-newfoundland-and-labrador-archives) 
- [Council of Nova Scotia Archives](https://www2.archivists.org/assoc-orgs/council-of-nova-scotia-archives) 
- [Réseau des services d'archives du Québec](https://www2.archivists.org/assoc-orgs/reseau-des-services-darchives-du-quebec) 
- [Saskatchewan Council for Archives and Archivists](https://www2.archivists.org/assoc-orgs/saskatchewan-council-for-archives-and-archivists)

You can find more organizations and initiatives on these other lists:

- [Wikipedia.org List of Web Archiving Initiatives](https://en.wikipedia.org/wiki/List_of_Web_archiving_initiatives)
- [SAA List of USA & Canada Based Archiving Organizations](https://www2.archivists.org/assoc-orgs/directory)
- [SAA List of International Archiving Organizations](https://www2.archivists.org/assoc-orgs/i_a_o)
- [Digital Preservation Coalition's Member List](https://www.dpconline.org/about/members)

</details>

---

## ArchiveBox Community Resources

### ArchiveBox Chat Rooms

- [Official ArchiveBox Zulip Chat Server](https://zulip.archivebox.io)
- [Unofficial ArchiveBox Matrix chat room](https://matrix.to/#/#archivebox:matrix.org) (old)
- [GitHub Discussions](https://github.com/ArchiveBox/ArchiveBox/discussions)

### ArchiveBox on Social Media

- [Twitter: @ArchiveBoxApp](https://twitter.com/ArchiveBoxApp)
- [LinkedIn: ArchiveBox](https://www.linkedin.com/company/archivebox/)
- [YouTube: @ArchiveBoxApp](https://www.youtube.com/@ArchiveBoxApp)
- [Reddit: r/ArchiveBox](https://www.reddit.com/r/ArchiveBox/)
- [Alternative.to](https://alternativeto.net/software/archivebox/about/)
- [ReposHub](https://reposhub.com/python/web-crawling/pirate-ArchiveBox.html)

### ArchiveBox on Package Distribution Platforms

- [Python PyPI](https://pypi.org/project/archivebox/)
- [Docker Hub](https://hub.docker.com/r/archivebox/archivebox)
- [ArchLinux AUR](https://aur.archlinux.org/packages/archivebox)
- [Ubuntu/Debian apt wrapper](https://github.com/ArchiveBox/debian-archivebox)

---

<div align="center">

[![](https://img.shields.io/badge/Donate-ArchiveBox.io-%23DD5D76.svg)](https://www.patreon.com/theSquashSH)
[![](https://img.shields.io/badge/Donate-Archive.org-%23115D76.svg)](https://archive.org/donate/)

<br/><br/>
<small><a href="#contents">^ &nbsp; Back to Top &nbsp; ^</a></small>
</div>
