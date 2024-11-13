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
* - {py:obj}`ArchivingConfig <archivebox.config.common.ArchivingConfig>`
  -
* - {py:obj}`SearchBackendConfig <archivebox.config.common.SearchBackendConfig>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.config.common.__package__>`
  - ```{autodoc2-docstring} archivebox.config.common.__package__
    :summary:
    ```
* - {py:obj}`SHELL_CONFIG <archivebox.config.common.SHELL_CONFIG>`
  - ```{autodoc2-docstring} archivebox.config.common.SHELL_CONFIG
    :summary:
    ```
* - {py:obj}`STORAGE_CONFIG <archivebox.config.common.STORAGE_CONFIG>`
  - ```{autodoc2-docstring} archivebox.config.common.STORAGE_CONFIG
    :summary:
    ```
* - {py:obj}`GENERAL_CONFIG <archivebox.config.common.GENERAL_CONFIG>`
  - ```{autodoc2-docstring} archivebox.config.common.GENERAL_CONFIG
    :summary:
    ```
* - {py:obj}`SERVER_CONFIG <archivebox.config.common.SERVER_CONFIG>`
  - ```{autodoc2-docstring} archivebox.config.common.SERVER_CONFIG
    :summary:
    ```
* - {py:obj}`ARCHIVING_CONFIG <archivebox.config.common.ARCHIVING_CONFIG>`
  - ```{autodoc2-docstring} archivebox.config.common.ARCHIVING_CONFIG
    :summary:
    ```
* - {py:obj}`SEARCH_BACKEND_CONFIG <archivebox.config.common.SEARCH_BACKEND_CONFIG>`
  - ```{autodoc2-docstring} archivebox.config.common.SEARCH_BACKEND_CONFIG
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.config.common.__package__
:value: >
   'archivebox.config'

```{autodoc2-docstring} archivebox.config.common.__package__
```

````

`````{py:class} ShellConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | None = None, _cli_ignore_unknown_args: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.config.common.ShellConfig

Bases: {py:obj}`abx_spec_config.base_configset.BaseConfigSet`

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
:type: typing.Dict[str, str]
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
:type: typing.Optional[str]

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

````{py:data} SHELL_CONFIG
:canonical: archivebox.config.common.SHELL_CONFIG
:value: >
   'ShellConfig(...)'

```{autodoc2-docstring} archivebox.config.common.SHELL_CONFIG
```

````

`````{py:class} StorageConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | None = None, _cli_ignore_unknown_args: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.config.common.StorageConfig

Bases: {py:obj}`abx_spec_config.base_configset.BaseConfigSet`

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

````{py:attribute} OUTPUT_PERMISSIONS
:canonical: archivebox.config.common.StorageConfig.OUTPUT_PERMISSIONS
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.StorageConfig.OUTPUT_PERMISSIONS
```

````

````{py:attribute} RESTRICT_FILE_NAMES
:canonical: archivebox.config.common.StorageConfig.RESTRICT_FILE_NAMES
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.StorageConfig.RESTRICT_FILE_NAMES
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

````{py:attribute} DIR_OUTPUT_PERMISSIONS
:canonical: archivebox.config.common.StorageConfig.DIR_OUTPUT_PERMISSIONS
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.StorageConfig.DIR_OUTPUT_PERMISSIONS
```

````

`````

````{py:data} STORAGE_CONFIG
:canonical: archivebox.config.common.STORAGE_CONFIG
:value: >
   'StorageConfig(...)'

```{autodoc2-docstring} archivebox.config.common.STORAGE_CONFIG
```

````

`````{py:class} GeneralConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | None = None, _cli_ignore_unknown_args: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.config.common.GeneralConfig

Bases: {py:obj}`abx_spec_config.base_configset.BaseConfigSet`

````{py:attribute} TAG_SEPARATOR_PATTERN
:canonical: archivebox.config.common.GeneralConfig.TAG_SEPARATOR_PATTERN
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.GeneralConfig.TAG_SEPARATOR_PATTERN
```

````

`````

````{py:data} GENERAL_CONFIG
:canonical: archivebox.config.common.GENERAL_CONFIG
:value: >
   'GeneralConfig(...)'

```{autodoc2-docstring} archivebox.config.common.GENERAL_CONFIG
```

````

`````{py:class} ServerConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | None = None, _cli_ignore_unknown_args: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.config.common.ServerConfig

Bases: {py:obj}`abx_spec_config.base_configset.BaseConfigSet`

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

