# {py:mod}`archivebox.extractors.wget`

```{py:module} archivebox.extractors.wget
```

```{autodoc2-docstring} archivebox.extractors.wget
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_output_path <archivebox.extractors.wget.get_output_path>`
  - ```{autodoc2-docstring} archivebox.extractors.wget.get_output_path
    :summary:
    ```
* - {py:obj}`get_embed_path <archivebox.extractors.wget.get_embed_path>`
  - ```{autodoc2-docstring} archivebox.extractors.wget.get_embed_path
    :summary:
    ```
* - {py:obj}`should_save_wget <archivebox.extractors.wget.should_save_wget>`
  - ```{autodoc2-docstring} archivebox.extractors.wget.should_save_wget
    :summary:
    ```
* - {py:obj}`save_wget <archivebox.extractors.wget.save_wget>`
  - ```{autodoc2-docstring} archivebox.extractors.wget.save_wget
    :summary:
    ```
* - {py:obj}`unsafe_wget_output_path <archivebox.extractors.wget.unsafe_wget_output_path>`
  - ```{autodoc2-docstring} archivebox.extractors.wget.unsafe_wget_output_path
    :summary:
    ```
* - {py:obj}`wget_output_path <archivebox.extractors.wget.wget_output_path>`
  - ```{autodoc2-docstring} archivebox.extractors.wget.wget_output_path
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.extractors.wget.__package__>`
  - ```{autodoc2-docstring} archivebox.extractors.wget.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.extractors.wget.__package__
:value: >
   'archivebox.extractors'

```{autodoc2-docstring} archivebox.extractors.wget.__package__
```

````

````{py:function} get_output_path()
:canonical: archivebox.extractors.wget.get_output_path

```{autodoc2-docstring} archivebox.extractors.wget.get_output_path
```
````

````{py:function} get_embed_path(archiveresult=None)
:canonical: archivebox.extractors.wget.get_embed_path

```{autodoc2-docstring} archivebox.extractors.wget.get_embed_path
```
````

````{py:function} should_save_wget(link: archivebox.index.schema.Link, out_dir: typing.Optional[pathlib.Path] = None, overwrite: typing.Optional[bool] = False) -> bool
:canonical: archivebox.extractors.wget.should_save_wget

```{autodoc2-docstring} archivebox.extractors.wget.should_save_wget
```
````

````{py:function} save_wget(link: archivebox.index.schema.Link, out_dir: typing.Optional[pathlib.Path] = None, timeout: int = WGET_CONFIG.WGET_TIMEOUT) -> archivebox.index.schema.ArchiveResult
:canonical: archivebox.extractors.wget.save_wget

```{autodoc2-docstring} archivebox.extractors.wget.save_wget
```
````

````{py:function} unsafe_wget_output_path(link: archivebox.index.schema.Link) -> typing.Optional[str]
:canonical: archivebox.extractors.wget.unsafe_wget_output_path

```{autodoc2-docstring} archivebox.extractors.wget.unsafe_wget_output_path
```
````

````{py:function} wget_output_path(link: archivebox.index.schema.Link, nocache: bool = False) -> typing.Optional[str]
:canonical: archivebox.extractors.wget.wget_output_path

```{autodoc2-docstring} archivebox.extractors.wget.wget_output_path
```
````
