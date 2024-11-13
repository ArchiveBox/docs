# {py:mod}`archivebox.core.models`

```{py:module} archivebox.core.models
```

```{autodoc2-docstring} archivebox.core.models
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Tag <archivebox.core.models.Tag>`
  - ```{autodoc2-docstring} archivebox.core.models.Tag
    :summary:
    ```
* - {py:obj}`SnapshotTag <archivebox.core.models.SnapshotTag>`
  -
* - {py:obj}`SnapshotManager <archivebox.core.models.SnapshotManager>`
  - ```{autodoc2-docstring} archivebox.core.models.SnapshotManager
    :summary:
    ```
* - {py:obj}`Snapshot <archivebox.core.models.Snapshot>`
  -
* - {py:obj}`ArchiveResultManager <archivebox.core.models.ArchiveResultManager>`
  - ```{autodoc2-docstring} archivebox.core.models.ArchiveResultManager
    :summary:
    ```
* - {py:obj}`ArchiveResult <archivebox.core.models.ArchiveResult>`
  -
````

### API

``````{py:class} Tag(*args: typing.Any, **kwargs: typing.Any)
:canonical: archivebox.core.models.Tag

Bases: {py:obj}`abid_utils.models.ABIDModel`

```{autodoc2-docstring} archivebox.core.models.Tag
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.core.models.Tag.__init__
```

````{py:attribute} abid_prefix
:canonical: archivebox.core.models.Tag.abid_prefix
:value: >
   'tag_'

```{autodoc2-docstring} archivebox.core.models.Tag.abid_prefix
```

````

````{py:attribute} abid_ts_src
:canonical: archivebox.core.models.Tag.abid_ts_src
:value: >
   'self.created_at'

```{autodoc2-docstring} archivebox.core.models.Tag.abid_ts_src
```

````

````{py:attribute} abid_uri_src
:canonical: archivebox.core.models.Tag.abid_uri_src
:value: >
   'self.slug'

```{autodoc2-docstring} archivebox.core.models.Tag.abid_uri_src
```

````

````{py:attribute} abid_subtype_src
:canonical: archivebox.core.models.Tag.abid_subtype_src
:value: >
   '"03"'

```{autodoc2-docstring} archivebox.core.models.Tag.abid_subtype_src
```

````

````{py:attribute} abid_rand_src
:canonical: archivebox.core.models.Tag.abid_rand_src
:value: >
   'self.id'

```{autodoc2-docstring} archivebox.core.models.Tag.abid_rand_src
```

````

````{py:attribute} abid_drift_allowed
:canonical: archivebox.core.models.Tag.abid_drift_allowed
:value: >
   True

```{autodoc2-docstring} archivebox.core.models.Tag.abid_drift_allowed
```

````

````{py:attribute} id
:canonical: archivebox.core.models.Tag.id
:value: >
   'UUIDField(...)'

```{autodoc2-docstring} archivebox.core.models.Tag.id
```

````

````{py:attribute} abid
:canonical: archivebox.core.models.Tag.abid
:value: >
   'ABIDField(...)'

```{autodoc2-docstring} archivebox.core.models.Tag.abid
```

````

````{py:attribute} created_by
:canonical: archivebox.core.models.Tag.created_by
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.core.models.Tag.created_by
```

````

````{py:attribute} created_at
:canonical: archivebox.core.models.Tag.created_at
:value: >
   'AutoDateTimeField(...)'

```{autodoc2-docstring} archivebox.core.models.Tag.created_at
```

````

````{py:attribute} modified_at
:canonical: archivebox.core.models.Tag.modified_at
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.core.models.Tag.modified_at
```

````

