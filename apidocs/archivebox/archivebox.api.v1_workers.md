# {py:mod}`archivebox.api.v1_workers`

```{py:module} archivebox.api.v1_workers
```

```{autodoc2-docstring} archivebox.api.v1_workers
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`QueueItemSchema <archivebox.api.v1_workers.QueueItemSchema>`
  - ```{autodoc2-docstring} archivebox.api.v1_workers.QueueItemSchema
    :summary:
    ```
* - {py:obj}`WorkerSchema <archivebox.api.v1_workers.WorkerSchema>`
  - ```{autodoc2-docstring} archivebox.api.v1_workers.WorkerSchema
    :summary:
    ```
* - {py:obj}`OrchestratorSchema <archivebox.api.v1_workers.OrchestratorSchema>`
  - ```{autodoc2-docstring} archivebox.api.v1_workers.OrchestratorSchema
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_orchestrator <archivebox.api.v1_workers.get_orchestrator>`
  - ```{autodoc2-docstring} archivebox.api.v1_workers.get_orchestrator
    :summary:
    ```
* - {py:obj}`get_workers <archivebox.api.v1_workers.get_workers>`
  - ```{autodoc2-docstring} archivebox.api.v1_workers.get_workers
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`router <archivebox.api.v1_workers.router>`
  - ```{autodoc2-docstring} archivebox.api.v1_workers.router
    :summary:
    ```
````

### API

````{py:data} router
:canonical: archivebox.api.v1_workers.router
:value: >
   'Router(...)'

```{autodoc2-docstring} archivebox.api.v1_workers.router
```

````

`````{py:class} QueueItemSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_workers.QueueItemSchema

Bases: {py:obj}`ninja.Schema`

```{autodoc2-docstring} archivebox.api.v1_workers.QueueItemSchema
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.api.v1_workers.QueueItemSchema.__init__
```

````{py:attribute} TYPE
:canonical: archivebox.api.v1_workers.QueueItemSchema.TYPE
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_workers.QueueItemSchema.TYPE
```

````

````{py:attribute} id
:canonical: archivebox.api.v1_workers.QueueItemSchema.id
:type: uuid.UUID
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_workers.QueueItemSchema.id
```

````

````{py:attribute} status
:canonical: archivebox.api.v1_workers.QueueItemSchema.status
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_workers.QueueItemSchema.status
```

````

````{py:attribute} retry_at
:canonical: archivebox.api.v1_workers.QueueItemSchema.retry_at
:type: datetime.datetime | None
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_workers.QueueItemSchema.retry_at
```

````

````{py:attribute} created_at
:canonical: archivebox.api.v1_workers.QueueItemSchema.created_at
:type: datetime.datetime
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_workers.QueueItemSchema.created_at
```

````

````{py:attribute} modified_at
:canonical: archivebox.api.v1_workers.QueueItemSchema.modified_at
:type: datetime.datetime
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_workers.QueueItemSchema.modified_at
```

````

````{py:attribute} description
:canonical: archivebox.api.v1_workers.QueueItemSchema.description
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_workers.QueueItemSchema.description
```

````

````{py:method} resolve_TYPE(obj) -> str
:canonical: archivebox.api.v1_workers.QueueItemSchema.resolve_TYPE
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_workers.QueueItemSchema.resolve_TYPE
```

````

````{py:method} resolve_description(obj) -> str
:canonical: archivebox.api.v1_workers.QueueItemSchema.resolve_description
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_workers.QueueItemSchema.resolve_description
```

````

`````

`````{py:class} WorkerSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_workers.WorkerSchema

Bases: {py:obj}`ninja.Schema`

```{autodoc2-docstring} archivebox.api.v1_workers.WorkerSchema
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.api.v1_workers.WorkerSchema.__init__
```

