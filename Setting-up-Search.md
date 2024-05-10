## How to Search in ArchiveBox

You can search your ArchiveBox data in a number of ways:

- using the CLI: `archivebox list --filter-type=search 'text to search'`
- using the Web UI: both the `/public` index and `/admin/core/snapshot` pages provide a search box
- using the REST API: `/api/v1/list?filter_type=search` provides the same search interface as the CLI  
- by searching the archive data folder directly with external tools (e.g. macOS Spotlight, [Cerebro](https://www.cerebroapp.com/), `ag`, [Yacy](https://yacy.net/), etc.)

![image](https://github.com/ArchiveBox/ArchiveBox/assets/511499/637675ee-bf4a-49f9-b936-c2da1bd64410)

<br/>

> *Note: ArchiveBox currently only returns the bare list of snapshots that match when performing a search.*  
>   
> This will be [improved in the future](https://zulip.archivebox.io/#narrow/stream/154-support/topic/Full.20Text.20Search.20works.2E.2E.2E.20but.20is.20there.20a.20UI.3F) to highlight the *specific paragraph/line/area that matched* within a Snapshot.  
> For now we recommend using Ctl+F in the browser or one of the external tools listed above to further filter for a term within a Snapshot's contents.


<br/>

---

## ArchiveBox Search Backends

ArchiveBox search works by doing substring matches in `Snapshot` metadata fields (`url`, `title`, `timestamp`, `tags`), and by searching the full archived content within each Snapshot (using the selected search backend below). You can find the search implementation source code here: [`archivebox/core/views.py: PublicIndex.get_queryset()`](https://github.com/ArchiveBox/ArchiveBox/blob/dev/archivebox/core/views.py#:~:text=title__icontains).

```bash
# this setting controls which search backend ArchiveBox uses
archivebox config --set SEARCH_BACKEND_ENGINE=[ripgrep]|sonic|sqlite

# to see information about the backend you are currently using, run:
archivebox version
archivebox config --get SEARCH_BACKEND_ENGINE
```

ArchiveBox provides search functionality out-of-the-box using a simple but efficient tool called [`ripgrep`](https://github.com/BurntSushi/ripgrep).

Ripgrep is the fastest currently available filesystem search tool that scans over the raw data directly. We chose it as the default so that beginners and 95% of users with small collections can have an experience that "just works", without needing to install and maintain complex additional dependencies or background workers.

However, there are some fundamental limitations of scanning through every file on disk each time a search is done, so ArchiveBox provides a number of additional search backend options for users that outgrow `ripgrep`.

> [!TIP]
> **You should consider switching ArchiveBox to use `sonic` or another backend IF:**
> 
> - you have more than 1,000 Snapshots saved in your archive
> - your archive data is stored on a slower filesystem like a spinning hard drive or remote network mount
> - you want more advanced search features like stemming, boolean operators, and ability to search PDFs, eBooks, ZIP/tar files, etc.

<br/>

<a name="ripgrep"></a>

### `ripgrep` *(the default)*

If you do not already have `ripgrep` installed, follow the [instructions here](https://github.com/BurntSushi/ripgrep#installation) to get it.
ArchiveBox will use `ripgrep` by default if it is found, however you can explicitly configure it to be used like so:

```bash
archivebox config --set SEARCH_BACKEND_ENGINE=ripgrep
archivebox config --set RIPGREP_BINARY=rg

# check that archivebox detects the installed version:
archivebox version

# then try it out by searching via the Web UI or CLI:
archivebox list --filter-type=search 'text to search for'
```

#### Pros
- supports advanced searching with regex patterns
- simple, few moving parts, and broadly available for all OSs and CPU architectures
- 0 idle resource use as there is no background indexer process running
- 0 additional disk storage needed as it searches the original data instead of maintaining a separate index
- reasonably fast on NVMe and SSD drives for small collections

#### Cons
- very slow as archive collection size increases (doesn't scale well beyond 500~1,000 Snapshots)
- very slow if underlying filesytem is slow (e.g. HDDs or network mounts)
- doesn't support stemming, boolean operators, or other advanced full-text search features

<br/>

<a name="ripgrep-all"></a>

### `ripgrep-all` (aka `rga`)

The same as ripgrep except that it supports searching more binary filetypes like PDFs, eBooks, Office documents, zip, tar.gz, etc.

To use it, follow the [install instruction for your OS](https://github.com/phiresky/ripgrep-all#installation), then configure ArchiveBox to use it like so:

```bash
archivebox config --set SEARCH_BACKEND_ENGINE=ripgrep
archivebox config --set RIPGREP_BINARY=rga

# check that archivebox detects the installed version:
archivebox version

# then try it out by searching via the Web UI or CLI:
archivebox list --filter-type=search 'text to search for'
```

<br/>

<a name="ugrep"></a>

### `ugrep`

Not tested by the ArchiveBox team but it's very similar to `ripgrep` and may work as a drop-in replacement, with some caveats. (contributions welcome to improve support)

`ugrep` is similar to `ripgrep` and `ripgrep-all` in that it's an indexless disk-search tool, but it provides some more of the full-text search features without the performance overhead of maintaining a separate search backend worker with an independent index.

https://github.com/Genivia/ugrep

```bash
archivebox config --set RIPGREP_BINARY=ugrep+
```

#### Pros

- supports [boolean operators](https://github.com/Genivia/ugrep#bool) in search queries
- supports binary formats like compressed archives, PDFs, eBooks, etc.
- better support for Unicode, special characters, and searching across multiple lines of text
- supports [fuzzy search](https://github.com/Genivia/ugrep#fuzzy)

#### Cons

- not as fast as `sonic` and but also not as simple as `ripgrep`
- not all of its features are fully integrated with ArchiveBox yet

<br/><br/>

<a name="sonic"></a>

### `sonic` ⭐️ (the recommended upgrade path for most people)

[Sonic](https://github.com/valeriansaliou/sonic) is a fast, lightweight, rust-based alternative to super-heavy traditional search backends like Elasticsearch. It is capable of normalizing natural language search queries, fuzzy matching, and searching Unicode, without needing to maintain a duplicate document store index of all the searchable text.

Internally it functions as an index store, storing only the original IDs of the Snapshots with a super-compressed representation of the text. This allows it to scale to searching terabytes of archive data while maintaining an index only a fraction of that size.

*ArchiveBox has supported Sonic for years, and it is the most thoroughly tested and recommended backend for ArchiveBox users that need to scale beyond `ripgrep`.*

Using [sonic with ArchiveBox in Docker Compose](https://github.com/ArchiveBox/ArchiveBox/blob/dev/docker-compose.yml) is the easiest way to get started, though you can also use it without Docker by [installing it manually](https://github.com/valeriansaliou/sonic#installation).

```bash
# edit docker-compose.yml to uncomment the lines that enable sonic
nano docker-compose.yml

# make sure ArchiveBox is configured to use the Sonic backend
docker compose run archivebox config --set SEARCH_BACKEND_ENGINE=sonic

# restart the containers to apply changes and start the Sonic worker
docker compose down
docker compose up

# check that the sonic container started without issues
docker compose logs sonic
docker compose run archivebox version

# backfill any existing archivebox data into the Sonic index (may take an hour or longer depending on storage speed and collection size)
docker compose run archivebox update --index-only

# then test it out:
docker compose run archivebox list --filter-type=search 'some text to search'
```

*Fore more detailed instructions [see here](https://github.com/ArchiveBox/ArchiveBox/issues/956#issuecomment-1320587158)...*

#### Pros

- extremely fast, most queries complete in microseconds even with 100k+ snapshots
- maintains lightweight, compressed search index that is minuscule compared to original data
- all-in-one binary written in rust, available cross-platform and easy to deploy
- supports advanced full-text search features like normalization, stemming, etc.
- supports indexing and querying on a remote server (many ArchiveBox instances can share a single `sonic` instance)

#### Cons

- one extra dependency to install and background worker to keep running (Docker Compose makes this easy though)
- does not support searching binary files like PDFs, eBooks, compressed archives, etc.

<br/>

<a name="fts5"></a>

### `SQLite FTS5`

This is a [recently added](https://github.com/ArchiveBox/ArchiveBox/pull/1241) experimental option that uses a separate SQLite3 Database (similar to the one ArchiveBox already uses for Snapshot metadata) to provide full-text search.

```bash
archivebox config --set SEARCH_BACKEND_ENGINE=sqlite

# add existing data to index by running update:
archivebox update --index-only

# test it out using the archivebox Web UI or CLI:
archivebox list --filter-type=search 'some text to search'

# or using SQLite3 directly;
sqlite3 ./search.sqlite3

> SELECT snapshot_id FROM snapshot_fts
      INNER JOIN snapshot_id_fts ON snapshot_id_fts.rowid = snapshot_fts.rowid
      WHERE snapshot_fts MATCH "some text to search";
```

```bash
# optional advanced tuning:
archivebox config --set FTS_SEPARATE_DATABASE=True
archivebox config --set FTS_TOKENIZERS="porter unicode61 remove_diacritics 2"
archivebox config --set FTS_SQLITE_MAX_LENGTH=1000000000
```

- https://www.sqlite.org/fts5.html
- https://github.com/ArchiveBox/ArchiveBox/pull/1241

#### Pros

- No additional dependencies needed to install, SQLite3 is already available and used by ArchiveBox
- No long-running background search worker process needed, 0 idle resource use
- Supports advanced full-text search features like boolean operators, stemming, phrases, etc.
- Comparable speed and efficiency to `sonic` for most use-cases (much faster than `ripgrep`/`ugrep`)
- Durability and portability, SQLite is widely used and supported by every major platform on earth

#### Cons

- Not as thoroughly-tested by ArchiveBox team as our `sonic` or `ripgrep` backends
- Maintains a (compressed, but still potentially large) duplicate copy of all searchable text in `search.sqlite3` db
- Does not support searching binary files PDFs, eBooks, compressed archives, etc.
- Search indexing and querying must be performed on same server as ArchiveBox data (we don't yet support sending FTS5 queries to a remote server)

<br/>

---

<br/>

### Further Reading

- https://github.com/ArchiveBox/ArchiveBox/blob/dev/docker-compose.yml#:~:text=SEARCH_BACKEND_ENGINE
- https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#ripgrep_binary

* [#22 Original Issue where full-text search functionality was proposed](https://github.com/ArchiveBox/ArchiveBox/issues/22)
* [#543 + #570 Original PR where full-text search functionality was implemented](https://github.com/ArchiveBox/ArchiveBox/pull/543)
* [#956 Documentation: Document how search works](https://github.com/ArchiveBox/ArchiveBox/issues/956#issuecomment-1320587158)
* [#654 Support: Search Backend only searching admin Snapshot fields instead of archive content](https://github.com/ArchiveBox/ArchiveBox/issues/654)
* [#1087 Support: Help setting up full text search](https://github.com/ArchiveBox/ArchiveBox/issues/1087) 
* [#1091 Support: Help switching to ripgrep-all](https://github.com/ArchiveBox/ArchiveBox/issues/1091)
* [#1318 Troubleshooting: Search times out on v0.7.2 installed on Synology using Portainer](https://github.com/ArchiveBox/ArchiveBox/issues/1318)
* [#1333 + #1316 Text Search and Filters don't work at the same time in the web UI](https://github.com/ArchiveBox/ArchiveBox/pull/1333)
* [#1320 Troubleshooting: Sonic backend Error: ENDED authentication_failed doesn't contain protocol(NUMBER)](https://github.com/ArchiveBox/ArchiveBox/pull/1320)

- [#1139 Feature Request: Add AI-assisted summarization, tagging, search, and more using LLMs / RAG](https://github.com/ArchiveBox/ArchiveBox/issues/1139)
- [#1358 Django Admin general improvements: tree view, better filters, better sorting, custom pages, etc.](https://github.com/ArchiveBox/ArchiveBox/issues/1358)