````{py:attribute} name
:canonical: archivebox.core.models.Tag.name
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.models.Tag.name
```

````

````{py:attribute} slug
:canonical: archivebox.core.models.Tag.slug
:value: >
   'SlugField(...)'

```{autodoc2-docstring} archivebox.core.models.Tag.slug
```

````

````{py:attribute} snapshot_set
:canonical: archivebox.core.models.Tag.snapshot_set
:type: django.db.models.Manager[Snapshot]
:value: >
   None

```{autodoc2-docstring} archivebox.core.models.Tag.snapshot_set
```

````

`````{py:class} Meta
:canonical: archivebox.core.models.Tag.Meta

Bases: {py:obj}`django_stubs_ext.db.models.TypedModelMeta`

````{py:attribute} verbose_name
:canonical: archivebox.core.models.Tag.Meta.verbose_name
:value: >
   'Tag'

```{autodoc2-docstring} archivebox.core.models.Tag.Meta.verbose_name
```

````

````{py:attribute} verbose_name_plural
:canonical: archivebox.core.models.Tag.Meta.verbose_name_plural
:value: >
   'Tags'

```{autodoc2-docstring} archivebox.core.models.Tag.Meta.verbose_name_plural
```

````

`````

````{py:method} __str__()
:canonical: archivebox.core.models.Tag.__str__

````

````{py:method} slugify(tag, i=None)
:canonical: archivebox.core.models.Tag.slugify

```{autodoc2-docstring} archivebox.core.models.Tag.slugify
```

````

````{py:method} clean(*args, **kwargs)
:canonical: archivebox.core.models.Tag.clean

````

````{py:method} save(*args, **kwargs)
:canonical: archivebox.core.models.Tag.save

````

````{py:property} api_url
:canonical: archivebox.core.models.Tag.api_url
:type: str

````

````{py:property} api_docs_url
:canonical: archivebox.core.models.Tag.api_docs_url
:type: str

````

``````

``````{py:class} SnapshotTag(*args, **kwargs)
:canonical: archivebox.core.models.SnapshotTag

Bases: {py:obj}`django.db.models.Model`

````{py:attribute} id
:canonical: archivebox.core.models.SnapshotTag.id
:value: >
   'AutoField(...)'

```{autodoc2-docstring} archivebox.core.models.SnapshotTag.id
```

````

````{py:attribute} snapshot
:canonical: archivebox.core.models.SnapshotTag.snapshot
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.core.models.SnapshotTag.snapshot
```

````

````{py:attribute} tag
:canonical: archivebox.core.models.SnapshotTag.tag
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.core.models.SnapshotTag.tag
```

````

`````{py:class} Meta
:canonical: archivebox.core.models.SnapshotTag.Meta

```{autodoc2-docstring} archivebox.core.models.SnapshotTag.Meta
```

````{py:attribute} db_table
:canonical: archivebox.core.models.SnapshotTag.Meta.db_table
:value: >
   'core_snapshot_tags'

```{autodoc2-docstring} archivebox.core.models.SnapshotTag.Meta.db_table
```

````

````{py:attribute} unique_together
:canonical: archivebox.core.models.SnapshotTag.Meta.unique_together
:value: >
   [('snapshot', 'tag')]

```{autodoc2-docstring} archivebox.core.models.SnapshotTag.Meta.unique_together
```

````

`````

``````

`````{py:class} SnapshotManager
:canonical: archivebox.core.models.SnapshotManager

Bases: {py:obj}`django.db.models.Manager`

```{autodoc2-docstring} archivebox.core.models.SnapshotManager
```

````{py:method} get_queryset()
:canonical: archivebox.core.models.SnapshotManager.get_queryset

```{autodoc2-docstring} archivebox.core.models.SnapshotManager.get_queryset
```

````

`````

`````{py:class} Snapshot(*args: typing.Any, **kwargs: typing.Any)
:canonical: archivebox.core.models.Snapshot

Bases: {py:obj}`abid_utils.models.ABIDModel`, {py:obj}`actors.models.ModelWithStateMachine`

````{py:attribute} abid_prefix
:canonical: archivebox.core.models.Snapshot.abid_prefix
:value: >
   'snp_'

```{autodoc2-docstring} archivebox.core.models.Snapshot.abid_prefix
```

