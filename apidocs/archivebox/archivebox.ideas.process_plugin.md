# {py:mod}`archivebox.ideas.process_plugin`

```{py:module} archivebox.ideas.process_plugin
```

```{autodoc2-docstring} archivebox.ideas.process_plugin
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ProcessRecord <archivebox.ideas.process_plugin.ProcessRecord>`
  -
* - {py:obj}`ProcessLaunch <archivebox.ideas.process_plugin.ProcessLaunch>`
  - ```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessLaunch
    :summary:
    ```
* - {py:obj}`ProcessStarted <archivebox.ideas.process_plugin.ProcessStarted>`
  - ```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessStarted
    :summary:
    ```
* - {py:obj}`ProcessExited <archivebox.ideas.process_plugin.ProcessExited>`
  - ```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessExited
    :summary:
    ```
* - {py:obj}`ProcessKill <archivebox.ideas.process_plugin.ProcessKill>`
  - ```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessKill
    :summary:
    ```
* - {py:obj}`_RunningProcess <archivebox.ideas.process_plugin._RunningProcess>`
  - ```{autodoc2-docstring} archivebox.ideas.process_plugin._RunningProcess
    :summary:
    ```
* - {py:obj}`ProcessPlugin <archivebox.ideas.process_plugin.ProcessPlugin>`
  - ```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessPlugin
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_utcnow <archivebox.ideas.process_plugin._utcnow>`
  - ```{autodoc2-docstring} archivebox.ideas.process_plugin._utcnow
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`JsonEventAdapter <archivebox.ideas.process_plugin.JsonEventAdapter>`
  - ```{autodoc2-docstring} archivebox.ideas.process_plugin.JsonEventAdapter
    :summary:
    ```
* - {py:obj}`__all__ <archivebox.ideas.process_plugin.__all__>`
  - ```{autodoc2-docstring} archivebox.ideas.process_plugin.__all__
    :summary:
    ```
````

### API

````{py:function} _utcnow() -> datetime.datetime
:canonical: archivebox.ideas.process_plugin._utcnow

```{autodoc2-docstring} archivebox.ideas.process_plugin._utcnow
```
````

`````{py:class} ProcessRecord(/, **data: typing.Any)
:canonical: archivebox.ideas.process_plugin.ProcessRecord

Bases: {py:obj}`pydantic.BaseModel`

````{py:attribute} id
:canonical: archivebox.ideas.process_plugin.ProcessRecord.id
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessRecord.id
```

````

````{py:attribute} cmd
:canonical: archivebox.ideas.process_plugin.ProcessRecord.cmd
:type: list[str]
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessRecord.cmd
```

````

````{py:attribute} cwd
:canonical: archivebox.ideas.process_plugin.ProcessRecord.cwd
:type: str | None
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessRecord.cwd
```

````

````{py:attribute} env
:canonical: archivebox.ideas.process_plugin.ProcessRecord.env
:type: dict[str, str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessRecord.env
```

````

````{py:attribute} pid
:canonical: archivebox.ideas.process_plugin.ProcessRecord.pid
:type: int | None
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessRecord.pid
```

````

````{py:attribute} started_at
:canonical: archivebox.ideas.process_plugin.ProcessRecord.started_at
:type: datetime.datetime | None
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessRecord.started_at
```

````

````{py:attribute} ended_at
:canonical: archivebox.ideas.process_plugin.ProcessRecord.ended_at
:type: datetime.datetime | None
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessRecord.ended_at
```

````

````{py:attribute} exit_code
:canonical: archivebox.ideas.process_plugin.ProcessRecord.exit_code
:type: int | None
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessRecord.exit_code
```

````

````{py:attribute} stdout_path
:canonical: archivebox.ideas.process_plugin.ProcessRecord.stdout_path
:type: str | None
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessRecord.stdout_path
```

````

````{py:attribute} stderr_path
:canonical: archivebox.ideas.process_plugin.ProcessRecord.stderr_path
:type: str | None
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessRecord.stderr_path
```

````

````{py:attribute} cmd_path
:canonical: archivebox.ideas.process_plugin.ProcessRecord.cmd_path
:type: str | None
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessRecord.cmd_path
```

````

````{py:attribute} pid_path
:canonical: archivebox.ideas.process_plugin.ProcessRecord.pid_path
:type: str | None
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessRecord.pid_path
```

````

