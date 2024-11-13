# {py:mod}`abx_plugin_sqlitefts_search.searchbackend`

```{py:module} abx_plugin_sqlitefts_search.searchbackend
```

```{autodoc2-docstring} abx_plugin_sqlitefts_search.searchbackend
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SqliteftsSearchBackend <abx_plugin_sqlitefts_search.searchbackend.SqliteftsSearchBackend>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_escape_sqlite3 <abx_plugin_sqlitefts_search.searchbackend._escape_sqlite3>`
  - ```{autodoc2-docstring} abx_plugin_sqlitefts_search.searchbackend._escape_sqlite3
    :summary:
    ```
* - {py:obj}`_escape_sqlite3_value <abx_plugin_sqlitefts_search.searchbackend._escape_sqlite3_value>`
  - ```{autodoc2-docstring} abx_plugin_sqlitefts_search.searchbackend._escape_sqlite3_value
    :summary:
    ```
* - {py:obj}`_escape_sqlite3_identifier <abx_plugin_sqlitefts_search.searchbackend._escape_sqlite3_identifier>`
  - ```{autodoc2-docstring} abx_plugin_sqlitefts_search.searchbackend._escape_sqlite3_identifier
    :summary:
    ```
* - {py:obj}`_create_tables <abx_plugin_sqlitefts_search.searchbackend._create_tables>`
  - ```{autodoc2-docstring} abx_plugin_sqlitefts_search.searchbackend._create_tables
    :summary:
    ```
* - {py:obj}`_handle_query_exception <abx_plugin_sqlitefts_search.searchbackend._handle_query_exception>`
  - ```{autodoc2-docstring} abx_plugin_sqlitefts_search.searchbackend._handle_query_exception
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <abx_plugin_sqlitefts_search.searchbackend.__package__>`
  - ```{autodoc2-docstring} abx_plugin_sqlitefts_search.searchbackend.__package__
    :summary:
    ```
* - {py:obj}`SQLITEFTS_SEARCH_BACKEND <abx_plugin_sqlitefts_search.searchbackend.SQLITEFTS_SEARCH_BACKEND>`
  - ```{autodoc2-docstring} abx_plugin_sqlitefts_search.searchbackend.SQLITEFTS_SEARCH_BACKEND
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: abx_plugin_sqlitefts_search.searchbackend.__package__
:value: >
   'abx_plugin_sqlitefts_search'

```{autodoc2-docstring} abx_plugin_sqlitefts_search.searchbackend.__package__
```

````

````{py:function} _escape_sqlite3(value: str, *, quote: str, errors='strict') -> str
:canonical: abx_plugin_sqlitefts_search.searchbackend._escape_sqlite3

```{autodoc2-docstring} abx_plugin_sqlitefts_search.searchbackend._escape_sqlite3
```
````

````{py:function} _escape_sqlite3_value(value: str, errors='strict') -> str
:canonical: abx_plugin_sqlitefts_search.searchbackend._escape_sqlite3_value

```{autodoc2-docstring} abx_plugin_sqlitefts_search.searchbackend._escape_sqlite3_value
```
````

````{py:function} _escape_sqlite3_identifier(value: str) -> str
:canonical: abx_plugin_sqlitefts_search.searchbackend._escape_sqlite3_identifier

```{autodoc2-docstring} abx_plugin_sqlitefts_search.searchbackend._escape_sqlite3_identifier
```
````

````{py:function} _create_tables()
:canonical: abx_plugin_sqlitefts_search.searchbackend._create_tables

```{autodoc2-docstring} abx_plugin_sqlitefts_search.searchbackend._create_tables
```
````

````{py:function} _handle_query_exception(exc: Exception)
:canonical: abx_plugin_sqlitefts_search.searchbackend._handle_query_exception

```{autodoc2-docstring} abx_plugin_sqlitefts_search.searchbackend._handle_query_exception
```
````

`````{py:class} SqliteftsSearchBackend
:canonical: abx_plugin_sqlitefts_search.searchbackend.SqliteftsSearchBackend

Bases: {py:obj}`abx_spec_searchbackend.BaseSearchBackend`

````{py:attribute} name
:canonical: abx_plugin_sqlitefts_search.searchbackend.SqliteftsSearchBackend.name
:type: str
:value: >
   'sqlite'

```{autodoc2-docstring} abx_plugin_sqlitefts_search.searchbackend.SqliteftsSearchBackend.name
```

````

````{py:attribute} docs_url
:canonical: abx_plugin_sqlitefts_search.searchbackend.SqliteftsSearchBackend.docs_url
:type: str
:value: >
   'https://www.sqlite.org/fts5.html'

```{autodoc2-docstring} abx_plugin_sqlitefts_search.searchbackend.SqliteftsSearchBackend.docs_url
```

````

````{py:method} index(snapshot_id: str, texts: typing.List[str])
:canonical: abx_plugin_sqlitefts_search.searchbackend.SqliteftsSearchBackend.index
:staticmethod:

```{autodoc2-docstring} abx_plugin_sqlitefts_search.searchbackend.SqliteftsSearchBackend.index
```

````

````{py:method} search(text: str) -> typing.List[str]
:canonical: abx_plugin_sqlitefts_search.searchbackend.SqliteftsSearchBackend.search
:staticmethod:

```{autodoc2-docstring} abx_plugin_sqlitefts_search.searchbackend.SqliteftsSearchBackend.search
```

````

````{py:method} flush(snapshot_ids: typing.Iterable[str])
:canonical: abx_plugin_sqlitefts_search.searchbackend.SqliteftsSearchBackend.flush
:staticmethod:

```{autodoc2-docstring} abx_plugin_sqlitefts_search.searchbackend.SqliteftsSearchBackend.flush
```

````

`````

````{py:data} SQLITEFTS_SEARCH_BACKEND
:canonical: abx_plugin_sqlitefts_search.searchbackend.SQLITEFTS_SEARCH_BACKEND
:value: >
   'SqliteftsSearchBackend(...)'

```{autodoc2-docstring} abx_plugin_sqlitefts_search.searchbackend.SQLITEFTS_SEARCH_BACKEND
```

````
