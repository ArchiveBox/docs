# {py:mod}`abx_plugin_readability.binaries`

```{py:module} abx_plugin_readability.binaries
```

```{autodoc2-docstring} abx_plugin_readability.binaries
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ReadabilityBinary <abx_plugin_readability.binaries.ReadabilityBinary>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`READABILITY_PACKAGE_NAME <abx_plugin_readability.binaries.READABILITY_PACKAGE_NAME>`
  - ```{autodoc2-docstring} abx_plugin_readability.binaries.READABILITY_PACKAGE_NAME
    :summary:
    ```
* - {py:obj}`READABILITY_BINARY <abx_plugin_readability.binaries.READABILITY_BINARY>`
  - ```{autodoc2-docstring} abx_plugin_readability.binaries.READABILITY_BINARY
    :summary:
    ```
````

### API

````{py:data} READABILITY_PACKAGE_NAME
:canonical: abx_plugin_readability.binaries.READABILITY_PACKAGE_NAME
:value: >
   'github:ArchiveBox/readability-extractor'

```{autodoc2-docstring} abx_plugin_readability.binaries.READABILITY_PACKAGE_NAME
```

````

`````{py:class} ReadabilityBinary(/, **data: typing.Any)
:canonical: abx_plugin_readability.binaries.ReadabilityBinary

Bases: {py:obj}`pydantic_pkgr.Binary`

````{py:attribute} name
:canonical: abx_plugin_readability.binaries.ReadabilityBinary.name
:type: pydantic_pkgr.BinName
:value: >
   None

```{autodoc2-docstring} abx_plugin_readability.binaries.ReadabilityBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: abx_plugin_readability.binaries.ReadabilityBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} abx_plugin_readability.binaries.ReadabilityBinary.binproviders_supported
```

````

````{py:attribute} overrides
:canonical: abx_plugin_readability.binaries.ReadabilityBinary.overrides
:type: pydantic_pkgr.BinaryOverrides
:value: >
   None

```{autodoc2-docstring} abx_plugin_readability.binaries.ReadabilityBinary.overrides
```

````

`````

````{py:data} READABILITY_BINARY
:canonical: abx_plugin_readability.binaries.READABILITY_BINARY
:value: >
   'ReadabilityBinary(...)'

```{autodoc2-docstring} abx_plugin_readability.binaries.READABILITY_BINARY
```

````
