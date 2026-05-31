# {py:mod}`archivebox.core.forms`

```{py:module} archivebox.core.forms
```

```{autodoc2-docstring} archivebox.core.forms
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AddLinkForm <archivebox.core.forms.AddLinkForm>`
  -
* - {py:obj}`TagWidgetMixin <archivebox.core.forms.TagWidgetMixin>`
  - ```{autodoc2-docstring} archivebox.core.forms.TagWidgetMixin
    :summary:
    ```
* - {py:obj}`TagWidget <archivebox.core.forms.TagWidget>`
  -
* - {py:obj}`TagField <archivebox.core.forms.TagField>`
  - ```{autodoc2-docstring} archivebox.core.forms.TagField
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_plugin_choices <archivebox.core.forms.get_plugin_choices>`
  - ```{autodoc2-docstring} archivebox.core.forms.get_plugin_choices
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DEPTH_CHOICES <archivebox.core.forms.DEPTH_CHOICES>`
  - ```{autodoc2-docstring} archivebox.core.forms.DEPTH_CHOICES
    :summary:
    ```
````

### API

````{py:data} DEPTH_CHOICES
:canonical: archivebox.core.forms.DEPTH_CHOICES
:value: >
   (('0', 'depth = 0 (archive just these URLs)'), ('1', 'depth = 1 (+ URLs one hop away)'), ('2', 'dept...

```{autodoc2-docstring} archivebox.core.forms.DEPTH_CHOICES
```

````

````{py:function} get_plugin_choices()
:canonical: archivebox.core.forms.get_plugin_choices

```{autodoc2-docstring} archivebox.core.forms.get_plugin_choices
```
````

`````{py:class} AddLinkForm(*args, **kwargs)
:canonical: archivebox.core.forms.AddLinkForm

Bases: {py:obj}`django.forms.Form`

````{py:attribute} url
:canonical: archivebox.core.forms.AddLinkForm.url
:value: >
   'RegexField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.url
```

````

````{py:attribute} tag
:canonical: archivebox.core.forms.AddLinkForm.tag
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.tag
```

````

````{py:attribute} depth
:canonical: archivebox.core.forms.AddLinkForm.depth
:value: >
   'ChoiceField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.depth
```

````

````{py:attribute} notes
:canonical: archivebox.core.forms.AddLinkForm.notes
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.notes
```

````

````{py:attribute} chrome_plugins
:canonical: archivebox.core.forms.AddLinkForm.chrome_plugins
:value: >
   'MultipleChoiceField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.chrome_plugins
```

````

````{py:attribute} archiving_plugins
:canonical: archivebox.core.forms.AddLinkForm.archiving_plugins
:value: >
   'MultipleChoiceField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.archiving_plugins
```

````

````{py:attribute} parsing_plugins
:canonical: archivebox.core.forms.AddLinkForm.parsing_plugins
:value: >
   'MultipleChoiceField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.parsing_plugins
```

````

````{py:attribute} search_plugins
:canonical: archivebox.core.forms.AddLinkForm.search_plugins
:value: >
   'MultipleChoiceField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.search_plugins
```

````

````{py:attribute} binary_plugins
:canonical: archivebox.core.forms.AddLinkForm.binary_plugins
:value: >
   'MultipleChoiceField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.binary_plugins
```

````

````{py:attribute} extension_plugins
:canonical: archivebox.core.forms.AddLinkForm.extension_plugins
:value: >
   'MultipleChoiceField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.extension_plugins
```

````

````{py:attribute} schedule
:canonical: archivebox.core.forms.AddLinkForm.schedule
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.schedule
```

````

````{py:attribute} persona
:canonical: archivebox.core.forms.AddLinkForm.persona
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.persona
```

````

````{py:attribute} overwrite
:canonical: archivebox.core.forms.AddLinkForm.overwrite
:value: >
   'BooleanField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.overwrite
```

````

````{py:attribute} update
:canonical: archivebox.core.forms.AddLinkForm.update
:value: >
   'BooleanField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.update
```

````

````{py:attribute} index_only
:canonical: archivebox.core.forms.AddLinkForm.index_only
:value: >
   'BooleanField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.index_only
```

````

````{py:attribute} config
:canonical: archivebox.core.forms.AddLinkForm.config
:value: >
   'JSONField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.config
```

````

````{py:method} clean()
:canonical: archivebox.core.forms.AddLinkForm.clean

````

````{py:method} clean_schedule()
:canonical: archivebox.core.forms.AddLinkForm.clean_schedule

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.clean_schedule
```

````

`````

`````{py:class} TagWidgetMixin
:canonical: archivebox.core.forms.TagWidgetMixin

```{autodoc2-docstring} archivebox.core.forms.TagWidgetMixin
```

````{py:method} format_value(value)
:canonical: archivebox.core.forms.TagWidgetMixin.format_value

```{autodoc2-docstring} archivebox.core.forms.TagWidgetMixin.format_value
```

````

`````

```{py:class} TagWidget(attrs=None)
:canonical: archivebox.core.forms.TagWidget

Bases: {py:obj}`archivebox.core.forms.TagWidgetMixin`, {py:obj}`django.forms.TextInput`

```

`````{py:class} TagField(*, max_length=None, min_length=None, strip=True, empty_value='', **kwargs)
:canonical: archivebox.core.forms.TagField

Bases: {py:obj}`django.forms.CharField`

```{autodoc2-docstring} archivebox.core.forms.TagField
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.core.forms.TagField.__init__
```

````{py:attribute} widget
:canonical: archivebox.core.forms.TagField.widget
:value: >
   None

```{autodoc2-docstring} archivebox.core.forms.TagField.widget
```

````

````{py:method} clean(value)
:canonical: archivebox.core.forms.TagField.clean

````

````{py:method} has_changed(initial_value, data_value)
:canonical: archivebox.core.forms.TagField.has_changed

````

`````
