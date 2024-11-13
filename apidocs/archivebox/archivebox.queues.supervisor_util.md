# {py:mod}`archivebox.queues.supervisor_util`

```{py:module} archivebox.queues.supervisor_util
```

```{autodoc2-docstring} archivebox.queues.supervisor_util
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_sock_file <archivebox.queues.supervisor_util.get_sock_file>`
  - ```{autodoc2-docstring} archivebox.queues.supervisor_util.get_sock_file
    :summary:
    ```
* - {py:obj}`follow <archivebox.queues.supervisor_util.follow>`
  - ```{autodoc2-docstring} archivebox.queues.supervisor_util.follow
    :summary:
    ```
* - {py:obj}`create_supervisord_config <archivebox.queues.supervisor_util.create_supervisord_config>`
  - ```{autodoc2-docstring} archivebox.queues.supervisor_util.create_supervisord_config
    :summary:
    ```
* - {py:obj}`create_worker_config <archivebox.queues.supervisor_util.create_worker_config>`
  - ```{autodoc2-docstring} archivebox.queues.supervisor_util.create_worker_config
    :summary:
    ```
* - {py:obj}`get_existing_supervisord_process <archivebox.queues.supervisor_util.get_existing_supervisord_process>`
  - ```{autodoc2-docstring} archivebox.queues.supervisor_util.get_existing_supervisord_process
    :summary:
    ```
* - {py:obj}`stop_existing_supervisord_process <archivebox.queues.supervisor_util.stop_existing_supervisord_process>`
  - ```{autodoc2-docstring} archivebox.queues.supervisor_util.stop_existing_supervisord_process
    :summary:
    ```
* - {py:obj}`start_new_supervisord_process <archivebox.queues.supervisor_util.start_new_supervisord_process>`
  - ```{autodoc2-docstring} archivebox.queues.supervisor_util.start_new_supervisord_process
    :summary:
    ```
* - {py:obj}`get_or_create_supervisord_process <archivebox.queues.supervisor_util.get_or_create_supervisord_process>`
  - ```{autodoc2-docstring} archivebox.queues.supervisor_util.get_or_create_supervisord_process
    :summary:
    ```
* - {py:obj}`start_worker <archivebox.queues.supervisor_util.start_worker>`
  - ```{autodoc2-docstring} archivebox.queues.supervisor_util.start_worker
    :summary:
    ```
* - {py:obj}`get_worker <archivebox.queues.supervisor_util.get_worker>`
  - ```{autodoc2-docstring} archivebox.queues.supervisor_util.get_worker
    :summary:
    ```
* - {py:obj}`stop_worker <archivebox.queues.supervisor_util.stop_worker>`
  - ```{autodoc2-docstring} archivebox.queues.supervisor_util.stop_worker
    :summary:
    ```
* - {py:obj}`tail_worker_logs <archivebox.queues.supervisor_util.tail_worker_logs>`
  - ```{autodoc2-docstring} archivebox.queues.supervisor_util.tail_worker_logs
    :summary:
    ```
* - {py:obj}`watch_worker <archivebox.queues.supervisor_util.watch_worker>`
  - ```{autodoc2-docstring} archivebox.queues.supervisor_util.watch_worker
    :summary:
    ```
* - {py:obj}`start_server_workers <archivebox.queues.supervisor_util.start_server_workers>`
  - ```{autodoc2-docstring} archivebox.queues.supervisor_util.start_server_workers
    :summary:
    ```
