# {py:mod}`abx_plugin_sqlitefts_search.config`

```{py:module} abx_plugin_sqlitefts_search.config
```

```{autodoc2-docstring} abx_plugin_sqlitefts_search.config
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SqliteftsConfig <abx_plugin_sqlitefts_search.config.SqliteftsConfig>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SQLITEFTS_CONFIG <abx_plugin_sqlitefts_search.config.SQLITEFTS_CONFIG>`
  - ```{autodoc2-docstring} abx_plugin_sqlitefts_search.config.SQLITEFTS_CONFIG
    :summary:
    ```
````

### API

`````{py:class} SqliteftsConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | None = None, _cli_ignore_unknown_args: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: abx_plugin_sqlitefts_search.config.SqliteftsConfig

Bases: {py:obj}`abx_spec_config.base_configset.BaseConfigSet`

````{py:attribute} SQLITEFTS_SEPARATE_DATABASE
:canonical: abx_plugin_sqlitefts_search.config.SqliteftsConfig.SQLITEFTS_SEPARATE_DATABASE
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_sqlitefts_search.config.SqliteftsConfig.SQLITEFTS_SEPARATE_DATABASE
```

````

````{py:attribute} SQLITEFTS_TOKENIZERS
:canonical: abx_plugin_sqlitefts_search.config.SqliteftsConfig.SQLITEFTS_TOKENIZERS
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_sqlitefts_search.config.SqliteftsConfig.SQLITEFTS_TOKENIZERS
```

````

````{py:attribute} SQLITEFTS_MAX_LENGTH
:canonical: abx_plugin_sqlitefts_search.config.SqliteftsConfig.SQLITEFTS_MAX_LENGTH
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_sqlitefts_search.config.SqliteftsConfig.SQLITEFTS_MAX_LENGTH
```

````

````{py:attribute} SQLITEFTS_DB
:canonical: abx_plugin_sqlitefts_search.config.SqliteftsConfig.SQLITEFTS_DB
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_sqlitefts_search.config.SqliteftsConfig.SQLITEFTS_DB
```

````

````{py:attribute} SQLITEFTS_TABLE
:canonical: abx_plugin_sqlitefts_search.config.SqliteftsConfig.SQLITEFTS_TABLE
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_sqlitefts_search.config.SqliteftsConfig.SQLITEFTS_TABLE
```

````

````{py:attribute} SQLITEFTS_ID_TABLE
:canonical: abx_plugin_sqlitefts_search.config.SqliteftsConfig.SQLITEFTS_ID_TABLE
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_sqlitefts_search.config.SqliteftsConfig.SQLITEFTS_ID_TABLE
```

````

````{py:attribute} SQLITEFTS_COLUMN
:canonical: abx_plugin_sqlitefts_search.config.SqliteftsConfig.SQLITEFTS_COLUMN
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_sqlitefts_search.config.SqliteftsConfig.SQLITEFTS_COLUMN
```

````

````{py:method} validate()
:canonical: abx_plugin_sqlitefts_search.config.SqliteftsConfig.validate

````

````{py:property} get_connection
:canonical: abx_plugin_sqlitefts_search.config.SqliteftsConfig.get_connection
:type: typing.Callable[[], sqlite3.Connection]

```{autodoc2-docstring} abx_plugin_sqlitefts_search.config.SqliteftsConfig.get_connection
```

````

````{py:property} SQLITE_BIND
:canonical: abx_plugin_sqlitefts_search.config.SqliteftsConfig.SQLITE_BIND
:type: str

```{autodoc2-docstring} abx_plugin_sqlitefts_search.config.SqliteftsConfig.SQLITE_BIND
```

````

````{py:property} SQLITE_LIMIT_LENGTH
:canonical: abx_plugin_sqlitefts_search.config.SqliteftsConfig.SQLITE_LIMIT_LENGTH
:type: int

```{autodoc2-docstring} abx_plugin_sqlitefts_search.config.SqliteftsConfig.SQLITE_LIMIT_LENGTH
```

````

`````

````{py:data} SQLITEFTS_CONFIG
:canonical: abx_plugin_sqlitefts_search.config.SQLITEFTS_CONFIG
:value: >
   'SqliteftsConfig(...)'

```{autodoc2-docstring} abx_plugin_sqlitefts_search.config.SQLITEFTS_CONFIG
```

````
