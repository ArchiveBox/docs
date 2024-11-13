# {py:mod}`abx_plugin_singlefile.models`

```{py:module} abx_plugin_singlefile.models
```

```{autodoc2-docstring} abx_plugin_singlefile.models
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SinglefileResultManager <abx_plugin_singlefile.models.SinglefileResultManager>`
  - ```{autodoc2-docstring} abx_plugin_singlefile.models.SinglefileResultManager
    :summary:
    ```
* - {py:obj}`SinglefileResult <abx_plugin_singlefile.models.SinglefileResult>`
  -
````

### API

`````{py:class} SinglefileResultManager
:canonical: abx_plugin_singlefile.models.SinglefileResultManager

Bases: {py:obj}`django.db.models.Manager`

```{autodoc2-docstring} abx_plugin_singlefile.models.SinglefileResultManager
```

````{py:method} get_queryset()
:canonical: abx_plugin_singlefile.models.SinglefileResultManager.get_queryset

```{autodoc2-docstring} abx_plugin_singlefile.models.SinglefileResultManager.get_queryset
```

````

`````

``````{py:class} SinglefileResult(*args: typing.Any, **kwargs: typing.Any)
:canonical: abx_plugin_singlefile.models.SinglefileResult

Bases: {py:obj}`core.models.ArchiveResult`

````{py:attribute} objects
:canonical: abx_plugin_singlefile.models.SinglefileResult.objects
:value: >
   'SinglefileResultManager(...)'

```{autodoc2-docstring} abx_plugin_singlefile.models.SinglefileResult.objects
```

````

`````{py:class} Meta
:canonical: abx_plugin_singlefile.models.SinglefileResult.Meta

```{autodoc2-docstring} abx_plugin_singlefile.models.SinglefileResult.Meta
```

````{py:attribute} proxy
:canonical: abx_plugin_singlefile.models.SinglefileResult.Meta.proxy
:value: >
   True

```{autodoc2-docstring} abx_plugin_singlefile.models.SinglefileResult.Meta.proxy
```

````

`````

``````