````{py:attribute} name
:canonical: archivebox.api.v1_workers.WorkerSchema.name
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_workers.WorkerSchema.name
```

````

````{py:attribute} model
:canonical: archivebox.api.v1_workers.WorkerSchema.model
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_workers.WorkerSchema.model
```

````

````{py:attribute} max_tick_time
:canonical: archivebox.api.v1_workers.WorkerSchema.max_tick_time
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_workers.WorkerSchema.max_tick_time
```

````

````{py:attribute} max_concurrent_tasks
:canonical: archivebox.api.v1_workers.WorkerSchema.max_concurrent_tasks
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_workers.WorkerSchema.max_concurrent_tasks
```

````

````{py:attribute} running_count
:canonical: archivebox.api.v1_workers.WorkerSchema.running_count
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_workers.WorkerSchema.running_count
```

````

````{py:attribute} running_workers
:canonical: archivebox.api.v1_workers.WorkerSchema.running_workers
:type: typing.List[dict[str, typing.Any]]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_workers.WorkerSchema.running_workers
```

````

````{py:method} resolve_model(obj) -> str
:canonical: archivebox.api.v1_workers.WorkerSchema.resolve_model
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_workers.WorkerSchema.resolve_model
```

````

````{py:method} resolve_max_tick_time(obj) -> int
:canonical: archivebox.api.v1_workers.WorkerSchema.resolve_max_tick_time
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_workers.WorkerSchema.resolve_max_tick_time
```

````

````{py:method} resolve_max_concurrent_tasks(obj) -> int
:canonical: archivebox.api.v1_workers.WorkerSchema.resolve_max_concurrent_tasks
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_workers.WorkerSchema.resolve_max_concurrent_tasks
```

````

````{py:method} resolve_running_count(obj) -> int
:canonical: archivebox.api.v1_workers.WorkerSchema.resolve_running_count
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_workers.WorkerSchema.resolve_running_count
```

````

````{py:method} resolve_running_workers(obj) -> typing.List[dict[str, typing.Any]]
:canonical: archivebox.api.v1_workers.WorkerSchema.resolve_running_workers
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_workers.WorkerSchema.resolve_running_workers
```

````

`````

`````{py:class} OrchestratorSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_workers.OrchestratorSchema

Bases: {py:obj}`ninja.Schema`

```{autodoc2-docstring} archivebox.api.v1_workers.OrchestratorSchema
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.api.v1_workers.OrchestratorSchema.__init__
```

````{py:attribute} is_running
:canonical: archivebox.api.v1_workers.OrchestratorSchema.is_running
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_workers.OrchestratorSchema.is_running
```

````

````{py:attribute} poll_interval
:canonical: archivebox.api.v1_workers.OrchestratorSchema.poll_interval
:type: float
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_workers.OrchestratorSchema.poll_interval
```

````

````{py:attribute} idle_timeout
:canonical: archivebox.api.v1_workers.OrchestratorSchema.idle_timeout
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_workers.OrchestratorSchema.idle_timeout
```

````

````{py:attribute} max_crawl_workers
:canonical: archivebox.api.v1_workers.OrchestratorSchema.max_crawl_workers
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_workers.OrchestratorSchema.max_crawl_workers
```

````

````{py:attribute} total_worker_count
:canonical: archivebox.api.v1_workers.OrchestratorSchema.total_worker_count
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_workers.OrchestratorSchema.total_worker_count
```

````

````{py:attribute} workers
:canonical: archivebox.api.v1_workers.OrchestratorSchema.workers
:type: typing.List[archivebox.api.v1_workers.WorkerSchema]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_workers.OrchestratorSchema.workers
```

````

`````

````{py:function} get_orchestrator(request)
:canonical: archivebox.api.v1_workers.get_orchestrator

```{autodoc2-docstring} archivebox.api.v1_workers.get_orchestrator
```
````

````{py:function} get_workers(request)
:canonical: archivebox.api.v1_workers.get_workers

```{autodoc2-docstring} archivebox.api.v1_workers.get_workers
```
````
