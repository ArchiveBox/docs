# {py:mod}`archivebox.queues.admin`

```{py:module} archivebox.queues.admin
```

```{autodoc2-docstring} archivebox.queues.admin
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CustomTaskModelAdmin <archivebox.queues.admin.CustomTaskModelAdmin>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`register_admin <archivebox.queues.admin.register_admin>`
  - ```{autodoc2-docstring} archivebox.queues.admin.register_admin
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.queues.admin.__package__>`
  - ```{autodoc2-docstring} archivebox.queues.admin.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.queues.admin.__package__
:value: >
   'archivebox.queues'

```{autodoc2-docstring} archivebox.queues.admin.__package__
```

````

`````{py:class} CustomTaskModelAdmin(model, admin_site)
:canonical: archivebox.queues.admin.CustomTaskModelAdmin

Bases: {py:obj}`huey_monitor.admin.TaskModelAdmin`

````{py:attribute} actions
:canonical: archivebox.queues.admin.CustomTaskModelAdmin.actions
:value: >
   ['delete_selected']

```{autodoc2-docstring} archivebox.queues.admin.CustomTaskModelAdmin.actions
```

````

````{py:method} has_delete_permission(request, obj=None)
:canonical: archivebox.queues.admin.CustomTaskModelAdmin.has_delete_permission

````

`````

````{py:function} register_admin(admin_site)
:canonical: archivebox.queues.admin.register_admin

```{autodoc2-docstring} archivebox.queues.admin.register_admin
```
````
