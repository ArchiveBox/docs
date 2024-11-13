# {py:mod}`archivebox.index.schema`

```{py:module} archivebox.index.schema
```

```{autodoc2-docstring} archivebox.index.schema
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ArchiveResult <archivebox.index.schema.ArchiveResult>`
  - ```{autodoc2-docstring} archivebox.index.schema.ArchiveResult
    :summary:
    ```
* - {py:obj}`Link <archivebox.index.schema.Link>`
  - ```{autodoc2-docstring} archivebox.index.schema.Link
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`LinkDict <archivebox.index.schema.LinkDict>`
  - ```{autodoc2-docstring} archivebox.index.schema.LinkDict
    :summary:
    ```
* - {py:obj}`ArchiveOutput <archivebox.index.schema.ArchiveOutput>`
  - ```{autodoc2-docstring} archivebox.index.schema.ArchiveOutput
    :summary:
    ```
````

### API

```{py:exception} ArchiveError(message, hints=None)
:canonical: archivebox.index.schema.ArchiveError

Bases: {py:obj}`Exception`

```

````{py:data} LinkDict
:canonical: archivebox.index.schema.LinkDict
:value: >
   None

```{autodoc2-docstring} archivebox.index.schema.LinkDict
```

````

````{py:data} ArchiveOutput
:canonical: archivebox.index.schema.ArchiveOutput
:value: >
   None

```{autodoc2-docstring} archivebox.index.schema.ArchiveOutput
```

````

`````{py:class} ArchiveResult
:canonical: archivebox.index.schema.ArchiveResult

```{autodoc2-docstring} archivebox.index.schema.ArchiveResult
```

````{py:attribute} cmd
:canonical: archivebox.index.schema.ArchiveResult.cmd
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} archivebox.index.schema.ArchiveResult.cmd
```

````

````{py:attribute} pwd
:canonical: archivebox.index.schema.ArchiveResult.pwd
:type: typing.Optional[str]
:value: >
   None

```{autodoc2-docstring} archivebox.index.schema.ArchiveResult.pwd
```

````

````{py:attribute} cmd_version
:canonical: archivebox.index.schema.ArchiveResult.cmd_version
:type: typing.Optional[str]
:value: >
   None

```{autodoc2-docstring} archivebox.index.schema.ArchiveResult.cmd_version
```

````

````{py:attribute} output
:canonical: archivebox.index.schema.ArchiveResult.output
:type: archivebox.index.schema.ArchiveOutput
:value: >
   None

```{autodoc2-docstring} archivebox.index.schema.ArchiveResult.output
```

````

````{py:attribute} status
:canonical: archivebox.index.schema.ArchiveResult.status
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.index.schema.ArchiveResult.status
```

````

````{py:attribute} start_ts
:canonical: archivebox.index.schema.ArchiveResult.start_ts
:type: datetime.datetime
:value: >
   None

```{autodoc2-docstring} archivebox.index.schema.ArchiveResult.start_ts
```

````

````{py:attribute} end_ts
:canonical: archivebox.index.schema.ArchiveResult.end_ts
:type: datetime.datetime
:value: >
   None

```{autodoc2-docstring} archivebox.index.schema.ArchiveResult.end_ts
```

````

````{py:attribute} index_texts
:canonical: archivebox.index.schema.ArchiveResult.index_texts
:type: typing.Union[typing.List[str], None]
:value: >
   None

```{autodoc2-docstring} archivebox.index.schema.ArchiveResult.index_texts
```

````

````{py:attribute} schema
:canonical: archivebox.index.schema.ArchiveResult.schema
:type: str
:value: >
   'ArchiveResult'

```{autodoc2-docstring} archivebox.index.schema.ArchiveResult.schema
```

````

````{py:method} __post_init__()
:canonical: archivebox.index.schema.ArchiveResult.__post_init__

```{autodoc2-docstring} archivebox.index.schema.ArchiveResult.__post_init__
```

````

````{py:method} _asdict()
:canonical: archivebox.index.schema.ArchiveResult._asdict

```{autodoc2-docstring} archivebox.index.schema.ArchiveResult._asdict
```

````

````{py:method} typecheck() -> None
:canonical: archivebox.index.schema.ArchiveResult.typecheck

```{autodoc2-docstring} archivebox.index.schema.ArchiveResult.typecheck
```

````

````{py:method} guess_ts(dict_info)
:canonical: archivebox.index.schema.ArchiveResult.guess_ts
:classmethod:

```{autodoc2-docstring} archivebox.index.schema.ArchiveResult.guess_ts
```

````

````{py:method} from_json(json_info, guess=False)
:canonical: archivebox.index.schema.ArchiveResult.from_json
:classmethod:

```{autodoc2-docstring} archivebox.index.schema.ArchiveResult.from_json
```

````

