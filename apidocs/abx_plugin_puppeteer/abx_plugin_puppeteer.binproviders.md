# {py:mod}`abx_plugin_puppeteer.binproviders`

```{py:module} abx_plugin_puppeteer.binproviders
```

```{autodoc2-docstring} abx_plugin_puppeteer.binproviders
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PuppeteerBinProvider <abx_plugin_puppeteer.binproviders.PuppeteerBinProvider>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PUPPETEER_BINPROVIDER <abx_plugin_puppeteer.binproviders.PUPPETEER_BINPROVIDER>`
  - ```{autodoc2-docstring} abx_plugin_puppeteer.binproviders.PUPPETEER_BINPROVIDER
    :summary:
    ```
````

### API

`````{py:class} PuppeteerBinProvider(/, **data: typing.Any)
:canonical: abx_plugin_puppeteer.binproviders.PuppeteerBinProvider

Bases: {py:obj}`abx_pkg.BinProvider`

````{py:attribute} name
:canonical: abx_plugin_puppeteer.binproviders.PuppeteerBinProvider.name
:type: abx_pkg.BinProviderName
:value: >
   'puppeteer'

```{autodoc2-docstring} abx_plugin_puppeteer.binproviders.PuppeteerBinProvider.name
```

````

````{py:attribute} INSTALLER_BIN
:canonical: abx_plugin_puppeteer.binproviders.PuppeteerBinProvider.INSTALLER_BIN
:type: abx_pkg.BinName
:value: >
   'npx'

```{autodoc2-docstring} abx_plugin_puppeteer.binproviders.PuppeteerBinProvider.INSTALLER_BIN
```

````

````{py:attribute} PATH
:canonical: abx_plugin_puppeteer.binproviders.PuppeteerBinProvider.PATH
:type: abx_pkg.PATHStr
:value: >
   'str(...)'

```{autodoc2-docstring} abx_plugin_puppeteer.binproviders.PuppeteerBinProvider.PATH
```

````

````{py:attribute} euid
:canonical: abx_plugin_puppeteer.binproviders.PuppeteerBinProvider.euid
:type: typing.Optional[int]
:value: >
   None

```{autodoc2-docstring} abx_plugin_puppeteer.binproviders.PuppeteerBinProvider.euid
```

````

````{py:attribute} puppeteer_browsers_dir
:canonical: abx_plugin_puppeteer.binproviders.PuppeteerBinProvider.puppeteer_browsers_dir
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} abx_plugin_puppeteer.binproviders.PuppeteerBinProvider.puppeteer_browsers_dir
```

````

````{py:attribute} puppeteer_install_args
:canonical: abx_plugin_puppeteer.binproviders.PuppeteerBinProvider.puppeteer_install_args
:type: typing.List[str]
:value: >
   ['--yes', '@puppeteer/browsers', 'install']

```{autodoc2-docstring} abx_plugin_puppeteer.binproviders.PuppeteerBinProvider.puppeteer_install_args
```

````

````{py:attribute} packages_handler
:canonical: abx_plugin_puppeteer.binproviders.PuppeteerBinProvider.packages_handler
:type: abx_pkg.BinProviderOverrides
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_puppeteer.binproviders.PuppeteerBinProvider.packages_handler
```

````

````{py:attribute} _browser_abspaths
:canonical: abx_plugin_puppeteer.binproviders.PuppeteerBinProvider._browser_abspaths
:type: typing.ClassVar[typing.Dict[str, abx_pkg.HostBinPath]]
:value: >
   None

```{autodoc2-docstring} abx_plugin_puppeteer.binproviders.PuppeteerBinProvider._browser_abspaths
```

````

````{py:method} setup() -> None
:canonical: abx_plugin_puppeteer.binproviders.PuppeteerBinProvider.setup

````

````{py:method} installed_browser_bins(browser_name: str = '*') -> typing.List[pathlib.Path]
:canonical: abx_plugin_puppeteer.binproviders.PuppeteerBinProvider.installed_browser_bins

```{autodoc2-docstring} abx_plugin_puppeteer.binproviders.PuppeteerBinProvider.installed_browser_bins
```

````

````{py:method} default_abspath_handler(bin_name: abx_pkg.BinName, **context) -> typing.Optional[abx_pkg.HostBinPath]
:canonical: abx_plugin_puppeteer.binproviders.PuppeteerBinProvider.default_abspath_handler

```{autodoc2-docstring} abx_plugin_puppeteer.binproviders.PuppeteerBinProvider.default_abspath_handler
```

````

````{py:method} default_install_handler(bin_name: str, packages: typing.Optional[abx_pkg.InstallArgs] = None, **context) -> str
:canonical: abx_plugin_puppeteer.binproviders.PuppeteerBinProvider.default_install_handler

```{autodoc2-docstring} abx_plugin_puppeteer.binproviders.PuppeteerBinProvider.default_install_handler
```

````

`````

````{py:data} PUPPETEER_BINPROVIDER
:canonical: abx_plugin_puppeteer.binproviders.PUPPETEER_BINPROVIDER
:value: >
   'PuppeteerBinProvider(...)'

```{autodoc2-docstring} abx_plugin_puppeteer.binproviders.PUPPETEER_BINPROVIDER
```

````
