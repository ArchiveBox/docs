# {py:mod}`abx_plugin_playwright.binproviders`

```{py:module} abx_plugin_playwright.binproviders
```

```{autodoc2-docstring} abx_plugin_playwright.binproviders
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PlaywrightBinProvider <abx_plugin_playwright.binproviders.PlaywrightBinProvider>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`USER_PLAYWRIGHT_CACHE_DIR <abx_plugin_playwright.binproviders.USER_PLAYWRIGHT_CACHE_DIR>`
  - ```{autodoc2-docstring} abx_plugin_playwright.binproviders.USER_PLAYWRIGHT_CACHE_DIR
    :summary:
    ```
* - {py:obj}`MACOS_PLAYWRIGHT_CACHE_DIR <abx_plugin_playwright.binproviders.MACOS_PLAYWRIGHT_CACHE_DIR>`
  - ```{autodoc2-docstring} abx_plugin_playwright.binproviders.MACOS_PLAYWRIGHT_CACHE_DIR
    :summary:
    ```
* - {py:obj}`LINUX_PLAYWRIGHT_CACHE_DIR <abx_plugin_playwright.binproviders.LINUX_PLAYWRIGHT_CACHE_DIR>`
  - ```{autodoc2-docstring} abx_plugin_playwright.binproviders.LINUX_PLAYWRIGHT_CACHE_DIR
    :summary:
    ```
* - {py:obj}`PLAYWRIGHT_CACHE_DIR <abx_plugin_playwright.binproviders.PLAYWRIGHT_CACHE_DIR>`
  - ```{autodoc2-docstring} abx_plugin_playwright.binproviders.PLAYWRIGHT_CACHE_DIR
    :summary:
    ```
* - {py:obj}`PLAYWRIGHT_BINPROVIDER <abx_plugin_playwright.binproviders.PLAYWRIGHT_BINPROVIDER>`
  - ```{autodoc2-docstring} abx_plugin_playwright.binproviders.PLAYWRIGHT_BINPROVIDER
    :summary:
    ```
````

### API

````{py:data} USER_PLAYWRIGHT_CACHE_DIR
:canonical: abx_plugin_playwright.binproviders.USER_PLAYWRIGHT_CACHE_DIR
:type: str | None
:value: >
   'get(...)'

```{autodoc2-docstring} abx_plugin_playwright.binproviders.USER_PLAYWRIGHT_CACHE_DIR
```

````

````{py:data} MACOS_PLAYWRIGHT_CACHE_DIR
:canonical: abx_plugin_playwright.binproviders.MACOS_PLAYWRIGHT_CACHE_DIR
:type: pathlib.Path
:value: >
   'Path(...)'

```{autodoc2-docstring} abx_plugin_playwright.binproviders.MACOS_PLAYWRIGHT_CACHE_DIR
```

````

````{py:data} LINUX_PLAYWRIGHT_CACHE_DIR
:canonical: abx_plugin_playwright.binproviders.LINUX_PLAYWRIGHT_CACHE_DIR
:type: pathlib.Path
:value: >
   'Path(...)'

```{autodoc2-docstring} abx_plugin_playwright.binproviders.LINUX_PLAYWRIGHT_CACHE_DIR
```

````

````{py:data} PLAYWRIGHT_CACHE_DIR
:canonical: abx_plugin_playwright.binproviders.PLAYWRIGHT_CACHE_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} abx_plugin_playwright.binproviders.PLAYWRIGHT_CACHE_DIR
```

````

