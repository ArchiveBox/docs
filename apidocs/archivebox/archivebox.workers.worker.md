# {py:mod}`archivebox.workers.worker`

```{py:module} archivebox.workers.worker
```

```{autodoc2-docstring} archivebox.workers.worker
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Worker <archivebox.workers.worker.Worker>`
  - ```{autodoc2-docstring} archivebox.workers.worker.Worker
    :summary:
    ```
* - {py:obj}`CrawlWorker <archivebox.workers.worker.CrawlWorker>`
  - ```{autodoc2-docstring} archivebox.workers.worker.CrawlWorker
    :summary:
    ```
* - {py:obj}`SnapshotWorker <archivebox.workers.worker.SnapshotWorker>`
  - ```{autodoc2-docstring} archivebox.workers.worker.SnapshotWorker
    :summary:
    ```
* - {py:obj}`BinaryWorker <archivebox.workers.worker.BinaryWorker>`
  - ```{autodoc2-docstring} archivebox.workers.worker.BinaryWorker
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_run_worker <archivebox.workers.worker._run_worker>`
  - ```{autodoc2-docstring} archivebox.workers.worker._run_worker
    :summary:
    ```
* - {py:obj}`_run_snapshot_worker <archivebox.workers.worker._run_snapshot_worker>`
  - ```{autodoc2-docstring} archivebox.workers.worker._run_snapshot_worker
    :summary:
    ```
* - {py:obj}`get_worker_class <archivebox.workers.worker.get_worker_class>`
  - ```{autodoc2-docstring} archivebox.workers.worker.get_worker_class
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CPU_COUNT <archivebox.workers.worker.CPU_COUNT>`
  - ```{autodoc2-docstring} archivebox.workers.worker.CPU_COUNT
    :summary:
    ```
* - {py:obj}`WORKER_TYPES <archivebox.workers.worker.WORKER_TYPES>`
  - ```{autodoc2-docstring} archivebox.workers.worker.WORKER_TYPES
    :summary:
    ```
````

### API

````{py:data} CPU_COUNT
:canonical: archivebox.workers.worker.CPU_COUNT
:value: >
   'cpu_count(...)'

```{autodoc2-docstring} archivebox.workers.worker.CPU_COUNT
```

````

````{py:data} WORKER_TYPES
:canonical: archivebox.workers.worker.WORKER_TYPES
:type: dict[str, type[archivebox.workers.worker.Worker]]
:value: >
   None

```{autodoc2-docstring} archivebox.workers.worker.WORKER_TYPES
```

````

````{py:function} _run_worker(worker_class_name: str, worker_id: int, **kwargs)
:canonical: archivebox.workers.worker._run_worker

```{autodoc2-docstring} archivebox.workers.worker._run_worker
```
````

````{py:function} _run_snapshot_worker(snapshot_id: str, worker_id: int, **kwargs)
:canonical: archivebox.workers.worker._run_snapshot_worker

```{autodoc2-docstring} archivebox.workers.worker._run_snapshot_worker
```
````

`````{py:class} Worker(worker_id: int = 0, **kwargs: typing.Any)
:canonical: archivebox.workers.worker.Worker

```{autodoc2-docstring} archivebox.workers.worker.Worker
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.workers.worker.Worker.__init__
```

````{py:attribute} name
:canonical: archivebox.workers.worker.Worker.name
:type: typing.ClassVar[str]
:value: >
   'worker'

```{autodoc2-docstring} archivebox.workers.worker.Worker.name
```

````

````{py:attribute} MAX_TICK_TIME
:canonical: archivebox.workers.worker.Worker.MAX_TICK_TIME
:type: typing.ClassVar[int]
:value: >
   60

```{autodoc2-docstring} archivebox.workers.worker.Worker.MAX_TICK_TIME
```

````

````{py:attribute} MAX_CONCURRENT_TASKS
:canonical: archivebox.workers.worker.Worker.MAX_CONCURRENT_TASKS
:type: typing.ClassVar[int]
:value: >
   1

```{autodoc2-docstring} archivebox.workers.worker.Worker.MAX_CONCURRENT_TASKS
```

````

````{py:method} __repr__() -> str
:canonical: archivebox.workers.worker.Worker.__repr__

````

````{py:method} get_model()
:canonical: archivebox.workers.worker.Worker.get_model
:abstractmethod:

```{autodoc2-docstring} archivebox.workers.worker.Worker.get_model
```

````

````{py:method} on_startup() -> None
:canonical: archivebox.workers.worker.Worker.on_startup

```{autodoc2-docstring} archivebox.workers.worker.Worker.on_startup
```

````

````{py:method} on_shutdown(error: BaseException | None = None) -> None
:canonical: archivebox.workers.worker.Worker.on_shutdown

```{autodoc2-docstring} archivebox.workers.worker.Worker.on_shutdown
```

````

````{py:method} _terminate_background_hooks(background_processes: dict[str, archivebox.machine.models.Process], worker_type: str, indent_level: int) -> None
:canonical: archivebox.workers.worker.Worker._terminate_background_hooks

```{autodoc2-docstring} archivebox.workers.worker.Worker._terminate_background_hooks
```

````

````{py:method} start(parent: typing.Any = None, **kwargs: typing.Any) -> int
:canonical: archivebox.workers.worker.Worker.start
:classmethod:

```{autodoc2-docstring} archivebox.workers.worker.Worker.start
```

````

````{py:method} get_running_workers() -> list
:canonical: archivebox.workers.worker.Worker.get_running_workers
:classmethod:

```{autodoc2-docstring} archivebox.workers.worker.Worker.get_running_workers
```

````

````{py:method} get_worker_count() -> int
:canonical: archivebox.workers.worker.Worker.get_worker_count
:classmethod:

```{autodoc2-docstring} archivebox.workers.worker.Worker.get_worker_count
```

````

`````

