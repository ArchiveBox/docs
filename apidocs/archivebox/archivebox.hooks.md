# {py:mod}`archivebox.hooks`

```{py:module} archivebox.hooks
```

```{autodoc2-docstring} archivebox.hooks
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ConfigLookup <archivebox.hooks.ConfigLookup>`
  -
* - {py:obj}`PluginSpecialConfig <archivebox.hooks.PluginSpecialConfig>`
  -
* - {py:obj}`ConfigDump <archivebox.hooks.ConfigDump>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_has_config_dump <archivebox.hooks._has_config_dump>`
  - ```{autodoc2-docstring} archivebox.hooks._has_config_dump
    :summary:
    ```
* - {py:obj}`_config_to_overrides <archivebox.hooks._config_to_overrides>`
  - ```{autodoc2-docstring} archivebox.hooks._config_to_overrides
    :summary:
    ```
* - {py:obj}`is_background_hook <archivebox.hooks.is_background_hook>`
  - ```{autodoc2-docstring} archivebox.hooks.is_background_hook
    :summary:
    ```
* - {py:obj}`is_finite_background_hook <archivebox.hooks.is_finite_background_hook>`
  - ```{autodoc2-docstring} archivebox.hooks.is_finite_background_hook
    :summary:
    ```
* - {py:obj}`iter_plugin_dirs <archivebox.hooks.iter_plugin_dirs>`
  - ```{autodoc2-docstring} archivebox.hooks.iter_plugin_dirs
    :summary:
    ```
* - {py:obj}`normalize_hook_event_name <archivebox.hooks.normalize_hook_event_name>`
  - ```{autodoc2-docstring} archivebox.hooks.normalize_hook_event_name
    :summary:
    ```
* - {py:obj}`_model_output_dir_from_child_path <archivebox.hooks._model_output_dir_from_child_path>`
  - ```{autodoc2-docstring} archivebox.hooks._model_output_dir_from_child_path
    :summary:
    ```
* - {py:obj}`discover_hooks <archivebox.hooks.discover_hooks>`
  - ```{autodoc2-docstring} archivebox.hooks.discover_hooks
    :summary:
    ```
* - {py:obj}`run_hook <archivebox.hooks.run_hook>`
  - ```{autodoc2-docstring} archivebox.hooks.run_hook
    :summary:
    ```
* - {py:obj}`extract_records_from_process <archivebox.hooks.extract_records_from_process>`
  - ```{autodoc2-docstring} archivebox.hooks.extract_records_from_process
    :summary:
    ```
* - {py:obj}`collect_urls_from_plugins <archivebox.hooks.collect_urls_from_plugins>`
  - ```{autodoc2-docstring} archivebox.hooks.collect_urls_from_plugins
    :summary:
    ```
* - {py:obj}`get_plugins <archivebox.hooks.get_plugins>`
  - ```{autodoc2-docstring} archivebox.hooks.get_plugins
    :summary:
    ```
* - {py:obj}`get_plugin_name <archivebox.hooks.get_plugin_name>`
  - ```{autodoc2-docstring} archivebox.hooks.get_plugin_name
    :summary:
    ```
* - {py:obj}`get_enabled_plugins <archivebox.hooks.get_enabled_plugins>`
  - ```{autodoc2-docstring} archivebox.hooks.get_enabled_plugins
    :summary:
    ```
* - {py:obj}`discover_plugins_that_provide_interface <archivebox.hooks.discover_plugins_that_provide_interface>`
  - ```{autodoc2-docstring} archivebox.hooks.discover_plugins_that_provide_interface
    :summary:
    ```
* - {py:obj}`get_search_backends <archivebox.hooks.get_search_backends>`
  - ```{autodoc2-docstring} archivebox.hooks.get_search_backends
    :summary:
    ```
* - {py:obj}`discover_plugin_configs <archivebox.hooks.discover_plugin_configs>`
  - ```{autodoc2-docstring} archivebox.hooks.discover_plugin_configs
    :summary:
    ```
* - {py:obj}`get_plugin_special_config <archivebox.hooks.get_plugin_special_config>`
  - ```{autodoc2-docstring} archivebox.hooks.get_plugin_special_config
    :summary:
    ```
* - {py:obj}`get_plugin_template <archivebox.hooks.get_plugin_template>`
  - ```{autodoc2-docstring} archivebox.hooks.get_plugin_template
    :summary:
    ```
* - {py:obj}`get_plugin_icon <archivebox.hooks.get_plugin_icon>`
  - ```{autodoc2-docstring} archivebox.hooks.get_plugin_icon
    :summary:
    ```
