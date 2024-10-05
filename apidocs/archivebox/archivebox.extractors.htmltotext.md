# {py:mod}`archivebox.extractors.htmltotext`

```{py:module} archivebox.extractors.htmltotext
```

```{autodoc2-docstring} archivebox.extractors.htmltotext
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`HTMLTextExtractor <archivebox.extractors.htmltotext.HTMLTextExtractor>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_output_path <archivebox.extractors.htmltotext.get_output_path>`
  - ```{autodoc2-docstring} archivebox.extractors.htmltotext.get_output_path
    :summary:
    ```
* - {py:obj}`should_save_htmltotext <archivebox.extractors.htmltotext.should_save_htmltotext>`
  - ```{autodoc2-docstring} archivebox.extractors.htmltotext.should_save_htmltotext
    :summary:
    ```
* - {py:obj}`save_htmltotext <archivebox.extractors.htmltotext.save_htmltotext>`
  - ```{autodoc2-docstring} archivebox.extractors.htmltotext.save_htmltotext
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.extractors.htmltotext.__package__>`
  - ```{autodoc2-docstring} archivebox.extractors.htmltotext.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.extractors.htmltotext.__package__
:value: >
   'archivebox.extractors'

```{autodoc2-docstring} archivebox.extractors.htmltotext.__package__
```

````

````{py:function} get_output_path()
:canonical: archivebox.extractors.htmltotext.get_output_path

```{autodoc2-docstring} archivebox.extractors.htmltotext.get_output_path
```
````

`````{py:class} HTMLTextExtractor()
:canonical: archivebox.extractors.htmltotext.HTMLTextExtractor

Bases: {py:obj}`html.parser.HTMLParser`

````{py:attribute} TEXT_ATTRS
:canonical: archivebox.extractors.htmltotext.HTMLTextExtractor.TEXT_ATTRS
:value: >
   ['alt', 'cite', 'href', 'label', 'list', 'placeholder', 'title', 'value']

```{autodoc2-docstring} archivebox.extractors.htmltotext.HTMLTextExtractor.TEXT_ATTRS
```

````

````{py:attribute} NOTEXT_TAGS
:canonical: archivebox.extractors.htmltotext.HTMLTextExtractor.NOTEXT_TAGS
:value: >
   ['script', 'style', 'template']

```{autodoc2-docstring} archivebox.extractors.htmltotext.HTMLTextExtractor.NOTEXT_TAGS
```

````

````{py:attribute} NOTEXT_HREF
:canonical: archivebox.extractors.htmltotext.HTMLTextExtractor.NOTEXT_HREF
:value: >
   ['data:', 'javascript:', '#']

```{autodoc2-docstring} archivebox.extractors.htmltotext.HTMLTextExtractor.NOTEXT_HREF
```

````

````{py:method} _is_text_attr(name, value)
:canonical: archivebox.extractors.htmltotext.HTMLTextExtractor._is_text_attr

```{autodoc2-docstring} archivebox.extractors.htmltotext.HTMLTextExtractor._is_text_attr
```

````

````{py:method} _parent_tag()
:canonical: archivebox.extractors.htmltotext.HTMLTextExtractor._parent_tag

```{autodoc2-docstring} archivebox.extractors.htmltotext.HTMLTextExtractor._parent_tag
```

````

````{py:method} _in_notext_tag()
:canonical: archivebox.extractors.htmltotext.HTMLTextExtractor._in_notext_tag

```{autodoc2-docstring} archivebox.extractors.htmltotext.HTMLTextExtractor._in_notext_tag
```

````

````{py:method} handle_starttag(tag, attrs)
:canonical: archivebox.extractors.htmltotext.HTMLTextExtractor.handle_starttag

```{autodoc2-docstring} archivebox.extractors.htmltotext.HTMLTextExtractor.handle_starttag
```

````

````{py:method} handle_endtag(tag)
:canonical: archivebox.extractors.htmltotext.HTMLTextExtractor.handle_endtag

```{autodoc2-docstring} archivebox.extractors.htmltotext.HTMLTextExtractor.handle_endtag
```

````

````{py:method} handle_data(data)
:canonical: archivebox.extractors.htmltotext.HTMLTextExtractor.handle_data

```{autodoc2-docstring} archivebox.extractors.htmltotext.HTMLTextExtractor.handle_data
```

````

````{py:method} __str__()
:canonical: archivebox.extractors.htmltotext.HTMLTextExtractor.__str__

````

`````

````{py:function} should_save_htmltotext(link: archivebox.index.schema.Link, out_dir: typing.Optional[pathlib.Path] = None, overwrite: typing.Optional[bool] = False) -> bool
:canonical: archivebox.extractors.htmltotext.should_save_htmltotext

```{autodoc2-docstring} archivebox.extractors.htmltotext.should_save_htmltotext
```
````

````{py:function} save_htmltotext(link: archivebox.index.schema.Link, out_dir: typing.Optional[pathlib.Path] = None, timeout: int = ARCHIVING_CONFIG.TIMEOUT) -> archivebox.index.schema.ArchiveResult
:canonical: archivebox.extractors.htmltotext.save_htmltotext

```{autodoc2-docstring} archivebox.extractors.htmltotext.save_htmltotext
```
````
