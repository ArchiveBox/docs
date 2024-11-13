# {py:mod}`archivebox.actors.actor`

```{py:module} archivebox.actors.actor
```

```{autodoc2-docstring} archivebox.actors.actor
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ActorType <archivebox.actors.actor.ActorType>`
  - ```{autodoc2-docstring} archivebox.actors.actor.ActorType
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`compile_sql_select <archivebox.actors.actor.compile_sql_select>`
  - ```{autodoc2-docstring} archivebox.actors.actor.compile_sql_select
    :summary:
    ```
* - {py:obj}`compile_sql_update <archivebox.actors.actor.compile_sql_update>`
  - ```{autodoc2-docstring} archivebox.actors.actor.compile_sql_update
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.actors.actor.__package__>`
  - ```{autodoc2-docstring} archivebox.actors.actor.__package__
    :summary:
    ```
* - {py:obj}`CPU_COUNT <archivebox.actors.actor.CPU_COUNT>`
  - ```{autodoc2-docstring} archivebox.actors.actor.CPU_COUNT
    :summary:
    ```
* - {py:obj}`DEFAULT_MAX_TICK_TIME <archivebox.actors.actor.DEFAULT_MAX_TICK_TIME>`
  - ```{autodoc2-docstring} archivebox.actors.actor.DEFAULT_MAX_TICK_TIME
    :summary:
    ```
* - {py:obj}`DEFAULT_MAX_CONCURRENT_ACTORS <archivebox.actors.actor.DEFAULT_MAX_CONCURRENT_ACTORS>`
  - ```{autodoc2-docstring} archivebox.actors.actor.DEFAULT_MAX_CONCURRENT_ACTORS
    :summary:
    ```
* - {py:obj}`limit <archivebox.actors.actor.limit>`
  - ```{autodoc2-docstring} archivebox.actors.actor.limit
    :summary:
    ```
* - {py:obj}`LaunchKwargs <archivebox.actors.actor.LaunchKwargs>`
  - ```{autodoc2-docstring} archivebox.actors.actor.LaunchKwargs
    :summary:
    ```
* - {py:obj}`ObjectState <archivebox.actors.actor.ObjectState>`
  - ```{autodoc2-docstring} archivebox.actors.actor.ObjectState
    :summary:
    ```
* - {py:obj}`ObjectStateList <archivebox.actors.actor.ObjectStateList>`
  - ```{autodoc2-docstring} archivebox.actors.actor.ObjectStateList
    :summary:
    ```
* - {py:obj}`ModelType <archivebox.actors.actor.ModelType>`
  - ```{autodoc2-docstring} archivebox.actors.actor.ModelType
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.actors.actor.__package__
:value: >
   'archivebox.actors'

```{autodoc2-docstring} archivebox.actors.actor.__package__
```

````

````{py:exception} ActorObjectAlreadyClaimed()
:canonical: archivebox.actors.actor.ActorObjectAlreadyClaimed

Bases: {py:obj}`Exception`

```{autodoc2-docstring} archivebox.actors.actor.ActorObjectAlreadyClaimed
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.actors.actor.ActorObjectAlreadyClaimed.__init__
```

````

````{py:exception} ActorQueueIsEmpty()
:canonical: archivebox.actors.actor.ActorQueueIsEmpty

Bases: {py:obj}`Exception`

```{autodoc2-docstring} archivebox.actors.actor.ActorQueueIsEmpty
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.actors.actor.ActorQueueIsEmpty.__init__
```

````

````{py:data} CPU_COUNT
:canonical: archivebox.actors.actor.CPU_COUNT
:value: >
   'cpu_count(...)'

```{autodoc2-docstring} archivebox.actors.actor.CPU_COUNT
```

````

````{py:data} DEFAULT_MAX_TICK_TIME
:canonical: archivebox.actors.actor.DEFAULT_MAX_TICK_TIME
:value: >
   60

```{autodoc2-docstring} archivebox.actors.actor.DEFAULT_MAX_TICK_TIME
```

````

