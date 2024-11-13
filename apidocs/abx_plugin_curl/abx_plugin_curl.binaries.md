# {py:mod}`abx_plugin_curl.binaries`

```{py:module} abx_plugin_curl.binaries
```

```{autodoc2-docstring} abx_plugin_curl.binaries
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CurlBinary <abx_plugin_curl.binaries.CurlBinary>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CURL_BINARY <abx_plugin_curl.binaries.CURL_BINARY>`
  - ```{autodoc2-docstring} abx_plugin_curl.binaries.CURL_BINARY
    :summary:
    ```
````

### API

`````{py:class} CurlBinary(/, **data: typing.Any)
:canonical: abx_plugin_curl.binaries.CurlBinary

Bases: {py:obj}`pydantic_pkgr.Binary`

````{py:attribute} name
:canonical: abx_plugin_curl.binaries.CurlBinary.name
:type: pydantic_pkgr.BinName
:value: >
   None

```{autodoc2-docstring} abx_plugin_curl.binaries.CurlBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: abx_plugin_curl.binaries.CurlBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} abx_plugin_curl.binaries.CurlBinary.binproviders_supported
```

````

`````

````{py:data} CURL_BINARY
:canonical: abx_plugin_curl.binaries.CURL_BINARY
:value: >
   'CurlBinary(...)'

```{autodoc2-docstring} abx_plugin_curl.binaries.CURL_BINARY
```

````
