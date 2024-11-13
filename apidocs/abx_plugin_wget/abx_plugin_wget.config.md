# {py:mod}`abx_plugin_wget.config`

```{py:module} abx_plugin_wget.config
```

```{autodoc2-docstring} abx_plugin_wget.config
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`WgetConfig <abx_plugin_wget.config.WgetConfig>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`WGET_CONFIG <abx_plugin_wget.config.WGET_CONFIG>`
  - ```{autodoc2-docstring} abx_plugin_wget.config.WGET_CONFIG
    :summary:
    ```
````

### API

`````{py:class} WgetConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | None = None, _cli_ignore_unknown_args: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: abx_plugin_wget.config.WgetConfig

Bases: {py:obj}`abx_spec_config.base_configset.BaseConfigSet`

````{py:attribute} SAVE_WGET
:canonical: abx_plugin_wget.config.WgetConfig.SAVE_WGET
:type: bool
:value: >
   True

```{autodoc2-docstring} abx_plugin_wget.config.WgetConfig.SAVE_WGET
```

````

````{py:attribute} SAVE_WARC
:canonical: abx_plugin_wget.config.WgetConfig.SAVE_WARC
:type: bool
:value: >
   True

```{autodoc2-docstring} abx_plugin_wget.config.WgetConfig.SAVE_WARC
```

````

````{py:attribute} USE_WGET
:canonical: abx_plugin_wget.config.WgetConfig.USE_WGET
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_wget.config.WgetConfig.USE_WGET
```

````

````{py:attribute} WGET_BINARY
:canonical: abx_plugin_wget.config.WgetConfig.WGET_BINARY
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_wget.config.WgetConfig.WGET_BINARY
```

````

````{py:attribute} WGET_ARGS
:canonical: abx_plugin_wget.config.WgetConfig.WGET_ARGS
:type: typing.List[str]
:value: >
   ['--no-verbose', '--adjust-extension', '--convert-links', '--force-directories', '--backup-converted...

```{autodoc2-docstring} abx_plugin_wget.config.WgetConfig.WGET_ARGS
```

````

````{py:attribute} WGET_EXTRA_ARGS
:canonical: abx_plugin_wget.config.WgetConfig.WGET_EXTRA_ARGS
:type: typing.List[str]
:value: >
   []

```{autodoc2-docstring} abx_plugin_wget.config.WgetConfig.WGET_EXTRA_ARGS
```

````

````{py:attribute} SAVE_WGET_REQUISITES
:canonical: abx_plugin_wget.config.WgetConfig.SAVE_WGET_REQUISITES
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_wget.config.WgetConfig.SAVE_WGET_REQUISITES
```

````

````{py:attribute} WGET_RESTRICT_FILE_NAMES
:canonical: abx_plugin_wget.config.WgetConfig.WGET_RESTRICT_FILE_NAMES
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_wget.config.WgetConfig.WGET_RESTRICT_FILE_NAMES
```

````

````{py:attribute} WGET_TIMEOUT
:canonical: abx_plugin_wget.config.WgetConfig.WGET_TIMEOUT
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_wget.config.WgetConfig.WGET_TIMEOUT
```

````

````{py:attribute} WGET_CHECK_SSL_VALIDITY
:canonical: abx_plugin_wget.config.WgetConfig.WGET_CHECK_SSL_VALIDITY
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_wget.config.WgetConfig.WGET_CHECK_SSL_VALIDITY
```

````

````{py:attribute} WGET_USER_AGENT
:canonical: abx_plugin_wget.config.WgetConfig.WGET_USER_AGENT
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_wget.config.WgetConfig.WGET_USER_AGENT
```

````

````{py:attribute} WGET_COOKIES_FILE
:canonical: abx_plugin_wget.config.WgetConfig.WGET_COOKIES_FILE
:type: typing.Optional[pathlib.Path]
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_wget.config.WgetConfig.WGET_COOKIES_FILE
```

````

````{py:method} validate()
:canonical: abx_plugin_wget.config.WgetConfig.validate

````

````{py:property} WGET_AUTO_COMPRESSION
:canonical: abx_plugin_wget.config.WgetConfig.WGET_AUTO_COMPRESSION
:type: bool

```{autodoc2-docstring} abx_plugin_wget.config.WgetConfig.WGET_AUTO_COMPRESSION
```

````

`````

````{py:data} WGET_CONFIG
:canonical: abx_plugin_wget.config.WGET_CONFIG
:value: >
   'WgetConfig(...)'

```{autodoc2-docstring} abx_plugin_wget.config.WGET_CONFIG
```

````
