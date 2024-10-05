# {py:mod}`archivebox.abx.archivebox.base_hook`

```{py:module} archivebox.abx.archivebox.base_hook
```

```{autodoc2-docstring} archivebox.abx.archivebox.base_hook
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseHook <archivebox.abx.archivebox.base_hook.BaseHook>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.abx.archivebox.base_hook.__package__>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_hook.__package__
    :summary:
    ```
* - {py:obj}`HookType <archivebox.abx.archivebox.base_hook.HookType>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_hook.HookType
    :summary:
    ```
* - {py:obj}`hook_type_names <archivebox.abx.archivebox.base_hook.hook_type_names>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_hook.hook_type_names
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.abx.archivebox.base_hook.__package__
:value: >
   'abx.archivebox'

```{autodoc2-docstring} archivebox.abx.archivebox.base_hook.__package__
```

````

````{py:data} HookType
:canonical: archivebox.abx.archivebox.base_hook.HookType
:value: >
   None

```{autodoc2-docstring} archivebox.abx.archivebox.base_hook.HookType
```

````

````{py:data} hook_type_names
:canonical: archivebox.abx.archivebox.base_hook.hook_type_names
:type: typing.Tuple[archivebox.abx.archivebox.base_hook.HookType]
:value: >
   'get_args(...)'

```{autodoc2-docstring} archivebox.abx.archivebox.base_hook.hook_type_names
```

````

`````{py:class} BaseHook(/, **data: typing.Any)
:canonical: archivebox.abx.archivebox.base_hook.BaseHook

Bases: {py:obj}`pydantic.BaseModel`

````{py:attribute} model_config
:canonical: archivebox.abx.archivebox.base_hook.BaseHook.model_config
:value: >
   'ConfigDict(...)'

```{autodoc2-docstring} archivebox.abx.archivebox.base_hook.BaseHook.model_config
```

````

````{py:attribute} hook_type
:canonical: archivebox.abx.archivebox.base_hook.BaseHook.hook_type
:type: typing.ClassVar[archivebox.abx.archivebox.base_hook.HookType]
:value: >
   None

```{autodoc2-docstring} archivebox.abx.archivebox.base_hook.BaseHook.hook_type
```

````

````{py:attribute} _is_registered
:canonical: archivebox.abx.archivebox.base_hook.BaseHook._is_registered
:type: bool
:value: >
   False

```{autodoc2-docstring} archivebox.abx.archivebox.base_hook.BaseHook._is_registered
```

````

````{py:attribute} _is_ready
:canonical: archivebox.abx.archivebox.base_hook.BaseHook._is_ready
:type: bool
:value: >
   False

```{autodoc2-docstring} archivebox.abx.archivebox.base_hook.BaseHook._is_ready
```

````

````{py:property} id
:canonical: archivebox.abx.archivebox.base_hook.BaseHook.id
:type: str

```{autodoc2-docstring} archivebox.abx.archivebox.base_hook.BaseHook.id
```

````

````{py:property} hook_module
:canonical: archivebox.abx.archivebox.base_hook.BaseHook.hook_module
:type: str

```{autodoc2-docstring} archivebox.abx.archivebox.base_hook.BaseHook.hook_module
```

````

````{py:property} hook_file
:canonical: archivebox.abx.archivebox.base_hook.BaseHook.hook_file
:type: pathlib.Path

```{autodoc2-docstring} archivebox.abx.archivebox.base_hook.BaseHook.hook_file
```

````

````{py:property} plugin_module
:canonical: archivebox.abx.archivebox.base_hook.BaseHook.plugin_module
:type: str

```{autodoc2-docstring} archivebox.abx.archivebox.base_hook.BaseHook.plugin_module
```

````

````{py:property} plugin_dir
:canonical: archivebox.abx.archivebox.base_hook.BaseHook.plugin_dir
:type: pathlib.Path

```{autodoc2-docstring} archivebox.abx.archivebox.base_hook.BaseHook.plugin_dir
```

````

````{py:property} admin_url
:canonical: archivebox.abx.archivebox.base_hook.BaseHook.admin_url
:type: str

```{autodoc2-docstring} archivebox.abx.archivebox.base_hook.BaseHook.admin_url
```

````

````{py:method} register(settings)
:canonical: archivebox.abx.archivebox.base_hook.BaseHook.register

```{autodoc2-docstring} archivebox.abx.archivebox.base_hook.BaseHook.register
```

````

````{py:method} ready()
:canonical: archivebox.abx.archivebox.base_hook.BaseHook.ready

```{autodoc2-docstring} archivebox.abx.archivebox.base_hook.BaseHook.ready
```

````

`````