````

````{py:attribute} abid_ts_src
:canonical: archivebox.core.models.Snapshot.abid_ts_src
:value: >
   'self.created_at'

```{autodoc2-docstring} archivebox.core.models.Snapshot.abid_ts_src
```

````

````{py:attribute} abid_uri_src
:canonical: archivebox.core.models.Snapshot.abid_uri_src
:value: >
   'self.url'

```{autodoc2-docstring} archivebox.core.models.Snapshot.abid_uri_src
```

````

````{py:attribute} abid_subtype_src
:canonical: archivebox.core.models.Snapshot.abid_subtype_src
:value: >
   '"01"'

```{autodoc2-docstring} archivebox.core.models.Snapshot.abid_subtype_src
```

````

````{py:attribute} abid_rand_src
:canonical: archivebox.core.models.Snapshot.abid_rand_src
:value: >
   'self.id'

```{autodoc2-docstring} archivebox.core.models.Snapshot.abid_rand_src
```

````

````{py:attribute} abid_drift_allowed
:canonical: archivebox.core.models.Snapshot.abid_drift_allowed
:value: >
   True

```{autodoc2-docstring} archivebox.core.models.Snapshot.abid_drift_allowed
```

````

````{py:attribute} state_machine_name
:canonical: archivebox.core.models.Snapshot.state_machine_name
:value: >
   'core.statemachines.SnapshotMachine'

```{autodoc2-docstring} archivebox.core.models.Snapshot.state_machine_name
```

````

````{py:attribute} state_field_name
:canonical: archivebox.core.models.Snapshot.state_field_name
:value: >
   'status'

```{autodoc2-docstring} archivebox.core.models.Snapshot.state_field_name
```

````

````{py:attribute} retry_at_field_name
:canonical: archivebox.core.models.Snapshot.retry_at_field_name
:value: >
   'retry_at'

```{autodoc2-docstring} archivebox.core.models.Snapshot.retry_at_field_name
```

````

````{py:attribute} StatusChoices
:canonical: archivebox.core.models.Snapshot.StatusChoices
:value: >
   None

```{autodoc2-docstring} archivebox.core.models.Snapshot.StatusChoices
```

````

````{py:attribute} active_state
:canonical: archivebox.core.models.Snapshot.active_state
:value: >
   None

```{autodoc2-docstring} archivebox.core.models.Snapshot.active_state
```

````

````{py:attribute} id
:canonical: archivebox.core.models.Snapshot.id
:value: >
   'UUIDField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.id
```

````

````{py:attribute} abid
:canonical: archivebox.core.models.Snapshot.abid
:value: >
   'ABIDField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.abid
```

````

````{py:attribute} created_by
:canonical: archivebox.core.models.Snapshot.created_by
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.created_by
```

````

````{py:attribute} created_at
:canonical: archivebox.core.models.Snapshot.created_at
:value: >
   'AutoDateTimeField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.created_at
```

````

````{py:attribute} modified_at
:canonical: archivebox.core.models.Snapshot.modified_at
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.modified_at
```

````

````{py:attribute} status
:canonical: archivebox.core.models.Snapshot.status
:value: >
   'StatusField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.status
```

````

````{py:attribute} retry_at
:canonical: archivebox.core.models.Snapshot.retry_at
:value: >
   'RetryAtField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.retry_at
```

````

````{py:attribute} bookmarked_at
:canonical: archivebox.core.models.Snapshot.bookmarked_at
:value: >
   'AutoDateTimeField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.bookmarked_at
```

````

````{py:attribute} downloaded_at
:canonical: archivebox.core.models.Snapshot.downloaded_at
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.downloaded_at
```

````

````{py:attribute} crawl
:canonical: archivebox.core.models.Snapshot.crawl
:type: crawls.models.Crawl
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.crawl
```

````

````{py:attribute} url
:canonical: archivebox.core.models.Snapshot.url
:value: >
   'URLField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.url
