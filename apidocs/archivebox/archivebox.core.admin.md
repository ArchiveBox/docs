# {py:mod}`archivebox.core.admin`

```{py:module} archivebox.core.admin
```

```{autodoc2-docstring} archivebox.core.admin
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ArchiveBoxAdmin <archivebox.core.admin.ArchiveBoxAdmin>`
  -
* - {py:obj}`CustomUserAdmin <archivebox.core.admin.CustomUserAdmin>`
  -
* - {py:obj}`CustomTaskModelAdmin <archivebox.core.admin.CustomTaskModelAdmin>`
  -
* - {py:obj}`AccelleratedPaginator <archivebox.core.admin.AccelleratedPaginator>`
  - ```{autodoc2-docstring} archivebox.core.admin.AccelleratedPaginator
    :summary:
    ```
* - {py:obj}`ArchiveResultInline <archivebox.core.admin.ArchiveResultInline>`
  -
* - {py:obj}`TagInline <archivebox.core.admin.TagInline>`
  -
* - {py:obj}`SnapshotActionForm <archivebox.core.admin.SnapshotActionForm>`
  -
* - {py:obj}`SnapshotAdmin <archivebox.core.admin.SnapshotAdmin>`
  -
* - {py:obj}`TagAdmin <archivebox.core.admin.TagAdmin>`
  -
* - {py:obj}`ArchiveResultAdmin <archivebox.core.admin.ArchiveResultAdmin>`
  -
* - {py:obj}`APITokenAdmin <archivebox.core.admin.APITokenAdmin>`
  -
* - {py:obj}`CustomWebhookAdmin <archivebox.core.admin.CustomWebhookAdmin>`
  -
* - {py:obj}`MachineAdmin <archivebox.core.admin.MachineAdmin>`
  -
* - {py:obj}`NetworkInterfaceAdmin <archivebox.core.admin.NetworkInterfaceAdmin>`
  -
* - {py:obj}`InstalledBinaryAdmin <archivebox.core.admin.InstalledBinaryAdmin>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`result_url <archivebox.core.admin.result_url>`
  - ```{autodoc2-docstring} archivebox.core.admin.result_url
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.core.admin.__package__>`
  - ```{autodoc2-docstring} archivebox.core.admin.__package__
    :summary:
    ```
* - {py:obj}`CONFIG <archivebox.core.admin.CONFIG>`
  - ```{autodoc2-docstring} archivebox.core.admin.CONFIG
    :summary:
    ```
* - {py:obj}`GLOBAL_CONTEXT <archivebox.core.admin.GLOBAL_CONTEXT>`
  - ```{autodoc2-docstring} archivebox.core.admin.GLOBAL_CONTEXT
    :summary:
    ```
* - {py:obj}`archivebox_admin <archivebox.core.admin.archivebox_admin>`
  - ```{autodoc2-docstring} archivebox.core.admin.archivebox_admin
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.core.admin.__package__
:value: >
   'archivebox.core'

```{autodoc2-docstring} archivebox.core.admin.__package__
```

````

````{py:data} CONFIG
:canonical: archivebox.core.admin.CONFIG
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin.CONFIG
```

````

````{py:data} GLOBAL_CONTEXT
:canonical: archivebox.core.admin.GLOBAL_CONTEXT
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin.GLOBAL_CONTEXT
```

````

`````{py:class} ArchiveBoxAdmin(name='admin')
:canonical: archivebox.core.admin.ArchiveBoxAdmin

Bases: {py:obj}`django.contrib.admin.AdminSite`

````{py:attribute} site_header
:canonical: archivebox.core.admin.ArchiveBoxAdmin.site_header
:value: >
   'ArchiveBox'

```{autodoc2-docstring} archivebox.core.admin.ArchiveBoxAdmin.site_header
```

````

````{py:attribute} index_title
:canonical: archivebox.core.admin.ArchiveBoxAdmin.index_title
:value: >
   'Links'

```{autodoc2-docstring} archivebox.core.admin.ArchiveBoxAdmin.index_title
```

````

````{py:attribute} site_title
:canonical: archivebox.core.admin.ArchiveBoxAdmin.site_title
:value: >
   'Index'

```{autodoc2-docstring} archivebox.core.admin.ArchiveBoxAdmin.site_title
```

````

````{py:attribute} namespace
:canonical: archivebox.core.admin.ArchiveBoxAdmin.namespace
:value: >
   'admin'

```{autodoc2-docstring} archivebox.core.admin.ArchiveBoxAdmin.namespace
```

````

`````

