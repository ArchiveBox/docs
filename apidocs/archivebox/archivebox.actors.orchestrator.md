# {py:mod}`archivebox.actors.orchestrator`

```{py:module} archivebox.actors.orchestrator
```

```{autodoc2-docstring} archivebox.actors.orchestrator
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Orchestrator <archivebox.actors.orchestrator.Orchestrator>`
  - ```{autodoc2-docstring} archivebox.actors.orchestrator.Orchestrator
    :summary:
    ```
````

### API

`````{py:class} Orchestrator(actor_types: typing.Dict[str, typing.Type[archivebox.actors.actor.ActorType]] | None = None, mode: typing.Literal[thread, process] | None = None, exit_on_idle: bool = True)
:canonical: archivebox.actors.orchestrator.Orchestrator

```{autodoc2-docstring} archivebox.actors.orchestrator.Orchestrator
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.actors.orchestrator.Orchestrator.__init__
```

````{py:attribute} pid
:canonical: archivebox.actors.orchestrator.Orchestrator.pid
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.actors.orchestrator.Orchestrator.pid
```

````

````{py:attribute} idle_count
:canonical: archivebox.actors.orchestrator.Orchestrator.idle_count
:type: int
:value: >
   0

```{autodoc2-docstring} archivebox.actors.orchestrator.Orchestrator.idle_count
```

````

````{py:attribute} actor_types
:canonical: archivebox.actors.orchestrator.Orchestrator.actor_types
:type: typing.Dict[str, typing.Type[archivebox.actors.actor.ActorType]]
:value: >
   None

```{autodoc2-docstring} archivebox.actors.orchestrator.Orchestrator.actor_types
```

````

````{py:attribute} mode
:canonical: archivebox.actors.orchestrator.Orchestrator.mode
:type: typing.Literal[thread, process]
:value: >
   'process'

```{autodoc2-docstring} archivebox.actors.orchestrator.Orchestrator.mode
```

````

````{py:attribute} exit_on_idle
:canonical: archivebox.actors.orchestrator.Orchestrator.exit_on_idle
:type: bool
:value: >
   True

```{autodoc2-docstring} archivebox.actors.orchestrator.Orchestrator.exit_on_idle
```

````

````{py:method} __repr__() -> str
:canonical: archivebox.actors.orchestrator.Orchestrator.__repr__

````

````{py:method} __str__() -> str
:canonical: archivebox.actors.orchestrator.Orchestrator.__str__

````

````{py:method} name() -> str
:canonical: archivebox.actors.orchestrator.Orchestrator.name

```{autodoc2-docstring} archivebox.actors.orchestrator.Orchestrator.name
```

````

````{py:method} fork_as_thread()
:canonical: archivebox.actors.orchestrator.Orchestrator.fork_as_thread

```{autodoc2-docstring} archivebox.actors.orchestrator.Orchestrator.fork_as_thread
```

````

````{py:method} fork_as_process()
:canonical: archivebox.actors.orchestrator.Orchestrator.fork_as_process

```{autodoc2-docstring} archivebox.actors.orchestrator.Orchestrator.fork_as_process
```

````

````{py:method} start() -> int
:canonical: archivebox.actors.orchestrator.Orchestrator.start

```{autodoc2-docstring} archivebox.actors.orchestrator.Orchestrator.start
```

````

````{py:method} autodiscover_actor_types() -> typing.Dict[str, typing.Type[archivebox.actors.actor.ActorType]]
:canonical: archivebox.actors.orchestrator.Orchestrator.autodiscover_actor_types
:classmethod:

```{autodoc2-docstring} archivebox.actors.orchestrator.Orchestrator.autodiscover_actor_types
```

````

````{py:method} get_orphaned_objects(all_queues) -> list
:canonical: archivebox.actors.orchestrator.Orchestrator.get_orphaned_objects
:classmethod:

```{autodoc2-docstring} archivebox.actors.orchestrator.Orchestrator.get_orphaned_objects
```

````

````{py:method} has_future_objects(all_queues) -> bool
:canonical: archivebox.actors.orchestrator.Orchestrator.has_future_objects
:classmethod:

```{autodoc2-docstring} archivebox.actors.orchestrator.Orchestrator.has_future_objects
```

````

````{py:method} on_startup()
:canonical: archivebox.actors.orchestrator.Orchestrator.on_startup

```{autodoc2-docstring} archivebox.actors.orchestrator.Orchestrator.on_startup
```

````

````{py:method} on_shutdown(err: BaseException | None = None)
:canonical: archivebox.actors.orchestrator.Orchestrator.on_shutdown

```{autodoc2-docstring} archivebox.actors.orchestrator.Orchestrator.on_shutdown
```

````

````{py:method} on_tick_started(all_queues)
:canonical: archivebox.actors.orchestrator.Orchestrator.on_tick_started

```{autodoc2-docstring} archivebox.actors.orchestrator.Orchestrator.on_tick_started
```

````

````{py:method} on_tick_finished(all_queues, all_existing_actors, all_spawned_actors)
:canonical: archivebox.actors.orchestrator.Orchestrator.on_tick_finished

```{autodoc2-docstring} archivebox.actors.orchestrator.Orchestrator.on_tick_finished
```

````

````{py:method} on_idle(all_queues)
:canonical: archivebox.actors.orchestrator.Orchestrator.on_idle

```{autodoc2-docstring} archivebox.actors.orchestrator.Orchestrator.on_idle
```

````

````{py:method} runloop()
:canonical: archivebox.actors.orchestrator.Orchestrator.runloop

```{autodoc2-docstring} archivebox.actors.orchestrator.Orchestrator.runloop
```

````

`````
