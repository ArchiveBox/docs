# {py:mod}`abx`

```{py:module} abx
```

```{autodoc2-docstring} abx
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`HookSpecDecoratorThatReturnsFirstResult <abx.HookSpecDecoratorThatReturnsFirstResult>`
  -
* - {py:obj}`HookSpecDecoratorThatReturnsListResults <abx.HookSpecDecoratorThatReturnsListResults>`
  -
* - {py:obj}`TypedHookspecMarker <abx.TypedHookspecMarker>`
  - ```{autodoc2-docstring} abx.TypedHookspecMarker
    :summary:
    ```
* - {py:obj}`PluginInfo <abx.PluginInfo>`
  -
* - {py:obj}`ABXPluginManager <abx.ABXPluginManager>`
  - ```{autodoc2-docstring} abx.ABXPluginManager
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`is_valid_attr_name <abx.is_valid_attr_name>`
  - ```{autodoc2-docstring} abx.is_valid_attr_name
    :summary:
    ```
* - {py:obj}`is_valid_module_name <abx.is_valid_module_name>`
  - ```{autodoc2-docstring} abx.is_valid_module_name
    :summary:
    ```
* - {py:obj}`get_plugin_order <abx.get_plugin_order>`
  - ```{autodoc2-docstring} abx.get_plugin_order
    :summary:
    ```
* - {py:obj}`get_plugin <abx.get_plugin>`
  - ```{autodoc2-docstring} abx.get_plugin
    :summary:
    ```
* - {py:obj}`get_all_plugins <abx.get_all_plugins>`
  - ```{autodoc2-docstring} abx.get_all_plugins
    :summary:
    ```
* - {py:obj}`get_all_hook_names <abx.get_all_hook_names>`
  - ```{autodoc2-docstring} abx.get_all_hook_names
    :summary:
    ```
* - {py:obj}`get_all_hook_specs <abx.get_all_hook_specs>`
  - ```{autodoc2-docstring} abx.get_all_hook_specs
    :summary:
    ```
* - {py:obj}`find_plugins_in_dir <abx.find_plugins_in_dir>`
  - ```{autodoc2-docstring} abx.find_plugins_in_dir
    :summary:
    ```
* - {py:obj}`get_pip_installed_plugins <abx.get_pip_installed_plugins>`
  - ```{autodoc2-docstring} abx.get_pip_installed_plugins
    :summary:
    ```
* - {py:obj}`load_plugins <abx.load_plugins>`
  - ```{autodoc2-docstring} abx.load_plugins
    :summary:
    ```
* - {py:obj}`get_plugin_hooks <abx.get_plugin_hooks>`
  - ```{autodoc2-docstring} abx.get_plugin_hooks
    :summary:
    ```
* - {py:obj}`as_list <abx.as_list>`
  - ```{autodoc2-docstring} abx.as_list
    :summary:
    ```
* - {py:obj}`as_dict <abx.as_dict>`
  - ```{autodoc2-docstring} abx.as_dict
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__id__ <abx.__id__>`
  - ```{autodoc2-docstring} abx.__id__
    :summary:
    ```
* - {py:obj}`__label__ <abx.__label__>`
  - ```{autodoc2-docstring} abx.__label__
    :summary:
    ```
* - {py:obj}`__author__ <abx.__author__>`
  - ```{autodoc2-docstring} abx.__author__
    :summary:
    ```
* - {py:obj}`__homepage__ <abx.__homepage__>`
  - ```{autodoc2-docstring} abx.__homepage__
    :summary:
    ```
* - {py:obj}`__order__ <abx.__order__>`
  - ```{autodoc2-docstring} abx.__order__
    :summary:
    ```
* - {py:obj}`ParamsT <abx.ParamsT>`
  - ```{autodoc2-docstring} abx.ParamsT
    :summary:
    ```
* - {py:obj}`ReturnT <abx.ReturnT>`
  - ```{autodoc2-docstring} abx.ReturnT
    :summary:
    ```
* - {py:obj}`AttrName <abx.AttrName>`
  - ```{autodoc2-docstring} abx.AttrName
    :summary:
    ```
* - {py:obj}`PluginId <abx.PluginId>`
  - ```{autodoc2-docstring} abx.PluginId
    :summary:
    ```
* - {py:obj}`PluginSpec <abx.PluginSpec>`
  - ```{autodoc2-docstring} abx.PluginSpec
    :summary:
    ```
* - {py:obj}`pm <abx.pm>`
  - ```{autodoc2-docstring} abx.pm
    :summary:
    ```
````

### API

````{py:data} __id__
:canonical: abx.__id__
:value: >
   'abx'

```{autodoc2-docstring} abx.__id__
```

````

````{py:data} __label__
:canonical: abx.__label__
:value: >
   'ABX'

```{autodoc2-docstring} abx.__label__
```

````

````{py:data} __author__
:canonical: abx.__author__
:value: >
   'Nick Sweeting'

```{autodoc2-docstring} abx.__author__
```

