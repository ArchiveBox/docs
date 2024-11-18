# {py:mod}`archivebox.api.v1_core`

```{py:module} archivebox.api.v1_core
```

```{autodoc2-docstring} archivebox.api.v1_core
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CustomPagination <archivebox.api.v1_core.CustomPagination>`
  -
* - {py:obj}`MinimalArchiveResultSchema <archivebox.api.v1_core.MinimalArchiveResultSchema>`
  -
* - {py:obj}`ArchiveResultSchema <archivebox.api.v1_core.ArchiveResultSchema>`
  -
* - {py:obj}`ArchiveResultFilterSchema <archivebox.api.v1_core.ArchiveResultFilterSchema>`
  -
* - {py:obj}`SnapshotSchema <archivebox.api.v1_core.SnapshotSchema>`
  -
* - {py:obj}`SnapshotFilterSchema <archivebox.api.v1_core.SnapshotFilterSchema>`
  -
* - {py:obj}`TagSchema <archivebox.api.v1_core.TagSchema>`
  -
* - {py:obj}`SeedSchema <archivebox.api.v1_core.SeedSchema>`
  -
* - {py:obj}`CrawlSchema <archivebox.api.v1_core.CrawlSchema>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_archiveresults <archivebox.api.v1_core.get_archiveresults>`
  - ```{autodoc2-docstring} archivebox.api.v1_core.get_archiveresults
    :summary:
    ```
* - {py:obj}`get_archiveresult <archivebox.api.v1_core.get_archiveresult>`
  - ```{autodoc2-docstring} archivebox.api.v1_core.get_archiveresult
    :summary:
    ```
* - {py:obj}`get_snapshots <archivebox.api.v1_core.get_snapshots>`
  - ```{autodoc2-docstring} archivebox.api.v1_core.get_snapshots
    :summary:
    ```
* - {py:obj}`get_snapshot <archivebox.api.v1_core.get_snapshot>`
  - ```{autodoc2-docstring} archivebox.api.v1_core.get_snapshot
    :summary:
    ```
* - {py:obj}`get_tags <archivebox.api.v1_core.get_tags>`
  - ```{autodoc2-docstring} archivebox.api.v1_core.get_tags
    :summary:
    ```
* - {py:obj}`get_tag <archivebox.api.v1_core.get_tag>`
  - ```{autodoc2-docstring} archivebox.api.v1_core.get_tag
    :summary:
    ```
* - {py:obj}`get_seeds <archivebox.api.v1_core.get_seeds>`
  - ```{autodoc2-docstring} archivebox.api.v1_core.get_seeds
    :summary:
    ```
* - {py:obj}`get_seed <archivebox.api.v1_core.get_seed>`
  - ```{autodoc2-docstring} archivebox.api.v1_core.get_seed
    :summary:
    ```
* - {py:obj}`get_crawls <archivebox.api.v1_core.get_crawls>`
  - ```{autodoc2-docstring} archivebox.api.v1_core.get_crawls
    :summary:
    ```
* - {py:obj}`get_crawl <archivebox.api.v1_core.get_crawl>`
  - ```{autodoc2-docstring} archivebox.api.v1_core.get_crawl
    :summary:
    ```
* - {py:obj}`get_any <archivebox.api.v1_core.get_any>`
  - ```{autodoc2-docstring} archivebox.api.v1_core.get_any
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`router <archivebox.api.v1_core.router>`
  - ```{autodoc2-docstring} archivebox.api.v1_core.router
    :summary:
    ```
````

### API

````{py:data} router
:canonical: archivebox.api.v1_core.router
:value: >
   'Router(...)'

```{autodoc2-docstring} archivebox.api.v1_core.router
```

````

``````{py:class} CustomPagination(*, pass_parameter: typing.Optional[str] = None, **kwargs: typing.Any)
:canonical: archivebox.api.v1_core.CustomPagination

Bases: {py:obj}`ninja.pagination.PaginationBase`

`````{py:class} Input(/, **data: typing.Any)
:canonical: archivebox.api.v1_core.CustomPagination.Input

Bases: {py:obj}`ninja.Schema`

````{py:attribute} limit
:canonical: archivebox.api.v1_core.CustomPagination.Input.limit
:type: int
:value: >
   200

```{autodoc2-docstring} archivebox.api.v1_core.CustomPagination.Input.limit
```

````

