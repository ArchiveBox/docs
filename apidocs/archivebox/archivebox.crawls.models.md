# {py:mod}`archivebox.crawls.models`

```{py:module} archivebox.crawls.models
```

```{autodoc2-docstring} archivebox.crawls.models
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CrawlSchedule <archivebox.crawls.models.CrawlSchedule>`
  - ```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule
    :summary:
    ```
* - {py:obj}`Crawl <archivebox.crawls.models.Crawl>`
  - ```{autodoc2-docstring} archivebox.crawls.models.Crawl
    :summary:
    ```
* - {py:obj}`Outlink <archivebox.crawls.models.Outlink>`
  - ```{autodoc2-docstring} archivebox.crawls.models.Outlink
    :summary:
    ```
````

### API

``````{py:class} CrawlSchedule(*args: typing.Any, **kwargs: typing.Any)
:canonical: archivebox.crawls.models.CrawlSchedule

Bases: {py:obj}`abid_utils.models.ABIDModel`, {py:obj}`abid_utils.models.ModelWithHealthStats`

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.__init__
```

````{py:attribute} abid_prefix
:canonical: archivebox.crawls.models.CrawlSchedule.abid_prefix
:value: >
   'cws_'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.abid_prefix
```

````

````{py:attribute} abid_ts_src
:canonical: archivebox.crawls.models.CrawlSchedule.abid_ts_src
:value: >
   'self.created_at'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.abid_ts_src
```

````

````{py:attribute} abid_uri_src
:canonical: archivebox.crawls.models.CrawlSchedule.abid_uri_src
:value: >
   'self.created_by_id'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.abid_uri_src
```

````

````{py:attribute} abid_subtype_src
:canonical: archivebox.crawls.models.CrawlSchedule.abid_subtype_src
:value: >
   'self.schedule'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.abid_subtype_src
```

````

````{py:attribute} abid_rand_src
:canonical: archivebox.crawls.models.CrawlSchedule.abid_rand_src
:value: >
   'self.id'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.abid_rand_src
```

````

````{py:attribute} id
:canonical: archivebox.crawls.models.CrawlSchedule.id
:value: >
   'UUIDField(...)'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.id
```

````

````{py:attribute} abid
:canonical: archivebox.crawls.models.CrawlSchedule.abid
:value: >
   'ABIDField(...)'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.abid
```

````

````{py:attribute} schedule
:canonical: archivebox.crawls.models.CrawlSchedule.schedule
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.schedule
```

````

````{py:attribute} label
:canonical: archivebox.crawls.models.CrawlSchedule.label
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.label
```

````

````{py:attribute} notes
:canonical: archivebox.crawls.models.CrawlSchedule.notes
:value: >
   'TextField(...)'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.notes
```

````

````{py:attribute} template
:canonical: archivebox.crawls.models.CrawlSchedule.template
:type: Crawl
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.template
```

````

````{py:attribute} created_by
:canonical: archivebox.crawls.models.CrawlSchedule.created_by
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.created_by
```

````

````{py:attribute} created_at
:canonical: archivebox.crawls.models.CrawlSchedule.created_at
:value: >
   'AutoDateTimeField(...)'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.created_at
```

````

````{py:attribute} modified_at
:canonical: archivebox.crawls.models.CrawlSchedule.modified_at
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.modified_at
```

````

````{py:attribute} is_enabled
:canonical: archivebox.crawls.models.CrawlSchedule.is_enabled
:value: >
   'BooleanField(...)'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.is_enabled
```

````

````{py:attribute} crawl_set
:canonical: archivebox.crawls.models.CrawlSchedule.crawl_set
:type: django.db.models.Manager[Crawl]
:value: >
   None

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.crawl_set
```

````

`````{py:class} Meta
:canonical: archivebox.crawls.models.CrawlSchedule.Meta

Bases: {py:obj}`django_stubs_ext.db.models.TypedModelMeta`

````{py:attribute} verbose_name
:canonical: archivebox.crawls.models.CrawlSchedule.Meta.verbose_name
:value: >
   'Scheduled Crawl'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.Meta.verbose_name
```

````

````{py:attribute} verbose_name_plural
:canonical: archivebox.crawls.models.CrawlSchedule.Meta.verbose_name_plural
:value: >
   'Scheduled Crawls'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.Meta.verbose_name_plural
```

````