* - {py:obj}`start_cli_workers <archivebox.queues.supervisor_util.start_cli_workers>`
  - ```{autodoc2-docstring} archivebox.queues.supervisor_util.start_cli_workers
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`LOG_FILE_NAME <archivebox.queues.supervisor_util.LOG_FILE_NAME>`
  - ```{autodoc2-docstring} archivebox.queues.supervisor_util.LOG_FILE_NAME
    :summary:
    ```
* - {py:obj}`CONFIG_FILE_NAME <archivebox.queues.supervisor_util.CONFIG_FILE_NAME>`
  - ```{autodoc2-docstring} archivebox.queues.supervisor_util.CONFIG_FILE_NAME
    :summary:
    ```
* - {py:obj}`PID_FILE_NAME <archivebox.queues.supervisor_util.PID_FILE_NAME>`
  - ```{autodoc2-docstring} archivebox.queues.supervisor_util.PID_FILE_NAME
    :summary:
    ```
* - {py:obj}`WORKERS_DIR_NAME <archivebox.queues.supervisor_util.WORKERS_DIR_NAME>`
  - ```{autodoc2-docstring} archivebox.queues.supervisor_util.WORKERS_DIR_NAME
    :summary:
    ```
* - {py:obj}`SCHEDULER_WORKER <archivebox.queues.supervisor_util.SCHEDULER_WORKER>`
  - ```{autodoc2-docstring} archivebox.queues.supervisor_util.SCHEDULER_WORKER
    :summary:
    ```
* - {py:obj}`COMMAND_WORKER <archivebox.queues.supervisor_util.COMMAND_WORKER>`
  - ```{autodoc2-docstring} archivebox.queues.supervisor_util.COMMAND_WORKER
    :summary:
    ```
````

### API

````{py:data} LOG_FILE_NAME
:canonical: archivebox.queues.supervisor_util.LOG_FILE_NAME
:value: >
   'supervisord.log'

```{autodoc2-docstring} archivebox.queues.supervisor_util.LOG_FILE_NAME
```

````

````{py:data} CONFIG_FILE_NAME
:canonical: archivebox.queues.supervisor_util.CONFIG_FILE_NAME
:value: >
   'supervisord.conf'

```{autodoc2-docstring} archivebox.queues.supervisor_util.CONFIG_FILE_NAME
```

````

````{py:data} PID_FILE_NAME
:canonical: archivebox.queues.supervisor_util.PID_FILE_NAME
:value: >
   'supervisord.pid'

```{autodoc2-docstring} archivebox.queues.supervisor_util.PID_FILE_NAME
```

````

````{py:data} WORKERS_DIR_NAME
:canonical: archivebox.queues.supervisor_util.WORKERS_DIR_NAME
:value: >
   'workers'

```{autodoc2-docstring} archivebox.queues.supervisor_util.WORKERS_DIR_NAME
```

````

````{py:data} SCHEDULER_WORKER
:canonical: archivebox.queues.supervisor_util.SCHEDULER_WORKER
:value: >
   None

```{autodoc2-docstring} archivebox.queues.supervisor_util.SCHEDULER_WORKER
```

````

````{py:data} COMMAND_WORKER
:canonical: archivebox.queues.supervisor_util.COMMAND_WORKER
:value: >
   None

```{autodoc2-docstring} archivebox.queues.supervisor_util.COMMAND_WORKER
```

````

````{py:function} get_sock_file()
:canonical: archivebox.queues.supervisor_util.get_sock_file

```{autodoc2-docstring} archivebox.queues.supervisor_util.get_sock_file
```
````

````{py:function} follow(file, sleep_sec=0.1) -> typing.Iterator[str]
:canonical: archivebox.queues.supervisor_util.follow

```{autodoc2-docstring} archivebox.queues.supervisor_util.follow
```
````

````{py:function} create_supervisord_config()
:canonical: archivebox.queues.supervisor_util.create_supervisord_config

```{autodoc2-docstring} archivebox.queues.supervisor_util.create_supervisord_config
```
````

````{py:function} create_worker_config(daemon)
:canonical: archivebox.queues.supervisor_util.create_worker_config

```{autodoc2-docstring} archivebox.queues.supervisor_util.create_worker_config
```
````

````{py:function} get_existing_supervisord_process()
:canonical: archivebox.queues.supervisor_util.get_existing_supervisord_process

```{autodoc2-docstring} archivebox.queues.supervisor_util.get_existing_supervisord_process
```
````

````{py:function} stop_existing_supervisord_process()
:canonical: archivebox.queues.supervisor_util.stop_existing_supervisord_process

```{autodoc2-docstring} archivebox.queues.supervisor_util.stop_existing_supervisord_process
```
````

````{py:function} start_new_supervisord_process(daemonize=False)
:canonical: archivebox.queues.supervisor_util.start_new_supervisord_process

```{autodoc2-docstring} archivebox.queues.supervisor_util.start_new_supervisord_process
```
````

````{py:function} get_or_create_supervisord_process(daemonize=False)
:canonical: archivebox.queues.supervisor_util.get_or_create_supervisord_process

```{autodoc2-docstring} archivebox.queues.supervisor_util.get_or_create_supervisord_process
```
````

````{py:function} start_worker(supervisor, daemon, lazy=False)
:canonical: archivebox.queues.supervisor_util.start_worker

```{autodoc2-docstring} archivebox.queues.supervisor_util.start_worker
```
````

````{py:function} get_worker(supervisor, daemon_name)
:canonical: archivebox.queues.supervisor_util.get_worker

```{autodoc2-docstring} archivebox.queues.supervisor_util.get_worker
```
````

````{py:function} stop_worker(supervisor, daemon_name)
:canonical: archivebox.queues.supervisor_util.stop_worker

```{autodoc2-docstring} archivebox.queues.supervisor_util.stop_worker
```
````

````{py:function} tail_worker_logs(log_path: str)
:canonical: archivebox.queues.supervisor_util.tail_worker_logs

```{autodoc2-docstring} archivebox.queues.supervisor_util.tail_worker_logs
```
````

````{py:function} watch_worker(supervisor, daemon_name, interval=5)
:canonical: archivebox.queues.supervisor_util.watch_worker

```{autodoc2-docstring} archivebox.queues.supervisor_util.watch_worker
```
````

````{py:function} start_server_workers(host='0.0.0.0', port='8000', daemonize=False)
:canonical: archivebox.queues.supervisor_util.start_server_workers

```{autodoc2-docstring} archivebox.queues.supervisor_util.start_server_workers
```
````

````{py:function} start_cli_workers(watch=False)
:canonical: archivebox.queues.supervisor_util.start_cli_workers

```{autodoc2-docstring} archivebox.queues.supervisor_util.start_cli_workers
```
````