````{py:attribute} offset
:canonical: archivebox.api.v1_core.CustomPagination.Input.offset
:type: int
:value: >
   0

```{autodoc2-docstring} archivebox.api.v1_core.CustomPagination.Input.offset
```

````

````{py:attribute} page
:canonical: archivebox.api.v1_core.CustomPagination.Input.page
:type: int
:value: >
   0

```{autodoc2-docstring} archivebox.api.v1_core.CustomPagination.Input.page
```

````

`````

`````{py:class} Output(/, **data: typing.Any)
:canonical: archivebox.api.v1_core.CustomPagination.Output

Bases: {py:obj}`ninja.Schema`

````{py:attribute} total_items
:canonical: archivebox.api.v1_core.CustomPagination.Output.total_items
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.CustomPagination.Output.total_items
```

````

````{py:attribute} total_pages
:canonical: archivebox.api.v1_core.CustomPagination.Output.total_pages
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.CustomPagination.Output.total_pages
```

````

````{py:attribute} page
:canonical: archivebox.api.v1_core.CustomPagination.Output.page
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.CustomPagination.Output.page
```

````

````{py:attribute} limit
:canonical: archivebox.api.v1_core.CustomPagination.Output.limit
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.CustomPagination.Output.limit
```

````

````{py:attribute} offset
:canonical: archivebox.api.v1_core.CustomPagination.Output.offset
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.CustomPagination.Output.offset
```

````

````{py:attribute} num_items
:canonical: archivebox.api.v1_core.CustomPagination.Output.num_items
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.CustomPagination.Output.num_items
```

````

````{py:attribute} items
:canonical: archivebox.api.v1_core.CustomPagination.Output.items
:type: typing.List[typing.Any]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.CustomPagination.Output.items
```

````

`````

````{py:method} paginate_queryset(queryset, pagination: Input, **params)
:canonical: archivebox.api.v1_core.CustomPagination.paginate_queryset

```{autodoc2-docstring} archivebox.api.v1_core.CustomPagination.paginate_queryset
```

````

``````

`````{py:class} MinimalArchiveResultSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema

Bases: {py:obj}`ninja.Schema`

````{py:attribute} TYPE
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.TYPE
:type: str
:value: >
   'core.models.ArchiveResult'

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.TYPE
```

````

````{py:attribute} id
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.id
:type: uuid.UUID
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.id
```

````

````{py:attribute} abid
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.abid
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.abid
```

````

````{py:attribute} created_at
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.created_at
:type: datetime.datetime | None
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.created_at
```

````

````{py:attribute} modified_at
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.modified_at
:type: datetime.datetime | None
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.modified_at
```

````

````{py:attribute} created_by_id
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.created_by_id
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.created_by_id
```

````

````{py:attribute} created_by_username
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.created_by_username
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.created_by_username
```

````

````{py:attribute} status
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.status
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.status
```

````

````{py:attribute} retry_at
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.retry_at
:type: datetime.datetime | None
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.retry_at
```

````

````{py:attribute} extractor
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.extractor
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.extractor
```

````

````{py:attribute} cmd_version
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.cmd_version
:type: str | None
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.cmd_version
```

````

````{py:attribute} cmd
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.cmd
:type: list[str] | None
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.cmd
```

````

````{py:attribute} pwd
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.pwd
:type: str | None
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.pwd
```

````

````{py:attribute} output
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.output
:type: str | None
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.output
```

````

````{py:attribute} start_ts
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.start_ts
:type: datetime.datetime | None
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.start_ts
```

````

````{py:attribute} end_ts
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.end_ts
:type: datetime.datetime | None
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.end_ts
```

````

````{py:method} resolve_created_by_id(obj)
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.resolve_created_by_id
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.resolve_created_by_id
```

````

````{py:method} resolve_created_by_username(obj) -> str
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.resolve_created_by_username
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.resolve_created_by_username
```

````

````{py:method} resolve_abid(obj)
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.resolve_abid
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.resolve_abid
```

````

````{py:method} resolve_snapshot_timestamp(obj)
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.resolve_snapshot_timestamp
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.resolve_snapshot_timestamp
```

````

````{py:method} resolve_snapshot_url(obj)
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.resolve_snapshot_url
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.resolve_snapshot_url
```

````

````{py:method} resolve_snapshot_id(obj)
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.resolve_snapshot_id
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.resolve_snapshot_id
```

````

````{py:method} resolve_snapshot_abid(obj)
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.resolve_snapshot_abid
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.resolve_snapshot_abid
```

