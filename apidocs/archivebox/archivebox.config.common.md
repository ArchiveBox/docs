# {py:mod}`archivebox.config.common`

```{py:module} archivebox.config.common
```

```{autodoc2-docstring} archivebox.config.common
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ShellConfig <archivebox.config.common.ShellConfig>`
  -
* - {py:obj}`StorageConfig <archivebox.config.common.StorageConfig>`
  -
* - {py:obj}`GeneralConfig <archivebox.config.common.GeneralConfig>`
  -
* - {py:obj}`ServerConfig <archivebox.config.common.ServerConfig>`
  -
* - {py:obj}`DatabaseConfig <archivebox.config.common.DatabaseConfig>`
  -
* - {py:obj}`ArchivingConfig <archivebox.config.common.ArchivingConfig>`
  -
* - {py:obj}`SearchBackendConfig <archivebox.config.common.SearchBackendConfig>`
  -
* - {py:obj}`ArchiveBoxBaseConfig <archivebox.config.common.ArchiveBoxBaseConfig>`
  - ```{autodoc2-docstring} archivebox.config.common.ArchiveBoxBaseConfig
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_legacy_bool <archivebox.config.common._legacy_bool>`
  - ```{autodoc2-docstring} archivebox.config.common._legacy_bool
    :summary:
    ```
* - {py:obj}`permissions_from_legacy_public_flags <archivebox.config.common.permissions_from_legacy_public_flags>`
  - ```{autodoc2-docstring} archivebox.config.common.permissions_from_legacy_public_flags
    :summary:
    ```
* - {py:obj}`is_sensitive_config_key <archivebox.config.common.is_sensitive_config_key>`
  - ```{autodoc2-docstring} archivebox.config.common.is_sensitive_config_key
    :summary:
    ```
* - {py:obj}`redact_sensitive_config <archivebox.config.common.redact_sensitive_config>`
  - ```{autodoc2-docstring} archivebox.config.common.redact_sensitive_config
    :summary:
    ```
* - {py:obj}`rprint <archivebox.config.common.rprint>`
  - ```{autodoc2-docstring} archivebox.config.common.rprint
    :summary:
    ```
* - {py:obj}`parse_delete_after <archivebox.config.common.parse_delete_after>`
  - ```{autodoc2-docstring} archivebox.config.common.parse_delete_after
    :summary:
    ```
* - {py:obj}`_plugin_user_config_value <archivebox.config.common._plugin_user_config_value>`
  - ```{autodoc2-docstring} archivebox.config.common._plugin_user_config_value
    :summary:
    ```
* - {py:obj}`_plugin_user_config <archivebox.config.common._plugin_user_config>`
  - ```{autodoc2-docstring} archivebox.config.common._plugin_user_config
    :summary:
    ```
* - {py:obj}`_discover_plugin_config_schemas <archivebox.config.common._discover_plugin_config_schemas>`
  - ```{autodoc2-docstring} archivebox.config.common._discover_plugin_config_schemas
    :summary:
    ```
* - {py:obj}`_plugin_config_properties <archivebox.config.common._plugin_config_properties>`
  - ```{autodoc2-docstring} archivebox.config.common._plugin_config_properties
    :summary:
    ```
* - {py:obj}`_plugin_config_model <archivebox.config.common._plugin_config_model>`
  - ```{autodoc2-docstring} archivebox.config.common._plugin_config_model
    :summary:
    ```
* - {py:obj}`_archivebox_config_input_names <archivebox.config.common._archivebox_config_input_names>`
  - ```{autodoc2-docstring} archivebox.config.common._archivebox_config_input_names
    :summary:
    ```
* - {py:obj}`_build_archivebox_config_model <archivebox.config.common._build_archivebox_config_model>`
  - ```{autodoc2-docstring} archivebox.config.common._build_archivebox_config_model
    :summary:
    ```
* - {py:obj}`get_config <archivebox.config.common.get_config>`
  - ```{autodoc2-docstring} archivebox.config.common.get_config
    :summary:
    ```
* - {py:obj}`get_all_configs <archivebox.config.common.get_all_configs>`
  - ```{autodoc2-docstring} archivebox.config.common.get_all_configs
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ConfigOverrides <archivebox.config.common.ConfigOverrides>`
  - ```{autodoc2-docstring} archivebox.config.common.ConfigOverrides
    :summary:
    ```
* - {py:obj}`ConfigPayload <archivebox.config.common.ConfigPayload>`
  - ```{autodoc2-docstring} archivebox.config.common.ConfigPayload
    :summary:
    ```
* - {py:obj}`PluginSchemaDocuments <archivebox.config.common.PluginSchemaDocuments>`
  - ```{autodoc2-docstring} archivebox.config.common.PluginSchemaDocuments
    :summary:
    ```
* - {py:obj}`_STDOUT_CONSOLE <archivebox.config.common._STDOUT_CONSOLE>`
  - ```{autodoc2-docstring} archivebox.config.common._STDOUT_CONSOLE
    :summary:
    ```
