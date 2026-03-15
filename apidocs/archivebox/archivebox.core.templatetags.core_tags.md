# {py:mod}`archivebox.core.templatetags.core_tags`

```{py:module} archivebox.core.templatetags.core_tags
```

```{autodoc2-docstring} archivebox.core.templatetags.core_tags
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_count_media_files <archivebox.core.templatetags.core_tags._count_media_files>`
  - ```{autodoc2-docstring} archivebox.core.templatetags.core_tags._count_media_files
    :summary:
    ```
* - {py:obj}`_list_media_files <archivebox.core.templatetags.core_tags._list_media_files>`
  - ```{autodoc2-docstring} archivebox.core.templatetags.core_tags._list_media_files
    :summary:
    ```
* - {py:obj}`split <archivebox.core.templatetags.core_tags.split>`
  - ```{autodoc2-docstring} archivebox.core.templatetags.core_tags.split
    :summary:
    ```
* - {py:obj}`file_size <archivebox.core.templatetags.core_tags.file_size>`
  - ```{autodoc2-docstring} archivebox.core.templatetags.core_tags.file_size
    :summary:
    ```
* - {py:obj}`result_list <archivebox.core.templatetags.core_tags.result_list>`
  - ```{autodoc2-docstring} archivebox.core.templatetags.core_tags.result_list
    :summary:
    ```
* - {py:obj}`result_list_tag <archivebox.core.templatetags.core_tags.result_list_tag>`
  - ```{autodoc2-docstring} archivebox.core.templatetags.core_tags.result_list_tag
    :summary:
    ```
* - {py:obj}`url_replace <archivebox.core.templatetags.core_tags.url_replace>`
  - ```{autodoc2-docstring} archivebox.core.templatetags.core_tags.url_replace
    :summary:
    ```
* - {py:obj}`admin_base_url <archivebox.core.templatetags.core_tags.admin_base_url>`
  - ```{autodoc2-docstring} archivebox.core.templatetags.core_tags.admin_base_url
    :summary:
    ```
* - {py:obj}`web_base_url <archivebox.core.templatetags.core_tags.web_base_url>`
  - ```{autodoc2-docstring} archivebox.core.templatetags.core_tags.web_base_url
    :summary:
    ```
* - {py:obj}`snapshot_base_url <archivebox.core.templatetags.core_tags.snapshot_base_url>`
  - ```{autodoc2-docstring} archivebox.core.templatetags.core_tags.snapshot_base_url
    :summary:
    ```
* - {py:obj}`snapshot_url <archivebox.core.templatetags.core_tags.snapshot_url>`
  - ```{autodoc2-docstring} archivebox.core.templatetags.core_tags.snapshot_url
    :summary:
    ```
* - {py:obj}`plugin_icon <archivebox.core.templatetags.core_tags.plugin_icon>`
  - ```{autodoc2-docstring} archivebox.core.templatetags.core_tags.plugin_icon
    :summary:
    ```
* - {py:obj}`plugin_card <archivebox.core.templatetags.core_tags.plugin_card>`
  - ```{autodoc2-docstring} archivebox.core.templatetags.core_tags.plugin_card
    :summary:
    ```
* - {py:obj}`plugin_full <archivebox.core.templatetags.core_tags.plugin_full>`
  - ```{autodoc2-docstring} archivebox.core.templatetags.core_tags.plugin_full
    :summary:
    ```
* - {py:obj}`plugin_name <archivebox.core.templatetags.core_tags.plugin_name>`
  - ```{autodoc2-docstring} archivebox.core.templatetags.core_tags.plugin_name
    :summary:
    ```