````{py:attribute} is_background
:canonical: archivebox.ideas.process_plugin.ProcessRecord.is_background
:type: bool
:value: >
   False

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessRecord.is_background
```

````

````{py:attribute} parent_process_id
:canonical: archivebox.ideas.process_plugin.ProcessRecord.parent_process_id
:type: str | None
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessRecord.parent_process_id
```

````

`````

`````{py:class} ProcessLaunch
:canonical: archivebox.ideas.process_plugin.ProcessLaunch

Bases: {py:obj}`bubus.BaseEvent`\[{py:obj}`archivebox.ideas.process_plugin.ProcessRecord`\]

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessLaunch
```

````{py:attribute} cmd
:canonical: archivebox.ideas.process_plugin.ProcessLaunch.cmd
:type: list[str]
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessLaunch.cmd
```

````

````{py:attribute} cwd
:canonical: archivebox.ideas.process_plugin.ProcessLaunch.cwd
:type: str | None
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessLaunch.cwd
```

````

````{py:attribute} env
:canonical: archivebox.ideas.process_plugin.ProcessLaunch.env
:type: dict[str, str] | None
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessLaunch.env
```

````

````{py:attribute} timeout
:canonical: archivebox.ideas.process_plugin.ProcessLaunch.timeout
:type: float | None
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessLaunch.timeout
```

````

````{py:attribute} output_dir
:canonical: archivebox.ideas.process_plugin.ProcessLaunch.output_dir
:type: str | None
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessLaunch.output_dir
```

````

````{py:attribute} log_prefix
:canonical: archivebox.ideas.process_plugin.ProcessLaunch.log_prefix
:type: str | None
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessLaunch.log_prefix
```

````

````{py:attribute} is_background
:canonical: archivebox.ideas.process_plugin.ProcessLaunch.is_background
:type: bool
:value: >
   False

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessLaunch.is_background
```

````

````{py:attribute} parent_process_id
:canonical: archivebox.ideas.process_plugin.ProcessLaunch.parent_process_id
:type: str | None
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessLaunch.parent_process_id
```

````

````{py:attribute} parse_stdout_events
:canonical: archivebox.ideas.process_plugin.ProcessLaunch.parse_stdout_events
:type: bool
:value: >
   True

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessLaunch.parse_stdout_events
```

````

`````

`````{py:class} ProcessStarted
:canonical: archivebox.ideas.process_plugin.ProcessStarted

Bases: {py:obj}`bubus.BaseEvent`\[{py:obj}`None`\]

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessStarted
```

````{py:attribute} process
:canonical: archivebox.ideas.process_plugin.ProcessStarted.process
:type: archivebox.ideas.process_plugin.ProcessRecord
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessStarted.process
```

````

`````

`````{py:class} ProcessExited
:canonical: archivebox.ideas.process_plugin.ProcessExited

Bases: {py:obj}`bubus.BaseEvent`\[{py:obj}`None`\]

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessExited
```

````{py:attribute} process
:canonical: archivebox.ideas.process_plugin.ProcessExited.process
:type: archivebox.ideas.process_plugin.ProcessRecord
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessExited.process
```

````

`````

`````{py:class} ProcessKill
:canonical: archivebox.ideas.process_plugin.ProcessKill

Bases: {py:obj}`bubus.BaseEvent`\[{py:obj}`archivebox.ideas.process_plugin.ProcessRecord`\]

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessKill
```

````{py:attribute} process_id
:canonical: archivebox.ideas.process_plugin.ProcessKill.process_id
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessKill.process_id
```

````

````{py:attribute} signal
:canonical: archivebox.ideas.process_plugin.ProcessKill.signal
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessKill.signal
```

````

````{py:attribute} timeout
:canonical: archivebox.ideas.process_plugin.ProcessKill.timeout
:type: float | None
:value: >
   10.0

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessKill.timeout
```

````

`````

`````{py:class} _RunningProcess
:canonical: archivebox.ideas.process_plugin._RunningProcess

```{autodoc2-docstring} archivebox.ideas.process_plugin._RunningProcess
```

````{py:attribute} process
:canonical: archivebox.ideas.process_plugin._RunningProcess.process
:type: asyncio.subprocess.Process
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin._RunningProcess.process
```

````

````{py:attribute} record
:canonical: archivebox.ideas.process_plugin._RunningProcess.record
:type: archivebox.ideas.process_plugin.ProcessRecord
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin._RunningProcess.record
```

````

