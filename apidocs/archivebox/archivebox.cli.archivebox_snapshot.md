# {py:mod}`archivebox.cli.archivebox_snapshot`

```{py:module} archivebox.cli.archivebox_snapshot
```

```{autodoc2-docstring} archivebox.cli.archivebox_snapshot
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`create_snapshots <archivebox.cli.archivebox_snapshot.create_snapshots>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.create_snapshots
    :summary:
    ```
* - {py:obj}`build_snapshot_queryset <archivebox.cli.archivebox_snapshot.build_snapshot_queryset>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.build_snapshot_queryset
    :summary:
    ```
* - {py:obj}`list_snapshots <archivebox.cli.archivebox_snapshot.list_snapshots>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.list_snapshots
    :summary:
    ```
* - {py:obj}`update_snapshots <archivebox.cli.archivebox_snapshot.update_snapshots>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.update_snapshots
    :summary:
    ```
* - {py:obj}`delete_snapshots <archivebox.cli.archivebox_snapshot.delete_snapshots>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.delete_snapshots
    :summary:
    ```
* - {py:obj}`main <archivebox.cli.archivebox_snapshot.main>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.main
    :summary:
    ```
* - {py:obj}`create_cmd <archivebox.cli.archivebox_snapshot.create_cmd>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.create_cmd
    :summary:
    ```
* - {py:obj}`list_cmd <archivebox.cli.archivebox_snapshot.list_cmd>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.list_cmd
    :summary:
    ```
* - {py:obj}`update_cmd <archivebox.cli.archivebox_snapshot.update_cmd>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.update_cmd
    :summary:
    ```
* - {py:obj}`delete_cmd <archivebox.cli.archivebox_snapshot.delete_cmd>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.delete_cmd
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__command__ <archivebox.cli.archivebox_snapshot.__command__>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.__command__
    :summary:
    ```
````

### API

````{py:data} __command__
:canonical: archivebox.cli.archivebox_snapshot.__command__
:value: >
   'archivebox snapshot'

```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.__command__
```

````

````{py:function} create_snapshots(urls: collections.abc.Iterable[str], tag: str = '', status: str = 'queued', depth: int = 0, created_by_id: int | None = None) -> int
:canonical: archivebox.cli.archivebox_snapshot.create_snapshots

```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.create_snapshots
```
````

````{py:function} build_snapshot_queryset(*, status: str | None = None, url__icontains: str | None = None, url__istartswith: str | None = None, tag: str | None = None, crawl_id: str | None = None, sort: str | None = None, search: str | None = None, query: str | None = None, limit: int | None = None) -> django.db.models.QuerySet
:canonical: archivebox.cli.archivebox_snapshot.build_snapshot_queryset

```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.build_snapshot_queryset
```
````

````{py:function} list_snapshots(status: str | None = None, url__icontains: str | None = None, url__istartswith: str | None = None, tag: str | None = None, crawl_id: str | None = None, limit: int | None = None, sort: str | None = None, csv: str | None = None, with_headers: bool = False, search: str | None = None, query: str | None = None) -> int
:canonical: archivebox.cli.archivebox_snapshot.list_snapshots

```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.list_snapshots
```
````

````{py:function} update_snapshots(status: str | None = None, tag: str | None = None) -> int
:canonical: archivebox.cli.archivebox_snapshot.update_snapshots

```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.update_snapshots
```
````

````{py:function} delete_snapshots(yes: bool = False, dry_run: bool = False) -> int
:canonical: archivebox.cli.archivebox_snapshot.delete_snapshots

```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.delete_snapshots
```
````

````{py:function} main()
:canonical: archivebox.cli.archivebox_snapshot.main

```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.main
```
````

````{py:function} create_cmd(urls: tuple, tag: str, status: str, depth: int)
:canonical: archivebox.cli.archivebox_snapshot.create_cmd

```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.create_cmd
```
````

````{py:function} list_cmd(status: str | None, url__icontains: str | None, url__istartswith: str | None, tag: str | None, crawl_id: str | None, limit: int | None, sort: str | None, csv: str | None, with_headers: bool, search: str | None, query: tuple[str, ...])
:canonical: archivebox.cli.archivebox_snapshot.list_cmd

```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.list_cmd
```
````

````{py:function} update_cmd(status: str | None, tag: str | None)
:canonical: archivebox.cli.archivebox_snapshot.update_cmd

```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.update_cmd
```
````

````{py:function} delete_cmd(yes: bool, dry_run: bool)
:canonical: archivebox.cli.archivebox_snapshot.delete_cmd

```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.delete_cmd
```
````
