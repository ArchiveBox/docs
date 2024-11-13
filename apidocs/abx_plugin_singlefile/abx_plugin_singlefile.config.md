# {py:mod}`abx_plugin_singlefile.config`

```{py:module} abx_plugin_singlefile.config
```

```{autodoc2-docstring} abx_plugin_singlefile.config
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SinglefileConfig <abx_plugin_singlefile.config.SinglefileConfig>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SINGLEFILE_CONFIG <abx_plugin_singlefile.config.SINGLEFILE_CONFIG>`
  - ```{autodoc2-docstring} abx_plugin_singlefile.config.SINGLEFILE_CONFIG
    :summary:
    ```
````

### API

`````{py:class} SinglefileConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | None = None, _cli_ignore_unknown_args: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: abx_plugin_singlefile.config.SinglefileConfig

Bases: {py:obj}`abx_spec_config.base_configset.BaseConfigSet`

````{py:attribute} SAVE_SINGLEFILE
:canonical: abx_plugin_singlefile.config.SinglefileConfig.SAVE_SINGLEFILE
:type: bool
:value: >
   True

```{autodoc2-docstring} abx_plugin_singlefile.config.SinglefileConfig.SAVE_SINGLEFILE
```

````

````{py:attribute} SINGLEFILE_USER_AGENT
:canonical: abx_plugin_singlefile.config.SinglefileConfig.SINGLEFILE_USER_AGENT
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_singlefile.config.SinglefileConfig.SINGLEFILE_USER_AGENT
```

````

````{py:attribute} SINGLEFILE_TIMEOUT
:canonical: abx_plugin_singlefile.config.SinglefileConfig.SINGLEFILE_TIMEOUT
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_singlefile.config.SinglefileConfig.SINGLEFILE_TIMEOUT
```

````

````{py:attribute} SINGLEFILE_CHECK_SSL_VALIDITY
:canonical: abx_plugin_singlefile.config.SinglefileConfig.SINGLEFILE_CHECK_SSL_VALIDITY
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_singlefile.config.SinglefileConfig.SINGLEFILE_CHECK_SSL_VALIDITY
```

````

````{py:attribute} SINGLEFILE_COOKIES_FILE
:canonical: abx_plugin_singlefile.config.SinglefileConfig.SINGLEFILE_COOKIES_FILE
:type: typing.Optional[pathlib.Path]
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_singlefile.config.SinglefileConfig.SINGLEFILE_COOKIES_FILE
```

````

````{py:attribute} SINGLEFILE_BINARY
:canonical: abx_plugin_singlefile.config.SinglefileConfig.SINGLEFILE_BINARY
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_singlefile.config.SinglefileConfig.SINGLEFILE_BINARY
```

````

````{py:attribute} SINGLEFILE_EXTRA_ARGS
:canonical: abx_plugin_singlefile.config.SinglefileConfig.SINGLEFILE_EXTRA_ARGS
:type: typing.List[str]
:value: >
   []

```{autodoc2-docstring} abx_plugin_singlefile.config.SinglefileConfig.SINGLEFILE_EXTRA_ARGS
```

````

`````

````{py:data} SINGLEFILE_CONFIG
:canonical: abx_plugin_singlefile.config.SINGLEFILE_CONFIG
:value: >
   'SinglefileConfig(...)'

```{autodoc2-docstring} abx_plugin_singlefile.config.SINGLEFILE_CONFIG
```

````