* - {py:obj}`_STDERR_CONSOLE <archivebox.config.common._STDERR_CONSOLE>`
  - ```{autodoc2-docstring} archivebox.config.common._STDERR_CONSOLE
    :summary:
    ```
* - {py:obj}`_WARNED_ARCHIVING_CONFIGS <archivebox.config.common._WARNED_ARCHIVING_CONFIGS>`
  - ```{autodoc2-docstring} archivebox.config.common._WARNED_ARCHIVING_CONFIGS
    :summary:
    ```
* - {py:obj}`_SENSITIVE_CONFIG_KEY_NEEDLES <archivebox.config.common._SENSITIVE_CONFIG_KEY_NEEDLES>`
  - ```{autodoc2-docstring} archivebox.config.common._SENSITIVE_CONFIG_KEY_NEEDLES
    :summary:
    ```
* - {py:obj}`SENSITIVE_CONFIG_VALUE_REDACTED <archivebox.config.common.SENSITIVE_CONFIG_VALUE_REDACTED>`
  - ```{autodoc2-docstring} archivebox.config.common.SENSITIVE_CONFIG_VALUE_REDACTED
    :summary:
    ```
* - {py:obj}`PLUGIN_CONFIG_SCHEMAS <archivebox.config.common.PLUGIN_CONFIG_SCHEMAS>`
  - ```{autodoc2-docstring} archivebox.config.common.PLUGIN_CONFIG_SCHEMAS
    :summary:
    ```
* - {py:obj}`ArchiveBoxConfig <archivebox.config.common.ArchiveBoxConfig>`
  - ```{autodoc2-docstring} archivebox.config.common.ArchiveBoxConfig
    :summary:
    ```
````

### API

````{py:data} ConfigOverrides
:canonical: archivebox.config.common.ConfigOverrides
:value: >
   None

```{autodoc2-docstring} archivebox.config.common.ConfigOverrides
```

````

````{py:data} ConfigPayload
:canonical: archivebox.config.common.ConfigPayload
:value: >
   None

```{autodoc2-docstring} archivebox.config.common.ConfigPayload
```

````

````{py:data} PluginSchemaDocuments
:canonical: archivebox.config.common.PluginSchemaDocuments
:value: >
   None

```{autodoc2-docstring} archivebox.config.common.PluginSchemaDocuments
```

````

````{py:data} _STDOUT_CONSOLE
:canonical: archivebox.config.common._STDOUT_CONSOLE
:value: >
   'Console(...)'

```{autodoc2-docstring} archivebox.config.common._STDOUT_CONSOLE
```

````

````{py:data} _STDERR_CONSOLE
:canonical: archivebox.config.common._STDERR_CONSOLE
:value: >
   'Console(...)'

```{autodoc2-docstring} archivebox.config.common._STDERR_CONSOLE
```

````

````{py:data} _WARNED_ARCHIVING_CONFIGS
:canonical: archivebox.config.common._WARNED_ARCHIVING_CONFIGS
:type: set[tuple[int, bool]]
:value: >
   'set(...)'

```{autodoc2-docstring} archivebox.config.common._WARNED_ARCHIVING_CONFIGS
```

````

````{py:function} _legacy_bool(value: object) -> bool | None
:canonical: archivebox.config.common._legacy_bool

```{autodoc2-docstring} archivebox.config.common._legacy_bool
```
````

````{py:function} permissions_from_legacy_public_flags(raw_config: collections.abc.Mapping[str, object]) -> str | None
:canonical: archivebox.config.common.permissions_from_legacy_public_flags

```{autodoc2-docstring} archivebox.config.common.permissions_from_legacy_public_flags
```
````

````{py:data} _SENSITIVE_CONFIG_KEY_NEEDLES
:canonical: archivebox.config.common._SENSITIVE_CONFIG_KEY_NEEDLES
:value: >
   ('TOKEN', 'SECRET', 'API_KEY', 'APIKEY', 'PASSWORD')

```{autodoc2-docstring} archivebox.config.common._SENSITIVE_CONFIG_KEY_NEEDLES
```

````

````{py:data} SENSITIVE_CONFIG_VALUE_REDACTED
:canonical: archivebox.config.common.SENSITIVE_CONFIG_VALUE_REDACTED
:value: >
   '********'

```{autodoc2-docstring} archivebox.config.common.SENSITIVE_CONFIG_VALUE_REDACTED
```

````

````{py:function} is_sensitive_config_key(key: str) -> bool
:canonical: archivebox.config.common.is_sensitive_config_key

```{autodoc2-docstring} archivebox.config.common.is_sensitive_config_key
```
````

````{py:function} redact_sensitive_config(config: collections.abc.Mapping[str, typing.Any] | None) -> dict[str, typing.Any]
:canonical: archivebox.config.common.redact_sensitive_config

```{autodoc2-docstring} archivebox.config.common.redact_sensitive_config
```
````

````{py:function} rprint(*args, file=None, **kwargs)
:canonical: archivebox.config.common.rprint

```{autodoc2-docstring} archivebox.config.common.rprint
```
````