`````{py:class} CrawlWorker(crawl_id: str, **kwargs: typing.Any)
:canonical: archivebox.workers.worker.CrawlWorker

Bases: {py:obj}`archivebox.workers.worker.Worker`

```{autodoc2-docstring} archivebox.workers.worker.CrawlWorker
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.workers.worker.CrawlWorker.__init__
```

````{py:attribute} name
:canonical: archivebox.workers.worker.CrawlWorker.name
:type: typing.ClassVar[str]
:value: >
   'crawl'

```{autodoc2-docstring} archivebox.workers.worker.CrawlWorker.name
```

````

````{py:attribute} MAX_TICK_TIME
:canonical: archivebox.workers.worker.CrawlWorker.MAX_TICK_TIME
:type: typing.ClassVar[int]
:value: >
   60

```{autodoc2-docstring} archivebox.workers.worker.CrawlWorker.MAX_TICK_TIME
```

````

````{py:attribute} MAX_SNAPSHOT_WORKERS
:canonical: archivebox.workers.worker.CrawlWorker.MAX_SNAPSHOT_WORKERS
:type: typing.ClassVar[int]
:value: >
   8

```{autodoc2-docstring} archivebox.workers.worker.CrawlWorker.MAX_SNAPSHOT_WORKERS
```

````

````{py:method} get_model()
:canonical: archivebox.workers.worker.CrawlWorker.get_model

````

````{py:method} on_startup() -> None
:canonical: archivebox.workers.worker.CrawlWorker.on_startup

```{autodoc2-docstring} archivebox.workers.worker.CrawlWorker.on_startup
```

````

````{py:method} runloop() -> None
:canonical: archivebox.workers.worker.CrawlWorker.runloop

```{autodoc2-docstring} archivebox.workers.worker.CrawlWorker.runloop
```

````

````{py:method} _spawn_snapshot_workers() -> None
:canonical: archivebox.workers.worker.CrawlWorker._spawn_snapshot_workers

```{autodoc2-docstring} archivebox.workers.worker.CrawlWorker._spawn_snapshot_workers
```

````

````{py:method} _terminate_running_snapshot_workers() -> None
:canonical: archivebox.workers.worker.CrawlWorker._terminate_running_snapshot_workers

```{autodoc2-docstring} archivebox.workers.worker.CrawlWorker._terminate_running_snapshot_workers
```

````

````{py:method} _is_crawl_finished() -> bool
:canonical: archivebox.workers.worker.CrawlWorker._is_crawl_finished

```{autodoc2-docstring} archivebox.workers.worker.CrawlWorker._is_crawl_finished
```

````

````{py:method} on_shutdown(error: BaseException | None = None) -> None
:canonical: archivebox.workers.worker.CrawlWorker.on_shutdown

```{autodoc2-docstring} archivebox.workers.worker.CrawlWorker.on_shutdown
```

````

`````

