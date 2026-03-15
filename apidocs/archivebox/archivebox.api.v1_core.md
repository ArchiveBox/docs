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
* - {py:obj}`SnapshotUpdateSchema <archivebox.api.v1_core.SnapshotUpdateSchema>`
  -
* - {py:obj}`SnapshotFilterSchema <archivebox.api.v1_core.SnapshotFilterSchema>`
  -
* - {py:obj}`TagSchema <archivebox.api.v1_core.TagSchema>`
  -
* - {py:obj}`TagAutocompleteSchema <archivebox.api.v1_core.TagAutocompleteSchema>`
  -
* - {py:obj}`TagCreateSchema <archivebox.api.v1_core.TagCreateSchema>`
  -
* - {py:obj}`TagCreateResponseSchema <archivebox.api.v1_core.TagCreateResponseSchema>`
  -
* - {py:obj}`TagSnapshotRequestSchema <archivebox.api.v1_core.TagSnapshotRequestSchema>`
  -
* - {py:obj}`TagSnapshotResponseSchema <archivebox.api.v1_core.TagSnapshotResponseSchema>`
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
* - {py:obj}`patch_snapshot <archivebox.api.v1_core.patch_snapshot>`
  - ```{autodoc2-docstring} archivebox.api.v1_core.patch_snapshot
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
* - {py:obj}`get_any <archivebox.api.v1_core.get_any>`
  - ```{autodoc2-docstring} archivebox.api.v1_core.get_any
    :summary:
    ```
* - {py:obj}`tags_autocomplete <archivebox.api.v1_core.tags_autocomplete>`
  - ```{autodoc2-docstring} archivebox.api.v1_core.tags_autocomplete
    :summary:
    ```
* - {py:obj}`tags_create <archivebox.api.v1_core.tags_create>`
  - ```{autodoc2-docstring} archivebox.api.v1_core.tags_create
    :summary:
    ```
* - {py:obj}`tags_add_to_snapshot <archivebox.api.v1_core.tags_add_to_snapshot>`
  - ```{autodoc2-docstring} archivebox.api.v1_core.tags_add_to_snapshot
    :summary:
    ```
* - {py:obj}`tags_remove_from_snapshot <archivebox.api.v1_core.tags_remove_from_snapshot>`
  - ```{autodoc2-docstring} archivebox.api.v1_core.tags_remove_from_snapshot
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

````{py:attribute} plugin
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.plugin
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.plugin
```

````

````{py:attribute} hook_name
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.hook_name
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.hook_name
```

````

````{py:attribute} process_id
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.process_id
:type: uuid.UUID | None
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.process_id
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

````{py:attribute} output_str
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.output_str
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.output_str
```

````

````{py:attribute} output_json
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.output_json
:type: dict | None
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.output_json
```

````

````{py:attribute} output_files
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.output_files
:type: dict | None
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.output_files
```

````

````{py:attribute} output_size
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.output_size
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.output_size
```

````

````{py:attribute} output_mimetypes
:canonical: archivebox.api.v1_core.MinimalArchiveResultSchema.output_mimetypes
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.MinimalArchiveResultSchema.output_mimetypes
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

````{py:method} resolve_snapshot_timestamp(obj)
:canonical: archivebox.api.v1_core.ArchiveResultSchema.resolve_snapshot_timestamp
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultSchema.resolve_snapshot_timestamp
```

````

````{py:method} resolve_snapshot_url(obj)
:canonical: archivebox.api.v1_core.ArchiveResultSchema.resolve_snapshot_url
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultSchema.resolve_snapshot_url
```

````

````{py:method} resolve_snapshot_id(obj)
:canonical: archivebox.api.v1_core.ArchiveResultSchema.resolve_snapshot_id
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultSchema.resolve_snapshot_id
```

````

````{py:method} resolve_snapshot_tags(obj)
:canonical: archivebox.api.v1_core.ArchiveResultSchema.resolve_snapshot_tags
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultSchema.resolve_snapshot_tags
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

````{py:attribute} output_str
:canonical: archivebox.api.v1_core.ArchiveResultFilterSchema.output_str
:type: typing.Optional[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultFilterSchema.output_str
```

````