`````{py:class} ShellConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_prefix_target: pydantic_settings.sources.EnvPrefixTarget | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_nested_max_split: int | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | typing.Literal[dual, toggle] | None = None, _cli_ignore_unknown_args: bool | None = None, _cli_kebab_case: bool | typing.Literal[all, no_enums] | None = None, _cli_shortcuts: collections.abc.Mapping[str, str | list[str]] | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, _build_sources: tuple[tuple[pydantic_settings.sources.PydanticBaseSettingsSource, ...], dict[str, typing.Any]] | None = None, **values: typing.Any)
:canonical: archivebox.config.common.ShellConfig

Bases: {py:obj}`archivebox.config.configset.BaseConfigSet`

````{py:attribute} toml_section_header
:canonical: archivebox.config.common.ShellConfig.toml_section_header
:type: str
:value: >
   'SHELL_CONFIG'

```{autodoc2-docstring} archivebox.config.common.ShellConfig.toml_section_header
```

````

````{py:attribute} DEBUG
:canonical: archivebox.config.common.ShellConfig.DEBUG
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ShellConfig.DEBUG
```

````

````{py:attribute} IS_TTY
:canonical: archivebox.config.common.ShellConfig.IS_TTY
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ShellConfig.IS_TTY
```

````

````{py:attribute} USE_COLOR
:canonical: archivebox.config.common.ShellConfig.USE_COLOR
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ShellConfig.USE_COLOR
```

````

````{py:attribute} SHOW_PROGRESS
:canonical: archivebox.config.common.ShellConfig.SHOW_PROGRESS
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ShellConfig.SHOW_PROGRESS
```

````

````{py:attribute} IN_DOCKER
:canonical: archivebox.config.common.ShellConfig.IN_DOCKER
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ShellConfig.IN_DOCKER
```

````

````{py:attribute} IN_QEMU
:canonical: archivebox.config.common.ShellConfig.IN_QEMU
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ShellConfig.IN_QEMU
```

````

````{py:attribute} ANSI
:canonical: archivebox.config.common.ShellConfig.ANSI
:type: dict[str, str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ShellConfig.ANSI
```

````

````{py:property} TERM_WIDTH
:canonical: archivebox.config.common.ShellConfig.TERM_WIDTH
:type: int

```{autodoc2-docstring} archivebox.config.common.ShellConfig.TERM_WIDTH
```

````

````{py:property} COMMIT_HASH
:canonical: archivebox.config.common.ShellConfig.COMMIT_HASH
:type: str | None

```{autodoc2-docstring} archivebox.config.common.ShellConfig.COMMIT_HASH
```

````

````{py:property} BUILD_TIME
:canonical: archivebox.config.common.ShellConfig.BUILD_TIME
:type: str

```{autodoc2-docstring} archivebox.config.common.ShellConfig.BUILD_TIME
```

````

`````

`````{py:class} StorageConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_prefix_target: pydantic_settings.sources.EnvPrefixTarget | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_nested_max_split: int | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | typing.Literal[dual, toggle] | None = None, _cli_ignore_unknown_args: bool | None = None, _cli_kebab_case: bool | typing.Literal[all, no_enums] | None = None, _cli_shortcuts: collections.abc.Mapping[str, str | list[str]] | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, _build_sources: tuple[tuple[pydantic_settings.sources.PydanticBaseSettingsSource, ...], dict[str, typing.Any]] | None = None, **values: typing.Any)
:canonical: archivebox.config.common.StorageConfig

Bases: {py:obj}`archivebox.config.configset.BaseConfigSet`

````{py:attribute} toml_section_header
:canonical: archivebox.config.common.StorageConfig.toml_section_header
:type: str
:value: >
   'STORAGE_CONFIG'

```{autodoc2-docstring} archivebox.config.common.StorageConfig.toml_section_header
```

````

````{py:attribute} ARCHIVE_DIR
:canonical: archivebox.config.common.StorageConfig.ARCHIVE_DIR
:type: pathlib.Path
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.StorageConfig.ARCHIVE_DIR
```

````

````{py:attribute} USERS_DIR
:canonical: archivebox.config.common.StorageConfig.USERS_DIR
:type: pathlib.Path
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.StorageConfig.USERS_DIR
```

````

````{py:attribute} PERSONAS_DIR
:canonical: archivebox.config.common.StorageConfig.PERSONAS_DIR
:type: pathlib.Path
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.StorageConfig.PERSONAS_DIR
```

````

````{py:attribute} TMP_DIR
:canonical: archivebox.config.common.StorageConfig.TMP_DIR
:type: pathlib.Path
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.StorageConfig.TMP_DIR
```

````

````{py:attribute} LIB_DIR
:canonical: archivebox.config.common.StorageConfig.LIB_DIR
:type: pathlib.Path
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.StorageConfig.LIB_DIR
```

````

````{py:attribute} LIB_BIN_DIR
:canonical: archivebox.config.common.StorageConfig.LIB_BIN_DIR
:type: pathlib.Path
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.StorageConfig.LIB_BIN_DIR
```

````