````{py:data} DEFAULT_MAX_CONCURRENT_ACTORS
:canonical: archivebox.actors.actor.DEFAULT_MAX_CONCURRENT_ACTORS
:value: >
   'min(...)'

```{autodoc2-docstring} archivebox.actors.actor.DEFAULT_MAX_CONCURRENT_ACTORS
```

````

````{py:data} limit
:canonical: archivebox.actors.actor.limit
:value: >
   None

```{autodoc2-docstring} archivebox.actors.actor.limit
```

````

````{py:data} LaunchKwargs
:canonical: archivebox.actors.actor.LaunchKwargs
:value: >
   None

```{autodoc2-docstring} archivebox.actors.actor.LaunchKwargs
```

````

````{py:data} ObjectState
:canonical: archivebox.actors.actor.ObjectState
:value: >
   None

```{autodoc2-docstring} archivebox.actors.actor.ObjectState
```

````

````{py:data} ObjectStateList
:canonical: archivebox.actors.actor.ObjectStateList
:value: >
   None

```{autodoc2-docstring} archivebox.actors.actor.ObjectStateList
```

````

````{py:data} ModelType
:canonical: archivebox.actors.actor.ModelType
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} archivebox.actors.actor.ModelType
```

````

`````{py:class} ActorType(mode: typing.Literal[thread, process] | None = None, **launch_kwargs: archivebox.actors.actor.LaunchKwargs)
:canonical: archivebox.actors.actor.ActorType

Bases: {py:obj}`typing.Generic`\[{py:obj}`archivebox.actors.actor.ModelType`\]

```{autodoc2-docstring} archivebox.actors.actor.ActorType
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.actors.actor.ActorType.__init__
```

````{py:attribute} Model
:canonical: archivebox.actors.actor.ActorType.Model
:type: typing.Type[archivebox.actors.actor.ModelType]
:value: >
   None

```{autodoc2-docstring} archivebox.actors.actor.ActorType.Model
```

````

````{py:attribute} StateMachineClass
:canonical: archivebox.actors.actor.ActorType.StateMachineClass
:type: typing.Type[statemachine.StateMachine]
:value: >
   None

```{autodoc2-docstring} archivebox.actors.actor.ActorType.StateMachineClass
```

````

````{py:attribute} STATE_FIELD_NAME
:canonical: archivebox.actors.actor.ActorType.STATE_FIELD_NAME
:type: typing.ClassVar[str]
:value: >
   None

```{autodoc2-docstring} archivebox.actors.actor.ActorType.STATE_FIELD_NAME
```

````

````{py:attribute} ACTIVE_STATE
:canonical: archivebox.actors.actor.ActorType.ACTIVE_STATE
:type: typing.ClassVar[archivebox.actors.actor.ObjectState]
:value: >
   None

```{autodoc2-docstring} archivebox.actors.actor.ActorType.ACTIVE_STATE
```

````

````{py:attribute} FINAL_STATES
:canonical: archivebox.actors.actor.ActorType.FINAL_STATES
:type: typing.ClassVar[archivebox.actors.actor.ObjectStateList]
:value: >
   None

```{autodoc2-docstring} archivebox.actors.actor.ActorType.FINAL_STATES
```

````

````{py:attribute} EVENT_NAME
:canonical: archivebox.actors.actor.ActorType.EVENT_NAME
:type: typing.ClassVar[str]
:value: >
   'tick'

```{autodoc2-docstring} archivebox.actors.actor.ActorType.EVENT_NAME
```

````

````{py:attribute} CLAIM_ORDER
:canonical: archivebox.actors.actor.ActorType.CLAIM_ORDER
:type: typing.ClassVar[tuple[str, ...]]
:value: >
   ('retry_at',)

```{autodoc2-docstring} archivebox.actors.actor.ActorType.CLAIM_ORDER
```

````

````{py:attribute} CLAIM_FROM_TOP_N
:canonical: archivebox.actors.actor.ActorType.CLAIM_FROM_TOP_N
:type: typing.ClassVar[int]
:value: >
   None

```{autodoc2-docstring} archivebox.actors.actor.ActorType.CLAIM_FROM_TOP_N
```

````

