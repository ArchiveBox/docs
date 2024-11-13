# {py:mod}`abx_plugin_curl.headers`

```{py:module} abx_plugin_curl.headers
```

```{autodoc2-docstring} abx_plugin_curl.headers
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_output_path <abx_plugin_curl.headers.get_output_path>`
  - ```{autodoc2-docstring} abx_plugin_curl.headers.get_output_path
    :summary:
    ```
* - {py:obj}`should_save_headers <abx_plugin_curl.headers.should_save_headers>`
  - ```{autodoc2-docstring} abx_plugin_curl.headers.should_save_headers
    :summary:
    ```
* - {py:obj}`save_headers <abx_plugin_curl.headers.save_headers>`
  - ```{autodoc2-docstring} abx_plugin_curl.headers.save_headers
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <abx_plugin_curl.headers.__package__>`
  - ```{autodoc2-docstring} abx_plugin_curl.headers.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: abx_plugin_curl.headers.__package__
:value: >
   'abx_plugin_curl'

```{autodoc2-docstring} abx_plugin_curl.headers.__package__
```

````

````{py:function} get_output_path()
:canonical: abx_plugin_curl.headers.get_output_path

```{autodoc2-docstring} abx_plugin_curl.headers.get_output_path
```
````

````{py:function} should_save_headers(link: archivebox.index.schema.Link, out_dir: typing.Optional[str] = None, overwrite: typing.Optional[bool] = False) -> bool
:canonical: abx_plugin_curl.headers.should_save_headers

```{autodoc2-docstring} abx_plugin_curl.headers.should_save_headers
```
````

````{py:function} save_headers(link: archivebox.index.schema.Link, out_dir: typing.Optional[str] = None, timeout: int = CURL_CONFIG.CURL_TIMEOUT) -> archivebox.index.schema.ArchiveResult
:canonical: abx_plugin_curl.headers.save_headers

```{autodoc2-docstring} abx_plugin_curl.headers.save_headers
```
````