```

````

````{py:attribute} timestamp
:canonical: archivebox.core.models.Snapshot.timestamp
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.timestamp
```

````

````{py:attribute} tags
:canonical: archivebox.core.models.Snapshot.tags
:value: >
   'ManyToManyField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.tags
```

````

````{py:attribute} title
:canonical: archivebox.core.models.Snapshot.title
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.title
```

````

````{py:attribute} keys
:canonical: archivebox.core.models.Snapshot.keys
:value: >
   ('url', 'timestamp', 'title', 'tags', 'downloaded_at')

```{autodoc2-docstring} archivebox.core.models.Snapshot.keys
```

````

````{py:attribute} archiveresult_set
:canonical: archivebox.core.models.Snapshot.archiveresult_set
:type: django.db.models.Manager[ArchiveResult]
:value: >
   None

```{autodoc2-docstring} archivebox.core.models.Snapshot.archiveresult_set
```

````

````{py:attribute} objects
:canonical: archivebox.core.models.Snapshot.objects
:value: >
   'SnapshotManager(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.objects
```

````

````{py:method} save(*args, **kwargs)
:canonical: archivebox.core.models.Snapshot.save

````

````{py:method} archive(overwrite=False, methods=None)
:canonical: archivebox.core.models.Snapshot.archive

```{autodoc2-docstring} archivebox.core.models.Snapshot.archive
```

````

````{py:method} __repr__() -> str
:canonical: archivebox.core.models.Snapshot.__repr__

````

````{py:method} __str__() -> str
:canonical: archivebox.core.models.Snapshot.__str__

````

````{py:method} from_json(info: dict)
:canonical: archivebox.core.models.Snapshot.from_json
:classmethod:

```{autodoc2-docstring} archivebox.core.models.Snapshot.from_json
```

````

````{py:method} as_json(*args) -> dict
:canonical: archivebox.core.models.Snapshot.as_json

```{autodoc2-docstring} archivebox.core.models.Snapshot.as_json
```

````

````{py:method} as_link() -> archivebox.index.schema.Link
:canonical: archivebox.core.models.Snapshot.as_link

```{autodoc2-docstring} archivebox.core.models.Snapshot.as_link
```

````

````{py:method} as_link_with_details() -> archivebox.index.schema.Link
:canonical: archivebox.core.models.Snapshot.as_link_with_details

```{autodoc2-docstring} archivebox.core.models.Snapshot.as_link_with_details
```

````

````{py:method} tags_str(nocache=True) -> str | None
:canonical: archivebox.core.models.Snapshot.tags_str

```{autodoc2-docstring} archivebox.core.models.Snapshot.tags_str
```

````

````{py:method} icons() -> str
:canonical: archivebox.core.models.Snapshot.icons

```{autodoc2-docstring} archivebox.core.models.Snapshot.icons
```

````

````{py:property} api_url
:canonical: archivebox.core.models.Snapshot.api_url
:type: str

````

````{py:property} api_docs_url
:canonical: archivebox.core.models.Snapshot.api_docs_url
:type: str

````

````{py:method} get_absolute_url()
:canonical: archivebox.core.models.Snapshot.get_absolute_url

```{autodoc2-docstring} archivebox.core.models.Snapshot.get_absolute_url
```

````

````{py:method} title_stripped() -> str
:canonical: archivebox.core.models.Snapshot.title_stripped

```{autodoc2-docstring} archivebox.core.models.Snapshot.title_stripped
```

````

````{py:method} extension() -> str
:canonical: archivebox.core.models.Snapshot.extension

```{autodoc2-docstring} archivebox.core.models.Snapshot.extension
```

````

````{py:method} bookmarked()
:canonical: archivebox.core.models.Snapshot.bookmarked

```{autodoc2-docstring} archivebox.core.models.Snapshot.bookmarked
```

````

````{py:method} bookmarked_date()
:canonical: archivebox.core.models.Snapshot.bookmarked_date

```{autodoc2-docstring} archivebox.core.models.Snapshot.bookmarked_date
```

````

````{py:method} is_archived()
:canonical: archivebox.core.models.Snapshot.is_archived

```{autodoc2-docstring} archivebox.core.models.Snapshot.is_archived
```

````

````{py:method} num_outputs() -> int
:canonical: archivebox.core.models.Snapshot.num_outputs

```{autodoc2-docstring} archivebox.core.models.Snapshot.num_outputs
```

````

````{py:method} base_url()
:canonical: archivebox.core.models.Snapshot.base_url

```{autodoc2-docstring} archivebox.core.models.Snapshot.base_url
```

````

````{py:method} link_dir()
:canonical: archivebox.core.models.Snapshot.link_dir

```{autodoc2-docstring} archivebox.core.models.Snapshot.link_dir
```

````

````{py:method} archive_path()
:canonical: archivebox.core.models.Snapshot.archive_path

```{autodoc2-docstring} archivebox.core.models.Snapshot.archive_path
```

````

````{py:method} archive_size()
:canonical: archivebox.core.models.Snapshot.archive_size

```{autodoc2-docstring} archivebox.core.models.Snapshot.archive_size
```

````

````{py:method} thumbnail_url() -> typing.Optional[str]
:canonical: archivebox.core.models.Snapshot.thumbnail_url

```{autodoc2-docstring} archivebox.core.models.Snapshot.thumbnail_url
```

````

````{py:method} headers() -> typing.Optional[typing.Dict[str, str]]
:canonical: archivebox.core.models.Snapshot.headers

```{autodoc2-docstring} archivebox.core.models.Snapshot.headers
```

````

````{py:method} status_code() -> typing.Optional[str]
:canonical: archivebox.core.models.Snapshot.status_code

```{autodoc2-docstring} archivebox.core.models.Snapshot.status_code
```

````

````{py:method} history() -> dict
:canonical: archivebox.core.models.Snapshot.history

```{autodoc2-docstring} archivebox.core.models.Snapshot.history
```

````

````{py:method} latest_title() -> typing.Optional[str]
:canonical: archivebox.core.models.Snapshot.latest_title

```{autodoc2-docstring} archivebox.core.models.Snapshot.latest_title
```

````

````{py:method} save_tags(tags: typing.Iterable[str] = ()) -> None
:canonical: archivebox.core.models.Snapshot.save_tags

```{autodoc2-docstring} archivebox.core.models.Snapshot.save_tags
```

````

````{py:method} has_pending_archiveresults() -> bool
:canonical: archivebox.core.models.Snapshot.has_pending_archiveresults

```{autodoc2-docstring} archivebox.core.models.Snapshot.has_pending_archiveresults
```

````

````{py:method} create_pending_archiveresults() -> list[archivebox.core.models.ArchiveResult]
:canonical: archivebox.core.models.Snapshot.create_pending_archiveresults

```{autodoc2-docstring} archivebox.core.models.Snapshot.create_pending_archiveresults
```

````

`````

