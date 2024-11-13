# {py:mod}`abx_spec_django`

```{py:module} abx_spec_django
```

```{autodoc2-docstring} abx_spec_django
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DjangoPluginSpec <abx_spec_django.DjangoPluginSpec>`
  - ```{autodoc2-docstring} abx_spec_django.DjangoPluginSpec
    :summary:
    ```
* - {py:obj}`ExpectedPluginSpec <abx_spec_django.ExpectedPluginSpec>`
  - ```{autodoc2-docstring} abx_spec_django.ExpectedPluginSpec
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__order__ <abx_spec_django.__order__>`
  - ```{autodoc2-docstring} abx_spec_django.__order__
    :summary:
    ```
* - {py:obj}`PLUGIN_SPEC <abx_spec_django.PLUGIN_SPEC>`
  - ```{autodoc2-docstring} abx_spec_django.PLUGIN_SPEC
    :summary:
    ```
* - {py:obj}`TypedPluginManager <abx_spec_django.TypedPluginManager>`
  - ```{autodoc2-docstring} abx_spec_django.TypedPluginManager
    :summary:
    ```
* - {py:obj}`pm <abx_spec_django.pm>`
  - ```{autodoc2-docstring} abx_spec_django.pm
    :summary:
    ```
````

### API

````{py:data} __order__
:canonical: abx_spec_django.__order__
:value: >
   300

```{autodoc2-docstring} abx_spec_django.__order__
```

````

`````{py:class} DjangoPluginSpec
:canonical: abx_spec_django.DjangoPluginSpec

```{autodoc2-docstring} abx_spec_django.DjangoPluginSpec
```

````{py:method} get_INSTALLED_APPS() -> typing.List[str]
:canonical: abx_spec_django.DjangoPluginSpec.get_INSTALLED_APPS

```{autodoc2-docstring} abx_spec_django.DjangoPluginSpec.get_INSTALLED_APPS
```

````

````{py:method} get_TEMPLATE_DIRS() -> typing.List[str]
:canonical: abx_spec_django.DjangoPluginSpec.get_TEMPLATE_DIRS

```{autodoc2-docstring} abx_spec_django.DjangoPluginSpec.get_TEMPLATE_DIRS
```

````

````{py:method} get_STATICFILES_DIRS() -> typing.List[str]
:canonical: abx_spec_django.DjangoPluginSpec.get_STATICFILES_DIRS

```{autodoc2-docstring} abx_spec_django.DjangoPluginSpec.get_STATICFILES_DIRS
```

````

````{py:method} get_MIDDLEWARES() -> typing.List[str]
:canonical: abx_spec_django.DjangoPluginSpec.get_MIDDLEWARES

```{autodoc2-docstring} abx_spec_django.DjangoPluginSpec.get_MIDDLEWARES
```

````

````{py:method} get_AUTHENTICATION_BACKENDS() -> typing.List[str]
:canonical: abx_spec_django.DjangoPluginSpec.get_AUTHENTICATION_BACKENDS

```{autodoc2-docstring} abx_spec_django.DjangoPluginSpec.get_AUTHENTICATION_BACKENDS
```

````

````{py:method} get_DJANGO_HUEY_QUEUES() -> typing.Dict[str, typing.Dict[str, typing.Any]]
:canonical: abx_spec_django.DjangoPluginSpec.get_DJANGO_HUEY_QUEUES

```{autodoc2-docstring} abx_spec_django.DjangoPluginSpec.get_DJANGO_HUEY_QUEUES
```

````

````{py:method} get_ADMIN_DATA_VIEWS_URLS() -> typing.List[str]
:canonical: abx_spec_django.DjangoPluginSpec.get_ADMIN_DATA_VIEWS_URLS

```{autodoc2-docstring} abx_spec_django.DjangoPluginSpec.get_ADMIN_DATA_VIEWS_URLS
```

````

````{py:method} get_urlpatterns() -> typing.List[str]
:canonical: abx_spec_django.DjangoPluginSpec.get_urlpatterns

```{autodoc2-docstring} abx_spec_django.DjangoPluginSpec.get_urlpatterns
```

````

````{py:method} register_admin() -> None
:canonical: abx_spec_django.DjangoPluginSpec.register_admin

```{autodoc2-docstring} abx_spec_django.DjangoPluginSpec.register_admin
```

````

````{py:method} ready() -> None
:canonical: abx_spec_django.DjangoPluginSpec.ready

```{autodoc2-docstring} abx_spec_django.DjangoPluginSpec.ready
```

````

`````

````{py:data} PLUGIN_SPEC
:canonical: abx_spec_django.PLUGIN_SPEC
:value: >
   None

```{autodoc2-docstring} abx_spec_django.PLUGIN_SPEC
```

````

````{py:class} ExpectedPluginSpec
:canonical: abx_spec_django.ExpectedPluginSpec

Bases: {py:obj}`abx_spec_django.DjangoPluginSpec`

```{autodoc2-docstring} abx_spec_django.ExpectedPluginSpec
```

````

````{py:data} TypedPluginManager
:canonical: abx_spec_django.TypedPluginManager
:value: >
   None

```{autodoc2-docstring} abx_spec_django.TypedPluginManager
```

````

````{py:data} pm
:canonical: abx_spec_django.pm
:value: >
   'cast(...)'

```{autodoc2-docstring} abx_spec_django.pm
```

````
