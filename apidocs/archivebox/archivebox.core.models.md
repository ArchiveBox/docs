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
  -
* - {py:obj}`SnapshotTag <archivebox.core.models.SnapshotTag>`
  -
* - {py:obj}`SnapshotQuerySet <archivebox.core.models.SnapshotQuerySet>`
  - ```{autodoc2-docstring} archivebox.core.models.SnapshotQuerySet
    :summary:
    ```
* - {py:obj}`SnapshotManager <archivebox.core.models.SnapshotManager>`
  - ```{autodoc2-docstring} archivebox.core.models.SnapshotManager
    :summary:
    ```
* - {py:obj}`Snapshot <archivebox.core.models.Snapshot>`
  -
* - {py:obj}`SnapshotMachine <archivebox.core.models.SnapshotMachine>`
  - ```{autodoc2-docstring} archivebox.core.models.SnapshotMachine
    :summary:
    ```
* - {py:obj}`ArchiveResult <archivebox.core.models.ArchiveResult>`
  -
* - {py:obj}`ArchiveResultMachine <archivebox.core.models.ArchiveResultMachine>`
  - ```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine
    :summary:
    ```
````

### API

``````{py:class} Tag(*args, **kwargs)
:canonical: archivebox.core.models.Tag

Bases: {py:obj}`archivebox.base_models.models.ModelWithUUID`

````{py:attribute} id
:canonical: archivebox.core.models.Tag.id
:value: >
   'AutoField(...)'

```{autodoc2-docstring} archivebox.core.models.Tag.id
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
   'DateTimeField(...)'

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

````{py:attribute} app_label
:canonical: archivebox.core.models.Tag.Meta.app_label
:value: >
   'core'

```{autodoc2-docstring} archivebox.core.models.Tag.Meta.app_label
```

````

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

````{py:method} save(*args, **kwargs)
:canonical: archivebox.core.models.Tag.save

````

````{py:property} api_url
:canonical: archivebox.core.models.Tag.api_url
:type: str

```{autodoc2-docstring} archivebox.core.models.Tag.api_url
```

````

````{py:method} to_json() -> dict
:canonical: archivebox.core.models.Tag.to_json

```{autodoc2-docstring} archivebox.core.models.Tag.to_json
```

````

````{py:method} from_json(record: typing.Dict[str, typing.Any], overrides: typing.Dict[str, typing.Any] = None)
:canonical: archivebox.core.models.Tag.from_json
:staticmethod:

```{autodoc2-docstring} archivebox.core.models.Tag.from_json
```

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

````{py:attribute} app_label
:canonical: archivebox.core.models.SnapshotTag.Meta.app_label
:value: >
   'core'

```{autodoc2-docstring} archivebox.core.models.SnapshotTag.Meta.app_label
```

````

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

`````{py:class} SnapshotQuerySet(model=None, query=None, using=None, hints=None)
:canonical: archivebox.core.models.SnapshotQuerySet

Bases: {py:obj}`django.db.models.QuerySet`

```{autodoc2-docstring} archivebox.core.models.SnapshotQuerySet
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.core.models.SnapshotQuerySet.__init__
```

````{py:attribute} FILTER_TYPES
:canonical: archivebox.core.models.SnapshotQuerySet.FILTER_TYPES
:value: >
   None

```{autodoc2-docstring} archivebox.core.models.SnapshotQuerySet.FILTER_TYPES
```

````

````{py:method} filter_by_patterns(patterns: typing.List[str], filter_type: str = 'exact') -> archivebox.core.models.SnapshotQuerySet
:canonical: archivebox.core.models.SnapshotQuerySet.filter_by_patterns

```{autodoc2-docstring} archivebox.core.models.SnapshotQuerySet.filter_by_patterns
```

````

````{py:method} search(patterns: typing.List[str]) -> archivebox.core.models.SnapshotQuerySet
:canonical: archivebox.core.models.SnapshotQuerySet.search

```{autodoc2-docstring} archivebox.core.models.SnapshotQuerySet.search
```

````

````{py:method} to_json(with_headers: bool = False) -> str
:canonical: archivebox.core.models.SnapshotQuerySet.to_json

```{autodoc2-docstring} archivebox.core.models.SnapshotQuerySet.to_json
```

````

````{py:method} to_csv(cols: typing.Optional[typing.List[str]] = None, header: bool = True, separator: str = ',', ljust: int = 0) -> str
:canonical: archivebox.core.models.SnapshotQuerySet.to_csv

```{autodoc2-docstring} archivebox.core.models.SnapshotQuerySet.to_csv
```

````

````{py:method} to_html(with_headers: bool = True) -> str
:canonical: archivebox.core.models.SnapshotQuerySet.to_html

```{autodoc2-docstring} archivebox.core.models.SnapshotQuerySet.to_html
```

````

`````

`````{py:class} SnapshotManager
:canonical: archivebox.core.models.SnapshotManager

Bases: {py:obj}`models.Manager.from_queryset`\({py:obj}`SnapshotQuerySet`\)

