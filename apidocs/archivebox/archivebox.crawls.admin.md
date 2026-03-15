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

* - {py:obj}`CrawlAdminForm <archivebox.crawls.admin.CrawlAdminForm>`
  - ```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdminForm
    :summary:
    ```
* - {py:obj}`CrawlAdmin <archivebox.crawls.admin.CrawlAdmin>`
  -
* - {py:obj}`CrawlScheduleAdmin <archivebox.crawls.admin.CrawlScheduleAdmin>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`render_snapshots_list <archivebox.crawls.admin.render_snapshots_list>`
  - ```{autodoc2-docstring} archivebox.crawls.admin.render_snapshots_list
    :summary:
    ```
* - {py:obj}`register_admin <archivebox.crawls.admin.register_admin>`
  - ```{autodoc2-docstring} archivebox.crawls.admin.register_admin
    :summary:
    ```
````

### API

````{py:function} render_snapshots_list(snapshots_qs, limit=20)
:canonical: archivebox.crawls.admin.render_snapshots_list

```{autodoc2-docstring} archivebox.crawls.admin.render_snapshots_list
```
````

``````{py:class} CrawlAdminForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)
:canonical: archivebox.crawls.admin.CrawlAdminForm

Bases: {py:obj}`django.forms.ModelForm`

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdminForm
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdminForm.__init__
```

`````{py:class} Meta
:canonical: archivebox.crawls.admin.CrawlAdminForm.Meta

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdminForm.Meta
```

````{py:attribute} model
:canonical: archivebox.crawls.admin.CrawlAdminForm.Meta.model
:value: >
   None

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdminForm.Meta.model
```

````

````{py:attribute} fields
:canonical: archivebox.crawls.admin.CrawlAdminForm.Meta.fields
:value: >
   '__all__'

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdminForm.Meta.fields
```

````

````{py:attribute} widgets
:canonical: archivebox.crawls.admin.CrawlAdminForm.Meta.widgets
:value: >
   None

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdminForm.Meta.widgets
```

````

`````

``````

`````{py:class} CrawlAdmin(model, admin_site)
:canonical: archivebox.crawls.admin.CrawlAdmin

Bases: {py:obj}`archivebox.base_models.admin.ConfigEditorMixin`, {py:obj}`archivebox.base_models.admin.BaseModelAdmin`

````{py:attribute} form
:canonical: archivebox.crawls.admin.CrawlAdmin.form
:value: >
   None

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.form
```

````

````{py:attribute} list_display
:canonical: archivebox.crawls.admin.CrawlAdmin.list_display
:value: >
   ('id', 'created_at', 'created_by', 'max_depth', 'label', 'notes', 'urls_preview', 'schedule_str', 's...

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.list_display
```

````

````{py:attribute} sort_fields
:canonical: archivebox.crawls.admin.CrawlAdmin.sort_fields
:value: >
   ('id', 'created_at', 'created_by', 'max_depth', 'label', 'notes', 'schedule_str', 'status', 'retry_a...

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.sort_fields
```

````

````{py:attribute} search_fields
:canonical: archivebox.crawls.admin.CrawlAdmin.search_fields
:value: >
   ('id', 'created_by__username', 'max_depth', 'label', 'notes', 'schedule_id', 'status', 'urls')

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.search_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.crawls.admin.CrawlAdmin.readonly_fields
:value: >
   ('created_at', 'modified_at', 'snapshots')

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.readonly_fields
```

````

````{py:attribute} fieldsets
:canonical: archivebox.crawls.admin.CrawlAdmin.fieldsets
:value: >
   (('URLs',), ('Info',), ('Settings',), ('Status',), ('Relations',), ('Timestamps',), ('Snapshots',))

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.fieldsets
```

````

````{py:attribute} list_filter
:canonical: archivebox.crawls.admin.CrawlAdmin.list_filter
:value: >
   ('max_depth', 'schedule', 'created_by', 'status', 'retry_at')

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
   ['delete_selected_batched']

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.actions
```

````

````{py:attribute} change_actions
:canonical: archivebox.crawls.admin.CrawlAdmin.change_actions
:value: >
   ['recrawl']

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.change_actions
```

````

````{py:method} get_queryset(request)
:canonical: archivebox.crawls.admin.CrawlAdmin.get_queryset

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.get_queryset
```

````

````{py:method} delete_selected_batched(request, queryset)
:canonical: archivebox.crawls.admin.CrawlAdmin.delete_selected_batched

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.delete_selected_batched
```

````

````{py:method} recrawl(request, obj)
:canonical: archivebox.crawls.admin.CrawlAdmin.recrawl

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.recrawl
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

````{py:method} urls_preview(obj)
:canonical: archivebox.crawls.admin.CrawlAdmin.urls_preview

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.urls_preview
```

````

````{py:method} health_display(obj)
:canonical: archivebox.crawls.admin.CrawlAdmin.health_display

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.health_display
```

````

````{py:method} urls_editor(obj)
:canonical: archivebox.crawls.admin.CrawlAdmin.urls_editor

```{autodoc2-docstring} archivebox.crawls.admin.CrawlAdmin.urls_editor
```

````

`````

`````{py:class} CrawlScheduleAdmin(model, admin_site)
:canonical: archivebox.crawls.admin.CrawlScheduleAdmin

Bases: {py:obj}`archivebox.base_models.admin.BaseModelAdmin`

````{py:attribute} list_display
:canonical: archivebox.crawls.admin.CrawlScheduleAdmin.list_display
:value: >
   ('id', 'created_at', 'created_by', 'label', 'notes', 'template_str', 'crawls', 'num_crawls', 'num_sn...

```{autodoc2-docstring} archivebox.crawls.admin.CrawlScheduleAdmin.list_display
```

````

````{py:attribute} sort_fields
:canonical: archivebox.crawls.admin.CrawlScheduleAdmin.sort_fields
:value: >
   ('id', 'created_at', 'created_by', 'label', 'notes', 'template_str')

```{autodoc2-docstring} archivebox.crawls.admin.CrawlScheduleAdmin.sort_fields
```

````

````{py:attribute} search_fields
:canonical: archivebox.crawls.admin.CrawlScheduleAdmin.search_fields
:value: >
   ('id', 'created_by__username', 'label', 'notes', 'schedule_id', 'template_id', 'template__urls')

```{autodoc2-docstring} archivebox.crawls.admin.CrawlScheduleAdmin.search_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.crawls.admin.CrawlScheduleAdmin.readonly_fields
:value: >
   ('created_at', 'modified_at', 'crawls', 'snapshots')

```{autodoc2-docstring} archivebox.crawls.admin.CrawlScheduleAdmin.readonly_fields
```

````

````{py:attribute} fieldsets
:canonical: archivebox.crawls.admin.CrawlScheduleAdmin.fieldsets
:value: >
   (('Schedule Info',), ('Configuration',), ('Metadata',), ('Crawls',), ('Snapshots',))

```{autodoc2-docstring} archivebox.crawls.admin.CrawlScheduleAdmin.fieldsets
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
