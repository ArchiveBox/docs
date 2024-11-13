# {py:mod}`abx_plugin_sonic_search.binaries`

```{py:module} abx_plugin_sonic_search.binaries
```

```{autodoc2-docstring} abx_plugin_sonic_search.binaries
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SonicBinary <abx_plugin_sonic_search.binaries.SonicBinary>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SONIC_BINARY <abx_plugin_sonic_search.binaries.SONIC_BINARY>`
  - ```{autodoc2-docstring} abx_plugin_sonic_search.binaries.SONIC_BINARY
    :summary:
    ```
````

### API

`````{py:class} SonicBinary(/, **data: typing.Any)
:canonical: abx_plugin_sonic_search.binaries.SonicBinary

Bases: {py:obj}`pydantic_pkgr.Binary`

````{py:attribute} name
:canonical: abx_plugin_sonic_search.binaries.SonicBinary.name
:type: pydantic_pkgr.BinName
:value: >
   None

```{autodoc2-docstring} abx_plugin_sonic_search.binaries.SonicBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: abx_plugin_sonic_search.binaries.SonicBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} abx_plugin_sonic_search.binaries.SonicBinary.binproviders_supported
```

````

````{py:attribute} overrides
:canonical: abx_plugin_sonic_search.binaries.SonicBinary.overrides
:type: pydantic_pkgr.BinaryOverrides
:value: >
   None

```{autodoc2-docstring} abx_plugin_sonic_search.binaries.SonicBinary.overrides
```

````

`````

````{py:data} SONIC_BINARY
:canonical: abx_plugin_sonic_search.binaries.SONIC_BINARY
:value: >
   'SonicBinary(...)'

```{autodoc2-docstring} abx_plugin_sonic_search.binaries.SONIC_BINARY
```

````
