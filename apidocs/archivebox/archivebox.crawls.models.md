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
  -
* - {py:obj}`Crawl <archivebox.crawls.models.Crawl>`
  -
* - {py:obj}`CrawlMachine <archivebox.crawls.models.CrawlMachine>`
  - ```{autodoc2-docstring} archivebox.crawls.models.CrawlMachine
    :summary:
    ```
````

### API

``````{py:class} CrawlSchedule(*args, **kwargs)
:canonical: archivebox.crawls.models.CrawlSchedule

Bases: {py:obj}`archivebox.base_models.models.ModelWithUUID`, {py:obj}`archivebox.base_models.models.ModelWithNotes`

````{py:attribute} id
:canonical: archivebox.crawls.models.CrawlSchedule.id
:value: >
   'UUIDField(...)'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.id
```

````

````{py:attribute} created_at
:canonical: archivebox.crawls.models.CrawlSchedule.created_at
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.created_at
```

````

````{py:attribute} created_by
:canonical: archivebox.crawls.models.CrawlSchedule.created_by
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.created_by
```

````

````{py:attribute} modified_at
:canonical: archivebox.crawls.models.CrawlSchedule.modified_at
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.modified_at
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

````{py:attribute} schedule
:canonical: archivebox.crawls.models.CrawlSchedule.schedule
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.schedule
```

````

````{py:attribute} is_enabled
:canonical: archivebox.crawls.models.CrawlSchedule.is_enabled
:value: >
   'BooleanField(...)'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.is_enabled
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

````{py:attribute} app_label
:canonical: archivebox.crawls.models.CrawlSchedule.Meta.app_label
:value: >
   'crawls'

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.Meta.app_label
```

````

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

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.api_url
```

````

````{py:method} save(*args, **kwargs)
:canonical: archivebox.crawls.models.CrawlSchedule.save

````

````{py:property} last_run_at
:canonical: archivebox.crawls.models.CrawlSchedule.last_run_at

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.last_run_at
```

````

````{py:property} next_run_at
:canonical: archivebox.crawls.models.CrawlSchedule.next_run_at

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.next_run_at
```

````

````{py:method} is_due(now=None) -> bool
:canonical: archivebox.crawls.models.CrawlSchedule.is_due

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.is_due
```

````

````{py:method} enqueue(queued_at=None) -> archivebox.crawls.models.Crawl
:canonical: archivebox.crawls.models.CrawlSchedule.enqueue

```{autodoc2-docstring} archivebox.crawls.models.CrawlSchedule.enqueue
```

````

``````

``````{py:class} Crawl(*args, **kwargs)
:canonical: archivebox.crawls.models.Crawl

Bases: {py:obj}`archivebox.base_models.models.ModelWithOutputDir`, {py:obj}`archivebox.base_models.models.ModelWithConfig`, {py:obj}`archivebox.base_models.models.ModelWithHealthStats`, {py:obj}`archivebox.workers.models.ModelWithStateMachine`

````{py:attribute} id
:canonical: archivebox.crawls.models.Crawl.id
:value: >
   'UUIDField(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.id
```

````

````{py:attribute} created_at
:canonical: archivebox.crawls.models.Crawl.created_at
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.created_at
```

````

````{py:attribute} created_by
:canonical: archivebox.crawls.models.Crawl.created_by
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.created_by
```

````

````{py:attribute} modified_at
:canonical: archivebox.crawls.models.Crawl.modified_at
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.modified_at
```

````

````{py:attribute} urls
:canonical: archivebox.crawls.models.Crawl.urls
:value: >
   'TextField(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.urls
```

````

````{py:attribute} config
:canonical: archivebox.crawls.models.Crawl.config
:value: >
   'JSONField(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.config
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

````{py:attribute} persona_id
:canonical: archivebox.crawls.models.Crawl.persona_id
:value: >
   'UUIDField(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.persona_id
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

````{py:attribute} schedule
:canonical: archivebox.crawls.models.Crawl.schedule
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.schedule
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

````{py:attribute} state_machine_name
:canonical: archivebox.crawls.models.Crawl.state_machine_name
:value: >
   'archivebox.crawls.models.CrawlMachine'

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

````{py:attribute} snapshot_set
:canonical: archivebox.crawls.models.Crawl.snapshot_set
:type: django.db.models.Manager[archivebox.core.models.Snapshot]
:value: >
   None

```{autodoc2-docstring} archivebox.crawls.models.Crawl.snapshot_set
```

````

