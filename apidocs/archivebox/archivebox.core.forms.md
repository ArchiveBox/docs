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

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PARSER_CHOICES <archivebox.core.forms.PARSER_CHOICES>`
  - ```{autodoc2-docstring} archivebox.core.forms.PARSER_CHOICES
    :summary:
    ```
* - {py:obj}`DEPTH_CHOICES <archivebox.core.forms.DEPTH_CHOICES>`
  - ```{autodoc2-docstring} archivebox.core.forms.DEPTH_CHOICES
    :summary:
    ```
* - {py:obj}`ARCHIVE_METHODS <archivebox.core.forms.ARCHIVE_METHODS>`
  - ```{autodoc2-docstring} archivebox.core.forms.ARCHIVE_METHODS
    :summary:
    ```
````

### API

````{py:data} PARSER_CHOICES
:canonical: archivebox.core.forms.PARSER_CHOICES
:value: >
   None

```{autodoc2-docstring} archivebox.core.forms.PARSER_CHOICES
```

````

````{py:data} DEPTH_CHOICES
:canonical: archivebox.core.forms.DEPTH_CHOICES
:value: >
   (('0', 'depth = 0 (archive just these URLs)'), ('1', 'depth = 1 (archive these URLs and all URLs one...

```{autodoc2-docstring} archivebox.core.forms.DEPTH_CHOICES
```

````

````{py:data} ARCHIVE_METHODS
:canonical: archivebox.core.forms.ARCHIVE_METHODS
:value: >
   None

```{autodoc2-docstring} archivebox.core.forms.ARCHIVE_METHODS
```

````

`````{py:class} AddLinkForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, field_order=None, use_required_attribute=None, renderer=None)
:canonical: archivebox.core.forms.AddLinkForm

Bases: {py:obj}`django.forms.Form`

````{py:attribute} url
:canonical: archivebox.core.forms.AddLinkForm.url
:value: >
   'RegexField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.url
```

````

````{py:attribute} parser
:canonical: archivebox.core.forms.AddLinkForm.parser
:value: >
   'ChoiceField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.parser
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

````{py:attribute} archive_methods
:canonical: archivebox.core.forms.AddLinkForm.archive_methods
:value: >
   'MultipleChoiceField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.archive_methods
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
