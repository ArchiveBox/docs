# {py:mod}`abx_plugin_pocket.config`

```{py:module} abx_plugin_pocket.config
```

```{autodoc2-docstring} abx_plugin_pocket.config
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PocketConfig <abx_plugin_pocket.config.PocketConfig>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`POCKET_CONFIG <abx_plugin_pocket.config.POCKET_CONFIG>`
  - ```{autodoc2-docstring} abx_plugin_pocket.config.POCKET_CONFIG
    :summary:
    ```
````

### API

`````{py:class} PocketConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | None = None, _cli_ignore_unknown_args: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: abx_plugin_pocket.config.PocketConfig

Bases: {py:obj}`abx_spec_config.BaseConfigSet`

````{py:attribute} POCKET_CONSUMER_KEY
:canonical: abx_plugin_pocket.config.PocketConfig.POCKET_CONSUMER_KEY
:type: str | None
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_pocket.config.PocketConfig.POCKET_CONSUMER_KEY
```

````

````{py:attribute} POCKET_ACCESS_TOKENS
:canonical: abx_plugin_pocket.config.PocketConfig.POCKET_ACCESS_TOKENS
:type: typing.Dict[str, str]
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_pocket.config.PocketConfig.POCKET_ACCESS_TOKENS
```

````

`````

````{py:data} POCKET_CONFIG
:canonical: abx_plugin_pocket.config.POCKET_CONFIG
:value: >
   'PocketConfig(...)'

```{autodoc2-docstring} abx_plugin_pocket.config.POCKET_CONFIG
```

````