````

````{py:method} resolve_snapshot_tags(obj)
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.resolve_snapshot_tags
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.resolve_snapshot_tags
```

````

`````

`````{py:class} ArchiveResultSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_core.ArchiveResultSchema

Bases: {py:obj}`archivebox.api.v1_core.MinimalArchiveResultSchema`

````{py:attribute} TYPE
:canonical: archivebox.api.v1_core.ArchiveResultSchema.TYPE
:type: str
:value: >
   'core.models.ArchiveResult'

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultSchema.TYPE
```

````

````{py:attribute} snapshot_id
:canonical: archivebox.api.v1_core.ArchiveResultSchema.snapshot_id
:type: uuid.UUID
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultSchema.snapshot_id
```

````

````{py:attribute} snapshot_abid
:canonical: archivebox.api.v1_core.ArchiveResultSchema.snapshot_abid
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultSchema.snapshot_abid
```

````

````{py:attribute} snapshot_timestamp
:canonical: archivebox.api.v1_core.ArchiveResultSchema.snapshot_timestamp
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultSchema.snapshot_timestamp
```

````

````{py:attribute} snapshot_url
:canonical: archivebox.api.v1_core.ArchiveResultSchema.snapshot_url
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultSchema.snapshot_url
```

````

````{py:attribute} snapshot_tags
:canonical: archivebox.api.v1_core.ArchiveResultSchema.snapshot_tags
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultSchema.snapshot_tags
```

````

`````

`````{py:class} ArchiveResultFilterSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_core.ArchiveResultFilterSchema

Bases: {py:obj}`ninja.FilterSchema`

````{py:attribute} id
:canonical: archivebox.api.v1_core.ArchiveResultFilterSchema.id
:type: typing.Optional[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultFilterSchema.id
```

````

