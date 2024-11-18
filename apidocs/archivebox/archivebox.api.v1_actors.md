# {py:mod}`archivebox.api.v1_actors`

```{py:module} archivebox.api.v1_actors
```

```{autodoc2-docstring} archivebox.api.v1_actors
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TaskSchema <archivebox.api.v1_actors.TaskSchema>`
  -
* - {py:obj}`ActorSchema <archivebox.api.v1_actors.ActorSchema>`
  -
* - {py:obj}`OrchestratorSchema <archivebox.api.v1_actors.OrchestratorSchema>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_orchestrators <archivebox.api.v1_actors.get_orchestrators>`
  - ```{autodoc2-docstring} archivebox.api.v1_actors.get_orchestrators
    :summary:
    ```
* - {py:obj}`get_actors <archivebox.api.v1_actors.get_actors>`
  - ```{autodoc2-docstring} archivebox.api.v1_actors.get_actors
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`router <archivebox.api.v1_actors.router>`
  - ```{autodoc2-docstring} archivebox.api.v1_actors.router
    :summary:
    ```
````

### API

````{py:data} router
:canonical: archivebox.api.v1_actors.router
:value: >
   'Router(...)'

```{autodoc2-docstring} archivebox.api.v1_actors.router
```

````

`````{py:class} TaskSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_actors.TaskSchema

Bases: {py:obj}`ninja.Schema`

````{py:attribute} TYPE
:canonical: archivebox.api.v1_actors.TaskSchema.TYPE
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.TaskSchema.TYPE
```

````

````{py:attribute} id
:canonical: archivebox.api.v1_actors.TaskSchema.id
:type: uuid.UUID
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.TaskSchema.id
```

````

````{py:attribute} abid
:canonical: archivebox.api.v1_actors.TaskSchema.abid
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.TaskSchema.abid
```

````

````{py:attribute} description
:canonical: archivebox.api.v1_actors.TaskSchema.description
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.TaskSchema.description
```

````

````{py:attribute} status
:canonical: archivebox.api.v1_actors.TaskSchema.status
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.TaskSchema.status
```

````

````{py:attribute} retry_at
:canonical: archivebox.api.v1_actors.TaskSchema.retry_at
:type: datetime.datetime | None
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.TaskSchema.retry_at
```

````

````{py:attribute} created_at
:canonical: archivebox.api.v1_actors.TaskSchema.created_at
:type: datetime.datetime
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.TaskSchema.created_at
```

````

````{py:attribute} modified_at
:canonical: archivebox.api.v1_actors.TaskSchema.modified_at
:type: datetime.datetime
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.TaskSchema.modified_at
```

````

````{py:attribute} created_by_id
:canonical: archivebox.api.v1_actors.TaskSchema.created_by_id
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.TaskSchema.created_by_id
```

````

````{py:method} resolve_description(obj) -> str
:canonical: archivebox.api.v1_actors.TaskSchema.resolve_description
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_actors.TaskSchema.resolve_description
```

````

`````

`````{py:class} ActorSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_actors.ActorSchema

Bases: {py:obj}`ninja.Schema`

````{py:attribute} idle_count
:canonical: archivebox.api.v1_actors.ActorSchema.idle_count
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.ActorSchema.idle_count
```

````

````{py:attribute} launch_kwargs
:canonical: archivebox.api.v1_actors.ActorSchema.launch_kwargs
:type: dict[str, typing.Any]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.ActorSchema.launch_kwargs
```

````

````{py:attribute} mode
:canonical: archivebox.api.v1_actors.ActorSchema.mode
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.ActorSchema.mode
```

````

````{py:attribute} model
:canonical: archivebox.api.v1_actors.ActorSchema.model
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.ActorSchema.model
```

````

````{py:attribute} statemachine
:canonical: archivebox.api.v1_actors.ActorSchema.statemachine
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.ActorSchema.statemachine
```

````

````{py:attribute} STATE_FIELD_NAME
:canonical: archivebox.api.v1_actors.ActorSchema.STATE_FIELD_NAME
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.ActorSchema.STATE_FIELD_NAME
```

````

````{py:attribute} FINAL_STATES
:canonical: archivebox.api.v1_actors.ActorSchema.FINAL_STATES
:type: list[str]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.ActorSchema.FINAL_STATES
```

````

````{py:attribute} EVENT_NAME
:canonical: archivebox.api.v1_actors.ActorSchema.EVENT_NAME
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.ActorSchema.EVENT_NAME
```