````{py:method} to_dict(*keys) -> dict
:canonical: archivebox.index.schema.ArchiveResult.to_dict

```{autodoc2-docstring} archivebox.index.schema.ArchiveResult.to_dict
```

````

````{py:method} to_json(indent=4, sort_keys=True) -> str
:canonical: archivebox.index.schema.ArchiveResult.to_json

```{autodoc2-docstring} archivebox.index.schema.ArchiveResult.to_json
```

````

````{py:method} to_csv(cols: typing.Optional[typing.List[str]] = None, separator: str = ',', ljust: int = 0) -> str
:canonical: archivebox.index.schema.ArchiveResult.to_csv

```{autodoc2-docstring} archivebox.index.schema.ArchiveResult.to_csv
```

````

````{py:method} field_names()
:canonical: archivebox.index.schema.ArchiveResult.field_names
:classmethod:

```{autodoc2-docstring} archivebox.index.schema.ArchiveResult.field_names
```

````

````{py:property} duration
:canonical: archivebox.index.schema.ArchiveResult.duration
:type: int

```{autodoc2-docstring} archivebox.index.schema.ArchiveResult.duration
```

````

`````

`````{py:class} Link
:canonical: archivebox.index.schema.Link

```{autodoc2-docstring} archivebox.index.schema.Link
```

````{py:attribute} timestamp
:canonical: archivebox.index.schema.Link.timestamp
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.index.schema.Link.timestamp
```

````

````{py:attribute} url
:canonical: archivebox.index.schema.Link.url
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.index.schema.Link.url
```

````

````{py:attribute} title
:canonical: archivebox.index.schema.Link.title
:type: typing.Optional[str]
:value: >
   None

```{autodoc2-docstring} archivebox.index.schema.Link.title
```

````

````{py:attribute} tags
:canonical: archivebox.index.schema.Link.tags
:type: typing.Optional[str]
:value: >
   None

```{autodoc2-docstring} archivebox.index.schema.Link.tags
```

````

