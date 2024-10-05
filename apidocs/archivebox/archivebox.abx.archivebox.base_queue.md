# {py:mod}`archivebox.abx.archivebox.base_queue`

```{py:module} archivebox.abx.archivebox.base_queue
```

```{autodoc2-docstring} archivebox.abx.archivebox.base_queue
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseQueue <archivebox.abx.archivebox.base_queue.BaseQueue>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.abx.archivebox.base_queue.__package__>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_queue.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.abx.archivebox.base_queue.__package__
:value: >
   'abx.archivebox'

```{autodoc2-docstring} archivebox.abx.archivebox.base_queue.__package__
```

````

`````{py:class} BaseQueue(/, **data: typing.Any)
:canonical: archivebox.abx.archivebox.base_queue.BaseQueue

Bases: {py:obj}`archivebox.abx.archivebox.base_hook.BaseHook`

````{py:attribute} hook_type
:canonical: archivebox.abx.archivebox.base_queue.BaseQueue.hook_type
:type: archivebox.abx.archivebox.base_hook.HookType
:value: >
   'QUEUE'

```{autodoc2-docstring} archivebox.abx.archivebox.base_queue.BaseQueue.hook_type
```

````

````{py:attribute} name
:canonical: archivebox.abx.archivebox.base_queue.BaseQueue.name
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.abx.archivebox.base_queue.BaseQueue.name
```

````

````{py:attribute} binaries
:canonical: archivebox.abx.archivebox.base_queue.BaseQueue.binaries
:type: typing.List[pydantic.InstanceOf[archivebox.abx.archivebox.base_binary.BaseBinary]]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.abx.archivebox.base_queue.BaseQueue.binaries
```

````

````{py:property} tasks
:canonical: archivebox.abx.archivebox.base_queue.BaseQueue.tasks
:type: typing.Dict[str, huey.api.TaskWrapper]

```{autodoc2-docstring} archivebox.abx.archivebox.base_queue.BaseQueue.tasks
```

````

````{py:method} get_django_huey_config(QUEUE_DATABASE_NAME) -> dict
:canonical: archivebox.abx.archivebox.base_queue.BaseQueue.get_django_huey_config

```{autodoc2-docstring} archivebox.abx.archivebox.base_queue.BaseQueue.get_django_huey_config
```

````

````{py:method} get_supervisord_config(settings) -> dict
:canonical: archivebox.abx.archivebox.base_queue.BaseQueue.get_supervisord_config

```{autodoc2-docstring} archivebox.abx.archivebox.base_queue.BaseQueue.get_supervisord_config
```

````

````{py:method} start_supervisord_worker(settings, lazy=True)
:canonical: archivebox.abx.archivebox.base_queue.BaseQueue.start_supervisord_worker

```{autodoc2-docstring} archivebox.abx.archivebox.base_queue.BaseQueue.start_supervisord_worker
```

````

````{py:method} get_QUEUES()
:canonical: archivebox.abx.archivebox.base_queue.BaseQueue.get_QUEUES

```{autodoc2-docstring} archivebox.abx.archivebox.base_queue.BaseQueue.get_QUEUES
```

````

````{py:method} get_DJANGO_HUEY_QUEUES(QUEUE_DATABASE_NAME)
:canonical: archivebox.abx.archivebox.base_queue.BaseQueue.get_DJANGO_HUEY_QUEUES

```{autodoc2-docstring} archivebox.abx.archivebox.base_queue.BaseQueue.get_DJANGO_HUEY_QUEUES
```

````

`````
