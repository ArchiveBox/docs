# {py:mod}`abx_plugin_singlefile.binaries`

```{py:module} abx_plugin_singlefile.binaries
```

```{autodoc2-docstring} abx_plugin_singlefile.binaries
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SinglefileBinary <abx_plugin_singlefile.binaries.SinglefileBinary>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SINGLEFILE_MIN_VERSION <abx_plugin_singlefile.binaries.SINGLEFILE_MIN_VERSION>`
  - ```{autodoc2-docstring} abx_plugin_singlefile.binaries.SINGLEFILE_MIN_VERSION
    :summary:
    ```
* - {py:obj}`SINGLEFILE_MAX_VERSION <abx_plugin_singlefile.binaries.SINGLEFILE_MAX_VERSION>`
  - ```{autodoc2-docstring} abx_plugin_singlefile.binaries.SINGLEFILE_MAX_VERSION
    :summary:
    ```
* - {py:obj}`SINGLEFILE_BINARY <abx_plugin_singlefile.binaries.SINGLEFILE_BINARY>`
  - ```{autodoc2-docstring} abx_plugin_singlefile.binaries.SINGLEFILE_BINARY
    :summary:
    ```
````

### API

````{py:data} SINGLEFILE_MIN_VERSION
:canonical: abx_plugin_singlefile.binaries.SINGLEFILE_MIN_VERSION
:value: >
   '1.1.54'

```{autodoc2-docstring} abx_plugin_singlefile.binaries.SINGLEFILE_MIN_VERSION
```

````

````{py:data} SINGLEFILE_MAX_VERSION
:canonical: abx_plugin_singlefile.binaries.SINGLEFILE_MAX_VERSION
:value: >
   '1.1.60'

```{autodoc2-docstring} abx_plugin_singlefile.binaries.SINGLEFILE_MAX_VERSION
```

````

`````{py:class} SinglefileBinary(/, **data: typing.Any)
:canonical: abx_plugin_singlefile.binaries.SinglefileBinary

Bases: {py:obj}`abx_pkg.Binary`

````{py:attribute} name
:canonical: abx_plugin_singlefile.binaries.SinglefileBinary.name
:type: abx_pkg.BinName
:value: >
   None

```{autodoc2-docstring} abx_plugin_singlefile.binaries.SinglefileBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: abx_plugin_singlefile.binaries.SinglefileBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[abx_pkg.BinProvider]]
:value: >
   None

```{autodoc2-docstring} abx_plugin_singlefile.binaries.SinglefileBinary.binproviders_supported
```

````

````{py:attribute} overrides
:canonical: abx_plugin_singlefile.binaries.SinglefileBinary.overrides
:type: abx_pkg.BinaryOverrides
:value: >
   None

```{autodoc2-docstring} abx_plugin_singlefile.binaries.SinglefileBinary.overrides
```

````

`````

````{py:data} SINGLEFILE_BINARY
:canonical: abx_plugin_singlefile.binaries.SINGLEFILE_BINARY
:value: >
   'SinglefileBinary(...)'

```{autodoc2-docstring} abx_plugin_singlefile.binaries.SINGLEFILE_BINARY
```

````
