# {py:mod}`abx_plugin_pip.config`

```{py:module} abx_plugin_pip.config
```

```{autodoc2-docstring} abx_plugin_pip.config
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PipDependencyConfigs <abx_plugin_pip.config.PipDependencyConfigs>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PIP_CONFIG <abx_plugin_pip.config.PIP_CONFIG>`
  - ```{autodoc2-docstring} abx_plugin_pip.config.PIP_CONFIG
    :summary:
    ```
````

### API

`````{py:class} PipDependencyConfigs(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | None = None, _cli_ignore_unknown_args: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: abx_plugin_pip.config.PipDependencyConfigs

Bases: {py:obj}`abx_spec_config.base_configset.BaseConfigSet`

````{py:attribute} USE_PIP
:canonical: abx_plugin_pip.config.PipDependencyConfigs.USE_PIP
:type: bool
:value: >
   True

```{autodoc2-docstring} abx_plugin_pip.config.PipDependencyConfigs.USE_PIP
```

````

````{py:attribute} PIP_BINARY
:canonical: abx_plugin_pip.config.PipDependencyConfigs.PIP_BINARY
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_pip.config.PipDependencyConfigs.PIP_BINARY
```

````

````{py:attribute} PIP_ARGS
:canonical: abx_plugin_pip.config.PipDependencyConfigs.PIP_ARGS
:type: typing.Optional[typing.List[str]]
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_pip.config.PipDependencyConfigs.PIP_ARGS
```

````

````{py:attribute} PIP_EXTRA_ARGS
:canonical: abx_plugin_pip.config.PipDependencyConfigs.PIP_EXTRA_ARGS
:type: typing.List[str]
:value: >
   []

```{autodoc2-docstring} abx_plugin_pip.config.PipDependencyConfigs.PIP_EXTRA_ARGS
```

````

````{py:attribute} PIP_DEFAULT_ARGS
:canonical: abx_plugin_pip.config.PipDependencyConfigs.PIP_DEFAULT_ARGS
:type: typing.List[str]
:value: >
   []

```{autodoc2-docstring} abx_plugin_pip.config.PipDependencyConfigs.PIP_DEFAULT_ARGS
```

````

`````

````{py:data} PIP_CONFIG
:canonical: abx_plugin_pip.config.PIP_CONFIG
:value: >
   'PipDependencyConfigs(...)'

```{autodoc2-docstring} abx_plugin_pip.config.PIP_CONFIG
```

````
