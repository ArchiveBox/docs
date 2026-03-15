# {py:mod}`archivebox.config.configset`

```{py:module} archivebox.config.configset
```

```{autodoc2-docstring} archivebox.config.configset
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IniConfigSettingsSource <archivebox.config.configset.IniConfigSettingsSource>`
  - ```{autodoc2-docstring} archivebox.config.configset.IniConfigSettingsSource
    :summary:
    ```
* - {py:obj}`BaseConfigSet <archivebox.config.configset.BaseConfigSet>`
  - ```{autodoc2-docstring} archivebox.config.configset.BaseConfigSet
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_config <archivebox.config.configset.get_config>`
  - ```{autodoc2-docstring} archivebox.config.configset.get_config
    :summary:
    ```
* - {py:obj}`get_flat_config <archivebox.config.configset.get_flat_config>`
  - ```{autodoc2-docstring} archivebox.config.configset.get_flat_config
    :summary:
    ```
* - {py:obj}`get_all_configs <archivebox.config.configset.get_all_configs>`
  - ```{autodoc2-docstring} archivebox.config.configset.get_all_configs
    :summary:
    ```
* - {py:obj}`_parse_env_value <archivebox.config.configset._parse_env_value>`
  - ```{autodoc2-docstring} archivebox.config.configset._parse_env_value
    :summary:
    ```
* - {py:obj}`get_worker_concurrency <archivebox.config.configset.get_worker_concurrency>`
  - ```{autodoc2-docstring} archivebox.config.configset.get_worker_concurrency
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DEFAULT_WORKER_CONCURRENCY <archivebox.config.configset.DEFAULT_WORKER_CONCURRENCY>`
  - ```{autodoc2-docstring} archivebox.config.configset.DEFAULT_WORKER_CONCURRENCY
    :summary:
    ```
````

### API

`````{py:class} IniConfigSettingsSource(settings_cls: type[pydantic_settings.main.BaseSettings])
:canonical: archivebox.config.configset.IniConfigSettingsSource

Bases: {py:obj}`pydantic_settings.PydanticBaseSettingsSource`

```{autodoc2-docstring} archivebox.config.configset.IniConfigSettingsSource
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.config.configset.IniConfigSettingsSource.__init__
```

````{py:method} get_field_value(field: typing.Any, field_name: str) -> typing.Tuple[typing.Any, str, bool]
:canonical: archivebox.config.configset.IniConfigSettingsSource.get_field_value

````

````{py:method} __call__() -> typing.Dict[str, typing.Any]
:canonical: archivebox.config.configset.IniConfigSettingsSource.__call__

```{autodoc2-docstring} archivebox.config.configset.IniConfigSettingsSource.__call__
```

````

````{py:method} _load_config_file() -> typing.Dict[str, typing.Any]
:canonical: archivebox.config.configset.IniConfigSettingsSource._load_config_file

```{autodoc2-docstring} archivebox.config.configset.IniConfigSettingsSource._load_config_file
```

````

`````

`````{py:class} BaseConfigSet(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_prefix_target: pydantic_settings.sources.EnvPrefixTarget | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_nested_max_split: int | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | typing.Literal[dual, toggle] | None = None, _cli_ignore_unknown_args: bool | None = None, _cli_kebab_case: bool | typing.Literal[all, no_enums] | None = None, _cli_shortcuts: collections.abc.Mapping[str, str | list[str]] | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, _build_sources: tuple[tuple[pydantic_settings.sources.PydanticBaseSettingsSource, ...], dict[str, typing.Any]] | None = None, **values: typing.Any)
:canonical: archivebox.config.configset.BaseConfigSet

Bases: {py:obj}`pydantic_settings.BaseSettings`

```{autodoc2-docstring} archivebox.config.configset.BaseConfigSet
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.config.configset.BaseConfigSet.__init__
```

````{py:attribute} model_config
:canonical: archivebox.config.configset.BaseConfigSet.model_config
:value: >
   'ConfigDict(...)'

```{autodoc2-docstring} archivebox.config.configset.BaseConfigSet.model_config
```

````

````{py:method} settings_customise_sources(settings_cls: typing.Type[pydantic_settings.BaseSettings], init_settings: pydantic_settings.PydanticBaseSettingsSource, env_settings: pydantic_settings.PydanticBaseSettingsSource, dotenv_settings: pydantic_settings.PydanticBaseSettingsSource, file_secret_settings: pydantic_settings.PydanticBaseSettingsSource) -> typing.Tuple[pydantic_settings.PydanticBaseSettingsSource, ...]
:canonical: archivebox.config.configset.BaseConfigSet.settings_customise_sources
:classmethod:

```{autodoc2-docstring} archivebox.config.configset.BaseConfigSet.settings_customise_sources
```

````

````{py:method} load_from_file(config_path: pathlib.Path) -> typing.Dict[str, str]
:canonical: archivebox.config.configset.BaseConfigSet.load_from_file
:classmethod:

```{autodoc2-docstring} archivebox.config.configset.BaseConfigSet.load_from_file
```

````

````{py:method} update_in_place(warn: bool = True, persist: bool = False, **kwargs) -> None
:canonical: archivebox.config.configset.BaseConfigSet.update_in_place

```{autodoc2-docstring} archivebox.config.configset.BaseConfigSet.update_in_place
```

````

`````

````{py:function} get_config(defaults: typing.Optional[typing.Dict] = None, persona: typing.Any = None, user: typing.Any = None, crawl: typing.Any = None, snapshot: typing.Any = None, archiveresult: typing.Any = None, machine: typing.Any = None) -> typing.Dict[str, typing.Any]
:canonical: archivebox.config.configset.get_config

```{autodoc2-docstring} archivebox.config.configset.get_config
```
````

````{py:function} get_flat_config() -> typing.Dict[str, typing.Any]
:canonical: archivebox.config.configset.get_flat_config

```{autodoc2-docstring} archivebox.config.configset.get_flat_config
```
````

````{py:function} get_all_configs() -> typing.Dict[str, archivebox.config.configset.BaseConfigSet]
:canonical: archivebox.config.configset.get_all_configs

```{autodoc2-docstring} archivebox.config.configset.get_all_configs
```
````

````{py:function} _parse_env_value(value: str, default: typing.Any = None) -> typing.Any
:canonical: archivebox.config.configset._parse_env_value

```{autodoc2-docstring} archivebox.config.configset._parse_env_value
```
````

````{py:data} DEFAULT_WORKER_CONCURRENCY
:canonical: archivebox.config.configset.DEFAULT_WORKER_CONCURRENCY
:value: >
   None

```{autodoc2-docstring} archivebox.config.configset.DEFAULT_WORKER_CONCURRENCY
```

````

````{py:function} get_worker_concurrency() -> typing.Dict[str, int]
:canonical: archivebox.config.configset.get_worker_concurrency

```{autodoc2-docstring} archivebox.config.configset.get_worker_concurrency
```
````
