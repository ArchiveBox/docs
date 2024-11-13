# {py:mod}`abx_plugin_wget.wget`

```{py:module} abx_plugin_wget.wget
```

```{autodoc2-docstring} abx_plugin_wget.wget
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_output_path <abx_plugin_wget.wget.get_output_path>`
  - ```{autodoc2-docstring} abx_plugin_wget.wget.get_output_path
    :summary:
    ```
* - {py:obj}`get_embed_path <abx_plugin_wget.wget.get_embed_path>`
  - ```{autodoc2-docstring} abx_plugin_wget.wget.get_embed_path
    :summary:
    ```
* - {py:obj}`should_save_wget <abx_plugin_wget.wget.should_save_wget>`
  - ```{autodoc2-docstring} abx_plugin_wget.wget.should_save_wget
    :summary:
    ```
* - {py:obj}`save_wget <abx_plugin_wget.wget.save_wget>`
  - ```{autodoc2-docstring} abx_plugin_wget.wget.save_wget
    :summary:
    ```
* - {py:obj}`unsafe_wget_output_path <abx_plugin_wget.wget.unsafe_wget_output_path>`
  - ```{autodoc2-docstring} abx_plugin_wget.wget.unsafe_wget_output_path
    :summary:
    ```
* - {py:obj}`wget_output_path <abx_plugin_wget.wget.wget_output_path>`
  - ```{autodoc2-docstring} abx_plugin_wget.wget.wget_output_path
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <abx_plugin_wget.wget.__package__>`
  - ```{autodoc2-docstring} abx_plugin_wget.wget.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: abx_plugin_wget.wget.__package__
:value: >
   'abx_plugin_wget'

```{autodoc2-docstring} abx_plugin_wget.wget.__package__
```

````

````{py:function} get_output_path()
:canonical: abx_plugin_wget.wget.get_output_path

```{autodoc2-docstring} abx_plugin_wget.wget.get_output_path
```
````

````{py:function} get_embed_path(archiveresult=None)
:canonical: abx_plugin_wget.wget.get_embed_path

```{autodoc2-docstring} abx_plugin_wget.wget.get_embed_path
```
````

````{py:function} should_save_wget(link: archivebox.index.schema.Link, out_dir: typing.Optional[pathlib.Path] = None, overwrite: typing.Optional[bool] = False) -> bool
:canonical: abx_plugin_wget.wget.should_save_wget

```{autodoc2-docstring} abx_plugin_wget.wget.should_save_wget
```
````

````{py:function} save_wget(link: archivebox.index.schema.Link, out_dir: typing.Optional[pathlib.Path] = None, timeout: int = WGET_CONFIG.WGET_TIMEOUT) -> archivebox.index.schema.ArchiveResult
:canonical: abx_plugin_wget.wget.save_wget

```{autodoc2-docstring} abx_plugin_wget.wget.save_wget
```
````

````{py:function} unsafe_wget_output_path(link: archivebox.index.schema.Link) -> typing.Optional[str]
:canonical: abx_plugin_wget.wget.unsafe_wget_output_path

```{autodoc2-docstring} abx_plugin_wget.wget.unsafe_wget_output_path
```
````

````{py:function} wget_output_path(link: archivebox.index.schema.Link, nocache: bool = False) -> typing.Optional[str]
:canonical: abx_plugin_wget.wget.wget_output_path

```{autodoc2-docstring} abx_plugin_wget.wget.wget_output_path
```
````
