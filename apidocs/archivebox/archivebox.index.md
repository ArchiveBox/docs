# {py:mod}`archivebox.index`

```{py:module} archivebox.index
```

```{autodoc2-docstring} archivebox.index
:allowtitles:
```

## Submodules

```{toctree}
:titlesonly:
:maxdepth: 1

archivebox.index.html
archivebox.index.csv
archivebox.index.sql
archivebox.index.json
archivebox.index.schema
```

## Package Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`merge_links <archivebox.index.merge_links>`
  - ```{autodoc2-docstring} archivebox.index.merge_links
    :summary:
    ```
* - {py:obj}`validate_links <archivebox.index.validate_links>`
  - ```{autodoc2-docstring} archivebox.index.validate_links
    :summary:
    ```
* - {py:obj}`archivable_links <archivebox.index.archivable_links>`
  - ```{autodoc2-docstring} archivebox.index.archivable_links
    :summary:
    ```
* - {py:obj}`fix_duplicate_links <archivebox.index.fix_duplicate_links>`
  - ```{autodoc2-docstring} archivebox.index.fix_duplicate_links
    :summary:
    ```
* - {py:obj}`sorted_links <archivebox.index.sorted_links>`
  - ```{autodoc2-docstring} archivebox.index.sorted_links
    :summary:
    ```
* - {py:obj}`links_after_timestamp <archivebox.index.links_after_timestamp>`
  - ```{autodoc2-docstring} archivebox.index.links_after_timestamp
    :summary:
    ```
* - {py:obj}`lowest_uniq_timestamp <archivebox.index.lowest_uniq_timestamp>`
  - ```{autodoc2-docstring} archivebox.index.lowest_uniq_timestamp
    :summary:
    ```
* - {py:obj}`timed_index_update <archivebox.index.timed_index_update>`
  - ```{autodoc2-docstring} archivebox.index.timed_index_update
    :summary:
    ```
* - {py:obj}`write_main_index <archivebox.index.write_main_index>`
  - ```{autodoc2-docstring} archivebox.index.write_main_index
    :summary:
    ```
* - {py:obj}`load_main_index <archivebox.index.load_main_index>`
  - ```{autodoc2-docstring} archivebox.index.load_main_index
    :summary:
    ```
* - {py:obj}`load_main_index_meta <archivebox.index.load_main_index_meta>`
  - ```{autodoc2-docstring} archivebox.index.load_main_index_meta
    :summary:
    ```
* - {py:obj}`parse_links_from_source <archivebox.index.parse_links_from_source>`
  - ```{autodoc2-docstring} archivebox.index.parse_links_from_source
    :summary:
    ```
* - {py:obj}`fix_duplicate_links_in_index <archivebox.index.fix_duplicate_links_in_index>`
  - ```{autodoc2-docstring} archivebox.index.fix_duplicate_links_in_index
    :summary:
    ```
* - {py:obj}`dedupe_links <archivebox.index.dedupe_links>`
  - ```{autodoc2-docstring} archivebox.index.dedupe_links
    :summary:
    ```
* - {py:obj}`write_link_details <archivebox.index.write_link_details>`
  - ```{autodoc2-docstring} archivebox.index.write_link_details
    :summary:
    ```
* - {py:obj}`load_link_details <archivebox.index.load_link_details>`
  - ```{autodoc2-docstring} archivebox.index.load_link_details
    :summary:
    ```
* - {py:obj}`q_filter <archivebox.index.q_filter>`
  - ```{autodoc2-docstring} archivebox.index.q_filter
    :summary:
    ```
* - {py:obj}`search_filter <archivebox.index.search_filter>`
  - ```{autodoc2-docstring} archivebox.index.search_filter
    :summary:
    ```
* - {py:obj}`snapshot_filter <archivebox.index.snapshot_filter>`
  - ```{autodoc2-docstring} archivebox.index.snapshot_filter
    :summary:
    ```
* - {py:obj}`get_indexed_folders <archivebox.index.get_indexed_folders>`
  - ```{autodoc2-docstring} archivebox.index.get_indexed_folders
    :summary:
    ```
* - {py:obj}`get_archived_folders <archivebox.index.get_archived_folders>`
  - ```{autodoc2-docstring} archivebox.index.get_archived_folders
    :summary:
    ```