```{autodoc2-docstring} archivebox.core.models.SnapshotManager
```

````{py:method} filter(*args, **kwargs)
:canonical: archivebox.core.models.SnapshotManager.filter

```{autodoc2-docstring} archivebox.core.models.SnapshotManager.filter
```

````

````{py:method} get_queryset()
:canonical: archivebox.core.models.SnapshotManager.get_queryset

```{autodoc2-docstring} archivebox.core.models.SnapshotManager.get_queryset
```

````

````{py:method} remove(atomic: bool = False) -> tuple
:canonical: archivebox.core.models.SnapshotManager.remove

```{autodoc2-docstring} archivebox.core.models.SnapshotManager.remove
```

````

`````

``````{py:class} Snapshot(*args, **kwargs)
:canonical: archivebox.core.models.Snapshot

Bases: {py:obj}`archivebox.base_models.models.ModelWithOutputDir`, {py:obj}`archivebox.base_models.models.ModelWithConfig`, {py:obj}`archivebox.base_models.models.ModelWithNotes`, {py:obj}`archivebox.base_models.models.ModelWithHealthStats`, {py:obj}`archivebox.workers.models.ModelWithStateMachine`

````{py:attribute} id
:canonical: archivebox.core.models.Snapshot.id
:value: >
   'UUIDField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.id
```

````

````{py:attribute} created_at
:canonical: archivebox.core.models.Snapshot.created_at
:value: >
   'DateTimeField(...)'

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

````{py:attribute} bookmarked_at
:canonical: archivebox.core.models.Snapshot.bookmarked_at
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.bookmarked_at
```

````

````{py:attribute} crawl
:canonical: archivebox.core.models.Snapshot.crawl
:type: archivebox.crawls.models.Crawl
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.crawl
```

````

````{py:attribute} parent_snapshot
:canonical: archivebox.core.models.Snapshot.parent_snapshot
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.parent_snapshot
```

````

````{py:attribute} title
:canonical: archivebox.core.models.Snapshot.title
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.title
```

````

````{py:attribute} downloaded_at
:canonical: archivebox.core.models.Snapshot.downloaded_at
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.downloaded_at
```

````

````{py:attribute} depth
:canonical: archivebox.core.models.Snapshot.depth
:value: >
   'PositiveSmallIntegerField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.depth
```

````

````{py:attribute} fs_version
:canonical: archivebox.core.models.Snapshot.fs_version
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.fs_version
```

````

````{py:attribute} current_step
:canonical: archivebox.core.models.Snapshot.current_step
:value: >
   'PositiveSmallIntegerField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.current_step
```

````

````{py:attribute} retry_at
:canonical: archivebox.core.models.Snapshot.retry_at
:value: >
   'RetryAtField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.retry_at
```

````

````{py:attribute} status
:canonical: archivebox.core.models.Snapshot.status
:value: >
   'StatusField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.status
```

````

````{py:attribute} config
:canonical: archivebox.core.models.Snapshot.config
:value: >
   'JSONField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.config
```

````

````{py:attribute} notes
:canonical: archivebox.core.models.Snapshot.notes
:value: >
   'TextField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.notes
```

````

````{py:attribute} tags
:canonical: archivebox.core.models.Snapshot.tags
:value: >
   'ManyToManyField(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.tags
```

````

````{py:attribute} state_machine_name
:canonical: archivebox.core.models.Snapshot.state_machine_name
:value: >
   'archivebox.core.models.SnapshotMachine'

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

````{py:attribute} objects
:canonical: archivebox.core.models.Snapshot.objects
:value: >
   'SnapshotManager(...)'

```{autodoc2-docstring} archivebox.core.models.Snapshot.objects
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

`````{py:class} Meta
:canonical: archivebox.core.models.Snapshot.Meta

Bases: {py:obj}`django_stubs_ext.db.models.TypedModelMeta`

````{py:attribute} app_label
:canonical: archivebox.core.models.Snapshot.Meta.app_label
:value: >
   'core'

```{autodoc2-docstring} archivebox.core.models.Snapshot.Meta.app_label
```

````

````{py:attribute} verbose_name
:canonical: archivebox.core.models.Snapshot.Meta.verbose_name
:value: >
   'Snapshot'

```{autodoc2-docstring} archivebox.core.models.Snapshot.Meta.verbose_name
```

````

````{py:attribute} verbose_name_plural
:canonical: archivebox.core.models.Snapshot.Meta.verbose_name_plural
:value: >
   'Snapshots'

```{autodoc2-docstring} archivebox.core.models.Snapshot.Meta.verbose_name_plural
```

````

````{py:attribute} constraints
:canonical: archivebox.core.models.Snapshot.Meta.constraints
:value: >
   None

```{autodoc2-docstring} archivebox.core.models.Snapshot.Meta.constraints
```

````

`````

````{py:method} __str__()
:canonical: archivebox.core.models.Snapshot.__str__

````

````{py:property} created_by
:canonical: archivebox.core.models.Snapshot.created_by

```{autodoc2-docstring} archivebox.core.models.Snapshot.created_by
```

````