`````{py:class} CustomUserAdmin(model, admin_site)
:canonical: archivebox.core.admin.CustomUserAdmin

Bases: {py:obj}`django.contrib.auth.admin.UserAdmin`

````{py:attribute} sort_fields
:canonical: archivebox.core.admin.CustomUserAdmin.sort_fields
:value: >
   ['id', 'email', 'username', 'is_superuser', 'last_login', 'date_joined']

```{autodoc2-docstring} archivebox.core.admin.CustomUserAdmin.sort_fields
```

````

````{py:attribute} list_display
:canonical: archivebox.core.admin.CustomUserAdmin.list_display
:value: >
   ['username', 'id', 'email', 'is_superuser', 'last_login', 'date_joined']

```{autodoc2-docstring} archivebox.core.admin.CustomUserAdmin.list_display
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.core.admin.CustomUserAdmin.readonly_fields
:value: >
   ('snapshot_set', 'archiveresult_set', 'tag_set', 'apitoken_set', 'outboundwebhook_set')

```{autodoc2-docstring} archivebox.core.admin.CustomUserAdmin.readonly_fields
```

````

````{py:attribute} fieldsets
:canonical: archivebox.core.admin.CustomUserAdmin.fieldsets
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin.CustomUserAdmin.fieldsets
```

````

````{py:method} snapshot_set(obj)
:canonical: archivebox.core.admin.CustomUserAdmin.snapshot_set

```{autodoc2-docstring} archivebox.core.admin.CustomUserAdmin.snapshot_set
```

````

````{py:method} archiveresult_set(obj)
:canonical: archivebox.core.admin.CustomUserAdmin.archiveresult_set

```{autodoc2-docstring} archivebox.core.admin.CustomUserAdmin.archiveresult_set
```

````

````{py:method} tag_set(obj)
:canonical: archivebox.core.admin.CustomUserAdmin.tag_set

```{autodoc2-docstring} archivebox.core.admin.CustomUserAdmin.tag_set
```

````

````{py:method} apitoken_set(obj)
:canonical: archivebox.core.admin.CustomUserAdmin.apitoken_set

```{autodoc2-docstring} archivebox.core.admin.CustomUserAdmin.apitoken_set
```

````

````{py:method} outboundwebhook_set(obj)
:canonical: archivebox.core.admin.CustomUserAdmin.outboundwebhook_set

```{autodoc2-docstring} archivebox.core.admin.CustomUserAdmin.outboundwebhook_set
```

````

`````

````{py:data} archivebox_admin
:canonical: archivebox.core.admin.archivebox_admin
:value: >
   'ArchiveBoxAdmin(...)'

```{autodoc2-docstring} archivebox.core.admin.archivebox_admin
```

````

`````{py:class} CustomTaskModelAdmin(model, admin_site)
:canonical: archivebox.core.admin.CustomTaskModelAdmin

Bases: {py:obj}`huey_monitor.admin.TaskModelAdmin`

````{py:attribute} actions
:canonical: archivebox.core.admin.CustomTaskModelAdmin.actions
:value: >
   ['delete_selected']

```{autodoc2-docstring} archivebox.core.admin.CustomTaskModelAdmin.actions
```

````

````{py:method} has_delete_permission(request, obj=None)
:canonical: archivebox.core.admin.CustomTaskModelAdmin.has_delete_permission

````

`````

````{py:function} result_url(result: huey_monitor.admin.TaskModel) -> str
:canonical: archivebox.core.admin.result_url

```{autodoc2-docstring} archivebox.core.admin.result_url
```
````

`````{py:class} AccelleratedPaginator(object_list, per_page, orphans=0, allow_empty_first_page=True, error_messages=None)
:canonical: archivebox.core.admin.AccelleratedPaginator

Bases: {py:obj}`django.core.paginator.Paginator`

```{autodoc2-docstring} archivebox.core.admin.AccelleratedPaginator
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.core.admin.AccelleratedPaginator.__init__
```

````{py:method} count()
:canonical: archivebox.core.admin.AccelleratedPaginator.count

````

`````

`````{py:class} ArchiveResultInline(parent_model, admin_site)
:canonical: archivebox.core.admin.ArchiveResultInline

Bases: {py:obj}`django.contrib.admin.TabularInline`

````{py:attribute} name
:canonical: archivebox.core.admin.ArchiveResultInline.name
:value: >
   'Archive Results Log'

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultInline.name
```

````

````{py:attribute} model
:canonical: archivebox.core.admin.ArchiveResultInline.model
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultInline.model
```

````

````{py:attribute} parent_model
:canonical: archivebox.core.admin.ArchiveResultInline.parent_model
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultInline.parent_model
```

````

````{py:attribute} extra
:canonical: archivebox.core.admin.ArchiveResultInline.extra
:value: >
   0

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultInline.extra
```

````

````{py:attribute} sort_fields
:canonical: archivebox.core.admin.ArchiveResultInline.sort_fields
:value: >
   ('end_ts', 'extractor', 'output', 'status', 'cmd_version')

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultInline.sort_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.core.admin.ArchiveResultInline.readonly_fields
:value: >
   ('id', 'result_id', 'completed', 'command', 'version')

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultInline.readonly_fields
```