`````{py:class} ArchiveResultManager
:canonical: archivebox.core.models.ArchiveResultManager

Bases: {py:obj}`django.db.models.Manager`

```{autodoc2-docstring} archivebox.core.models.ArchiveResultManager
```

````{py:method} indexable(sorted: bool = True)
:canonical: archivebox.core.models.ArchiveResultManager.indexable

```{autodoc2-docstring} archivebox.core.models.ArchiveResultManager.indexable
```

````

`````

``````{py:class} ArchiveResult(*args: typing.Any, **kwargs: typing.Any)
:canonical: archivebox.core.models.ArchiveResult

Bases: {py:obj}`abid_utils.models.ABIDModel`, {py:obj}`actors.models.ModelWithStateMachine`

````{py:attribute} abid_prefix
:canonical: archivebox.core.models.ArchiveResult.abid_prefix
:value: >
   'res_'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.abid_prefix
```

````

````{py:attribute} abid_ts_src
:canonical: archivebox.core.models.ArchiveResult.abid_ts_src
:value: >
   'self.snapshot.created_at'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.abid_ts_src
```

````

````{py:attribute} abid_uri_src
:canonical: archivebox.core.models.ArchiveResult.abid_uri_src
:value: >
   'self.snapshot.url'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.abid_uri_src