````{py:attribute} SNAPSHOTS_PER_PAGE
:canonical: archivebox.config.common.ServerConfig.SNAPSHOTS_PER_PAGE
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ServerConfig.SNAPSHOTS_PER_PAGE
```

````

````{py:attribute} PREVIEW_ORIGINALS
:canonical: archivebox.config.common.ServerConfig.PREVIEW_ORIGINALS
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ServerConfig.PREVIEW_ORIGINALS
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

````{py:attribute} PUBLIC_SNAPSHOTS
:canonical: archivebox.config.common.ServerConfig.PUBLIC_SNAPSHOTS
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ServerConfig.PUBLIC_SNAPSHOTS
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
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ServerConfig.ADMIN_USERNAME
```

````

````{py:attribute} ADMIN_PASSWORD
:canonical: archivebox.config.common.ServerConfig.ADMIN_PASSWORD
:type: str
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

`````

````{py:data} SERVER_CONFIG
:canonical: archivebox.config.common.SERVER_CONFIG
:value: >
   'ServerConfig(...)'

```{autodoc2-docstring} archivebox.config.common.SERVER_CONFIG
```

````

`````{py:class} ArchivingConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | None = None, _cli_ignore_unknown_args: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.config.common.ArchivingConfig

Bases: {py:obj}`abx_spec_config.base_configset.BaseConfigSet`

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

````{py:attribute} MEDIA_TIMEOUT
:canonical: archivebox.config.common.ArchivingConfig.MEDIA_TIMEOUT
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.MEDIA_TIMEOUT
```

````

````{py:attribute} MEDIA_MAX_SIZE
:canonical: archivebox.config.common.ArchivingConfig.MEDIA_MAX_SIZE
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.MEDIA_MAX_SIZE
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

````{py:attribute} SAVE_ALLOWLIST
:canonical: archivebox.config.common.ArchivingConfig.SAVE_ALLOWLIST
:type: typing.Dict[str, typing.List[str]]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.SAVE_ALLOWLIST
```

````

````{py:attribute} SAVE_DENYLIST
:canonical: archivebox.config.common.ArchivingConfig.SAVE_DENYLIST
:type: typing.Dict[str, typing.List[str]]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.SAVE_DENYLIST
```

````

````{py:method} validate()
:canonical: archivebox.config.common.ArchivingConfig.validate

````

````{py:method} validate_check_ssl_validity(v)
:canonical: archivebox.config.common.ArchivingConfig.validate_check_ssl_validity

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.validate_check_ssl_validity
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

````{py:property} SAVE_ALLOWLIST_PTNS
:canonical: archivebox.config.common.ArchivingConfig.SAVE_ALLOWLIST_PTNS
:type: typing.Dict[re.Pattern, typing.List[str]]

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.SAVE_ALLOWLIST_PTNS
```

````

````{py:property} SAVE_DENYLIST_PTNS
:canonical: archivebox.config.common.ArchivingConfig.SAVE_DENYLIST_PTNS
:type: typing.Dict[re.Pattern, typing.List[str]]

```{autodoc2-docstring} archivebox.config.common.ArchivingConfig.SAVE_DENYLIST_PTNS
```

````

`````

````{py:data} ARCHIVING_CONFIG
:canonical: archivebox.config.common.ARCHIVING_CONFIG
:value: >
   'ArchivingConfig(...)'

```{autodoc2-docstring} archivebox.config.common.ARCHIVING_CONFIG
```

````

`````{py:class} SearchBackendConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | None = None, _cli_ignore_unknown_args: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.config.common.SearchBackendConfig

Bases: {py:obj}`abx_spec_config.base_configset.BaseConfigSet`

````{py:attribute} USE_INDEXING_BACKEND
:canonical: archivebox.config.common.SearchBackendConfig.USE_INDEXING_BACKEND
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.SearchBackendConfig.USE_INDEXING_BACKEND
```

````

````{py:attribute} USE_SEARCHING_BACKEND
:canonical: archivebox.config.common.SearchBackendConfig.USE_SEARCHING_BACKEND
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.SearchBackendConfig.USE_SEARCHING_BACKEND
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

````{py:attribute} SEARCH_PROCESS_HTML
:canonical: archivebox.config.common.SearchBackendConfig.SEARCH_PROCESS_HTML
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.SearchBackendConfig.SEARCH_PROCESS_HTML
```

````

````{py:attribute} SEARCH_BACKEND_TIMEOUT
:canonical: archivebox.config.common.SearchBackendConfig.SEARCH_BACKEND_TIMEOUT
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.config.common.SearchBackendConfig.SEARCH_BACKEND_TIMEOUT
```

````

`````

````{py:data} SEARCH_BACKEND_CONFIG
:canonical: archivebox.config.common.SEARCH_BACKEND_CONFIG
:value: >
   'SearchBackendConfig(...)'

```{autodoc2-docstring} archivebox.config.common.SEARCH_BACKEND_CONFIG
```

````