* - {py:obj}`api_token <archivebox.core.templatetags.core_tags.api_token>`
  - ```{autodoc2-docstring} archivebox.core.templatetags.core_tags.api_token
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`register <archivebox.core.templatetags.core_tags.register>`
  - ```{autodoc2-docstring} archivebox.core.templatetags.core_tags.register
    :summary:
    ```
* - {py:obj}`_MEDIA_FILE_EXTS <archivebox.core.templatetags.core_tags._MEDIA_FILE_EXTS>`
  - ```{autodoc2-docstring} archivebox.core.templatetags.core_tags._MEDIA_FILE_EXTS
    :summary:
    ```
````

### API

````{py:data} register
:canonical: archivebox.core.templatetags.core_tags.register
:value: >
   'Library(...)'

```{autodoc2-docstring} archivebox.core.templatetags.core_tags.register
```

````

````{py:data} _MEDIA_FILE_EXTS
:canonical: archivebox.core.templatetags.core_tags._MEDIA_FILE_EXTS
:value: >
   None

```{autodoc2-docstring} archivebox.core.templatetags.core_tags._MEDIA_FILE_EXTS
```

````

````{py:function} _count_media_files(result) -> int
:canonical: archivebox.core.templatetags.core_tags._count_media_files

```{autodoc2-docstring} archivebox.core.templatetags.core_tags._count_media_files
```
````

````{py:function} _list_media_files(result) -> list[dict]
:canonical: archivebox.core.templatetags.core_tags._list_media_files

```{autodoc2-docstring} archivebox.core.templatetags.core_tags._list_media_files
```
````

````{py:function} split(value, separator: str = ',')
:canonical: archivebox.core.templatetags.core_tags.split

```{autodoc2-docstring} archivebox.core.templatetags.core_tags.split
```
````

````{py:function} file_size(num_bytes: typing.Union[int, float]) -> str
:canonical: archivebox.core.templatetags.core_tags.file_size

```{autodoc2-docstring} archivebox.core.templatetags.core_tags.file_size
```
````

````{py:function} result_list(cl)
:canonical: archivebox.core.templatetags.core_tags.result_list

```{autodoc2-docstring} archivebox.core.templatetags.core_tags.result_list
```
````

````{py:function} result_list_tag(parser, token)
:canonical: archivebox.core.templatetags.core_tags.result_list_tag

```{autodoc2-docstring} archivebox.core.templatetags.core_tags.result_list_tag
```
````

````{py:function} url_replace(context, **kwargs)
:canonical: archivebox.core.templatetags.core_tags.url_replace

```{autodoc2-docstring} archivebox.core.templatetags.core_tags.url_replace
```
````

````{py:function} admin_base_url(context) -> str
:canonical: archivebox.core.templatetags.core_tags.admin_base_url

```{autodoc2-docstring} archivebox.core.templatetags.core_tags.admin_base_url
```
````

````{py:function} web_base_url(context) -> str
:canonical: archivebox.core.templatetags.core_tags.web_base_url

```{autodoc2-docstring} archivebox.core.templatetags.core_tags.web_base_url
```
````

````{py:function} snapshot_base_url(context, snapshot) -> str
:canonical: archivebox.core.templatetags.core_tags.snapshot_base_url

```{autodoc2-docstring} archivebox.core.templatetags.core_tags.snapshot_base_url
```
````

````{py:function} snapshot_url(context, snapshot, path: str = '') -> str
:canonical: archivebox.core.templatetags.core_tags.snapshot_url

```{autodoc2-docstring} archivebox.core.templatetags.core_tags.snapshot_url
```
````

````{py:function} plugin_icon(plugin: str) -> str
:canonical: archivebox.core.templatetags.core_tags.plugin_icon

```{autodoc2-docstring} archivebox.core.templatetags.core_tags.plugin_icon
```
````

````{py:function} plugin_card(context, result) -> str
:canonical: archivebox.core.templatetags.core_tags.plugin_card

```{autodoc2-docstring} archivebox.core.templatetags.core_tags.plugin_card
```
````

````{py:function} plugin_full(context, result) -> str
:canonical: archivebox.core.templatetags.core_tags.plugin_full

```{autodoc2-docstring} archivebox.core.templatetags.core_tags.plugin_full
```
````

````{py:function} plugin_name(value: str) -> str
:canonical: archivebox.core.templatetags.core_tags.plugin_name

```{autodoc2-docstring} archivebox.core.templatetags.core_tags.plugin_name
```
````

````{py:function} api_token(context) -> str
:canonical: archivebox.core.templatetags.core_tags.api_token

```{autodoc2-docstring} archivebox.core.templatetags.core_tags.api_token
```
````
