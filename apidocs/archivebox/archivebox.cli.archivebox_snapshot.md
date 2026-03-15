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

````{py:function} create_snapshots(urls: typing.Iterable[str], tag: str = '', status: str = 'queued', depth: int = 0, created_by_id: typing.Optional[int] = None) -> int
:canonical: archivebox.cli.archivebox_snapshot.create_snapshots

```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.create_snapshots
```
````

````{py:function} list_snapshots(status: typing.Optional[str] = None, url__icontains: typing.Optional[str] = None, url__istartswith: typing.Optional[str] = None, tag: typing.Optional[str] = None, crawl_id: typing.Optional[str] = None, limit: typing.Optional[int] = None) -> int
:canonical: archivebox.cli.archivebox_snapshot.list_snapshots

```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.list_snapshots
```
````

````{py:function} update_snapshots(status: typing.Optional[str] = None, tag: typing.Optional[str] = None) -> int
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

````{py:function} list_cmd(status: typing.Optional[str], url__icontains: typing.Optional[str], url__istartswith: typing.Optional[str], tag: typing.Optional[str], crawl_id: typing.Optional[str], limit: typing.Optional[int])
:canonical: archivebox.cli.archivebox_snapshot.list_cmd

```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.list_cmd
```
````

````{py:function} update_cmd(status: typing.Optional[str], tag: typing.Optional[str])
:canonical: archivebox.cli.archivebox_snapshot.update_cmd

```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.update_cmd
```
````

````{py:function} delete_cmd(yes: bool, dry_run: bool)
:canonical: archivebox.cli.archivebox_snapshot.delete_cmd

```{autodoc2-docstring} archivebox.cli.archivebox_snapshot.delete_cmd
```
````
