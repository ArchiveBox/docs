# {py:mod}`archivebox.extractors.mercury`

```{py:module} archivebox.extractors.mercury
```

```{autodoc2-docstring} archivebox.extractors.mercury
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_output_path <archivebox.extractors.mercury.get_output_path>`
  - ```{autodoc2-docstring} archivebox.extractors.mercury.get_output_path
    :summary:
    ```
* - {py:obj}`get_embed_path <archivebox.extractors.mercury.get_embed_path>`
  - ```{autodoc2-docstring} archivebox.extractors.mercury.get_embed_path
    :summary:
    ```
* - {py:obj}`ShellError <archivebox.extractors.mercury.ShellError>`
  - ```{autodoc2-docstring} archivebox.extractors.mercury.ShellError
    :summary:
    ```
* - {py:obj}`should_save_mercury <archivebox.extractors.mercury.should_save_mercury>`
  - ```{autodoc2-docstring} archivebox.extractors.mercury.should_save_mercury
    :summary:
    ```
* - {py:obj}`save_mercury <archivebox.extractors.mercury.save_mercury>`
  - ```{autodoc2-docstring} archivebox.extractors.mercury.save_mercury
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.extractors.mercury.__package__>`
  - ```{autodoc2-docstring} archivebox.extractors.mercury.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.extractors.mercury.__package__
:value: >
   'archivebox.extractors'

```{autodoc2-docstring} archivebox.extractors.mercury.__package__
```

````

````{py:function} get_output_path()
:canonical: archivebox.extractors.mercury.get_output_path

```{autodoc2-docstring} archivebox.extractors.mercury.get_output_path
```
````

````{py:function} get_embed_path(archiveresult=None)
:canonical: archivebox.extractors.mercury.get_embed_path

```{autodoc2-docstring} archivebox.extractors.mercury.get_embed_path
```
````

````{py:function} ShellError(cmd: typing.List[str], result: subprocess.CompletedProcess, lines: int = 20) -> archivebox.index.schema.ArchiveError
:canonical: archivebox.extractors.mercury.ShellError

```{autodoc2-docstring} archivebox.extractors.mercury.ShellError
```
````

````{py:function} should_save_mercury(link: archivebox.index.schema.Link, out_dir: typing.Optional[str] = None, overwrite: typing.Optional[bool] = False) -> bool
:canonical: archivebox.extractors.mercury.should_save_mercury

```{autodoc2-docstring} archivebox.extractors.mercury.should_save_mercury
```
````

````{py:function} save_mercury(link: archivebox.index.schema.Link, out_dir: typing.Optional[pathlib.Path] = None, timeout: int = MERCURY_CONFIG.MERCURY_TIMEOUT) -> archivebox.index.schema.ArchiveResult
:canonical: archivebox.extractors.mercury.save_mercury

```{autodoc2-docstring} archivebox.extractors.mercury.save_mercury
```
````