````{py:attribute} CUSTOM_TEMPLATES_DIR
:canonical: archivebox.config.common.StorageConfig.CUSTOM_TEMPLATES_DIR
:type: pathlib.Path
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.StorageConfig.CUSTOM_TEMPLATES_DIR
```

````

````{py:attribute} OUTPUT_PERMISSIONS
:canonical: archivebox.config.common.StorageConfig.OUTPUT_PERMISSIONS
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.StorageConfig.OUTPUT_PERMISSIONS
```

````

````{py:attribute} ENFORCE_ATOMIC_WRITES
:canonical: archivebox.config.common.StorageConfig.ENFORCE_ATOMIC_WRITES
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.StorageConfig.ENFORCE_ATOMIC_WRITES
```

````

````{py:attribute} ALLOW_NO_UNIX_SOCKETS
:canonical: archivebox.config.common.StorageConfig.ALLOW_NO_UNIX_SOCKETS
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.StorageConfig.ALLOW_NO_UNIX_SOCKETS
```

````

`````

`````{py:class} GeneralConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_prefix_target: pydantic_settings.sources.EnvPrefixTarget | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_nested_max_split: int | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | typing.Literal[dual, toggle] | None = None, _cli_ignore_unknown_args: bool | None = None, _cli_kebab_case: bool | typing.Literal[all, no_enums] | None = None, _cli_shortcuts: collections.abc.Mapping[str, str | list[str]] | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, _build_sources: tuple[tuple[pydantic_settings.sources.PydanticBaseSettingsSource, ...], dict[str, typing.Any]] | None = None, **values: typing.Any)
:canonical: archivebox.config.common.GeneralConfig

Bases: {py:obj}`archivebox.config.configset.BaseConfigSet`

````{py:attribute} toml_section_header
:canonical: archivebox.config.common.GeneralConfig.toml_section_header
:type: str
:value: >
   'GENERAL_CONFIG'

```{autodoc2-docstring} archivebox.config.common.GeneralConfig.toml_section_header
```

````

````{py:attribute} TAG_SEPARATOR_PATTERN
:canonical: archivebox.config.common.GeneralConfig.TAG_SEPARATOR_PATTERN
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.GeneralConfig.TAG_SEPARATOR_PATTERN
```

````

`````

`````{py:class} ServerConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_prefix_target: pydantic_settings.sources.EnvPrefixTarget | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_nested_max_split: int | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | typing.Literal[dual, toggle] | None = None, _cli_ignore_unknown_args: bool | None = None, _cli_kebab_case: bool | typing.Literal[all, no_enums] | None = None, _cli_shortcuts: collections.abc.Mapping[str, str | list[str]] | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, _build_sources: tuple[tuple[pydantic_settings.sources.PydanticBaseSettingsSource, ...], dict[str, typing.Any]] | None = None, **values: typing.Any)
:canonical: archivebox.config.common.ServerConfig

Bases: {py:obj}`archivebox.config.configset.BaseConfigSet`

````{py:attribute} toml_section_header
:canonical: archivebox.config.common.ServerConfig.toml_section_header
:type: str
:value: >
   'SERVER_CONFIG'

```{autodoc2-docstring} archivebox.config.common.ServerConfig.toml_section_header
```

````

````{py:attribute} SERVER_SECURITY_MODES
:canonical: archivebox.config.common.ServerConfig.SERVER_SECURITY_MODES
:type: typing.ClassVar[tuple[str, ...]]
:value: >
   ('safe-subdomains-fullreplay', 'safe-onedomain-nojsreplay', 'unsafe-onedomain-noadmin', 'danger-oned...

```{autodoc2-docstring} archivebox.config.common.ServerConfig.SERVER_SECURITY_MODES
```

````

````{py:attribute} SECRET_KEY
:canonical: archivebox.config.common.ServerConfig.SECRET_KEY
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ServerConfig.SECRET_KEY
```

````

````{py:attribute} BIND_ADDR
:canonical: archivebox.config.common.ServerConfig.BIND_ADDR
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ServerConfig.BIND_ADDR
```

````

````{py:attribute} BASE_URL
:canonical: archivebox.config.common.ServerConfig.BASE_URL
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ServerConfig.BASE_URL
```

````

````{py:attribute} ALLOWED_HOSTS
:canonical: archivebox.config.common.ServerConfig.ALLOWED_HOSTS
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ServerConfig.ALLOWED_HOSTS
```

````

````{py:attribute} CSRF_TRUSTED_ORIGINS
:canonical: archivebox.config.common.ServerConfig.CSRF_TRUSTED_ORIGINS
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ServerConfig.CSRF_TRUSTED_ORIGINS
```

````

````{py:attribute} SERVER_SECURITY_MODE
:canonical: archivebox.config.common.ServerConfig.SERVER_SECURITY_MODE
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ServerConfig.SERVER_SECURITY_MODE
```

````

````{py:attribute} SNAPSHOTS_PER_PAGE
:canonical: archivebox.config.common.ServerConfig.SNAPSHOTS_PER_PAGE
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ServerConfig.SNAPSHOTS_PER_PAGE
```

````