`````{py:class} Meta
:canonical: archivebox.crawls.models.Crawl.Meta

Bases: {py:obj}`django_stubs_ext.db.models.TypedModelMeta`

````{py:attribute} app_label
:canonical: archivebox.crawls.models.Crawl.Meta.app_label
:value: >
   'crawls'

```{autodoc2-docstring} archivebox.crawls.models.Crawl.Meta.app_label
```

````

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

````{py:method} save(*args, **kwargs)
:canonical: archivebox.crawls.models.Crawl.save

````

````{py:property} api_url
:canonical: archivebox.crawls.models.Crawl.api_url
:type: str

```{autodoc2-docstring} archivebox.crawls.models.Crawl.api_url
```

````

````{py:method} to_json() -> dict
:canonical: archivebox.crawls.models.Crawl.to_json

```{autodoc2-docstring} archivebox.crawls.models.Crawl.to_json
```

````

````{py:method} from_json(record: dict, overrides: dict = None)
:canonical: archivebox.crawls.models.Crawl.from_json
:staticmethod:

```{autodoc2-docstring} archivebox.crawls.models.Crawl.from_json
```

````

````{py:property} output_dir
:canonical: archivebox.crawls.models.Crawl.output_dir
:type: pathlib.Path

```{autodoc2-docstring} archivebox.crawls.models.Crawl.output_dir
```

````

````{py:method} get_urls_list() -> list[str]
:canonical: archivebox.crawls.models.Crawl.get_urls_list

```{autodoc2-docstring} archivebox.crawls.models.Crawl.get_urls_list
```

````

````{py:method} get_system_task() -> str | None
:canonical: archivebox.crawls.models.Crawl.get_system_task

```{autodoc2-docstring} archivebox.crawls.models.Crawl.get_system_task
```

````

````{py:method} add_url(entry: dict) -> bool
:canonical: archivebox.crawls.models.Crawl.add_url

```{autodoc2-docstring} archivebox.crawls.models.Crawl.add_url
```

````

````{py:method} create_snapshots_from_urls() -> list[archivebox.core.models.Snapshot]
:canonical: archivebox.crawls.models.Crawl.create_snapshots_from_urls

```{autodoc2-docstring} archivebox.crawls.models.Crawl.create_snapshots_from_urls
```

````

````{py:method} run() -> Snapshot | None
:canonical: archivebox.crawls.models.Crawl.run

```{autodoc2-docstring} archivebox.crawls.models.Crawl.run
```

````

````{py:method} is_finished() -> bool
:canonical: archivebox.crawls.models.Crawl.is_finished

```{autodoc2-docstring} archivebox.crawls.models.Crawl.is_finished
```

````

````{py:method} cleanup()
:canonical: archivebox.crawls.models.Crawl.cleanup

```{autodoc2-docstring} archivebox.crawls.models.Crawl.cleanup
```

````

``````

`````{py:class} CrawlMachine(obj, *args, **kwargs)
:canonical: archivebox.crawls.models.CrawlMachine

Bases: {py:obj}`archivebox.workers.models.BaseStateMachine`

```{autodoc2-docstring} archivebox.crawls.models.CrawlMachine
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.crawls.models.CrawlMachine.__init__
```

````{py:attribute} model_attr_name
:canonical: archivebox.crawls.models.CrawlMachine.model_attr_name
:value: >
   'crawl'

```{autodoc2-docstring} archivebox.crawls.models.CrawlMachine.model_attr_name
```

````

````{py:attribute} queued
:canonical: archivebox.crawls.models.CrawlMachine.queued
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.crawls.models.CrawlMachine.queued
```

````

````{py:attribute} started
:canonical: archivebox.crawls.models.CrawlMachine.started
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.crawls.models.CrawlMachine.started
```

````

````{py:attribute} sealed
:canonical: archivebox.crawls.models.CrawlMachine.sealed
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.crawls.models.CrawlMachine.sealed
```

````

````{py:attribute} tick
:canonical: archivebox.crawls.models.CrawlMachine.tick
:value: >
   None

```{autodoc2-docstring} archivebox.crawls.models.CrawlMachine.tick
```

````

````{py:attribute} seal
:canonical: archivebox.crawls.models.CrawlMachine.seal
:value: >
   'to(...)'

```{autodoc2-docstring} archivebox.crawls.models.CrawlMachine.seal
```

````

````{py:method} can_start() -> bool
:canonical: archivebox.crawls.models.CrawlMachine.can_start

```{autodoc2-docstring} archivebox.crawls.models.CrawlMachine.can_start
```

````

````{py:method} is_finished() -> bool
:canonical: archivebox.crawls.models.CrawlMachine.is_finished

```{autodoc2-docstring} archivebox.crawls.models.CrawlMachine.is_finished
```

````

````{py:method} enter_started()
:canonical: archivebox.crawls.models.CrawlMachine.enter_started

```{autodoc2-docstring} archivebox.crawls.models.CrawlMachine.enter_started
```

````

````{py:method} enter_sealed()
:canonical: archivebox.crawls.models.CrawlMachine.enter_sealed

```{autodoc2-docstring} archivebox.crawls.models.CrawlMachine.enter_sealed
```

````

`````
