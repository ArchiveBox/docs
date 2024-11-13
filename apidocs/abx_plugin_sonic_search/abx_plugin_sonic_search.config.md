# {py:mod}`abx_plugin_sonic_search.config`

```{py:module} abx_plugin_sonic_search.config
```

```{autodoc2-docstring} abx_plugin_sonic_search.config
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SonicConfig <abx_plugin_sonic_search.config.SonicConfig>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SONIC_LIB <abx_plugin_sonic_search.config.SONIC_LIB>`
  - ```{autodoc2-docstring} abx_plugin_sonic_search.config.SONIC_LIB
    :summary:
    ```
* - {py:obj}`SONIC_CONFIG <abx_plugin_sonic_search.config.SONIC_CONFIG>`
  - ```{autodoc2-docstring} abx_plugin_sonic_search.config.SONIC_CONFIG
    :summary:
    ```
````

### API

````{py:data} SONIC_LIB
:canonical: abx_plugin_sonic_search.config.SONIC_LIB
:value: >
   None

```{autodoc2-docstring} abx_plugin_sonic_search.config.SONIC_LIB
```

````

`````{py:class} SonicConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | None = None, _cli_ignore_unknown_args: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: abx_plugin_sonic_search.config.SonicConfig

Bases: {py:obj}`abx_spec_config.base_configset.BaseConfigSet`

````{py:attribute} SONIC_BINARY
:canonical: abx_plugin_sonic_search.config.SonicConfig.SONIC_BINARY
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_sonic_search.config.SonicConfig.SONIC_BINARY
```

````

````{py:attribute} SONIC_HOST
:canonical: abx_plugin_sonic_search.config.SonicConfig.SONIC_HOST
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_sonic_search.config.SonicConfig.SONIC_HOST
```

````

````{py:attribute} SONIC_PORT
:canonical: abx_plugin_sonic_search.config.SonicConfig.SONIC_PORT
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_sonic_search.config.SonicConfig.SONIC_PORT
```

````

````{py:attribute} SONIC_PASSWORD
:canonical: abx_plugin_sonic_search.config.SonicConfig.SONIC_PASSWORD
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_sonic_search.config.SonicConfig.SONIC_PASSWORD
```

````

````{py:attribute} SONIC_COLLECTION
:canonical: abx_plugin_sonic_search.config.SonicConfig.SONIC_COLLECTION
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_sonic_search.config.SonicConfig.SONIC_COLLECTION
```

````

````{py:attribute} SONIC_BUCKET
:canonical: abx_plugin_sonic_search.config.SonicConfig.SONIC_BUCKET
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_sonic_search.config.SonicConfig.SONIC_BUCKET
```

````

````{py:attribute} SONIC_MAX_CHUNK_LENGTH
:canonical: abx_plugin_sonic_search.config.SonicConfig.SONIC_MAX_CHUNK_LENGTH
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_sonic_search.config.SonicConfig.SONIC_MAX_CHUNK_LENGTH
```

````

````{py:attribute} SONIC_MAX_TEXT_LENGTH
:canonical: abx_plugin_sonic_search.config.SonicConfig.SONIC_MAX_TEXT_LENGTH
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_sonic_search.config.SonicConfig.SONIC_MAX_TEXT_LENGTH
```

````

````{py:attribute} SONIC_MAX_RETRIES
:canonical: abx_plugin_sonic_search.config.SonicConfig.SONIC_MAX_RETRIES
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_sonic_search.config.SonicConfig.SONIC_MAX_RETRIES
```

````

````{py:method} validate()
:canonical: abx_plugin_sonic_search.config.SonicConfig.validate

````

`````

````{py:data} SONIC_CONFIG
:canonical: abx_plugin_sonic_search.config.SONIC_CONFIG
:value: >
   'SonicConfig(...)'

```{autodoc2-docstring} abx_plugin_sonic_search.config.SONIC_CONFIG
```

````
