# {py:mod}`archivebox.parsers.pocket_api`

```{py:module} archivebox.parsers.pocket_api
```

```{autodoc2-docstring} archivebox.parsers.pocket_api
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_pocket_articles <archivebox.parsers.pocket_api.get_pocket_articles>`
  - ```{autodoc2-docstring} archivebox.parsers.pocket_api.get_pocket_articles
    :summary:
    ```
* - {py:obj}`link_from_article <archivebox.parsers.pocket_api.link_from_article>`
  - ```{autodoc2-docstring} archivebox.parsers.pocket_api.link_from_article
    :summary:
    ```
* - {py:obj}`write_since <archivebox.parsers.pocket_api.write_since>`
  - ```{autodoc2-docstring} archivebox.parsers.pocket_api.write_since
    :summary:
    ```
* - {py:obj}`read_since <archivebox.parsers.pocket_api.read_since>`
  - ```{autodoc2-docstring} archivebox.parsers.pocket_api.read_since
    :summary:
    ```
* - {py:obj}`should_parse_as_pocket_api <archivebox.parsers.pocket_api.should_parse_as_pocket_api>`
  - ```{autodoc2-docstring} archivebox.parsers.pocket_api.should_parse_as_pocket_api
    :summary:
    ```
* - {py:obj}`parse_pocket_api_export <archivebox.parsers.pocket_api.parse_pocket_api_export>`
  - ```{autodoc2-docstring} archivebox.parsers.pocket_api.parse_pocket_api_export
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.parsers.pocket_api.__package__>`
  - ```{autodoc2-docstring} archivebox.parsers.pocket_api.__package__
    :summary:
    ```
* - {py:obj}`COUNT_PER_PAGE <archivebox.parsers.pocket_api.COUNT_PER_PAGE>`
  - ```{autodoc2-docstring} archivebox.parsers.pocket_api.COUNT_PER_PAGE
    :summary:
    ```
* - {py:obj}`API_DB_PATH <archivebox.parsers.pocket_api.API_DB_PATH>`
  - ```{autodoc2-docstring} archivebox.parsers.pocket_api.API_DB_PATH
    :summary:
    ```
* - {py:obj}`_BROKEN_PROTOCOL_RE <archivebox.parsers.pocket_api._BROKEN_PROTOCOL_RE>`
  - ```{autodoc2-docstring} archivebox.parsers.pocket_api._BROKEN_PROTOCOL_RE
    :summary:
    ```
* - {py:obj}`KEY <archivebox.parsers.pocket_api.KEY>`
  - ```{autodoc2-docstring} archivebox.parsers.pocket_api.KEY
    :summary:
    ```
* - {py:obj}`NAME <archivebox.parsers.pocket_api.NAME>`
  - ```{autodoc2-docstring} archivebox.parsers.pocket_api.NAME
    :summary:
    ```
* - {py:obj}`PARSER <archivebox.parsers.pocket_api.PARSER>`
  - ```{autodoc2-docstring} archivebox.parsers.pocket_api.PARSER
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.parsers.pocket_api.__package__
:value: >
   'archivebox.parsers'

```{autodoc2-docstring} archivebox.parsers.pocket_api.__package__
```

````

````{py:data} COUNT_PER_PAGE
:canonical: archivebox.parsers.pocket_api.COUNT_PER_PAGE
:value: >
   500

```{autodoc2-docstring} archivebox.parsers.pocket_api.COUNT_PER_PAGE
```

````

````{py:data} API_DB_PATH
:canonical: archivebox.parsers.pocket_api.API_DB_PATH
:value: >
   None

```{autodoc2-docstring} archivebox.parsers.pocket_api.API_DB_PATH
```

````

````{py:data} _BROKEN_PROTOCOL_RE
:canonical: archivebox.parsers.pocket_api._BROKEN_PROTOCOL_RE
:value: >
   'compile(...)'

```{autodoc2-docstring} archivebox.parsers.pocket_api._BROKEN_PROTOCOL_RE
```

````

````{py:function} get_pocket_articles(api: pocket.Pocket, since=None, page=0)
:canonical: archivebox.parsers.pocket_api.get_pocket_articles

```{autodoc2-docstring} archivebox.parsers.pocket_api.get_pocket_articles
```
````

````{py:function} link_from_article(article: dict, sources: list)
:canonical: archivebox.parsers.pocket_api.link_from_article

```{autodoc2-docstring} archivebox.parsers.pocket_api.link_from_article
```
````

````{py:function} write_since(username: str, since: str)
:canonical: archivebox.parsers.pocket_api.write_since

```{autodoc2-docstring} archivebox.parsers.pocket_api.write_since
```
````

````{py:function} read_since(username: str) -> typing.Optional[str]
:canonical: archivebox.parsers.pocket_api.read_since

```{autodoc2-docstring} archivebox.parsers.pocket_api.read_since
```
````

````{py:function} should_parse_as_pocket_api(text: str) -> bool
:canonical: archivebox.parsers.pocket_api.should_parse_as_pocket_api

```{autodoc2-docstring} archivebox.parsers.pocket_api.should_parse_as_pocket_api
```
````

````{py:function} parse_pocket_api_export(input_buffer: typing.IO[str], **_kwargs) -> typing.Iterable[archivebox.index.schema.Link]
:canonical: archivebox.parsers.pocket_api.parse_pocket_api_export

```{autodoc2-docstring} archivebox.parsers.pocket_api.parse_pocket_api_export
```
````

````{py:data} KEY
:canonical: archivebox.parsers.pocket_api.KEY
:value: >
   'pocket_api'

```{autodoc2-docstring} archivebox.parsers.pocket_api.KEY
```

````

````{py:data} NAME
:canonical: archivebox.parsers.pocket_api.NAME
:value: >
   'Pocket API'

```{autodoc2-docstring} archivebox.parsers.pocket_api.NAME
```

````

````{py:data} PARSER
:canonical: archivebox.parsers.pocket_api.PARSER
:value: >
   None

```{autodoc2-docstring} archivebox.parsers.pocket_api.PARSER
```

````
