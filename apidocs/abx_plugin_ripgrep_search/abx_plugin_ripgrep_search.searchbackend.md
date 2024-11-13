# {py:mod}`abx_plugin_ripgrep_search.searchbackend`

```{py:module} abx_plugin_ripgrep_search.searchbackend
```

```{autodoc2-docstring} abx_plugin_ripgrep_search.searchbackend
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`RipgrepSearchBackend <abx_plugin_ripgrep_search.searchbackend.RipgrepSearchBackend>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TIMESTAMP_REGEX <abx_plugin_ripgrep_search.searchbackend.TIMESTAMP_REGEX>`
  - ```{autodoc2-docstring} abx_plugin_ripgrep_search.searchbackend.TIMESTAMP_REGEX
    :summary:
    ```
* - {py:obj}`RIPGREP_SEARCH_BACKEND <abx_plugin_ripgrep_search.searchbackend.RIPGREP_SEARCH_BACKEND>`
  - ```{autodoc2-docstring} abx_plugin_ripgrep_search.searchbackend.RIPGREP_SEARCH_BACKEND
    :summary:
    ```
````

### API

````{py:data} TIMESTAMP_REGEX
:canonical: abx_plugin_ripgrep_search.searchbackend.TIMESTAMP_REGEX
:value: >
   'compile(...)'

```{autodoc2-docstring} abx_plugin_ripgrep_search.searchbackend.TIMESTAMP_REGEX
```

````

`````{py:class} RipgrepSearchBackend
:canonical: abx_plugin_ripgrep_search.searchbackend.RipgrepSearchBackend

Bases: {py:obj}`abx_spec_searchbackend.BaseSearchBackend`

````{py:attribute} name
:canonical: abx_plugin_ripgrep_search.searchbackend.RipgrepSearchBackend.name
:type: str
:value: >
   'ripgrep'

```{autodoc2-docstring} abx_plugin_ripgrep_search.searchbackend.RipgrepSearchBackend.name
```

````

````{py:attribute} docs_url
:canonical: abx_plugin_ripgrep_search.searchbackend.RipgrepSearchBackend.docs_url
:type: str
:value: >
   'https://github.com/BurntSushi/ripgrep'

```{autodoc2-docstring} abx_plugin_ripgrep_search.searchbackend.RipgrepSearchBackend.docs_url
```

````

````{py:method} index(snapshot_id: str, texts: typing.List[str])
:canonical: abx_plugin_ripgrep_search.searchbackend.RipgrepSearchBackend.index
:staticmethod:

```{autodoc2-docstring} abx_plugin_ripgrep_search.searchbackend.RipgrepSearchBackend.index
```

````

````{py:method} flush(snapshot_ids: typing.Iterable[str])
:canonical: abx_plugin_ripgrep_search.searchbackend.RipgrepSearchBackend.flush
:staticmethod:

```{autodoc2-docstring} abx_plugin_ripgrep_search.searchbackend.RipgrepSearchBackend.flush
```

````

````{py:method} search(text: str) -> typing.List[str]
:canonical: abx_plugin_ripgrep_search.searchbackend.RipgrepSearchBackend.search
:staticmethod:

```{autodoc2-docstring} abx_plugin_ripgrep_search.searchbackend.RipgrepSearchBackend.search
```

````

`````

````{py:data} RIPGREP_SEARCH_BACKEND
:canonical: abx_plugin_ripgrep_search.searchbackend.RIPGREP_SEARCH_BACKEND
:value: >
   'RipgrepSearchBackend(...)'

```{autodoc2-docstring} abx_plugin_ripgrep_search.searchbackend.RIPGREP_SEARCH_BACKEND
```

````
