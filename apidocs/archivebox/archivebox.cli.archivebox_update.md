# {py:mod}`archivebox.cli.archivebox_update`

```{py:module} archivebox.cli.archivebox_update
```

```{autodoc2-docstring} archivebox.cli.archivebox_update
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`update <archivebox.cli.archivebox_update.update>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_update.update
    :summary:
    ```
* - {py:obj}`drain_old_archive_dirs <archivebox.cli.archivebox_update.drain_old_archive_dirs>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_update.drain_old_archive_dirs
    :summary:
    ```
* - {py:obj}`process_all_db_snapshots <archivebox.cli.archivebox_update.process_all_db_snapshots>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_update.process_all_db_snapshots
    :summary:
    ```
* - {py:obj}`process_filtered_snapshots <archivebox.cli.archivebox_update.process_filtered_snapshots>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_update.process_filtered_snapshots
    :summary:
    ```
* - {py:obj}`print_stats <archivebox.cli.archivebox_update.print_stats>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_update.print_stats
    :summary:
    ```
* - {py:obj}`print_combined_stats <archivebox.cli.archivebox_update.print_combined_stats>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_update.print_combined_stats
    :summary:
    ```
* - {py:obj}`main <archivebox.cli.archivebox_update.main>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_update.main
    :summary:
    ```
````

### API

````{py:function} update(filter_patterns: typing.Iterable[str] = (), filter_type: str = 'exact', before: float | None = None, after: float | None = None, resume: str | None = None, batch_size: int = 100, continuous: bool = False) -> None
:canonical: archivebox.cli.archivebox_update.update

```{autodoc2-docstring} archivebox.cli.archivebox_update.update
```
````

````{py:function} drain_old_archive_dirs(resume_from: str = None, batch_size: int = 100) -> dict
:canonical: archivebox.cli.archivebox_update.drain_old_archive_dirs

```{autodoc2-docstring} archivebox.cli.archivebox_update.drain_old_archive_dirs
```
````

````{py:function} process_all_db_snapshots(batch_size: int = 100) -> dict
:canonical: archivebox.cli.archivebox_update.process_all_db_snapshots

```{autodoc2-docstring} archivebox.cli.archivebox_update.process_all_db_snapshots
```
````

````{py:function} process_filtered_snapshots(filter_patterns: typing.Iterable[str], filter_type: str, before: float | None, after: float | None, batch_size: int) -> dict
:canonical: archivebox.cli.archivebox_update.process_filtered_snapshots

```{autodoc2-docstring} archivebox.cli.archivebox_update.process_filtered_snapshots
```
````

````{py:function} print_stats(stats: dict)
:canonical: archivebox.cli.archivebox_update.print_stats

```{autodoc2-docstring} archivebox.cli.archivebox_update.print_stats
```
````

````{py:function} print_combined_stats(stats_combined: dict)
:canonical: archivebox.cli.archivebox_update.print_combined_stats

```{autodoc2-docstring} archivebox.cli.archivebox_update.print_combined_stats
```
````

````{py:function} main(**kwargs)
:canonical: archivebox.cli.archivebox_update.main

```{autodoc2-docstring} archivebox.cli.archivebox_update.main
```
````
