# {py:mod}`abx_plugin_ytdlp.media`

```{py:module} abx_plugin_ytdlp.media
```

```{autodoc2-docstring} abx_plugin_ytdlp.media
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_output_path <abx_plugin_ytdlp.media.get_output_path>`
  - ```{autodoc2-docstring} abx_plugin_ytdlp.media.get_output_path
    :summary:
    ```
* - {py:obj}`get_embed_path <abx_plugin_ytdlp.media.get_embed_path>`
  - ```{autodoc2-docstring} abx_plugin_ytdlp.media.get_embed_path
    :summary:
    ```
* - {py:obj}`should_save_media <abx_plugin_ytdlp.media.should_save_media>`
  - ```{autodoc2-docstring} abx_plugin_ytdlp.media.should_save_media
    :summary:
    ```
* - {py:obj}`save_media <abx_plugin_ytdlp.media.save_media>`
  - ```{autodoc2-docstring} abx_plugin_ytdlp.media.save_media
    :summary:
    ```
````

### API

````{py:function} get_output_path()
:canonical: abx_plugin_ytdlp.media.get_output_path

```{autodoc2-docstring} abx_plugin_ytdlp.media.get_output_path
```
````

````{py:function} get_embed_path(archiveresult=None)
:canonical: abx_plugin_ytdlp.media.get_embed_path

```{autodoc2-docstring} abx_plugin_ytdlp.media.get_embed_path
```
````

````{py:function} should_save_media(link: archivebox.index.schema.Link, out_dir: typing.Optional[pathlib.Path] = None, overwrite: typing.Optional[bool] = False) -> bool
:canonical: abx_plugin_ytdlp.media.should_save_media

```{autodoc2-docstring} abx_plugin_ytdlp.media.should_save_media
```
````

````{py:function} save_media(link: archivebox.index.schema.Link, out_dir: typing.Optional[pathlib.Path] = None, timeout: int = 0) -> archivebox.index.schema.ArchiveResult
:canonical: abx_plugin_ytdlp.media.save_media

```{autodoc2-docstring} abx_plugin_ytdlp.media.save_media
```
````
