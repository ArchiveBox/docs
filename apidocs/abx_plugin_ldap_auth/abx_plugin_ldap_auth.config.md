# {py:mod}`abx_plugin_ldap_auth.config`

```{py:module} abx_plugin_ldap_auth.config
```

```{autodoc2-docstring} abx_plugin_ldap_auth.config
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`LdapConfig <abx_plugin_ldap_auth.config.LdapConfig>`
  - ```{autodoc2-docstring} abx_plugin_ldap_auth.config.LdapConfig
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_ldap_lib <abx_plugin_ldap_auth.config.get_ldap_lib>`
  - ```{autodoc2-docstring} abx_plugin_ldap_auth.config.get_ldap_lib
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`LDAP_LIB <abx_plugin_ldap_auth.config.LDAP_LIB>`
  - ```{autodoc2-docstring} abx_plugin_ldap_auth.config.LDAP_LIB
    :summary:
    ```
* - {py:obj}`LDAP_SEARCH <abx_plugin_ldap_auth.config.LDAP_SEARCH>`
  - ```{autodoc2-docstring} abx_plugin_ldap_auth.config.LDAP_SEARCH
    :summary:
    ```
* - {py:obj}`LDAP_CONFIG <abx_plugin_ldap_auth.config.LDAP_CONFIG>`
  - ```{autodoc2-docstring} abx_plugin_ldap_auth.config.LDAP_CONFIG
    :summary:
    ```
````

### API

````{py:data} LDAP_LIB
:canonical: abx_plugin_ldap_auth.config.LDAP_LIB
:value: >
   None

```{autodoc2-docstring} abx_plugin_ldap_auth.config.LDAP_LIB
```

````

````{py:data} LDAP_SEARCH
:canonical: abx_plugin_ldap_auth.config.LDAP_SEARCH
:value: >
   None

```{autodoc2-docstring} abx_plugin_ldap_auth.config.LDAP_SEARCH
```

````

````{py:function} get_ldap_lib(extra_paths=())
:canonical: abx_plugin_ldap_auth.config.get_ldap_lib

```{autodoc2-docstring} abx_plugin_ldap_auth.config.get_ldap_lib
```
````

`````{py:class} LdapConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | None = None, _cli_ignore_unknown_args: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: abx_plugin_ldap_auth.config.LdapConfig

Bases: {py:obj}`abx_spec_config.base_configset.BaseConfigSet`

```{autodoc2-docstring} abx_plugin_ldap_auth.config.LdapConfig
```

```{rubric} Initialization
```

```{autodoc2-docstring} abx_plugin_ldap_auth.config.LdapConfig.__init__
```

````{py:attribute} LDAP_ENABLED
:canonical: abx_plugin_ldap_auth.config.LdapConfig.LDAP_ENABLED
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_ldap_auth.config.LdapConfig.LDAP_ENABLED
```

````

````{py:attribute} LDAP_SERVER_URI
:canonical: abx_plugin_ldap_auth.config.LdapConfig.LDAP_SERVER_URI
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_ldap_auth.config.LdapConfig.LDAP_SERVER_URI
```

````

````{py:attribute} LDAP_BIND_DN
:canonical: abx_plugin_ldap_auth.config.LdapConfig.LDAP_BIND_DN
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_ldap_auth.config.LdapConfig.LDAP_BIND_DN
```

````

````{py:attribute} LDAP_BIND_PASSWORD
:canonical: abx_plugin_ldap_auth.config.LdapConfig.LDAP_BIND_PASSWORD
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_ldap_auth.config.LdapConfig.LDAP_BIND_PASSWORD
```

````

````{py:attribute} LDAP_USER_BASE
:canonical: abx_plugin_ldap_auth.config.LdapConfig.LDAP_USER_BASE
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_ldap_auth.config.LdapConfig.LDAP_USER_BASE
```

````

````{py:attribute} LDAP_USER_FILTER
:canonical: abx_plugin_ldap_auth.config.LdapConfig.LDAP_USER_FILTER
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_ldap_auth.config.LdapConfig.LDAP_USER_FILTER
```

````

````{py:attribute} LDAP_CREATE_SUPERUSER
:canonical: abx_plugin_ldap_auth.config.LdapConfig.LDAP_CREATE_SUPERUSER
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_ldap_auth.config.LdapConfig.LDAP_CREATE_SUPERUSER
```

````

````{py:attribute} LDAP_USERNAME_ATTR
:canonical: abx_plugin_ldap_auth.config.LdapConfig.LDAP_USERNAME_ATTR
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_ldap_auth.config.LdapConfig.LDAP_USERNAME_ATTR
```

````

````{py:attribute} LDAP_FIRSTNAME_ATTR
:canonical: abx_plugin_ldap_auth.config.LdapConfig.LDAP_FIRSTNAME_ATTR
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_ldap_auth.config.LdapConfig.LDAP_FIRSTNAME_ATTR
```

````

````{py:attribute} LDAP_LASTNAME_ATTR
:canonical: abx_plugin_ldap_auth.config.LdapConfig.LDAP_LASTNAME_ATTR
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_ldap_auth.config.LdapConfig.LDAP_LASTNAME_ATTR
```

````

````{py:attribute} LDAP_EMAIL_ATTR
:canonical: abx_plugin_ldap_auth.config.LdapConfig.LDAP_EMAIL_ATTR
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_ldap_auth.config.LdapConfig.LDAP_EMAIL_ATTR
```

````

````{py:method} validate()
:canonical: abx_plugin_ldap_auth.config.LdapConfig.validate

````

````{py:property} LDAP_CONFIG_IS_SET
:canonical: abx_plugin_ldap_auth.config.LdapConfig.LDAP_CONFIG_IS_SET
:type: bool

```{autodoc2-docstring} abx_plugin_ldap_auth.config.LdapConfig.LDAP_CONFIG_IS_SET
```

````

````{py:property} LDAP_USER_ATTR_MAP
:canonical: abx_plugin_ldap_auth.config.LdapConfig.LDAP_USER_ATTR_MAP
:type: typing.Dict[str, str]

```{autodoc2-docstring} abx_plugin_ldap_auth.config.LdapConfig.LDAP_USER_ATTR_MAP
```

````

````{py:property} AUTHENTICATION_BACKENDS
:canonical: abx_plugin_ldap_auth.config.LdapConfig.AUTHENTICATION_BACKENDS
:type: typing.List[str]

```{autodoc2-docstring} abx_plugin_ldap_auth.config.LdapConfig.AUTHENTICATION_BACKENDS
```

````

````{py:property} AUTH_LDAP_USER_SEARCH
:canonical: abx_plugin_ldap_auth.config.LdapConfig.AUTH_LDAP_USER_SEARCH
:type: typing.Optional[object]

```{autodoc2-docstring} abx_plugin_ldap_auth.config.LdapConfig.AUTH_LDAP_USER_SEARCH
```

````

`````

````{py:data} LDAP_CONFIG
:canonical: abx_plugin_ldap_auth.config.LDAP_CONFIG
:value: >
   'LdapConfig(...)'

```{autodoc2-docstring} abx_plugin_ldap_auth.config.LDAP_CONFIG
```

````