````{py:property} process_set
:canonical: archivebox.core.models.Snapshot.process_set

```{autodoc2-docstring} archivebox.core.models.Snapshot.process_set
```

````

````{py:property} binary_set
:canonical: archivebox.core.models.Snapshot.binary_set

```{autodoc2-docstring} archivebox.core.models.Snapshot.binary_set
```

````

````{py:method} save(*args, **kwargs)
:canonical: archivebox.core.models.Snapshot.save

````

````{py:method} _fs_current_version() -> str
:canonical: archivebox.core.models.Snapshot._fs_current_version
:staticmethod:

```{autodoc2-docstring} archivebox.core.models.Snapshot._fs_current_version
```

````

````{py:property} fs_migration_needed
:canonical: archivebox.core.models.Snapshot.fs_migration_needed
:type: bool

```{autodoc2-docstring} archivebox.core.models.Snapshot.fs_migration_needed
```

````

````{py:method} _fs_next_version(version: str) -> str
:canonical: archivebox.core.models.Snapshot._fs_next_version

```{autodoc2-docstring} archivebox.core.models.Snapshot._fs_next_version
```

````

````{py:method} _fs_migrate_from_0_8_0_to_0_9_0()
:canonical: archivebox.core.models.Snapshot._fs_migrate_from_0_8_0_to_0_9_0

```{autodoc2-docstring} archivebox.core.models.Snapshot._fs_migrate_from_0_8_0_to_0_9_0
```

````

````{py:method} _cleanup_old_migration_dir(old_dir: pathlib.Path, new_dir: pathlib.Path)
:canonical: archivebox.core.models.Snapshot._cleanup_old_migration_dir

```{autodoc2-docstring} archivebox.core.models.Snapshot._cleanup_old_migration_dir
```

````

````{py:method} extract_domain_from_url(url: str) -> str
:canonical: archivebox.core.models.Snapshot.extract_domain_from_url
:staticmethod:

```{autodoc2-docstring} archivebox.core.models.Snapshot.extract_domain_from_url
```

````

````{py:method} get_storage_path_for_version(version: str) -> pathlib.Path
:canonical: archivebox.core.models.Snapshot.get_storage_path_for_version

```{autodoc2-docstring} archivebox.core.models.Snapshot.get_storage_path_for_version
```

````

````{py:method} load_from_directory(snapshot_dir: pathlib.Path) -> typing.Optional[archivebox.core.models.Snapshot]
:canonical: archivebox.core.models.Snapshot.load_from_directory
:classmethod:

```{autodoc2-docstring} archivebox.core.models.Snapshot.load_from_directory
```

````

````{py:method} create_from_directory(snapshot_dir: pathlib.Path) -> typing.Optional[archivebox.core.models.Snapshot]
:canonical: archivebox.core.models.Snapshot.create_from_directory
:classmethod:

```{autodoc2-docstring} archivebox.core.models.Snapshot.create_from_directory
```

````

````{py:method} _select_best_timestamp(index_timestamp: str, folder_name: str) -> typing.Optional[str]
:canonical: archivebox.core.models.Snapshot._select_best_timestamp
:staticmethod:

```{autodoc2-docstring} archivebox.core.models.Snapshot._select_best_timestamp
```

````

````{py:method} _ensure_unique_timestamp(url: str, timestamp: str) -> str
:canonical: archivebox.core.models.Snapshot._ensure_unique_timestamp
:classmethod:

```{autodoc2-docstring} archivebox.core.models.Snapshot._ensure_unique_timestamp
```

````

````{py:method} _detect_fs_version_from_index(data: dict) -> str
:canonical: archivebox.core.models.Snapshot._detect_fs_version_from_index
:staticmethod:

```{autodoc2-docstring} archivebox.core.models.Snapshot._detect_fs_version_from_index
```

````

````{py:method} reconcile_with_index()
:canonical: archivebox.core.models.Snapshot.reconcile_with_index

```{autodoc2-docstring} archivebox.core.models.Snapshot.reconcile_with_index
```

````

````{py:method} reconcile_with_index_json()
:canonical: archivebox.core.models.Snapshot.reconcile_with_index_json

```{autodoc2-docstring} archivebox.core.models.Snapshot.reconcile_with_index_json
```

````

````{py:method} _merge_title_from_index(index_data: dict)
:canonical: archivebox.core.models.Snapshot._merge_title_from_index

```{autodoc2-docstring} archivebox.core.models.Snapshot._merge_title_from_index
```

````

````{py:method} _merge_tags_from_index(index_data: dict)
:canonical: archivebox.core.models.Snapshot._merge_tags_from_index

```{autodoc2-docstring} archivebox.core.models.Snapshot._merge_tags_from_index
```

````

````{py:method} _merge_archive_results_from_index(index_data: dict)
:canonical: archivebox.core.models.Snapshot._merge_archive_results_from_index

```{autodoc2-docstring} archivebox.core.models.Snapshot._merge_archive_results_from_index
```

````

