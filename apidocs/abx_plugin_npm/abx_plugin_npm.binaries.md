# {py:mod}`abx_plugin_npm.binaries`

```{py:module} abx_plugin_npm.binaries
```

```{autodoc2-docstring} abx_plugin_npm.binaries
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`NodeBinary <abx_plugin_npm.binaries.NodeBinary>`
  -
* - {py:obj}`NpmBinary <abx_plugin_npm.binaries.NpmBinary>`
  -
* - {py:obj}`NpxBinary <abx_plugin_npm.binaries.NpxBinary>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DEFAULT_BINPROVIDERS <abx_plugin_npm.binaries.DEFAULT_BINPROVIDERS>`
  - ```{autodoc2-docstring} abx_plugin_npm.binaries.DEFAULT_BINPROVIDERS
    :summary:
    ```
* - {py:obj}`env <abx_plugin_npm.binaries.env>`
  - ```{autodoc2-docstring} abx_plugin_npm.binaries.env
    :summary:
    ```
* - {py:obj}`apt <abx_plugin_npm.binaries.apt>`
  - ```{autodoc2-docstring} abx_plugin_npm.binaries.apt
    :summary:
    ```
* - {py:obj}`brew <abx_plugin_npm.binaries.brew>`
  - ```{autodoc2-docstring} abx_plugin_npm.binaries.brew
    :summary:
    ```
* - {py:obj}`NODE_BINARY <abx_plugin_npm.binaries.NODE_BINARY>`
  - ```{autodoc2-docstring} abx_plugin_npm.binaries.NODE_BINARY
    :summary:
    ```
* - {py:obj}`NPM_BINARY <abx_plugin_npm.binaries.NPM_BINARY>`
  - ```{autodoc2-docstring} abx_plugin_npm.binaries.NPM_BINARY
    :summary:
    ```
* - {py:obj}`NPX_BINARY <abx_plugin_npm.binaries.NPX_BINARY>`
  - ```{autodoc2-docstring} abx_plugin_npm.binaries.NPX_BINARY
    :summary:
    ```
````

### API

````{py:data} DEFAULT_BINPROVIDERS
:canonical: abx_plugin_npm.binaries.DEFAULT_BINPROVIDERS
:value: >
   'benedict(...)'

```{autodoc2-docstring} abx_plugin_npm.binaries.DEFAULT_BINPROVIDERS
```

````

````{py:data} env
:canonical: abx_plugin_npm.binaries.env
:value: >
   None

```{autodoc2-docstring} abx_plugin_npm.binaries.env
```

````

````{py:data} apt
:canonical: abx_plugin_npm.binaries.apt
:value: >
   None

```{autodoc2-docstring} abx_plugin_npm.binaries.apt
```

````

````{py:data} brew
:canonical: abx_plugin_npm.binaries.brew
:value: >
   None

```{autodoc2-docstring} abx_plugin_npm.binaries.brew
```

````

`````{py:class} NodeBinary(/, **data: typing.Any)
:canonical: abx_plugin_npm.binaries.NodeBinary

Bases: {py:obj}`pydantic_pkgr.Binary`

````{py:attribute} name
:canonical: abx_plugin_npm.binaries.NodeBinary.name
:type: pydantic_pkgr.BinName
:value: >
   'node'

```{autodoc2-docstring} abx_plugin_npm.binaries.NodeBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: abx_plugin_npm.binaries.NodeBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} abx_plugin_npm.binaries.NodeBinary.binproviders_supported
```

````

````{py:attribute} overrides
:canonical: abx_plugin_npm.binaries.NodeBinary.overrides
:type: pydantic_pkgr.BinaryOverrides
:value: >
   None

```{autodoc2-docstring} abx_plugin_npm.binaries.NodeBinary.overrides
```

````

`````

````{py:data} NODE_BINARY
:canonical: abx_plugin_npm.binaries.NODE_BINARY
:value: >
   'NodeBinary(...)'

```{autodoc2-docstring} abx_plugin_npm.binaries.NODE_BINARY
```

````

`````{py:class} NpmBinary(/, **data: typing.Any)
:canonical: abx_plugin_npm.binaries.NpmBinary

Bases: {py:obj}`pydantic_pkgr.Binary`

````{py:attribute} name
:canonical: abx_plugin_npm.binaries.NpmBinary.name
:type: pydantic_pkgr.BinName
:value: >
   'npm'

```{autodoc2-docstring} abx_plugin_npm.binaries.NpmBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: abx_plugin_npm.binaries.NpmBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} abx_plugin_npm.binaries.NpmBinary.binproviders_supported
```

````

````{py:attribute} overrides
:canonical: abx_plugin_npm.binaries.NpmBinary.overrides
:type: pydantic_pkgr.BinaryOverrides
:value: >
   None

```{autodoc2-docstring} abx_plugin_npm.binaries.NpmBinary.overrides
```

````

`````

````{py:data} NPM_BINARY
:canonical: abx_plugin_npm.binaries.NPM_BINARY
:value: >
   'NpmBinary(...)'

```{autodoc2-docstring} abx_plugin_npm.binaries.NPM_BINARY
```

````

`````{py:class} NpxBinary(/, **data: typing.Any)
:canonical: abx_plugin_npm.binaries.NpxBinary

Bases: {py:obj}`pydantic_pkgr.Binary`

````{py:attribute} name
:canonical: abx_plugin_npm.binaries.NpxBinary.name
:type: pydantic_pkgr.BinName
:value: >
   'npx'

```{autodoc2-docstring} abx_plugin_npm.binaries.NpxBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: abx_plugin_npm.binaries.NpxBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} abx_plugin_npm.binaries.NpxBinary.binproviders_supported
```

````

````{py:attribute} overrides
:canonical: abx_plugin_npm.binaries.NpxBinary.overrides
:type: pydantic_pkgr.BinaryOverrides
:value: >
   None

```{autodoc2-docstring} abx_plugin_npm.binaries.NpxBinary.overrides
```

````

`````

````{py:data} NPX_BINARY
:canonical: abx_plugin_npm.binaries.NPX_BINARY
:value: >
   'NpxBinary(...)'

```{autodoc2-docstring} abx_plugin_npm.binaries.NPX_BINARY
```

````
