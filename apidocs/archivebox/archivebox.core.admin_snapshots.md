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
* - {py:obj}`TagNameListFilter <archivebox.core.admin_snapshots.TagNameListFilter>`
  - ```{autodoc2-docstring} archivebox.core.admin_snapshots.TagNameListFilter
    :summary:
    ```
* - {py:obj}`SnapshotAdminForm <archivebox.core.admin_snapshots.SnapshotAdminForm>`
  - ```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdminForm
    :summary:
    ```
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

`````{py:class} SnapshotActionForm(*args, **kwargs)
:canonical: archivebox.core.admin_snapshots.SnapshotActionForm

Bases: {py:obj}`django.contrib.admin.helpers.ActionForm`

````{py:method} clean_tags()
:canonical: archivebox.core.admin_snapshots.SnapshotActionForm.clean_tags

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotActionForm.clean_tags
```

````

`````

`````{py:class} TagNameListFilter(request, params, model, model_admin)
:canonical: archivebox.core.admin_snapshots.TagNameListFilter

Bases: {py:obj}`django.contrib.admin.SimpleListFilter`

```{autodoc2-docstring} archivebox.core.admin_snapshots.TagNameListFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.core.admin_snapshots.TagNameListFilter.__init__
```

````{py:attribute} title
:canonical: archivebox.core.admin_snapshots.TagNameListFilter.title
:value: >
   'By tag name'

```{autodoc2-docstring} archivebox.core.admin_snapshots.TagNameListFilter.title
```

````

````{py:attribute} parameter_name
:canonical: archivebox.core.admin_snapshots.TagNameListFilter.parameter_name
:value: >
   'tag'

```{autodoc2-docstring} archivebox.core.admin_snapshots.TagNameListFilter.parameter_name
```

````

````{py:method} lookups(request, model_admin)
:canonical: archivebox.core.admin_snapshots.TagNameListFilter.lookups

````

````{py:method} queryset(request, queryset)
:canonical: archivebox.core.admin_snapshots.TagNameListFilter.queryset

````

`````

``````{py:class} SnapshotAdminForm(*args, **kwargs)
:canonical: archivebox.core.admin_snapshots.SnapshotAdminForm

Bases: {py:obj}`django.forms.ModelForm`

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdminForm
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdminForm.__init__
```

````{py:attribute} tags_editor
:canonical: archivebox.core.admin_snapshots.SnapshotAdminForm.tags_editor
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdminForm.tags_editor
```

````

`````{py:class} Meta
:canonical: archivebox.core.admin_snapshots.SnapshotAdminForm.Meta

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdminForm.Meta
```

````{py:attribute} model
:canonical: archivebox.core.admin_snapshots.SnapshotAdminForm.Meta.model
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdminForm.Meta.model
```

````

````{py:attribute} fields
:canonical: archivebox.core.admin_snapshots.SnapshotAdminForm.Meta.fields
:value: >
   '__all__'

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdminForm.Meta.fields
```

````

`````

````{py:method} save(commit=True)
:canonical: archivebox.core.admin_snapshots.SnapshotAdminForm.save

````

``````

`````{py:class} SnapshotAdmin(model, admin_site)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin

Bases: {py:obj}`archivebox.search.admin.SearchResultsAdminMixin`, {py:obj}`archivebox.base_models.admin.ConfigEditorMixin`, {py:obj}`archivebox.base_models.admin.BaseModelAdmin`

````{py:attribute} form
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.form
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.form
```

````

````{py:attribute} list_display
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.list_display
:value: >
   ('created_at', 'preview_icon', 'title_str', 'tags_inline', 'status_with_progress', 'files', 'size_wi...

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.list_display
```

````

````{py:attribute} sort_fields
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.sort_fields
:value: >
   ('title_str', 'created_at', 'status', 'crawl')

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.sort_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.readonly_fields
:value: >
   ('admin_actions', 'status_info', 'imported_timestamp', 'created_at', 'modified_at', 'downloaded_at',...

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.readonly_fields
```

````

````{py:attribute} search_fields
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.search_fields
:value: >
   ('id', 'url', 'timestamp', 'title', 'tags__name')

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.search_fields
```

````

````{py:attribute} list_filter
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.list_filter
:value: >
   ('created_at', 'downloaded_at', 'archiveresult__status', 'crawl__created_by')

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.list_filter
```

````

````{py:attribute} fieldsets
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.fieldsets
:value: >
   (('Actions',), ('URL',), ('Tags',), ('Status',), ('Timestamps',), ('Relations',), ('Config',), ('Fil...

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.fieldsets
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
   ['add_tags', 'remove_tags', 'resnapshot_snapshot', 'update_snapshots', 'overwrite_snapshots', 'delet...

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.actions
```

````

````{py:attribute} inlines
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.inlines
:value: >
   []

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

````{py:method} get_actions(request)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.get_actions

````

````{py:method} get_urls()
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.get_urls

````

````{py:method} get_queryset(request)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.get_queryset

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

````{py:method} archiveresults_list(obj)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.archiveresults_list

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.archiveresults_list
```

````

````{py:method} title_str(obj)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.title_str

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.title_str
```

````

````{py:method} tags_inline(obj)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.tags_inline

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.tags_inline
```

````

````{py:method} preview_icon(obj)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.preview_icon

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.preview_icon
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

````{py:method} status_with_progress(obj)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.status_with_progress

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.status_with_progress
```

````

````{py:method} size_with_stats(obj)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.size_with_stats

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.size_with_stats
```

````

````{py:method} _get_progress_stats(obj)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin._get_progress_stats

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin._get_progress_stats
```

````

````{py:method} _get_prefetched_results(obj)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin._get_prefetched_results

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin._get_prefetched_results
```

````

````{py:method} _get_ordering_fields(request)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin._get_ordering_fields

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin._get_ordering_fields
```

````

````{py:method} url_str(obj)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.url_str

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.url_str
```

````

````{py:method} health_display(obj)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.health_display

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.health_display
```

````

````{py:method} grid_view(request, extra_context=None)
:canonical: archivebox.core.admin_snapshots.SnapshotAdmin.grid_view

```{autodoc2-docstring} archivebox.core.admin_snapshots.SnapshotAdmin.grid_view
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
