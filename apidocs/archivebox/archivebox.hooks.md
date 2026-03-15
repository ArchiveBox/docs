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

* - {py:obj}`HookResult <archivebox.hooks.HookResult>`
  - ```{autodoc2-docstring} archivebox.hooks.HookResult
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`extract_step <archivebox.hooks.extract_step>`
  - ```{autodoc2-docstring} archivebox.hooks.extract_step
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
* - {py:obj}`run_hooks <archivebox.hooks.run_hooks>`
  - ```{autodoc2-docstring} archivebox.hooks.run_hooks
    :summary:
    ```
* - {py:obj}`get_plugins <archivebox.hooks.get_plugins>`
  - ```{autodoc2-docstring} archivebox.hooks.get_plugins
    :summary:
    ```
* - {py:obj}`get_parser_plugins <archivebox.hooks.get_parser_plugins>`
  - ```{autodoc2-docstring} archivebox.hooks.get_parser_plugins
    :summary:
    ```
* - {py:obj}`get_plugin_name <archivebox.hooks.get_plugin_name>`
  - ```{autodoc2-docstring} archivebox.hooks.get_plugin_name
    :summary:
    ```
* - {py:obj}`is_parser_plugin <archivebox.hooks.is_parser_plugin>`
  - ```{autodoc2-docstring} archivebox.hooks.is_parser_plugin
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
* - {py:obj}`get_config_defaults_from_plugins <archivebox.hooks.get_config_defaults_from_plugins>`
  - ```{autodoc2-docstring} archivebox.hooks.get_config_defaults_from_plugins
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
* - {py:obj}`get_all_plugin_icons <archivebox.hooks.get_all_plugin_icons>`
  - ```{autodoc2-docstring} archivebox.hooks.get_all_plugin_icons
    :summary:
    ```
* - {py:obj}`discover_plugin_templates <archivebox.hooks.discover_plugin_templates>`
  - ```{autodoc2-docstring} archivebox.hooks.discover_plugin_templates
    :summary:
    ```
* - {py:obj}`find_binary_for_cmd <archivebox.hooks.find_binary_for_cmd>`
  - ```{autodoc2-docstring} archivebox.hooks.find_binary_for_cmd
    :summary:
    ```
* - {py:obj}`create_model_record <archivebox.hooks.create_model_record>`
  - ```{autodoc2-docstring} archivebox.hooks.create_model_record
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

````{py:function} extract_step(hook_name: str) -> int
:canonical: archivebox.hooks.extract_step

```{autodoc2-docstring} archivebox.hooks.extract_step
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

````{py:function} iter_plugin_dirs() -> typing.List[pathlib.Path]
:canonical: archivebox.hooks.iter_plugin_dirs

```{autodoc2-docstring} archivebox.hooks.iter_plugin_dirs
```
````

`````{py:class} HookResult()
:canonical: archivebox.hooks.HookResult

Bases: {py:obj}`typing.TypedDict`

```{autodoc2-docstring} archivebox.hooks.HookResult
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.hooks.HookResult.__init__
```

````{py:attribute} returncode
:canonical: archivebox.hooks.HookResult.returncode
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.hooks.HookResult.returncode
```

````

````{py:attribute} stdout
:canonical: archivebox.hooks.HookResult.stdout
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.hooks.HookResult.stdout
```

````

````{py:attribute} stderr
:canonical: archivebox.hooks.HookResult.stderr
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.hooks.HookResult.stderr
```

````

````{py:attribute} output_json
:canonical: archivebox.hooks.HookResult.output_json
:type: typing.Optional[typing.Dict[str, typing.Any]]
:value: >
   None

```{autodoc2-docstring} archivebox.hooks.HookResult.output_json
```

````

````{py:attribute} output_files
:canonical: archivebox.hooks.HookResult.output_files
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} archivebox.hooks.HookResult.output_files
```

````

````{py:attribute} duration_ms
:canonical: archivebox.hooks.HookResult.duration_ms
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.hooks.HookResult.duration_ms
```

````

````{py:attribute} hook
:canonical: archivebox.hooks.HookResult.hook
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.hooks.HookResult.hook
```

````

````{py:attribute} plugin
:canonical: archivebox.hooks.HookResult.plugin
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.hooks.HookResult.plugin
```

````

````{py:attribute} hook_name
:canonical: archivebox.hooks.HookResult.hook_name
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.hooks.HookResult.hook_name
```

````

````{py:attribute} records
:canonical: archivebox.hooks.HookResult.records
:type: typing.List[typing.Dict[str, typing.Any]]
:value: >
   None

```{autodoc2-docstring} archivebox.hooks.HookResult.records
```

````

`````

````{py:function} discover_hooks(event_name: str, filter_disabled: bool = True, config: typing.Optional[typing.Dict[str, typing.Any]] = None) -> typing.List[pathlib.Path]
:canonical: archivebox.hooks.discover_hooks

```{autodoc2-docstring} archivebox.hooks.discover_hooks
```
````

````{py:function} run_hook(script: pathlib.Path, output_dir: pathlib.Path, config: typing.Dict[str, typing.Any], timeout: typing.Optional[int] = None, parent: typing.Optional[archivebox.machine.models.Process] = None, **kwargs: typing.Any) -> archivebox.machine.models.Process
:canonical: archivebox.hooks.run_hook

