## How to Search in ArchiveBox

You can search your ArchiveBox data in a number of ways:

- using the CLI: `archivebox list --filter-type=search 'text to search'`
- using the Web UI: both the `/public` index and `/admin/core/snapshot` pages provide a search box
- using the REST API: `/api/v1/list?filter_type=search` provides the same search interface as the CLI  
- by searching the archive data on the filesystem with external tools (e.g. macOS Spotlight, [Cerebro](https://www.cerebroapp.com/), `ag`, `grep -r`, `SQLite FTS5`, etc.)


> [!IMPORTANT]
> *ArchiveBox currently only returns a plain list of snapshots that match when performing a search.*  
> This will be improved in the future to highlight the specific paragraph/line/area that matched within a Snapshot.  
> For now we recommend using Ctl+F in the browser or one of the external tools listed above to further filter for a term within a Snapshot's contents.

<br/>

---

## ArchiveBox Search Backends

```bash
# this setting controls which search backend ArchiveBox uses
archivebox config --set SEARCH_BACKEND_ENGINE=[ripgrep]|sonic|sqlite
```

ArchiveBox provides search functionality out-of-the-box using a simple but efficient disk-search tool called [`ripgrep`](https://github.com/BurntSushi/ripgrep).

Ripgrep is the fastest currently available search tool that works without maintaining an separate index. However, there are some fundamental limitations of scanning through every file on disk each time a search is done, so ArchiveBox provides a number of additional search backend options that users can choose from when they outgrow the `ripgrep` default.

> You should consider switching ArchiveBox to use one of its more powerful search backends if:
> 
> - you have more than 1000 Snapshots in your archive
> - you're using a slow filesystem like a spinning hard drive or remote network mount
> - you want fuzzy-search features like stemming, boolean operators, searching binary files like PDFs, etc.

<br/>

### `ripgrep` (aka `rg`, the default)

> *Note: You must have `ripgrep` installed on your system to use this backend (it's available automatically if you use ArchiveBox in Docker)*

If you do not already have `ripgrep` installed, follow the [instructions here](https://github.com/BurntSushi/ripgrep#installation) to get it.
You can then configure ArchiveBox to use it like so:

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
- lower idle resource use as there is no background worker using up resources
- lower disk storage use as there is no separate search index containing copies of all the text
- reasonably fast on NVMe and SSD drives for small collections

#### Cons
- very slow as archive collection size increases
- very slow if underlying filesytem is slow (e.g. HDDs or network mounts)
- doesn't support stemming, boolean operators, or other advanced full-text search features

<br/>

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

#### Pros & Cons

Same as `ripgrep` with the addition of some extra supported filetypes, however `rga` is slightly less easy to install than `rg`.

<br/>

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

<br/>

### `sonic` ⭐️ (the recommended upgrade option for most people)

Sonic is a fast, lightweight, rust-based alternative to super-heavy traditional search backends like Elasticsearch. It is capable of normalizing natural language search queries, fuzzy matching, and searching Unicode, without needing to maintain a duplicate document store index of all the searchable text. Instead it works as an index store, storing only the IDs of the Snapshots with a super-compressed internal index. This allows it to scale to searching terabytes of archive data while maintaining an index only a fraction of that size.

It is the recommended backend for most ArchiveBox users who need to scale beyond what `ripgrep` can provide.

Using sonic with ArchiveBox in Docker Compose is the easiest way to get started, though you can also use it without Docker.

```bash
# edit docker-compose.yml and uncomment the lines related to sonic
nano docker-compose.yml

# make sure ArchiveBox is configured to use Sonic
docker compose run archivebox config --set SEARCH_BACKEND_ENGINE=sonic

# restart all the containers to apply the changes
docker compose down
docker compose up

# check that the sonic container started without issues
docker compose logs sonic
docker compose run archivebox version

# add any existing archivebox data to the new Sonic index (may take an hour or longer depending on storage speed and collection size)
docker compose run archivebox update --index-only

# then test it out:
docker compose run archivebox list --filter-type=search 'some text to search'
```

#### Pros

- extremely fast, most queries complete in microseconds even with 100k+ snapshots
- maintains lightweight, compressed search index that is minuscule compared to original data
- all-in-one binary written in rust, available cross-platform and easy to deploy
- supports advanced full-text search features like normalization, stemming, etc.
- supports indexing and querying on a remote server (many separate ArchiveBox instances can share a single `sonic` instance)

#### Cons

- one extra dependency to install and background worker to keep running (Docker Compose makes this easy though)
- does not support searching binary files like PDFs, eBooks, compressed archives, etc.

<br/>

### `SQLite FTS5`

This is a recently added experimental option that uses a separate SQLite3 Database (similar to the one archivebox already uses for Snapshot records) to provide full-text search.

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