# {py:mod}`archivebox.workers.supervisord_util`

```{py:module} archivebox.workers.supervisord_util
```

```{autodoc2-docstring} archivebox.workers.supervisord_util
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`is_port_in_use <archivebox.workers.supervisord_util.is_port_in_use>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.is_port_in_use
    :summary:
    ```
* - {py:obj}`get_sock_file <archivebox.workers.supervisord_util.get_sock_file>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.get_sock_file
    :summary:
    ```
* - {py:obj}`follow <archivebox.workers.supervisord_util.follow>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.follow
    :summary:
    ```
* - {py:obj}`create_supervisord_config <archivebox.workers.supervisord_util.create_supervisord_config>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.create_supervisord_config
    :summary:
    ```
* - {py:obj}`create_worker_config <archivebox.workers.supervisord_util.create_worker_config>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.create_worker_config
    :summary:
    ```
* - {py:obj}`get_existing_supervisord_process <archivebox.workers.supervisord_util.get_existing_supervisord_process>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.get_existing_supervisord_process
    :summary:
    ```
* - {py:obj}`stop_existing_supervisord_process <archivebox.workers.supervisord_util.stop_existing_supervisord_process>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.stop_existing_supervisord_process
    :summary:
    ```
* - {py:obj}`start_new_supervisord_process <archivebox.workers.supervisord_util.start_new_supervisord_process>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.start_new_supervisord_process
    :summary:
    ```
* - {py:obj}`wait_for_supervisord_ready <archivebox.workers.supervisord_util.wait_for_supervisord_ready>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.wait_for_supervisord_ready
    :summary:
    ```
* - {py:obj}`get_or_create_supervisord_process <archivebox.workers.supervisord_util.get_or_create_supervisord_process>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.get_or_create_supervisord_process
    :summary:
    ```
* - {py:obj}`start_worker <archivebox.workers.supervisord_util.start_worker>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.start_worker
    :summary:
    ```
* - {py:obj}`get_worker <archivebox.workers.supervisord_util.get_worker>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.get_worker
    :summary:
    ```
* - {py:obj}`stop_worker <archivebox.workers.supervisord_util.stop_worker>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.stop_worker
    :summary:
    ```
* - {py:obj}`tail_worker_logs <archivebox.workers.supervisord_util.tail_worker_logs>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.tail_worker_logs
    :summary:
    ```
* - {py:obj}`tail_multiple_worker_logs <archivebox.workers.supervisord_util.tail_multiple_worker_logs>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.tail_multiple_worker_logs
    :summary:
    ```
* - {py:obj}`watch_worker <archivebox.workers.supervisord_util.watch_worker>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.watch_worker
    :summary:
    ```
* - {py:obj}`start_server_workers <archivebox.workers.supervisord_util.start_server_workers>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.start_server_workers
    :summary:
    ```
* - {py:obj}`start_cli_workers <archivebox.workers.supervisord_util.start_cli_workers>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.start_cli_workers
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`LOG_FILE_NAME <archivebox.workers.supervisord_util.LOG_FILE_NAME>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.LOG_FILE_NAME
    :summary:
    ```
* - {py:obj}`CONFIG_FILE_NAME <archivebox.workers.supervisord_util.CONFIG_FILE_NAME>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.CONFIG_FILE_NAME
    :summary:
    ```
* - {py:obj}`PID_FILE_NAME <archivebox.workers.supervisord_util.PID_FILE_NAME>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.PID_FILE_NAME
    :summary:
    ```
* - {py:obj}`WORKERS_DIR_NAME <archivebox.workers.supervisord_util.WORKERS_DIR_NAME>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.WORKERS_DIR_NAME
    :summary:
    ```
* - {py:obj}`_supervisord_proc <archivebox.workers.supervisord_util._supervisord_proc>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util._supervisord_proc
    :summary:
    ```
* - {py:obj}`ORCHESTRATOR_WORKER <archivebox.workers.supervisord_util.ORCHESTRATOR_WORKER>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.ORCHESTRATOR_WORKER
    :summary:
    ```
* - {py:obj}`SERVER_WORKER <archivebox.workers.supervisord_util.SERVER_WORKER>`
  - ```{autodoc2-docstring} archivebox.workers.supervisord_util.SERVER_WORKER
    :summary:
    ```
````

### API

````{py:data} LOG_FILE_NAME
:canonical: archivebox.workers.supervisord_util.LOG_FILE_NAME
:value: >
   'supervisord.log'

```{autodoc2-docstring} archivebox.workers.supervisord_util.LOG_FILE_NAME
```

````

````{py:data} CONFIG_FILE_NAME
:canonical: archivebox.workers.supervisord_util.CONFIG_FILE_NAME
:value: >
   'supervisord.conf'

```{autodoc2-docstring} archivebox.workers.supervisord_util.CONFIG_FILE_NAME
```

````

````{py:data} PID_FILE_NAME
:canonical: archivebox.workers.supervisord_util.PID_FILE_NAME
:value: >
   'supervisord.pid'

```{autodoc2-docstring} archivebox.workers.supervisord_util.PID_FILE_NAME
```

````

````{py:data} WORKERS_DIR_NAME
:canonical: archivebox.workers.supervisord_util.WORKERS_DIR_NAME
:value: >
   'workers'

