# {py:mod}`archivebox.plugins_auth.ldap.apps`

```{py:module} archivebox.plugins_auth.ldap.apps
```

```{autodoc2-docstring} archivebox.plugins_auth.ldap.apps
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`LdapBinary <archivebox.plugins_auth.ldap.apps.LdapBinary>`
  -
* - {py:obj}`LdapAuthPlugin <archivebox.plugins_auth.ldap.apps.LdapAuthPlugin>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.plugins_auth.ldap.apps.__package__>`
  - ```{autodoc2-docstring} archivebox.plugins_auth.ldap.apps.__package__
    :summary:
    ```
* - {py:obj}`LDAP_LIB <archivebox.plugins_auth.ldap.apps.LDAP_LIB>`
  - ```{autodoc2-docstring} archivebox.plugins_auth.ldap.apps.LDAP_LIB
    :summary:
    ```
* - {py:obj}`LDAP_BINARY <archivebox.plugins_auth.ldap.apps.LDAP_BINARY>`
  - ```{autodoc2-docstring} archivebox.plugins_auth.ldap.apps.LDAP_BINARY
    :summary:
    ```
* - {py:obj}`PLUGIN <archivebox.plugins_auth.ldap.apps.PLUGIN>`
  - ```{autodoc2-docstring} archivebox.plugins_auth.ldap.apps.PLUGIN
    :summary:
    ```
* - {py:obj}`DJANGO_APP <archivebox.plugins_auth.ldap.apps.DJANGO_APP>`
  - ```{autodoc2-docstring} archivebox.plugins_auth.ldap.apps.DJANGO_APP
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.plugins_auth.ldap.apps.__package__
:value: >
   'archivebox.plugins_auth.ldap'

```{autodoc2-docstring} archivebox.plugins_auth.ldap.apps.__package__
```

````

````{py:data} LDAP_LIB
:canonical: archivebox.plugins_auth.ldap.apps.LDAP_LIB
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_auth.ldap.apps.LDAP_LIB
```

````

`````{py:class} LdapBinary(/, **data: typing.Any)
:canonical: archivebox.plugins_auth.ldap.apps.LdapBinary

Bases: {py:obj}`abx.archivebox.base_binary.BaseBinary`

````{py:attribute} name
:canonical: archivebox.plugins_auth.ldap.apps.LdapBinary.name
:type: str
:value: >
   'ldap'

```{autodoc2-docstring} archivebox.plugins_auth.ldap.apps.LdapBinary.name
```

````

````{py:attribute} description
:canonical: archivebox.plugins_auth.ldap.apps.LdapBinary.description
:type: str
:value: >
   'LDAP Authentication'

```{autodoc2-docstring} archivebox.plugins_auth.ldap.apps.LdapBinary.description
```

````

````{py:attribute} binproviders_supported
:canonical: archivebox.plugins_auth.ldap.apps.LdapBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[abx.archivebox.base_binary.BaseBinProvider]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_auth.ldap.apps.LdapBinary.binproviders_supported
```

````

````{py:attribute} provider_overrides
:canonical: archivebox.plugins_auth.ldap.apps.LdapBinary.provider_overrides
:type: typing.Dict[pydantic_pkgr.BinProviderName, pydantic_pkgr.ProviderLookupDict]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_auth.ldap.apps.LdapBinary.provider_overrides
```

````

`````

````{py:data} LDAP_BINARY
:canonical: archivebox.plugins_auth.ldap.apps.LDAP_BINARY
:value: >
   'LdapBinary(...)'

```{autodoc2-docstring} archivebox.plugins_auth.ldap.apps.LDAP_BINARY
```

````

`````{py:class} LdapAuthPlugin(/, **data: typing.Any)
:canonical: archivebox.plugins_auth.ldap.apps.LdapAuthPlugin

Bases: {py:obj}`abx.archivebox.base_plugin.BasePlugin`

````{py:attribute} app_label
:canonical: archivebox.plugins_auth.ldap.apps.LdapAuthPlugin.app_label
:type: str
:value: >
   'ldap'

```{autodoc2-docstring} archivebox.plugins_auth.ldap.apps.LdapAuthPlugin.app_label
```

````

````{py:attribute} verbose_name
:canonical: archivebox.plugins_auth.ldap.apps.LdapAuthPlugin.verbose_name
:type: str
:value: >
   'LDAP Authentication'

```{autodoc2-docstring} archivebox.plugins_auth.ldap.apps.LdapAuthPlugin.verbose_name
```

````

````{py:attribute} hooks
:canonical: archivebox.plugins_auth.ldap.apps.LdapAuthPlugin.hooks
:type: typing.List[pydantic.InstanceOf[abx.archivebox.base_hook.BaseHook]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_auth.ldap.apps.LdapAuthPlugin.hooks
```

````

`````

````{py:data} PLUGIN
:canonical: archivebox.plugins_auth.ldap.apps.PLUGIN
:value: >
   'LdapAuthPlugin(...)'

```{autodoc2-docstring} archivebox.plugins_auth.ldap.apps.PLUGIN
```

````

````{py:data} DJANGO_APP
:canonical: archivebox.plugins_auth.ldap.apps.DJANGO_APP
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_auth.ldap.apps.DJANGO_APP
```

````
