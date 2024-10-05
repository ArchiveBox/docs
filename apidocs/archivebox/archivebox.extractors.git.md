# {py:mod}`archivebox.extractors.git`

```{py:module} archivebox.extractors.git
```

```{autodoc2-docstring} archivebox.extractors.git
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_output_path <archivebox.extractors.git.get_output_path>`
  - ```{autodoc2-docstring} archivebox.extractors.git.get_output_path
    :summary:
    ```
* - {py:obj}`get_embed_path <archivebox.extractors.git.get_embed_path>`
  - ```{autodoc2-docstring} archivebox.extractors.git.get_embed_path
    :summary:
    ```
* - {py:obj}`should_save_git <archivebox.extractors.git.should_save_git>`
  - ```{autodoc2-docstring} archivebox.extractors.git.should_save_git
    :summary:
    ```
* - {py:obj}`save_git <archivebox.extractors.git.save_git>`
  - ```{autodoc2-docstring} archivebox.extractors.git.save_git
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.extractors.git.__package__>`
  - ```{autodoc2-docstring} archivebox.extractors.git.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.extractors.git.__package__
:value: >
   'archivebox.extractors'

```{autodoc2-docstring} archivebox.extractors.git.__package__
```

````

````{py:function} get_output_path()
:canonical: archivebox.extractors.git.get_output_path

```{autodoc2-docstring} archivebox.extractors.git.get_output_path
```
````

````{py:function} get_embed_path(archiveresult=None)
:canonical: archivebox.extractors.git.get_embed_path

```{autodoc2-docstring} archivebox.extractors.git.get_embed_path
```
````

````{py:function} should_save_git(link: archivebox.index.schema.Link, out_dir: typing.Optional[pathlib.Path] = None, overwrite: typing.Optional[bool] = False) -> bool
:canonical: archivebox.extractors.git.should_save_git

```{autodoc2-docstring} archivebox.extractors.git.should_save_git
```
````

````{py:function} save_git(link: archivebox.index.schema.Link, out_dir: typing.Optional[pathlib.Path] = None, timeout: int = GIT_CONFIG.GIT_TIMEOUT) -> archivebox.index.schema.ArchiveResult
:canonical: archivebox.extractors.git.save_git

```{autodoc2-docstring} archivebox.extractors.git.save_git
```
````
