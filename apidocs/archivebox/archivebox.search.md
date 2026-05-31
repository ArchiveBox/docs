# {py:mod}`archivebox.search`

```{py:module} archivebox.search
```

```{autodoc2-docstring} archivebox.search
:allowtitles:
```

## Submodules

```{toctree}
:titlesonly:
:maxdepth: 1

archivebox.search.sonic_daemon
archivebox.search.admin
```

## Package Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`search_backend_env <archivebox.search.search_backend_env>`
  - ```{autodoc2-docstring} archivebox.search.search_backend_env
    :summary:
    ```
* - {py:obj}`normalize_search_backend_name <archivebox.search.normalize_search_backend_name>`
  - ```{autodoc2-docstring} archivebox.search.normalize_search_backend_name
    :summary:
    ```
* - {py:obj}`get_search_backend_display_name <archivebox.search.get_search_backend_display_name>`
  - ```{autodoc2-docstring} archivebox.search.get_search_backend_display_name
    :summary:
    ```
* - {py:obj}`get_default_search_mode <archivebox.search.get_default_search_mode>`
  - ```{autodoc2-docstring} archivebox.search.get_default_search_mode
    :summary:
    ```
* - {py:obj}`get_search_mode <archivebox.search.get_search_mode>`
  - ```{autodoc2-docstring} archivebox.search.get_search_mode
    :summary:
    ```
* - {py:obj}`get_search_mode_base <archivebox.search.get_search_mode_base>`
  - ```{autodoc2-docstring} archivebox.search.get_search_mode_base
    :summary:
    ```
* - {py:obj}`get_search_mode_backend <archivebox.search.get_search_mode_backend>`
  - ```{autodoc2-docstring} archivebox.search.get_search_mode_backend
    :summary:
    ```
* - {py:obj}`get_search_mode_options <archivebox.search.get_search_mode_options>`
  - ```{autodoc2-docstring} archivebox.search.get_search_mode_options
    :summary:
    ```
* - {py:obj}`prioritize_metadata_matches <archivebox.search.prioritize_metadata_matches>`
  - ```{autodoc2-docstring} archivebox.search.prioritize_metadata_matches
    :summary:
    ```
* - {py:obj}`get_available_backends <archivebox.search.get_available_backends>`
  - ```{autodoc2-docstring} archivebox.search.get_available_backends
    :summary:
    ```
* - {py:obj}`get_backend <archivebox.search.get_backend>`
  - ```{autodoc2-docstring} archivebox.search.get_backend
    :summary:
    ```
* - {py:obj}`query_search_index <archivebox.search.query_search_index>`
  - ```{autodoc2-docstring} archivebox.search.query_search_index
    :summary:
    ```
* - {py:obj}`iter_query_search_ids <archivebox.search.iter_query_search_ids>`
  - ```{autodoc2-docstring} archivebox.search.iter_query_search_ids
    :summary:
    ```
* - {py:obj}`flush_search_index <archivebox.search.flush_search_index>`
  - ```{autodoc2-docstring} archivebox.search.flush_search_index
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_search_backends_cache <archivebox.search._search_backends_cache>`
  - ```{autodoc2-docstring} archivebox.search._search_backends_cache
    :summary:
    ```
* - {py:obj}`SEARCH_MODES <archivebox.search.SEARCH_MODES>`
  - ```{autodoc2-docstring} archivebox.search.SEARCH_MODES
    :summary:
    ```
* - {py:obj}`SEARCH_BACKEND_UI_NAMES <archivebox.search.SEARCH_BACKEND_UI_NAMES>`
  - ```{autodoc2-docstring} archivebox.search.SEARCH_BACKEND_UI_NAMES
    :summary:
    ```
* - {py:obj}`MAX_SEARCH_RANK_IDS <archivebox.search.MAX_SEARCH_RANK_IDS>`
  - ```{autodoc2-docstring} archivebox.search.MAX_SEARCH_RANK_IDS
    :summary:
    ```
````

### API

````{py:data} _search_backends_cache
:canonical: archivebox.search._search_backends_cache
:type: dict | None
:value: >
   None

```{autodoc2-docstring} archivebox.search._search_backends_cache
```

````

````{py:data} SEARCH_MODES
:canonical: archivebox.search.SEARCH_MODES
:value: >
   ('meta', 'contents', 'deep')

```{autodoc2-docstring} archivebox.search.SEARCH_MODES
```

````