`````

````{py:method} __str__() -> str
:canonical: archivebox.crawls.models.CrawlSchedule.__str__

````

````{py:property} api_url
:canonical: archivebox.crawls.models.CrawlSchedule.api_url
:type: str

````

````{py:property} api_docs_url
:canonical: archivebox.crawls.models.CrawlSchedule.api_docs_url
:type: str

````

````{py:method} save(*args, **kwargs)
:canonical: archivebox.crawls.models.CrawlSchedule.save

````

````{py:property} snapshot_set
:canonical: archivebox.crawls.models.CrawlSchedule.snapshot_set
:type: django.db.models.QuerySet[core.models.Snapshot]

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.snapshot_set
```

````

``````

``````{py:class} Crawl(*args: typing.Any, **kwargs: typing.Any)
:canonical: archivebox.crawls.models.Crawl

Bases: {py:obj}`abid_utils.models.ABIDModel`, {py:obj}`abid_utils.models.ModelWithHealthStats`, {py:obj}`actors.models.ModelWithStateMachine`

```{autodoc2-docstring} archivebox.crawls.models.Crawl
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.crawls.models.Crawl.__init__
```

````{py:attribute} abid_prefix
:canonical: archivebox.crawls.models.Crawl.abid_prefix
:value: >
   'cwl_'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.abid_prefix
```

````

````{py:attribute} abid_ts_src
:canonical: archivebox.crawls.models.Crawl.abid_ts_src
:value: >
   'self.created_at'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.abid_ts_src
```

````

````{py:attribute} abid_uri_src
:canonical: archivebox.crawls.models.Crawl.abid_uri_src
:value: >
   'self.seed.uri'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.abid_uri_src
```

````

````{py:attribute} abid_subtype_src
:canonical: archivebox.crawls.models.Crawl.abid_subtype_src
:value: >
   'self.persona'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.abid_subtype_src
```

````

````{py:attribute} abid_rand_src
:canonical: archivebox.crawls.models.Crawl.abid_rand_src
:value: >
   'self.id'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.abid_rand_src
```

````

````{py:attribute} abid_drift_allowed
:canonical: archivebox.crawls.models.Crawl.abid_drift_allowed
:value: >
   True

```{autodoc2-docstring} archivebox.crawls.models.Crawl.abid_drift_allowed
```

````

````{py:attribute} state_machine_name
:canonical: archivebox.crawls.models.Crawl.state_machine_name
:value: >
   'crawls.statemachines.CrawlMachine'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.state_machine_name
```

````

````{py:attribute} retry_at_field_name
:canonical: archivebox.crawls.models.Crawl.retry_at_field_name
:value: >
   'retry_at'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.retry_at_field_name
```

````

````{py:attribute} state_field_name
:canonical: archivebox.crawls.models.Crawl.state_field_name
:value: >
   'status'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.state_field_name
```

````

````{py:attribute} StatusChoices
:canonical: archivebox.crawls.models.Crawl.StatusChoices
:value: >
   None

```{autodoc2-docstring} archivebox.crawls.models.Crawl.StatusChoices
```

````

````{py:attribute} active_state
:canonical: archivebox.crawls.models.Crawl.active_state
:value: >
   None

```{autodoc2-docstring} archivebox.crawls.models.Crawl.active_state
```

````

````{py:attribute} id
:canonical: archivebox.crawls.models.Crawl.id
:value: >
   'UUIDField(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.id
```

````

````{py:attribute} abid
:canonical: archivebox.crawls.models.Crawl.abid
:value: >
   'ABIDField(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.abid
```

````

````{py:attribute} created_by
:canonical: archivebox.crawls.models.Crawl.created_by
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.created_by
```

````

````{py:attribute} created_at
:canonical: archivebox.crawls.models.Crawl.created_at
:value: >
   'AutoDateTimeField(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.created_at
```

````

````{py:attribute} modified_at
:canonical: archivebox.crawls.models.Crawl.modified_at
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.modified_at
```

````

````{py:attribute} status
:canonical: archivebox.crawls.models.Crawl.status
:value: >
   'StatusField(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.status
```

````

````{py:attribute} retry_at
:canonical: archivebox.crawls.models.Crawl.retry_at
:value: >
   'RetryAtField(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.retry_at
```

````

````{py:attribute} seed
:canonical: archivebox.crawls.models.Crawl.seed
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.seed
```

````

````{py:attribute} label
:canonical: archivebox.crawls.models.Crawl.label
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.label
```

````

````{py:attribute} notes
:canonical: archivebox.crawls.models.Crawl.notes
:value: >
   'TextField(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.notes
```

````

````{py:attribute} max_depth
:canonical: archivebox.crawls.models.Crawl.max_depth
:value: >
   'PositiveSmallIntegerField(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.max_depth
```

````

````{py:attribute} tags_str
:canonical: archivebox.crawls.models.Crawl.tags_str
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.tags_str
```