* - {py:obj}`get_unarchived_folders <archivebox.index.get_unarchived_folders>`
  - ```{autodoc2-docstring} archivebox.index.get_unarchived_folders
    :summary:
    ```
* - {py:obj}`get_present_folders <archivebox.index.get_present_folders>`
  - ```{autodoc2-docstring} archivebox.index.get_present_folders
    :summary:
    ```
* - {py:obj}`get_valid_folders <archivebox.index.get_valid_folders>`
  - ```{autodoc2-docstring} archivebox.index.get_valid_folders
    :summary:
    ```
* - {py:obj}`get_invalid_folders <archivebox.index.get_invalid_folders>`
  - ```{autodoc2-docstring} archivebox.index.get_invalid_folders
    :summary:
    ```
* - {py:obj}`get_duplicate_folders <archivebox.index.get_duplicate_folders>`
  - ```{autodoc2-docstring} archivebox.index.get_duplicate_folders
    :summary:
    ```
* - {py:obj}`get_orphaned_folders <archivebox.index.get_orphaned_folders>`
  - ```{autodoc2-docstring} archivebox.index.get_orphaned_folders
    :summary:
    ```
* - {py:obj}`get_corrupted_folders <archivebox.index.get_corrupted_folders>`
  - ```{autodoc2-docstring} archivebox.index.get_corrupted_folders
    :summary:
    ```
* - {py:obj}`get_unrecognized_folders <archivebox.index.get_unrecognized_folders>`
  - ```{autodoc2-docstring} archivebox.index.get_unrecognized_folders
    :summary:
    ```
* - {py:obj}`is_valid <archivebox.index.is_valid>`
  - ```{autodoc2-docstring} archivebox.index.is_valid
    :summary:
    ```
* - {py:obj}`is_corrupt <archivebox.index.is_corrupt>`
  - ```{autodoc2-docstring} archivebox.index.is_corrupt
    :summary:
    ```
* - {py:obj}`is_archived <archivebox.index.is_archived>`
  - ```{autodoc2-docstring} archivebox.index.is_archived
    :summary:
    ```
* - {py:obj}`is_unarchived <archivebox.index.is_unarchived>`
  - ```{autodoc2-docstring} archivebox.index.is_unarchived
    :summary:
    ```
* - {py:obj}`fix_invalid_folder_locations <archivebox.index.fix_invalid_folder_locations>`
  - ```{autodoc2-docstring} archivebox.index.fix_invalid_folder_locations
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.index.__package__>`
  - ```{autodoc2-docstring} archivebox.index.__package__
    :summary:
    ```