````{py:method} _create_archive_result_if_missing(result_data: dict, existing: dict)
:canonical: archivebox.core.models.Snapshot._create_archive_result_if_missing

```{autodoc2-docstring} archivebox.core.models.Snapshot._create_archive_result_if_missing
```

````

````{py:method} write_index_json()
:canonical: archivebox.core.models.Snapshot.write_index_json

```{autodoc2-docstring} archivebox.core.models.Snapshot.write_index_json
```

````

````{py:method} write_index_jsonl()
:canonical: archivebox.core.models.Snapshot.write_index_jsonl

```{autodoc2-docstring} archivebox.core.models.Snapshot.write_index_jsonl
```

````

````{py:method} read_index_jsonl() -> dict
:canonical: archivebox.core.models.Snapshot.read_index_jsonl

```{autodoc2-docstring} archivebox.core.models.Snapshot.read_index_jsonl
```

````

````{py:method} convert_index_json_to_jsonl() -> bool
:canonical: archivebox.core.models.Snapshot.convert_index_json_to_jsonl

```{autodoc2-docstring} archivebox.core.models.Snapshot.convert_index_json_to_jsonl
```

````

````{py:method} move_directory_to_invalid(snapshot_dir: pathlib.Path)
:canonical: archivebox.core.models.Snapshot.move_directory_to_invalid
:staticmethod:

```{autodoc2-docstring} archivebox.core.models.Snapshot.move_directory_to_invalid
```

````

````{py:method} find_and_merge_duplicates() -> int
:canonical: archivebox.core.models.Snapshot.find_and_merge_duplicates
:classmethod:

```{autodoc2-docstring} archivebox.core.models.Snapshot.find_and_merge_duplicates
```

````

````{py:method} _merge_snapshots(snapshots: list[archivebox.core.models.Snapshot])
:canonical: archivebox.core.models.Snapshot._merge_snapshots
:classmethod:

```{autodoc2-docstring} archivebox.core.models.Snapshot._merge_snapshots
```

````

````{py:property} output_dir_parent
:canonical: archivebox.core.models.Snapshot.output_dir_parent
:type: str

```{autodoc2-docstring} archivebox.core.models.Snapshot.output_dir_parent
```

````

````{py:property} output_dir_name
:canonical: archivebox.core.models.Snapshot.output_dir_name
:type: str

```{autodoc2-docstring} archivebox.core.models.Snapshot.output_dir_name
```

````

````{py:method} archive(overwrite=False, methods=None)
:canonical: archivebox.core.models.Snapshot.archive

```{autodoc2-docstring} archivebox.core.models.Snapshot.archive
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

```{autodoc2-docstring} archivebox.core.models.Snapshot.api_url
```

````

````{py:method} get_absolute_url()
:canonical: archivebox.core.models.Snapshot.get_absolute_url

```{autodoc2-docstring} archivebox.core.models.Snapshot.get_absolute_url
```

````

````{py:method} domain() -> str
:canonical: archivebox.core.models.Snapshot.domain

```{autodoc2-docstring} archivebox.core.models.Snapshot.domain
```

````

````{py:property} output_dir
:canonical: archivebox.core.models.Snapshot.output_dir

```{autodoc2-docstring} archivebox.core.models.Snapshot.output_dir
```

````

````{py:method} ensure_legacy_archive_symlink() -> None
:canonical: archivebox.core.models.Snapshot.ensure_legacy_archive_symlink

```{autodoc2-docstring} archivebox.core.models.Snapshot.ensure_legacy_archive_symlink
```

````

````{py:method} ensure_crawl_symlink() -> None
:canonical: archivebox.core.models.Snapshot.ensure_crawl_symlink

```{autodoc2-docstring} archivebox.core.models.Snapshot.ensure_crawl_symlink
```

````

````{py:method} legacy_archive_path() -> str
:canonical: archivebox.core.models.Snapshot.legacy_archive_path

```{autodoc2-docstring} archivebox.core.models.Snapshot.legacy_archive_path
```

````

````{py:method} url_path() -> str
:canonical: archivebox.core.models.Snapshot.url_path

```{autodoc2-docstring} archivebox.core.models.Snapshot.url_path
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

````{py:method} save_tags(tags: typing.Iterable[str] = ()) -> None
:canonical: archivebox.core.models.Snapshot.save_tags

```{autodoc2-docstring} archivebox.core.models.Snapshot.save_tags
```

````

````{py:method} pending_archiveresults() -> django.db.models.QuerySet[archivebox.core.models.ArchiveResult]
:canonical: archivebox.core.models.Snapshot.pending_archiveresults

```{autodoc2-docstring} archivebox.core.models.Snapshot.pending_archiveresults
```

````

````{py:method} run() -> list[archivebox.core.models.ArchiveResult]
:canonical: archivebox.core.models.Snapshot.run

```{autodoc2-docstring} archivebox.core.models.Snapshot.run
```

````

````{py:method} cleanup()
:canonical: archivebox.core.models.Snapshot.cleanup

```{autodoc2-docstring} archivebox.core.models.Snapshot.cleanup
```

````

