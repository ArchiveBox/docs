# {py:mod}`archivebox.cli.archivebox_search`

```{py:module} archivebox.cli.archivebox_search
```

```{autodoc2-docstring} archivebox.cli.archivebox_search
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_apply_pattern_filters <archivebox.cli.archivebox_search._apply_pattern_filters>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_search._apply_pattern_filters
    :summary:
    ```
* - {py:obj}`_snapshots_to_json <archivebox.cli.archivebox_search._snapshots_to_json>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_search._snapshots_to_json
    :summary:
    ```
* - {py:obj}`_snapshots_to_csv <archivebox.cli.archivebox_search._snapshots_to_csv>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_search._snapshots_to_csv
    :summary:
    ```
* - {py:obj}`_snapshots_to_html <archivebox.cli.archivebox_search._snapshots_to_html>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_search._snapshots_to_html
    :summary:
    ```
* - {py:obj}`get_snapshots <archivebox.cli.archivebox_search.get_snapshots>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_search.get_snapshots
    :summary:
    ```
* - {py:obj}`search <archivebox.cli.archivebox_search.search>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_search.search
    :summary:
    ```
* - {py:obj}`main <archivebox.cli.archivebox_search.main>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_search.main
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__command__ <archivebox.cli.archivebox_search.__command__>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_search.__command__
    :summary:
    ```
* - {py:obj}`LINK_FILTERS <archivebox.cli.archivebox_search.LINK_FILTERS>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_search.LINK_FILTERS
    :summary:
    ```
* - {py:obj}`STATUS_CHOICES <archivebox.cli.archivebox_search.STATUS_CHOICES>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_search.STATUS_CHOICES
    :summary:
    ```
````

### API

````{py:data} __command__
:canonical: archivebox.cli.archivebox_search.__command__
:value: >
   'archivebox search'

```{autodoc2-docstring} archivebox.cli.archivebox_search.__command__
```

````

````{py:data} LINK_FILTERS
:canonical: archivebox.cli.archivebox_search.LINK_FILTERS
:type: dict[str, collections.abc.Callable[[str], django.db.models.Q]]
:value: >
   None

```{autodoc2-docstring} archivebox.cli.archivebox_search.LINK_FILTERS
```

````

````{py:data} STATUS_CHOICES
:canonical: archivebox.cli.archivebox_search.STATUS_CHOICES
:value: >
   ['indexed', 'archived', 'unarchived']

```{autodoc2-docstring} archivebox.cli.archivebox_search.STATUS_CHOICES
```

````

````{py:function} _apply_pattern_filters(snapshots: django.db.models.QuerySet[archivebox.core.models.Snapshot, archivebox.core.models.Snapshot], filter_patterns: list[str], filter_type: str) -> django.db.models.QuerySet[archivebox.core.models.Snapshot, archivebox.core.models.Snapshot]
:canonical: archivebox.cli.archivebox_search._apply_pattern_filters

```{autodoc2-docstring} archivebox.cli.archivebox_search._apply_pattern_filters
```
````

````{py:function} _snapshots_to_json(snapshots: django.db.models.QuerySet[archivebox.core.models.Snapshot, archivebox.core.models.Snapshot], *, with_headers: bool) -> str
:canonical: archivebox.cli.archivebox_search._snapshots_to_json

```{autodoc2-docstring} archivebox.cli.archivebox_search._snapshots_to_json
```
````

````{py:function} _snapshots_to_csv(snapshots: django.db.models.QuerySet[archivebox.core.models.Snapshot, archivebox.core.models.Snapshot], *, cols: list[str], with_headers: bool) -> str
:canonical: archivebox.cli.archivebox_search._snapshots_to_csv

```{autodoc2-docstring} archivebox.cli.archivebox_search._snapshots_to_csv
```
````

````{py:function} _snapshots_to_html(snapshots: django.db.models.QuerySet[archivebox.core.models.Snapshot, archivebox.core.models.Snapshot], *, with_headers: bool) -> str
:canonical: archivebox.cli.archivebox_search._snapshots_to_html

```{autodoc2-docstring} archivebox.cli.archivebox_search._snapshots_to_html
```
````

````{py:function} get_snapshots(snapshots: django.db.models.QuerySet[archivebox.core.models.Snapshot, archivebox.core.models.Snapshot] | None = None, filter_patterns: list[str] | None = None, filter_type: str = 'substring', after: float | None = None, before: float | None = None, out_dir: pathlib.Path = DATA_DIR) -> django.db.models.QuerySet[archivebox.core.models.Snapshot, archivebox.core.models.Snapshot]
:canonical: archivebox.cli.archivebox_search.get_snapshots

```{autodoc2-docstring} archivebox.cli.archivebox_search.get_snapshots
```
````

````{py:function} search(filter_patterns: list[str] | None = None, filter_type: str = 'substring', status: str = 'indexed', before: float | None = None, after: float | None = None, sort: str | None = None, json: bool = False, html: bool = False, csv: str | None = None, with_headers: bool = False)
:canonical: archivebox.cli.archivebox_search.search

```{autodoc2-docstring} archivebox.cli.archivebox_search.search
```
````

````{py:function} main(**kwargs)
:canonical: archivebox.cli.archivebox_search.main

```{autodoc2-docstring} archivebox.cli.archivebox_search.main
```
````