````{py:attribute} CLAIM_ATOMIC
:canonical: archivebox.actors.actor.ActorType.CLAIM_ATOMIC
:type: typing.ClassVar[bool]
:value: >
   True

```{autodoc2-docstring} archivebox.actors.actor.ActorType.CLAIM_ATOMIC
```

````

````{py:attribute} MAX_TICK_TIME
:canonical: archivebox.actors.actor.ActorType.MAX_TICK_TIME
:type: typing.ClassVar[int]
:value: >
   None

```{autodoc2-docstring} archivebox.actors.actor.ActorType.MAX_TICK_TIME
```

````

````{py:attribute} MAX_CONCURRENT_ACTORS
:canonical: archivebox.actors.actor.ActorType.MAX_CONCURRENT_ACTORS
:type: typing.ClassVar[int]
:value: >
   None

```{autodoc2-docstring} archivebox.actors.actor.ActorType.MAX_CONCURRENT_ACTORS
```

````

````{py:attribute} _SPAWNED_ACTOR_PIDS
:canonical: archivebox.actors.actor.ActorType._SPAWNED_ACTOR_PIDS
:type: typing.ClassVar[list[psutil.Process]]
:value: >
   []

```{autodoc2-docstring} archivebox.actors.actor.ActorType._SPAWNED_ACTOR_PIDS
```

````

