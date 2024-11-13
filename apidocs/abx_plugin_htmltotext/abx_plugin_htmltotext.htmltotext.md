# {py:mod}`abx_plugin_htmltotext.htmltotext`

```{py:module} abx_plugin_htmltotext.htmltotext
```

```{autodoc2-docstring} abx_plugin_htmltotext.htmltotext
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`HTMLTextExtractor <abx_plugin_htmltotext.htmltotext.HTMLTextExtractor>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_output_path <abx_plugin_htmltotext.htmltotext.get_output_path>`
  - ```{autodoc2-docstring} abx_plugin_htmltotext.htmltotext.get_output_path
    :summary:
    ```
* - {py:obj}`should_save_htmltotext <abx_plugin_htmltotext.htmltotext.should_save_htmltotext>`
  - ```{autodoc2-docstring} abx_plugin_htmltotext.htmltotext.should_save_htmltotext
    :summary:
    ```
* - {py:obj}`save_htmltotext <abx_plugin_htmltotext.htmltotext.save_htmltotext>`
  - ```{autodoc2-docstring} abx_plugin_htmltotext.htmltotext.save_htmltotext
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <abx_plugin_htmltotext.htmltotext.__package__>`
  - ```{autodoc2-docstring} abx_plugin_htmltotext.htmltotext.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: abx_plugin_htmltotext.htmltotext.__package__
:value: >
   'abx_plugin_htmltotext'

```{autodoc2-docstring} abx_plugin_htmltotext.htmltotext.__package__
```

````

````{py:function} get_output_path()
:canonical: abx_plugin_htmltotext.htmltotext.get_output_path

```{autodoc2-docstring} abx_plugin_htmltotext.htmltotext.get_output_path
```
````

`````{py:class} HTMLTextExtractor()
:canonical: abx_plugin_htmltotext.htmltotext.HTMLTextExtractor

Bases: {py:obj}`html.parser.HTMLParser`

````{py:attribute} TEXT_ATTRS
:canonical: abx_plugin_htmltotext.htmltotext.HTMLTextExtractor.TEXT_ATTRS
:value: >
   ['alt', 'cite', 'href', 'label', 'list', 'placeholder', 'title', 'value']

```{autodoc2-docstring} abx_plugin_htmltotext.htmltotext.HTMLTextExtractor.TEXT_ATTRS
```

````

````{py:attribute} NOTEXT_TAGS
:canonical: abx_plugin_htmltotext.htmltotext.HTMLTextExtractor.NOTEXT_TAGS
:value: >
   ['script', 'style', 'template']

```{autodoc2-docstring} abx_plugin_htmltotext.htmltotext.HTMLTextExtractor.NOTEXT_TAGS
```

````

````{py:attribute} NOTEXT_HREF
:canonical: abx_plugin_htmltotext.htmltotext.HTMLTextExtractor.NOTEXT_HREF
:value: >
   ['data:', 'javascript:', '#']

```{autodoc2-docstring} abx_plugin_htmltotext.htmltotext.HTMLTextExtractor.NOTEXT_HREF
```

````

````{py:method} _is_text_attr(name, value)
:canonical: abx_plugin_htmltotext.htmltotext.HTMLTextExtractor._is_text_attr

```{autodoc2-docstring} abx_plugin_htmltotext.htmltotext.HTMLTextExtractor._is_text_attr
```

````

````{py:method} _parent_tag()
:canonical: abx_plugin_htmltotext.htmltotext.HTMLTextExtractor._parent_tag

```{autodoc2-docstring} abx_plugin_htmltotext.htmltotext.HTMLTextExtractor._parent_tag
```

````

````{py:method} _in_notext_tag()
:canonical: abx_plugin_htmltotext.htmltotext.HTMLTextExtractor._in_notext_tag

```{autodoc2-docstring} abx_plugin_htmltotext.htmltotext.HTMLTextExtractor._in_notext_tag
```

````

````{py:method} handle_starttag(tag, attrs)
:canonical: abx_plugin_htmltotext.htmltotext.HTMLTextExtractor.handle_starttag

```{autodoc2-docstring} abx_plugin_htmltotext.htmltotext.HTMLTextExtractor.handle_starttag
```

````

````{py:method} handle_endtag(tag)
:canonical: abx_plugin_htmltotext.htmltotext.HTMLTextExtractor.handle_endtag

```{autodoc2-docstring} abx_plugin_htmltotext.htmltotext.HTMLTextExtractor.handle_endtag
```

````

````{py:method} handle_data(data)
:canonical: abx_plugin_htmltotext.htmltotext.HTMLTextExtractor.handle_data

```{autodoc2-docstring} abx_plugin_htmltotext.htmltotext.HTMLTextExtractor.handle_data
```

````

````{py:method} __str__()
:canonical: abx_plugin_htmltotext.htmltotext.HTMLTextExtractor.__str__

````

`````

````{py:function} should_save_htmltotext(link: archivebox.index.schema.Link, out_dir: typing.Optional[pathlib.Path] = None, overwrite: typing.Optional[bool] = False) -> bool
:canonical: abx_plugin_htmltotext.htmltotext.should_save_htmltotext

```{autodoc2-docstring} abx_plugin_htmltotext.htmltotext.should_save_htmltotext
```
````

````{py:function} save_htmltotext(link: archivebox.index.schema.Link, out_dir: typing.Optional[pathlib.Path] = None, timeout: int = ARCHIVING_CONFIG.TIMEOUT) -> archivebox.index.schema.ArchiveResult
:canonical: abx_plugin_htmltotext.htmltotext.save_htmltotext

```{autodoc2-docstring} abx_plugin_htmltotext.htmltotext.save_htmltotext
```
````
