# {py:mod}`archivebox.index.json`

```{py:module} archivebox.index.json
```

```{autodoc2-docstring} archivebox.index.json
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ExtendedEncoder <archivebox.index.json.ExtendedEncoder>`
  - ```{autodoc2-docstring} archivebox.index.json.ExtendedEncoder
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`generate_json_index_from_links <archivebox.index.json.generate_json_index_from_links>`
  - ```{autodoc2-docstring} archivebox.index.json.generate_json_index_from_links
    :summary:
    ```
* - {py:obj}`parse_json_main_index <archivebox.index.json.parse_json_main_index>`
  - ```{autodoc2-docstring} archivebox.index.json.parse_json_main_index
    :summary:
    ```
* - {py:obj}`write_json_link_details <archivebox.index.json.write_json_link_details>`
  - ```{autodoc2-docstring} archivebox.index.json.write_json_link_details
    :summary:
    ```
* - {py:obj}`parse_json_link_details <archivebox.index.json.parse_json_link_details>`
  - ```{autodoc2-docstring} archivebox.index.json.parse_json_link_details
    :summary:
    ```
* - {py:obj}`parse_json_links_details <archivebox.index.json.parse_json_links_details>`
  - ```{autodoc2-docstring} archivebox.index.json.parse_json_links_details
    :summary:
    ```
* - {py:obj}`to_json <archivebox.index.json.to_json>`
  - ```{autodoc2-docstring} archivebox.index.json.to_json
    :summary:
    ```
````

### API

````{py:function} generate_json_index_from_links(links: typing.List[archivebox.index.schema.Link], with_headers: bool)
:canonical: archivebox.index.json.generate_json_index_from_links

```{autodoc2-docstring} archivebox.index.json.generate_json_index_from_links
```
````

````{py:function} parse_json_main_index(out_dir: pathlib.Path = DATA_DIR) -> typing.Iterator[archivebox.index.schema.Link]
:canonical: archivebox.index.json.parse_json_main_index

```{autodoc2-docstring} archivebox.index.json.parse_json_main_index
```
````

````{py:function} write_json_link_details(link: archivebox.index.schema.Link, out_dir: typing.Optional[str] = None) -> None
:canonical: archivebox.index.json.write_json_link_details

```{autodoc2-docstring} archivebox.index.json.write_json_link_details
```
````

````{py:function} parse_json_link_details(out_dir: typing.Union[pathlib.Path, str], guess: bool = False) -> typing.Optional[archivebox.index.schema.Link]
:canonical: archivebox.index.json.parse_json_link_details

```{autodoc2-docstring} archivebox.index.json.parse_json_link_details
```
````

````{py:function} parse_json_links_details(out_dir: typing.Union[pathlib.Path, str]) -> typing.Iterator[archivebox.index.schema.Link]
:canonical: archivebox.index.json.parse_json_links_details

```{autodoc2-docstring} archivebox.index.json.parse_json_links_details
```
````

`````{py:class} ExtendedEncoder(*, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)
:canonical: archivebox.index.json.ExtendedEncoder

Bases: {py:obj}`json.JSONEncoder`

```{autodoc2-docstring} archivebox.index.json.ExtendedEncoder
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.index.json.ExtendedEncoder.__init__
```

````{py:method} default(obj)
:canonical: archivebox.index.json.ExtendedEncoder.default

````

`````

````{py:function} to_json(obj: typing.Any, indent: typing.Optional[int] = 4, sort_keys: bool = True, cls=ExtendedEncoder) -> str
:canonical: archivebox.index.json.to_json

```{autodoc2-docstring} archivebox.index.json.to_json
```
````