````{py:method} to_json() -> dict
:canonical: archivebox.core.models.Snapshot.to_json

```{autodoc2-docstring} archivebox.core.models.Snapshot.to_json
```

````

````{py:method} from_json(record: typing.Dict[str, typing.Any], overrides: typing.Dict[str, typing.Any] = None, queue_for_extraction: bool = True)
:canonical: archivebox.core.models.Snapshot.from_json
:staticmethod:

```{autodoc2-docstring} archivebox.core.models.Snapshot.from_json
```

````

````{py:method} create_pending_archiveresults() -> list[archivebox.core.models.ArchiveResult]
:canonical: archivebox.core.models.Snapshot.create_pending_archiveresults

```{autodoc2-docstring} archivebox.core.models.Snapshot.create_pending_archiveresults
```

````

````{py:method} is_finished_processing() -> bool
:canonical: archivebox.core.models.Snapshot.is_finished_processing

```{autodoc2-docstring} archivebox.core.models.Snapshot.is_finished_processing
```

````

````{py:method} get_progress_stats() -> dict
:canonical: archivebox.core.models.Snapshot.get_progress_stats

```{autodoc2-docstring} archivebox.core.models.Snapshot.get_progress_stats
```

````

````{py:method} retry_failed_archiveresults(retry_at: typing.Optional[django.utils.timezone.datetime] = None) -> int
:canonical: archivebox.core.models.Snapshot.retry_failed_archiveresults

```{autodoc2-docstring} archivebox.core.models.Snapshot.retry_failed_archiveresults
```

````

````{py:method} url_hash() -> str
:canonical: archivebox.core.models.Snapshot.url_hash

```{autodoc2-docstring} archivebox.core.models.Snapshot.url_hash
```

````

````{py:method} scheme() -> str
:canonical: archivebox.core.models.Snapshot.scheme

```{autodoc2-docstring} archivebox.core.models.Snapshot.scheme
```

````

````{py:method} path() -> str
:canonical: archivebox.core.models.Snapshot.path

```{autodoc2-docstring} archivebox.core.models.Snapshot.path
```

````

````{py:method} basename() -> str
:canonical: archivebox.core.models.Snapshot.basename

```{autodoc2-docstring} archivebox.core.models.Snapshot.basename
```

````

````{py:method} extension() -> str
:canonical: archivebox.core.models.Snapshot.extension

```{autodoc2-docstring} archivebox.core.models.Snapshot.extension
```

````

````{py:method} base_url() -> str
:canonical: archivebox.core.models.Snapshot.base_url

```{autodoc2-docstring} archivebox.core.models.Snapshot.base_url
```

````

````{py:method} is_static() -> bool
:canonical: archivebox.core.models.Snapshot.is_static

```{autodoc2-docstring} archivebox.core.models.Snapshot.is_static
```

````

````{py:method} is_archived() -> bool
:canonical: archivebox.core.models.Snapshot.is_archived

```{autodoc2-docstring} archivebox.core.models.Snapshot.is_archived
```

````

````{py:method} bookmarked_date() -> typing.Optional[str]
:canonical: archivebox.core.models.Snapshot.bookmarked_date

```{autodoc2-docstring} archivebox.core.models.Snapshot.bookmarked_date
```

````

````{py:method} downloaded_datestr() -> typing.Optional[str]
:canonical: archivebox.core.models.Snapshot.downloaded_datestr

```{autodoc2-docstring} archivebox.core.models.Snapshot.downloaded_datestr
```

````

````{py:method} archive_dates() -> typing.List[datetime.datetime]
:canonical: archivebox.core.models.Snapshot.archive_dates

```{autodoc2-docstring} archivebox.core.models.Snapshot.archive_dates
```

````

````{py:method} oldest_archive_date() -> typing.Optional[datetime.datetime]
:canonical: archivebox.core.models.Snapshot.oldest_archive_date

```{autodoc2-docstring} archivebox.core.models.Snapshot.oldest_archive_date
```

````

````{py:method} newest_archive_date() -> typing.Optional[datetime.datetime]
:canonical: archivebox.core.models.Snapshot.newest_archive_date

```{autodoc2-docstring} archivebox.core.models.Snapshot.newest_archive_date
```

````

````{py:method} num_outputs() -> int
:canonical: archivebox.core.models.Snapshot.num_outputs

```{autodoc2-docstring} archivebox.core.models.Snapshot.num_outputs
```

````

````{py:method} num_failures() -> int
:canonical: archivebox.core.models.Snapshot.num_failures

```{autodoc2-docstring} archivebox.core.models.Snapshot.num_failures
```

````

````{py:method} latest_outputs(status: typing.Optional[str] = None) -> typing.Dict[str, typing.Any]
:canonical: archivebox.core.models.Snapshot.latest_outputs

```{autodoc2-docstring} archivebox.core.models.Snapshot.latest_outputs
```

````

````{py:method} discover_outputs() -> list[dict]
:canonical: archivebox.core.models.Snapshot.discover_outputs

```{autodoc2-docstring} archivebox.core.models.Snapshot.discover_outputs
```

