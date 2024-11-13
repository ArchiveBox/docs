# {py:mod}`abx_plugin_favicon.favicon`

```{py:module} abx_plugin_favicon.favicon
```

```{autodoc2-docstring} abx_plugin_favicon.favicon
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`should_save_favicon <abx_plugin_favicon.favicon.should_save_favicon>`
  - ```{autodoc2-docstring} abx_plugin_favicon.favicon.should_save_favicon
    :summary:
    ```
* - {py:obj}`get_output_path <abx_plugin_favicon.favicon.get_output_path>`
  - ```{autodoc2-docstring} abx_plugin_favicon.favicon.get_output_path
    :summary:
    ```
* - {py:obj}`save_favicon <abx_plugin_favicon.favicon.save_favicon>`
  - ```{autodoc2-docstring} abx_plugin_favicon.favicon.save_favicon
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <abx_plugin_favicon.favicon.__package__>`
  - ```{autodoc2-docstring} abx_plugin_favicon.favicon.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: abx_plugin_favicon.favicon.__package__
:value: >
   'abx_plugin_favicon'

```{autodoc2-docstring} abx_plugin_favicon.favicon.__package__
```

````

````{py:function} should_save_favicon(link: archivebox.index.schema.Link, out_dir: str | pathlib.Path | None = None, overwrite: bool = False) -> bool
:canonical: abx_plugin_favicon.favicon.should_save_favicon

```{autodoc2-docstring} abx_plugin_favicon.favicon.should_save_favicon
```
````

````{py:function} get_output_path()
:canonical: abx_plugin_favicon.favicon.get_output_path

```{autodoc2-docstring} abx_plugin_favicon.favicon.get_output_path
```
````

````{py:function} save_favicon(link: archivebox.index.schema.Link, out_dir: str | pathlib.Path | None = None, timeout: int = CURL_CONFIG.CURL_TIMEOUT) -> archivebox.index.schema.ArchiveResult
:canonical: abx_plugin_favicon.favicon.save_favicon

```{autodoc2-docstring} abx_plugin_favicon.favicon.save_favicon
```
````
