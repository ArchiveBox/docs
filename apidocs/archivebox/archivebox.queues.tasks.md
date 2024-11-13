# {py:mod}`archivebox.queues.tasks`

```{py:module} archivebox.queues.tasks
```

```{autodoc2-docstring} archivebox.queues.tasks
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`db_task_with_parent <archivebox.queues.tasks.db_task_with_parent>`
  - ```{autodoc2-docstring} archivebox.queues.tasks.db_task_with_parent
    :summary:
    ```
* - {py:obj}`bg_add <archivebox.queues.tasks.bg_add>`
  - ```{autodoc2-docstring} archivebox.queues.tasks.bg_add
    :summary:
    ```
* - {py:obj}`bg_archive_links <archivebox.queues.tasks.bg_archive_links>`
  - ```{autodoc2-docstring} archivebox.queues.tasks.bg_archive_links
    :summary:
    ```
* - {py:obj}`bg_archive_link <archivebox.queues.tasks.bg_archive_link>`
  - ```{autodoc2-docstring} archivebox.queues.tasks.bg_archive_link
    :summary:
    ```
* - {py:obj}`bg_archive_snapshot <archivebox.queues.tasks.bg_archive_snapshot>`
  - ```{autodoc2-docstring} archivebox.queues.tasks.bg_archive_snapshot
    :summary:
    ```
````

### API

````{py:function} db_task_with_parent(func)
:canonical: archivebox.queues.tasks.db_task_with_parent

```{autodoc2-docstring} archivebox.queues.tasks.db_task_with_parent
```
````

````{py:function} bg_add(add_kwargs, task=None, parent_task_id=None)
:canonical: archivebox.queues.tasks.bg_add

```{autodoc2-docstring} archivebox.queues.tasks.bg_add
```
````

````{py:function} bg_archive_links(args, kwargs=None, task=None, parent_task_id=None)
:canonical: archivebox.queues.tasks.bg_archive_links

```{autodoc2-docstring} archivebox.queues.tasks.bg_archive_links
```
````

````{py:function} bg_archive_link(args, kwargs=None, task=None, parent_task_id=None)
:canonical: archivebox.queues.tasks.bg_archive_link

```{autodoc2-docstring} archivebox.queues.tasks.bg_archive_link
```
````

````{py:function} bg_archive_snapshot(snapshot, overwrite=False, methods=None, task=None, parent_task_id=None)
:canonical: archivebox.queues.tasks.bg_archive_snapshot

```{autodoc2-docstring} archivebox.queues.tasks.bg_archive_snapshot
```
````
