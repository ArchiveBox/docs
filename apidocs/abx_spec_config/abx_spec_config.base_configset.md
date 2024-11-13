# {py:mod}`abx_spec_config.base_configset`

```{py:module} abx_spec_config.base_configset
```

```{autodoc2-docstring} abx_spec_config.base_configset
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`FlatTomlConfigSettingsSource <abx_spec_config.base_configset.FlatTomlConfigSettingsSource>`
  - ```{autodoc2-docstring} abx_spec_config.base_configset.FlatTomlConfigSettingsSource
    :summary:
    ```
* - {py:obj}`BaseConfigSet <abx_spec_config.base_configset.BaseConfigSet>`
  - ```{autodoc2-docstring} abx_spec_config.base_configset.BaseConfigSet
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`func_takes_args_or_kwargs <abx_spec_config.base_configset.func_takes_args_or_kwargs>`
  - ```{autodoc2-docstring} abx_spec_config.base_configset.func_takes_args_or_kwargs
    :summary:
    ```
* - {py:obj}`convert_ini_to_toml <abx_spec_config.base_configset.convert_ini_to_toml>`
  - ```{autodoc2-docstring} abx_spec_config.base_configset.convert_ini_to_toml
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AUTOFIXES_HEADER <abx_spec_config.base_configset.AUTOFIXES_HEADER>`
  - ```{autodoc2-docstring} abx_spec_config.base_configset.AUTOFIXES_HEADER
    :summary:
    ```
* - {py:obj}`AUTOFIXES_SUBHEADER <abx_spec_config.base_configset.AUTOFIXES_SUBHEADER>`
  - ```{autodoc2-docstring} abx_spec_config.base_configset.AUTOFIXES_SUBHEADER
    :summary:
    ```
* - {py:obj}`_ALREADY_WARNED_ABOUT_UPDATED_CONFIG <abx_spec_config.base_configset._ALREADY_WARNED_ABOUT_UPDATED_CONFIG>`
  - ```{autodoc2-docstring} abx_spec_config.base_configset._ALREADY_WARNED_ABOUT_UPDATED_CONFIG
    :summary:
    ```
* - {py:obj}`ConfigKeyStr <abx_spec_config.base_configset.ConfigKeyStr>`
  - ```{autodoc2-docstring} abx_spec_config.base_configset.ConfigKeyStr
    :summary:
    ```
````

### API

````{py:data} AUTOFIXES_HEADER
:canonical: abx_spec_config.base_configset.AUTOFIXES_HEADER
:value: >
   '[AUTOFIXES]'

```{autodoc2-docstring} abx_spec_config.base_configset.AUTOFIXES_HEADER
```

````

````{py:data} AUTOFIXES_SUBHEADER
:canonical: abx_spec_config.base_configset.AUTOFIXES_SUBHEADER
:value: >
   '# The following config was added automatically to fix problems detected at startup:'

```{autodoc2-docstring} abx_spec_config.base_configset.AUTOFIXES_SUBHEADER
```

````

````{py:data} _ALREADY_WARNED_ABOUT_UPDATED_CONFIG
:canonical: abx_spec_config.base_configset._ALREADY_WARNED_ABOUT_UPDATED_CONFIG
:value: >
   'set(...)'

```{autodoc2-docstring} abx_spec_config.base_configset._ALREADY_WARNED_ABOUT_UPDATED_CONFIG
```

````

````{py:data} ConfigKeyStr
:canonical: abx_spec_config.base_configset.ConfigKeyStr
:value: >
   None

```{autodoc2-docstring} abx_spec_config.base_configset.ConfigKeyStr
```

````

````{py:class} FlatTomlConfigSettingsSource(settings_cls: type[pydantic_settings.BaseSettings], toml_file: pathlib.Path | None = None)
:canonical: abx_spec_config.base_configset.FlatTomlConfigSettingsSource

Bases: {py:obj}`pydantic_settings.sources.TomlConfigSettingsSource`

```{autodoc2-docstring} abx_spec_config.base_configset.FlatTomlConfigSettingsSource
```

```{rubric} Initialization
```

```{autodoc2-docstring} abx_spec_config.base_configset.FlatTomlConfigSettingsSource.__init__
```

````

