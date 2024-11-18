# {py:mod}`abx_spec_searchbackend`

```{py:module} abx_spec_searchbackend
```

```{autodoc2-docstring} abx_spec_searchbackend
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseSearchBackend <abx_spec_searchbackend.BaseSearchBackend>`
  -
* - {py:obj}`SearchBackendPluginSpec <abx_spec_searchbackend.SearchBackendPluginSpec>`
  - ```{autodoc2-docstring} abx_spec_searchbackend.SearchBackendPluginSpec
    :summary:
    ```
* - {py:obj}`ExpectedPluginSpec <abx_spec_searchbackend.ExpectedPluginSpec>`
  - ```{autodoc2-docstring} abx_spec_searchbackend.ExpectedPluginSpec
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PLUGIN_SPEC <abx_spec_searchbackend.PLUGIN_SPEC>`
  - ```{autodoc2-docstring} abx_spec_searchbackend.PLUGIN_SPEC
    :summary:
    ```
* - {py:obj}`TypedPluginManager <abx_spec_searchbackend.TypedPluginManager>`
  - ```{autodoc2-docstring} abx_spec_searchbackend.TypedPluginManager
    :summary:
    ```
* - {py:obj}`pm <abx_spec_searchbackend.pm>`
  - ```{autodoc2-docstring} abx_spec_searchbackend.pm
    :summary:
    ```
````

### API

`````{py:class} BaseSearchBackend
:canonical: abx_spec_searchbackend.BaseSearchBackend

Bases: {py:obj}`abc.ABC`

````{py:attribute} name
:canonical: abx_spec_searchbackend.BaseSearchBackend.name
:type: str
:value: >
   None

```{autodoc2-docstring} abx_spec_searchbackend.BaseSearchBackend.name
```

````

````{py:method} index(snapshot_id: str, texts: typing.List[str])
:canonical: abx_spec_searchbackend.BaseSearchBackend.index
:abstractmethod:
:staticmethod:

```{autodoc2-docstring} abx_spec_searchbackend.BaseSearchBackend.index
```

````

````{py:method} flush(snapshot_ids: typing.Iterable[str])
:canonical: abx_spec_searchbackend.BaseSearchBackend.flush
:abstractmethod:
:staticmethod:

```{autodoc2-docstring} abx_spec_searchbackend.BaseSearchBackend.flush
```

````

````{py:method} search(text: str) -> typing.List[str]
:canonical: abx_spec_searchbackend.BaseSearchBackend.search
:abstractmethod:
:staticmethod:

```{autodoc2-docstring} abx_spec_searchbackend.BaseSearchBackend.search
```

````

`````

`````{py:class} SearchBackendPluginSpec
:canonical: abx_spec_searchbackend.SearchBackendPluginSpec

```{autodoc2-docstring} abx_spec_searchbackend.SearchBackendPluginSpec
```

````{py:attribute} __order__
:canonical: abx_spec_searchbackend.SearchBackendPluginSpec.__order__
:value: >
   10

```{autodoc2-docstring} abx_spec_searchbackend.SearchBackendPluginSpec.__order__
```

````

````{py:method} get_SEARCHBACKENDS() -> typing.Dict[abx.PluginId, abx_spec_searchbackend.BaseSearchBackend]
:canonical: abx_spec_searchbackend.SearchBackendPluginSpec.get_SEARCHBACKENDS
:staticmethod:

```{autodoc2-docstring} abx_spec_searchbackend.SearchBackendPluginSpec.get_SEARCHBACKENDS
```

````

`````

````{py:class} ExpectedPluginSpec
:canonical: abx_spec_searchbackend.ExpectedPluginSpec

Bases: {py:obj}`abx_spec_searchbackend.SearchBackendPluginSpec`, {py:obj}`abx_spec_config.ConfigPluginSpec`

```{autodoc2-docstring} abx_spec_searchbackend.ExpectedPluginSpec
```

````

````{py:data} PLUGIN_SPEC
:canonical: abx_spec_searchbackend.PLUGIN_SPEC
:value: >
   None

```{autodoc2-docstring} abx_spec_searchbackend.PLUGIN_SPEC
```

````

````{py:data} TypedPluginManager
:canonical: abx_spec_searchbackend.TypedPluginManager
:value: >
   None

```{autodoc2-docstring} abx_spec_searchbackend.TypedPluginManager
```

````

````{py:data} pm
:canonical: abx_spec_searchbackend.pm
:value: >
   'cast(...)'

```{autodoc2-docstring} abx_spec_searchbackend.pm
```

````
