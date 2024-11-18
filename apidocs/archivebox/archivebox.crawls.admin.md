# {py:mod}`archivebox.crawls.admin`

```{py:module} archivebox.crawls.admin
```

```{autodoc2-docstring} archivebox.crawls.admin
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CrawlAdmin <archivebox.crawls.admin.CrawlAdmin>`
  -
* - {py:obj}`CrawlScheduleAdmin <archivebox.crawls.admin.CrawlScheduleAdmin>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`register_admin <archivebox.crawls.admin.register_admin>`
  - ```{autodoc2-docstring} archivebox.crawls.admin.register_admin
    :summary:
    ```
````

### API

`````{py:class} CrawlAdmin(model, admin_site)
:canonical: archivebox.crawls.admin.CrawlAdmin

Bases: {py:obj}`abid_utils.admin.ABIDModelAdmin`

````{py:attribute} list_display
:canonical: archivebox.crawls.admin.CrawlAdmin.list_display
:value: >
   ('abid', 'created_at', 'created_by', 'max_depth', 'label', 'notes', 'seed_str', 'schedule_str', 'sta...

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.list_display
```

````

````{py:attribute} sort_fields
:canonical: archivebox.crawls.admin.CrawlAdmin.sort_fields
:value: >
   ('abid', 'created_at', 'created_by', 'max_depth', 'label', 'notes', 'seed_str', 'schedule_str', 'sta...

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.sort_fields
```

````

````{py:attribute} search_fields
:canonical: archivebox.crawls.admin.CrawlAdmin.search_fields
:value: >
   ('abid', 'created_by__username', 'max_depth', 'label', 'notes', 'seed_id', 'seed__abid', 'schedule_i...

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.search_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.crawls.admin.CrawlAdmin.readonly_fields
:value: >
   ('created_at', 'modified_at', 'abid_info', 'snapshots', 'seed_contents')

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.readonly_fields
```

````

````{py:attribute} fields
:canonical: archivebox.crawls.admin.CrawlAdmin.fields
:value: >
   ('label', 'notes', 'status', 'retry_at', 'max_depth', 'seed', 'schedule', 'created_by')

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.fields
```

````

````{py:attribute} list_filter
:canonical: archivebox.crawls.admin.CrawlAdmin.list_filter
:value: >
   ('max_depth', 'seed', 'schedule', 'created_by', 'status', 'retry_at')

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.list_filter
```

````

````{py:attribute} ordering
:canonical: archivebox.crawls.admin.CrawlAdmin.ordering
:value: >
   ['-created_at', '-retry_at']

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.ordering
```

````

````{py:attribute} list_per_page
:canonical: archivebox.crawls.admin.CrawlAdmin.list_per_page
:value: >
   100

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.list_per_page
```

````

````{py:attribute} actions
:canonical: archivebox.crawls.admin.CrawlAdmin.actions
:value: >
   ['delete_selected']

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.actions
```

````

````{py:method} num_snapshots(obj)
:canonical: archivebox.crawls.admin.CrawlAdmin.num_snapshots

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.num_snapshots
```

````

````{py:method} snapshots(obj)
:canonical: archivebox.crawls.admin.CrawlAdmin.snapshots

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.snapshots
```

````

````{py:method} schedule_str(obj)
:canonical: archivebox.crawls.admin.CrawlAdmin.schedule_str

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.schedule_str
```

````

````{py:method} seed_str(obj)
:canonical: archivebox.crawls.admin.CrawlAdmin.seed_str

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.seed_str
```

````

````{py:method} seed_contents(obj)
:canonical: archivebox.crawls.admin.CrawlAdmin.seed_contents

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.seed_contents
```

````

`````

`````{py:class} CrawlScheduleAdmin(model, admin_site)
:canonical: archivebox.crawls.admin.CrawlScheduleAdmin

Bases: {py:obj}`abid_utils.admin.ABIDModelAdmin`

````{py:attribute} list_display
:canonical: archivebox.crawls.admin.CrawlScheduleAdmin.list_display
:value: >
   ('abid', 'created_at', 'created_by', 'label', 'notes', 'template_str', 'crawls', 'num_crawls', 'num_...

```{autodoc2-docstring} archivebox.crawls.admin.CrawlScheduleAdmin.list_display
```

````

````{py:attribute} sort_fields
:canonical: archivebox.crawls.admin.CrawlScheduleAdmin.sort_fields
:value: >
   ('abid', 'created_at', 'created_by', 'label', 'notes', 'template_str')

```{autodoc2-docstring} archivebox.crawls.admin.CrawlScheduleAdmin.sort_fields
```

````

````{py:attribute} search_fields
:canonical: archivebox.crawls.admin.CrawlScheduleAdmin.search_fields
:value: >
   ('abid', 'created_by__username', 'label', 'notes', 'schedule_id', 'schedule__abid', 'template_id', '...

```{autodoc2-docstring} archivebox.crawls.admin.CrawlScheduleAdmin.search_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.crawls.admin.CrawlScheduleAdmin.readonly_fields
:value: >
   ('created_at', 'modified_at', 'abid_info', 'crawls', 'snapshots')

```{autodoc2-docstring} archivebox.crawls.admin.CrawlScheduleAdmin.readonly_fields
```

````

````{py:attribute} fields
:canonical: archivebox.crawls.admin.CrawlScheduleAdmin.fields
:value: >
   ('label', 'notes', 'schedule', 'template', 'created_by')

```{autodoc2-docstring} archivebox.crawls.admin.CrawlScheduleAdmin.fields
```

````

````{py:attribute} list_filter
:canonical: archivebox.crawls.admin.CrawlScheduleAdmin.list_filter
:value: >
   ('created_by',)

```{autodoc2-docstring} archivebox.crawls.admin.CrawlScheduleAdmin.list_filter
```

````

````{py:attribute} ordering
:canonical: archivebox.crawls.admin.CrawlScheduleAdmin.ordering
:value: >
   ['-created_at']

```{autodoc2-docstring} archivebox.crawls.admin.CrawlScheduleAdmin.ordering
```

````

````{py:attribute} list_per_page
:canonical: archivebox.crawls.admin.CrawlScheduleAdmin.list_per_page
:value: >
   100

```{autodoc2-docstring} archivebox.crawls.admin.CrawlScheduleAdmin.list_per_page
```

````

````{py:attribute} actions
:canonical: archivebox.crawls.admin.CrawlScheduleAdmin.actions
:value: >
   ['delete_selected']

```{autodoc2-docstring} archivebox.crawls.admin.CrawlScheduleAdmin.actions
```

````

````{py:method} template_str(obj)
:canonical: archivebox.crawls.admin.CrawlScheduleAdmin.template_str

```{autodoc2-docstring} archivebox.crawls.admin.CrawlScheduleAdmin.template_str
```

````

````{py:method} num_crawls(obj)
:canonical: archivebox.crawls.admin.CrawlScheduleAdmin.num_crawls

```{autodoc2-docstring} archivebox.crawls.admin.CrawlScheduleAdmin.num_crawls
```

````

````{py:method} num_snapshots(obj)
:canonical: archivebox.crawls.admin.CrawlScheduleAdmin.num_snapshots

```{autodoc2-docstring} archivebox.crawls.admin.CrawlScheduleAdmin.num_snapshots
```

````

````{py:method} crawls(obj)
:canonical: archivebox.crawls.admin.CrawlScheduleAdmin.crawls

```{autodoc2-docstring} archivebox.crawls.admin.CrawlScheduleAdmin.crawls
```

````

````{py:method} snapshots(obj)
:canonical: archivebox.crawls.admin.CrawlScheduleAdmin.snapshots

```{autodoc2-docstring} archivebox.crawls.admin.CrawlScheduleAdmin.snapshots
```

````

`````

````{py:function} register_admin(admin_site)
:canonical: archivebox.crawls.admin.register_admin

```{autodoc2-docstring} archivebox.crawls.admin.register_admin
```
````
