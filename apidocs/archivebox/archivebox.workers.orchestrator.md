# {py:mod}`archivebox.workers.orchestrator`

```{py:module} archivebox.workers.orchestrator
```

```{autodoc2-docstring} archivebox.workers.orchestrator
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Orchestrator <archivebox.workers.orchestrator.Orchestrator>`
  - ```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_run_orchestrator_process <archivebox.workers.orchestrator._run_orchestrator_process>`
  - ```{autodoc2-docstring} archivebox.workers.orchestrator._run_orchestrator_process
    :summary:
    ```
````

### API

````{py:function} _run_orchestrator_process(exit_on_idle: bool) -> None
:canonical: archivebox.workers.orchestrator._run_orchestrator_process

```{autodoc2-docstring} archivebox.workers.orchestrator._run_orchestrator_process
```
````

`````{py:class} Orchestrator(exit_on_idle: bool = True, crawl_id: str | None = None)
:canonical: archivebox.workers.orchestrator.Orchestrator

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.__init__
```

````{py:attribute} WORKER_TYPES
:canonical: archivebox.workers.orchestrator.Orchestrator.WORKER_TYPES
:type: list[typing.Type[archivebox.workers.worker.Worker]]
:value: >
   None

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.WORKER_TYPES
```

````

````{py:attribute} POLL_INTERVAL
:canonical: archivebox.workers.orchestrator.Orchestrator.POLL_INTERVAL
:type: float
:value: >
   2.0

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.POLL_INTERVAL
```

````

````{py:attribute} IDLE_TIMEOUT
:canonical: archivebox.workers.orchestrator.Orchestrator.IDLE_TIMEOUT
:type: int
:value: >
   3

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.IDLE_TIMEOUT
```

````

````{py:attribute} MAX_CRAWL_WORKERS
:canonical: archivebox.workers.orchestrator.Orchestrator.MAX_CRAWL_WORKERS
:type: int
:value: >
   8

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.MAX_CRAWL_WORKERS
```

````

````{py:attribute} MAX_BINARY_WORKERS
:canonical: archivebox.workers.orchestrator.Orchestrator.MAX_BINARY_WORKERS
:type: int
:value: >
   1

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.MAX_BINARY_WORKERS
```

````

````{py:method} __repr__() -> str
:canonical: archivebox.workers.orchestrator.Orchestrator.__repr__

````

````{py:method} is_running() -> bool
:canonical: archivebox.workers.orchestrator.Orchestrator.is_running
:classmethod:

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.is_running
```

````

````{py:method} on_startup() -> None
:canonical: archivebox.workers.orchestrator.Orchestrator.on_startup

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.on_startup
```

````

````{py:method} terminate_all_workers() -> None
:canonical: archivebox.workers.orchestrator.Orchestrator.terminate_all_workers

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.terminate_all_workers
```

````

````{py:method} on_shutdown(error: BaseException | None = None) -> None
:canonical: archivebox.workers.orchestrator.Orchestrator.on_shutdown

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.on_shutdown
```

````

````{py:method} get_total_worker_count() -> int
:canonical: archivebox.workers.orchestrator.Orchestrator.get_total_worker_count

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.get_total_worker_count
```

````

````{py:method} get_running_workers_for_type(WorkerClass: typing.Type[archivebox.workers.worker.Worker]) -> int
:canonical: archivebox.workers.orchestrator.Orchestrator.get_running_workers_for_type

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.get_running_workers_for_type
```

````

````{py:method} _get_scoped_running_workers()
:canonical: archivebox.workers.orchestrator.Orchestrator._get_scoped_running_workers

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator._get_scoped_running_workers
```

````

````{py:method} should_spawn_worker(WorkerClass: typing.Type[archivebox.workers.worker.Worker], queue_count: int) -> bool
:canonical: archivebox.workers.orchestrator.Orchestrator.should_spawn_worker

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.should_spawn_worker
```

````

````{py:method} spawn_worker(WorkerClass: typing.Type[archivebox.workers.worker.Worker]) -> int | None
:canonical: archivebox.workers.orchestrator.Orchestrator.spawn_worker

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.spawn_worker
```

````

````{py:method} check_queues_and_spawn_workers() -> dict[str, int]
:canonical: archivebox.workers.orchestrator.Orchestrator.check_queues_and_spawn_workers

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.check_queues_and_spawn_workers
```

````

````{py:method} _should_process_schedules() -> bool
:canonical: archivebox.workers.orchestrator.Orchestrator._should_process_schedules

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator._should_process_schedules
```

````

````{py:method} _materialize_due_schedules() -> None
:canonical: archivebox.workers.orchestrator.Orchestrator._materialize_due_schedules

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator._materialize_due_schedules
```

````

````{py:method} _enforce_hard_timeouts() -> None
:canonical: archivebox.workers.orchestrator.Orchestrator._enforce_hard_timeouts

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator._enforce_hard_timeouts
```

````

````{py:method} _claim_crawl(crawl) -> bool
:canonical: archivebox.workers.orchestrator.Orchestrator._claim_crawl

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator._claim_crawl
```

````

````{py:method} has_pending_work(queue_sizes: dict[str, int]) -> bool
:canonical: archivebox.workers.orchestrator.Orchestrator.has_pending_work

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.has_pending_work
```

````

````{py:method} has_running_workers() -> bool
:canonical: archivebox.workers.orchestrator.Orchestrator.has_running_workers

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.has_running_workers
```

````

````{py:method} has_future_work() -> bool
:canonical: archivebox.workers.orchestrator.Orchestrator.has_future_work

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.has_future_work
```

````

````{py:method} on_tick(queue_sizes: dict[str, int]) -> None
:canonical: archivebox.workers.orchestrator.Orchestrator.on_tick

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.on_tick
```

````

````{py:method} on_idle() -> None
:canonical: archivebox.workers.orchestrator.Orchestrator.on_idle

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.on_idle
```

````

````{py:method} should_exit(queue_sizes: dict[str, int]) -> bool
:canonical: archivebox.workers.orchestrator.Orchestrator.should_exit

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.should_exit
```

````

````{py:method} runloop() -> None
:canonical: archivebox.workers.orchestrator.Orchestrator.runloop

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.runloop
```

````

````{py:method} _run_orchestrator_loop(progress_layout, plain_output: bool = False)
:canonical: archivebox.workers.orchestrator.Orchestrator._run_orchestrator_loop

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator._run_orchestrator_loop
```

````

````{py:method} start() -> int
:canonical: archivebox.workers.orchestrator.Orchestrator.start

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.start
```

````

````{py:method} get_or_start(exit_on_idle: bool = True) -> archivebox.workers.orchestrator.Orchestrator
:canonical: archivebox.workers.orchestrator.Orchestrator.get_or_start
:classmethod:

```{autodoc2-docstring} archivebox.workers.orchestrator.Orchestrator.get_or_start
```

````

`````