````{py:attribute} FOOTER_INFO
:canonical: archivebox.config.common.ServerConfig.FOOTER_INFO
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ServerConfig.FOOTER_INFO
```

````

````{py:attribute} PUBLIC_INDEX
:canonical: archivebox.config.common.ServerConfig.PUBLIC_INDEX
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ServerConfig.PUBLIC_INDEX
```

````

````{py:attribute} PUBLIC_ADD_VIEW
:canonical: archivebox.config.common.ServerConfig.PUBLIC_ADD_VIEW
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ServerConfig.PUBLIC_ADD_VIEW
```

````

````{py:attribute} ADMIN_USERNAME
:canonical: archivebox.config.common.ServerConfig.ADMIN_USERNAME
:type: str | None
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ServerConfig.ADMIN_USERNAME
```

````

````{py:attribute} ADMIN_PASSWORD
:canonical: archivebox.config.common.ServerConfig.ADMIN_PASSWORD
:type: str | None
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ServerConfig.ADMIN_PASSWORD
```

````

````{py:attribute} REVERSE_PROXY_USER_HEADER
:canonical: archivebox.config.common.ServerConfig.REVERSE_PROXY_USER_HEADER
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ServerConfig.REVERSE_PROXY_USER_HEADER
```

````

````{py:attribute} REVERSE_PROXY_WHITELIST
:canonical: archivebox.config.common.ServerConfig.REVERSE_PROXY_WHITELIST
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ServerConfig.REVERSE_PROXY_WHITELIST
```

````

````{py:attribute} LOGOUT_REDIRECT_URL
:canonical: archivebox.config.common.ServerConfig.LOGOUT_REDIRECT_URL
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ServerConfig.LOGOUT_REDIRECT_URL
```

````

````{py:method} validate_server_security_mode(v: str) -> str
:canonical: archivebox.config.common.ServerConfig.validate_server_security_mode

```{autodoc2-docstring} archivebox.config.common.ServerConfig.validate_server_security_mode
```

````

````{py:property} USES_SUBDOMAIN_ROUTING
:canonical: archivebox.config.common.ServerConfig.USES_SUBDOMAIN_ROUTING
:type: bool

```{autodoc2-docstring} archivebox.config.common.ServerConfig.USES_SUBDOMAIN_ROUTING
```

````

````{py:property} ENABLES_FULL_JS_REPLAY
:canonical: archivebox.config.common.ServerConfig.ENABLES_FULL_JS_REPLAY
:type: bool

```{autodoc2-docstring} archivebox.config.common.ServerConfig.ENABLES_FULL_JS_REPLAY
```

````

````{py:property} CONTROL_PLANE_ENABLED
:canonical: archivebox.config.common.ServerConfig.CONTROL_PLANE_ENABLED
:type: bool

```{autodoc2-docstring} archivebox.config.common.ServerConfig.CONTROL_PLANE_ENABLED
```

````

````{py:property} BLOCK_UNSAFE_METHODS
:canonical: archivebox.config.common.ServerConfig.BLOCK_UNSAFE_METHODS
:type: bool

```{autodoc2-docstring} archivebox.config.common.ServerConfig.BLOCK_UNSAFE_METHODS
```

````

````{py:property} SHOULD_NEUTER_RISKY_REPLAY
:canonical: archivebox.config.common.ServerConfig.SHOULD_NEUTER_RISKY_REPLAY
:type: bool

```{autodoc2-docstring} archivebox.config.common.ServerConfig.SHOULD_NEUTER_RISKY_REPLAY
```

````

````{py:property} IS_UNSAFE_MODE
:canonical: archivebox.config.common.ServerConfig.IS_UNSAFE_MODE
:type: bool

```{autodoc2-docstring} archivebox.config.common.ServerConfig.IS_UNSAFE_MODE
```

````

````{py:property} IS_DANGEROUS_MODE
:canonical: archivebox.config.common.ServerConfig.IS_DANGEROUS_MODE
:type: bool

```{autodoc2-docstring} archivebox.config.common.ServerConfig.IS_DANGEROUS_MODE
```

````

````{py:property} IS_LOWER_SECURITY_MODE
:canonical: archivebox.config.common.ServerConfig.IS_LOWER_SECURITY_MODE
:type: bool

```{autodoc2-docstring} archivebox.config.common.ServerConfig.IS_LOWER_SECURITY_MODE
```

````

`````

`````{py:class} DatabaseConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_prefix_target: pydantic_settings.sources.EnvPrefixTarget | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_nested_max_split: int | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | typing.Literal[dual, toggle] | None = None, _cli_ignore_unknown_args: bool | None = None, _cli_kebab_case: bool | typing.Literal[all, no_enums] | None = None, _cli_shortcuts: collections.abc.Mapping[str, str | list[str]] | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, _build_sources: tuple[tuple[pydantic_settings.sources.PydanticBaseSettingsSource, ...], dict[str, typing.Any]] | None = None, **values: typing.Any)
:canonical: archivebox.config.common.DatabaseConfig

Bases: {py:obj}`archivebox.config.configset.BaseConfigSet`

