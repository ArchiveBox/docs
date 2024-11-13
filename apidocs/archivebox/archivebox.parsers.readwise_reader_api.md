# {py:mod}`archivebox.parsers.readwise_reader_api`

```{py:module} archivebox.parsers.readwise_reader_api
```

```{autodoc2-docstring} archivebox.parsers.readwise_reader_api
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ReadwiseReaderAPI <archivebox.parsers.readwise_reader_api.ReadwiseReaderAPI>`
  - ```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.ReadwiseReaderAPI
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_readwise_reader_articles <archivebox.parsers.readwise_reader_api.get_readwise_reader_articles>`
  - ```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.get_readwise_reader_articles
    :summary:
    ```
* - {py:obj}`link_from_article <archivebox.parsers.readwise_reader_api.link_from_article>`
  - ```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.link_from_article
    :summary:
    ```
* - {py:obj}`write_cursor <archivebox.parsers.readwise_reader_api.write_cursor>`
  - ```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.write_cursor
    :summary:
    ```
* - {py:obj}`read_cursor <archivebox.parsers.readwise_reader_api.read_cursor>`
  - ```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.read_cursor
    :summary:
    ```
* - {py:obj}`should_parse_as_readwise_reader_api <archivebox.parsers.readwise_reader_api.should_parse_as_readwise_reader_api>`
  - ```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.should_parse_as_readwise_reader_api
    :summary:
    ```
* - {py:obj}`parse_readwise_reader_api_export <archivebox.parsers.readwise_reader_api.parse_readwise_reader_api_export>`
  - ```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.parse_readwise_reader_api_export
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.parsers.readwise_reader_api.__package__>`
  - ```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.__package__
    :summary:
    ```
* - {py:obj}`KEY <archivebox.parsers.readwise_reader_api.KEY>`
  - ```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.KEY
    :summary:
    ```
* - {py:obj}`NAME <archivebox.parsers.readwise_reader_api.NAME>`
  - ```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.NAME
    :summary:
    ```
* - {py:obj}`PARSER <archivebox.parsers.readwise_reader_api.PARSER>`
  - ```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.PARSER
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.parsers.readwise_reader_api.__package__
:value: >
   'archivebox.parsers'

```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.__package__
```

````

`````{py:class} ReadwiseReaderAPI(api_token, cursor=None)
:canonical: archivebox.parsers.readwise_reader_api.ReadwiseReaderAPI

```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.ReadwiseReaderAPI
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.ReadwiseReaderAPI.__init__
```

````{py:attribute} cursor
:canonical: archivebox.parsers.readwise_reader_api.ReadwiseReaderAPI.cursor
:type: typing.Optional[str]
:value: >
   None

```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.ReadwiseReaderAPI.cursor
```

````

````{py:method} get_archive()
:canonical: archivebox.parsers.readwise_reader_api.ReadwiseReaderAPI.get_archive

```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.ReadwiseReaderAPI.get_archive
```

````

`````

````{py:function} get_readwise_reader_articles(api: archivebox.parsers.readwise_reader_api.ReadwiseReaderAPI)
:canonical: archivebox.parsers.readwise_reader_api.get_readwise_reader_articles

```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.get_readwise_reader_articles
```
````

````{py:function} link_from_article(article: dict, sources: list)
:canonical: archivebox.parsers.readwise_reader_api.link_from_article

```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.link_from_article
```
````

````{py:function} write_cursor(username: str, since: str)
:canonical: archivebox.parsers.readwise_reader_api.write_cursor

```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.write_cursor
```
````

````{py:function} read_cursor(username: str) -> typing.Optional[str]
:canonical: archivebox.parsers.readwise_reader_api.read_cursor

```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.read_cursor
```
````

````{py:function} should_parse_as_readwise_reader_api(text: str) -> bool
:canonical: archivebox.parsers.readwise_reader_api.should_parse_as_readwise_reader_api

```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.should_parse_as_readwise_reader_api
```
````

````{py:function} parse_readwise_reader_api_export(input_buffer: typing.IO[str], **_kwargs) -> typing.Iterable[archivebox.index.schema.Link]
:canonical: archivebox.parsers.readwise_reader_api.parse_readwise_reader_api_export

```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.parse_readwise_reader_api_export
```
````

````{py:data} KEY
:canonical: archivebox.parsers.readwise_reader_api.KEY
:value: >
   'readwise_reader_api'

```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.KEY
```

````

````{py:data} NAME
:canonical: archivebox.parsers.readwise_reader_api.NAME
:value: >
   'Readwise Reader API'

```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.NAME
```

````

````{py:data} PARSER
:canonical: archivebox.parsers.readwise_reader_api.PARSER
:value: >
   None

```{autodoc2-docstring} archivebox.parsers.readwise_reader_api.PARSER
```

````
