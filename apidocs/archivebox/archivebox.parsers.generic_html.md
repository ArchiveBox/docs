# {py:mod}`archivebox.parsers.generic_html`

```{py:module} archivebox.parsers.generic_html
```

```{autodoc2-docstring} archivebox.parsers.generic_html
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`HrefParser <archivebox.parsers.generic_html.HrefParser>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`parse_generic_html_export <archivebox.parsers.generic_html.parse_generic_html_export>`
  - ```{autodoc2-docstring} archivebox.parsers.generic_html.parse_generic_html_export
    :summary:
    ```
* - {py:obj}`did_urljoin_misbehave <archivebox.parsers.generic_html.did_urljoin_misbehave>`
  - ```{autodoc2-docstring} archivebox.parsers.generic_html.did_urljoin_misbehave
    :summary:
    ```
* - {py:obj}`fix_urljoin_bug <archivebox.parsers.generic_html.fix_urljoin_bug>`
  - ```{autodoc2-docstring} archivebox.parsers.generic_html.fix_urljoin_bug
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.parsers.generic_html.__package__>`
  - ```{autodoc2-docstring} archivebox.parsers.generic_html.__package__
    :summary:
    ```
* - {py:obj}`KEY <archivebox.parsers.generic_html.KEY>`
  - ```{autodoc2-docstring} archivebox.parsers.generic_html.KEY
    :summary:
    ```
* - {py:obj}`NAME <archivebox.parsers.generic_html.NAME>`
  - ```{autodoc2-docstring} archivebox.parsers.generic_html.NAME
    :summary:
    ```
* - {py:obj}`PARSER <archivebox.parsers.generic_html.PARSER>`
  - ```{autodoc2-docstring} archivebox.parsers.generic_html.PARSER
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.parsers.generic_html.__package__
:value: >
   'archivebox.parsers'

```{autodoc2-docstring} archivebox.parsers.generic_html.__package__
```

````

`````{py:class} HrefParser()
:canonical: archivebox.parsers.generic_html.HrefParser

Bases: {py:obj}`html.parser.HTMLParser`

````{py:method} handle_starttag(tag, attrs)
:canonical: archivebox.parsers.generic_html.HrefParser.handle_starttag

```{autodoc2-docstring} archivebox.parsers.generic_html.HrefParser.handle_starttag
```

````

`````

````{py:function} parse_generic_html_export(html_file: typing.IO[str], root_url: typing.Optional[str] = None, **_kwargs) -> typing.Iterable[archivebox.index.schema.Link]
:canonical: archivebox.parsers.generic_html.parse_generic_html_export

```{autodoc2-docstring} archivebox.parsers.generic_html.parse_generic_html_export
```
````

````{py:data} KEY
:canonical: archivebox.parsers.generic_html.KEY
:value: >
   'html'

```{autodoc2-docstring} archivebox.parsers.generic_html.KEY
```

````

````{py:data} NAME
:canonical: archivebox.parsers.generic_html.NAME
:value: >
   'Generic HTML'

```{autodoc2-docstring} archivebox.parsers.generic_html.NAME
```

````

````{py:data} PARSER
:canonical: archivebox.parsers.generic_html.PARSER
:value: >
   None

```{autodoc2-docstring} archivebox.parsers.generic_html.PARSER
```

````

````{py:function} did_urljoin_misbehave(root_url: str, relative_path: str, final_url: str) -> bool
:canonical: archivebox.parsers.generic_html.did_urljoin_misbehave

```{autodoc2-docstring} archivebox.parsers.generic_html.did_urljoin_misbehave
```
````

````{py:function} fix_urljoin_bug(url: str, nesting_limit=5)
:canonical: archivebox.parsers.generic_html.fix_urljoin_bug

```{autodoc2-docstring} archivebox.parsers.generic_html.fix_urljoin_bug
```
````
