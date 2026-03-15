# {py:mod}`archivebox.base_models.admin`

```{py:module} archivebox.base_models.admin
```

```{autodoc2-docstring} archivebox.base_models.admin
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`KeyValueWidget <archivebox.base_models.admin.KeyValueWidget>`
  - ```{autodoc2-docstring} archivebox.base_models.admin.KeyValueWidget
    :summary:
    ```
* - {py:obj}`ConfigEditorMixin <archivebox.base_models.admin.ConfigEditorMixin>`
  - ```{autodoc2-docstring} archivebox.base_models.admin.ConfigEditorMixin
    :summary:
    ```
* - {py:obj}`BaseModelAdmin <archivebox.base_models.admin.BaseModelAdmin>`
  -
````

### API

``````{py:class} KeyValueWidget(attrs=None)
:canonical: archivebox.base_models.admin.KeyValueWidget

Bases: {py:obj}`django.forms.Widget`

```{autodoc2-docstring} archivebox.base_models.admin.KeyValueWidget
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.base_models.admin.KeyValueWidget.__init__
```

````{py:attribute} template_name
:canonical: archivebox.base_models.admin.KeyValueWidget.template_name
:value: >
   None

```{autodoc2-docstring} archivebox.base_models.admin.KeyValueWidget.template_name
```

````

`````{py:class} Media
:canonical: archivebox.base_models.admin.KeyValueWidget.Media

```{autodoc2-docstring} archivebox.base_models.admin.KeyValueWidget.Media
```

````{py:attribute} css
:canonical: archivebox.base_models.admin.KeyValueWidget.Media.css
:value: >
   None

```{autodoc2-docstring} archivebox.base_models.admin.KeyValueWidget.Media.css
```

````

````{py:attribute} js
:canonical: archivebox.base_models.admin.KeyValueWidget.Media.js
:value: >
   []

```{autodoc2-docstring} archivebox.base_models.admin.KeyValueWidget.Media.js
```

````

`````

````{py:method} _get_config_options()
:canonical: archivebox.base_models.admin.KeyValueWidget._get_config_options

```{autodoc2-docstring} archivebox.base_models.admin.KeyValueWidget._get_config_options
```

````

````{py:method} render(name, value, attrs=None, renderer=None)
:canonical: archivebox.base_models.admin.KeyValueWidget.render

````

````{py:method} _render_row(widget_id, idx, key, value)
:canonical: archivebox.base_models.admin.KeyValueWidget._render_row

```{autodoc2-docstring} archivebox.base_models.admin.KeyValueWidget._render_row
```

````

````{py:method} _escape(s)
:canonical: archivebox.base_models.admin.KeyValueWidget._escape

```{autodoc2-docstring} archivebox.base_models.admin.KeyValueWidget._escape
```

````

````{py:method} value_from_datadict(data, files, name)
:canonical: archivebox.base_models.admin.KeyValueWidget.value_from_datadict

````

``````

`````{py:class} ConfigEditorMixin
:canonical: archivebox.base_models.admin.ConfigEditorMixin

```{autodoc2-docstring} archivebox.base_models.admin.ConfigEditorMixin
```

````{py:method} formfield_for_dbfield(db_field, request, **kwargs)
:canonical: archivebox.base_models.admin.ConfigEditorMixin.formfield_for_dbfield

```{autodoc2-docstring} archivebox.base_models.admin.ConfigEditorMixin.formfield_for_dbfield
```

````

`````

`````{py:class} BaseModelAdmin(model, admin_site)
:canonical: archivebox.base_models.admin.BaseModelAdmin

Bases: {py:obj}`django_object_actions.DjangoObjectActions`, {py:obj}`django.contrib.admin.ModelAdmin`

````{py:attribute} list_display
:canonical: archivebox.base_models.admin.BaseModelAdmin.list_display
:value: >
   ('id', 'created_at', 'created_by')

```{autodoc2-docstring} archivebox.base_models.admin.BaseModelAdmin.list_display
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.base_models.admin.BaseModelAdmin.readonly_fields
:value: >
   ('id', 'created_at', 'modified_at')

```{autodoc2-docstring} archivebox.base_models.admin.BaseModelAdmin.readonly_fields
```

````

````{py:method} get_form(request, obj=None, **kwargs)
:canonical: archivebox.base_models.admin.BaseModelAdmin.get_form

````

`````
