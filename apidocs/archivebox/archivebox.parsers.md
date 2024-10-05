# {py:mod}`archivebox.parsers`

```{py:module} archivebox.parsers
```

```{autodoc2-docstring} archivebox.parsers
:allowtitles:
```

## Submodules

```{toctree}
:titlesonly:
:maxdepth: 1

archivebox.parsers.readwise_reader_api
archivebox.parsers.generic_json
archivebox.parsers.generic_txt
archivebox.parsers.generic_jsonl
archivebox.parsers.wallabag_atom
archivebox.parsers.generic_rss
archivebox.parsers.pocket_html
archivebox.parsers.medium_rss
archivebox.parsers.netscape_html
archivebox.parsers.url_list
archivebox.parsers.pinboard_rss
archivebox.parsers.generic_html
archivebox.parsers.shaarli_rss
archivebox.parsers.pocket_api
```

## Package Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`parse_links_memory <archivebox.parsers.parse_links_memory>`
  - ```{autodoc2-docstring} archivebox.parsers.parse_links_memory
    :summary:
    ```
* - {py:obj}`parse_links <archivebox.parsers.parse_links>`
  - ```{autodoc2-docstring} archivebox.parsers.parse_links
    :summary:
    ```
* - {py:obj}`run_parser_functions <archivebox.parsers.run_parser_functions>`
  - ```{autodoc2-docstring} archivebox.parsers.run_parser_functions
    :summary:
    ```
* - {py:obj}`save_text_as_source <archivebox.parsers.save_text_as_source>`
  - ```{autodoc2-docstring} archivebox.parsers.save_text_as_source
    :summary:
    ```
* - {py:obj}`save_file_as_source <archivebox.parsers.save_file_as_source>`
  - ```{autodoc2-docstring} archivebox.parsers.save_file_as_source
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.parsers.__package__>`
  - ```{autodoc2-docstring} archivebox.parsers.__package__
    :summary:
    ```
* - {py:obj}`PARSERS <archivebox.parsers.PARSERS>`
  - ```{autodoc2-docstring} archivebox.parsers.PARSERS
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.parsers.__package__
:value: >
   'archivebox.parsers'

```{autodoc2-docstring} archivebox.parsers.__package__
```

````

````{py:data} PARSERS
:canonical: archivebox.parsers.PARSERS
:value: >
   None

```{autodoc2-docstring} archivebox.parsers.PARSERS
```

````

````{py:function} parse_links_memory(urls: typing.List[str], root_url: typing.Optional[str] = None)
:canonical: archivebox.parsers.parse_links_memory

```{autodoc2-docstring} archivebox.parsers.parse_links_memory
```
````

````{py:function} parse_links(source_file: str, root_url: typing.Optional[str] = None, parser: str = 'auto') -> typing.Tuple[typing.List[archivebox.index.schema.Link], str]
:canonical: archivebox.parsers.parse_links

```{autodoc2-docstring} archivebox.parsers.parse_links
```
````

````{py:function} run_parser_functions(to_parse: typing.IO[str], timer, root_url: typing.Optional[str] = None, parser: str = 'auto') -> typing.Tuple[typing.List[archivebox.index.schema.Link], typing.Optional[str]]
:canonical: archivebox.parsers.run_parser_functions

```{autodoc2-docstring} archivebox.parsers.run_parser_functions
```
````

````{py:function} save_text_as_source(raw_text: str, filename: str = '{ts}-stdin.txt', out_dir: pathlib.Path = DATA_DIR) -> str
:canonical: archivebox.parsers.save_text_as_source

```{autodoc2-docstring} archivebox.parsers.save_text_as_source
```
````

````{py:function} save_file_as_source(path: str, timeout: int = ARCHIVING_CONFIG.TIMEOUT, filename: str = '{ts}-{basename}.txt', out_dir: pathlib.Path = DATA_DIR) -> str
:canonical: archivebox.parsers.save_file_as_source

```{autodoc2-docstring} archivebox.parsers.save_file_as_source
```
````
