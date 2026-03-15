# {py:mod}`archivebox.misc.jsonl`

```{py:module} archivebox.misc.jsonl
```

```{autodoc2-docstring} archivebox.misc.jsonl
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`parse_line <archivebox.misc.jsonl.parse_line>`
  - ```{autodoc2-docstring} archivebox.misc.jsonl.parse_line
    :summary:
    ```
* - {py:obj}`read_stdin <archivebox.misc.jsonl.read_stdin>`
  - ```{autodoc2-docstring} archivebox.misc.jsonl.read_stdin
    :summary:
    ```
* - {py:obj}`read_file <archivebox.misc.jsonl.read_file>`
  - ```{autodoc2-docstring} archivebox.misc.jsonl.read_file
    :summary:
    ```
* - {py:obj}`read_args_or_stdin <archivebox.misc.jsonl.read_args_or_stdin>`
  - ```{autodoc2-docstring} archivebox.misc.jsonl.read_args_or_stdin
    :summary:
    ```
* - {py:obj}`write_record <archivebox.misc.jsonl.write_record>`
  - ```{autodoc2-docstring} archivebox.misc.jsonl.write_record
    :summary:
    ```
* - {py:obj}`write_records <archivebox.misc.jsonl.write_records>`
  - ```{autodoc2-docstring} archivebox.misc.jsonl.write_records
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TYPE_SNAPSHOT <archivebox.misc.jsonl.TYPE_SNAPSHOT>`
  - ```{autodoc2-docstring} archivebox.misc.jsonl.TYPE_SNAPSHOT
    :summary:
    ```
* - {py:obj}`TYPE_ARCHIVERESULT <archivebox.misc.jsonl.TYPE_ARCHIVERESULT>`
  - ```{autodoc2-docstring} archivebox.misc.jsonl.TYPE_ARCHIVERESULT
    :summary:
    ```
* - {py:obj}`TYPE_TAG <archivebox.misc.jsonl.TYPE_TAG>`
  - ```{autodoc2-docstring} archivebox.misc.jsonl.TYPE_TAG
    :summary:
    ```
* - {py:obj}`TYPE_CRAWL <archivebox.misc.jsonl.TYPE_CRAWL>`
  - ```{autodoc2-docstring} archivebox.misc.jsonl.TYPE_CRAWL
    :summary:
    ```
* - {py:obj}`TYPE_BINARY <archivebox.misc.jsonl.TYPE_BINARY>`
  - ```{autodoc2-docstring} archivebox.misc.jsonl.TYPE_BINARY
    :summary:
    ```
* - {py:obj}`TYPE_PROCESS <archivebox.misc.jsonl.TYPE_PROCESS>`
  - ```{autodoc2-docstring} archivebox.misc.jsonl.TYPE_PROCESS
    :summary:
    ```
* - {py:obj}`TYPE_MACHINE <archivebox.misc.jsonl.TYPE_MACHINE>`
  - ```{autodoc2-docstring} archivebox.misc.jsonl.TYPE_MACHINE
    :summary:
    ```
* - {py:obj}`VALID_TYPES <archivebox.misc.jsonl.VALID_TYPES>`
  - ```{autodoc2-docstring} archivebox.misc.jsonl.VALID_TYPES
    :summary:
    ```
````

### API

````{py:data} TYPE_SNAPSHOT
:canonical: archivebox.misc.jsonl.TYPE_SNAPSHOT
:value: >
   'Snapshot'

```{autodoc2-docstring} archivebox.misc.jsonl.TYPE_SNAPSHOT
```

````

````{py:data} TYPE_ARCHIVERESULT
:canonical: archivebox.misc.jsonl.TYPE_ARCHIVERESULT
:value: >
   'ArchiveResult'

```{autodoc2-docstring} archivebox.misc.jsonl.TYPE_ARCHIVERESULT
```

````

````{py:data} TYPE_TAG
:canonical: archivebox.misc.jsonl.TYPE_TAG
:value: >
   'Tag'

```{autodoc2-docstring} archivebox.misc.jsonl.TYPE_TAG
```

````

````{py:data} TYPE_CRAWL
:canonical: archivebox.misc.jsonl.TYPE_CRAWL
:value: >
   'Crawl'

```{autodoc2-docstring} archivebox.misc.jsonl.TYPE_CRAWL
```

````

````{py:data} TYPE_BINARY
:canonical: archivebox.misc.jsonl.TYPE_BINARY
:value: >
   'Binary'

```{autodoc2-docstring} archivebox.misc.jsonl.TYPE_BINARY
```

````

````{py:data} TYPE_PROCESS
:canonical: archivebox.misc.jsonl.TYPE_PROCESS
:value: >
   'Process'

```{autodoc2-docstring} archivebox.misc.jsonl.TYPE_PROCESS
```

````

````{py:data} TYPE_MACHINE
:canonical: archivebox.misc.jsonl.TYPE_MACHINE
:value: >
   'Machine'

```{autodoc2-docstring} archivebox.misc.jsonl.TYPE_MACHINE
```

````

````{py:data} VALID_TYPES
:canonical: archivebox.misc.jsonl.VALID_TYPES
:value: >
   None

```{autodoc2-docstring} archivebox.misc.jsonl.VALID_TYPES
```

````

````{py:function} parse_line(line: str) -> typing.Optional[typing.Dict[str, typing.Any]]
:canonical: archivebox.misc.jsonl.parse_line

```{autodoc2-docstring} archivebox.misc.jsonl.parse_line
```
````

````{py:function} read_stdin(stream: typing.Optional[typing.TextIO] = None) -> typing.Iterator[typing.Dict[str, typing.Any]]
:canonical: archivebox.misc.jsonl.read_stdin

```{autodoc2-docstring} archivebox.misc.jsonl.read_stdin
```
````

````{py:function} read_file(path: pathlib.Path) -> typing.Iterator[typing.Dict[str, typing.Any]]
:canonical: archivebox.misc.jsonl.read_file

```{autodoc2-docstring} archivebox.misc.jsonl.read_file
```
````

````{py:function} read_args_or_stdin(args: tuple, stream: typing.Optional[typing.TextIO] = None) -> typing.Iterator[typing.Dict[str, typing.Any]]
:canonical: archivebox.misc.jsonl.read_args_or_stdin

```{autodoc2-docstring} archivebox.misc.jsonl.read_args_or_stdin
```
````

````{py:function} write_record(record: typing.Dict[str, typing.Any], stream: typing.Optional[typing.TextIO] = None) -> None
:canonical: archivebox.misc.jsonl.write_record

```{autodoc2-docstring} archivebox.misc.jsonl.write_record
```
````

````{py:function} write_records(records: typing.Iterator[typing.Dict[str, typing.Any]], stream: typing.Optional[typing.TextIO] = None) -> int
:canonical: archivebox.misc.jsonl.write_records

```{autodoc2-docstring} archivebox.misc.jsonl.write_records
```
````