````

````{py:attribute} fields
:canonical: archivebox.core.admin.ArchiveResultInline.fields
:value: >
   ('start_ts', 'end_ts')

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultInline.fields
```

````

````{py:attribute} ordering
:canonical: archivebox.core.admin.ArchiveResultInline.ordering
:value: >
   ('end_ts',)

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultInline.ordering
```

````

````{py:attribute} show_change_link
:canonical: archivebox.core.admin.ArchiveResultInline.show_change_link
:value: >
   True

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultInline.show_change_link
```

````

````{py:method} get_parent_object_from_request(request)
:canonical: archivebox.core.admin.ArchiveResultInline.get_parent_object_from_request

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultInline.get_parent_object_from_request
```

````

````{py:method} completed(obj)
:canonical: archivebox.core.admin.ArchiveResultInline.completed

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultInline.completed
```

````

````{py:method} result_id(obj)
:canonical: archivebox.core.admin.ArchiveResultInline.result_id

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultInline.result_id
```

````

````{py:method} command(obj)
:canonical: archivebox.core.admin.ArchiveResultInline.command

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultInline.command
```

````

````{py:method} version(obj)
:canonical: archivebox.core.admin.ArchiveResultInline.version

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultInline.version
```

````

````{py:method} get_formset(request, obj=None, **kwargs)
:canonical: archivebox.core.admin.ArchiveResultInline.get_formset

````

````{py:method} get_readonly_fields(request, obj=None)
:canonical: archivebox.core.admin.ArchiveResultInline.get_readonly_fields

````

`````

`````{py:class} TagInline(parent_model, admin_site)
:canonical: archivebox.core.admin.TagInline

Bases: {py:obj}`django.contrib.admin.TabularInline`

````{py:attribute} model
:canonical: archivebox.core.admin.TagInline.model
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin.TagInline.model
```

````

````{py:attribute} fields
:canonical: archivebox.core.admin.TagInline.fields
:value: >
   ('id', 'tag')

```{autodoc2-docstring} archivebox.core.admin.TagInline.fields
```

````

````{py:attribute} extra
:canonical: archivebox.core.admin.TagInline.extra
:value: >
   1

```{autodoc2-docstring} archivebox.core.admin.TagInline.extra
```

````

````{py:attribute} max_num
:canonical: archivebox.core.admin.TagInline.max_num
:value: >
   1000

```{autodoc2-docstring} archivebox.core.admin.TagInline.max_num
```

````

````{py:attribute} autocomplete_fields
:canonical: archivebox.core.admin.TagInline.autocomplete_fields
:value: >
   ('tag',)

```{autodoc2-docstring} archivebox.core.admin.TagInline.autocomplete_fields
```

````

`````

`````{py:class} SnapshotActionForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, field_order=None, use_required_attribute=None, renderer=None)
:canonical: archivebox.core.admin.SnapshotActionForm

Bases: {py:obj}`django.contrib.admin.helpers.ActionForm`

````{py:attribute} tags
:canonical: archivebox.core.admin.SnapshotActionForm.tags
:value: >
   'ModelMultipleChoiceField(...)'

```{autodoc2-docstring} archivebox.core.admin.SnapshotActionForm.tags
```

````

`````

`````{py:class} SnapshotAdmin(model, admin_site)
:canonical: archivebox.core.admin.SnapshotAdmin

Bases: {py:obj}`core.mixins.SearchResultsAdminMixin`, {py:obj}`abid_utils.admin.ABIDModelAdmin`

````{py:attribute} list_display
:canonical: archivebox.core.admin.SnapshotAdmin.list_display
:value: >
   ('created_at', 'title_str', 'files', 'size', 'url_str')

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.list_display
```

````