````{py:attribute} search
:canonical: archivebox.api.v1_core.ArchiveResultFilterSchema.search
:type: typing.Optional[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultFilterSchema.search
```

````

````{py:attribute} snapshot_id
:canonical: archivebox.api.v1_core.ArchiveResultFilterSchema.snapshot_id
:type: typing.Optional[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultFilterSchema.snapshot_id
```

````

````{py:attribute} snapshot_url
:canonical: archivebox.api.v1_core.ArchiveResultFilterSchema.snapshot_url
:type: typing.Optional[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultFilterSchema.snapshot_url
```

````

````{py:attribute} snapshot_tag
:canonical: archivebox.api.v1_core.ArchiveResultFilterSchema.snapshot_tag
:type: typing.Optional[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultFilterSchema.snapshot_tag
```

````

````{py:attribute} status
:canonical: archivebox.api.v1_core.ArchiveResultFilterSchema.status
:type: typing.Optional[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultFilterSchema.status
```

````

````{py:attribute} output
:canonical: archivebox.api.v1_core.ArchiveResultFilterSchema.output
:type: typing.Optional[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultFilterSchema.output
```

````

````{py:attribute} extractor
:canonical: archivebox.api.v1_core.ArchiveResultFilterSchema.extractor
:type: typing.Optional[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultFilterSchema.extractor
```

````

````{py:attribute} cmd
:canonical: archivebox.api.v1_core.ArchiveResultFilterSchema.cmd
:type: typing.Optional[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultFilterSchema.cmd
```

````

````{py:attribute} pwd
:canonical: archivebox.api.v1_core.ArchiveResultFilterSchema.pwd
:type: typing.Optional[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultFilterSchema.pwd
```

````

````{py:attribute} cmd_version
:canonical: archivebox.api.v1_core.ArchiveResultFilterSchema.cmd_version
:type: typing.Optional[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultFilterSchema.cmd_version
```

````

````{py:attribute} created_at
:canonical: archivebox.api.v1_core.ArchiveResultFilterSchema.created_at
:type: typing.Optional[datetime.datetime]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultFilterSchema.created_at
```

````

````{py:attribute} created_at__gte
:canonical: archivebox.api.v1_core.ArchiveResultFilterSchema.created_at__gte
:type: typing.Optional[datetime.datetime]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultFilterSchema.created_at__gte
```

````

````{py:attribute} created_at__lt
:canonical: archivebox.api.v1_core.ArchiveResultFilterSchema.created_at__lt
:type: typing.Optional[datetime.datetime]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultFilterSchema.created_at__lt
```

````

`````

````{py:function} get_archiveresults(request, filters: archivebox.api.v1_core.ArchiveResultFilterSchema = Query(...))
:canonical: archivebox.api.v1_core.get_archiveresults

```{autodoc2-docstring} archivebox.api.v1_core.get_archiveresults
```
````

````{py:function} get_archiveresult(request, archiveresult_id: str)
:canonical: archivebox.api.v1_core.get_archiveresult

```{autodoc2-docstring} archivebox.api.v1_core.get_archiveresult
```
````

`````{py:class} SnapshotSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_core.SnapshotSchema

Bases: {py:obj}`ninja.Schema`

````{py:attribute} TYPE
:canonical: archivebox.api.v1_core.SnapshotSchema.TYPE
:type: str
:value: >
   'core.models.Snapshot'

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.TYPE
```

````

````{py:attribute} id
:canonical: archivebox.api.v1_core.SnapshotSchema.id
:type: uuid.UUID
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.id
```

````

````{py:attribute} abid
:canonical: archivebox.api.v1_core.SnapshotSchema.abid
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.abid
```

````

````{py:attribute} created_by_id
:canonical: archivebox.api.v1_core.SnapshotSchema.created_by_id
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.created_by_id
```

````

````{py:attribute} created_by_username
:canonical: archivebox.api.v1_core.SnapshotSchema.created_by_username
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.created_by_username
```

````

````{py:attribute} created_at
:canonical: archivebox.api.v1_core.SnapshotSchema.created_at
:type: datetime.datetime
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.created_at
```

````

````{py:attribute} modified_at
:canonical: archivebox.api.v1_core.SnapshotSchema.modified_at
:type: datetime.datetime
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.modified_at
```

````

````{py:attribute} status
:canonical: archivebox.api.v1_core.SnapshotSchema.status
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.status
```

````

````{py:attribute} retry_at
:canonical: archivebox.api.v1_core.SnapshotSchema.retry_at
:type: datetime.datetime | None
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.retry_at
```

````

````{py:attribute} bookmarked_at
:canonical: archivebox.api.v1_core.SnapshotSchema.bookmarked_at
:type: datetime.datetime
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.bookmarked_at
```

````

````{py:attribute} downloaded_at
:canonical: archivebox.api.v1_core.SnapshotSchema.downloaded_at
:type: typing.Optional[datetime.datetime]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.downloaded_at
```

````

````{py:attribute} url
:canonical: archivebox.api.v1_core.SnapshotSchema.url
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.url
```

````

````{py:attribute} tags
:canonical: archivebox.api.v1_core.SnapshotSchema.tags
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.tags
```

````

````{py:attribute} title
:canonical: archivebox.api.v1_core.SnapshotSchema.title
:type: typing.Optional[str]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.title
```

````

````{py:attribute} timestamp
:canonical: archivebox.api.v1_core.SnapshotSchema.timestamp
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.timestamp
```

````

````{py:attribute} archive_path
:canonical: archivebox.api.v1_core.SnapshotSchema.archive_path
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.archive_path
```

````

````{py:attribute} num_archiveresults
:canonical: archivebox.api.v1_core.SnapshotSchema.num_archiveresults
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.num_archiveresults
```

````

````{py:attribute} archiveresults
:canonical: archivebox.api.v1_core.SnapshotSchema.archiveresults
:type: typing.List[archivebox.api.v1_core.MinimalArchiveResultSchema]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.archiveresults
```

````

````{py:method} resolve_created_by_id(obj)
:canonical: archivebox.api.v1_core.SnapshotSchema.resolve_created_by_id
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.resolve_created_by_id
```

````

````{py:method} resolve_created_by_username(obj)
:canonical: archivebox.api.v1_core.SnapshotSchema.resolve_created_by_username
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.resolve_created_by_username
```

````

````{py:method} resolve_abid(obj)
:canonical: archivebox.api.v1_core.SnapshotSchema.resolve_abid
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.resolve_abid
```

````

````{py:method} resolve_tags(obj)
:canonical: archivebox.api.v1_core.SnapshotSchema.resolve_tags
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.resolve_tags
```

````

````{py:method} resolve_num_archiveresults(obj, context)
:canonical: archivebox.api.v1_core.SnapshotSchema.resolve_num_archiveresults
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.resolve_num_archiveresults
```

````

````{py:method} resolve_archiveresults(obj, context)
:canonical: archivebox.api.v1_core.SnapshotSchema.resolve_archiveresults
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotSchema.resolve_archiveresults
```

````

`````

`````{py:class} SnapshotFilterSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_core.SnapshotFilterSchema

Bases: {py:obj}`ninja.FilterSchema`

````{py:attribute} id
:canonical: archivebox.api.v1_core.SnapshotFilterSchema.id
:type: typing.Optional[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotFilterSchema.id
```

````

````{py:attribute} abid
:canonical: archivebox.api.v1_core.SnapshotFilterSchema.abid
:type: typing.Optional[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotFilterSchema.abid
```

````

````{py:attribute} created_by_id
:canonical: archivebox.api.v1_core.SnapshotFilterSchema.created_by_id
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotFilterSchema.created_by_id
```

````

````{py:attribute} created_by_username
:canonical: archivebox.api.v1_core.SnapshotFilterSchema.created_by_username
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotFilterSchema.created_by_username
```

````

````{py:attribute} created_at__gte
:canonical: archivebox.api.v1_core.SnapshotFilterSchema.created_at__gte
:type: datetime.datetime
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotFilterSchema.created_at__gte
```

````

````{py:attribute} created_at__lt
:canonical: archivebox.api.v1_core.SnapshotFilterSchema.created_at__lt
:type: datetime.datetime
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotFilterSchema.created_at__lt
```

````

````{py:attribute} created_at
:canonical: archivebox.api.v1_core.SnapshotFilterSchema.created_at
:type: datetime.datetime
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotFilterSchema.created_at
```

````

````{py:attribute} modified_at
:canonical: archivebox.api.v1_core.SnapshotFilterSchema.modified_at
:type: datetime.datetime
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotFilterSchema.modified_at
```

````

````{py:attribute} modified_at__gte
:canonical: archivebox.api.v1_core.SnapshotFilterSchema.modified_at__gte
:type: datetime.datetime
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotFilterSchema.modified_at__gte
```

````

````{py:attribute} modified_at__lt
:canonical: archivebox.api.v1_core.SnapshotFilterSchema.modified_at__lt
:type: datetime.datetime
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotFilterSchema.modified_at__lt
```

````

````{py:attribute} search
:canonical: archivebox.api.v1_core.SnapshotFilterSchema.search
:type: typing.Optional[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotFilterSchema.search
```

````

````{py:attribute} url
:canonical: archivebox.api.v1_core.SnapshotFilterSchema.url
:type: typing.Optional[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotFilterSchema.url
```

````

````{py:attribute} tag
:canonical: archivebox.api.v1_core.SnapshotFilterSchema.tag
:type: typing.Optional[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotFilterSchema.tag
```

````

````{py:attribute} title
:canonical: archivebox.api.v1_core.SnapshotFilterSchema.title
:type: typing.Optional[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotFilterSchema.title
```

````

````{py:attribute} timestamp
:canonical: archivebox.api.v1_core.SnapshotFilterSchema.timestamp
:type: typing.Optional[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotFilterSchema.timestamp
```

````

````{py:attribute} bookmarked_at__gte
:canonical: archivebox.api.v1_core.SnapshotFilterSchema.bookmarked_at__gte
:type: typing.Optional[datetime.datetime]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotFilterSchema.bookmarked_at__gte
```

````

````{py:attribute} bookmarked_at__lt
:canonical: archivebox.api.v1_core.SnapshotFilterSchema.bookmarked_at__lt
:type: typing.Optional[datetime.datetime]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotFilterSchema.bookmarked_at__lt
```

````

`````

````{py:function} get_snapshots(request, filters: archivebox.api.v1_core.SnapshotFilterSchema = Query(...), with_archiveresults: bool = False)
:canonical: archivebox.api.v1_core.get_snapshots

```{autodoc2-docstring} archivebox.api.v1_core.get_snapshots
```
````

````{py:function} get_snapshot(request, snapshot_id: str, with_archiveresults: bool = True)
:canonical: archivebox.api.v1_core.get_snapshot

```{autodoc2-docstring} archivebox.api.v1_core.get_snapshot
```
````

`````{py:class} TagSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_core.TagSchema

Bases: {py:obj}`ninja.Schema`

````{py:attribute} TYPE
:canonical: archivebox.api.v1_core.TagSchema.TYPE
:type: str
:value: >
   'core.models.Tag'

```{autodoc2-docstring} archivebox.api.v1_core.TagSchema.TYPE
```

````

````{py:attribute} id
:canonical: archivebox.api.v1_core.TagSchema.id
:type: uuid.UUID
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.TagSchema.id
```

````

````{py:attribute} abid
:canonical: archivebox.api.v1_core.TagSchema.abid
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.TagSchema.abid
```

````

````{py:attribute} modified_at
:canonical: archivebox.api.v1_core.TagSchema.modified_at
:type: datetime.datetime
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.TagSchema.modified_at
```

````

````{py:attribute} created_at
:canonical: archivebox.api.v1_core.TagSchema.created_at
:type: datetime.datetime
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.TagSchema.created_at
```

````

````{py:attribute} created_by_id
:canonical: archivebox.api.v1_core.TagSchema.created_by_id
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.TagSchema.created_by_id
```

````

````{py:attribute} created_by_username
:canonical: archivebox.api.v1_core.TagSchema.created_by_username
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.TagSchema.created_by_username
```

````

````{py:attribute} name
:canonical: archivebox.api.v1_core.TagSchema.name
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.TagSchema.name
```

````

````{py:attribute} slug
:canonical: archivebox.api.v1_core.TagSchema.slug
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.TagSchema.slug
```

````

````{py:attribute} num_snapshots
:canonical: archivebox.api.v1_core.TagSchema.num_snapshots
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.TagSchema.num_snapshots
```

````

````{py:attribute} snapshots
:canonical: archivebox.api.v1_core.TagSchema.snapshots
:type: typing.List[archivebox.api.v1_core.SnapshotSchema]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.TagSchema.snapshots
```

````

````{py:method} resolve_created_by_id(obj)
:canonical: archivebox.api.v1_core.TagSchema.resolve_created_by_id
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.TagSchema.resolve_created_by_id
```

````

````{py:method} resolve_created_by_username(obj)
:canonical: archivebox.api.v1_core.TagSchema.resolve_created_by_username
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.TagSchema.resolve_created_by_username
```

````

````{py:method} resolve_num_snapshots(obj, context)
:canonical: archivebox.api.v1_core.TagSchema.resolve_num_snapshots
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.TagSchema.resolve_num_snapshots
```

````

````{py:method} resolve_snapshots(obj, context)
:canonical: archivebox.api.v1_core.TagSchema.resolve_snapshots
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.TagSchema.resolve_snapshots
```

````

`````

````{py:function} get_tags(request)
:canonical: archivebox.api.v1_core.get_tags

```{autodoc2-docstring} archivebox.api.v1_core.get_tags
```
````

````{py:function} get_tag(request, tag_id: str, with_snapshots: bool = True)
:canonical: archivebox.api.v1_core.get_tag

```{autodoc2-docstring} archivebox.api.v1_core.get_tag
```
````

`````{py:class} SeedSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_core.SeedSchema

Bases: {py:obj}`ninja.Schema`

````{py:attribute} TYPE
:canonical: archivebox.api.v1_core.SeedSchema.TYPE
:type: str
:value: >
   'seeds.models.Seed'

```{autodoc2-docstring} archivebox.api.v1_core.SeedSchema.TYPE
```

````

````{py:attribute} id
:canonical: archivebox.api.v1_core.SeedSchema.id
:type: uuid.UUID
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SeedSchema.id
```

````

````{py:attribute} abid
:canonical: archivebox.api.v1_core.SeedSchema.abid
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SeedSchema.abid
```

````

````{py:attribute} modified_at
:canonical: archivebox.api.v1_core.SeedSchema.modified_at
:type: datetime.datetime
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SeedSchema.modified_at
```

````

````{py:attribute} created_at
:canonical: archivebox.api.v1_core.SeedSchema.created_at
:type: datetime.datetime
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SeedSchema.created_at
```

````

````{py:attribute} created_by_id
:canonical: archivebox.api.v1_core.SeedSchema.created_by_id
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SeedSchema.created_by_id
```

````

````{py:attribute} created_by_username
:canonical: archivebox.api.v1_core.SeedSchema.created_by_username
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SeedSchema.created_by_username
```

````

````{py:attribute} uri
:canonical: archivebox.api.v1_core.SeedSchema.uri
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SeedSchema.uri
```

````

````{py:attribute} tags_str
:canonical: archivebox.api.v1_core.SeedSchema.tags_str
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SeedSchema.tags_str
```

````

````{py:attribute} config
:canonical: archivebox.api.v1_core.SeedSchema.config
:type: dict
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SeedSchema.config
```

````

````{py:method} resolve_created_by_id(obj)
:canonical: archivebox.api.v1_core.SeedSchema.resolve_created_by_id
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.SeedSchema.resolve_created_by_id
```

````

````{py:method} resolve_created_by_username(obj)
:canonical: archivebox.api.v1_core.SeedSchema.resolve_created_by_username
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.SeedSchema.resolve_created_by_username
```

````

`````

````{py:function} get_seeds(request)
:canonical: archivebox.api.v1_core.get_seeds

```{autodoc2-docstring} archivebox.api.v1_core.get_seeds
```
````

````{py:function} get_seed(request, seed_id: str)
:canonical: archivebox.api.v1_core.get_seed

```{autodoc2-docstring} archivebox.api.v1_core.get_seed
```
````

`````{py:class} CrawlSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_core.CrawlSchema

Bases: {py:obj}`ninja.Schema`

````{py:attribute} TYPE
:canonical: archivebox.api.v1_core.CrawlSchema.TYPE
:type: str
:value: >
   'core.models.Crawl'

```{autodoc2-docstring} archivebox.api.v1_core.CrawlSchema.TYPE
```

````

````{py:attribute} id
:canonical: archivebox.api.v1_core.CrawlSchema.id
:type: uuid.UUID
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.CrawlSchema.id
```

````

````{py:attribute} abid
:canonical: archivebox.api.v1_core.CrawlSchema.abid
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.CrawlSchema.abid
```

````

````{py:attribute} modified_at
:canonical: archivebox.api.v1_core.CrawlSchema.modified_at
:type: datetime.datetime
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.CrawlSchema.modified_at
```

````

````{py:attribute} created_at
:canonical: archivebox.api.v1_core.CrawlSchema.created_at
:type: datetime.datetime
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.CrawlSchema.created_at
```

````

````{py:attribute} created_by_id
:canonical: archivebox.api.v1_core.CrawlSchema.created_by_id
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.CrawlSchema.created_by_id
```

````

````{py:attribute} created_by_username
:canonical: archivebox.api.v1_core.CrawlSchema.created_by_username
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.CrawlSchema.created_by_username
```

````

````{py:attribute} status
:canonical: archivebox.api.v1_core.CrawlSchema.status
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.CrawlSchema.status
```

````

````{py:attribute} retry_at
:canonical: archivebox.api.v1_core.CrawlSchema.retry_at
:type: datetime.datetime | None
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.CrawlSchema.retry_at
```

````

````{py:attribute} seed
:canonical: archivebox.api.v1_core.CrawlSchema.seed
:type: archivebox.api.v1_core.SeedSchema
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.CrawlSchema.seed
```

````

````{py:attribute} max_depth
:canonical: archivebox.api.v1_core.CrawlSchema.max_depth
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.CrawlSchema.max_depth
```

````

````{py:method} resolve_created_by_id(obj)
:canonical: archivebox.api.v1_core.CrawlSchema.resolve_created_by_id
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.CrawlSchema.resolve_created_by_id
```

````

````{py:method} resolve_created_by_username(obj)
:canonical: archivebox.api.v1_core.CrawlSchema.resolve_created_by_username
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.CrawlSchema.resolve_created_by_username
```

````

````{py:method} resolve_snapshots(obj, context)
:canonical: archivebox.api.v1_core.CrawlSchema.resolve_snapshots
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.CrawlSchema.resolve_snapshots
```

````

`````

````{py:function} get_crawls(request)
:canonical: archivebox.api.v1_core.get_crawls

```{autodoc2-docstring} archivebox.api.v1_core.get_crawls
```
````

````{py:function} get_crawl(request, crawl_id: str, with_snapshots: bool = False, with_archiveresults: bool = False)
:canonical: archivebox.api.v1_core.get_crawl

```{autodoc2-docstring} archivebox.api.v1_core.get_crawl
```
````

````{py:function} get_any(request, abid: str)
:canonical: archivebox.api.v1_core.get_any

```{autodoc2-docstring} archivebox.api.v1_core.get_any
```
````