````{py:attribute} stdout_task
:canonical: archivebox.ideas.process_plugin._RunningProcess.stdout_task
:type: asyncio.Task[None] | None
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin._RunningProcess.stdout_task
```

````

````{py:attribute} stderr_task
:canonical: archivebox.ideas.process_plugin._RunningProcess.stderr_task
:type: asyncio.Task[None] | None
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin._RunningProcess.stderr_task
```

````

````{py:attribute} watcher_task
:canonical: archivebox.ideas.process_plugin._RunningProcess.watcher_task
:type: asyncio.Task[None] | None
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin._RunningProcess.watcher_task
```

````

````{py:attribute} parent_event_id
:canonical: archivebox.ideas.process_plugin._RunningProcess.parent_event_id
:type: str | None
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin._RunningProcess.parent_event_id
```

````

`````

````{py:data} JsonEventAdapter
:canonical: archivebox.ideas.process_plugin.JsonEventAdapter
:value: >
   None

```{autodoc2-docstring} archivebox.ideas.process_plugin.JsonEventAdapter
```

````

`````{py:class} ProcessPlugin(bus: bubus.EventBus, *, env: typing.Mapping[str, str] | None = None, json_event_adapter: archivebox.ideas.process_plugin.JsonEventAdapter | None = None)
:canonical: archivebox.ideas.process_plugin.ProcessPlugin

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessPlugin
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessPlugin.__init__
```

````{py:method} register_event_handlers() -> None
:canonical: archivebox.ideas.process_plugin.ProcessPlugin.register_event_handlers

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessPlugin.register_event_handlers
```

````

````{py:method} on_ProcessLaunch(event: archivebox.ideas.process_plugin.ProcessLaunch) -> archivebox.ideas.process_plugin.ProcessRecord
:canonical: archivebox.ideas.process_plugin.ProcessPlugin.on_ProcessLaunch
:async:

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessPlugin.on_ProcessLaunch
```

````

````{py:method} on_ProcessKill(event: archivebox.ideas.process_plugin.ProcessKill) -> archivebox.ideas.process_plugin.ProcessRecord
:canonical: archivebox.ideas.process_plugin.ProcessPlugin.on_ProcessKill
:async:

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessPlugin.on_ProcessKill
```

````

````{py:method} _watch_process(process_id: str, timeout: float | None) -> None
:canonical: archivebox.ideas.process_plugin.ProcessPlugin._watch_process
:async:

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessPlugin._watch_process
```

````

````{py:method} _finalize_process(process_id: str) -> None
:canonical: archivebox.ideas.process_plugin.ProcessPlugin._finalize_process
:async:

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessPlugin._finalize_process
```

````

````{py:method} _consume_stream(stream: asyncio.StreamReader | None, path: pathlib.Path, parent_event_id: str | None, parse_events: bool) -> None
:canonical: archivebox.ideas.process_plugin.ProcessPlugin._consume_stream
:async:

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessPlugin._consume_stream
```

````

````{py:method} _maybe_dispatch_json_event(line: str, parent_event_id: str | None) -> None
:canonical: archivebox.ideas.process_plugin.ProcessPlugin._maybe_dispatch_json_event
:async:

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessPlugin._maybe_dispatch_json_event
```

````

````{py:method} _write_cmd_file(path: pathlib.Path, cmd: list[str]) -> None
:canonical: archivebox.ideas.process_plugin.ProcessPlugin._write_cmd_file
:staticmethod:

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessPlugin._write_cmd_file
```

````

````{py:method} _write_pid_file(path: pathlib.Path, pid: int) -> None
:canonical: archivebox.ideas.process_plugin.ProcessPlugin._write_pid_file
:staticmethod:

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessPlugin._write_pid_file
```

````

````{py:method} _terminate_process(proc: asyncio.subprocess.Process, sig: int) -> None
:canonical: archivebox.ideas.process_plugin.ProcessPlugin._terminate_process
:staticmethod:

```{autodoc2-docstring} archivebox.ideas.process_plugin.ProcessPlugin._terminate_process
```

````

`````

````{py:data} __all__
:canonical: archivebox.ideas.process_plugin.__all__
:value: >
   ['ProcessRecord', 'ProcessLaunch', 'ProcessStarted', 'ProcessExited', 'ProcessKill', 'ProcessPlugin'...

```{autodoc2-docstring} archivebox.ideas.process_plugin.__all__
```

````
