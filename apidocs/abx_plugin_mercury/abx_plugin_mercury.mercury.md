# {py:mod}`abx_plugin_mercury.mercury`

```{py:module} abx_plugin_mercury.mercury
```

```{autodoc2-docstring} abx_plugin_mercury.mercury
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_output_path <abx_plugin_mercury.mercury.get_output_path>`
  - ```{autodoc2-docstring} abx_plugin_mercury.mercury.get_output_path
    :summary:
    ```
* - {py:obj}`get_embed_path <abx_plugin_mercury.mercury.get_embed_path>`
  - ```{autodoc2-docstring} abx_plugin_mercury.mercury.get_embed_path
    :summary:
    ```
* - {py:obj}`ShellError <abx_plugin_mercury.mercury.ShellError>`
  - ```{autodoc2-docstring} abx_plugin_mercury.mercury.ShellError
    :summary:
    ```
* - {py:obj}`should_save_mercury <abx_plugin_mercury.mercury.should_save_mercury>`
  - ```{autodoc2-docstring} abx_plugin_mercury.mercury.should_save_mercury
    :summary:
    ```
* - {py:obj}`save_mercury <abx_plugin_mercury.mercury.save_mercury>`
  - ```{autodoc2-docstring} abx_plugin_mercury.mercury.save_mercury
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <abx_plugin_mercury.mercury.__package__>`
  - ```{autodoc2-docstring} abx_plugin_mercury.mercury.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: abx_plugin_mercury.mercury.__package__
:value: >
   'abx_plugin_mercury'

```{autodoc2-docstring} abx_plugin_mercury.mercury.__package__
```

````

````{py:function} get_output_path()
:canonical: abx_plugin_mercury.mercury.get_output_path

```{autodoc2-docstring} abx_plugin_mercury.mercury.get_output_path
```
````

````{py:function} get_embed_path(archiveresult=None)
:canonical: abx_plugin_mercury.mercury.get_embed_path

```{autodoc2-docstring} abx_plugin_mercury.mercury.get_embed_path
```
````

````{py:function} ShellError(cmd: typing.List[str], result: subprocess.CompletedProcess, lines: int = 20) -> archivebox.index.schema.ArchiveError
:canonical: abx_plugin_mercury.mercury.ShellError

```{autodoc2-docstring} abx_plugin_mercury.mercury.ShellError
```
````

````{py:function} should_save_mercury(link: archivebox.index.schema.Link, out_dir: typing.Optional[str] = None, overwrite: typing.Optional[bool] = False) -> bool
:canonical: abx_plugin_mercury.mercury.should_save_mercury

```{autodoc2-docstring} abx_plugin_mercury.mercury.should_save_mercury
```
````

````{py:function} save_mercury(link: archivebox.index.schema.Link, out_dir: typing.Optional[pathlib.Path] = None, timeout: int = MERCURY_CONFIG.MERCURY_TIMEOUT) -> archivebox.index.schema.ArchiveResult
:canonical: abx_plugin_mercury.mercury.save_mercury

```{autodoc2-docstring} abx_plugin_mercury.mercury.save_mercury
```
````