* - {py:obj}`LINK_FILTERS <archivebox.index.LINK_FILTERS>`
  - ```{autodoc2-docstring} archivebox.index.LINK_FILTERS
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.index.__package__
:value: >
   'archivebox.index'

```{autodoc2-docstring} archivebox.index.__package__
```

````

````{py:function} merge_links(a: archivebox.index.schema.Link, b: archivebox.index.schema.Link) -> archivebox.index.schema.Link
:canonical: archivebox.index.merge_links

```{autodoc2-docstring} archivebox.index.merge_links
```
````

````{py:function} validate_links(links: typing.Iterable[archivebox.index.schema.Link]) -> typing.List[archivebox.index.schema.Link]
:canonical: archivebox.index.validate_links

```{autodoc2-docstring} archivebox.index.validate_links
```
````

````{py:function} archivable_links(links: typing.Iterable[archivebox.index.schema.Link]) -> typing.Iterable[archivebox.index.schema.Link]
:canonical: archivebox.index.archivable_links

```{autodoc2-docstring} archivebox.index.archivable_links
```
````

````{py:function} fix_duplicate_links(sorted_links: typing.Iterable[archivebox.index.schema.Link]) -> typing.Iterable[archivebox.index.schema.Link]
:canonical: archivebox.index.fix_duplicate_links

```{autodoc2-docstring} archivebox.index.fix_duplicate_links
```
````

````{py:function} sorted_links(links: typing.Iterable[archivebox.index.schema.Link]) -> typing.Iterable[archivebox.index.schema.Link]
:canonical: archivebox.index.sorted_links

```{autodoc2-docstring} archivebox.index.sorted_links
```
````

````{py:function} links_after_timestamp(links: typing.Iterable[archivebox.index.schema.Link], resume: typing.Optional[float] = None) -> typing.Iterable[archivebox.index.schema.Link]
:canonical: archivebox.index.links_after_timestamp

```{autodoc2-docstring} archivebox.index.links_after_timestamp
```
````

````{py:function} lowest_uniq_timestamp(used_timestamps: collections.OrderedDict, timestamp: str) -> str
:canonical: archivebox.index.lowest_uniq_timestamp

```{autodoc2-docstring} archivebox.index.lowest_uniq_timestamp
```
````

````{py:function} timed_index_update(out_path: pathlib.Path)
:canonical: archivebox.index.timed_index_update

```{autodoc2-docstring} archivebox.index.timed_index_update
```
````

````{py:function} write_main_index(links: typing.List[archivebox.index.schema.Link], out_dir: pathlib.Path = DATA_DIR, created_by_id: int | None = None) -> None
:canonical: archivebox.index.write_main_index

```{autodoc2-docstring} archivebox.index.write_main_index
```
````

````{py:function} load_main_index(out_dir: pathlib.Path | str = DATA_DIR, warn: bool = True) -> typing.List[archivebox.index.schema.Link]
:canonical: archivebox.index.load_main_index

```{autodoc2-docstring} archivebox.index.load_main_index
```
````

````{py:function} load_main_index_meta(out_dir: pathlib.Path = DATA_DIR) -> typing.Optional[dict]
:canonical: archivebox.index.load_main_index_meta

```{autodoc2-docstring} archivebox.index.load_main_index_meta
```
````

````{py:function} parse_links_from_source(source_path: str, root_url: typing.Optional[str] = None, parser: str = 'auto') -> typing.List[archivebox.index.schema.Link]
:canonical: archivebox.index.parse_links_from_source

```{autodoc2-docstring} archivebox.index.parse_links_from_source
```
````

````{py:function} fix_duplicate_links_in_index(snapshots: django.db.models.QuerySet, links: typing.Iterable[archivebox.index.schema.Link]) -> typing.Iterable[archivebox.index.schema.Link]
:canonical: archivebox.index.fix_duplicate_links_in_index

```{autodoc2-docstring} archivebox.index.fix_duplicate_links_in_index
```
````

````{py:function} dedupe_links(snapshots: django.db.models.QuerySet, new_links: typing.List[archivebox.index.schema.Link]) -> typing.List[archivebox.index.schema.Link]
:canonical: archivebox.index.dedupe_links

```{autodoc2-docstring} archivebox.index.dedupe_links
```
````

````{py:function} write_link_details(link: archivebox.index.schema.Link, out_dir: typing.Optional[str] = None, skip_sql_index: bool = False) -> None
:canonical: archivebox.index.write_link_details

```{autodoc2-docstring} archivebox.index.write_link_details
```
````

````{py:function} load_link_details(link: archivebox.index.schema.Link, out_dir: typing.Optional[str] = None) -> archivebox.index.schema.Link
:canonical: archivebox.index.load_link_details

```{autodoc2-docstring} archivebox.index.load_link_details
```
````

````{py:data} LINK_FILTERS
:canonical: archivebox.index.LINK_FILTERS
:value: >
   None

```{autodoc2-docstring} archivebox.index.LINK_FILTERS
```

````

````{py:function} q_filter(snapshots: django.db.models.QuerySet, filter_patterns: typing.List[str], filter_type: str = 'exact') -> django.db.models.QuerySet
:canonical: archivebox.index.q_filter

```{autodoc2-docstring} archivebox.index.q_filter
```
````

````{py:function} search_filter(snapshots: django.db.models.QuerySet, filter_patterns: typing.List[str], filter_type: str = 'search') -> django.db.models.QuerySet
:canonical: archivebox.index.search_filter

```{autodoc2-docstring} archivebox.index.search_filter
```
````

````{py:function} snapshot_filter(snapshots: django.db.models.QuerySet, filter_patterns: typing.List[str], filter_type: str = 'exact') -> django.db.models.QuerySet
:canonical: archivebox.index.snapshot_filter

```{autodoc2-docstring} archivebox.index.snapshot_filter
```
````

````{py:function} get_indexed_folders(snapshots, out_dir: pathlib.Path = DATA_DIR) -> typing.Dict[str, typing.Optional[archivebox.index.schema.Link]]
:canonical: archivebox.index.get_indexed_folders

```{autodoc2-docstring} archivebox.index.get_indexed_folders
```
````

````{py:function} get_archived_folders(snapshots, out_dir: pathlib.Path = DATA_DIR) -> typing.Dict[str, typing.Optional[archivebox.index.schema.Link]]
:canonical: archivebox.index.get_archived_folders

```{autodoc2-docstring} archivebox.index.get_archived_folders
```
````

````{py:function} get_unarchived_folders(snapshots, out_dir: pathlib.Path = DATA_DIR) -> typing.Dict[str, typing.Optional[archivebox.index.schema.Link]]
:canonical: archivebox.index.get_unarchived_folders

```{autodoc2-docstring} archivebox.index.get_unarchived_folders
```
````

````{py:function} get_present_folders(snapshots, out_dir: pathlib.Path = DATA_DIR) -> typing.Dict[str, typing.Optional[archivebox.index.schema.Link]]
:canonical: archivebox.index.get_present_folders

```{autodoc2-docstring} archivebox.index.get_present_folders
```
````

````{py:function} get_valid_folders(snapshots, out_dir: pathlib.Path = DATA_DIR) -> typing.Dict[str, typing.Optional[archivebox.index.schema.Link]]
:canonical: archivebox.index.get_valid_folders

```{autodoc2-docstring} archivebox.index.get_valid_folders
```
````

````{py:function} get_invalid_folders(snapshots, out_dir: pathlib.Path = DATA_DIR) -> typing.Dict[str, typing.Optional[archivebox.index.schema.Link]]
:canonical: archivebox.index.get_invalid_folders

```{autodoc2-docstring} archivebox.index.get_invalid_folders
```
````

````{py:function} get_duplicate_folders(snapshots, out_dir: pathlib.Path = DATA_DIR) -> typing.Dict[str, typing.Optional[archivebox.index.schema.Link]]
:canonical: archivebox.index.get_duplicate_folders

```{autodoc2-docstring} archivebox.index.get_duplicate_folders
```
````

````{py:function} get_orphaned_folders(snapshots, out_dir: pathlib.Path = DATA_DIR) -> typing.Dict[str, typing.Optional[archivebox.index.schema.Link]]
:canonical: archivebox.index.get_orphaned_folders

```{autodoc2-docstring} archivebox.index.get_orphaned_folders
```
````

````{py:function} get_corrupted_folders(snapshots, out_dir: pathlib.Path = DATA_DIR) -> typing.Dict[str, typing.Optional[archivebox.index.schema.Link]]
:canonical: archivebox.index.get_corrupted_folders

```{autodoc2-docstring} archivebox.index.get_corrupted_folders
```
````

````{py:function} get_unrecognized_folders(snapshots, out_dir: pathlib.Path = DATA_DIR) -> typing.Dict[str, typing.Optional[archivebox.index.schema.Link]]
:canonical: archivebox.index.get_unrecognized_folders

```{autodoc2-docstring} archivebox.index.get_unrecognized_folders
```
````

````{py:function} is_valid(link: archivebox.index.schema.Link) -> bool
:canonical: archivebox.index.is_valid

```{autodoc2-docstring} archivebox.index.is_valid
```
````

````{py:function} is_corrupt(link: archivebox.index.schema.Link) -> bool
:canonical: archivebox.index.is_corrupt

```{autodoc2-docstring} archivebox.index.is_corrupt
```
````

````{py:function} is_archived(link: archivebox.index.schema.Link) -> bool
:canonical: archivebox.index.is_archived

```{autodoc2-docstring} archivebox.index.is_archived
```
````

````{py:function} is_unarchived(link: archivebox.index.schema.Link) -> bool
:canonical: archivebox.index.is_unarchived

```{autodoc2-docstring} archivebox.index.is_unarchived
```
````

````{py:function} fix_invalid_folder_locations(out_dir: pathlib.Path = DATA_DIR) -> typing.Tuple[typing.List[str], typing.List[str]]
:canonical: archivebox.index.fix_invalid_folder_locations

```{autodoc2-docstring} archivebox.index.fix_invalid_folder_locations
```
````