````

````{py:attribute} persona
:canonical: archivebox.crawls.models.Crawl.persona
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.persona
```

````

````{py:attribute} config
:canonical: archivebox.crawls.models.Crawl.config
:value: >
   'JSONField(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.config
```

````

````{py:attribute} schedule
:canonical: archivebox.crawls.models.Crawl.schedule
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.schedule
```

````

````{py:attribute} snapshot_set
:canonical: archivebox.crawls.models.Crawl.snapshot_set
:type: django.db.models.Manager[core.models.Snapshot]
:value: >
   None

```{autodoc2-docstring} archivebox.crawls.models.Crawl.snapshot_set
```

````

`````{py:class} Meta
:canonical: archivebox.crawls.models.Crawl.Meta

Bases: {py:obj}`django_stubs_ext.db.models.TypedModelMeta`

````{py:attribute} verbose_name
:canonical: archivebox.crawls.models.Crawl.Meta.verbose_name
:value: >
   'Crawl'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.Meta.verbose_name
```

````

````{py:attribute} verbose_name_plural
:canonical: archivebox.crawls.models.Crawl.Meta.verbose_name_plural
:value: >
   'Crawls'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.Meta.verbose_name_plural
```

````

`````

````{py:method} __str__()
:canonical: archivebox.crawls.models.Crawl.__str__

````

````{py:method} from_seed(seed: seeds.models.Seed, max_depth: int = 0, persona: str = 'Default', tags_str: str = '', config: dict | None = None, created_by: int | None = None)
:canonical: archivebox.crawls.models.Crawl.from_seed
:classmethod:

```{autodoc2-docstring} archivebox.crawls.models.Crawl.from_seed
```

````

````{py:property} template
:canonical: archivebox.crawls.models.Crawl.template

```{autodoc2-docstring} archivebox.crawls.models.Crawl.template
```

````

````{py:property} api_url
:canonical: archivebox.crawls.models.Crawl.api_url
:type: str

````

````{py:property} api_docs_url
:canonical: archivebox.crawls.models.Crawl.api_docs_url
:type: str

````

````{py:method} pending_snapshots() -> django.db.models.QuerySet[core.models.Snapshot]
:canonical: archivebox.crawls.models.Crawl.pending_snapshots

```{autodoc2-docstring} archivebox.crawls.models.Crawl.pending_snapshots
```

````

````{py:method} pending_archiveresults() -> django.db.models.QuerySet[core.models.ArchiveResult]
:canonical: archivebox.crawls.models.Crawl.pending_archiveresults

```{autodoc2-docstring} archivebox.crawls.models.Crawl.pending_archiveresults
```

````

````{py:method} create_root_snapshot() -> core.models.Snapshot
:canonical: archivebox.crawls.models.Crawl.create_root_snapshot

```{autodoc2-docstring} archivebox.crawls.models.Crawl.create_root_snapshot
```

````

``````

``````{py:class} Outlink(*args, **kwargs)
:canonical: archivebox.crawls.models.Outlink

Bases: {py:obj}`django.db.models.Model`

```{autodoc2-docstring} archivebox.crawls.models.Outlink
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.crawls.models.Outlink.__init__
```

````{py:attribute} id
:canonical: archivebox.crawls.models.Outlink.id
:value: >
   'UUIDField(...)'

```{autodoc2-docstring} archivebox.crawls.models.Outlink.id
```

````

````{py:attribute} src
:canonical: archivebox.crawls.models.Outlink.src
:value: >
   'URLField(...)'

```{autodoc2-docstring} archivebox.crawls.models.Outlink.src
```

````

````{py:attribute} dst
:canonical: archivebox.crawls.models.Outlink.dst
:value: >
   'URLField(...)'

```{autodoc2-docstring} archivebox.crawls.models.Outlink.dst
```

````

````{py:attribute} crawl
:canonical: archivebox.crawls.models.Outlink.crawl
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.crawls.models.Outlink.crawl
```

````

````{py:attribute} via
:canonical: archivebox.crawls.models.Outlink.via
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.crawls.models.Outlink.via
```

````

`````{py:class} Meta
:canonical: archivebox.crawls.models.Outlink.Meta

```{autodoc2-docstring} archivebox.crawls.models.Outlink.Meta
```

````{py:attribute} unique_together
:canonical: archivebox.crawls.models.Outlink.Meta.unique_together
:value: >
   (('src', 'dst', 'via'),)

```{autodoc2-docstring} archivebox.crawls.models.Outlink.Meta.unique_together
```

````

`````

``````
