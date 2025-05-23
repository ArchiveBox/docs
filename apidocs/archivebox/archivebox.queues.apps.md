# {py:mod}`archivebox.queues.apps`

```{py:module} archivebox.queues.apps
```

```{autodoc2-docstring} archivebox.queues.apps
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`QueuesConfig <archivebox.queues.apps.QueuesConfig>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`register_admin <archivebox.queues.apps.register_admin>`
  - ```{autodoc2-docstring} archivebox.queues.apps.register_admin
    :summary:
    ```
````

### API

`````{py:class} QueuesConfig(app_name, app_module)
:canonical: archivebox.queues.apps.QueuesConfig

Bases: {py:obj}`django.apps.AppConfig`

````{py:attribute} default_auto_field
:canonical: archivebox.queues.apps.QueuesConfig.default_auto_field
:value: >
   'django.db.models.BigAutoField'

```{autodoc2-docstring} archivebox.queues.apps.QueuesConfig.default_auto_field
```

````

````{py:attribute} name
:canonical: archivebox.queues.apps.QueuesConfig.name
:value: >
   'queues'

```{autodoc2-docstring} archivebox.queues.apps.QueuesConfig.name
```

````

`````

````{py:function} register_admin(admin_site)
:canonical: archivebox.queues.apps.register_admin

```{autodoc2-docstring} archivebox.queues.apps.register_admin
```
````