```{autodoc2-docstring} archivebox.hooks.run_hook
```
````

````{py:function} extract_records_from_process(process: Process) -> typing.List[typing.Dict[str, typing.Any]]
:canonical: archivebox.hooks.extract_records_from_process

```{autodoc2-docstring} archivebox.hooks.extract_records_from_process
```
````

````{py:function} collect_urls_from_plugins(snapshot_dir: pathlib.Path) -> typing.List[typing.Dict[str, typing.Any]]
:canonical: archivebox.hooks.collect_urls_from_plugins

```{autodoc2-docstring} archivebox.hooks.collect_urls_from_plugins
```
````

````{py:function} run_hooks(event_name: str, output_dir: pathlib.Path, config: typing.Dict[str, typing.Any], timeout: typing.Optional[int] = None, stop_on_failure: bool = False, **kwargs: typing.Any) -> typing.List[archivebox.hooks.HookResult]
:canonical: archivebox.hooks.run_hooks

```{autodoc2-docstring} archivebox.hooks.run_hooks
```
````

````{py:function} get_plugins() -> typing.List[str]
:canonical: archivebox.hooks.get_plugins

```{autodoc2-docstring} archivebox.hooks.get_plugins
```
````

````{py:function} get_parser_plugins() -> typing.List[str]
:canonical: archivebox.hooks.get_parser_plugins

```{autodoc2-docstring} archivebox.hooks.get_parser_plugins
```
````

````{py:function} get_plugin_name(plugin: str) -> str
:canonical: archivebox.hooks.get_plugin_name

```{autodoc2-docstring} archivebox.hooks.get_plugin_name
```
````

````{py:function} is_parser_plugin(plugin: str) -> bool
:canonical: archivebox.hooks.is_parser_plugin

```{autodoc2-docstring} archivebox.hooks.is_parser_plugin
```
````

````{py:function} get_enabled_plugins(config: typing.Optional[typing.Dict[str, typing.Any]] = None) -> typing.List[str]
:canonical: archivebox.hooks.get_enabled_plugins

```{autodoc2-docstring} archivebox.hooks.get_enabled_plugins
```
````

````{py:function} discover_plugins_that_provide_interface(module_name: str, required_attrs: typing.List[str], plugin_prefix: typing.Optional[str] = None) -> typing.Dict[str, typing.Any]
:canonical: archivebox.hooks.discover_plugins_that_provide_interface

```{autodoc2-docstring} archivebox.hooks.discover_plugins_that_provide_interface
```
````

````{py:function} get_search_backends() -> typing.Dict[str, typing.Any]
:canonical: archivebox.hooks.get_search_backends

```{autodoc2-docstring} archivebox.hooks.get_search_backends
```
````

````{py:function} discover_plugin_configs() -> typing.Dict[str, typing.Dict[str, typing.Any]]
:canonical: archivebox.hooks.discover_plugin_configs

```{autodoc2-docstring} archivebox.hooks.discover_plugin_configs
```
````

````{py:function} get_config_defaults_from_plugins() -> typing.Dict[str, typing.Any]
:canonical: archivebox.hooks.get_config_defaults_from_plugins

```{autodoc2-docstring} archivebox.hooks.get_config_defaults_from_plugins
```
````

````{py:function} get_plugin_special_config(plugin_name: str, config: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]
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

````{py:function} get_plugin_template(plugin: str, template_name: str, fallback: bool = True) -> typing.Optional[str]
:canonical: archivebox.hooks.get_plugin_template

```{autodoc2-docstring} archivebox.hooks.get_plugin_template
```
````

````{py:function} get_plugin_icon(plugin: str) -> str
:canonical: archivebox.hooks.get_plugin_icon

```{autodoc2-docstring} archivebox.hooks.get_plugin_icon
```
````

````{py:function} get_all_plugin_icons() -> typing.Dict[str, str]
:canonical: archivebox.hooks.get_all_plugin_icons

```{autodoc2-docstring} archivebox.hooks.get_all_plugin_icons
```
````

````{py:function} discover_plugin_templates() -> typing.Dict[str, typing.Dict[str, str]]
:canonical: archivebox.hooks.discover_plugin_templates

```{autodoc2-docstring} archivebox.hooks.discover_plugin_templates
```
````

````{py:function} find_binary_for_cmd(cmd: typing.List[str], machine_id: str) -> typing.Optional[str]
:canonical: archivebox.hooks.find_binary_for_cmd

```{autodoc2-docstring} archivebox.hooks.find_binary_for_cmd
```
````

````{py:function} create_model_record(record: typing.Dict[str, typing.Any]) -> typing.Any
:canonical: archivebox.hooks.create_model_record

```{autodoc2-docstring} archivebox.hooks.create_model_record
```
````

````{py:function} process_hook_records(records: typing.List[typing.Dict[str, typing.Any]], overrides: typing.Dict[str, typing.Any] = None) -> typing.Dict[str, int]
:canonical: archivebox.hooks.process_hook_records

```{autodoc2-docstring} archivebox.hooks.process_hook_records
```
````
