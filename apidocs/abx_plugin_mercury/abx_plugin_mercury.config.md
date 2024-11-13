# {py:mod}`abx_plugin_mercury.config`

```{py:module} abx_plugin_mercury.config
```

```{autodoc2-docstring} abx_plugin_mercury.config
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`MercuryConfig <abx_plugin_mercury.config.MercuryConfig>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`MERCURY_CONFIG <abx_plugin_mercury.config.MERCURY_CONFIG>`
  - ```{autodoc2-docstring} abx_plugin_mercury.config.MERCURY_CONFIG
    :summary:
    ```
````

### API

`````{py:class} MercuryConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | None = None, _cli_ignore_unknown_args: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: abx_plugin_mercury.config.MercuryConfig

Bases: {py:obj}`abx_spec_config.base_configset.BaseConfigSet`

````{py:attribute} SAVE_MERCURY
:canonical: abx_plugin_mercury.config.MercuryConfig.SAVE_MERCURY
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_mercury.config.MercuryConfig.SAVE_MERCURY
```

````

````{py:attribute} MERCURY_BINARY
:canonical: abx_plugin_mercury.config.MercuryConfig.MERCURY_BINARY
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_mercury.config.MercuryConfig.MERCURY_BINARY
```

````

````{py:attribute} MERCURY_EXTRA_ARGS
:canonical: abx_plugin_mercury.config.MercuryConfig.MERCURY_EXTRA_ARGS
:type: typing.List[str]
:value: >
   []

```{autodoc2-docstring} abx_plugin_mercury.config.MercuryConfig.MERCURY_EXTRA_ARGS
```

````

````{py:attribute} SAVE_MERCURY_REQUISITES
:canonical: abx_plugin_mercury.config.MercuryConfig.SAVE_MERCURY_REQUISITES
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_mercury.config.MercuryConfig.SAVE_MERCURY_REQUISITES
```

````

````{py:attribute} MERCURY_RESTRICT_FILE_NAMES
:canonical: abx_plugin_mercury.config.MercuryConfig.MERCURY_RESTRICT_FILE_NAMES
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_mercury.config.MercuryConfig.MERCURY_RESTRICT_FILE_NAMES
```

````

````{py:attribute} MERCURY_TIMEOUT
:canonical: abx_plugin_mercury.config.MercuryConfig.MERCURY_TIMEOUT
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_mercury.config.MercuryConfig.MERCURY_TIMEOUT
```

````

````{py:attribute} MERCURY_CHECK_SSL_VALIDITY
:canonical: abx_plugin_mercury.config.MercuryConfig.MERCURY_CHECK_SSL_VALIDITY
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_mercury.config.MercuryConfig.MERCURY_CHECK_SSL_VALIDITY
```

````

````{py:attribute} MERCURY_USER_AGENT
:canonical: abx_plugin_mercury.config.MercuryConfig.MERCURY_USER_AGENT
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_mercury.config.MercuryConfig.MERCURY_USER_AGENT
```

````

````{py:attribute} MERCURY_COOKIES_FILE
:canonical: abx_plugin_mercury.config.MercuryConfig.MERCURY_COOKIES_FILE
:type: typing.Optional[pathlib.Path]
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_mercury.config.MercuryConfig.MERCURY_COOKIES_FILE
```

````

`````

````{py:data} MERCURY_CONFIG
:canonical: abx_plugin_mercury.config.MERCURY_CONFIG
:value: >
   'MercuryConfig(...)'

```{autodoc2-docstring} abx_plugin_mercury.config.MERCURY_CONFIG
```

````
