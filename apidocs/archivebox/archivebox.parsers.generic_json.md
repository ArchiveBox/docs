# {py:mod}`archivebox.parsers.generic_json`

```{py:module} archivebox.parsers.generic_json
```

```{autodoc2-docstring} archivebox.parsers.generic_json
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`jsonObjectToLink <archivebox.parsers.generic_json.jsonObjectToLink>`
  - ```{autodoc2-docstring} archivebox.parsers.generic_json.jsonObjectToLink
    :summary:
    ```
* - {py:obj}`parse_generic_json_export <archivebox.parsers.generic_json.parse_generic_json_export>`
  - ```{autodoc2-docstring} archivebox.parsers.generic_json.parse_generic_json_export
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.parsers.generic_json.__package__>`
  - ```{autodoc2-docstring} archivebox.parsers.generic_json.__package__
    :summary:
    ```
* - {py:obj}`KEY <archivebox.parsers.generic_json.KEY>`
  - ```{autodoc2-docstring} archivebox.parsers.generic_json.KEY
    :summary:
    ```
* - {py:obj}`NAME <archivebox.parsers.generic_json.NAME>`
  - ```{autodoc2-docstring} archivebox.parsers.generic_json.NAME
    :summary:
    ```
* - {py:obj}`PARSER <archivebox.parsers.generic_json.PARSER>`
  - ```{autodoc2-docstring} archivebox.parsers.generic_json.PARSER
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.parsers.generic_json.__package__
:value: >
   'archivebox.parsers'

```{autodoc2-docstring} archivebox.parsers.generic_json.__package__
```

````

````{py:function} jsonObjectToLink(link: str, source: str)
:canonical: archivebox.parsers.generic_json.jsonObjectToLink

```{autodoc2-docstring} archivebox.parsers.generic_json.jsonObjectToLink
```
````

````{py:function} parse_generic_json_export(json_file: typing.IO[str], **_kwargs) -> typing.Iterable[archivebox.index.schema.Link]
:canonical: archivebox.parsers.generic_json.parse_generic_json_export

```{autodoc2-docstring} archivebox.parsers.generic_json.parse_generic_json_export
```
````

````{py:data} KEY
:canonical: archivebox.parsers.generic_json.KEY
:value: >
   'json'

```{autodoc2-docstring} archivebox.parsers.generic_json.KEY
```

````

````{py:data} NAME
:canonical: archivebox.parsers.generic_json.NAME
:value: >
   'Generic JSON'

```{autodoc2-docstring} archivebox.parsers.generic_json.NAME
```

````

````{py:data} PARSER
:canonical: archivebox.parsers.generic_json.PARSER
:value: >
   None

```{autodoc2-docstring} archivebox.parsers.generic_json.PARSER
```

````
