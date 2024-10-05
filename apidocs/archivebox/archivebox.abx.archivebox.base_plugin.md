# {py:mod}`archivebox.abx.archivebox.base_plugin`

```{py:module} archivebox.abx.archivebox.base_plugin
```

```{autodoc2-docstring} archivebox.abx.archivebox.base_plugin
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BasePlugin <archivebox.abx.archivebox.base_plugin.BasePlugin>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.abx.archivebox.base_plugin.__package__>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_plugin.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.abx.archivebox.base_plugin.__package__
:value: >
   'abx.archivebox'

```{autodoc2-docstring} archivebox.abx.archivebox.base_plugin.__package__
```

````

`````{py:class} BasePlugin(/, **data: typing.Any)
:canonical: archivebox.abx.archivebox.base_plugin.BasePlugin

Bases: {py:obj}`pydantic.BaseModel`

````{py:attribute} model_config
:canonical: archivebox.abx.archivebox.base_plugin.BasePlugin.model_config
:value: >
   'ConfigDict(...)'

```{autodoc2-docstring} archivebox.abx.archivebox.base_plugin.BasePlugin.model_config
```

````

````{py:attribute} app_label
:canonical: archivebox.abx.archivebox.base_plugin.BasePlugin.app_label
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.abx.archivebox.base_plugin.BasePlugin.app_label
```

````

````{py:attribute} verbose_name
:canonical: archivebox.abx.archivebox.base_plugin.BasePlugin.verbose_name
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.abx.archivebox.base_plugin.BasePlugin.verbose_name
```

````

````{py:attribute} docs_url
:canonical: archivebox.abx.archivebox.base_plugin.BasePlugin.docs_url
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.abx.archivebox.base_plugin.BasePlugin.docs_url
```

````

````{py:attribute} hooks
:canonical: archivebox.abx.archivebox.base_plugin.BasePlugin.hooks
:type: typing.List[pydantic.InstanceOf[archivebox.abx.archivebox.base_hook.BaseHook]]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.abx.archivebox.base_plugin.BasePlugin.hooks
```

````

````{py:attribute} _is_registered
:canonical: archivebox.abx.archivebox.base_plugin.BasePlugin._is_registered
:type: bool
:value: >
   False

```{autodoc2-docstring} archivebox.abx.archivebox.base_plugin.BasePlugin._is_registered
```

````

````{py:attribute} _is_ready
:canonical: archivebox.abx.archivebox.base_plugin.BasePlugin._is_ready
:type: bool
:value: >
   False

```{autodoc2-docstring} archivebox.abx.archivebox.base_plugin.BasePlugin._is_ready
```

````

````{py:property} id
:canonical: archivebox.abx.archivebox.base_plugin.BasePlugin.id
:type: str

```{autodoc2-docstring} archivebox.abx.archivebox.base_plugin.BasePlugin.id
```

````

````{py:property} name
:canonical: archivebox.abx.archivebox.base_plugin.BasePlugin.name
:type: str

```{autodoc2-docstring} archivebox.abx.archivebox.base_plugin.BasePlugin.name
```

````

````{py:property} plugin_module
:canonical: archivebox.abx.archivebox.base_plugin.BasePlugin.plugin_module
:type: str

```{autodoc2-docstring} archivebox.abx.archivebox.base_plugin.BasePlugin.plugin_module
```

````

````{py:property} plugin_module_full
:canonical: archivebox.abx.archivebox.base_plugin.BasePlugin.plugin_module_full
:type: str

```{autodoc2-docstring} archivebox.abx.archivebox.base_plugin.BasePlugin.plugin_module_full
```

````

````{py:property} plugin_dir
:canonical: archivebox.abx.archivebox.base_plugin.BasePlugin.plugin_dir
:type: pathlib.Path

```{autodoc2-docstring} archivebox.abx.archivebox.base_plugin.BasePlugin.plugin_dir
```

````

````{py:method} validate() -> typing_extensions.Self
:canonical: archivebox.abx.archivebox.base_plugin.BasePlugin.validate

```{autodoc2-docstring} archivebox.abx.archivebox.base_plugin.BasePlugin.validate
```

````

````{py:property} AppConfig
:canonical: archivebox.abx.archivebox.base_plugin.BasePlugin.AppConfig
:type: typing.Type[django.apps.AppConfig]

```{autodoc2-docstring} archivebox.abx.archivebox.base_plugin.BasePlugin.AppConfig
```

````

````{py:property} HOOKS_BY_ID
:canonical: archivebox.abx.archivebox.base_plugin.BasePlugin.HOOKS_BY_ID
:type: typing.Dict[str, pydantic.InstanceOf[archivebox.abx.archivebox.base_hook.BaseHook]]

```{autodoc2-docstring} archivebox.abx.archivebox.base_plugin.BasePlugin.HOOKS_BY_ID
```

````

````{py:property} HOOKS_BY_TYPE
:canonical: archivebox.abx.archivebox.base_plugin.BasePlugin.HOOKS_BY_TYPE
:type: typing.Dict[archivebox.abx.archivebox.base_hook.HookType, typing.Dict[str, pydantic.InstanceOf[archivebox.abx.archivebox.base_hook.BaseHook]]]

```{autodoc2-docstring} archivebox.abx.archivebox.base_plugin.BasePlugin.HOOKS_BY_TYPE
```

````

````{py:method} register(settings)
:canonical: archivebox.abx.archivebox.base_plugin.BasePlugin.register

```{autodoc2-docstring} archivebox.abx.archivebox.base_plugin.BasePlugin.register
```

````

````{py:method} ready(settings=None)
:canonical: archivebox.abx.archivebox.base_plugin.BasePlugin.ready

```{autodoc2-docstring} archivebox.abx.archivebox.base_plugin.BasePlugin.ready
```

````

````{py:method} get_INSTALLED_APPS()
:canonical: archivebox.abx.archivebox.base_plugin.BasePlugin.get_INSTALLED_APPS

```{autodoc2-docstring} archivebox.abx.archivebox.base_plugin.BasePlugin.get_INSTALLED_APPS
```

````

`````
