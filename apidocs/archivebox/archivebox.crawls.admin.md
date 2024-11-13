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
   ('abid', 'created_at', 'created_by', 'depth', 'parser', 'urls')

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.list_display
```

````

````{py:attribute} sort_fields
:canonical: archivebox.crawls.admin.CrawlAdmin.sort_fields
:value: >
   ('abid', 'created_at', 'created_by', 'depth', 'parser', 'urls')

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.sort_fields
```

````

````{py:attribute} search_fields
:canonical: archivebox.crawls.admin.CrawlAdmin.search_fields
:value: >
   ('abid', 'created_by__username', 'depth', 'parser', 'urls')

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.search_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.crawls.admin.CrawlAdmin.readonly_fields
:value: >
   ('created_at', 'modified_at', 'abid_info')

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.readonly_fields
```

````

````{py:attribute} fields
:canonical: archivebox.crawls.admin.CrawlAdmin.fields
:value: >
   ('urls', 'depth', 'parser', 'created_by')

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.fields
```

````

````{py:attribute} list_filter
:canonical: archivebox.crawls.admin.CrawlAdmin.list_filter
:value: >
   ('depth', 'parser', 'created_by')

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.list_filter
```

````

````{py:attribute} ordering
:canonical: archivebox.crawls.admin.CrawlAdmin.ordering
:value: >
   ['-created_at']

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

`````

````{py:function} register_admin(admin_site)
:canonical: archivebox.crawls.admin.register_admin

```{autodoc2-docstring} archivebox.crawls.admin.register_admin
```
````
