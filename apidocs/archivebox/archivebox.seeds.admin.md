# {py:mod}`archivebox.seeds.admin`

```{py:module} archivebox.seeds.admin
```

```{autodoc2-docstring} archivebox.seeds.admin
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SeedAdmin <archivebox.seeds.admin.SeedAdmin>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`register_admin <archivebox.seeds.admin.register_admin>`
  - ```{autodoc2-docstring} archivebox.seeds.admin.register_admin
    :summary:
    ```
````

### API

`````{py:class} SeedAdmin(model, admin_site)
:canonical: archivebox.seeds.admin.SeedAdmin

Bases: {py:obj}`abid_utils.admin.ABIDModelAdmin`

````{py:attribute} list_display
:canonical: archivebox.seeds.admin.SeedAdmin.list_display
:value: >
   ('abid', 'created_at', 'created_by', 'label', 'notes', 'uri', 'extractor', 'tags_str', 'crawls', 'nu...

```{autodoc2-docstring} archivebox.seeds.admin.SeedAdmin.list_display
```

````

````{py:attribute} sort_fields
:canonical: archivebox.seeds.admin.SeedAdmin.sort_fields
:value: >
   ('abid', 'created_at', 'created_by', 'label', 'notes', 'uri', 'extractor', 'tags_str')

```{autodoc2-docstring} archivebox.seeds.admin.SeedAdmin.sort_fields
```

````

````{py:attribute} search_fields
:canonical: archivebox.seeds.admin.SeedAdmin.search_fields
:value: >
   ('abid', 'created_by__username', 'label', 'notes', 'uri', 'extractor', 'tags_str')

```{autodoc2-docstring} archivebox.seeds.admin.SeedAdmin.search_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.seeds.admin.SeedAdmin.readonly_fields
:value: >
   ('created_at', 'modified_at', 'abid_info', 'scheduled_crawls', 'crawls', 'snapshots', 'contents')

```{autodoc2-docstring} archivebox.seeds.admin.SeedAdmin.readonly_fields
```

````

````{py:attribute} fields
:canonical: archivebox.seeds.admin.SeedAdmin.fields
:value: >
   ('label', 'notes', 'uri', 'extractor', 'tags_str', 'config', 'created_by')

```{autodoc2-docstring} archivebox.seeds.admin.SeedAdmin.fields
```

````

````{py:attribute} list_filter
:canonical: archivebox.seeds.admin.SeedAdmin.list_filter
:value: >
   ('extractor', 'created_by')

```{autodoc2-docstring} archivebox.seeds.admin.SeedAdmin.list_filter
```

````

````{py:attribute} ordering
:canonical: archivebox.seeds.admin.SeedAdmin.ordering
:value: >
   ['-created_at']

```{autodoc2-docstring} archivebox.seeds.admin.SeedAdmin.ordering
```

````

````{py:attribute} list_per_page
:canonical: archivebox.seeds.admin.SeedAdmin.list_per_page
:value: >
   100

```{autodoc2-docstring} archivebox.seeds.admin.SeedAdmin.list_per_page
```

````

````{py:attribute} actions
:canonical: archivebox.seeds.admin.SeedAdmin.actions
:value: >
   ['delete_selected']

```{autodoc2-docstring} archivebox.seeds.admin.SeedAdmin.actions
```

````

````{py:method} num_crawls(obj)
:canonical: archivebox.seeds.admin.SeedAdmin.num_crawls

```{autodoc2-docstring} archivebox.seeds.admin.SeedAdmin.num_crawls
```

````

````{py:method} num_snapshots(obj)
:canonical: archivebox.seeds.admin.SeedAdmin.num_snapshots

```{autodoc2-docstring} archivebox.seeds.admin.SeedAdmin.num_snapshots
```

````

````{py:method} scheduled_crawls(obj)
:canonical: archivebox.seeds.admin.SeedAdmin.scheduled_crawls

```{autodoc2-docstring} archivebox.seeds.admin.SeedAdmin.scheduled_crawls
```

````

````{py:method} crawls(obj)
:canonical: archivebox.seeds.admin.SeedAdmin.crawls

```{autodoc2-docstring} archivebox.seeds.admin.SeedAdmin.crawls
```

````

````{py:method} snapshots(obj)
:canonical: archivebox.seeds.admin.SeedAdmin.snapshots

```{autodoc2-docstring} archivebox.seeds.admin.SeedAdmin.snapshots
```

````

````{py:method} contents(obj)
:canonical: archivebox.seeds.admin.SeedAdmin.contents

```{autodoc2-docstring} archivebox.seeds.admin.SeedAdmin.contents
```

````

`````

````{py:function} register_admin(admin_site)
:canonical: archivebox.seeds.admin.register_admin

```{autodoc2-docstring} archivebox.seeds.admin.register_admin
```
````