````{py:attribute} sources
:canonical: archivebox.index.schema.Link.sources
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} archivebox.index.schema.Link.sources
```

````

````{py:attribute} history
:canonical: archivebox.index.schema.Link.history
:type: typing.Dict[str, typing.List[archivebox.index.schema.ArchiveResult]]
:value: >
   'field(...)'

```{autodoc2-docstring} archivebox.index.schema.Link.history
```

````

````{py:attribute} downloaded_at
:canonical: archivebox.index.schema.Link.downloaded_at
:type: typing.Optional[datetime.datetime]
:value: >
   None

```{autodoc2-docstring} archivebox.index.schema.Link.downloaded_at
```

````

````{py:attribute} schema
:canonical: archivebox.index.schema.Link.schema
:type: str
:value: >
   'Link'

```{autodoc2-docstring} archivebox.index.schema.Link.schema
```

````

````{py:method} __str__() -> str
:canonical: archivebox.index.schema.Link.__str__

````

````{py:method} __post_init__()
:canonical: archivebox.index.schema.Link.__post_init__

```{autodoc2-docstring} archivebox.index.schema.Link.__post_init__
```

````

````{py:method} overwrite(**kwargs)
:canonical: archivebox.index.schema.Link.overwrite

```{autodoc2-docstring} archivebox.index.schema.Link.overwrite
```

````

````{py:method} __eq__(other)
:canonical: archivebox.index.schema.Link.__eq__

````

````{py:method} __gt__(other)
:canonical: archivebox.index.schema.Link.__gt__

````

````{py:method} typecheck() -> None
:canonical: archivebox.index.schema.Link.typecheck

```{autodoc2-docstring} archivebox.index.schema.Link.typecheck
```

````

````{py:method} _asdict(extended=False)
:canonical: archivebox.index.schema.Link._asdict

```{autodoc2-docstring} archivebox.index.schema.Link._asdict
```

````

````{py:method} as_snapshot()
:canonical: archivebox.index.schema.Link.as_snapshot

```{autodoc2-docstring} archivebox.index.schema.Link.as_snapshot
```

````

````{py:method} from_json(json_info, guess=False)
:canonical: archivebox.index.schema.Link.from_json
:classmethod:

```{autodoc2-docstring} archivebox.index.schema.Link.from_json
```

````

````{py:method} to_json(indent=4, sort_keys=True) -> str
:canonical: archivebox.index.schema.Link.to_json

```{autodoc2-docstring} archivebox.index.schema.Link.to_json
```

````

````{py:method} to_csv(cols: typing.Optional[typing.List[str]] = None, separator: str = ',', ljust: int = 0) -> str
:canonical: archivebox.index.schema.Link.to_csv

```{autodoc2-docstring} archivebox.index.schema.Link.to_csv
```

````

````{py:method} snapshot()
:canonical: archivebox.index.schema.Link.snapshot

```{autodoc2-docstring} archivebox.index.schema.Link.snapshot
```

````

````{py:method} snapshot_id()
:canonical: archivebox.index.schema.Link.snapshot_id

```{autodoc2-docstring} archivebox.index.schema.Link.snapshot_id
```

````

````{py:method} snapshot_abid()
:canonical: archivebox.index.schema.Link.snapshot_abid

```{autodoc2-docstring} archivebox.index.schema.Link.snapshot_abid
```

````

````{py:method} field_names()
:canonical: archivebox.index.schema.Link.field_names
:classmethod:

```{autodoc2-docstring} archivebox.index.schema.Link.field_names
```

````

````{py:property} link_dir
:canonical: archivebox.index.schema.Link.link_dir
:type: str

```{autodoc2-docstring} archivebox.index.schema.Link.link_dir
```

````

````{py:property} archive_path
:canonical: archivebox.index.schema.Link.archive_path
:type: str

```{autodoc2-docstring} archivebox.index.schema.Link.archive_path
```

````

````{py:property} archive_size
:canonical: archivebox.index.schema.Link.archive_size
:type: float

```{autodoc2-docstring} archivebox.index.schema.Link.archive_size
```

````

````{py:property} url_hash
:canonical: archivebox.index.schema.Link.url_hash

```{autodoc2-docstring} archivebox.index.schema.Link.url_hash
```

````

````{py:property} scheme
:canonical: archivebox.index.schema.Link.scheme
:type: str

```{autodoc2-docstring} archivebox.index.schema.Link.scheme
```

````

````{py:property} extension
:canonical: archivebox.index.schema.Link.extension
:type: str

```{autodoc2-docstring} archivebox.index.schema.Link.extension
```

````

````{py:property} domain
:canonical: archivebox.index.schema.Link.domain
:type: str

```{autodoc2-docstring} archivebox.index.schema.Link.domain
```

````

````{py:property} path
:canonical: archivebox.index.schema.Link.path
:type: str

```{autodoc2-docstring} archivebox.index.schema.Link.path
```

````

````{py:property} basename
:canonical: archivebox.index.schema.Link.basename
:type: str

```{autodoc2-docstring} archivebox.index.schema.Link.basename
```

````

````{py:property} base_url
:canonical: archivebox.index.schema.Link.base_url
:type: str

```{autodoc2-docstring} archivebox.index.schema.Link.base_url
```

````

````{py:property} bookmarked_date
:canonical: archivebox.index.schema.Link.bookmarked_date
:type: typing.Optional[str]

```{autodoc2-docstring} archivebox.index.schema.Link.bookmarked_date
```

````

````{py:property} downloaded_datestr
:canonical: archivebox.index.schema.Link.downloaded_datestr
:type: typing.Optional[str]

```{autodoc2-docstring} archivebox.index.schema.Link.downloaded_datestr
```

````

````{py:property} archive_dates
:canonical: archivebox.index.schema.Link.archive_dates
:type: typing.List[datetime.datetime]

```{autodoc2-docstring} archivebox.index.schema.Link.archive_dates
```

````

````{py:property} oldest_archive_date
:canonical: archivebox.index.schema.Link.oldest_archive_date
:type: typing.Optional[datetime.datetime]

```{autodoc2-docstring} archivebox.index.schema.Link.oldest_archive_date
```

````

````{py:property} newest_archive_date
:canonical: archivebox.index.schema.Link.newest_archive_date
:type: typing.Optional[datetime.datetime]

```{autodoc2-docstring} archivebox.index.schema.Link.newest_archive_date
```

````

````{py:property} num_outputs
:canonical: archivebox.index.schema.Link.num_outputs
:type: int

```{autodoc2-docstring} archivebox.index.schema.Link.num_outputs
```

````

````{py:property} num_failures
:canonical: archivebox.index.schema.Link.num_failures
:type: int

```{autodoc2-docstring} archivebox.index.schema.Link.num_failures
```

````

````{py:property} is_static
:canonical: archivebox.index.schema.Link.is_static
:type: bool

```{autodoc2-docstring} archivebox.index.schema.Link.is_static
```

````

````{py:property} is_archived
:canonical: archivebox.index.schema.Link.is_archived
:type: bool

```{autodoc2-docstring} archivebox.index.schema.Link.is_archived
```

````

````{py:method} latest_outputs(status: str = None) -> typing.Dict[str, archivebox.index.schema.ArchiveOutput]
:canonical: archivebox.index.schema.Link.latest_outputs

```{autodoc2-docstring} archivebox.index.schema.Link.latest_outputs
```

````

````{py:method} canonical_outputs() -> typing.Dict[str, typing.Optional[str]]
:canonical: archivebox.index.schema.Link.canonical_outputs

```{autodoc2-docstring} archivebox.index.schema.Link.canonical_outputs
```

````

`````
