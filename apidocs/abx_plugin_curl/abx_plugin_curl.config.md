# {py:mod}`abx_plugin_curl.config`

```{py:module} abx_plugin_curl.config
```

```{autodoc2-docstring} abx_plugin_curl.config
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CurlConfig <abx_plugin_curl.config.CurlConfig>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <abx_plugin_curl.config.__package__>`
  - ```{autodoc2-docstring} abx_plugin_curl.config.__package__
    :summary:
    ```
* - {py:obj}`CURL_CONFIG <abx_plugin_curl.config.CURL_CONFIG>`
  - ```{autodoc2-docstring} abx_plugin_curl.config.CURL_CONFIG
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: abx_plugin_curl.config.__package__
:value: >
   'abx_plugin_curl'

```{autodoc2-docstring} abx_plugin_curl.config.__package__
```

````

`````{py:class} CurlConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | None = None, _cli_ignore_unknown_args: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: abx_plugin_curl.config.CurlConfig

Bases: {py:obj}`abx_spec_config.base_configset.BaseConfigSet`

````{py:attribute} SAVE_TITLE
:canonical: abx_plugin_curl.config.CurlConfig.SAVE_TITLE
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_curl.config.CurlConfig.SAVE_TITLE
```

````

````{py:attribute} SAVE_HEADERS
:canonical: abx_plugin_curl.config.CurlConfig.SAVE_HEADERS
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_curl.config.CurlConfig.SAVE_HEADERS
```

````

````{py:attribute} USE_CURL
:canonical: abx_plugin_curl.config.CurlConfig.USE_CURL
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_curl.config.CurlConfig.USE_CURL
```

````

````{py:attribute} CURL_BINARY
:canonical: abx_plugin_curl.config.CurlConfig.CURL_BINARY
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_curl.config.CurlConfig.CURL_BINARY
```

````

````{py:attribute} CURL_ARGS
:canonical: abx_plugin_curl.config.CurlConfig.CURL_ARGS
:type: typing.List[str]
:value: >
   ['--silent', '--location', '--compressed']

```{autodoc2-docstring} abx_plugin_curl.config.CurlConfig.CURL_ARGS
```

````

````{py:attribute} CURL_EXTRA_ARGS
:canonical: abx_plugin_curl.config.CurlConfig.CURL_EXTRA_ARGS
:type: typing.List[str]
:value: >
   []

```{autodoc2-docstring} abx_plugin_curl.config.CurlConfig.CURL_EXTRA_ARGS
```

````

````{py:attribute} CURL_TIMEOUT
:canonical: abx_plugin_curl.config.CurlConfig.CURL_TIMEOUT
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_curl.config.CurlConfig.CURL_TIMEOUT
```

````

````{py:attribute} CURL_CHECK_SSL_VALIDITY
:canonical: abx_plugin_curl.config.CurlConfig.CURL_CHECK_SSL_VALIDITY
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_curl.config.CurlConfig.CURL_CHECK_SSL_VALIDITY
```

````

````{py:attribute} CURL_USER_AGENT
:canonical: abx_plugin_curl.config.CurlConfig.CURL_USER_AGENT
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_curl.config.CurlConfig.CURL_USER_AGENT
```

````

````{py:attribute} CURL_COOKIES_FILE
:canonical: abx_plugin_curl.config.CurlConfig.CURL_COOKIES_FILE
:type: typing.Optional[pathlib.Path]
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_curl.config.CurlConfig.CURL_COOKIES_FILE
```

````

`````

````{py:data} CURL_CONFIG
:canonical: abx_plugin_curl.config.CURL_CONFIG
:value: >
   'CurlConfig(...)'

```{autodoc2-docstring} abx_plugin_curl.config.CURL_CONFIG
```

````
