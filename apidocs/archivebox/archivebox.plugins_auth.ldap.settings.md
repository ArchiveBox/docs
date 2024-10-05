# {py:mod}`archivebox.plugins_auth.ldap.settings`

```{py:module} archivebox.plugins_auth.ldap.settings
```

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`LdapConfig <archivebox.plugins_auth.ldap.settings.LdapConfig>`
  - ```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LdapConfig
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_ldap_lib <archivebox.plugins_auth.ldap.settings.get_ldap_lib>`
  - ```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.get_ldap_lib
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.plugins_auth.ldap.settings.__package__>`
  - ```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.__package__
    :summary:
    ```
* - {py:obj}`LDAP_LIB <archivebox.plugins_auth.ldap.settings.LDAP_LIB>`
  - ```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LDAP_LIB
    :summary:
    ```
* - {py:obj}`LDAP_SEARCH <archivebox.plugins_auth.ldap.settings.LDAP_SEARCH>`
  - ```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LDAP_SEARCH
    :summary:
    ```
* - {py:obj}`LDAP_CONFIG <archivebox.plugins_auth.ldap.settings.LDAP_CONFIG>`
  - ```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LDAP_CONFIG
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.plugins_auth.ldap.settings.__package__
:value: >
   'archivebox.plugins_auth.ldap'

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.__package__
```

````

````{py:data} LDAP_LIB
:canonical: archivebox.plugins_auth.ldap.settings.LDAP_LIB
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LDAP_LIB
```

````

````{py:data} LDAP_SEARCH
:canonical: archivebox.plugins_auth.ldap.settings.LDAP_SEARCH
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LDAP_SEARCH
```

````

````{py:function} get_ldap_lib()
:canonical: archivebox.plugins_auth.ldap.settings.get_ldap_lib

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.get_ldap_lib
```
````

`````{py:class} LdapConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_implicit_flags: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.plugins_auth.ldap.settings.LdapConfig

Bases: {py:obj}`abx.archivebox.base_configset.BaseConfigSet`

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LdapConfig
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LdapConfig.__init__
```

````{py:attribute} LDAP_ENABLED
:canonical: archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_ENABLED
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_ENABLED
```

````

````{py:attribute} LDAP_SERVER_URI
:canonical: archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_SERVER_URI
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_SERVER_URI
```

````

````{py:attribute} LDAP_BIND_DN
:canonical: archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_BIND_DN
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_BIND_DN
```

````

````{py:attribute} LDAP_BIND_PASSWORD
:canonical: archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_BIND_PASSWORD
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_BIND_PASSWORD
```

````

````{py:attribute} LDAP_USER_BASE
:canonical: archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_USER_BASE
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_USER_BASE
```

````

````{py:attribute} LDAP_USER_FILTER
:canonical: archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_USER_FILTER
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_USER_FILTER
```

````

````{py:attribute} LDAP_CREATE_SUPERUSER
:canonical: archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_CREATE_SUPERUSER
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_CREATE_SUPERUSER
```

````

````{py:attribute} LDAP_USERNAME_ATTR
:canonical: archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_USERNAME_ATTR
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_USERNAME_ATTR
```

````

````{py:attribute} LDAP_FIRSTNAME_ATTR
:canonical: archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_FIRSTNAME_ATTR
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_FIRSTNAME_ATTR
```

````

````{py:attribute} LDAP_LASTNAME_ATTR
:canonical: archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_LASTNAME_ATTR
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_LASTNAME_ATTR
```

````

````{py:attribute} LDAP_EMAIL_ATTR
:canonical: archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_EMAIL_ATTR
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_EMAIL_ATTR
```

````

````{py:method} validate_ldap_config()
:canonical: archivebox.plugins_auth.ldap.settings.LdapConfig.validate_ldap_config

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LdapConfig.validate_ldap_config
```

````

````{py:property} LDAP_CONFIG_IS_SET
:canonical: archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_CONFIG_IS_SET
:type: bool

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_CONFIG_IS_SET
```

````

````{py:property} LDAP_USER_ATTR_MAP
:canonical: archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_USER_ATTR_MAP
:type: typing.Dict[str, str]

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LdapConfig.LDAP_USER_ATTR_MAP
```

````

````{py:property} AUTHENTICATION_BACKENDS
:canonical: archivebox.plugins_auth.ldap.settings.LdapConfig.AUTHENTICATION_BACKENDS
:type: typing.List[str]

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LdapConfig.AUTHENTICATION_BACKENDS
```

````

````{py:property} AUTH_LDAP_USER_SEARCH
:canonical: archivebox.plugins_auth.ldap.settings.LdapConfig.AUTH_LDAP_USER_SEARCH
:type: typing.Optional[object]

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LdapConfig.AUTH_LDAP_USER_SEARCH
```

````

`````

````{py:data} LDAP_CONFIG
:canonical: archivebox.plugins_auth.ldap.settings.LDAP_CONFIG
:value: >
   'LdapConfig(...)'

```{autodoc2-docstring} archivebox.plugins_auth.ldap.settings.LDAP_CONFIG
```

````
