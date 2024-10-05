# {py:mod}`archivebox.abx.archivebox.base_configset`

```{py:module} archivebox.abx.archivebox.base_configset
```

```{autodoc2-docstring} archivebox.abx.archivebox.base_configset
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`FlatTomlConfigSettingsSource <archivebox.abx.archivebox.base_configset.FlatTomlConfigSettingsSource>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.FlatTomlConfigSettingsSource
    :summary:
    ```
* - {py:obj}`ArchiveBoxBaseConfig <archivebox.abx.archivebox.base_configset.ArchiveBoxBaseConfig>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.ArchiveBoxBaseConfig
    :summary:
    ```
* - {py:obj}`BaseConfigSet <archivebox.abx.archivebox.base_configset.BaseConfigSet>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.abx.archivebox.base_configset.__package__>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.__package__
    :summary:
    ```
* - {py:obj}`PACKAGE_DIR <archivebox.abx.archivebox.base_configset.PACKAGE_DIR>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.PACKAGE_DIR
    :summary:
    ```
* - {py:obj}`DATA_DIR <archivebox.abx.archivebox.base_configset.DATA_DIR>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.DATA_DIR
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.abx.archivebox.base_configset.__package__
:value: >
   'abx.archivebox'

```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.__package__
```

````

````{py:data} PACKAGE_DIR
:canonical: archivebox.abx.archivebox.base_configset.PACKAGE_DIR
:value: >
   None

```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.PACKAGE_DIR
```

````

````{py:data} DATA_DIR
:canonical: archivebox.abx.archivebox.base_configset.DATA_DIR
:value: >
   'resolve(...)'

```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.DATA_DIR
```

````

````{py:class} FlatTomlConfigSettingsSource(settings_cls: type[pydantic_settings.BaseSettings], toml_file: pathlib.Path | None = None)
:canonical: archivebox.abx.archivebox.base_configset.FlatTomlConfigSettingsSource

Bases: {py:obj}`pydantic_settings.sources.TomlConfigSettingsSource`

```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.FlatTomlConfigSettingsSource
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.FlatTomlConfigSettingsSource.__init__
```

````

`````{py:class} ArchiveBoxBaseConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_implicit_flags: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.abx.archivebox.base_configset.ArchiveBoxBaseConfig

Bases: {py:obj}`pydantic_settings.BaseSettings`

```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.ArchiveBoxBaseConfig
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.ArchiveBoxBaseConfig.__init__
```

````{py:attribute} model_config
:canonical: archivebox.abx.archivebox.base_configset.ArchiveBoxBaseConfig.model_config
:value: >
   'SettingsConfigDict(...)'

```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.ArchiveBoxBaseConfig.model_config
```

````

````{py:attribute} load_from_defaults
:canonical: archivebox.abx.archivebox.base_configset.ArchiveBoxBaseConfig.load_from_defaults
:type: typing.ClassVar[bool]
:value: >
   True

```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.ArchiveBoxBaseConfig.load_from_defaults
```

````

````{py:attribute} load_from_configfile
:canonical: archivebox.abx.archivebox.base_configset.ArchiveBoxBaseConfig.load_from_configfile
:type: typing.ClassVar[bool]
:value: >
   True

```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.ArchiveBoxBaseConfig.load_from_configfile
```

````

````{py:attribute} load_from_environment
:canonical: archivebox.abx.archivebox.base_configset.ArchiveBoxBaseConfig.load_from_environment
:type: typing.ClassVar[bool]
:value: >
   True

```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.ArchiveBoxBaseConfig.load_from_environment
```

````

````{py:method} settings_customise_sources(settings_cls: typing.Type[pydantic_settings.BaseSettings], init_settings: pydantic_settings.PydanticBaseSettingsSource, env_settings: pydantic_settings.PydanticBaseSettingsSource, dotenv_settings: pydantic_settings.PydanticBaseSettingsSource, file_secret_settings: pydantic_settings.PydanticBaseSettingsSource) -> typing.Tuple[pydantic_settings.PydanticBaseSettingsSource, ...]
:canonical: archivebox.abx.archivebox.base_configset.ArchiveBoxBaseConfig.settings_customise_sources
:classmethod:

```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.ArchiveBoxBaseConfig.settings_customise_sources
```

````

````{py:method} fill_defaults()
:canonical: archivebox.abx.archivebox.base_configset.ArchiveBoxBaseConfig.fill_defaults

```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.ArchiveBoxBaseConfig.fill_defaults
```

````

````{py:method} update_in_place(warn=True, **kwargs)
:canonical: archivebox.abx.archivebox.base_configset.ArchiveBoxBaseConfig.update_in_place

```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.ArchiveBoxBaseConfig.update_in_place
```

````

````{py:method} as_legacy_config_schema()
:canonical: archivebox.abx.archivebox.base_configset.ArchiveBoxBaseConfig.as_legacy_config_schema

```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.ArchiveBoxBaseConfig.as_legacy_config_schema
```

````

`````

`````{py:class} BaseConfigSet(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_implicit_flags: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.abx.archivebox.base_configset.BaseConfigSet

Bases: {py:obj}`archivebox.abx.archivebox.base_configset.ArchiveBoxBaseConfig`, {py:obj}`archivebox.abx.archivebox.base_hook.BaseHook`

````{py:attribute} hook_type
:canonical: archivebox.abx.archivebox.base_configset.BaseConfigSet.hook_type
:type: typing.ClassVar[archivebox.abx.archivebox.base_hook.HookType]
:value: >
   'CONFIG'

```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.BaseConfigSet.hook_type
```

````

````{py:method} get_CONFIGS()
:canonical: archivebox.abx.archivebox.base_configset.BaseConfigSet.get_CONFIGS

```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.BaseConfigSet.get_CONFIGS
```

````

````{py:method} get_FLAT_CONFIG()
:canonical: archivebox.abx.archivebox.base_configset.BaseConfigSet.get_FLAT_CONFIG

```{autodoc2-docstring} archivebox.abx.archivebox.base_configset.BaseConfigSet.get_FLAT_CONFIG
```

````

`````
