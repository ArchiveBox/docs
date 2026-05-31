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

archivebox.search.admin
```

## Package Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

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
````

### API

````{py:data} _search_backends_cache
:canonical: archivebox.search._search_backends_cache
:type: typing.Optional[dict]
:value: >
   None

```{autodoc2-docstring} archivebox.search._search_backends_cache
```

````

````{py:function} get_available_backends() -> dict
:canonical: archivebox.search.get_available_backends

```{autodoc2-docstring} archivebox.search.get_available_backends
```
````

````{py:function} get_backend() -> typing.Any
:canonical: archivebox.search.get_backend

```{autodoc2-docstring} archivebox.search.get_backend
```
````

````{py:function} query_search_index(query: str) -> django.db.models.QuerySet
:canonical: archivebox.search.query_search_index

```{autodoc2-docstring} archivebox.search.query_search_index
```
````

````{py:function} flush_search_index(snapshots: django.db.models.QuerySet) -> None
:canonical: archivebox.search.flush_search_index

```{autodoc2-docstring} archivebox.search.flush_search_index
```
````
