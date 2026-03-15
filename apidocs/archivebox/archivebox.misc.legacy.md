# {py:mod}`archivebox.misc.legacy`

```{py:module} archivebox.misc.legacy
```

```{autodoc2-docstring} archivebox.misc.legacy
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SnapshotDict <archivebox.misc.legacy.SnapshotDict>`
  - ```{autodoc2-docstring} archivebox.misc.legacy.SnapshotDict
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`parse_json_main_index <archivebox.misc.legacy.parse_json_main_index>`
  - ```{autodoc2-docstring} archivebox.misc.legacy.parse_json_main_index
    :summary:
    ```
* - {py:obj}`parse_json_links_details <archivebox.misc.legacy.parse_json_links_details>`
  - ```{autodoc2-docstring} archivebox.misc.legacy.parse_json_links_details
    :summary:
    ```
````

### API

`````{py:class} SnapshotDict()
:canonical: archivebox.misc.legacy.SnapshotDict

Bases: {py:obj}`typing.TypedDict`

```{autodoc2-docstring} archivebox.misc.legacy.SnapshotDict
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.misc.legacy.SnapshotDict.__init__
```

````{py:attribute} url
:canonical: archivebox.misc.legacy.SnapshotDict.url
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.misc.legacy.SnapshotDict.url
```

````

````{py:attribute} timestamp
:canonical: archivebox.misc.legacy.SnapshotDict.timestamp
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.misc.legacy.SnapshotDict.timestamp
```

````

````{py:attribute} title
:canonical: archivebox.misc.legacy.SnapshotDict.title
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.misc.legacy.SnapshotDict.title
```

````

````{py:attribute} tags
:canonical: archivebox.misc.legacy.SnapshotDict.tags
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.misc.legacy.SnapshotDict.tags
```

````

````{py:attribute} sources
:canonical: archivebox.misc.legacy.SnapshotDict.sources
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} archivebox.misc.legacy.SnapshotDict.sources
```

````

`````

````{py:function} parse_json_main_index(out_dir: pathlib.Path) -> typing.Iterator[archivebox.misc.legacy.SnapshotDict]
:canonical: archivebox.misc.legacy.parse_json_main_index

```{autodoc2-docstring} archivebox.misc.legacy.parse_json_main_index
```
````

````{py:function} parse_json_links_details(out_dir: pathlib.Path) -> typing.Iterator[archivebox.misc.legacy.SnapshotDict]
:canonical: archivebox.misc.legacy.parse_json_links_details

```{autodoc2-docstring} archivebox.misc.legacy.parse_json_links_details
```
````
