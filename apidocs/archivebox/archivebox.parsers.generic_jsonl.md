# {py:mod}`archivebox.parsers.generic_jsonl`

```{py:module} archivebox.parsers.generic_jsonl
```

```{autodoc2-docstring} archivebox.parsers.generic_jsonl
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`parse_line <archivebox.parsers.generic_jsonl.parse_line>`
  - ```{autodoc2-docstring} archivebox.parsers.generic_jsonl.parse_line
    :summary:
    ```
* - {py:obj}`parse_generic_jsonl_export <archivebox.parsers.generic_jsonl.parse_generic_jsonl_export>`
  - ```{autodoc2-docstring} archivebox.parsers.generic_jsonl.parse_generic_jsonl_export
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.parsers.generic_jsonl.__package__>`
  - ```{autodoc2-docstring} archivebox.parsers.generic_jsonl.__package__
    :summary:
    ```
* - {py:obj}`KEY <archivebox.parsers.generic_jsonl.KEY>`
  - ```{autodoc2-docstring} archivebox.parsers.generic_jsonl.KEY
    :summary:
    ```
* - {py:obj}`NAME <archivebox.parsers.generic_jsonl.NAME>`
  - ```{autodoc2-docstring} archivebox.parsers.generic_jsonl.NAME
    :summary:
    ```
* - {py:obj}`PARSER <archivebox.parsers.generic_jsonl.PARSER>`
  - ```{autodoc2-docstring} archivebox.parsers.generic_jsonl.PARSER
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.parsers.generic_jsonl.__package__
:value: >
   'archivebox.parsers'

```{autodoc2-docstring} archivebox.parsers.generic_jsonl.__package__
```

````

````{py:function} parse_line(line: str)
:canonical: archivebox.parsers.generic_jsonl.parse_line

```{autodoc2-docstring} archivebox.parsers.generic_jsonl.parse_line
```
````

````{py:function} parse_generic_jsonl_export(json_file: typing.IO[str], **_kwargs) -> typing.Iterable[archivebox.index.schema.Link]
:canonical: archivebox.parsers.generic_jsonl.parse_generic_jsonl_export

```{autodoc2-docstring} archivebox.parsers.generic_jsonl.parse_generic_jsonl_export
```
````

````{py:data} KEY
:canonical: archivebox.parsers.generic_jsonl.KEY
:value: >
   'jsonl'

```{autodoc2-docstring} archivebox.parsers.generic_jsonl.KEY
```

````

````{py:data} NAME
:canonical: archivebox.parsers.generic_jsonl.NAME
:value: >
   'Generic JSONL'

```{autodoc2-docstring} archivebox.parsers.generic_jsonl.NAME
```

````

````{py:data} PARSER
:canonical: archivebox.parsers.generic_jsonl.PARSER
:value: >
   None

```{autodoc2-docstring} archivebox.parsers.generic_jsonl.PARSER
```

````