```{autodoc2-docstring} archivebox.workers.supervisord_util.WORKERS_DIR_NAME
```

````

````{py:data} _supervisord_proc
:canonical: archivebox.workers.supervisord_util._supervisord_proc
:value: >
   None

```{autodoc2-docstring} archivebox.workers.supervisord_util._supervisord_proc
```

````

````{py:data} ORCHESTRATOR_WORKER
:canonical: archivebox.workers.supervisord_util.ORCHESTRATOR_WORKER
:value: >
   None

```{autodoc2-docstring} archivebox.workers.supervisord_util.ORCHESTRATOR_WORKER
```

````

````{py:data} SERVER_WORKER
:canonical: archivebox.workers.supervisord_util.SERVER_WORKER
:value: >
   None

```{autodoc2-docstring} archivebox.workers.supervisord_util.SERVER_WORKER
```

````

````{py:function} is_port_in_use(host: str, port: int) -> bool
:canonical: archivebox.workers.supervisord_util.is_port_in_use

```{autodoc2-docstring} archivebox.workers.supervisord_util.is_port_in_use
```
````

````{py:function} get_sock_file()
:canonical: archivebox.workers.supervisord_util.get_sock_file

```{autodoc2-docstring} archivebox.workers.supervisord_util.get_sock_file
```
````

````{py:function} follow(file, sleep_sec=0.1) -> typing.Iterator[str]
:canonical: archivebox.workers.supervisord_util.follow

```{autodoc2-docstring} archivebox.workers.supervisord_util.follow
```
````

````{py:function} create_supervisord_config()
:canonical: archivebox.workers.supervisord_util.create_supervisord_config

```{autodoc2-docstring} archivebox.workers.supervisord_util.create_supervisord_config
```
````

````{py:function} create_worker_config(daemon)
:canonical: archivebox.workers.supervisord_util.create_worker_config

```{autodoc2-docstring} archivebox.workers.supervisord_util.create_worker_config
```
````

````{py:function} get_existing_supervisord_process()
:canonical: archivebox.workers.supervisord_util.get_existing_supervisord_process

```{autodoc2-docstring} archivebox.workers.supervisord_util.get_existing_supervisord_process
```
````

````{py:function} stop_existing_supervisord_process()
:canonical: archivebox.workers.supervisord_util.stop_existing_supervisord_process

```{autodoc2-docstring} archivebox.workers.supervisord_util.stop_existing_supervisord_process
```
````

````{py:function} start_new_supervisord_process(daemonize=False)
:canonical: archivebox.workers.supervisord_util.start_new_supervisord_process

```{autodoc2-docstring} archivebox.workers.supervisord_util.start_new_supervisord_process
```
````

````{py:function} wait_for_supervisord_ready(max_wait_sec: float = 5.0, interval_sec: float = 0.1)
:canonical: archivebox.workers.supervisord_util.wait_for_supervisord_ready

```{autodoc2-docstring} archivebox.workers.supervisord_util.wait_for_supervisord_ready
```
````

````{py:function} get_or_create_supervisord_process(daemonize=False)
:canonical: archivebox.workers.supervisord_util.get_or_create_supervisord_process

```{autodoc2-docstring} archivebox.workers.supervisord_util.get_or_create_supervisord_process
```
````

````{py:function} start_worker(supervisor, daemon, lazy=False)
:canonical: archivebox.workers.supervisord_util.start_worker

```{autodoc2-docstring} archivebox.workers.supervisord_util.start_worker
```
````

````{py:function} get_worker(supervisor, daemon_name)
:canonical: archivebox.workers.supervisord_util.get_worker

```{autodoc2-docstring} archivebox.workers.supervisord_util.get_worker
```
````

````{py:function} stop_worker(supervisor, daemon_name)
:canonical: archivebox.workers.supervisord_util.stop_worker

```{autodoc2-docstring} archivebox.workers.supervisord_util.stop_worker
```
````

````{py:function} tail_worker_logs(log_path: str)
:canonical: archivebox.workers.supervisord_util.tail_worker_logs

```{autodoc2-docstring} archivebox.workers.supervisord_util.tail_worker_logs
```
````

````{py:function} tail_multiple_worker_logs(log_files: list[str], follow=True, proc=None)
:canonical: archivebox.workers.supervisord_util.tail_multiple_worker_logs

```{autodoc2-docstring} archivebox.workers.supervisord_util.tail_multiple_worker_logs
```
````

````{py:function} watch_worker(supervisor, daemon_name, interval=5)
:canonical: archivebox.workers.supervisord_util.watch_worker

```{autodoc2-docstring} archivebox.workers.supervisord_util.watch_worker
```
````

````{py:function} start_server_workers(host='0.0.0.0', port='8000', daemonize=False)
:canonical: archivebox.workers.supervisord_util.start_server_workers

```{autodoc2-docstring} archivebox.workers.supervisord_util.start_server_workers
```
````

````{py:function} start_cli_workers(watch=False)
:canonical: archivebox.workers.supervisord_util.start_cli_workers

```{autodoc2-docstring} archivebox.workers.supervisord_util.start_cli_workers
```
````