````{py:attribute} toml_section_header
:canonical: archivebox.config.common.DatabaseConfig.toml_section_header
:type: str
:value: >
   'DATABASE_CONFIG'

```{autodoc2-docstring} archivebox.config.common.DatabaseConfig.toml_section_header
```

````

````{py:attribute} DATABASE_NAME
:canonical: archivebox.config.common.DatabaseConfig.DATABASE_NAME
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.DatabaseConfig.DATABASE_NAME
```

````

````{py:attribute} SQLITE_JOURNAL_MODE
:canonical: archivebox.config.common.DatabaseConfig.SQLITE_JOURNAL_MODE
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.DatabaseConfig.SQLITE_JOURNAL_MODE
```

````

````{py:attribute} SQLITE_MMAP_SIZE
:canonical: archivebox.config.common.DatabaseConfig.SQLITE_MMAP_SIZE
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.DatabaseConfig.SQLITE_MMAP_SIZE
```

````

````{py:attribute} SQLITE_BUSY_TIMEOUT
:canonical: archivebox.config.common.DatabaseConfig.SQLITE_BUSY_TIMEOUT
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.DatabaseConfig.SQLITE_BUSY_TIMEOUT
```

````

````{py:attribute} SQLITE_LOCK_RETRY_TIMEOUT
:canonical: archivebox.config.common.DatabaseConfig.SQLITE_LOCK_RETRY_TIMEOUT
:type: float
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.DatabaseConfig.SQLITE_LOCK_RETRY_TIMEOUT
```

````

````{py:attribute} SQLITE_LOCK_RETRY_INTERVAL
:canonical: archivebox.config.common.DatabaseConfig.SQLITE_LOCK_RETRY_INTERVAL
:type: float
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.DatabaseConfig.SQLITE_LOCK_RETRY_INTERVAL
```

````

`````

`````{py:class} ArchivingConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_prefix_target: pydantic_settings.sources.EnvPrefixTarget | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_nested_max_split: int | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | typing.Literal[dual, toggle] | None = None, _cli_ignore_unknown_args: bool | None = None, _cli_kebab_case: bool | typing.Literal[all, no_enums] | None = None, _cli_shortcuts: collections.abc.Mapping[str, str | list[str]] | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, _build_sources: tuple[tuple[pydantic_settings.sources.PydanticBaseSettingsSource, ...], dict[str, typing.Any]] | None = None, **values: typing.Any)
:canonical: archivebox.config.common.ArchivingConfig

Bases: {py:obj}`archivebox.config.configset.BaseConfigSet`

````{py:attribute} toml_section_header
:canonical: archivebox.config.common.ArchivingConfig.toml_section_header
:type: str
:value: >
   'ARCHIVING_CONFIG'

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.toml_section_header
```

````

````{py:attribute} PLUGINS
:canonical: archivebox.config.common.ArchivingConfig.PLUGINS
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.PLUGINS
```

````

````{py:attribute} ONLY_NEW
:canonical: archivebox.config.common.ArchivingConfig.ONLY_NEW
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.ONLY_NEW
```

````

````{py:attribute} TIMEOUT
:canonical: archivebox.config.common.ArchivingConfig.TIMEOUT
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.TIMEOUT
```

````

````{py:attribute} CRAWL_MAX_URLS
:canonical: archivebox.config.common.ArchivingConfig.CRAWL_MAX_URLS
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.CRAWL_MAX_URLS
```

````

````{py:attribute} CRAWL_MAX_SIZE
:canonical: archivebox.config.common.ArchivingConfig.CRAWL_MAX_SIZE
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.CRAWL_MAX_SIZE
```

````

````{py:attribute} CRAWL_TIMEOUT
:canonical: archivebox.config.common.ArchivingConfig.CRAWL_TIMEOUT
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.CRAWL_TIMEOUT
```

````

````{py:attribute} CRAWL_MAX_CONCURRENT_SNAPSHOTS
:canonical: archivebox.config.common.ArchivingConfig.CRAWL_MAX_CONCURRENT_SNAPSHOTS
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.CRAWL_MAX_CONCURRENT_SNAPSHOTS
```

````

````{py:attribute} SNAPSHOT_MAX_SIZE
:canonical: archivebox.config.common.ArchivingConfig.SNAPSHOT_MAX_SIZE
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.SNAPSHOT_MAX_SIZE
```

````

````{py:attribute} RESOLUTION
:canonical: archivebox.config.common.ArchivingConfig.RESOLUTION
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.RESOLUTION
```

````

````{py:attribute} CHECK_SSL_VALIDITY
:canonical: archivebox.config.common.ArchivingConfig.CHECK_SSL_VALIDITY
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.CHECK_SSL_VALIDITY
```

````

````{py:attribute} USER_AGENT
:canonical: archivebox.config.common.ArchivingConfig.USER_AGENT
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.USER_AGENT
```

````

````{py:attribute} COOKIES_FILE
:canonical: archivebox.config.common.ArchivingConfig.COOKIES_FILE
:type: pathlib.Path | None
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.COOKIES_FILE
```

````

````{py:attribute} URL_DENYLIST
:canonical: archivebox.config.common.ArchivingConfig.URL_DENYLIST
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.URL_DENYLIST
```