````

````{py:method} to_dict(extended: bool = False) -> typing.Dict[str, typing.Any]
:canonical: archivebox.core.models.Snapshot.to_dict

```{autodoc2-docstring} archivebox.core.models.Snapshot.to_dict
```

````

````{py:method} to_json_str(indent: int = 4) -> str
:canonical: archivebox.core.models.Snapshot.to_json_str

```{autodoc2-docstring} archivebox.core.models.Snapshot.to_json_str
```

````

````{py:method} to_csv(cols: typing.Optional[typing.List[str]] = None, separator: str = ',', ljust: int = 0) -> str
:canonical: archivebox.core.models.Snapshot.to_csv

```{autodoc2-docstring} archivebox.core.models.Snapshot.to_csv
```

````

````{py:method} write_json_details(out_dir: typing.Optional[str] = None) -> None
:canonical: archivebox.core.models.Snapshot.write_json_details

```{autodoc2-docstring} archivebox.core.models.Snapshot.write_json_details
```

````

````{py:method} write_html_details(out_dir: typing.Optional[str] = None) -> None
:canonical: archivebox.core.models.Snapshot.write_html_details

```{autodoc2-docstring} archivebox.core.models.Snapshot.write_html_details
```

````

````{py:method} _ts_to_date_str(dt: typing.Optional[datetime.datetime]) -> typing.Optional[str]
:canonical: archivebox.core.models.Snapshot._ts_to_date_str
:staticmethod:

```{autodoc2-docstring} archivebox.core.models.Snapshot._ts_to_date_str
```

````

``````

`````{py:class} SnapshotMachine(obj, *args, **kwargs)
:canonical: archivebox.core.models.SnapshotMachine

Bases: {py:obj}`archivebox.workers.models.BaseStateMachine`

```{autodoc2-docstring} archivebox.core.models.SnapshotMachine
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.core.models.SnapshotMachine.__init__
```

````{py:attribute} model_attr_name
:canonical: archivebox.core.models.SnapshotMachine.model_attr_name
:value: >
   'snapshot'

```{autodoc2-docstring} archivebox.core.models.SnapshotMachine.model_attr_name
```

````

````{py:attribute} queued
:canonical: archivebox.core.models.SnapshotMachine.queued
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.core.models.SnapshotMachine.queued
```

````

````{py:attribute} started
:canonical: archivebox.core.models.SnapshotMachine.started
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.core.models.SnapshotMachine.started
```

````

````{py:attribute} sealed
:canonical: archivebox.core.models.SnapshotMachine.sealed
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.core.models.SnapshotMachine.sealed
```

````

````{py:attribute} tick
:canonical: archivebox.core.models.SnapshotMachine.tick
:value: >
   None

```{autodoc2-docstring} archivebox.core.models.SnapshotMachine.tick
```

````

````{py:attribute} seal
:canonical: archivebox.core.models.SnapshotMachine.seal
:value: >
   'to(...)'

```{autodoc2-docstring} archivebox.core.models.SnapshotMachine.seal
```

````

````{py:method} can_start() -> bool
:canonical: archivebox.core.models.SnapshotMachine.can_start

```{autodoc2-docstring} archivebox.core.models.SnapshotMachine.can_start
```

````

````{py:method} is_finished() -> bool
:canonical: archivebox.core.models.SnapshotMachine.is_finished

```{autodoc2-docstring} archivebox.core.models.SnapshotMachine.is_finished
```

````

````{py:method} enter_queued()
:canonical: archivebox.core.models.SnapshotMachine.enter_queued

```{autodoc2-docstring} archivebox.core.models.SnapshotMachine.enter_queued
```

````

````{py:method} enter_started()
:canonical: archivebox.core.models.SnapshotMachine.enter_started

```{autodoc2-docstring} archivebox.core.models.SnapshotMachine.enter_started
```

````

````{py:method} enter_sealed()
:canonical: archivebox.core.models.SnapshotMachine.enter_sealed

```{autodoc2-docstring} archivebox.core.models.SnapshotMachine.enter_sealed
```

````

`````

``````{py:class} ArchiveResult(*args, **kwargs)
:canonical: archivebox.core.models.ArchiveResult

Bases: {py:obj}`archivebox.base_models.models.ModelWithOutputDir`, {py:obj}`archivebox.base_models.models.ModelWithConfig`, {py:obj}`archivebox.base_models.models.ModelWithNotes`, {py:obj}`archivebox.workers.models.ModelWithStateMachine`

`````{py:class} StatusChoices()
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

````{py:method} get_plugin_choices()
:canonical: archivebox.core.models.ArchiveResult.get_plugin_choices
:classmethod:

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.get_plugin_choices
```

````

````{py:attribute} id
:canonical: archivebox.core.models.ArchiveResult.id
:value: >
   'UUIDField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.id
```

````

````{py:attribute} created_at
:canonical: archivebox.core.models.ArchiveResult.created_at
:value: >
   'DateTimeField(...)'

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

