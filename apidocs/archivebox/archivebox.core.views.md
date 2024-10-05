# {py:mod}`archivebox.core.views`

```{py:module} archivebox.core.views
```

```{autodoc2-docstring} archivebox.core.views
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`HomepageView <archivebox.core.views.HomepageView>`
  -
* - {py:obj}`SnapshotView <archivebox.core.views.SnapshotView>`
  -
* - {py:obj}`PublicIndexView <archivebox.core.views.PublicIndexView>`
  -
* - {py:obj}`AddView <archivebox.core.views.AddView>`
  -
* - {py:obj}`HealthCheckView <archivebox.core.views.HealthCheckView>`
  - ```{autodoc2-docstring} archivebox.core.views.HealthCheckView
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`find_config_section <archivebox.core.views.find_config_section>`
  - ```{autodoc2-docstring} archivebox.core.views.find_config_section
    :summary:
    ```
* - {py:obj}`find_config_default <archivebox.core.views.find_config_default>`
  - ```{autodoc2-docstring} archivebox.core.views.find_config_default
    :summary:
    ```
* - {py:obj}`find_config_type <archivebox.core.views.find_config_type>`
  - ```{autodoc2-docstring} archivebox.core.views.find_config_type
    :summary:
    ```
* - {py:obj}`key_is_safe <archivebox.core.views.key_is_safe>`
  - ```{autodoc2-docstring} archivebox.core.views.key_is_safe
    :summary:
    ```
* - {py:obj}`live_config_list_view <archivebox.core.views.live_config_list_view>`
  - ```{autodoc2-docstring} archivebox.core.views.live_config_list_view
    :summary:
    ```
* - {py:obj}`live_config_value_view <archivebox.core.views.live_config_value_view>`
  - ```{autodoc2-docstring} archivebox.core.views.live_config_value_view
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.core.views.__package__>`
  - ```{autodoc2-docstring} archivebox.core.views.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.core.views.__package__
:value: >
   'archivebox.core'

```{autodoc2-docstring} archivebox.core.views.__package__
```

````

`````{py:class} HomepageView(**kwargs)
:canonical: archivebox.core.views.HomepageView

Bases: {py:obj}`django.views.View`

````{py:method} get(request)
:canonical: archivebox.core.views.HomepageView.get

```{autodoc2-docstring} archivebox.core.views.HomepageView.get
```

````

`````

`````{py:class} SnapshotView(**kwargs)
:canonical: archivebox.core.views.SnapshotView

Bases: {py:obj}`django.views.View`

````{py:method} render_live_index(request, snapshot)
:canonical: archivebox.core.views.SnapshotView.render_live_index
:staticmethod:

```{autodoc2-docstring} archivebox.core.views.SnapshotView.render_live_index
```

````

````{py:method} get(request, path)
:canonical: archivebox.core.views.SnapshotView.get

```{autodoc2-docstring} archivebox.core.views.SnapshotView.get
```

````

`````

`````{py:class} PublicIndexView(**kwargs)
:canonical: archivebox.core.views.PublicIndexView

Bases: {py:obj}`django.views.generic.list.ListView`

````{py:attribute} template_name
:canonical: archivebox.core.views.PublicIndexView.template_name
:value: >
   'public_index.html'

```{autodoc2-docstring} archivebox.core.views.PublicIndexView.template_name
```

````

````{py:attribute} model
:canonical: archivebox.core.views.PublicIndexView.model
:value: >
   None

```{autodoc2-docstring} archivebox.core.views.PublicIndexView.model
```

````

````{py:attribute} paginate_by
:canonical: archivebox.core.views.PublicIndexView.paginate_by
:value: >
   None

```{autodoc2-docstring} archivebox.core.views.PublicIndexView.paginate_by
```

````

````{py:attribute} ordering
:canonical: archivebox.core.views.PublicIndexView.ordering
:value: >
   ['-bookmarked_at', '-created_at']

```{autodoc2-docstring} archivebox.core.views.PublicIndexView.ordering
```

````

````{py:method} get_context_data(**kwargs)
:canonical: archivebox.core.views.PublicIndexView.get_context_data

````

````{py:method} get_queryset(**kwargs)
:canonical: archivebox.core.views.PublicIndexView.get_queryset

````

````{py:method} get(*args, **kwargs)
:canonical: archivebox.core.views.PublicIndexView.get

```{autodoc2-docstring} archivebox.core.views.PublicIndexView.get
```

````

`````

`````{py:class} AddView(**kwargs)
:canonical: archivebox.core.views.AddView

Bases: {py:obj}`django.contrib.auth.mixins.UserPassesTestMixin`, {py:obj}`django.views.generic.FormView`

````{py:attribute} template_name
:canonical: archivebox.core.views.AddView.template_name
:value: >
   'add.html'

```{autodoc2-docstring} archivebox.core.views.AddView.template_name
```

````

````{py:attribute} form_class
:canonical: archivebox.core.views.AddView.form_class
:value: >
   None

```{autodoc2-docstring} archivebox.core.views.AddView.form_class
```

````

````{py:method} get_initial()
:canonical: archivebox.core.views.AddView.get_initial

```{autodoc2-docstring} archivebox.core.views.AddView.get_initial
```

````

````{py:method} test_func()
:canonical: archivebox.core.views.AddView.test_func

```{autodoc2-docstring} archivebox.core.views.AddView.test_func
```

````

````{py:method} get_context_data(**kwargs)
:canonical: archivebox.core.views.AddView.get_context_data

````

````{py:method} form_valid(form)
:canonical: archivebox.core.views.AddView.form_valid

````

`````

`````{py:class} HealthCheckView(**kwargs)
:canonical: archivebox.core.views.HealthCheckView

Bases: {py:obj}`django.views.View`

```{autodoc2-docstring} archivebox.core.views.HealthCheckView
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.core.views.HealthCheckView.__init__
```

````{py:method} get(request)
:canonical: archivebox.core.views.HealthCheckView.get

```{autodoc2-docstring} archivebox.core.views.HealthCheckView.get
```

````

`````

````{py:function} find_config_section(key: str) -> str
:canonical: archivebox.core.views.find_config_section

```{autodoc2-docstring} archivebox.core.views.find_config_section
```
````

````{py:function} find_config_default(key: str) -> str
:canonical: archivebox.core.views.find_config_default

```{autodoc2-docstring} archivebox.core.views.find_config_default
```
````

````{py:function} find_config_type(key: str) -> str
:canonical: archivebox.core.views.find_config_type

```{autodoc2-docstring} archivebox.core.views.find_config_type
```
````

````{py:function} key_is_safe(key: str) -> bool
:canonical: archivebox.core.views.key_is_safe

```{autodoc2-docstring} archivebox.core.views.key_is_safe
```
````

````{py:function} live_config_list_view(request: django.http.HttpRequest, **kwargs) -> admin_data_views.typing.TableContext
:canonical: archivebox.core.views.live_config_list_view

```{autodoc2-docstring} archivebox.core.views.live_config_list_view
```
````

````{py:function} live_config_value_view(request: django.http.HttpRequest, key: str, **kwargs) -> admin_data_views.typing.ItemContext
:canonical: archivebox.core.views.live_config_value_view

```{autodoc2-docstring} archivebox.core.views.live_config_value_view
```
````