```

````

````{py:attribute} abid_subtype_src
:canonical: archivebox.core.models.ArchiveResult.abid_subtype_src
:value: >
   'self.extractor'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.abid_subtype_src
```

````

````{py:attribute} abid_rand_src
:canonical: archivebox.core.models.ArchiveResult.abid_rand_src
:value: >
   'self.id'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.abid_rand_src
```

````

````{py:attribute} abid_drift_allowed
:canonical: archivebox.core.models.ArchiveResult.abid_drift_allowed
:value: >
   True

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.abid_drift_allowed
```

````

`````{py:class} StatusChoices(*args, **kwds)
:canonical: archivebox.core.models.ArchiveResult.StatusChoices

Bases: {py:obj}`django.db.models.TextChoices`

````{py:attribute} QUEUED
:canonical: archivebox.core.models.ArchiveResult.StatusChoices.QUEUED
:value: >
   ('queued', 'Queued')

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.StatusChoices.QUEUED
```

````

````{py:attribute} STARTED
:canonical: archivebox.core.models.ArchiveResult.StatusChoices.STARTED
:value: >
   ('started', 'Started')

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.StatusChoices.STARTED
```

````

````{py:attribute} BACKOFF
:canonical: archivebox.core.models.ArchiveResult.StatusChoices.BACKOFF
:value: >
   ('backoff', 'Waiting to retry')

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.StatusChoices.BACKOFF
```

````

````{py:attribute} SUCCEEDED
:canonical: archivebox.core.models.ArchiveResult.StatusChoices.SUCCEEDED
:value: >
   ('succeeded', 'Succeeded')

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.StatusChoices.SUCCEEDED
```

````

````{py:attribute} FAILED
:canonical: archivebox.core.models.ArchiveResult.StatusChoices.FAILED
:value: >
   ('failed', 'Failed')

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.StatusChoices.FAILED
```

````

````{py:attribute} SKIPPED
:canonical: archivebox.core.models.ArchiveResult.StatusChoices.SKIPPED
:value: >
   ('skipped', 'Skipped')

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.StatusChoices.SKIPPED
```

````

`````

````{py:attribute} state_machine_name
:canonical: archivebox.core.models.ArchiveResult.state_machine_name
:value: >
   'core.statemachines.ArchiveResultMachine'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.state_machine_name
```

````

````{py:attribute} retry_at_field_name
:canonical: archivebox.core.models.ArchiveResult.retry_at_field_name
:value: >
   'retry_at'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.retry_at_field_name
```

````

````{py:attribute} state_field_name
:canonical: archivebox.core.models.ArchiveResult.state_field_name
:value: >
   'status'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.state_field_name
```

````

````{py:attribute} active_state
:canonical: archivebox.core.models.ArchiveResult.active_state
:value: >
   None

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.active_state
```

````

