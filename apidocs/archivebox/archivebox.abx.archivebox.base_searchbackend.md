# {py:mod}`archivebox.abx.archivebox.base_searchbackend`

```{py:module} archivebox.abx.archivebox.base_searchbackend
```

```{autodoc2-docstring} archivebox.abx.archivebox.base_searchbackend
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseSearchBackend <archivebox.abx.archivebox.base_searchbackend.BaseSearchBackend>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.abx.archivebox.base_searchbackend.__package__>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_searchbackend.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.abx.archivebox.base_searchbackend.__package__
:value: >
   'abx.archivebox'

```{autodoc2-docstring} archivebox.abx.archivebox.base_searchbackend.__package__
```

````

`````{py:class} BaseSearchBackend(/, **data: typing.Any)
:canonical: archivebox.abx.archivebox.base_searchbackend.BaseSearchBackend

Bases: {py:obj}`archivebox.abx.archivebox.base_hook.BaseHook`

````{py:attribute} hook_type
:canonical: archivebox.abx.archivebox.base_searchbackend.BaseSearchBackend.hook_type
:type: archivebox.abx.archivebox.base_hook.HookType
:value: >
   'SEARCHBACKEND'

```{autodoc2-docstring} archivebox.abx.archivebox.base_searchbackend.BaseSearchBackend.hook_type
```

````

````{py:attribute} name
:canonical: archivebox.abx.archivebox.base_searchbackend.BaseSearchBackend.name
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.abx.archivebox.base_searchbackend.BaseSearchBackend.name
```

````

````{py:method} index(snapshot_id: str, texts: typing.List[str])
:canonical: archivebox.abx.archivebox.base_searchbackend.BaseSearchBackend.index
:staticmethod:

```{autodoc2-docstring} archivebox.abx.archivebox.base_searchbackend.BaseSearchBackend.index
```

````

````{py:method} flush(snapshot_ids: typing.Iterable[str])
:canonical: archivebox.abx.archivebox.base_searchbackend.BaseSearchBackend.flush
:staticmethod:

```{autodoc2-docstring} archivebox.abx.archivebox.base_searchbackend.BaseSearchBackend.flush
```

````

````{py:method} search(text: str) -> typing.List[str]
:canonical: archivebox.abx.archivebox.base_searchbackend.BaseSearchBackend.search
:abstractmethod:
:staticmethod:

```{autodoc2-docstring} archivebox.abx.archivebox.base_searchbackend.BaseSearchBackend.search
```

````

````{py:method} get_SEARCHBACKENDS()
:canonical: archivebox.abx.archivebox.base_searchbackend.BaseSearchBackend.get_SEARCHBACKENDS

```{autodoc2-docstring} archivebox.abx.archivebox.base_searchbackend.BaseSearchBackend.get_SEARCHBACKENDS
```

````

`````
