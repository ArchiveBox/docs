# {py:mod}`archivebox.extractors`

```{py:module} archivebox.extractors
```

```{autodoc2-docstring} archivebox.extractors
:allowtitles:
```

## Submodules

```{toctree}
:titlesonly:
:maxdepth: 1

archivebox.extractors.htmltotext
archivebox.extractors.git
archivebox.extractors.singlefile
archivebox.extractors.media
archivebox.extractors.archive_org
archivebox.extractors.readability
archivebox.extractors.mercury
archivebox.extractors.favicon
archivebox.extractors.pdf
archivebox.extractors.headers
archivebox.extractors.screenshot
archivebox.extractors.dom
archivebox.extractors.title
archivebox.extractors.wget
```

## Package Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ExtractorModuleProtocol <archivebox.extractors.ExtractorModuleProtocol>`
  - ```{autodoc2-docstring} archivebox.extractors.ExtractorModuleProtocol
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_default_archive_methods <archivebox.extractors.get_default_archive_methods>`
  - ```{autodoc2-docstring} archivebox.extractors.get_default_archive_methods
    :summary:
    ```
* - {py:obj}`get_archive_methods_for_link <archivebox.extractors.get_archive_methods_for_link>`
  - ```{autodoc2-docstring} archivebox.extractors.get_archive_methods_for_link
    :summary:
    ```
* - {py:obj}`ignore_methods <archivebox.extractors.ignore_methods>`
  - ```{autodoc2-docstring} archivebox.extractors.ignore_methods
    :summary:
    ```
* - {py:obj}`archive_link <archivebox.extractors.archive_link>`
  - ```{autodoc2-docstring} archivebox.extractors.archive_link
    :summary:
    ```
* - {py:obj}`archive_links <archivebox.extractors.archive_links>`
  - ```{autodoc2-docstring} archivebox.extractors.archive_links
    :summary:
    ```
* - {py:obj}`get_extractors <archivebox.extractors.get_extractors>`
  - ```{autodoc2-docstring} archivebox.extractors.get_extractors
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.extractors.__package__>`
  - ```{autodoc2-docstring} archivebox.extractors.__package__
    :summary:
    ```
* - {py:obj}`ShouldSaveFunction <archivebox.extractors.ShouldSaveFunction>`
  - ```{autodoc2-docstring} archivebox.extractors.ShouldSaveFunction
    :summary:
    ```
* - {py:obj}`SaveFunction <archivebox.extractors.SaveFunction>`
  - ```{autodoc2-docstring} archivebox.extractors.SaveFunction
    :summary:
    ```
* - {py:obj}`ArchiveMethodEntry <archivebox.extractors.ArchiveMethodEntry>`
  - ```{autodoc2-docstring} archivebox.extractors.ArchiveMethodEntry
    :summary:
    ```
* - {py:obj}`ARCHIVE_METHODS_INDEXING_PRECEDENCE <archivebox.extractors.ARCHIVE_METHODS_INDEXING_PRECEDENCE>`
  - ```{autodoc2-docstring} archivebox.extractors.ARCHIVE_METHODS_INDEXING_PRECEDENCE
    :summary:
    ```
* - {py:obj}`EXTRACTORS_DIR <archivebox.extractors.EXTRACTORS_DIR>`
  - ```{autodoc2-docstring} archivebox.extractors.EXTRACTORS_DIR
    :summary:
    ```
