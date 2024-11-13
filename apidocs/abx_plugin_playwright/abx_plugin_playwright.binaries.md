# {py:mod}`abx_plugin_playwright.binaries`

```{py:module} abx_plugin_playwright.binaries
```

```{autodoc2-docstring} abx_plugin_playwright.binaries
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PlaywrightBinary <abx_plugin_playwright.binaries.PlaywrightBinary>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PLAYWRIGHT_BINARY <abx_plugin_playwright.binaries.PLAYWRIGHT_BINARY>`
  - ```{autodoc2-docstring} abx_plugin_playwright.binaries.PLAYWRIGHT_BINARY
    :summary:
    ```
````

### API

`````{py:class} PlaywrightBinary(/, **data: typing.Any)
:canonical: abx_plugin_playwright.binaries.PlaywrightBinary

Bases: {py:obj}`pydantic_pkgr.Binary`

````{py:attribute} name
:canonical: abx_plugin_playwright.binaries.PlaywrightBinary.name
:type: pydantic_pkgr.BinName
:value: >
   None

```{autodoc2-docstring} abx_plugin_playwright.binaries.PlaywrightBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: abx_plugin_playwright.binaries.PlaywrightBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} abx_plugin_playwright.binaries.PlaywrightBinary.binproviders_supported
```

````

`````

````{py:data} PLAYWRIGHT_BINARY
:canonical: abx_plugin_playwright.binaries.PLAYWRIGHT_BINARY
:value: >
   'PlaywrightBinary(...)'

```{autodoc2-docstring} abx_plugin_playwright.binaries.PLAYWRIGHT_BINARY
```

````