* - {py:obj}`process_hook_records <archivebox.hooks.process_hook_records>`
  - ```{autodoc2-docstring} archivebox.hooks.process_hook_records
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BUILTIN_PLUGINS_DIR <archivebox.hooks.BUILTIN_PLUGINS_DIR>`
  - ```{autodoc2-docstring} archivebox.hooks.BUILTIN_PLUGINS_DIR
    :summary:
    ```
* - {py:obj}`USER_PLUGINS_DIR <archivebox.hooks.USER_PLUGINS_DIR>`
  - ```{autodoc2-docstring} archivebox.hooks.USER_PLUGINS_DIR
    :summary:
    ```
* - {py:obj}`DEFAULT_TEMPLATES <archivebox.hooks.DEFAULT_TEMPLATES>`
  - ```{autodoc2-docstring} archivebox.hooks.DEFAULT_TEMPLATES
    :summary:
    ```
````

### API

`````{py:class} ConfigLookup
:canonical: archivebox.hooks.ConfigLookup

Bases: {py:obj}`typing.Protocol`

````{py:method} get(key: str, default: typing.Any = None) -> typing.Any
:canonical: archivebox.hooks.ConfigLookup.get

```{autodoc2-docstring} archivebox.hooks.ConfigLookup.get
```

````

````{py:method} items() -> collections.abc.Iterable[tuple[str, typing.Any]]
:canonical: archivebox.hooks.ConfigLookup.items

```{autodoc2-docstring} archivebox.hooks.ConfigLookup.items
```

````

`````

`````{py:class} PluginSpecialConfig()
:canonical: archivebox.hooks.PluginSpecialConfig

Bases: {py:obj}`typing.TypedDict`

````{py:attribute} enabled
:canonical: archivebox.hooks.PluginSpecialConfig.enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.hooks.PluginSpecialConfig.enabled
```

````

````{py:attribute} timeout
:canonical: archivebox.hooks.PluginSpecialConfig.timeout
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.hooks.PluginSpecialConfig.timeout
```

````

````{py:attribute} binary
:canonical: archivebox.hooks.PluginSpecialConfig.binary
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.hooks.PluginSpecialConfig.binary
```

````

`````

`````{py:class} ConfigDump
:canonical: archivebox.hooks.ConfigDump

Bases: {py:obj}`typing.Protocol`

````{py:method} as_dict() -> dict[str, typing.Any]
:canonical: archivebox.hooks.ConfigDump.as_dict

```{autodoc2-docstring} archivebox.hooks.ConfigDump.as_dict
```

````