````

````{py:attribute} URL_ALLOWLIST
:canonical: archivebox.config.common.ArchivingConfig.URL_ALLOWLIST
:type: str | None
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.URL_ALLOWLIST
```

````

````{py:attribute} DEFAULT_PERSONA
:canonical: archivebox.config.common.ArchivingConfig.DEFAULT_PERSONA
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.DEFAULT_PERSONA
```

````

````{py:attribute} PERMISSIONS
:canonical: archivebox.config.common.ArchivingConfig.PERMISSIONS
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.PERMISSIONS
```

````

````{py:attribute} DELETE_AFTER
:canonical: archivebox.config.common.ArchivingConfig.DELETE_AFTER
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.DELETE_AFTER
```

````

````{py:method} warn_if_invalid() -> None
:canonical: archivebox.config.common.ArchivingConfig.warn_if_invalid

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.warn_if_invalid
```

````

````{py:method} validate_check_ssl_validity(v)
:canonical: archivebox.config.common.ArchivingConfig.validate_check_ssl_validity

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.validate_check_ssl_validity
```

````

````{py:method} validate_delete_after(value)
:canonical: archivebox.config.common.ArchivingConfig.validate_delete_after
:classmethod:

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.validate_delete_after
```

````

````{py:method} validate_permissions(value)
:canonical: archivebox.config.common.ArchivingConfig.validate_permissions
:classmethod:

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.validate_permissions
```

````

````{py:property} URL_ALLOWLIST_PTN
:canonical: archivebox.config.common.ArchivingConfig.URL_ALLOWLIST_PTN
:type: re.Pattern | None

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.URL_ALLOWLIST_PTN
```

````

````{py:property} URL_DENYLIST_PTN
:canonical: archivebox.config.common.ArchivingConfig.URL_DENYLIST_PTN
:type: re.Pattern

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.URL_DENYLIST_PTN
```

````

`````

````{py:function} parse_delete_after(value) -> datetime.timedelta | None
:canonical: archivebox.config.common.parse_delete_after

```{autodoc2-docstring} archivebox.config.common.parse_delete_after
```
````

`````{py:class} SearchBackendConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_prefix_target: pydantic_settings.sources.EnvPrefixTarget | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_nested_max_split: int | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | typing.Literal[dual, toggle] | None = None, _cli_ignore_unknown_args: bool | None = None, _cli_kebab_case: bool | typing.Literal[all, no_enums] | None = None, _cli_shortcuts: collections.abc.Mapping[str, str | list[str]] | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, _build_sources: tuple[tuple[pydantic_settings.sources.PydanticBaseSettingsSource, ...], dict[str, typing.Any]] | None = None, **values: typing.Any)
:canonical: archivebox.config.common.SearchBackendConfig

Bases: {py:obj}`archivebox.config.configset.BaseConfigSet`

````{py:attribute} toml_section_header
:canonical: archivebox.config.common.SearchBackendConfig.toml_section_header
:type: str
:value: >
   'SEARCH_BACKEND_CONFIG'

```{autodoc2-docstring} archivebox.config.common.SearchBackendConfig.toml_section_header
```

````

````{py:attribute} SEARCH_BACKEND_ENGINE
:canonical: archivebox.config.common.SearchBackendConfig.SEARCH_BACKEND_ENGINE
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.SearchBackendConfig.SEARCH_BACKEND_ENGINE
```

````

`````

````{py:function} _plugin_user_config_value(value: typing.Any) -> str
:canonical: archivebox.config.common._plugin_user_config_value

```{autodoc2-docstring} archivebox.config.common._plugin_user_config_value
```
````

````{py:function} _plugin_user_config(config: collections.abc.Mapping[str, object]) -> dict[str, str]
:canonical: archivebox.config.common._plugin_user_config

```{autodoc2-docstring} archivebox.config.common._plugin_user_config
```
````

````{py:function} _discover_plugin_config_schemas() -> archivebox.config.common.PluginSchemaDocuments
:canonical: archivebox.config.common._discover_plugin_config_schemas

```{autodoc2-docstring} archivebox.config.common._discover_plugin_config_schemas
```
````

````{py:function} _plugin_config_properties(plugin_schemas: archivebox.config.common.PluginSchemaDocuments) -> dict[str, dict[str, typing.Any]]
:canonical: archivebox.config.common._plugin_config_properties

```{autodoc2-docstring} archivebox.config.common._plugin_config_properties
```
````

````{py:function} _plugin_config_model(plugin_schemas: archivebox.config.common.PluginSchemaDocuments) -> type[pydantic.BaseModel]
:canonical: archivebox.config.common._plugin_config_model

```{autodoc2-docstring} archivebox.config.common._plugin_config_model
```
````

````{py:function} _archivebox_config_input_names() -> set[str]
:canonical: archivebox.config.common._archivebox_config_input_names

```{autodoc2-docstring} archivebox.config.common._archivebox_config_input_names
```
````

`````{py:class} ArchiveBoxBaseConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_prefix_target: pydantic_settings.sources.EnvPrefixTarget | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_nested_max_split: int | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | typing.Literal[dual, toggle] | None = None, _cli_ignore_unknown_args: bool | None = None, _cli_kebab_case: bool | typing.Literal[all, no_enums] | None = None, _cli_shortcuts: collections.abc.Mapping[str, str | list[str]] | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, _build_sources: tuple[tuple[pydantic_settings.sources.PydanticBaseSettingsSource, ...], dict[str, typing.Any]] | None = None, **values: typing.Any)
:canonical: archivebox.config.common.ArchiveBoxBaseConfig

Bases: {py:obj}`archivebox.config.common.ShellConfig`, {py:obj}`archivebox.config.common.StorageConfig`, {py:obj}`archivebox.config.common.GeneralConfig`, {py:obj}`archivebox.config.common.ServerConfig`, {py:obj}`archivebox.config.common.DatabaseConfig`, {py:obj}`archivebox.config.common.ArchivingConfig`, {py:obj}`archivebox.config.common.SearchBackendConfig`, {py:obj}`archivebox.config.ldap.LDAPConfig`

```{autodoc2-docstring} archivebox.config.common.ArchiveBoxBaseConfig
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.config.common.ArchiveBoxBaseConfig.__init__
```

````{py:attribute} model_config
:canonical: archivebox.config.common.ArchiveBoxBaseConfig.model_config
:value: >
   'SettingsConfigDict(...)'

```{autodoc2-docstring} archivebox.config.common.ArchiveBoxBaseConfig.model_config
```

````

````{py:attribute} DATA_DIR
:canonical: archivebox.config.common.ArchiveBoxBaseConfig.DATA_DIR
:type: pathlib.Path
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchiveBoxBaseConfig.DATA_DIR
```

````

````{py:attribute} ABX_RUNTIME
:canonical: archivebox.config.common.ArchiveBoxBaseConfig.ABX_RUNTIME
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchiveBoxBaseConfig.ABX_RUNTIME
```

````

````{py:attribute} CRAWL_DIR
:canonical: archivebox.config.common.ArchiveBoxBaseConfig.CRAWL_DIR
:type: pathlib.Path | None
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchiveBoxBaseConfig.CRAWL_DIR
```

````

````{py:attribute} SNAP_DIR
:canonical: archivebox.config.common.ArchiveBoxBaseConfig.SNAP_DIR
:type: pathlib.Path | None
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchiveBoxBaseConfig.SNAP_DIR
```

````

````{py:attribute} computed_config_keys
:canonical: archivebox.config.common.ArchiveBoxBaseConfig.computed_config_keys
:type: typing.ClassVar[tuple[str, ...]]
:value: >
   None

```{autodoc2-docstring} archivebox.config.common.ArchiveBoxBaseConfig.computed_config_keys
```

````

````{py:method} resolve_runtime_paths()
:canonical: archivebox.config.common.ArchiveBoxBaseConfig.resolve_runtime_paths

```{autodoc2-docstring} archivebox.config.common.ArchiveBoxBaseConfig.resolve_runtime_paths
```

````

`````

````{py:function} _build_archivebox_config_model(plugin_schemas: archivebox.config.common.PluginSchemaDocuments) -> type[archivebox.config.common.ArchiveBoxBaseConfig]
:canonical: archivebox.config.common._build_archivebox_config_model

```{autodoc2-docstring} archivebox.config.common._build_archivebox_config_model
```
````

````{py:data} PLUGIN_CONFIG_SCHEMAS
:canonical: archivebox.config.common.PLUGIN_CONFIG_SCHEMAS
:value: >
   '_discover_plugin_config_schemas(...)'

```{autodoc2-docstring} archivebox.config.common.PLUGIN_CONFIG_SCHEMAS
```

````

````{py:data} ArchiveBoxConfig
:canonical: archivebox.config.common.ArchiveBoxConfig
:value: >
   '_build_archivebox_config_model(...)'

```{autodoc2-docstring} archivebox.config.common.ArchiveBoxConfig
```

````

````{py:function} get_config(defaults: archivebox.config.common.ConfigOverrides | None = None, overrides: archivebox.config.common.ConfigOverrides | None = None, base_config: archivebox.config.common.ArchiveBoxBaseConfig | collections.abc.Mapping[str, object] | None = None, persona: typing.Any = None, user: typing.Any = None, crawl: typing.Any = None, snapshot: typing.Any = None, archiveresult: typing.Any = None, machine: typing.Any = None, include_machine: bool = True, resolve_plugins: bool = True) -> archivebox.config.common.ArchiveBoxBaseConfig
:canonical: archivebox.config.common.get_config

```{autodoc2-docstring} archivebox.config.common.get_config
```
````

````{py:function} get_all_configs() -> dict[str, archivebox.config.configset.BaseConfigSet]
:canonical: archivebox.config.common.get_all_configs

```{autodoc2-docstring} archivebox.config.common.get_all_configs
```
````
