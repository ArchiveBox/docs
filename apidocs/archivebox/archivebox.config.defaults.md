# {py:mod}`archivebox.config.defaults`

```{py:module} archivebox.config.defaults
```

```{autodoc2-docstring} archivebox.config.defaults
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ShellConfig <archivebox.config.defaults.ShellConfig>`
  -
* - {py:obj}`StorageConfig <archivebox.config.defaults.StorageConfig>`
  -
* - {py:obj}`GeneralConfig <archivebox.config.defaults.GeneralConfig>`
  -
* - {py:obj}`ServerConfig <archivebox.config.defaults.ServerConfig>`
  -
* - {py:obj}`ArchivingConfig <archivebox.config.defaults.ArchivingConfig>`
  -
* - {py:obj}`SearchBackendConfig <archivebox.config.defaults.SearchBackendConfig>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.config.defaults.__package__>`
  - ```{autodoc2-docstring} archivebox.config.defaults.__package__
    :summary:
    ```
* - {py:obj}`SHELL_CONFIG <archivebox.config.defaults.SHELL_CONFIG>`
  - ```{autodoc2-docstring} archivebox.config.defaults.SHELL_CONFIG
    :summary:
    ```
* - {py:obj}`STORAGE_CONFIG <archivebox.config.defaults.STORAGE_CONFIG>`
  - ```{autodoc2-docstring} archivebox.config.defaults.STORAGE_CONFIG
    :summary:
    ```
* - {py:obj}`GENERAL_CONFIG <archivebox.config.defaults.GENERAL_CONFIG>`
  - ```{autodoc2-docstring} archivebox.config.defaults.GENERAL_CONFIG
    :summary:
    ```
* - {py:obj}`SERVER_CONFIG <archivebox.config.defaults.SERVER_CONFIG>`
  - ```{autodoc2-docstring} archivebox.config.defaults.SERVER_CONFIG
    :summary:
    ```
* - {py:obj}`ARCHIVING_CONFIG <archivebox.config.defaults.ARCHIVING_CONFIG>`
  - ```{autodoc2-docstring} archivebox.config.defaults.ARCHIVING_CONFIG
    :summary:
    ```
* - {py:obj}`SEARCH_BACKEND_CONFIG <archivebox.config.defaults.SEARCH_BACKEND_CONFIG>`
  - ```{autodoc2-docstring} archivebox.config.defaults.SEARCH_BACKEND_CONFIG
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.config.defaults.__package__
:value: >
   'archivebox.config'

```{autodoc2-docstring} archivebox.config.defaults.__package__
```

````

`````{py:class} ShellConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_implicit_flags: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.config.defaults.ShellConfig

Bases: {py:obj}`abx.archivebox.base_configset.BaseConfigSet`

````{py:attribute} DEBUG
:canonical: archivebox.config.defaults.ShellConfig.DEBUG
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ShellConfig.DEBUG
```

````

````{py:attribute} IS_TTY
:canonical: archivebox.config.defaults.ShellConfig.IS_TTY
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ShellConfig.IS_TTY
```

````

````{py:attribute} USE_COLOR
:canonical: archivebox.config.defaults.ShellConfig.USE_COLOR
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ShellConfig.USE_COLOR
```

````

````{py:attribute} SHOW_PROGRESS
:canonical: archivebox.config.defaults.ShellConfig.SHOW_PROGRESS
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ShellConfig.SHOW_PROGRESS
```

````

````{py:attribute} IN_DOCKER
:canonical: archivebox.config.defaults.ShellConfig.IN_DOCKER
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ShellConfig.IN_DOCKER
```

````

````{py:attribute} IN_QEMU
:canonical: archivebox.config.defaults.ShellConfig.IN_QEMU
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ShellConfig.IN_QEMU
```

````

````{py:attribute} USER
:canonical: archivebox.config.defaults.ShellConfig.USER
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ShellConfig.USER
```

````

````{py:attribute} PUID
:canonical: archivebox.config.defaults.ShellConfig.PUID
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ShellConfig.PUID
```

````

````{py:attribute} PGID
:canonical: archivebox.config.defaults.ShellConfig.PGID
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ShellConfig.PGID
```

````

````{py:attribute} PYTHON_ENCODING
:canonical: archivebox.config.defaults.ShellConfig.PYTHON_ENCODING
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ShellConfig.PYTHON_ENCODING
```