````{py:data} SEARCH_BACKEND_UI_NAMES
:canonical: archivebox.search.SEARCH_BACKEND_UI_NAMES
:value: >
   None

```{autodoc2-docstring} archivebox.search.SEARCH_BACKEND_UI_NAMES
```

````

````{py:data} MAX_SEARCH_RANK_IDS
:canonical: archivebox.search.MAX_SEARCH_RANK_IDS
:value: >
   500

```{autodoc2-docstring} archivebox.search.MAX_SEARCH_RANK_IDS
```

````

````{py:function} search_backend_env(config: dict[str, typing.Any] | None = None, **config_kwargs: typing.Any)
:canonical: archivebox.search.search_backend_env

```{autodoc2-docstring} archivebox.search.search_backend_env
```
````

````{py:function} normalize_search_backend_name(backend_name: str | None) -> str
:canonical: archivebox.search.normalize_search_backend_name

```{autodoc2-docstring} archivebox.search.normalize_search_backend_name
```
````

````{py:function} get_search_backend_display_name(backend_name: str) -> str
:canonical: archivebox.search.get_search_backend_display_name

```{autodoc2-docstring} archivebox.search.get_search_backend_display_name
```
````

````{py:function} get_default_search_mode(config: dict[str, typing.Any] | None = None, **config_kwargs: typing.Any) -> str
:canonical: archivebox.search.get_default_search_mode

```{autodoc2-docstring} archivebox.search.get_default_search_mode
```
````

````{py:function} get_search_mode(search_mode: str | None, config: dict[str, typing.Any] | None = None, **config_kwargs: typing.Any) -> str
:canonical: archivebox.search.get_search_mode

```{autodoc2-docstring} archivebox.search.get_search_mode
```
````

````{py:function} get_search_mode_base(search_mode: str | None, config: dict[str, typing.Any] | None = None, **config_kwargs: typing.Any) -> str
:canonical: archivebox.search.get_search_mode_base

```{autodoc2-docstring} archivebox.search.get_search_mode_base
```
````

````{py:function} get_search_mode_backend(search_mode: str | None, config: dict[str, typing.Any] | None = None, **config_kwargs: typing.Any) -> str | None
:canonical: archivebox.search.get_search_mode_backend

```{autodoc2-docstring} archivebox.search.get_search_mode_backend
```
````

````{py:function} get_search_mode_options(config: dict[str, typing.Any] | None = None, **config_kwargs: typing.Any) -> list[dict[str, str]]
:canonical: archivebox.search.get_search_mode_options

```{autodoc2-docstring} archivebox.search.get_search_mode_options
```
````

````{py:function} prioritize_metadata_matches(base_queryset: django.db.models.QuerySet, metadata_queryset: django.db.models.QuerySet, fulltext_queryset: django.db.models.QuerySet, *, deep_queryset: django.db.models.QuerySet | None = None, ordering: list[str] | tuple[str, ...] | None = None) -> django.db.models.QuerySet
:canonical: archivebox.search.prioritize_metadata_matches

```{autodoc2-docstring} archivebox.search.prioritize_metadata_matches
```
````

````{py:function} get_available_backends() -> dict
:canonical: archivebox.search.get_available_backends

```{autodoc2-docstring} archivebox.search.get_available_backends
```
````

````{py:function} get_backend(config: dict[str, typing.Any] | None = None, **config_kwargs: typing.Any) -> typing.Any
:canonical: archivebox.search.get_backend

```{autodoc2-docstring} archivebox.search.get_backend
```
````

````{py:function} query_search_index(query: str, search_mode: str | None = None, config: dict[str, typing.Any] | None = None, max_results: int | None = None, **config_kwargs: typing.Any) -> django.db.models.QuerySet
:canonical: archivebox.search.query_search_index

```{autodoc2-docstring} archivebox.search.query_search_index
```
````

````{py:function} iter_query_search_ids(query: str, search_mode: str | None = None, config: dict[str, typing.Any] | None = None, max_results: int | None = None, **config_kwargs: typing.Any)
:canonical: archivebox.search.iter_query_search_ids

```{autodoc2-docstring} archivebox.search.iter_query_search_ids
```
````

````{py:function} flush_search_index(snapshots: django.db.models.QuerySet, config: dict[str, typing.Any] | None = None, **config_kwargs: typing.Any) -> None
:canonical: archivebox.search.flush_search_index

```{autodoc2-docstring} archivebox.search.flush_search_index
```
````