````{py:attribute} snapshot
:canonical: archivebox.core.models.ArchiveResult.snapshot
:type: archivebox.core.models.Snapshot
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.snapshot
```

````

````{py:attribute} plugin
:canonical: archivebox.core.models.ArchiveResult.plugin
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.plugin
```

````

````{py:attribute} hook_name
:canonical: archivebox.core.models.ArchiveResult.hook_name
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.hook_name
```

````

````{py:attribute} process
:canonical: archivebox.core.models.ArchiveResult.process
:value: >
   'OneToOneField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.process
```

````

````{py:attribute} output_str
:canonical: archivebox.core.models.ArchiveResult.output_str
:value: >
   'TextField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.output_str
```

````

````{py:attribute} output_json
:canonical: archivebox.core.models.ArchiveResult.output_json
:value: >
   'JSONField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.output_json
```

````

````{py:attribute} output_files
:canonical: archivebox.core.models.ArchiveResult.output_files
:value: >
   'JSONField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.output_files
```

````

````{py:attribute} output_size
:canonical: archivebox.core.models.ArchiveResult.output_size
:value: >
   'BigIntegerField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.output_size
```

````

````{py:attribute} output_mimetypes
:canonical: archivebox.core.models.ArchiveResult.output_mimetypes
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.output_mimetypes
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

````{py:attribute} notes
:canonical: archivebox.core.models.ArchiveResult.notes
:value: >
   'TextField(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.notes
```

````

````{py:attribute} state_machine_name
:canonical: archivebox.core.models.ArchiveResult.state_machine_name
:value: >
   'archivebox.core.models.ArchiveResultMachine'

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

`````{py:class} Meta
:canonical: archivebox.core.models.ArchiveResult.Meta

Bases: {py:obj}`django_stubs_ext.db.models.TypedModelMeta`

````{py:attribute} app_label
:canonical: archivebox.core.models.ArchiveResult.Meta.app_label
:value: >
   'core'

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.Meta.app_label
```

````

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

````{py:attribute} indexes
:canonical: archivebox.core.models.ArchiveResult.Meta.indexes
:value: >
   None

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.Meta.indexes
```

````

`````

````{py:method} __str__()
:canonical: archivebox.core.models.ArchiveResult.__str__

````

````{py:property} created_by
:canonical: archivebox.core.models.ArchiveResult.created_by

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.created_by
```

````

````{py:method} to_json() -> dict
:canonical: archivebox.core.models.ArchiveResult.to_json

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.to_json
```

````

````{py:method} from_json(record: typing.Dict[str, typing.Any], overrides: typing.Dict[str, typing.Any] = None)
:canonical: archivebox.core.models.ArchiveResult.from_json
:staticmethod:

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.from_json
```

````

````{py:method} save(*args, **kwargs)
:canonical: archivebox.core.models.ArchiveResult.save

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

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.api_url
```

````

````{py:method} get_absolute_url()
:canonical: archivebox.core.models.ArchiveResult.get_absolute_url

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.get_absolute_url
```

````

````{py:property} plugin_module
:canonical: archivebox.core.models.ArchiveResult.plugin_module
:type: typing.Any | None

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.plugin_module
```

````

````{py:method} output_exists() -> bool
:canonical: archivebox.core.models.ArchiveResult.output_exists

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.output_exists
```

````

````{py:method} _find_best_output_file(dir_path: pathlib.Path, plugin_name: str | None = None) -> typing.Optional[pathlib.Path]
:canonical: archivebox.core.models.ArchiveResult._find_best_output_file
:staticmethod:

```{autodoc2-docstring} archivebox.core.models.ArchiveResult._find_best_output_file
```

````

````{py:method} embed_path() -> typing.Optional[str]
:canonical: archivebox.core.models.ArchiveResult.embed_path

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.embed_path
```

````

````{py:method} create_output_dir()
:canonical: archivebox.core.models.ArchiveResult.create_output_dir

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.create_output_dir
```

````

````{py:property} output_dir_name
:canonical: archivebox.core.models.ArchiveResult.output_dir_name
:type: str

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.output_dir_name
```

````

````{py:property} output_dir_parent
:canonical: archivebox.core.models.ArchiveResult.output_dir_parent
:type: str

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.output_dir_parent
```

````

````{py:property} pwd
:canonical: archivebox.core.models.ArchiveResult.pwd
:type: str

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.pwd
```

````

````{py:property} cmd
:canonical: archivebox.core.models.ArchiveResult.cmd
:type: list

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.cmd
```

````

````{py:property} cmd_version
:canonical: archivebox.core.models.ArchiveResult.cmd_version
:type: str

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.cmd_version
```

````

````{py:property} binary
:canonical: archivebox.core.models.ArchiveResult.binary

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.binary
```

````

````{py:property} iface
:canonical: archivebox.core.models.ArchiveResult.iface

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.iface
```

````

````{py:property} machine
:canonical: archivebox.core.models.ArchiveResult.machine

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.machine
```

````

````{py:property} timeout
:canonical: archivebox.core.models.ArchiveResult.timeout
:type: int

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.timeout
```

````

````{py:method} save_search_index()
:canonical: archivebox.core.models.ArchiveResult.save_search_index

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.save_search_index
```

