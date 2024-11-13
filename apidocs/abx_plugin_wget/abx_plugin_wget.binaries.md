# {py:mod}`abx_plugin_wget.binaries`

```{py:module} abx_plugin_wget.binaries
```

```{autodoc2-docstring} abx_plugin_wget.binaries
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`WgetBinary <abx_plugin_wget.binaries.WgetBinary>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <abx_plugin_wget.binaries.__package__>`
  - ```{autodoc2-docstring} abx_plugin_wget.binaries.__package__
    :summary:
    ```
* - {py:obj}`WGET_BINARY <abx_plugin_wget.binaries.WGET_BINARY>`
  - ```{autodoc2-docstring} abx_plugin_wget.binaries.WGET_BINARY
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: abx_plugin_wget.binaries.__package__
:value: >
   'abx_plugin_wget'

```{autodoc2-docstring} abx_plugin_wget.binaries.__package__
```

````

`````{py:class} WgetBinary(/, **data: typing.Any)
:canonical: abx_plugin_wget.binaries.WgetBinary

Bases: {py:obj}`pydantic_pkgr.Binary`

````{py:attribute} name
:canonical: abx_plugin_wget.binaries.WgetBinary.name
:type: pydantic_pkgr.BinName
:value: >
   None

```{autodoc2-docstring} abx_plugin_wget.binaries.WgetBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: abx_plugin_wget.binaries.WgetBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} abx_plugin_wget.binaries.WgetBinary.binproviders_supported
```

````

`````

````{py:data} WGET_BINARY
:canonical: abx_plugin_wget.binaries.WGET_BINARY
:value: >
   'WgetBinary(...)'

```{autodoc2-docstring} abx_plugin_wget.binaries.WGET_BINARY
```

````
