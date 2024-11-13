# {py:mod}`abx_plugin_git.git`

```{py:module} abx_plugin_git.git
```

```{autodoc2-docstring} abx_plugin_git.git
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_output_path <abx_plugin_git.git.get_output_path>`
  - ```{autodoc2-docstring} abx_plugin_git.git.get_output_path
    :summary:
    ```
* - {py:obj}`get_embed_path <abx_plugin_git.git.get_embed_path>`
  - ```{autodoc2-docstring} abx_plugin_git.git.get_embed_path
    :summary:
    ```
* - {py:obj}`should_save_git <abx_plugin_git.git.should_save_git>`
  - ```{autodoc2-docstring} abx_plugin_git.git.should_save_git
    :summary:
    ```
* - {py:obj}`save_git <abx_plugin_git.git.save_git>`
  - ```{autodoc2-docstring} abx_plugin_git.git.save_git
    :summary:
    ```
````

### API

````{py:function} get_output_path()
:canonical: abx_plugin_git.git.get_output_path

```{autodoc2-docstring} abx_plugin_git.git.get_output_path
```
````

````{py:function} get_embed_path(archiveresult=None)
:canonical: abx_plugin_git.git.get_embed_path

```{autodoc2-docstring} abx_plugin_git.git.get_embed_path
```
````

````{py:function} should_save_git(link: archivebox.index.schema.Link, out_dir: typing.Optional[pathlib.Path] = None, overwrite: typing.Optional[bool] = False) -> bool
:canonical: abx_plugin_git.git.should_save_git

```{autodoc2-docstring} abx_plugin_git.git.should_save_git
```
````

````{py:function} save_git(link: archivebox.index.schema.Link, out_dir: typing.Optional[pathlib.Path] = None, timeout: int = GIT_CONFIG.GIT_TIMEOUT) -> archivebox.index.schema.ArchiveResult
:canonical: abx_plugin_git.git.save_git

```{autodoc2-docstring} abx_plugin_git.git.save_git
```
````