````

````{py:data} __homepage__
:canonical: abx.__homepage__
:value: >
   'https://github.com/ArchiveBox'

```{autodoc2-docstring} abx.__homepage__
```

````

````{py:data} __order__
:canonical: abx.__order__
:value: >
   0

```{autodoc2-docstring} abx.__order__
```

````

````{py:data} ParamsT
:canonical: abx.ParamsT
:value: >
   'ParamSpec(...)'

```{autodoc2-docstring} abx.ParamsT
```

````

````{py:data} ReturnT
:canonical: abx.ReturnT
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} abx.ReturnT
```

````

`````{py:class} HookSpecDecoratorThatReturnsFirstResult
:canonical: abx.HookSpecDecoratorThatReturnsFirstResult

Bases: {py:obj}`typing.Protocol`

````{py:method} __call__(func: typing.Callable[abx.ParamsT, abx.ReturnT]) -> typing.Callable[abx.ParamsT, abx.ReturnT]
:canonical: abx.HookSpecDecoratorThatReturnsFirstResult.__call__

```{autodoc2-docstring} abx.HookSpecDecoratorThatReturnsFirstResult.__call__
```

````

`````

`````{py:class} HookSpecDecoratorThatReturnsListResults
:canonical: abx.HookSpecDecoratorThatReturnsListResults

Bases: {py:obj}`typing.Protocol`

````{py:method} __call__(func: typing.Callable[abx.ParamsT, abx.ReturnT]) -> typing.Callable[abx.ParamsT, typing.List[abx.ReturnT]]
:canonical: abx.HookSpecDecoratorThatReturnsListResults.__call__

```{autodoc2-docstring} abx.HookSpecDecoratorThatReturnsListResults.__call__
```

````

`````

`````{py:class} TypedHookspecMarker(project_name: str)
:canonical: abx.TypedHookspecMarker

```{autodoc2-docstring} abx.TypedHookspecMarker
```

```{rubric} Initialization
```

```{autodoc2-docstring} abx.TypedHookspecMarker.__init__
```

````{py:attribute} __slots__
:canonical: abx.TypedHookspecMarker.__slots__
:value: >
   ('project_name',)

```{autodoc2-docstring} abx.TypedHookspecMarker.__slots__
```

````

````{py:method} __call__(function: typing.Callable[abx.ParamsT, abx.ReturnT] | None = None, firstresult: bool = False, historic: bool = False, warn_on_impl: Warning | None = None, warn_on_impl_args: typing.Mapping[str, Warning] | None = None) -> typing.Callable[abx.ParamsT, typing.List[abx.ReturnT]] | abx.HookSpecDecoratorThatReturnsListResults | abx.HookSpecDecoratorThatReturnsFirstResult
:canonical: abx.TypedHookspecMarker.__call__

```{autodoc2-docstring} abx.TypedHookspecMarker.__call__
```

````

`````

````{py:function} is_valid_attr_name(x: str) -> str
:canonical: abx.is_valid_attr_name

```{autodoc2-docstring} abx.is_valid_attr_name
```
````

````{py:function} is_valid_module_name(x: str) -> str
:canonical: abx.is_valid_module_name

```{autodoc2-docstring} abx.is_valid_module_name
```
````

````{py:data} AttrName
:canonical: abx.AttrName
:value: >
   None

```{autodoc2-docstring} abx.AttrName
```

````

````{py:data} PluginId
:canonical: abx.PluginId
:value: >
   None

```{autodoc2-docstring} abx.PluginId
```

````

`````{py:class} PluginInfo()
:canonical: abx.PluginInfo

Bases: {py:obj}`typing.TypedDict`

````{py:attribute} id
:canonical: abx.PluginInfo.id
:type: abx.PluginId
:value: >
   None

```{autodoc2-docstring} abx.PluginInfo.id
```

````

````{py:attribute} package
:canonical: abx.PluginInfo.package
:type: abx.AttrName
:value: >
   None

```{autodoc2-docstring} abx.PluginInfo.package
```

````

````{py:attribute} label
:canonical: abx.PluginInfo.label
:type: str
:value: >
   None

```{autodoc2-docstring} abx.PluginInfo.label
```

````

````{py:attribute} version
:canonical: abx.PluginInfo.version
:type: str
:value: >
   None

```{autodoc2-docstring} abx.PluginInfo.version
```

````

````{py:attribute} author
:canonical: abx.PluginInfo.author
:type: str
:value: >
   None

```{autodoc2-docstring} abx.PluginInfo.author
```

````

````{py:attribute} homepage
:canonical: abx.PluginInfo.homepage
:type: str
:value: >
   None

```{autodoc2-docstring} abx.PluginInfo.homepage
```

````