````

````{py:attribute} CLAIM_ORDER
:canonical: archivebox.api.v1_actors.ActorSchema.CLAIM_ORDER
:type: list[str]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.ActorSchema.CLAIM_ORDER
```

````

````{py:attribute} CLAIM_FROM_TOP_N
:canonical: archivebox.api.v1_actors.ActorSchema.CLAIM_FROM_TOP_N
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.ActorSchema.CLAIM_FROM_TOP_N
```

````

````{py:attribute} CLAIM_ATOMIC
:canonical: archivebox.api.v1_actors.ActorSchema.CLAIM_ATOMIC
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.ActorSchema.CLAIM_ATOMIC
```

````

````{py:attribute} MAX_TICK_TIME
:canonical: archivebox.api.v1_actors.ActorSchema.MAX_TICK_TIME
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.ActorSchema.MAX_TICK_TIME
```

````

````{py:attribute} MAX_CONCURRENT_ACTORS
:canonical: archivebox.api.v1_actors.ActorSchema.MAX_CONCURRENT_ACTORS
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.ActorSchema.MAX_CONCURRENT_ACTORS
```

````

````{py:attribute} queue
:canonical: archivebox.api.v1_actors.ActorSchema.queue
:type: list[archivebox.api.v1_actors.TaskSchema]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.ActorSchema.queue
```

````

````{py:attribute} past
:canonical: archivebox.api.v1_actors.ActorSchema.past
:type: list[archivebox.api.v1_actors.TaskSchema]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.ActorSchema.past
```

````

````{py:method} resolve_model(obj) -> str
:canonical: archivebox.api.v1_actors.ActorSchema.resolve_model
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_actors.ActorSchema.resolve_model
```

````

````{py:method} resolve_statemachine(obj) -> str
:canonical: archivebox.api.v1_actors.ActorSchema.resolve_statemachine
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_actors.ActorSchema.resolve_statemachine
```

````

````{py:method} resolve_name(obj) -> str
:canonical: archivebox.api.v1_actors.ActorSchema.resolve_name
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_actors.ActorSchema.resolve_name
```

````

````{py:method} resolve_FINAL_STATES(obj) -> list[str]
:canonical: archivebox.api.v1_actors.ActorSchema.resolve_FINAL_STATES
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_actors.ActorSchema.resolve_FINAL_STATES
```

````

````{py:method} resolve_queue(obj) -> list[archivebox.api.v1_actors.TaskSchema]
:canonical: archivebox.api.v1_actors.ActorSchema.resolve_queue
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_actors.ActorSchema.resolve_queue
```

````

````{py:method} resolve_past(obj) -> list[archivebox.api.v1_actors.TaskSchema]
:canonical: archivebox.api.v1_actors.ActorSchema.resolve_past
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_actors.ActorSchema.resolve_past
```

````

`````

`````{py:class} OrchestratorSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_actors.OrchestratorSchema

Bases: {py:obj}`ninja.Schema`

````{py:attribute} exit_on_idle
:canonical: archivebox.api.v1_actors.OrchestratorSchema.exit_on_idle
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.OrchestratorSchema.exit_on_idle
```

````

````{py:attribute} mode
:canonical: archivebox.api.v1_actors.OrchestratorSchema.mode
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.OrchestratorSchema.mode
```

````

````{py:attribute} actors
:canonical: archivebox.api.v1_actors.OrchestratorSchema.actors
:type: list[archivebox.api.v1_actors.ActorSchema]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_actors.OrchestratorSchema.actors
```

````

````{py:method} resolve_actors(obj) -> list[archivebox.api.v1_actors.ActorSchema]
:canonical: archivebox.api.v1_actors.OrchestratorSchema.resolve_actors
:staticmethod:

```{autodoc2-docstring} archivebox.api.v1_actors.OrchestratorSchema.resolve_actors
```

````

`````

````{py:function} get_orchestrators(request)
:canonical: archivebox.api.v1_actors.get_orchestrators

```{autodoc2-docstring} archivebox.api.v1_actors.get_orchestrators
```
````

````{py:function} get_actors(request)
:canonical: archivebox.api.v1_actors.get_actors

```{autodoc2-docstring} archivebox.api.v1_actors.get_actors
```
````
