# {py:mod}`archivebox.core.admin_tags`

```{py:module} archivebox.core.admin_tags
```

```{autodoc2-docstring} archivebox.core.admin_tags
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TagInline <archivebox.core.admin_tags.TagInline>`
  -
* - {py:obj}`TagAdmin <archivebox.core.admin_tags.TagAdmin>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`register_admin <archivebox.core.admin_tags.register_admin>`
  - ```{autodoc2-docstring} archivebox.core.admin_tags.register_admin
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.core.admin_tags.__package__>`
  - ```{autodoc2-docstring} archivebox.core.admin_tags.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.core.admin_tags.__package__
:value: >
   'archivebox.core'

```{autodoc2-docstring} archivebox.core.admin_tags.__package__
```

````

`````{py:class} TagInline(parent_model, admin_site)
:canonical: archivebox.core.admin_tags.TagInline

Bases: {py:obj}`django.contrib.admin.TabularInline`

````{py:attribute} model
:canonical: archivebox.core.admin_tags.TagInline.model
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin_tags.TagInline.model
```

````

````{py:attribute} fields
:canonical: archivebox.core.admin_tags.TagInline.fields
:value: >
   ('id', 'tag')

```{autodoc2-docstring} archivebox.core.admin_tags.TagInline.fields
```

````

````{py:attribute} extra
:canonical: archivebox.core.admin_tags.TagInline.extra
:value: >
   1

```{autodoc2-docstring} archivebox.core.admin_tags.TagInline.extra
```

````

````{py:attribute} max_num
:canonical: archivebox.core.admin_tags.TagInline.max_num
:value: >
   1000

```{autodoc2-docstring} archivebox.core.admin_tags.TagInline.max_num
```

````

````{py:attribute} autocomplete_fields
:canonical: archivebox.core.admin_tags.TagInline.autocomplete_fields
:value: >
   ('tag',)

```{autodoc2-docstring} archivebox.core.admin_tags.TagInline.autocomplete_fields
```

````

`````

`````{py:class} TagAdmin(model, admin_site)
:canonical: archivebox.core.admin_tags.TagAdmin

Bases: {py:obj}`abid_utils.admin.ABIDModelAdmin`

````{py:attribute} list_display
:canonical: archivebox.core.admin_tags.TagAdmin.list_display
:value: >
   ('created_at', 'created_by', 'abid', 'name', 'num_snapshots', 'snapshots')

```{autodoc2-docstring} archivebox.core.admin_tags.TagAdmin.list_display
```

````

````{py:attribute} list_filter
:canonical: archivebox.core.admin_tags.TagAdmin.list_filter
:value: >
   ('created_at', 'created_by')

```{autodoc2-docstring} archivebox.core.admin_tags.TagAdmin.list_filter
```

````

````{py:attribute} sort_fields
:canonical: archivebox.core.admin_tags.TagAdmin.sort_fields
:value: >
   ('name', 'slug', 'abid', 'created_by', 'created_at')

```{autodoc2-docstring} archivebox.core.admin_tags.TagAdmin.sort_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.core.admin_tags.TagAdmin.readonly_fields
:value: >
   ('slug', 'abid', 'created_at', 'modified_at', 'abid_info', 'snapshots')

```{autodoc2-docstring} archivebox.core.admin_tags.TagAdmin.readonly_fields
```

````

````{py:attribute} search_fields
:canonical: archivebox.core.admin_tags.TagAdmin.search_fields
:value: >
   ('abid', 'name', 'slug')

```{autodoc2-docstring} archivebox.core.admin_tags.TagAdmin.search_fields
```

````

````{py:attribute} fields
:canonical: archivebox.core.admin_tags.TagAdmin.fields
:value: >
   ('name', 'created_by')

```{autodoc2-docstring} archivebox.core.admin_tags.TagAdmin.fields
```

````

````{py:attribute} actions
:canonical: archivebox.core.admin_tags.TagAdmin.actions
:value: >
   ['delete_selected', 'merge_tags']

```{autodoc2-docstring} archivebox.core.admin_tags.TagAdmin.actions
```

````

````{py:attribute} ordering
:canonical: archivebox.core.admin_tags.TagAdmin.ordering
:value: >
   ['-created_at']

```{autodoc2-docstring} archivebox.core.admin_tags.TagAdmin.ordering
```

````

````{py:attribute} paginator
:canonical: archivebox.core.admin_tags.TagAdmin.paginator
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin_tags.TagAdmin.paginator
```

````

````{py:method} num_snapshots(tag)
:canonical: archivebox.core.admin_tags.TagAdmin.num_snapshots

```{autodoc2-docstring} archivebox.core.admin_tags.TagAdmin.num_snapshots
```

````

````{py:method} snapshots(tag)
:canonical: archivebox.core.admin_tags.TagAdmin.snapshots

```{autodoc2-docstring} archivebox.core.admin_tags.TagAdmin.snapshots
```

````

`````

````{py:function} register_admin(admin_site)
:canonical: archivebox.core.admin_tags.register_admin

```{autodoc2-docstring} archivebox.core.admin_tags.register_admin
```
````
