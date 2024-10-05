# {py:mod}`archivebox.abid_utils.admin`

```{py:module} archivebox.abid_utils.admin
```

```{autodoc2-docstring} archivebox.abid_utils.admin
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ABIDModelAdmin <archivebox.abid_utils.admin.ABIDModelAdmin>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`highlight_diff <archivebox.abid_utils.admin.highlight_diff>`
  - ```{autodoc2-docstring} archivebox.abid_utils.admin.highlight_diff
    :summary:
    ```
* - {py:obj}`get_abid_info <archivebox.abid_utils.admin.get_abid_info>`
  - ```{autodoc2-docstring} archivebox.abid_utils.admin.get_abid_info
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.abid_utils.admin.__package__>`
  - ```{autodoc2-docstring} archivebox.abid_utils.admin.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.abid_utils.admin.__package__
:value: >
   'archivebox.abid_utils'

```{autodoc2-docstring} archivebox.abid_utils.admin.__package__
```

````

````{py:function} highlight_diff(display_val: typing.Any, compare_val: typing.Any, invert: bool = False, color_same: str | None = None, color_diff: str | None = None)
:canonical: archivebox.abid_utils.admin.highlight_diff

```{autodoc2-docstring} archivebox.abid_utils.admin.highlight_diff
```
````

````{py:function} get_abid_info(self, obj, request=None)
:canonical: archivebox.abid_utils.admin.get_abid_info

```{autodoc2-docstring} archivebox.abid_utils.admin.get_abid_info
```
````

`````{py:class} ABIDModelAdmin(model, admin_site)
:canonical: archivebox.abid_utils.admin.ABIDModelAdmin

Bases: {py:obj}`django_object_actions.DjangoObjectActions`, {py:obj}`django.contrib.admin.ModelAdmin`

````{py:attribute} list_display
:canonical: archivebox.abid_utils.admin.ABIDModelAdmin.list_display
:value: >
   ('created_at', 'created_by', 'abid')

```{autodoc2-docstring} archivebox.abid_utils.admin.ABIDModelAdmin.list_display
```

````

````{py:attribute} sort_fields
:canonical: archivebox.abid_utils.admin.ABIDModelAdmin.sort_fields
:value: >
   ('created_at', 'created_by', 'abid')

```{autodoc2-docstring} archivebox.abid_utils.admin.ABIDModelAdmin.sort_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.abid_utils.admin.ABIDModelAdmin.readonly_fields
:value: >
   ('created_at', 'modified_at', 'abid_info')

```{autodoc2-docstring} archivebox.abid_utils.admin.ABIDModelAdmin.readonly_fields
```

````

````{py:attribute} change_actions
:canonical: archivebox.abid_utils.admin.ABIDModelAdmin.change_actions
:value: >
   ('regenerate_abid',)

```{autodoc2-docstring} archivebox.abid_utils.admin.ABIDModelAdmin.change_actions
```

````

````{py:method} _get_obj_does_not_exist_redirect(request, opts, object_id)
:canonical: archivebox.abid_utils.admin.ABIDModelAdmin._get_obj_does_not_exist_redirect

````

````{py:method} queryset(request)
:canonical: archivebox.abid_utils.admin.ABIDModelAdmin.queryset

```{autodoc2-docstring} archivebox.abid_utils.admin.ABIDModelAdmin.queryset
```

````

````{py:method} change_view(request, object_id, form_url='', extra_context=None)
:canonical: archivebox.abid_utils.admin.ABIDModelAdmin.change_view

```{autodoc2-docstring} archivebox.abid_utils.admin.ABIDModelAdmin.change_view
```

````

````{py:method} get_form(request, obj=None, **kwargs)
:canonical: archivebox.abid_utils.admin.ABIDModelAdmin.get_form

````

````{py:method} get_formset(request, formset=None, obj=None, **kwargs)
:canonical: archivebox.abid_utils.admin.ABIDModelAdmin.get_formset

```{autodoc2-docstring} archivebox.abid_utils.admin.ABIDModelAdmin.get_formset
```

````

````{py:method} save_model(request, obj, form, change)
:canonical: archivebox.abid_utils.admin.ABIDModelAdmin.save_model

````

````{py:method} abid_info(obj)
:canonical: archivebox.abid_utils.admin.ABIDModelAdmin.abid_info

```{autodoc2-docstring} archivebox.abid_utils.admin.ABIDModelAdmin.abid_info
```

````

````{py:method} regenerate_abid(request, obj)
:canonical: archivebox.abid_utils.admin.ABIDModelAdmin.regenerate_abid

```{autodoc2-docstring} archivebox.abid_utils.admin.ABIDModelAdmin.regenerate_abid
```

````

`````