````{py:attribute} dependencies
:canonical: abx.PluginInfo.dependencies
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} abx.PluginInfo.dependencies
```

````

````{py:attribute} source_code
:canonical: abx.PluginInfo.source_code
:type: str
:value: >
   None

```{autodoc2-docstring} abx.PluginInfo.source_code
```

````

````{py:attribute} hooks
:canonical: abx.PluginInfo.hooks
:type: typing.Dict[abx.AttrName, typing.Callable]
:value: >
   None

```{autodoc2-docstring} abx.PluginInfo.hooks
```

````

````{py:attribute} module
:canonical: abx.PluginInfo.module
:type: types.ModuleType
:value: >
   None

```{autodoc2-docstring} abx.PluginInfo.module
```

````

`````

````{py:data} PluginSpec
:canonical: abx.PluginSpec
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} abx.PluginSpec
```

````

`````{py:class} ABXPluginManager(project_name: str)
:canonical: abx.ABXPluginManager

Bases: {py:obj}`pluggy.PluginManager`, {py:obj}`typing.Generic`\[{py:obj}`abx.PluginSpec`\]

```{autodoc2-docstring} abx.ABXPluginManager
```

```{rubric} Initialization
```

```{autodoc2-docstring} abx.ABXPluginManager.__init__
```

````{py:attribute} hook
:canonical: abx.ABXPluginManager.hook
:type: abx.PluginSpec
:value: >
   None

```{autodoc2-docstring} abx.ABXPluginManager.hook
```

````

````{py:method} create_typed_hookcaller(name: str, module_or_class: typing.Type[abx.PluginSpec], spec_opts: pluggy.HookspecOpts) -> pluggy.HookCaller
:canonical: abx.ABXPluginManager.create_typed_hookcaller

```{autodoc2-docstring} abx.ABXPluginManager.create_typed_hookcaller
```

````

````{py:method} add_hookspecs(module_or_class: typing.Type[abx.PluginSpec]) -> None
:canonical: abx.ABXPluginManager.add_hookspecs

```{autodoc2-docstring} abx.ABXPluginManager.add_hookspecs
```

````

````{py:method} parse_hookimpl_opts(plugin, name: str) -> pluggy.HookimplOpts | None
:canonical: abx.ABXPluginManager.parse_hookimpl_opts

````

`````

````{py:data} pm
:canonical: abx.pm
:value: >
   'ABXPluginManager(...)'

```{autodoc2-docstring} abx.pm
```

````

````{py:function} get_plugin_order(plugin: abx.PluginId | pathlib.Path | types.ModuleType | typing.Type) -> typing.Tuple[int, pathlib.Path]
:canonical: abx.get_plugin_order

```{autodoc2-docstring} abx.get_plugin_order
```
````

````{py:function} get_plugin(plugin: abx.PluginId | types.ModuleType | typing.Type) -> abx.PluginInfo
:canonical: abx.get_plugin

```{autodoc2-docstring} abx.get_plugin
```
````

````{py:function} get_all_plugins() -> typing.Dict[abx.PluginId, abx.PluginInfo]
:canonical: abx.get_all_plugins

```{autodoc2-docstring} abx.get_all_plugins
```
````

````{py:function} get_all_hook_names() -> typing.Set[str]
:canonical: abx.get_all_hook_names

```{autodoc2-docstring} abx.get_all_hook_names
```
````

````{py:function} get_all_hook_specs() -> typing.Dict[str, typing.Dict[str, typing.Any]]
:canonical: abx.get_all_hook_specs

```{autodoc2-docstring} abx.get_all_hook_specs
```
````

````{py:function} find_plugins_in_dir(plugins_dir: pathlib.Path) -> typing.Dict[abx.PluginId, pathlib.Path]
:canonical: abx.find_plugins_in_dir

```{autodoc2-docstring} abx.find_plugins_in_dir
```
````

````{py:function} get_pip_installed_plugins(group: abx.PluginId = 'abx') -> typing.Dict[abx.PluginId, pathlib.Path]
:canonical: abx.get_pip_installed_plugins

```{autodoc2-docstring} abx.get_pip_installed_plugins
```
````

````{py:function} load_plugins(plugins: typing.Iterable[abx.PluginId | types.ModuleType | typing.Type] | typing.Dict[abx.PluginId, pathlib.Path])
:canonical: abx.load_plugins

```{autodoc2-docstring} abx.load_plugins
```
````

````{py:function} get_plugin_hooks(plugin: abx.PluginId | types.ModuleType | typing.Type | None) -> typing.Dict[abx.AttrName, typing.Callable]
:canonical: abx.get_plugin_hooks

```{autodoc2-docstring} abx.get_plugin_hooks
```
````

````{py:function} as_list(results: typing.List[typing.List[abx.ReturnT]]) -> typing.List[abx.ReturnT]
:canonical: abx.as_list

```{autodoc2-docstring} abx.as_list
```
````

````{py:function} as_dict(results: typing.List[typing.Dict[abx.PluginId, abx.ReturnT]]) -> typing.Dict[abx.PluginId, abx.ReturnT]
:canonical: abx.as_dict

```{autodoc2-docstring} abx.as_dict
```
````
