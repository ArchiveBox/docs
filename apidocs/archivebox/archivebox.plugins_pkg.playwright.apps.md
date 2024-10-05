# {py:mod}`archivebox.plugins_pkg.playwright.apps`

```{py:module} archivebox.plugins_pkg.playwright.apps
```

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PlaywrightConfigs <archivebox.plugins_pkg.playwright.apps.PlaywrightConfigs>`
  -
* - {py:obj}`PlaywrightBinary <archivebox.plugins_pkg.playwright.apps.PlaywrightBinary>`
  -
* - {py:obj}`PlaywrightBinProvider <archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider>`
  -
* - {py:obj}`PlaywrightPlugin <archivebox.plugins_pkg.playwright.apps.PlaywrightPlugin>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.plugins_pkg.playwright.apps.__package__>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.__package__
    :summary:
    ```
* - {py:obj}`PLAYWRIGHT_CONFIG <archivebox.plugins_pkg.playwright.apps.PLAYWRIGHT_CONFIG>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PLAYWRIGHT_CONFIG
    :summary:
    ```
* - {py:obj}`LIB_DIR_BROWSERS <archivebox.plugins_pkg.playwright.apps.LIB_DIR_BROWSERS>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.LIB_DIR_BROWSERS
    :summary:
    ```
* - {py:obj}`PLAYWRIGHT_BINARY <archivebox.plugins_pkg.playwright.apps.PLAYWRIGHT_BINARY>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PLAYWRIGHT_BINARY
    :summary:
    ```
* - {py:obj}`PLAYWRIGHT_BINPROVIDER <archivebox.plugins_pkg.playwright.apps.PLAYWRIGHT_BINPROVIDER>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PLAYWRIGHT_BINPROVIDER
    :summary:
    ```
* - {py:obj}`PLUGIN <archivebox.plugins_pkg.playwright.apps.PLUGIN>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PLUGIN
    :summary:
    ```
* - {py:obj}`DJANGO_APP <archivebox.plugins_pkg.playwright.apps.DJANGO_APP>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.DJANGO_APP
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.plugins_pkg.playwright.apps.__package__
:value: >
   'archivebox.plugins_pkg.playwright'

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.__package__
```

````

```{py:class} PlaywrightConfigs(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_implicit_flags: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.plugins_pkg.playwright.apps.PlaywrightConfigs

Bases: {py:obj}`abx.archivebox.base_configset.BaseConfigSet`

```

````{py:data} PLAYWRIGHT_CONFIG
:canonical: archivebox.plugins_pkg.playwright.apps.PLAYWRIGHT_CONFIG
:value: >
   'PlaywrightConfigs(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PLAYWRIGHT_CONFIG
```

````

````{py:data} LIB_DIR_BROWSERS
:canonical: archivebox.plugins_pkg.playwright.apps.LIB_DIR_BROWSERS
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.LIB_DIR_BROWSERS
```

````

`````{py:class} PlaywrightBinary(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.playwright.apps.PlaywrightBinary

Bases: {py:obj}`abx.archivebox.base_binary.BaseBinary`

````{py:attribute} name
:canonical: archivebox.plugins_pkg.playwright.apps.PlaywrightBinary.name
:type: pydantic_pkgr.BinName
:value: >
   'playwright'

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PlaywrightBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: archivebox.plugins_pkg.playwright.apps.PlaywrightBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PlaywrightBinary.binproviders_supported
```

````

`````

````{py:data} PLAYWRIGHT_BINARY
:canonical: archivebox.plugins_pkg.playwright.apps.PLAYWRIGHT_BINARY
:value: >
   'PlaywrightBinary(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PLAYWRIGHT_BINARY
```

````

`````{py:class} PlaywrightBinProvider(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider

Bases: {py:obj}`abx.archivebox.base_binary.BaseBinProvider`

````{py:attribute} name
:canonical: archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider.name
:type: pydantic_pkgr.BinProviderName
:value: >
   'playwright'

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider.name
```

````

````{py:attribute} INSTALLER_BIN
:canonical: archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider.INSTALLER_BIN
:type: pydantic_pkgr.BinName
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider.INSTALLER_BIN
```

````

````{py:attribute} PATH
:canonical: archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider.PATH
:type: pydantic_pkgr.PATHStr
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider.PATH
```

````

````{py:attribute} puppeteer_browsers_dir
:canonical: archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider.puppeteer_browsers_dir
:type: typing.Optional[pathlib.Path]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider.puppeteer_browsers_dir
```

````

````{py:attribute} puppeteer_install_args
:canonical: archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider.puppeteer_install_args
:type: typing.List[str]
:value: >
   ['install']

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider.puppeteer_install_args
```

````

````{py:attribute} packages_handler
:canonical: archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider.packages_handler
:type: pydantic_pkgr.ProviderLookupDict
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider.packages_handler
```

````

````{py:attribute} _browser_abspaths
:canonical: archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider._browser_abspaths
:type: typing.ClassVar[typing.Dict[str, pydantic_pkgr.HostBinPath]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider._browser_abspaths
```

````

````{py:property} INSTALLER_BIN_ABSPATH
:canonical: archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider.INSTALLER_BIN_ABSPATH
:type: pydantic_pkgr.HostBinPath | None

````

````{py:method} setup() -> None
:canonical: archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider.setup

````

````{py:method} installed_browser_bins(browser_name: str = '*') -> typing.List[pathlib.Path]
:canonical: archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider.installed_browser_bins

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider.installed_browser_bins
```

````

````{py:method} on_get_abspath(bin_name: pydantic_pkgr.BinName, **context) -> typing.Optional[pydantic_pkgr.HostBinPath]
:canonical: archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider.on_get_abspath

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider.on_get_abspath
```

````

````{py:method} on_install(bin_name: str, packages: typing.Optional[pydantic_pkgr.InstallArgs] = None, **context) -> str
:canonical: archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider.on_install

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PlaywrightBinProvider.on_install
```

````

`````

````{py:data} PLAYWRIGHT_BINPROVIDER
:canonical: archivebox.plugins_pkg.playwright.apps.PLAYWRIGHT_BINPROVIDER
:value: >
   'PlaywrightBinProvider(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PLAYWRIGHT_BINPROVIDER
```

````

`````{py:class} PlaywrightPlugin(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.playwright.apps.PlaywrightPlugin

Bases: {py:obj}`abx.archivebox.base_plugin.BasePlugin`

````{py:attribute} app_label
:canonical: archivebox.plugins_pkg.playwright.apps.PlaywrightPlugin.app_label
:type: str
:value: >
   'playwright'

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PlaywrightPlugin.app_label
```

````

````{py:attribute} verbose_name
:canonical: archivebox.plugins_pkg.playwright.apps.PlaywrightPlugin.verbose_name
:type: str
:value: >
   'Playwright (PIP)'

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PlaywrightPlugin.verbose_name
```

````

````{py:attribute} hooks
:canonical: archivebox.plugins_pkg.playwright.apps.PlaywrightPlugin.hooks
:type: typing.List[pydantic.InstanceOf[abx.archivebox.base_hook.BaseHook]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PlaywrightPlugin.hooks
```

````

`````

````{py:data} PLUGIN
:canonical: archivebox.plugins_pkg.playwright.apps.PLUGIN
:value: >
   'PlaywrightPlugin(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.PLUGIN
```

````

````{py:data} DJANGO_APP
:canonical: archivebox.plugins_pkg.playwright.apps.DJANGO_APP
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.playwright.apps.DJANGO_APP
```

````