````{py:attribute} pid
:canonical: archivebox.actors.actor.ActorType.pid
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.actors.actor.ActorType.pid
```

````

````{py:attribute} idle_count
:canonical: archivebox.actors.actor.ActorType.idle_count
:type: int
:value: >
   0

```{autodoc2-docstring} archivebox.actors.actor.ActorType.idle_count
```

````

````{py:attribute} launch_kwargs
:canonical: archivebox.actors.actor.ActorType.launch_kwargs
:type: archivebox.actors.actor.LaunchKwargs
:value: >
   None

```{autodoc2-docstring} archivebox.actors.actor.ActorType.launch_kwargs
```

````

````{py:attribute} mode
:canonical: archivebox.actors.actor.ActorType.mode
:type: typing.Literal[thread, process]
:value: >
   'process'

```{autodoc2-docstring} archivebox.actors.actor.ActorType.mode
```

````

````{py:method} __init_subclass__() -> None
:canonical: archivebox.actors.actor.ActorType.__init_subclass__
:classmethod:

```{autodoc2-docstring} archivebox.actors.actor.ActorType.__init_subclass__
```

````

````{py:method} name() -> str
:canonical: archivebox.actors.actor.ActorType.name

```{autodoc2-docstring} archivebox.actors.actor.ActorType.name
```

````

````{py:method} __str__() -> str
:canonical: archivebox.actors.actor.ActorType.__str__

````

````{py:method} __repr__() -> str
:canonical: archivebox.actors.actor.ActorType.__repr__

```{autodoc2-docstring} archivebox.actors.actor.ActorType.__repr__
```

````

````{py:method} _state_to_str(state: archivebox.actors.actor.ObjectState) -> str
:canonical: archivebox.actors.actor.ActorType._state_to_str
:staticmethod:

```{autodoc2-docstring} archivebox.actors.actor.ActorType._state_to_str
```

````

````{py:method} _sql_for_select_top_n_candidates(qs: django.db.models.QuerySet, claim_from_top_n: int = CLAIM_FROM_TOP_N) -> tuple[str, tuple[typing.Any, ...]]
:canonical: archivebox.actors.actor.ActorType._sql_for_select_top_n_candidates
:staticmethod:

```{autodoc2-docstring} archivebox.actors.actor.ActorType._sql_for_select_top_n_candidates
```

````

````{py:method} _sql_for_update_claimed_obj(qs: django.db.models.QuerySet, update_kwargs: dict[str, typing.Any]) -> tuple[str, tuple[typing.Any, ...]]
:canonical: archivebox.actors.actor.ActorType._sql_for_update_claimed_obj
:staticmethod:

```{autodoc2-docstring} archivebox.actors.actor.ActorType._sql_for_update_claimed_obj
```

````

````{py:method} _get_model_from_generic_typevar() -> typing.Type[archivebox.actors.actor.ModelType]
:canonical: archivebox.actors.actor.ActorType._get_model_from_generic_typevar
:classmethod:

```{autodoc2-docstring} archivebox.actors.actor.ActorType._get_model_from_generic_typevar
```

````

````{py:method} _get_state_machine_cls(Model: typing.Type[archivebox.actors.actor.ModelType]) -> typing.Type[archivebox.actors.actor.ActorType._get_state_machine_cls.StateMachine]
:canonical: archivebox.actors.actor.ActorType._get_state_machine_cls
:staticmethod:

```{autodoc2-docstring} archivebox.actors.actor.ActorType._get_state_machine_cls
```

````

````{py:method} _get_state_machine_instance(obj: archivebox.actors.actor.ModelType) -> statemachine.StateMachine
:canonical: archivebox.actors.actor.ActorType._get_state_machine_instance
:classmethod:

```{autodoc2-docstring} archivebox.actors.actor.ActorType._get_state_machine_instance
```

````

````{py:method} _populate_missing_classvars_from_model(Model: typing.Type[archivebox.actors.actor.ModelType])
:canonical: archivebox.actors.actor.ActorType._populate_missing_classvars_from_model
:classmethod:

```{autodoc2-docstring} archivebox.actors.actor.ActorType._populate_missing_classvars_from_model
```

````

````{py:method} _fork_actor_as_thread(**launch_kwargs: archivebox.actors.actor.LaunchKwargs) -> int
:canonical: archivebox.actors.actor.ActorType._fork_actor_as_thread
:classmethod:

```{autodoc2-docstring} archivebox.actors.actor.ActorType._fork_actor_as_thread
```

````

````{py:method} _fork_actor_as_process(**launch_kwargs: archivebox.actors.actor.LaunchKwargs) -> int
:canonical: archivebox.actors.actor.ActorType._fork_actor_as_process
:classmethod:

```{autodoc2-docstring} archivebox.actors.actor.ActorType._fork_actor_as_process
```

````

````{py:method} get_running_actors() -> list[int]
:canonical: archivebox.actors.actor.ActorType.get_running_actors
:classmethod:

```{autodoc2-docstring} archivebox.actors.actor.ActorType.get_running_actors
```

````

````{py:method} get_actors_to_spawn(queue: django.db.models.QuerySet, running_actors: list[int]) -> list[archivebox.actors.actor.LaunchKwargs]
:canonical: archivebox.actors.actor.ActorType.get_actors_to_spawn
:classmethod:

```{autodoc2-docstring} archivebox.actors.actor.ActorType.get_actors_to_spawn
```

````

````{py:method} start(mode: typing.Literal[thread, process] = 'process', **launch_kwargs: archivebox.actors.actor.LaunchKwargs) -> int
:canonical: archivebox.actors.actor.ActorType.start
:classmethod:

```{autodoc2-docstring} archivebox.actors.actor.ActorType.start
```

````

````{py:method} qs() -> django.db.models.QuerySet[archivebox.actors.actor.ModelType]
:canonical: archivebox.actors.actor.ActorType.qs

```{autodoc2-docstring} archivebox.actors.actor.ActorType.qs
```

````

````{py:method} final_q() -> django.db.models.Q
:canonical: archivebox.actors.actor.ActorType.final_q

```{autodoc2-docstring} archivebox.actors.actor.ActorType.final_q
```

````

````{py:method} active_q() -> django.db.models.Q
:canonical: archivebox.actors.actor.ActorType.active_q

```{autodoc2-docstring} archivebox.actors.actor.ActorType.active_q
```

````

````{py:method} stalled_q() -> django.db.models.Q
:canonical: archivebox.actors.actor.ActorType.stalled_q

```{autodoc2-docstring} archivebox.actors.actor.ActorType.stalled_q
```

````

````{py:method} future_q() -> django.db.models.Q
:canonical: archivebox.actors.actor.ActorType.future_q

```{autodoc2-docstring} archivebox.actors.actor.ActorType.future_q
```

````

````{py:method} pending_q() -> django.db.models.Q
:canonical: archivebox.actors.actor.ActorType.pending_q

```{autodoc2-docstring} archivebox.actors.actor.ActorType.pending_q
```

````

````{py:method} get_queue(sort: bool = True) -> django.db.models.QuerySet[archivebox.actors.actor.ModelType]
:canonical: archivebox.actors.actor.ActorType.get_queue
:classmethod:

```{autodoc2-docstring} archivebox.actors.actor.ActorType.get_queue
```

````

````{py:method} runloop()
:canonical: archivebox.actors.actor.ActorType.runloop

```{autodoc2-docstring} archivebox.actors.actor.ActorType.runloop
```

````

````{py:method} get_update_kwargs_to_claim_obj() -> dict[str, typing.Any]
:canonical: archivebox.actors.actor.ActorType.get_update_kwargs_to_claim_obj

```{autodoc2-docstring} archivebox.actors.actor.ActorType.get_update_kwargs_to_claim_obj
```

````

````{py:method} get_next(atomic: bool | None = None) -> archivebox.actors.actor.ModelType | None
:canonical: archivebox.actors.actor.ActorType.get_next

```{autodoc2-docstring} archivebox.actors.actor.ActorType.get_next
```

````

````{py:method} get_next_non_atomic() -> archivebox.actors.actor.ModelType
:canonical: archivebox.actors.actor.ActorType.get_next_non_atomic

```{autodoc2-docstring} archivebox.actors.actor.ActorType.get_next_non_atomic
```

````

````{py:method} get_next_atomic() -> archivebox.actors.actor.ModelType | None
:canonical: archivebox.actors.actor.ActorType.get_next_atomic

```{autodoc2-docstring} archivebox.actors.actor.ActorType.get_next_atomic
```

````

````{py:method} tick(obj_to_process: archivebox.actors.actor.ModelType) -> None
:canonical: archivebox.actors.actor.ActorType.tick

```{autodoc2-docstring} archivebox.actors.actor.ActorType.tick
```

````

````{py:method} on_startup() -> None
:canonical: archivebox.actors.actor.ActorType.on_startup

```{autodoc2-docstring} archivebox.actors.actor.ActorType.on_startup
```

````

````{py:method} on_shutdown(last_obj: archivebox.actors.actor.ModelType | None = None, last_error: BaseException | None = None) -> None
:canonical: archivebox.actors.actor.ActorType.on_shutdown

```{autodoc2-docstring} archivebox.actors.actor.ActorType.on_shutdown
```

````

````{py:method} on_tick_start(obj_to_process: archivebox.actors.actor.ModelType) -> None
:canonical: archivebox.actors.actor.ActorType.on_tick_start

```{autodoc2-docstring} archivebox.actors.actor.ActorType.on_tick_start
```

````

````{py:method} on_tick_end(obj_to_process: archivebox.actors.actor.ModelType) -> None
:canonical: archivebox.actors.actor.ActorType.on_tick_end

```{autodoc2-docstring} archivebox.actors.actor.ActorType.on_tick_end
```

````

````{py:method} on_tick_exception(obj_to_process: archivebox.actors.actor.ModelType, error: Exception) -> None
:canonical: archivebox.actors.actor.ActorType.on_tick_exception

```{autodoc2-docstring} archivebox.actors.actor.ActorType.on_tick_exception
```

````

`````

````{py:function} compile_sql_select(queryset: django.db.models.QuerySet, filter_kwargs: dict[str, typing.Any] | None = None, order_args: tuple[str, ...] = (), limit: int | None = None) -> tuple[str, tuple[typing.Any, ...]]
:canonical: archivebox.actors.actor.compile_sql_select

```{autodoc2-docstring} archivebox.actors.actor.compile_sql_select
```
````

````{py:function} compile_sql_update(queryset: django.db.models.QuerySet, update_kwargs: dict[str, typing.Any], filter_kwargs: dict[str, typing.Any] | None = None) -> tuple[str, tuple[typing.Any, ...]]
:canonical: archivebox.actors.actor.compile_sql_update

```{autodoc2-docstring} archivebox.actors.actor.compile_sql_update
```
````
