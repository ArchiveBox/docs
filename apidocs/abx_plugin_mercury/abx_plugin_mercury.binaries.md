# {py:mod}`abx_plugin_mercury.binaries`

```{py:module} abx_plugin_mercury.binaries
```

```{autodoc2-docstring} abx_plugin_mercury.binaries
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`MercuryBinary <abx_plugin_mercury.binaries.MercuryBinary>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`MERCURY_BINARY <abx_plugin_mercury.binaries.MERCURY_BINARY>`
  - ```{autodoc2-docstring} abx_plugin_mercury.binaries.MERCURY_BINARY
    :summary:
    ```
````

### API

`````{py:class} MercuryBinary(/, **data: typing.Any)
:canonical: abx_plugin_mercury.binaries.MercuryBinary

Bases: {py:obj}`pydantic_pkgr.Binary`

````{py:attribute} name
:canonical: abx_plugin_mercury.binaries.MercuryBinary.name
:type: pydantic_pkgr.BinName
:value: >
   None

```{autodoc2-docstring} abx_plugin_mercury.binaries.MercuryBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: abx_plugin_mercury.binaries.MercuryBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} abx_plugin_mercury.binaries.MercuryBinary.binproviders_supported
```

````

````{py:attribute} overrides
:canonical: abx_plugin_mercury.binaries.MercuryBinary.overrides
:type: pydantic_pkgr.BinaryOverrides
:value: >
   None

```{autodoc2-docstring} abx_plugin_mercury.binaries.MercuryBinary.overrides
```

````

`````

````{py:data} MERCURY_BINARY
:canonical: abx_plugin_mercury.binaries.MERCURY_BINARY
:value: >
   'MercuryBinary(...)'

```{autodoc2-docstring} abx_plugin_mercury.binaries.MERCURY_BINARY
```

````
