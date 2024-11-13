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

* - {py:obj}`log_index_started <archivebox.search.log_index_started>`
  - ```{autodoc2-docstring} archivebox.search.log_index_started
    :summary:
    ```
* - {py:obj}`get_file_result_content <archivebox.search.get_file_result_content>`
  - ```{autodoc2-docstring} archivebox.search.get_file_result_content
    :summary:
    ```
* - {py:obj}`get_indexable_content <archivebox.search.get_indexable_content>`
  - ```{autodoc2-docstring} archivebox.search.get_indexable_content
    :summary:
    ```
* - {py:obj}`import_backend <archivebox.search.import_backend>`
  - ```{autodoc2-docstring} archivebox.search.import_backend
    :summary:
    ```
* - {py:obj}`write_search_index <archivebox.search.write_search_index>`
  - ```{autodoc2-docstring} archivebox.search.write_search_index
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
* - {py:obj}`index_links <archivebox.search.index_links>`
  - ```{autodoc2-docstring} archivebox.search.index_links
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.search.__package__>`
  - ```{autodoc2-docstring} archivebox.search.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.search.__package__
:value: >
   'archivebox.search'

```{autodoc2-docstring} archivebox.search.__package__
```

````

````{py:function} log_index_started(url)
:canonical: archivebox.search.log_index_started

```{autodoc2-docstring} archivebox.search.log_index_started
```
````

````{py:function} get_file_result_content(res, extra_path, use_pwd=False)
:canonical: archivebox.search.get_file_result_content

```{autodoc2-docstring} archivebox.search.get_file_result_content
```
````

````{py:function} get_indexable_content(results: django.db.models.QuerySet)
:canonical: archivebox.search.get_indexable_content

```{autodoc2-docstring} archivebox.search.get_indexable_content
```
````

````{py:function} import_backend()
:canonical: archivebox.search.import_backend

```{autodoc2-docstring} archivebox.search.import_backend
```
````

````{py:function} write_search_index(link: archivebox.index.schema.Link, texts: typing.Union[typing.List[str], None] = None, out_dir: pathlib.Path = settings.DATA_DIR, skip_text_index: bool = False) -> None
:canonical: archivebox.search.write_search_index

```{autodoc2-docstring} archivebox.search.write_search_index
```
````

````{py:function} query_search_index(query: str, out_dir: pathlib.Path = settings.DATA_DIR) -> django.db.models.QuerySet
:canonical: archivebox.search.query_search_index

```{autodoc2-docstring} archivebox.search.query_search_index
```
````

````{py:function} flush_search_index(snapshots: django.db.models.QuerySet)
:canonical: archivebox.search.flush_search_index

```{autodoc2-docstring} archivebox.search.flush_search_index
```
````

````{py:function} index_links(links: typing.Union[typing.List[archivebox.index.schema.Link], None], out_dir: pathlib.Path = settings.DATA_DIR)
:canonical: archivebox.search.index_links

```{autodoc2-docstring} archivebox.search.index_links
```
````
