# {py:mod}`archivebox.core.admin_archiveresults`

```{py:module} archivebox.core.admin_archiveresults
```

```{autodoc2-docstring} archivebox.core.admin_archiveresults
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ArchiveResultInline <archivebox.core.admin_archiveresults.ArchiveResultInline>`
  -
* - {py:obj}`ArchiveResultAdmin <archivebox.core.admin_archiveresults.ArchiveResultAdmin>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`result_url <archivebox.core.admin_archiveresults.result_url>`
  - ```{autodoc2-docstring} archivebox.core.admin_archiveresults.result_url
    :summary:
    ```
* - {py:obj}`register_admin <archivebox.core.admin_archiveresults.register_admin>`
  - ```{autodoc2-docstring} archivebox.core.admin_archiveresults.register_admin
    :summary:
    ```
````

### API

````{py:function} result_url(result: huey_monitor.admin.TaskModel) -> str
:canonical: archivebox.core.admin_archiveresults.result_url

```{autodoc2-docstring} archivebox.core.admin_archiveresults.result_url
```
````

`````{py:class} ArchiveResultInline(parent_model, admin_site)
:canonical: archivebox.core.admin_archiveresults.ArchiveResultInline

Bases: {py:obj}`django.contrib.admin.TabularInline`

````{py:attribute} name
:canonical: archivebox.core.admin_archiveresults.ArchiveResultInline.name
:value: >
   'Archive Results Log'

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultInline.name
```

````

````{py:attribute} model
:canonical: archivebox.core.admin_archiveresults.ArchiveResultInline.model
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultInline.model
```

````

````{py:attribute} parent_model
:canonical: archivebox.core.admin_archiveresults.ArchiveResultInline.parent_model
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultInline.parent_model
```

````

````{py:attribute} extra
:canonical: archivebox.core.admin_archiveresults.ArchiveResultInline.extra
:value: >
   0

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultInline.extra
```

````

````{py:attribute} sort_fields
:canonical: archivebox.core.admin_archiveresults.ArchiveResultInline.sort_fields
:value: >
   ('end_ts', 'extractor', 'output', 'status', 'cmd_version')

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultInline.sort_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.core.admin_archiveresults.ArchiveResultInline.readonly_fields
:value: >
   ('id', 'result_id', 'completed', 'command', 'version')

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultInline.readonly_fields
```

````

````{py:attribute} fields
:canonical: archivebox.core.admin_archiveresults.ArchiveResultInline.fields
:value: >
   ('start_ts', 'end_ts')

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultInline.fields
```

````

````{py:attribute} ordering
:canonical: archivebox.core.admin_archiveresults.ArchiveResultInline.ordering
:value: >
   ('end_ts',)

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultInline.ordering
```

````

````{py:attribute} show_change_link
:canonical: archivebox.core.admin_archiveresults.ArchiveResultInline.show_change_link
:value: >
   True

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultInline.show_change_link
```

````

````{py:method} get_parent_object_from_request(request)
:canonical: archivebox.core.admin_archiveresults.ArchiveResultInline.get_parent_object_from_request

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultInline.get_parent_object_from_request
```

````

````{py:method} completed(obj)
:canonical: archivebox.core.admin_archiveresults.ArchiveResultInline.completed

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultInline.completed
```

````

````{py:method} result_id(obj)
:canonical: archivebox.core.admin_archiveresults.ArchiveResultInline.result_id

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultInline.result_id
```

````

````{py:method} command(obj)
:canonical: archivebox.core.admin_archiveresults.ArchiveResultInline.command

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultInline.command
```

````

````{py:method} version(obj)
:canonical: archivebox.core.admin_archiveresults.ArchiveResultInline.version

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultInline.version
```

````

````{py:method} get_formset(request, obj=None, **kwargs)
:canonical: archivebox.core.admin_archiveresults.ArchiveResultInline.get_formset

````

````{py:method} get_readonly_fields(request, obj=None)
:canonical: archivebox.core.admin_archiveresults.ArchiveResultInline.get_readonly_fields

````

`````

``````{py:class} ArchiveResultAdmin(model, admin_site)
:canonical: archivebox.core.admin_archiveresults.ArchiveResultAdmin

Bases: {py:obj}`abid_utils.admin.ABIDModelAdmin`