* - {py:obj}`EXTRACTORS <archivebox.extractors.EXTRACTORS>`
  - ```{autodoc2-docstring} archivebox.extractors.EXTRACTORS
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.extractors.__package__
:value: >
   'archivebox.extractors'

```{autodoc2-docstring} archivebox.extractors.__package__
```

````

````{py:data} ShouldSaveFunction
:canonical: archivebox.extractors.ShouldSaveFunction
:value: >
   None

```{autodoc2-docstring} archivebox.extractors.ShouldSaveFunction
```

````

````{py:data} SaveFunction
:canonical: archivebox.extractors.SaveFunction
:value: >
   None

```{autodoc2-docstring} archivebox.extractors.SaveFunction
```

````

````{py:data} ArchiveMethodEntry
:canonical: archivebox.extractors.ArchiveMethodEntry
:value: >
   None

```{autodoc2-docstring} archivebox.extractors.ArchiveMethodEntry
```

````

````{py:function} get_default_archive_methods() -> typing.List[archivebox.extractors.ArchiveMethodEntry]
:canonical: archivebox.extractors.get_default_archive_methods

```{autodoc2-docstring} archivebox.extractors.get_default_archive_methods
```
````

````{py:data} ARCHIVE_METHODS_INDEXING_PRECEDENCE
:canonical: archivebox.extractors.ARCHIVE_METHODS_INDEXING_PRECEDENCE
:value: >
   [('readability', 1), ('mercury', 2), ('htmltotext', 3), ('singlefile', 4), ('dom', 5), ('wget', 6)]

```{autodoc2-docstring} archivebox.extractors.ARCHIVE_METHODS_INDEXING_PRECEDENCE
```

````

````{py:function} get_archive_methods_for_link(link: archivebox.index.schema.Link) -> typing.Iterable[archivebox.extractors.ArchiveMethodEntry]
:canonical: archivebox.extractors.get_archive_methods_for_link

```{autodoc2-docstring} archivebox.extractors.get_archive_methods_for_link
```
````

````{py:function} ignore_methods(to_ignore: typing.List[str]) -> typing.Iterable[str]
:canonical: archivebox.extractors.ignore_methods

```{autodoc2-docstring} archivebox.extractors.ignore_methods
```
````

````{py:function} archive_link(link: archivebox.index.schema.Link, overwrite: bool = False, methods: typing.Optional[typing.Iterable[str]] = None, out_dir: typing.Optional[pathlib.Path] = None, created_by_id: int | None = None) -> archivebox.index.schema.Link
:canonical: archivebox.extractors.archive_link

```{autodoc2-docstring} archivebox.extractors.archive_link
```
````

````{py:function} archive_links(all_links: typing.Union[typing.Iterable[archivebox.index.schema.Link], django.db.models.QuerySet], overwrite: bool = False, methods: typing.Optional[typing.Iterable[str]] = None, out_dir: typing.Optional[pathlib.Path] = None, created_by_id: int | None = None) -> typing.List[archivebox.index.schema.Link]
:canonical: archivebox.extractors.archive_links

```{autodoc2-docstring} archivebox.extractors.archive_links
```
````

````{py:data} EXTRACTORS_DIR
:canonical: archivebox.extractors.EXTRACTORS_DIR
:value: >
   None

```{autodoc2-docstring} archivebox.extractors.EXTRACTORS_DIR
```

````

`````{py:class} ExtractorModuleProtocol
:canonical: archivebox.extractors.ExtractorModuleProtocol

Bases: {py:obj}`typing.Protocol`

```{autodoc2-docstring} archivebox.extractors.ExtractorModuleProtocol
```

````{py:attribute} get_output_path
:canonical: archivebox.extractors.ExtractorModuleProtocol.get_output_path
:type: typing.Callable
:value: >
   None

```{autodoc2-docstring} archivebox.extractors.ExtractorModuleProtocol.get_output_path
```

````

`````

````{py:function} get_extractors(dir: pathlib.Path = EXTRACTORS_DIR) -> typing.Dict[str, archivebox.extractors.ExtractorModuleProtocol]
:canonical: archivebox.extractors.get_extractors

```{autodoc2-docstring} archivebox.extractors.get_extractors
```
````

````{py:data} EXTRACTORS
:canonical: archivebox.extractors.EXTRACTORS
:value: >
   'get_extractors(...)'

```{autodoc2-docstring} archivebox.extractors.EXTRACTORS
```

````
