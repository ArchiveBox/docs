# {py:mod}`abx_plugin_title.extractor`

```{py:module} abx_plugin_title.extractor
```

```{autodoc2-docstring} abx_plugin_title.extractor
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TitleParser <abx_plugin_title.extractor.TitleParser>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_html <abx_plugin_title.extractor.get_html>`
  - ```{autodoc2-docstring} abx_plugin_title.extractor.get_html
    :summary:
    ```
* - {py:obj}`get_output_path <abx_plugin_title.extractor.get_output_path>`
  - ```{autodoc2-docstring} abx_plugin_title.extractor.get_output_path
    :summary:
    ```
* - {py:obj}`should_save_title <abx_plugin_title.extractor.should_save_title>`
  - ```{autodoc2-docstring} abx_plugin_title.extractor.should_save_title
    :summary:
    ```
* - {py:obj}`extract_title_with_regex <abx_plugin_title.extractor.extract_title_with_regex>`
  - ```{autodoc2-docstring} abx_plugin_title.extractor.extract_title_with_regex
    :summary:
    ```
* - {py:obj}`save_title <abx_plugin_title.extractor.save_title>`
  - ```{autodoc2-docstring} abx_plugin_title.extractor.save_title
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`HTML_TITLE_REGEX <abx_plugin_title.extractor.HTML_TITLE_REGEX>`
  - ```{autodoc2-docstring} abx_plugin_title.extractor.HTML_TITLE_REGEX
    :summary:
    ```
````

### API

````{py:data} HTML_TITLE_REGEX
:canonical: abx_plugin_title.extractor.HTML_TITLE_REGEX
:value: >
   'compile(...)'

```{autodoc2-docstring} abx_plugin_title.extractor.HTML_TITLE_REGEX
```

````

`````{py:class} TitleParser(*args, **kwargs)
:canonical: abx_plugin_title.extractor.TitleParser

Bases: {py:obj}`html.parser.HTMLParser`

````{py:property} title
:canonical: abx_plugin_title.extractor.TitleParser.title

```{autodoc2-docstring} abx_plugin_title.extractor.TitleParser.title
```

````

````{py:method} handle_starttag(tag, attrs)
:canonical: abx_plugin_title.extractor.TitleParser.handle_starttag

```{autodoc2-docstring} abx_plugin_title.extractor.TitleParser.handle_starttag
```

````

````{py:method} handle_data(data)
:canonical: abx_plugin_title.extractor.TitleParser.handle_data

```{autodoc2-docstring} abx_plugin_title.extractor.TitleParser.handle_data
```

````

````{py:method} handle_endtag(tag)
:canonical: abx_plugin_title.extractor.TitleParser.handle_endtag

```{autodoc2-docstring} abx_plugin_title.extractor.TitleParser.handle_endtag
```

````

`````

````{py:function} get_html(link: archivebox.index.schema.Link, path: pathlib.Path, timeout: int = CURL_CONFIG.CURL_TIMEOUT) -> str
:canonical: abx_plugin_title.extractor.get_html

```{autodoc2-docstring} abx_plugin_title.extractor.get_html
```
````

````{py:function} get_output_path()
:canonical: abx_plugin_title.extractor.get_output_path

```{autodoc2-docstring} abx_plugin_title.extractor.get_output_path
```
````

````{py:function} should_save_title(link: archivebox.index.schema.Link, out_dir: typing.Optional[str] = None, overwrite: typing.Optional[bool] = False) -> bool
:canonical: abx_plugin_title.extractor.should_save_title

```{autodoc2-docstring} abx_plugin_title.extractor.should_save_title
```
````

````{py:function} extract_title_with_regex(html)
:canonical: abx_plugin_title.extractor.extract_title_with_regex

```{autodoc2-docstring} abx_plugin_title.extractor.extract_title_with_regex
```
````

````{py:function} save_title(link: archivebox.index.schema.Link, out_dir: typing.Optional[pathlib.Path] = None, timeout: int = CURL_CONFIG.CURL_TIMEOUT) -> archivebox.index.schema.ArchiveResult
:canonical: abx_plugin_title.extractor.save_title

```{autodoc2-docstring} abx_plugin_title.extractor.save_title
```
````
