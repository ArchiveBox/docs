# {py:mod}`archivebox.queues.semaphores`

```{py:module} archivebox.queues.semaphores
```

```{autodoc2-docstring} archivebox.queues.semaphores
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SqliteSemaphore <archivebox.queues.semaphores.SqliteSemaphore>`
  - ```{autodoc2-docstring} archivebox.queues.semaphores.SqliteSemaphore
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`lock_task_semaphore <archivebox.queues.semaphores.lock_task_semaphore>`
  - ```{autodoc2-docstring} archivebox.queues.semaphores.lock_task_semaphore
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`LOCKS_DB_PATH <archivebox.queues.semaphores.LOCKS_DB_PATH>`
  - ```{autodoc2-docstring} archivebox.queues.semaphores.LOCKS_DB_PATH
    :summary:
    ```
````

### API

`````{py:class} SqliteSemaphore(db_path, table_name, name, value=1, timeout=None)
:canonical: archivebox.queues.semaphores.SqliteSemaphore

```{autodoc2-docstring} archivebox.queues.semaphores.SqliteSemaphore
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.queues.semaphores.SqliteSemaphore.__init__
```

````{py:method} acquire(name=None)
:canonical: archivebox.queues.semaphores.SqliteSemaphore.acquire

```{autodoc2-docstring} archivebox.queues.semaphores.SqliteSemaphore.acquire
```

````

````{py:method} release(name)
:canonical: archivebox.queues.semaphores.SqliteSemaphore.release

```{autodoc2-docstring} archivebox.queues.semaphores.SqliteSemaphore.release
```

````

`````

````{py:data} LOCKS_DB_PATH
:canonical: archivebox.queues.semaphores.LOCKS_DB_PATH
:value: >
   None

```{autodoc2-docstring} archivebox.queues.semaphores.LOCKS_DB_PATH
```

````

````{py:function} lock_task_semaphore(db_path, table_name, lock_name, value=1, timeout=None)
:canonical: archivebox.queues.semaphores.lock_task_semaphore

```{autodoc2-docstring} archivebox.queues.semaphores.lock_task_semaphore
```
````
