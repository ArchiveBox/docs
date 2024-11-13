# {py:mod}`abx_plugin_sonic_search.searchbackend`

```{py:module} abx_plugin_sonic_search.searchbackend
```

```{autodoc2-docstring} abx_plugin_sonic_search.searchbackend
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SonicSearchBackend <abx_plugin_sonic_search.searchbackend.SonicSearchBackend>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <abx_plugin_sonic_search.searchbackend.__package__>`
  - ```{autodoc2-docstring} abx_plugin_sonic_search.searchbackend.__package__
    :summary:
    ```
* - {py:obj}`SONIC_SEARCH_BACKEND <abx_plugin_sonic_search.searchbackend.SONIC_SEARCH_BACKEND>`
  - ```{autodoc2-docstring} abx_plugin_sonic_search.searchbackend.SONIC_SEARCH_BACKEND
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: abx_plugin_sonic_search.searchbackend.__package__
:value: >
   'plugins_search.sonic'

```{autodoc2-docstring} abx_plugin_sonic_search.searchbackend.__package__
```

````

`````{py:class} SonicSearchBackend
:canonical: abx_plugin_sonic_search.searchbackend.SonicSearchBackend

Bases: {py:obj}`abx_spec_searchbackend.BaseSearchBackend`

````{py:attribute} name
:canonical: abx_plugin_sonic_search.searchbackend.SonicSearchBackend.name
:type: str
:value: >
   'sonic'

```{autodoc2-docstring} abx_plugin_sonic_search.searchbackend.SonicSearchBackend.name
```

````

````{py:attribute} docs_url
:canonical: abx_plugin_sonic_search.searchbackend.SonicSearchBackend.docs_url
:type: str
:value: >
   'https://github.com/valeriansaliou/sonic'

```{autodoc2-docstring} abx_plugin_sonic_search.searchbackend.SonicSearchBackend.docs_url
```

````

````{py:method} index(snapshot_id: str, texts: typing.List[str])
:canonical: abx_plugin_sonic_search.searchbackend.SonicSearchBackend.index
:staticmethod:

```{autodoc2-docstring} abx_plugin_sonic_search.searchbackend.SonicSearchBackend.index
```

````

````{py:method} flush(snapshot_ids: typing.Generator[str, None, None])
:canonical: abx_plugin_sonic_search.searchbackend.SonicSearchBackend.flush
:staticmethod:

```{autodoc2-docstring} abx_plugin_sonic_search.searchbackend.SonicSearchBackend.flush
```

````

````{py:method} search(text: str) -> typing.List[str]
:canonical: abx_plugin_sonic_search.searchbackend.SonicSearchBackend.search
:staticmethod:

```{autodoc2-docstring} abx_plugin_sonic_search.searchbackend.SonicSearchBackend.search
```

````

`````

````{py:data} SONIC_SEARCH_BACKEND
:canonical: abx_plugin_sonic_search.searchbackend.SONIC_SEARCH_BACKEND
:value: >
   'SonicSearchBackend(...)'

```{autodoc2-docstring} abx_plugin_sonic_search.searchbackend.SONIC_SEARCH_BACKEND
```

````