`````{py:class} PlaywrightBinProvider(/, **data: typing.Any)
:canonical: abx_plugin_playwright.binproviders.PlaywrightBinProvider

Bases: {py:obj}`pydantic_pkgr.BinProvider`

````{py:attribute} name
:canonical: abx_plugin_playwright.binproviders.PlaywrightBinProvider.name
:type: pydantic_pkgr.BinProviderName
:value: >
   'playwright'

```{autodoc2-docstring} abx_plugin_playwright.binproviders.PlaywrightBinProvider.name
```

````

````{py:attribute} INSTALLER_BIN
:canonical: abx_plugin_playwright.binproviders.PlaywrightBinProvider.INSTALLER_BIN
:type: pydantic_pkgr.BinName
:value: >
   None

```{autodoc2-docstring} abx_plugin_playwright.binproviders.PlaywrightBinProvider.INSTALLER_BIN
```

````

````{py:attribute} PATH
:canonical: abx_plugin_playwright.binproviders.PlaywrightBinProvider.PATH
:type: pydantic_pkgr.PATHStr
:value: >
   None

```{autodoc2-docstring} abx_plugin_playwright.binproviders.PlaywrightBinProvider.PATH
```

````

````{py:attribute} playwright_browsers_dir
:canonical: abx_plugin_playwright.binproviders.PlaywrightBinProvider.playwright_browsers_dir
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} abx_plugin_playwright.binproviders.PlaywrightBinProvider.playwright_browsers_dir
```

````

````{py:attribute} playwright_install_args
:canonical: abx_plugin_playwright.binproviders.PlaywrightBinProvider.playwright_install_args
:type: typing.List[str]
:value: >
   ['install']

```{autodoc2-docstring} abx_plugin_playwright.binproviders.PlaywrightBinProvider.playwright_install_args
```

````

````{py:attribute} packages_handler
:canonical: abx_plugin_playwright.binproviders.PlaywrightBinProvider.packages_handler
:type: pydantic_pkgr.BinProviderOverrides
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_playwright.binproviders.PlaywrightBinProvider.packages_handler
```

````

````{py:attribute} _browser_abspaths
:canonical: abx_plugin_playwright.binproviders.PlaywrightBinProvider._browser_abspaths
:type: typing.ClassVar[typing.Dict[str, pydantic_pkgr.HostBinPath]]
:value: >
   None

```{autodoc2-docstring} abx_plugin_playwright.binproviders.PlaywrightBinProvider._browser_abspaths
```

````

````{py:property} INSTALLER_BIN_ABSPATH
:canonical: abx_plugin_playwright.binproviders.PlaywrightBinProvider.INSTALLER_BIN_ABSPATH
:type: pydantic_pkgr.HostBinPath | None

````

````{py:method} setup() -> None
:canonical: abx_plugin_playwright.binproviders.PlaywrightBinProvider.setup

````

````{py:method} installed_browser_bins(browser_name: str = '*') -> typing.List[pathlib.Path]
:canonical: abx_plugin_playwright.binproviders.PlaywrightBinProvider.installed_browser_bins

```{autodoc2-docstring} abx_plugin_playwright.binproviders.PlaywrightBinProvider.installed_browser_bins
```

````

````{py:method} default_abspath_handler(bin_name: pydantic_pkgr.BinName, **context) -> typing.Optional[pydantic_pkgr.HostBinPath]
:canonical: abx_plugin_playwright.binproviders.PlaywrightBinProvider.default_abspath_handler

```{autodoc2-docstring} abx_plugin_playwright.binproviders.PlaywrightBinProvider.default_abspath_handler
```

````

````{py:method} default_install_handler(bin_name: str, packages: typing.Optional[pydantic_pkgr.InstallArgs] = None, **context) -> str
:canonical: abx_plugin_playwright.binproviders.PlaywrightBinProvider.default_install_handler

```{autodoc2-docstring} abx_plugin_playwright.binproviders.PlaywrightBinProvider.default_install_handler
```

````

`````

````{py:data} PLAYWRIGHT_BINPROVIDER
:canonical: abx_plugin_playwright.binproviders.PLAYWRIGHT_BINPROVIDER
:value: >
   'PlaywrightBinProvider(...)'

```{autodoc2-docstring} abx_plugin_playwright.binproviders.PLAYWRIGHT_BINPROVIDER
```

````