````

````{py:attribute} ANSI
:canonical: archivebox.config.defaults.ShellConfig.ANSI
:type: typing.Dict[str, str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ShellConfig.ANSI
```

````

````{py:attribute} VERSIONS_AVAILABLE
:canonical: archivebox.config.defaults.ShellConfig.VERSIONS_AVAILABLE
:type: bool
:value: >
   False

```{autodoc2-docstring} archivebox.config.defaults.ShellConfig.VERSIONS_AVAILABLE
```

````

````{py:attribute} CAN_UPGRADE
:canonical: archivebox.config.defaults.ShellConfig.CAN_UPGRADE
:type: bool
:value: >
   False

```{autodoc2-docstring} archivebox.config.defaults.ShellConfig.CAN_UPGRADE
```

````

````{py:property} TERM_WIDTH
:canonical: archivebox.config.defaults.ShellConfig.TERM_WIDTH
:type: int

```{autodoc2-docstring} archivebox.config.defaults.ShellConfig.TERM_WIDTH
```

````

````{py:property} COMMIT_HASH
:canonical: archivebox.config.defaults.ShellConfig.COMMIT_HASH
:type: typing.Optional[str]

```{autodoc2-docstring} archivebox.config.defaults.ShellConfig.COMMIT_HASH
```

````

````{py:property} BUILD_TIME
:canonical: archivebox.config.defaults.ShellConfig.BUILD_TIME
:type: str

```{autodoc2-docstring} archivebox.config.defaults.ShellConfig.BUILD_TIME
```

````

````{py:method} validate_not_running_as_root()
:canonical: archivebox.config.defaults.ShellConfig.validate_not_running_as_root

```{autodoc2-docstring} archivebox.config.defaults.ShellConfig.validate_not_running_as_root
```

````

`````

````{py:data} SHELL_CONFIG
:canonical: archivebox.config.defaults.SHELL_CONFIG
:value: >
   'ShellConfig(...)'

```{autodoc2-docstring} archivebox.config.defaults.SHELL_CONFIG
```

````

`````{py:class} StorageConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_implicit_flags: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.config.defaults.StorageConfig

Bases: {py:obj}`abx.archivebox.base_configset.BaseConfigSet`

````{py:attribute} OUTPUT_PERMISSIONS
:canonical: archivebox.config.defaults.StorageConfig.OUTPUT_PERMISSIONS
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.StorageConfig.OUTPUT_PERMISSIONS
```

````

````{py:attribute} RESTRICT_FILE_NAMES
:canonical: archivebox.config.defaults.StorageConfig.RESTRICT_FILE_NAMES
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.StorageConfig.RESTRICT_FILE_NAMES
```

````

````{py:attribute} ENFORCE_ATOMIC_WRITES
:canonical: archivebox.config.defaults.StorageConfig.ENFORCE_ATOMIC_WRITES
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.StorageConfig.ENFORCE_ATOMIC_WRITES
```

````

````{py:attribute} DIR_OUTPUT_PERMISSIONS
:canonical: archivebox.config.defaults.StorageConfig.DIR_OUTPUT_PERMISSIONS
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.StorageConfig.DIR_OUTPUT_PERMISSIONS
```

````

`````

````{py:data} STORAGE_CONFIG
:canonical: archivebox.config.defaults.STORAGE_CONFIG
:value: >
   'StorageConfig(...)'

```{autodoc2-docstring} archivebox.config.defaults.STORAGE_CONFIG
```

````

`````{py:class} GeneralConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_implicit_flags: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.config.defaults.GeneralConfig

Bases: {py:obj}`abx.archivebox.base_configset.BaseConfigSet`

````{py:attribute} TAG_SEPARATOR_PATTERN
:canonical: archivebox.config.defaults.GeneralConfig.TAG_SEPARATOR_PATTERN
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.GeneralConfig.TAG_SEPARATOR_PATTERN
```

````

`````

````{py:data} GENERAL_CONFIG
:canonical: archivebox.config.defaults.GENERAL_CONFIG
:value: >
   'GeneralConfig(...)'

```{autodoc2-docstring} archivebox.config.defaults.GENERAL_CONFIG
```

````

`````{py:class} ServerConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_implicit_flags: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.config.defaults.ServerConfig

Bases: {py:obj}`abx.archivebox.base_configset.BaseConfigSet`

````{py:attribute} SECRET_KEY
:canonical: archivebox.config.defaults.ServerConfig.SECRET_KEY
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ServerConfig.SECRET_KEY
```

````

````{py:attribute} BIND_ADDR
:canonical: archivebox.config.defaults.ServerConfig.BIND_ADDR
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ServerConfig.BIND_ADDR
```

````

````{py:attribute} ALLOWED_HOSTS
:canonical: archivebox.config.defaults.ServerConfig.ALLOWED_HOSTS
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ServerConfig.ALLOWED_HOSTS
```

````

````{py:attribute} CSRF_TRUSTED_ORIGINS
:canonical: archivebox.config.defaults.ServerConfig.CSRF_TRUSTED_ORIGINS
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ServerConfig.CSRF_TRUSTED_ORIGINS
```

````

````{py:attribute} SNAPSHOTS_PER_PAGE
:canonical: archivebox.config.defaults.ServerConfig.SNAPSHOTS_PER_PAGE
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ServerConfig.SNAPSHOTS_PER_PAGE
```

````

````{py:attribute} FOOTER_INFO
:canonical: archivebox.config.defaults.ServerConfig.FOOTER_INFO
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ServerConfig.FOOTER_INFO
```

````

````{py:attribute} PUBLIC_INDEX
:canonical: archivebox.config.defaults.ServerConfig.PUBLIC_INDEX
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ServerConfig.PUBLIC_INDEX
```

````

````{py:attribute} PUBLIC_SNAPSHOTS
:canonical: archivebox.config.defaults.ServerConfig.PUBLIC_SNAPSHOTS
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ServerConfig.PUBLIC_SNAPSHOTS
```

````

````{py:attribute} PUBLIC_ADD_VIEW
:canonical: archivebox.config.defaults.ServerConfig.PUBLIC_ADD_VIEW
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ServerConfig.PUBLIC_ADD_VIEW
```

````

````{py:attribute} ADMIN_USERNAME
:canonical: archivebox.config.defaults.ServerConfig.ADMIN_USERNAME
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ServerConfig.ADMIN_USERNAME
```

````

````{py:attribute} ADMIN_PASSWORD
:canonical: archivebox.config.defaults.ServerConfig.ADMIN_PASSWORD
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ServerConfig.ADMIN_PASSWORD
```

````

````{py:attribute} REVERSE_PROXY_USER_HEADER
:canonical: archivebox.config.defaults.ServerConfig.REVERSE_PROXY_USER_HEADER
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ServerConfig.REVERSE_PROXY_USER_HEADER
```

````

````{py:attribute} REVERSE_PROXY_WHITELIST
:canonical: archivebox.config.defaults.ServerConfig.REVERSE_PROXY_WHITELIST
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ServerConfig.REVERSE_PROXY_WHITELIST
```

````

````{py:attribute} LOGOUT_REDIRECT_URL
:canonical: archivebox.config.defaults.ServerConfig.LOGOUT_REDIRECT_URL
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ServerConfig.LOGOUT_REDIRECT_URL
```

````

````{py:attribute} PREVIEW_ORIGINALS
:canonical: archivebox.config.defaults.ServerConfig.PREVIEW_ORIGINALS
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ServerConfig.PREVIEW_ORIGINALS
```

````

`````

````{py:data} SERVER_CONFIG
:canonical: archivebox.config.defaults.SERVER_CONFIG
:value: >
   'ServerConfig(...)'

```{autodoc2-docstring} archivebox.config.defaults.SERVER_CONFIG
```

````

`````{py:class} ArchivingConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_implicit_flags: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.config.defaults.ArchivingConfig

Bases: {py:obj}`abx.archivebox.base_configset.BaseConfigSet`

````{py:attribute} ONLY_NEW
:canonical: archivebox.config.defaults.ArchivingConfig.ONLY_NEW
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ArchivingConfig.ONLY_NEW
```

````

````{py:attribute} TIMEOUT
:canonical: archivebox.config.defaults.ArchivingConfig.TIMEOUT
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ArchivingConfig.TIMEOUT
```

````

````{py:attribute} MEDIA_TIMEOUT
:canonical: archivebox.config.defaults.ArchivingConfig.MEDIA_TIMEOUT
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ArchivingConfig.MEDIA_TIMEOUT
```

````

````{py:attribute} MEDIA_MAX_SIZE
:canonical: archivebox.config.defaults.ArchivingConfig.MEDIA_MAX_SIZE
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ArchivingConfig.MEDIA_MAX_SIZE
```

````

````{py:attribute} RESOLUTION
:canonical: archivebox.config.defaults.ArchivingConfig.RESOLUTION
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ArchivingConfig.RESOLUTION
```

````

````{py:attribute} CHECK_SSL_VALIDITY
:canonical: archivebox.config.defaults.ArchivingConfig.CHECK_SSL_VALIDITY
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ArchivingConfig.CHECK_SSL_VALIDITY
```

````

````{py:attribute} USER_AGENT
:canonical: archivebox.config.defaults.ArchivingConfig.USER_AGENT
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ArchivingConfig.USER_AGENT
```

````

````{py:attribute} COOKIES_FILE
:canonical: archivebox.config.defaults.ArchivingConfig.COOKIES_FILE
:type: pathlib.Path | None
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ArchivingConfig.COOKIES_FILE
```

````

````{py:attribute} URL_DENYLIST
:canonical: archivebox.config.defaults.ArchivingConfig.URL_DENYLIST
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ArchivingConfig.URL_DENYLIST
```

````

````{py:attribute} URL_ALLOWLIST
:canonical: archivebox.config.defaults.ArchivingConfig.URL_ALLOWLIST
:type: str | None
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.ArchivingConfig.URL_ALLOWLIST
```

````

````{py:method} validate_timeout(v)
:canonical: archivebox.config.defaults.ArchivingConfig.validate_timeout

```{autodoc2-docstring} archivebox.config.defaults.ArchivingConfig.validate_timeout
```

````

````{py:method} validate_check_ssl_validity(v)
:canonical: archivebox.config.defaults.ArchivingConfig.validate_check_ssl_validity

```{autodoc2-docstring} archivebox.config.defaults.ArchivingConfig.validate_check_ssl_validity
```

````

`````

````{py:data} ARCHIVING_CONFIG
:canonical: archivebox.config.defaults.ARCHIVING_CONFIG
:value: >
   'ArchivingConfig(...)'

```{autodoc2-docstring} archivebox.config.defaults.ARCHIVING_CONFIG
```

````

`````{py:class} SearchBackendConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_implicit_flags: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.config.defaults.SearchBackendConfig

Bases: {py:obj}`abx.archivebox.base_configset.BaseConfigSet`

````{py:attribute} USE_INDEXING_BACKEND
:canonical: archivebox.config.defaults.SearchBackendConfig.USE_INDEXING_BACKEND
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.SearchBackendConfig.USE_INDEXING_BACKEND
```

````

````{py:attribute} USE_SEARCHING_BACKEND
:canonical: archivebox.config.defaults.SearchBackendConfig.USE_SEARCHING_BACKEND
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.SearchBackendConfig.USE_SEARCHING_BACKEND
```

````

````{py:attribute} SEARCH_BACKEND_ENGINE
:canonical: archivebox.config.defaults.SearchBackendConfig.SEARCH_BACKEND_ENGINE
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.SearchBackendConfig.SEARCH_BACKEND_ENGINE
```

````

````{py:attribute} SEARCH_PROCESS_HTML
:canonical: archivebox.config.defaults.SearchBackendConfig.SEARCH_PROCESS_HTML
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.SearchBackendConfig.SEARCH_PROCESS_HTML
```

````

````{py:attribute} SEARCH_BACKEND_TIMEOUT
:canonical: archivebox.config.defaults.SearchBackendConfig.SEARCH_BACKEND_TIMEOUT
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.defaults.SearchBackendConfig.SEARCH_BACKEND_TIMEOUT
```

````

`````

````{py:data} SEARCH_BACKEND_CONFIG
:canonical: archivebox.config.defaults.SEARCH_BACKEND_CONFIG
:value: >
   'SearchBackendConfig(...)'

```{autodoc2-docstring} archivebox.config.defaults.SEARCH_BACKEND_CONFIG
```

````
