# {py:mod}`archivebox.config.apps`

```{py:module} archivebox.config.apps
```

```{autodoc2-docstring} archivebox.config.apps
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ConfigPlugin <archivebox.config.apps.ConfigPlugin>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.config.apps.__package__>`
  - ```{autodoc2-docstring} archivebox.config.apps.__package__
    :summary:
    ```
* - {py:obj}`PLUGIN <archivebox.config.apps.PLUGIN>`
  - ```{autodoc2-docstring} archivebox.config.apps.PLUGIN
    :summary:
    ```
* - {py:obj}`DJANGO_APP <archivebox.config.apps.DJANGO_APP>`
  - ```{autodoc2-docstring} archivebox.config.apps.DJANGO_APP
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.config.apps.__package__
:value: >
   'archivebox.config'

```{autodoc2-docstring} archivebox.config.apps.__package__
```

````

`````{py:class} ConfigPlugin(/, **data: typing.Any)
:canonical: archivebox.config.apps.ConfigPlugin

Bases: {py:obj}`abx.archivebox.base_plugin.BasePlugin`

````{py:attribute} app_label
:canonical: archivebox.config.apps.ConfigPlugin.app_label
:type: str
:value: >
   'CONFIG'

```{autodoc2-docstring} archivebox.config.apps.ConfigPlugin.app_label
```

````

````{py:attribute} verbose_name
:canonical: archivebox.config.apps.ConfigPlugin.verbose_name
:type: str
:value: >
   'Configuration'

```{autodoc2-docstring} archivebox.config.apps.ConfigPlugin.verbose_name
```

````

````{py:attribute} hooks
:canonical: archivebox.config.apps.ConfigPlugin.hooks
:type: typing.List[pydantic.InstanceOf[abx.archivebox.base_hook.BaseHook]]
:value: >
   None

```{autodoc2-docstring} archivebox.config.apps.ConfigPlugin.hooks
```

````

`````

````{py:data} PLUGIN
:canonical: archivebox.config.apps.PLUGIN
:value: >
   'ConfigPlugin(...)'

```{autodoc2-docstring} archivebox.config.apps.PLUGIN
```

````

````{py:data} DJANGO_APP
:canonical: archivebox.config.apps.DJANGO_APP
:value: >
   None

```{autodoc2-docstring} archivebox.config.apps.DJANGO_APP
```

````
