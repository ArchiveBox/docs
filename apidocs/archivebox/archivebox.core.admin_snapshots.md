# {py:mod}`archivebox.core.admin_snapshots`

```{py:module} archivebox.core.admin_snapshots
```

```{autodoc2-docstring} archivebox.core.admin_snapshots
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SnapshotActionForm <archivebox.core.admin_snapshots.SnapshotActionForm>`
  -
* - {py:obj}`SnapshotAdmin <archivebox.core.admin_snapshots.SnapshotAdmin>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`GLOBAL_CONTEXT <archivebox.core.admin_snapshots.GLOBAL_CONTEXT>`
  - ```{autodoc2-docstring} archivebox.core.admin_snapshots.GLOBAL_CONTEXT
    :summary:
    ```
````

### API

````{py:data} GLOBAL_CONTEXT
:canonical: archivebox.core.admin_snapshots.GLOBAL_CONTEXT
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin_snapshots.GLOBAL_CONTEXT
```

````

`````{py:class} SnapshotActionForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, field_order=None, use_required_attribute=None, renderer=None)
:canonical: archivebox.core.admin_snapshots.SnapshotActionForm

Bases: {py:obj}`django.contrib.admin.helpers.ActionForm`

````{py:attribute} tags
:canonical: archivebox.core.admin_snapshots.SnapshotActionForm.tags
:value: >
   'ModelMultipleChoiceField(...)'

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotActionForm.tags
```

````

`````

`````{py:class} SnapshotAdmin(model, admin_site)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin

Bases: {py:obj}`archivebox.search.admin.SearchResultsAdminMixin`, {py:obj}`archivebox.abid_utils.admin.ABIDModelAdmin`

````{py:attribute} list_display
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.list_display
:value: >
   ('created_at', 'title_str', 'files', 'size', 'url_str')

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.list_display
```

````

````{py:attribute} sort_fields
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.sort_fields
:value: >
   ('title_str', 'url_str', 'created_at')

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.sort_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.readonly_fields
:value: >
   ('admin_actions', 'status_info', 'tags_str', 'imported_timestamp', 'created_at', 'modified_at', 'dow...

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.readonly_fields
```

````

````{py:attribute} search_fields
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.search_fields
:value: >
   ('id', 'url', 'abid', 'timestamp', 'title', 'tags__name')

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.search_fields
```

````

````{py:attribute} list_filter
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.list_filter
:value: >
   ('created_at', 'downloaded_at', 'archiveresult__status', 'created_by', 'tags__name')

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.list_filter
```

````

````{py:attribute} fields
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.fields
:value: >
   ('url', 'title', 'created_by', 'bookmarked_at')

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.fields
```

````

````{py:attribute} ordering
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.ordering
:value: >
   ['-created_at']

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.ordering
```

````

````{py:attribute} actions
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.actions
:value: >
   ['add_tags', 'remove_tags', 'update_titles', 'update_snapshots', 'resnapshot_snapshot', 'overwrite_s...

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.actions
```

````

````{py:attribute} inlines
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.inlines
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.inlines
```

````

````{py:attribute} list_per_page
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.list_per_page
:value: >
   'min(...)'

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.list_per_page
```

````

````{py:attribute} action_form
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.action_form
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.action_form
```

````

````{py:attribute} paginator
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.paginator
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.paginator
```

````

````{py:attribute} save_on_top
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.save_on_top
:value: >
   True

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.save_on_top
```

````

````{py:attribute} show_full_result_count
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.show_full_result_count
:value: >
   False

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.show_full_result_count
```

````

````{py:method} changelist_view(request, extra_context=None)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.changelist_view

````

````{py:method} get_urls()
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.get_urls

````

````{py:method} imported_timestamp(obj)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.imported_timestamp

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.imported_timestamp
```

````

````{py:method} admin_actions(obj)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.admin_actions

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.admin_actions
```

````

````{py:method} status_info(obj)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.status_info

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.status_info
```

````

````{py:method} title_str(obj)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.title_str

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.title_str
```

````

````{py:method} files(obj)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.files

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.files
```

````

````{py:method} size(obj)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.size

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.size
```

````

````{py:method} url_str(obj)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.url_str

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.url_str
```

````

````{py:method} grid_view(request, extra_context=None)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.grid_view

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.grid_view
```

````

````{py:method} update_titles(request, queryset)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.update_titles

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.update_titles
```

````

````{py:method} update_snapshots(request, queryset)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.update_snapshots

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.update_snapshots
```

````

````{py:method} resnapshot_snapshot(request, queryset)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.resnapshot_snapshot

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.resnapshot_snapshot
```

````

````{py:method} overwrite_snapshots(request, queryset)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.overwrite_snapshots

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.overwrite_snapshots
```

````

````{py:method} delete_snapshots(request, queryset)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.delete_snapshots

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.delete_snapshots
```

````

````{py:method} add_tags(request, queryset)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.add_tags

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.add_tags
```

````

````{py:method} remove_tags(request, queryset)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.remove_tags

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.remove_tags
```

````

`````