````{py:attribute} plugin
:canonical: archivebox.api.v1_core.ArchiveResultFilterSchema.plugin
:type: typing.Optional[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultFilterSchema.plugin
```

````

````{py:attribute} hook_name
:canonical: archivebox.api.v1_core.ArchiveResultFilterSchema.hook_name
:type: typing.Optional[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultFilterSchema.hook_name
```

````

````{py:attribute} process_id
:canonical: archivebox.api.v1_core.ArchiveResultFilterSchema.process_id
:type: typing.Optional[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.api.v1_core.ArchiveResultFilterSchema.process_id
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

`````{py:class} SnapshotUpdateSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_core.SnapshotUpdateSchema

Bases: {py:obj}`ninja.Schema`

````{py:attribute} status
:canonical: archivebox.api.v1_core.SnapshotUpdateSchema.status
:type: str | None
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotUpdateSchema.status
```

````

````{py:attribute} retry_at
:canonical: archivebox.api.v1_core.SnapshotUpdateSchema.retry_at
:type: datetime.datetime | None
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.SnapshotUpdateSchema.retry_at
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

````{py:function} patch_snapshot(request, snapshot_id: str, data: archivebox.api.v1_core.SnapshotUpdateSchema)
:canonical: archivebox.api.v1_core.patch_snapshot

```{autodoc2-docstring} archivebox.api.v1_core.patch_snapshot
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

````{py:function} get_any(request, id: str)
:canonical: archivebox.api.v1_core.get_any

```{autodoc2-docstring} archivebox.api.v1_core.get_any
```
````

`````{py:class} TagAutocompleteSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_core.TagAutocompleteSchema

Bases: {py:obj}`ninja.Schema`

````{py:attribute} tags
:canonical: archivebox.api.v1_core.TagAutocompleteSchema.tags
:type: typing.List[dict]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.TagAutocompleteSchema.tags
```

````

`````

`````{py:class} TagCreateSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_core.TagCreateSchema

Bases: {py:obj}`ninja.Schema`

````{py:attribute} name
:canonical: archivebox.api.v1_core.TagCreateSchema.name
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.TagCreateSchema.name
```

````

`````

`````{py:class} TagCreateResponseSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_core.TagCreateResponseSchema

Bases: {py:obj}`ninja.Schema`

````{py:attribute} success
:canonical: archivebox.api.v1_core.TagCreateResponseSchema.success
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.TagCreateResponseSchema.success
```

````

````{py:attribute} tag_id
:canonical: archivebox.api.v1_core.TagCreateResponseSchema.tag_id
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.TagCreateResponseSchema.tag_id
```

````

````{py:attribute} tag_name
:canonical: archivebox.api.v1_core.TagCreateResponseSchema.tag_name
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.TagCreateResponseSchema.tag_name
```

````

````{py:attribute} created
:canonical: archivebox.api.v1_core.TagCreateResponseSchema.created
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.TagCreateResponseSchema.created
```

````

`````

`````{py:class} TagSnapshotRequestSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_core.TagSnapshotRequestSchema

Bases: {py:obj}`ninja.Schema`

````{py:attribute} snapshot_id
:canonical: archivebox.api.v1_core.TagSnapshotRequestSchema.snapshot_id
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.TagSnapshotRequestSchema.snapshot_id
```

````

````{py:attribute} tag_name
:canonical: archivebox.api.v1_core.TagSnapshotRequestSchema.tag_name
:type: typing.Optional[str]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.TagSnapshotRequestSchema.tag_name
```

````

````{py:attribute} tag_id
:canonical: archivebox.api.v1_core.TagSnapshotRequestSchema.tag_id
:type: typing.Optional[int]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.TagSnapshotRequestSchema.tag_id
```

````

`````

`````{py:class} TagSnapshotResponseSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_core.TagSnapshotResponseSchema

Bases: {py:obj}`ninja.Schema`

````{py:attribute} success
:canonical: archivebox.api.v1_core.TagSnapshotResponseSchema.success
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.TagSnapshotResponseSchema.success
```

````

````{py:attribute} tag_id
:canonical: archivebox.api.v1_core.TagSnapshotResponseSchema.tag_id
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.TagSnapshotResponseSchema.tag_id
```

````

````{py:attribute} tag_name
:canonical: archivebox.api.v1_core.TagSnapshotResponseSchema.tag_name
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_core.TagSnapshotResponseSchema.tag_name
```

````

`````

````{py:function} tags_autocomplete(request, q: str = '')
:canonical: archivebox.api.v1_core.tags_autocomplete

```{autodoc2-docstring} archivebox.api.v1_core.tags_autocomplete
```
````

````{py:function} tags_create(request, data: archivebox.api.v1_core.TagCreateSchema)
:canonical: archivebox.api.v1_core.tags_create

```{autodoc2-docstring} archivebox.api.v1_core.tags_create
```
````

````{py:function} tags_add_to_snapshot(request, data: archivebox.api.v1_core.TagSnapshotRequestSchema)
:canonical: archivebox.api.v1_core.tags_add_to_snapshot

```{autodoc2-docstring} archivebox.api.v1_core.tags_add_to_snapshot
```
````

````{py:function} tags_remove_from_snapshot(request, data: archivebox.api.v1_core.TagSnapshotRequestSchema)
:canonical: archivebox.api.v1_core.tags_remove_from_snapshot

```{autodoc2-docstring} archivebox.api.v1_core.tags_remove_from_snapshot
```
````