````{py:attribute} sort_fields
:canonical: archivebox.core.admin.SnapshotAdmin.sort_fields
:value: >
   ('title_str', 'url_str', 'created_at')

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.sort_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.core.admin.SnapshotAdmin.readonly_fields
:value: >
   ('admin_actions', 'status_info', 'tags_str', 'imported_timestamp', 'created_at', 'modified_at', 'dow...

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.readonly_fields
```

````

````{py:attribute} search_fields
:canonical: archivebox.core.admin.SnapshotAdmin.search_fields
:value: >
   ('id', 'url', 'abid', 'timestamp', 'title', 'tags__name')

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.search_fields
```

````

````{py:attribute} list_filter
:canonical: archivebox.core.admin.SnapshotAdmin.list_filter
:value: >
   ('created_at', 'downloaded_at', 'archiveresult__status', 'created_by', 'tags__name')

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.list_filter
```

````

````{py:attribute} fields
:canonical: archivebox.core.admin.SnapshotAdmin.fields
:value: >
   ('url', 'title', 'created_by', 'bookmarked_at')

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.fields
```

````

````{py:attribute} ordering
:canonical: archivebox.core.admin.SnapshotAdmin.ordering
:value: >
   ['-created_at']

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.ordering
```

````

````{py:attribute} actions
:canonical: archivebox.core.admin.SnapshotAdmin.actions
:value: >
   ['add_tags', 'remove_tags', 'update_titles', 'update_snapshots', 'resnapshot_snapshot', 'overwrite_s...

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.actions
```

````

````{py:attribute} inlines
:canonical: archivebox.core.admin.SnapshotAdmin.inlines
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.inlines
```

````

````{py:attribute} list_per_page
:canonical: archivebox.core.admin.SnapshotAdmin.list_per_page
:value: >
   'min(...)'

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.list_per_page
```

````

````{py:attribute} action_form
:canonical: archivebox.core.admin.SnapshotAdmin.action_form
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.action_form
```

````

````{py:attribute} paginator
:canonical: archivebox.core.admin.SnapshotAdmin.paginator
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.paginator
```

````

````{py:attribute} save_on_top
:canonical: archivebox.core.admin.SnapshotAdmin.save_on_top
:value: >
   True

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.save_on_top
```

````

````{py:attribute} show_full_result_count
:canonical: archivebox.core.admin.SnapshotAdmin.show_full_result_count
:value: >
   False

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.show_full_result_count
```

````

````{py:method} changelist_view(request, extra_context=None)
:canonical: archivebox.core.admin.SnapshotAdmin.changelist_view

````

````{py:method} get_urls()
:canonical: archivebox.core.admin.SnapshotAdmin.get_urls

````

````{py:method} imported_timestamp(obj)
:canonical: archivebox.core.admin.SnapshotAdmin.imported_timestamp

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.imported_timestamp
```

````

````{py:method} admin_actions(obj)
:canonical: archivebox.core.admin.SnapshotAdmin.admin_actions

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.admin_actions
```

````

````{py:method} status_info(obj)
:canonical: archivebox.core.admin.SnapshotAdmin.status_info

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.status_info
```

````

````{py:method} title_str(obj)
:canonical: archivebox.core.admin.SnapshotAdmin.title_str

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.title_str
```

````

````{py:method} files(obj)
:canonical: archivebox.core.admin.SnapshotAdmin.files

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.files
```

````

````{py:method} size(obj)
:canonical: archivebox.core.admin.SnapshotAdmin.size

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.size
```

````

````{py:method} url_str(obj)
:canonical: archivebox.core.admin.SnapshotAdmin.url_str

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.url_str
```

````

````{py:method} grid_view(request, extra_context=None)
:canonical: archivebox.core.admin.SnapshotAdmin.grid_view

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.grid_view
```

````

````{py:method} update_titles(request, queryset)
:canonical: archivebox.core.admin.SnapshotAdmin.update_titles

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.update_titles
```

````

````{py:method} update_snapshots(request, queryset)
:canonical: archivebox.core.admin.SnapshotAdmin.update_snapshots

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.update_snapshots
```

````

````{py:method} resnapshot_snapshot(request, queryset)
:canonical: archivebox.core.admin.SnapshotAdmin.resnapshot_snapshot

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.resnapshot_snapshot
```

````

````{py:method} overwrite_snapshots(request, queryset)
:canonical: archivebox.core.admin.SnapshotAdmin.overwrite_snapshots

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.overwrite_snapshots
```

````

````{py:method} delete_snapshots(request, queryset)
:canonical: archivebox.core.admin.SnapshotAdmin.delete_snapshots

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.delete_snapshots
```

````

````{py:method} add_tags(request, queryset)
:canonical: archivebox.core.admin.SnapshotAdmin.add_tags

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.add_tags
```

````

````{py:method} remove_tags(request, queryset)
:canonical: archivebox.core.admin.SnapshotAdmin.remove_tags

```{autodoc2-docstring} archivebox.core.admin.SnapshotAdmin.remove_tags
```

````

`````

`````{py:class} TagAdmin(model, admin_site)
:canonical: archivebox.core.admin.TagAdmin

Bases: {py:obj}`abid_utils.admin.ABIDModelAdmin`

````{py:attribute} list_display
:canonical: archivebox.core.admin.TagAdmin.list_display
:value: >
   ('created_at', 'created_by', 'abid', 'name', 'num_snapshots', 'snapshots')

```{autodoc2-docstring} archivebox.core.admin.TagAdmin.list_display
```

````

````{py:attribute} list_filter
:canonical: archivebox.core.admin.TagAdmin.list_filter
:value: >
   ('created_at', 'created_by')

```{autodoc2-docstring} archivebox.core.admin.TagAdmin.list_filter
```

````

````{py:attribute} sort_fields
:canonical: archivebox.core.admin.TagAdmin.sort_fields
:value: >
   ('name', 'slug', 'abid', 'created_by', 'created_at')

```{autodoc2-docstring} archivebox.core.admin.TagAdmin.sort_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.core.admin.TagAdmin.readonly_fields
:value: >
   ('slug', 'abid', 'created_at', 'modified_at', 'abid_info', 'snapshots')

```{autodoc2-docstring} archivebox.core.admin.TagAdmin.readonly_fields
```

````

````{py:attribute} search_fields
:canonical: archivebox.core.admin.TagAdmin.search_fields
:value: >
   ('abid', 'name', 'slug')

```{autodoc2-docstring} archivebox.core.admin.TagAdmin.search_fields
```

````

````{py:attribute} fields
:canonical: archivebox.core.admin.TagAdmin.fields
:value: >
   ('name', 'created_by')

```{autodoc2-docstring} archivebox.core.admin.TagAdmin.fields
```

````

````{py:attribute} actions
:canonical: archivebox.core.admin.TagAdmin.actions
:value: >
   ['delete_selected']

```{autodoc2-docstring} archivebox.core.admin.TagAdmin.actions
```

````

````{py:attribute} ordering
:canonical: archivebox.core.admin.TagAdmin.ordering
:value: >
   ['-created_at']

```{autodoc2-docstring} archivebox.core.admin.TagAdmin.ordering
```

````

````{py:attribute} paginator
:canonical: archivebox.core.admin.TagAdmin.paginator
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin.TagAdmin.paginator
```

````

````{py:method} num_snapshots(tag)
:canonical: archivebox.core.admin.TagAdmin.num_snapshots

```{autodoc2-docstring} archivebox.core.admin.TagAdmin.num_snapshots
```

````

````{py:method} snapshots(tag)
:canonical: archivebox.core.admin.TagAdmin.snapshots

```{autodoc2-docstring} archivebox.core.admin.TagAdmin.snapshots
```

````

`````

``````{py:class} ArchiveResultAdmin(model, admin_site)
:canonical: archivebox.core.admin.ArchiveResultAdmin

Bases: {py:obj}`abid_utils.admin.ABIDModelAdmin`

````{py:attribute} list_display
:canonical: archivebox.core.admin.ArchiveResultAdmin.list_display
:value: >
   ('start_ts', 'snapshot_info', 'tags_str', 'extractor', 'cmd_str', 'status', 'output_str')

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultAdmin.list_display
```

````

````{py:attribute} sort_fields
:canonical: archivebox.core.admin.ArchiveResultAdmin.sort_fields
:value: >
   ('start_ts', 'extractor', 'status')

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultAdmin.sort_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.core.admin.ArchiveResultAdmin.readonly_fields
:value: >
   ('cmd_str', 'snapshot_info', 'tags_str', 'created_at', 'modified_at', 'abid_info', 'output_summary')

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultAdmin.readonly_fields
```

````

````{py:attribute} search_fields
:canonical: archivebox.core.admin.ArchiveResultAdmin.search_fields
:value: >
   ('id', 'abid', 'snapshot__url', 'extractor', 'output', 'cmd_version', 'cmd', 'snapshot__timestamp')

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultAdmin.search_fields
```

````

````{py:attribute} fields
:canonical: archivebox.core.admin.ArchiveResultAdmin.fields
:value: >
   ('snapshot', 'extractor', 'status', 'output', 'pwd', 'start_ts', 'end_ts', 'created_by', 'cmd_versio...

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultAdmin.fields
```

````

````{py:attribute} autocomplete_fields
:canonical: archivebox.core.admin.ArchiveResultAdmin.autocomplete_fields
:value: >
   ['snapshot']

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultAdmin.autocomplete_fields
```

````

````{py:attribute} list_filter
:canonical: archivebox.core.admin.ArchiveResultAdmin.list_filter
:value: >
   ('status', 'extractor', 'start_ts', 'cmd_version')

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultAdmin.list_filter
```

````

````{py:attribute} ordering
:canonical: archivebox.core.admin.ArchiveResultAdmin.ordering
:value: >
   ['-start_ts']

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultAdmin.ordering
```

````

````{py:attribute} list_per_page
:canonical: archivebox.core.admin.ArchiveResultAdmin.list_per_page
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultAdmin.list_per_page
```

````

````{py:attribute} paginator
:canonical: archivebox.core.admin.ArchiveResultAdmin.paginator
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultAdmin.paginator
```

````

````{py:attribute} save_on_top
:canonical: archivebox.core.admin.ArchiveResultAdmin.save_on_top
:value: >
   True

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultAdmin.save_on_top
```

````

````{py:attribute} actions
:canonical: archivebox.core.admin.ArchiveResultAdmin.actions
:value: >
   ['delete_selected']

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultAdmin.actions
```

````

`````{py:class} Meta
:canonical: archivebox.core.admin.ArchiveResultAdmin.Meta

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultAdmin.Meta
```

````{py:attribute} verbose_name
:canonical: archivebox.core.admin.ArchiveResultAdmin.Meta.verbose_name
:value: >
   'Archive Result'

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultAdmin.Meta.verbose_name
```

````

````{py:attribute} verbose_name_plural
:canonical: archivebox.core.admin.ArchiveResultAdmin.Meta.verbose_name_plural
:value: >
   'Archive Results'

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultAdmin.Meta.verbose_name_plural
```

````

`````

````{py:method} change_view(request, object_id, form_url='', extra_context=None)
:canonical: archivebox.core.admin.ArchiveResultAdmin.change_view

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultAdmin.change_view
```

````

````{py:method} snapshot_info(result)
:canonical: archivebox.core.admin.ArchiveResultAdmin.snapshot_info

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultAdmin.snapshot_info
```

````

````{py:method} tags_str(result)
:canonical: archivebox.core.admin.ArchiveResultAdmin.tags_str

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultAdmin.tags_str
```

````

````{py:method} cmd_str(result)
:canonical: archivebox.core.admin.ArchiveResultAdmin.cmd_str

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultAdmin.cmd_str
```

````

````{py:method} output_str(result)
:canonical: archivebox.core.admin.ArchiveResultAdmin.output_str

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultAdmin.output_str
```

````

````{py:method} output_summary(result)
:canonical: archivebox.core.admin.ArchiveResultAdmin.output_summary

```{autodoc2-docstring} archivebox.core.admin.ArchiveResultAdmin.output_summary
```

````

``````

`````{py:class} APITokenAdmin(model, admin_site)
:canonical: archivebox.core.admin.APITokenAdmin

Bases: {py:obj}`abid_utils.admin.ABIDModelAdmin`

````{py:attribute} list_display
:canonical: archivebox.core.admin.APITokenAdmin.list_display
:value: >
   ('created_at', 'abid', 'created_by', 'token_redacted', 'expires')

```{autodoc2-docstring} archivebox.core.admin.APITokenAdmin.list_display
```

````

````{py:attribute} sort_fields
:canonical: archivebox.core.admin.APITokenAdmin.sort_fields
:value: >
   ('abid', 'created_at', 'created_by', 'expires')

```{autodoc2-docstring} archivebox.core.admin.APITokenAdmin.sort_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.core.admin.APITokenAdmin.readonly_fields
:value: >
   ('created_at', 'modified_at', 'abid_info')

```{autodoc2-docstring} archivebox.core.admin.APITokenAdmin.readonly_fields
```

````

````{py:attribute} search_fields
:canonical: archivebox.core.admin.APITokenAdmin.search_fields
:value: >
   ('id', 'abid', 'created_by__username', 'token')

```{autodoc2-docstring} archivebox.core.admin.APITokenAdmin.search_fields
```

````

````{py:attribute} fields
:canonical: archivebox.core.admin.APITokenAdmin.fields
:value: >
   ('created_by', 'token', 'expires')

```{autodoc2-docstring} archivebox.core.admin.APITokenAdmin.fields
```

````

````{py:attribute} list_filter
:canonical: archivebox.core.admin.APITokenAdmin.list_filter
:value: >
   ('created_by',)

```{autodoc2-docstring} archivebox.core.admin.APITokenAdmin.list_filter
```

````

````{py:attribute} ordering
:canonical: archivebox.core.admin.APITokenAdmin.ordering
:value: >
   ['-created_at']

```{autodoc2-docstring} archivebox.core.admin.APITokenAdmin.ordering
```

````

````{py:attribute} list_per_page
:canonical: archivebox.core.admin.APITokenAdmin.list_per_page
:value: >
   100

```{autodoc2-docstring} archivebox.core.admin.APITokenAdmin.list_per_page
```

````

`````

`````{py:class} CustomWebhookAdmin(model, admin_site)
:canonical: archivebox.core.admin.CustomWebhookAdmin

Bases: {py:obj}`signal_webhooks.admin.WebhookAdmin`, {py:obj}`abid_utils.admin.ABIDModelAdmin`

````{py:attribute} list_display
:canonical: archivebox.core.admin.CustomWebhookAdmin.list_display
:value: >
   ('created_at', 'created_by', 'abid')

```{autodoc2-docstring} archivebox.core.admin.CustomWebhookAdmin.list_display
```

````

````{py:attribute} sort_fields
:canonical: archivebox.core.admin.CustomWebhookAdmin.sort_fields
:value: >
   ('created_at', 'created_by', 'abid', 'referenced_model', 'endpoint', 'last_success', 'last_error')

```{autodoc2-docstring} archivebox.core.admin.CustomWebhookAdmin.sort_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.core.admin.CustomWebhookAdmin.readonly_fields
:value: >
   ('created_at', 'modified_at', 'abid_info')

```{autodoc2-docstring} archivebox.core.admin.CustomWebhookAdmin.readonly_fields
```

````

`````

`````{py:class} MachineAdmin(model, admin_site)
:canonical: archivebox.core.admin.MachineAdmin

Bases: {py:obj}`abid_utils.admin.ABIDModelAdmin`

````{py:attribute} list_display
:canonical: archivebox.core.admin.MachineAdmin.list_display
:value: >
   ('abid', 'created_at', 'hostname', 'ips', 'os_platform', 'hw_in_docker', 'hw_in_vm', 'hw_manufacture...

```{autodoc2-docstring} archivebox.core.admin.MachineAdmin.list_display
```

````

````{py:attribute} sort_fields
:canonical: archivebox.core.admin.MachineAdmin.sort_fields
:value: >
   ('abid', 'created_at', 'hostname', 'ips', 'os_platform', 'hw_in_docker', 'hw_in_vm', 'hw_manufacture...

```{autodoc2-docstring} archivebox.core.admin.MachineAdmin.sort_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.core.admin.MachineAdmin.readonly_fields
:value: >
   ('guid', 'created_at', 'modified_at', 'abid_info', 'ips')

```{autodoc2-docstring} archivebox.core.admin.MachineAdmin.readonly_fields
```

````

````{py:attribute} fields
:canonical: archivebox.core.admin.MachineAdmin.fields
:value: >
   ()

```{autodoc2-docstring} archivebox.core.admin.MachineAdmin.fields
```

````

````{py:attribute} list_filter
:canonical: archivebox.core.admin.MachineAdmin.list_filter
:value: >
   ('hw_in_docker', 'hw_in_vm', 'os_arch', 'os_family', 'os_platform')

```{autodoc2-docstring} archivebox.core.admin.MachineAdmin.list_filter
```

````

````{py:attribute} ordering
:canonical: archivebox.core.admin.MachineAdmin.ordering
:value: >
   ['-created_at']

```{autodoc2-docstring} archivebox.core.admin.MachineAdmin.ordering
```

````

````{py:attribute} list_per_page
:canonical: archivebox.core.admin.MachineAdmin.list_per_page
:value: >
   100

```{autodoc2-docstring} archivebox.core.admin.MachineAdmin.list_per_page
```

````

````{py:attribute} actions
:canonical: archivebox.core.admin.MachineAdmin.actions
:value: >
   ['delete_selected']

```{autodoc2-docstring} archivebox.core.admin.MachineAdmin.actions
```

````

````{py:method} ips(machine)
:canonical: archivebox.core.admin.MachineAdmin.ips

```{autodoc2-docstring} archivebox.core.admin.MachineAdmin.ips
```

````

`````

`````{py:class} NetworkInterfaceAdmin(model, admin_site)
:canonical: archivebox.core.admin.NetworkInterfaceAdmin

Bases: {py:obj}`abid_utils.admin.ABIDModelAdmin`

````{py:attribute} list_display
:canonical: archivebox.core.admin.NetworkInterfaceAdmin.list_display
:value: >
   ('abid', 'created_at', 'machine_info', 'ip_public', 'dns_server', 'isp', 'country', 'region', 'city'...

```{autodoc2-docstring} archivebox.core.admin.NetworkInterfaceAdmin.list_display
```

````

````{py:attribute} sort_fields
:canonical: archivebox.core.admin.NetworkInterfaceAdmin.sort_fields
:value: >
   ('abid', 'created_at', 'machine_info', 'ip_public', 'dns_server', 'isp', 'country', 'region', 'city'...

```{autodoc2-docstring} archivebox.core.admin.NetworkInterfaceAdmin.sort_fields
```

````

````{py:attribute} search_fields
:canonical: archivebox.core.admin.NetworkInterfaceAdmin.search_fields
:value: >
   ('abid', 'machine__abid', 'iface', 'ip_public', 'ip_local', 'mac_address', 'dns_server', 'hostname',...

```{autodoc2-docstring} archivebox.core.admin.NetworkInterfaceAdmin.search_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.core.admin.NetworkInterfaceAdmin.readonly_fields
:value: >
   ('machine', 'created_at', 'modified_at', 'abid_info', 'mac_address', 'ip_public', 'ip_local', 'dns_s...

```{autodoc2-docstring} archivebox.core.admin.NetworkInterfaceAdmin.readonly_fields
```

````

````{py:attribute} fields
:canonical: archivebox.core.admin.NetworkInterfaceAdmin.fields
:value: >
   ()

```{autodoc2-docstring} archivebox.core.admin.NetworkInterfaceAdmin.fields
```

````

````{py:attribute} list_filter
:canonical: archivebox.core.admin.NetworkInterfaceAdmin.list_filter
:value: >
   ('isp', 'country', 'region')

```{autodoc2-docstring} archivebox.core.admin.NetworkInterfaceAdmin.list_filter
```

````

````{py:attribute} ordering
:canonical: archivebox.core.admin.NetworkInterfaceAdmin.ordering
:value: >
   ['-created_at']

```{autodoc2-docstring} archivebox.core.admin.NetworkInterfaceAdmin.ordering
```

````

````{py:attribute} list_per_page
:canonical: archivebox.core.admin.NetworkInterfaceAdmin.list_per_page
:value: >
   100

```{autodoc2-docstring} archivebox.core.admin.NetworkInterfaceAdmin.list_per_page
```

````

````{py:attribute} actions
:canonical: archivebox.core.admin.NetworkInterfaceAdmin.actions
:value: >
   ['delete_selected']

```{autodoc2-docstring} archivebox.core.admin.NetworkInterfaceAdmin.actions
```

````

````{py:method} machine_info(iface)
:canonical: archivebox.core.admin.NetworkInterfaceAdmin.machine_info

```{autodoc2-docstring} archivebox.core.admin.NetworkInterfaceAdmin.machine_info
```

````

`````

`````{py:class} InstalledBinaryAdmin(model, admin_site)
:canonical: archivebox.core.admin.InstalledBinaryAdmin

Bases: {py:obj}`abid_utils.admin.ABIDModelAdmin`

````{py:attribute} list_display
:canonical: archivebox.core.admin.InstalledBinaryAdmin.list_display
:value: >
   ('abid', 'created_at', 'machine_info', 'name', 'binprovider', 'version', 'abspath', 'sha256', 'healt...

```{autodoc2-docstring} archivebox.core.admin.InstalledBinaryAdmin.list_display
```

````

````{py:attribute} sort_fields
:canonical: archivebox.core.admin.InstalledBinaryAdmin.sort_fields
:value: >
   ('abid', 'created_at', 'machine_info', 'name', 'binprovider', 'version', 'abspath', 'sha256')

```{autodoc2-docstring} archivebox.core.admin.InstalledBinaryAdmin.sort_fields
```

````

````{py:attribute} search_fields
:canonical: archivebox.core.admin.InstalledBinaryAdmin.search_fields
:value: >
   ('abid', 'machine__abid', 'name', 'binprovider', 'version', 'abspath', 'sha256')

```{autodoc2-docstring} archivebox.core.admin.InstalledBinaryAdmin.search_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.core.admin.InstalledBinaryAdmin.readonly_fields
:value: >
   ('created_at', 'modified_at', 'abid_info')

```{autodoc2-docstring} archivebox.core.admin.InstalledBinaryAdmin.readonly_fields
```

````

````{py:attribute} fields
:canonical: archivebox.core.admin.InstalledBinaryAdmin.fields
:value: >
   ('machine', 'name', 'binprovider', 'abspath', 'version', 'sha256')

```{autodoc2-docstring} archivebox.core.admin.InstalledBinaryAdmin.fields
```

````

````{py:attribute} list_filter
:canonical: archivebox.core.admin.InstalledBinaryAdmin.list_filter
:value: >
   ('name', 'binprovider', 'machine_id')

```{autodoc2-docstring} archivebox.core.admin.InstalledBinaryAdmin.list_filter
```

````

````{py:attribute} ordering
:canonical: archivebox.core.admin.InstalledBinaryAdmin.ordering
:value: >
   ['-created_at']

```{autodoc2-docstring} archivebox.core.admin.InstalledBinaryAdmin.ordering
```

````

````{py:attribute} list_per_page
:canonical: archivebox.core.admin.InstalledBinaryAdmin.list_per_page
:value: >
   100

```{autodoc2-docstring} archivebox.core.admin.InstalledBinaryAdmin.list_per_page
```

````

````{py:attribute} actions
:canonical: archivebox.core.admin.InstalledBinaryAdmin.actions
:value: >
   ['delete_selected']

```{autodoc2-docstring} archivebox.core.admin.InstalledBinaryAdmin.actions
```

````

````{py:method} machine_info(installed_binary)
:canonical: archivebox.core.admin.InstalledBinaryAdmin.machine_info

```{autodoc2-docstring} archivebox.core.admin.InstalledBinaryAdmin.machine_info
```

````

`````