`````{py:class} SnapshotWorker(snapshot_id: str, **kwargs: typing.Any)
:canonical: archivebox.workers.worker.SnapshotWorker

Bases: {py:obj}`archivebox.workers.worker.Worker`

```{autodoc2-docstring} archivebox.workers.worker.SnapshotWorker
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.workers.worker.SnapshotWorker.__init__
```

````{py:attribute} name
:canonical: archivebox.workers.worker.SnapshotWorker.name
:type: typing.ClassVar[str]
:value: >
   'snapshot'

```{autodoc2-docstring} archivebox.workers.worker.SnapshotWorker.name
```

````

````{py:method} get_model()
:canonical: archivebox.workers.worker.SnapshotWorker.get_model

```{autodoc2-docstring} archivebox.workers.worker.SnapshotWorker.get_model
```

````

````{py:method} on_startup() -> None
:canonical: archivebox.workers.worker.SnapshotWorker.on_startup

```{autodoc2-docstring} archivebox.workers.worker.SnapshotWorker.on_startup
```

````

````{py:method} runloop() -> None
:canonical: archivebox.workers.worker.SnapshotWorker.runloop

```{autodoc2-docstring} archivebox.workers.worker.SnapshotWorker.runloop
```

````

````{py:method} _run_hook(hook_path: pathlib.Path, ar: typing.Any, config: dict) -> typing.Any
:canonical: archivebox.workers.worker.SnapshotWorker._run_hook

```{autodoc2-docstring} archivebox.workers.worker.SnapshotWorker._run_hook
```

````

````{py:method} _wait_for_hook(process: typing.Any, ar: typing.Any) -> None
:canonical: archivebox.workers.worker.SnapshotWorker._wait_for_hook

```{autodoc2-docstring} archivebox.workers.worker.SnapshotWorker._wait_for_hook
```

````

````{py:method} _retry_failed_empty_foreground_hooks(hooks: list[tuple[pathlib.Path, typing.Any]], config: dict) -> None
:canonical: archivebox.workers.worker.SnapshotWorker._retry_failed_empty_foreground_hooks

```{autodoc2-docstring} archivebox.workers.worker.SnapshotWorker._retry_failed_empty_foreground_hooks
```

````

````{py:method} _finalize_background_hooks() -> None
:canonical: archivebox.workers.worker.SnapshotWorker._finalize_background_hooks

```{autodoc2-docstring} archivebox.workers.worker.SnapshotWorker._finalize_background_hooks
```

````

````{py:method} _reap_background_hooks() -> None
:canonical: archivebox.workers.worker.SnapshotWorker._reap_background_hooks

```{autodoc2-docstring} archivebox.workers.worker.SnapshotWorker._reap_background_hooks
```

````

````{py:method} _snapshot_exceeded_hard_timeout() -> bool
:canonical: archivebox.workers.worker.SnapshotWorker._snapshot_exceeded_hard_timeout

```{autodoc2-docstring} archivebox.workers.worker.SnapshotWorker._snapshot_exceeded_hard_timeout
```

````

````{py:method} _seal_snapshot_due_to_timeout() -> None
:canonical: archivebox.workers.worker.SnapshotWorker._seal_snapshot_due_to_timeout

```{autodoc2-docstring} archivebox.workers.worker.SnapshotWorker._seal_snapshot_due_to_timeout
```

````

````{py:method} on_shutdown(error: BaseException | None = None) -> None
:canonical: archivebox.workers.worker.SnapshotWorker.on_shutdown

```{autodoc2-docstring} archivebox.workers.worker.SnapshotWorker.on_shutdown
```

````

````{py:method} _extract_plugin_name(hook_path: pathlib.Path, hook_name: str) -> str
:canonical: archivebox.workers.worker.SnapshotWorker._extract_plugin_name
:staticmethod:

```{autodoc2-docstring} archivebox.workers.worker.SnapshotWorker._extract_plugin_name
```

````

`````

`````{py:class} BinaryWorker(binary_id: str = None, worker_id: int = 0)
:canonical: archivebox.workers.worker.BinaryWorker

Bases: {py:obj}`archivebox.workers.worker.Worker`

```{autodoc2-docstring} archivebox.workers.worker.BinaryWorker
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.workers.worker.BinaryWorker.__init__
```

````{py:attribute} name
:canonical: archivebox.workers.worker.BinaryWorker.name
:type: typing.ClassVar[str]
:value: >
   'binary'

```{autodoc2-docstring} archivebox.workers.worker.BinaryWorker.name
```

````

````{py:attribute} MAX_TICK_TIME
:canonical: archivebox.workers.worker.BinaryWorker.MAX_TICK_TIME
:type: typing.ClassVar[int]
:value: >
   600

```{autodoc2-docstring} archivebox.workers.worker.BinaryWorker.MAX_TICK_TIME
```

````

````{py:attribute} MAX_CONCURRENT_TASKS
:canonical: archivebox.workers.worker.BinaryWorker.MAX_CONCURRENT_TASKS
:type: typing.ClassVar[int]
:value: >
   1

```{autodoc2-docstring} archivebox.workers.worker.BinaryWorker.MAX_CONCURRENT_TASKS
```

````

````{py:attribute} POLL_INTERVAL
:canonical: archivebox.workers.worker.BinaryWorker.POLL_INTERVAL
:type: typing.ClassVar[float]
:value: >
   0.5

```{autodoc2-docstring} archivebox.workers.worker.BinaryWorker.POLL_INTERVAL
```

````

````{py:method} get_model()
:canonical: archivebox.workers.worker.BinaryWorker.get_model

````

````{py:method} get_next_item()
:canonical: archivebox.workers.worker.BinaryWorker.get_next_item

```{autodoc2-docstring} archivebox.workers.worker.BinaryWorker.get_next_item
```

````

````{py:method} runloop() -> None
:canonical: archivebox.workers.worker.BinaryWorker.runloop

```{autodoc2-docstring} archivebox.workers.worker.BinaryWorker.runloop
```

````

````{py:method} _process_single_binary()
:canonical: archivebox.workers.worker.BinaryWorker._process_single_binary

```{autodoc2-docstring} archivebox.workers.worker.BinaryWorker._process_single_binary
```

````

````{py:method} _daemon_loop()
:canonical: archivebox.workers.worker.BinaryWorker._daemon_loop

```{autodoc2-docstring} archivebox.workers.worker.BinaryWorker._daemon_loop
```

````

`````

````{py:function} get_worker_class(name: str) -> type[archivebox.workers.worker.Worker]
:canonical: archivebox.workers.worker.get_worker_class

```{autodoc2-docstring} archivebox.workers.worker.get_worker_class
```
````