`````{py:class} BaseConfigSet(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | None = None, _cli_ignore_unknown_args: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: abx_spec_config.base_configset.BaseConfigSet

Bases: {py:obj}`pydantic_settings.BaseSettings`

```{autodoc2-docstring} abx_spec_config.base_configset.BaseConfigSet
```

```{rubric} Initialization
```

```{autodoc2-docstring} abx_spec_config.base_configset.BaseConfigSet.__init__
```

````{py:attribute} model_config
:canonical: abx_spec_config.base_configset.BaseConfigSet.model_config
:value: >
   'SettingsConfigDict(...)'

```{autodoc2-docstring} abx_spec_config.base_configset.BaseConfigSet.model_config
```

````

````{py:attribute} load_from_defaults
:canonical: abx_spec_config.base_configset.BaseConfigSet.load_from_defaults
:type: typing.ClassVar[bool]
:value: >
   True

```{autodoc2-docstring} abx_spec_config.base_configset.BaseConfigSet.load_from_defaults
```

````

````{py:attribute} load_from_system
:canonical: abx_spec_config.base_configset.BaseConfigSet.load_from_system
:type: typing.ClassVar[bool]
:value: >
   True

```{autodoc2-docstring} abx_spec_config.base_configset.BaseConfigSet.load_from_system
```

````

````{py:attribute} load_from_collection
:canonical: abx_spec_config.base_configset.BaseConfigSet.load_from_collection
:type: typing.ClassVar[bool]
:value: >
   True

```{autodoc2-docstring} abx_spec_config.base_configset.BaseConfigSet.load_from_collection
```

````

````{py:attribute} load_from_environment
:canonical: abx_spec_config.base_configset.BaseConfigSet.load_from_environment
:type: typing.ClassVar[bool]
:value: >
   True

```{autodoc2-docstring} abx_spec_config.base_configset.BaseConfigSet.load_from_environment
```

````

````{py:method} settings_customise_sources(settings_cls: typing.Type[pydantic_settings.BaseSettings], init_settings: pydantic_settings.PydanticBaseSettingsSource, env_settings: pydantic_settings.PydanticBaseSettingsSource, dotenv_settings: pydantic_settings.PydanticBaseSettingsSource, file_secret_settings: pydantic_settings.PydanticBaseSettingsSource) -> typing.Tuple[pydantic_settings.PydanticBaseSettingsSource, ...]
:canonical: abx_spec_config.base_configset.BaseConfigSet.settings_customise_sources
:classmethod:

```{autodoc2-docstring} abx_spec_config.base_configset.BaseConfigSet.settings_customise_sources
```

````

````{py:method} fill_defaults()
:canonical: abx_spec_config.base_configset.BaseConfigSet.fill_defaults

```{autodoc2-docstring} abx_spec_config.base_configset.BaseConfigSet.fill_defaults
```

````

````{py:method} validate()
:canonical: abx_spec_config.base_configset.BaseConfigSet.validate

```{autodoc2-docstring} abx_spec_config.base_configset.BaseConfigSet.validate
```

````

````{py:method} get_default_value(key: abx_spec_config.base_configset.ConfigKeyStr)
:canonical: abx_spec_config.base_configset.BaseConfigSet.get_default_value

```{autodoc2-docstring} abx_spec_config.base_configset.BaseConfigSet.get_default_value
```

````

````{py:method} update_in_place(warn=True, persist=False, hint='', **kwargs)
:canonical: abx_spec_config.base_configset.BaseConfigSet.update_in_place

```{autodoc2-docstring} abx_spec_config.base_configset.BaseConfigSet.update_in_place
```

````

````{py:property} aliases
:canonical: abx_spec_config.base_configset.BaseConfigSet.aliases
:type: typing.Dict[abx_spec_config.base_configset.ConfigKeyStr, abx_spec_config.base_configset.ConfigKeyStr]

```{autodoc2-docstring} abx_spec_config.base_configset.BaseConfigSet.aliases
```

````

````{py:property} toml_section_header
:canonical: abx_spec_config.base_configset.BaseConfigSet.toml_section_header

```{autodoc2-docstring} abx_spec_config.base_configset.BaseConfigSet.toml_section_header
```

````

````{py:method} from_defaults() -> typing.Dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.base_configset.BaseConfigSet.from_defaults

```{autodoc2-docstring} abx_spec_config.base_configset.BaseConfigSet.from_defaults
```

````

````{py:method} from_collection() -> typing.Dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.base_configset.BaseConfigSet.from_collection

```{autodoc2-docstring} abx_spec_config.base_configset.BaseConfigSet.from_collection
```

````

````{py:method} from_environment() -> typing.Dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.base_configset.BaseConfigSet.from_environment

```{autodoc2-docstring} abx_spec_config.base_configset.BaseConfigSet.from_environment
```

````

````{py:method} from_computed() -> typing.Dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.base_configset.BaseConfigSet.from_computed

```{autodoc2-docstring} abx_spec_config.base_configset.BaseConfigSet.from_computed
```

````

````{py:method} to_toml_dict(defaults=False) -> typing.Dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.base_configset.BaseConfigSet.to_toml_dict

```{autodoc2-docstring} abx_spec_config.base_configset.BaseConfigSet.to_toml_dict
```

````

````{py:method} to_toml_str(defaults=False) -> str
:canonical: abx_spec_config.base_configset.BaseConfigSet.to_toml_str

```{autodoc2-docstring} abx_spec_config.base_configset.BaseConfigSet.to_toml_str
```

````

`````

````{py:function} func_takes_args_or_kwargs(lambda_func: typing.Callable[..., typing.Any]) -> bool
:canonical: abx_spec_config.base_configset.func_takes_args_or_kwargs

```{autodoc2-docstring} abx_spec_config.base_configset.func_takes_args_or_kwargs
```
````

````{py:function} convert_ini_to_toml(ini_file: pathlib.Path)
:canonical: abx_spec_config.base_configset.convert_ini_to_toml

```{autodoc2-docstring} abx_spec_config.base_configset.convert_ini_to_toml
```
````
