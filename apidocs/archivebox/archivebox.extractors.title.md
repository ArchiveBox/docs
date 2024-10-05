# {py:mod}`archivebox.extractors.title`

```{py:module} archivebox.extractors.title
```

```{autodoc2-docstring} archivebox.extractors.title
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TitleParser <archivebox.extractors.title.TitleParser>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_html <archivebox.extractors.title.get_html>`
  - ```{autodoc2-docstring} archivebox.extractors.title.get_html
    :summary:
    ```
* - {py:obj}`get_output_path <archivebox.extractors.title.get_output_path>`
  - ```{autodoc2-docstring} archivebox.extractors.title.get_output_path
    :summary:
    ```
* - {py:obj}`should_save_title <archivebox.extractors.title.should_save_title>`
  - ```{autodoc2-docstring} archivebox.extractors.title.should_save_title
    :summary:
    ```
* - {py:obj}`extract_title_with_regex <archivebox.extractors.title.extract_title_with_regex>`
  - ```{autodoc2-docstring} archivebox.extractors.title.extract_title_with_regex
    :summary:
    ```
* - {py:obj}`save_title <archivebox.extractors.title.save_title>`
  - ```{autodoc2-docstring} archivebox.extractors.title.save_title
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.extractors.title.__package__>`
  - ```{autodoc2-docstring} archivebox.extractors.title.__package__
    :summary:
    ```
* - {py:obj}`HTML_TITLE_REGEX <archivebox.extractors.title.HTML_TITLE_REGEX>`
  - ```{autodoc2-docstring} archivebox.extractors.title.HTML_TITLE_REGEX
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.extractors.title.__package__
:value: >
   'archivebox.extractors'

```{autodoc2-docstring} archivebox.extractors.title.__package__
```

````

````{py:data} HTML_TITLE_REGEX
:canonical: archivebox.extractors.title.HTML_TITLE_REGEX
:value: >
   'compile(...)'

```{autodoc2-docstring} archivebox.extractors.title.HTML_TITLE_REGEX
```

````

`````{py:class} TitleParser(*args, **kwargs)
:canonical: archivebox.extractors.title.TitleParser

Bases: {py:obj}`html.parser.HTMLParser`

````{py:property} title
:canonical: archivebox.extractors.title.TitleParser.title

```{autodoc2-docstring} archivebox.extractors.title.TitleParser.title
```

````

````{py:method} handle_starttag(tag, attrs)
:canonical: archivebox.extractors.title.TitleParser.handle_starttag

```{autodoc2-docstring} archivebox.extractors.title.TitleParser.handle_starttag
```

````

````{py:method} handle_data(data)
:canonical: archivebox.extractors.title.TitleParser.handle_data

```{autodoc2-docstring} archivebox.extractors.title.TitleParser.handle_data
```

````

````{py:method} handle_endtag(tag)
:canonical: archivebox.extractors.title.TitleParser.handle_endtag

```{autodoc2-docstring} archivebox.extractors.title.TitleParser.handle_endtag
```

````

`````

````{py:function} get_html(link: archivebox.index.schema.Link, path: pathlib.Path, timeout: int = CURL_CONFIG.CURL_TIMEOUT) -> str
:canonical: archivebox.extractors.title.get_html

```{autodoc2-docstring} archivebox.extractors.title.get_html
```
````

````{py:function} get_output_path()
:canonical: archivebox.extractors.title.get_output_path

```{autodoc2-docstring} archivebox.extractors.title.get_output_path
```
````

````{py:function} should_save_title(link: archivebox.index.schema.Link, out_dir: typing.Optional[str] = None, overwrite: typing.Optional[bool] = False) -> bool
:canonical: archivebox.extractors.title.should_save_title

```{autodoc2-docstring} archivebox.extractors.title.should_save_title
```
````

````{py:function} extract_title_with_regex(html)
:canonical: archivebox.extractors.title.extract_title_with_regex

```{autodoc2-docstring} archivebox.extractors.title.extract_title_with_regex
```
````

````{py:function} save_title(link: archivebox.index.schema.Link, out_dir: typing.Optional[pathlib.Path] = None, timeout: int = CURL_CONFIG.CURL_TIMEOUT) -> archivebox.index.schema.ArchiveResult
:canonical: archivebox.extractors.title.save_title

```{autodoc2-docstring} archivebox.extractors.title.save_title
```
````