`````

````{py:function} _has_config_dump(config: object) -> typing.TypeGuard[archivebox.hooks.ConfigDump]
:canonical: archivebox.hooks._has_config_dump

```{autodoc2-docstring} archivebox.hooks._has_config_dump
```
````

````{py:function} _config_to_overrides(config: archivebox.hooks.ConfigLookup | collections.abc.Mapping[str, typing.Any] | None) -> dict[str, typing.Any]
:canonical: archivebox.hooks._config_to_overrides

```{autodoc2-docstring} archivebox.hooks._config_to_overrides
```
````

````{py:data} BUILTIN_PLUGINS_DIR
:canonical: archivebox.hooks.BUILTIN_PLUGINS_DIR
:value: >
   'resolve(...)'

```{autodoc2-docstring} archivebox.hooks.BUILTIN_PLUGINS_DIR
```

````

````{py:data} USER_PLUGINS_DIR
:canonical: archivebox.hooks.USER_PLUGINS_DIR
:value: >
   'expanduser(...)'

```{autodoc2-docstring} archivebox.hooks.USER_PLUGINS_DIR
```

````

````{py:function} is_background_hook(hook_name: str) -> bool
:canonical: archivebox.hooks.is_background_hook

```{autodoc2-docstring} archivebox.hooks.is_background_hook
```
````

````{py:function} is_finite_background_hook(hook_name: str) -> bool
:canonical: archivebox.hooks.is_finite_background_hook

```{autodoc2-docstring} archivebox.hooks.is_finite_background_hook
```
````

````{py:function} iter_plugin_dirs() -> list[pathlib.Path]
:canonical: archivebox.hooks.iter_plugin_dirs

```{autodoc2-docstring} archivebox.hooks.iter_plugin_dirs
```
````

````{py:function} normalize_hook_event_name(event_name: str) -> str | None
:canonical: archivebox.hooks.normalize_hook_event_name

```{autodoc2-docstring} archivebox.hooks.normalize_hook_event_name
```
````

````{py:function} _model_output_dir_from_child_path(path: pathlib.Path, marker: str) -> pathlib.Path | None
:canonical: archivebox.hooks._model_output_dir_from_child_path

```{autodoc2-docstring} archivebox.hooks._model_output_dir_from_child_path
```
````

````{py:function} discover_hooks(event_name: str, filter_disabled: bool = True, config: archivebox.hooks.ConfigLookup | None = None, **config_kwargs: typing.Any) -> list[pathlib.Path]
:canonical: archivebox.hooks.discover_hooks

```{autodoc2-docstring} archivebox.hooks.discover_hooks
```
````

````{py:function} run_hook(script: pathlib.Path, output_dir: pathlib.Path, config: archivebox.hooks.ConfigLookup | collections.abc.Mapping[str, typing.Any] | None = None, timeout: int | None = None, parent: typing.Optional[archivebox.machine.models.Process] = None, **kwargs: typing.Any) -> archivebox.machine.models.Process
:canonical: archivebox.hooks.run_hook

```{autodoc2-docstring} archivebox.hooks.run_hook
```
````

````{py:function} extract_records_from_process(process: archivebox.machine.models.Process) -> list[dict[str, typing.Any]]
:canonical: archivebox.hooks.extract_records_from_process

```{autodoc2-docstring} archivebox.hooks.extract_records_from_process
```
````

````{py:function} collect_urls_from_plugins(snapshot_dir: pathlib.Path) -> list[dict[str, typing.Any]]
:canonical: archivebox.hooks.collect_urls_from_plugins

```{autodoc2-docstring} archivebox.hooks.collect_urls_from_plugins
```
````

````{py:function} get_plugins() -> list[str]
:canonical: archivebox.hooks.get_plugins

```{autodoc2-docstring} archivebox.hooks.get_plugins
```
````

````{py:function} get_plugin_name(plugin: str) -> str
:canonical: archivebox.hooks.get_plugin_name

```{autodoc2-docstring} archivebox.hooks.get_plugin_name
```
````

````{py:function} get_enabled_plugins(config: archivebox.hooks.ConfigLookup | None = None, **config_kwargs: typing.Any) -> list[str]
:canonical: archivebox.hooks.get_enabled_plugins

```{autodoc2-docstring} archivebox.hooks.get_enabled_plugins
```
````

````{py:function} discover_plugins_that_provide_interface(module_name: str, required_attrs: list[str], plugin_prefix: str | None = None) -> dict[str, typing.Any]
:canonical: archivebox.hooks.discover_plugins_that_provide_interface

```{autodoc2-docstring} archivebox.hooks.discover_plugins_that_provide_interface
```
````

````{py:function} get_search_backends() -> dict[str, typing.Any]
:canonical: archivebox.hooks.get_search_backends

```{autodoc2-docstring} archivebox.hooks.get_search_backends
```
````

````{py:function} discover_plugin_configs() -> dict[str, dict[str, typing.Any]]
:canonical: archivebox.hooks.discover_plugin_configs

```{autodoc2-docstring} archivebox.hooks.discover_plugin_configs
```
````

````{py:function} get_plugin_special_config(plugin_name: str, config: archivebox.hooks.ConfigLookup, _visited: set[str] | None = None) -> archivebox.hooks.PluginSpecialConfig
:canonical: archivebox.hooks.get_plugin_special_config

```{autodoc2-docstring} archivebox.hooks.get_plugin_special_config
```
````

````{py:data} DEFAULT_TEMPLATES
:canonical: archivebox.hooks.DEFAULT_TEMPLATES
:value: >
   None

```{autodoc2-docstring} archivebox.hooks.DEFAULT_TEMPLATES
```

````

````{py:function} get_plugin_template(plugin: str, template_name: str, fallback: bool = True) -> str | None
:canonical: archivebox.hooks.get_plugin_template

```{autodoc2-docstring} archivebox.hooks.get_plugin_template
```
````

````{py:function} get_plugin_icon(plugin: str) -> str
:canonical: archivebox.hooks.get_plugin_icon

```{autodoc2-docstring} archivebox.hooks.get_plugin_icon
```
````

````{py:function} process_hook_records(records: list[dict[str, typing.Any]], overrides: dict[str, typing.Any] | None = None) -> dict[str, int]
:canonical: archivebox.hooks.process_hook_records

```{autodoc2-docstring} archivebox.hooks.process_hook_records
```
````