````{py:attribute} list_display
:canonical: archivebox.core.admin_archiveresults.ArchiveResultAdmin.list_display
:value: >
   ('abid', 'created_by', 'created_at', 'snapshot_info', 'tags_str', 'status', 'extractor', 'cmd_str', ...

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultAdmin.list_display
```

````

````{py:attribute} sort_fields
:canonical: archivebox.core.admin_archiveresults.ArchiveResultAdmin.sort_fields
:value: >
   ('abid', 'created_by', 'created_at', 'extractor', 'status')

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultAdmin.sort_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.core.admin_archiveresults.ArchiveResultAdmin.readonly_fields
:value: >
   ('cmd_str', 'snapshot_info', 'tags_str', 'created_at', 'modified_at', 'abid_info', 'output_summary')

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultAdmin.readonly_fields
```

````

````{py:attribute} search_fields
:canonical: archivebox.core.admin_archiveresults.ArchiveResultAdmin.search_fields
:value: >
   ('id', 'abid', 'snapshot__url', 'extractor', 'output', 'cmd_version', 'cmd', 'snapshot__timestamp')

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultAdmin.search_fields
```

````

````{py:attribute} fields
:canonical: archivebox.core.admin_archiveresults.ArchiveResultAdmin.fields
:value: >
   ('snapshot', 'extractor', 'status', 'retry_at', 'start_ts', 'end_ts', 'created_by', 'pwd', 'cmd_vers...

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultAdmin.fields
```

````

````{py:attribute} autocomplete_fields
:canonical: archivebox.core.admin_archiveresults.ArchiveResultAdmin.autocomplete_fields
:value: >
   ['snapshot']

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultAdmin.autocomplete_fields
```

````

````{py:attribute} list_filter
:canonical: archivebox.core.admin_archiveresults.ArchiveResultAdmin.list_filter
:value: >
   ('status', 'extractor', 'start_ts', 'cmd_version')

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultAdmin.list_filter
```

````

````{py:attribute} ordering
:canonical: archivebox.core.admin_archiveresults.ArchiveResultAdmin.ordering
:value: >
   ['-start_ts']

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultAdmin.ordering
```

````

````{py:attribute} list_per_page
:canonical: archivebox.core.admin_archiveresults.ArchiveResultAdmin.list_per_page
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultAdmin.list_per_page
```

````

````{py:attribute} paginator
:canonical: archivebox.core.admin_archiveresults.ArchiveResultAdmin.paginator
:value: >
   None

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultAdmin.paginator
```

````

````{py:attribute} save_on_top
:canonical: archivebox.core.admin_archiveresults.ArchiveResultAdmin.save_on_top
:value: >
   True

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultAdmin.save_on_top
```

````

````{py:attribute} actions
:canonical: archivebox.core.admin_archiveresults.ArchiveResultAdmin.actions
:value: >
   ['delete_selected']

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultAdmin.actions
```

````

`````{py:class} Meta
:canonical: archivebox.core.admin_archiveresults.ArchiveResultAdmin.Meta

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultAdmin.Meta
```

````{py:attribute} verbose_name
:canonical: archivebox.core.admin_archiveresults.ArchiveResultAdmin.Meta.verbose_name
:value: >
   'Archive Result'

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultAdmin.Meta.verbose_name
```

````

````{py:attribute} verbose_name_plural
:canonical: archivebox.core.admin_archiveresults.ArchiveResultAdmin.Meta.verbose_name_plural
:value: >
   'Archive Results'

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultAdmin.Meta.verbose_name_plural
```

````

`````

````{py:method} change_view(request, object_id, form_url='', extra_context=None)
:canonical: archivebox.core.admin_archiveresults.ArchiveResultAdmin.change_view

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultAdmin.change_view
```

````

````{py:method} snapshot_info(result)
:canonical: archivebox.core.admin_archiveresults.ArchiveResultAdmin.snapshot_info

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultAdmin.snapshot_info
```

````

````{py:method} tags_str(result)
:canonical: archivebox.core.admin_archiveresults.ArchiveResultAdmin.tags_str

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultAdmin.tags_str
```

````

````{py:method} cmd_str(result)
:canonical: archivebox.core.admin_archiveresults.ArchiveResultAdmin.cmd_str

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultAdmin.cmd_str
```

````

````{py:method} output_str(result)
:canonical: archivebox.core.admin_archiveresults.ArchiveResultAdmin.output_str

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultAdmin.output_str
```

````

````{py:method} output_summary(result)
:canonical: archivebox.core.admin_archiveresults.ArchiveResultAdmin.output_summary

```{autodoc2-docstring} archivebox.core.admin_archiveresults.ArchiveResultAdmin.output_summary
```

````

``````

````{py:function} register_admin(admin_site)
:canonical: archivebox.core.admin_archiveresults.register_admin

```{autodoc2-docstring} archivebox.core.admin_archiveresults.register_admin
```
````