````{py:attribute} EXTRACTOR_CHOICES
:canonical: archivebox.core.models.ArchiveResult.EXTRACTOR_CHOICES
:value: >
   (('htmltotext', 'htmltotext'), ('git', 'git'), ('singlefile', 'singlefile'), ('media', 'media'), ('a...

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.EXTRACTOR_CHOICES
```

````

````{py:attribute} id
:canonical: archivebox.core.models.ArchiveResult.id
:value: >
   'UUIDField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.id
```

````

````{py:attribute} abid
:canonical: archivebox.core.models.ArchiveResult.abid
:value: >
   'ABIDField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.abid
```

````

````{py:attribute} created_by
:canonical: archivebox.core.models.ArchiveResult.created_by
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.created_by
```

````

````{py:attribute} created_at
:canonical: archivebox.core.models.ArchiveResult.created_at
:value: >
   'AutoDateTimeField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.created_at
```

````

````{py:attribute} modified_at
:canonical: archivebox.core.models.ArchiveResult.modified_at
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.modified_at
```

````

````{py:attribute} status
:canonical: archivebox.core.models.ArchiveResult.status
:value: >
   'StatusField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.status
```

````

````{py:attribute} retry_at
:canonical: archivebox.core.models.ArchiveResult.retry_at
:value: >
   'RetryAtField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.retry_at
```

````

````{py:attribute} snapshot
:canonical: archivebox.core.models.ArchiveResult.snapshot
:type: archivebox.core.models.Snapshot
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.snapshot
```

````

````{py:attribute} extractor
:canonical: archivebox.core.models.ArchiveResult.extractor
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.extractor
```

````

````{py:attribute} cmd
:canonical: archivebox.core.models.ArchiveResult.cmd
:value: >
   'JSONField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.cmd
```

````

````{py:attribute} pwd
:canonical: archivebox.core.models.ArchiveResult.pwd
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.pwd
```

````

````{py:attribute} cmd_version
:canonical: archivebox.core.models.ArchiveResult.cmd_version
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.cmd_version
```

````

````{py:attribute} output
:canonical: archivebox.core.models.ArchiveResult.output
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.output
```

````

````{py:attribute} start_ts
:canonical: archivebox.core.models.ArchiveResult.start_ts
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.start_ts
```

````

````{py:attribute} end_ts
:canonical: archivebox.core.models.ArchiveResult.end_ts
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.end_ts
```

````

````{py:attribute} objects
:canonical: archivebox.core.models.ArchiveResult.objects
:value: >
   'ArchiveResultManager(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.objects
```

````

`````{py:class} Meta
:canonical: archivebox.core.models.ArchiveResult.Meta

Bases: {py:obj}`django_stubs_ext.db.models.TypedModelMeta`

````{py:attribute} verbose_name
:canonical: archivebox.core.models.ArchiveResult.Meta.verbose_name
:value: >
   'Archive Result'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.Meta.verbose_name
```

````

````{py:attribute} verbose_name_plural
:canonical: archivebox.core.models.ArchiveResult.Meta.verbose_name_plural
:value: >
   'Archive Results Log'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.Meta.verbose_name_plural
```

````

`````

````{py:method} __repr__()
:canonical: archivebox.core.models.ArchiveResult.__repr__

````

````{py:method} __str__()
:canonical: archivebox.core.models.ArchiveResult.__str__

````

````{py:method} snapshot_dir()
:canonical: archivebox.core.models.ArchiveResult.snapshot_dir

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.snapshot_dir
```

````

````{py:method} url()
:canonical: archivebox.core.models.ArchiveResult.url

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.url
```

````

````{py:property} api_url
:canonical: archivebox.core.models.ArchiveResult.api_url
:type: str

````

````{py:property} api_docs_url
:canonical: archivebox.core.models.ArchiveResult.api_docs_url
:type: str

````

````{py:method} get_absolute_url()
:canonical: archivebox.core.models.ArchiveResult.get_absolute_url

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.get_absolute_url
```

````

````{py:property} extractor_module
:canonical: archivebox.core.models.ArchiveResult.extractor_module

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.extractor_module
```

````

````{py:method} output_path() -> str
:canonical: archivebox.core.models.ArchiveResult.output_path

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.output_path
```

````

````{py:method} embed_path() -> str
:canonical: archivebox.core.models.ArchiveResult.embed_path

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.embed_path
```

````

````{py:method} legacy_output_path()
:canonical: archivebox.core.models.ArchiveResult.legacy_output_path

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.legacy_output_path
```

````

````{py:method} output_exists() -> bool
:canonical: archivebox.core.models.ArchiveResult.output_exists

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.output_exists
```

````

````{py:method} create_output_dir()
:canonical: archivebox.core.models.ArchiveResult.create_output_dir

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.create_output_dir
```

````

``````
