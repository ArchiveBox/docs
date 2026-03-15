# {py:mod}`archivebox.workers.tasks`

```{py:module} archivebox.workers.tasks
```

```{autodoc2-docstring} archivebox.workers.tasks
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`bg_add <archivebox.workers.tasks.bg_add>`
  - ```{autodoc2-docstring} archivebox.workers.tasks.bg_add
    :summary:
    ```
* - {py:obj}`bg_archive_snapshots <archivebox.workers.tasks.bg_archive_snapshots>`
  - ```{autodoc2-docstring} archivebox.workers.tasks.bg_archive_snapshots
    :summary:
    ```
* - {py:obj}`bg_archive_snapshot <archivebox.workers.tasks.bg_archive_snapshot>`
  - ```{autodoc2-docstring} archivebox.workers.tasks.bg_archive_snapshot
    :summary:
    ```
````

### API

````{py:function} bg_add(add_kwargs: dict) -> int
:canonical: archivebox.workers.tasks.bg_add

```{autodoc2-docstring} archivebox.workers.tasks.bg_add
```
````

````{py:function} bg_archive_snapshots(snapshots, kwargs: dict | None = None) -> int
:canonical: archivebox.workers.tasks.bg_archive_snapshots

```{autodoc2-docstring} archivebox.workers.tasks.bg_archive_snapshots
```
````

````{py:function} bg_archive_snapshot(snapshot, overwrite: bool = False, methods: list | None = None) -> int
:canonical: archivebox.workers.tasks.bg_archive_snapshot

```{autodoc2-docstring} archivebox.workers.tasks.bg_archive_snapshot
```
````
