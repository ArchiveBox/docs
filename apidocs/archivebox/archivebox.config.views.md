# {py:mod}`archivebox.config.views`

```{py:module} archivebox.config.views
```

```{autodoc2-docstring} archivebox.config.views
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`obj_to_yaml <archivebox.config.views.obj_to_yaml>`
  - ```{autodoc2-docstring} archivebox.config.views.obj_to_yaml
    :summary:
    ```
* - {py:obj}`get_detected_binaries <archivebox.config.views.get_detected_binaries>`
  - ```{autodoc2-docstring} archivebox.config.views.get_detected_binaries
    :summary:
    ```
* - {py:obj}`get_filesystem_plugins <archivebox.config.views.get_filesystem_plugins>`
  - ```{autodoc2-docstring} archivebox.config.views.get_filesystem_plugins
    :summary:
    ```
* - {py:obj}`binaries_list_view <archivebox.config.views.binaries_list_view>`
  - ```{autodoc2-docstring} archivebox.config.views.binaries_list_view
    :summary:
    ```
* - {py:obj}`binary_detail_view <archivebox.config.views.binary_detail_view>`
  - ```{autodoc2-docstring} archivebox.config.views.binary_detail_view
    :summary:
    ```
* - {py:obj}`plugins_list_view <archivebox.config.views.plugins_list_view>`
  - ```{autodoc2-docstring} archivebox.config.views.plugins_list_view
    :summary:
    ```
* - {py:obj}`plugin_detail_view <archivebox.config.views.plugin_detail_view>`
  - ```{autodoc2-docstring} archivebox.config.views.plugin_detail_view
    :summary:
    ```
* - {py:obj}`worker_list_view <archivebox.config.views.worker_list_view>`
  - ```{autodoc2-docstring} archivebox.config.views.worker_list_view
    :summary:
    ```
* - {py:obj}`worker_detail_view <archivebox.config.views.worker_detail_view>`
  - ```{autodoc2-docstring} archivebox.config.views.worker_detail_view
    :summary:
    ```
* - {py:obj}`log_list_view <archivebox.config.views.log_list_view>`
  - ```{autodoc2-docstring} archivebox.config.views.log_list_view
    :summary:
    ```
* - {py:obj}`log_detail_view <archivebox.config.views.log_detail_view>`
  - ```{autodoc2-docstring} archivebox.config.views.log_detail_view
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`KNOWN_BINARIES <archivebox.config.views.KNOWN_BINARIES>`
  - ```{autodoc2-docstring} archivebox.config.views.KNOWN_BINARIES
    :summary:
    ```
````

### API

````{py:data} KNOWN_BINARIES
:canonical: archivebox.config.views.KNOWN_BINARIES
:value: >
   ['wget', 'curl', 'chromium', 'chrome', 'google-chrome', 'google-chrome-stable', 'node', 'npm', 'npx'...

```{autodoc2-docstring} archivebox.config.views.KNOWN_BINARIES
```

````

````{py:function} obj_to_yaml(obj: typing.Any, indent: int = 0) -> str
:canonical: archivebox.config.views.obj_to_yaml

```{autodoc2-docstring} archivebox.config.views.obj_to_yaml
```
````

````{py:function} get_detected_binaries() -> typing.Dict[str, typing.Dict[str, typing.Any]]
:canonical: archivebox.config.views.get_detected_binaries

```{autodoc2-docstring} archivebox.config.views.get_detected_binaries
```
````

````{py:function} get_filesystem_plugins() -> typing.Dict[str, typing.Dict[str, typing.Any]]
:canonical: archivebox.config.views.get_filesystem_plugins

```{autodoc2-docstring} archivebox.config.views.get_filesystem_plugins
```
````

````{py:function} binaries_list_view(request: django.http.HttpRequest, **kwargs) -> admin_data_views.typing.TableContext
:canonical: archivebox.config.views.binaries_list_view

```{autodoc2-docstring} archivebox.config.views.binaries_list_view
```
````

````{py:function} binary_detail_view(request: django.http.HttpRequest, key: str, **kwargs) -> admin_data_views.typing.ItemContext
:canonical: archivebox.config.views.binary_detail_view

```{autodoc2-docstring} archivebox.config.views.binary_detail_view
```
````

````{py:function} plugins_list_view(request: django.http.HttpRequest, **kwargs) -> admin_data_views.typing.TableContext
:canonical: archivebox.config.views.plugins_list_view

```{autodoc2-docstring} archivebox.config.views.plugins_list_view
```
````

````{py:function} plugin_detail_view(request: django.http.HttpRequest, key: str, **kwargs) -> admin_data_views.typing.ItemContext
:canonical: archivebox.config.views.plugin_detail_view

```{autodoc2-docstring} archivebox.config.views.plugin_detail_view
```
````

````{py:function} worker_list_view(request: django.http.HttpRequest, **kwargs) -> admin_data_views.typing.TableContext
:canonical: archivebox.config.views.worker_list_view

```{autodoc2-docstring} archivebox.config.views.worker_list_view
```
````

````{py:function} worker_detail_view(request: django.http.HttpRequest, key: str, **kwargs) -> admin_data_views.typing.ItemContext
:canonical: archivebox.config.views.worker_detail_view

```{autodoc2-docstring} archivebox.config.views.worker_detail_view
```
````

````{py:function} log_list_view(request: django.http.HttpRequest, **kwargs) -> admin_data_views.typing.TableContext
:canonical: archivebox.config.views.log_list_view

```{autodoc2-docstring} archivebox.config.views.log_list_view
```
````

````{py:function} log_detail_view(request: django.http.HttpRequest, key: str, **kwargs) -> admin_data_views.typing.ItemContext
:canonical: archivebox.config.views.log_detail_view

```{autodoc2-docstring} archivebox.config.views.log_detail_view
```
````