````

````{py:method} cascade_health_update(success: bool)
:canonical: archivebox.core.models.ArchiveResult.cascade_health_update

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.cascade_health_update
```

````

````{py:method} run()
:canonical: archivebox.core.models.ArchiveResult.run

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.run
```

````

````{py:method} update_from_output()
:canonical: archivebox.core.models.ArchiveResult.update_from_output

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.update_from_output
```

````

````{py:method} _set_binary_from_cmd(cmd: list) -> None
:canonical: archivebox.core.models.ArchiveResult._set_binary_from_cmd

```{autodoc2-docstring} archivebox.core.models.ArchiveResult._set_binary_from_cmd
```

````

````{py:method} _url_passes_filters(url: str) -> bool
:canonical: archivebox.core.models.ArchiveResult._url_passes_filters

```{autodoc2-docstring} archivebox.core.models.ArchiveResult._url_passes_filters
```

````

````{py:property} output_dir
:canonical: archivebox.core.models.ArchiveResult.output_dir
:type: pathlib.Path

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.output_dir
```

````

````{py:method} is_background_hook() -> bool
:canonical: archivebox.core.models.ArchiveResult.is_background_hook

```{autodoc2-docstring} archivebox.core.models.ArchiveResult.is_background_hook
```

````

``````

`````{py:class} ArchiveResultMachine(obj, *args, **kwargs)
:canonical: archivebox.core.models.ArchiveResultMachine

Bases: {py:obj}`archivebox.workers.models.BaseStateMachine`

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine.__init__
```

````{py:attribute} model_attr_name
:canonical: archivebox.core.models.ArchiveResultMachine.model_attr_name
:value: >
   'archiveresult'

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine.model_attr_name
```

````

````{py:attribute} queued
:canonical: archivebox.core.models.ArchiveResultMachine.queued
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine.queued
```

````

````{py:attribute} started
:canonical: archivebox.core.models.ArchiveResultMachine.started
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine.started
```

````

````{py:attribute} backoff
:canonical: archivebox.core.models.ArchiveResultMachine.backoff
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine.backoff
```

````

````{py:attribute} succeeded
:canonical: archivebox.core.models.ArchiveResultMachine.succeeded
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine.succeeded
```

````

````{py:attribute} failed
:canonical: archivebox.core.models.ArchiveResultMachine.failed
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine.failed
```

````

````{py:attribute} skipped
:canonical: archivebox.core.models.ArchiveResultMachine.skipped
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine.skipped
```

````

````{py:attribute} tick
:canonical: archivebox.core.models.ArchiveResultMachine.tick
:value: >
   None

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine.tick
```

````

````{py:method} can_start() -> bool
:canonical: archivebox.core.models.ArchiveResultMachine.can_start

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine.can_start
```

````

````{py:method} is_exceeded_max_attempts() -> bool
:canonical: archivebox.core.models.ArchiveResultMachine.is_exceeded_max_attempts

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine.is_exceeded_max_attempts
```

````

````{py:method} is_succeeded() -> bool
:canonical: archivebox.core.models.ArchiveResultMachine.is_succeeded

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine.is_succeeded
```

````

````{py:method} is_failed() -> bool
:canonical: archivebox.core.models.ArchiveResultMachine.is_failed

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine.is_failed
```

````

````{py:method} is_skipped() -> bool
:canonical: archivebox.core.models.ArchiveResultMachine.is_skipped

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine.is_skipped
```

````

````{py:method} is_backoff() -> bool
:canonical: archivebox.core.models.ArchiveResultMachine.is_backoff

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine.is_backoff
```

````

````{py:method} is_finished() -> bool
:canonical: archivebox.core.models.ArchiveResultMachine.is_finished

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine.is_finished
```

````

````{py:method} enter_queued()
:canonical: archivebox.core.models.ArchiveResultMachine.enter_queued

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine.enter_queued
```

````

````{py:method} enter_started()
:canonical: archivebox.core.models.ArchiveResultMachine.enter_started

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine.enter_started
```

````

````{py:method} enter_backoff()
:canonical: archivebox.core.models.ArchiveResultMachine.enter_backoff

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine.enter_backoff
```

````

````{py:method} _check_and_seal_parent_snapshot()
:canonical: archivebox.core.models.ArchiveResultMachine._check_and_seal_parent_snapshot

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine._check_and_seal_parent_snapshot
```

````

````{py:method} enter_succeeded()
:canonical: archivebox.core.models.ArchiveResultMachine.enter_succeeded

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine.enter_succeeded
```

````

````{py:method} enter_failed()
:canonical: archivebox.core.models.ArchiveResultMachine.enter_failed

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine.enter_failed
```

````

````{py:method} enter_skipped()
:canonical: archivebox.core.models.ArchiveResultMachine.enter_skipped

```{autodoc2-docstring} archivebox.core.models.ArchiveResultMachine.enter_skipped
```

````

`````
