# {py:mod}`abx_plugin_ldap_auth.binaries`

```{py:module} abx_plugin_ldap_auth.binaries
```

```{autodoc2-docstring} abx_plugin_ldap_auth.binaries
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`LdapBinary <abx_plugin_ldap_auth.binaries.LdapBinary>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_LDAP_LIB_path <abx_plugin_ldap_auth.binaries.get_LDAP_LIB_path>`
  - ```{autodoc2-docstring} abx_plugin_ldap_auth.binaries.get_LDAP_LIB_path
    :summary:
    ```
* - {py:obj}`get_LDAP_LIB_version <abx_plugin_ldap_auth.binaries.get_LDAP_LIB_version>`
  - ```{autodoc2-docstring} abx_plugin_ldap_auth.binaries.get_LDAP_LIB_version
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <abx_plugin_ldap_auth.binaries.__package__>`
  - ```{autodoc2-docstring} abx_plugin_ldap_auth.binaries.__package__
    :summary:
    ```
* - {py:obj}`LDAP_BINARY <abx_plugin_ldap_auth.binaries.LDAP_BINARY>`
  - ```{autodoc2-docstring} abx_plugin_ldap_auth.binaries.LDAP_BINARY
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: abx_plugin_ldap_auth.binaries.__package__
:value: >
   'abx_plugin_ldap_auth'

```{autodoc2-docstring} abx_plugin_ldap_auth.binaries.__package__
```

````

````{py:function} get_LDAP_LIB_path(paths=())
:canonical: abx_plugin_ldap_auth.binaries.get_LDAP_LIB_path

```{autodoc2-docstring} abx_plugin_ldap_auth.binaries.get_LDAP_LIB_path
```
````

````{py:function} get_LDAP_LIB_version()
:canonical: abx_plugin_ldap_auth.binaries.get_LDAP_LIB_version

```{autodoc2-docstring} abx_plugin_ldap_auth.binaries.get_LDAP_LIB_version
```
````

`````{py:class} LdapBinary(/, **data: typing.Any)
:canonical: abx_plugin_ldap_auth.binaries.LdapBinary

Bases: {py:obj}`pydantic_pkgr.Binary`

````{py:attribute} name
:canonical: abx_plugin_ldap_auth.binaries.LdapBinary.name
:type: str
:value: >
   'ldap'

```{autodoc2-docstring} abx_plugin_ldap_auth.binaries.LdapBinary.name
```

````

````{py:attribute} description
:canonical: abx_plugin_ldap_auth.binaries.LdapBinary.description
:type: str
:value: >
   'LDAP Authentication'

```{autodoc2-docstring} abx_plugin_ldap_auth.binaries.LdapBinary.description
```

````

````{py:attribute} binproviders_supported
:canonical: abx_plugin_ldap_auth.binaries.LdapBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} abx_plugin_ldap_auth.binaries.LdapBinary.binproviders_supported
```

````

````{py:attribute} overrides
:canonical: abx_plugin_ldap_auth.binaries.LdapBinary.overrides
:type: pydantic_pkgr.BinaryOverrides
:value: >
   None

```{autodoc2-docstring} abx_plugin_ldap_auth.binaries.LdapBinary.overrides
```

````

`````

````{py:data} LDAP_BINARY
:canonical: abx_plugin_ldap_auth.binaries.LDAP_BINARY
:value: >
   'LdapBinary(...)'

```{autodoc2-docstring} abx_plugin_ldap_auth.binaries.LDAP_BINARY
```

````
