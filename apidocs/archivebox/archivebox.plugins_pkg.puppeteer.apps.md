# {py:mod}`archivebox.plugins_pkg.puppeteer.apps`

```{py:module} archivebox.plugins_pkg.puppeteer.apps
```

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PuppeteerConfigs <archivebox.plugins_pkg.puppeteer.apps.PuppeteerConfigs>`
  -
* - {py:obj}`PuppeteerBinary <archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinary>`
  -
* - {py:obj}`PuppeteerBinProvider <archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider>`
  -
* - {py:obj}`PuppeteerPlugin <archivebox.plugins_pkg.puppeteer.apps.PuppeteerPlugin>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.plugins_pkg.puppeteer.apps.__package__>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.__package__
    :summary:
    ```
* - {py:obj}`PUPPETEER_CONFIG <archivebox.plugins_pkg.puppeteer.apps.PUPPETEER_CONFIG>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PUPPETEER_CONFIG
    :summary:
    ```
* - {py:obj}`LIB_DIR_BROWSERS <archivebox.plugins_pkg.puppeteer.apps.LIB_DIR_BROWSERS>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.LIB_DIR_BROWSERS
    :summary:
    ```
* - {py:obj}`PUPPETEER_BINARY <archivebox.plugins_pkg.puppeteer.apps.PUPPETEER_BINARY>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PUPPETEER_BINARY
    :summary:
    ```
* - {py:obj}`PUPPETEER_BINPROVIDER <archivebox.plugins_pkg.puppeteer.apps.PUPPETEER_BINPROVIDER>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PUPPETEER_BINPROVIDER
    :summary:
    ```
* - {py:obj}`PLUGIN <archivebox.plugins_pkg.puppeteer.apps.PLUGIN>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PLUGIN
    :summary:
    ```
* - {py:obj}`DJANGO_APP <archivebox.plugins_pkg.puppeteer.apps.DJANGO_APP>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.DJANGO_APP
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.plugins_pkg.puppeteer.apps.__package__
:value: >
   'archivebox.plugins_pkg.puppeteer'

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.__package__
```

````

```{py:class} PuppeteerConfigs(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_implicit_flags: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.plugins_pkg.puppeteer.apps.PuppeteerConfigs

Bases: {py:obj}`abx.archivebox.base_configset.BaseConfigSet`

```

````{py:data} PUPPETEER_CONFIG
:canonical: archivebox.plugins_pkg.puppeteer.apps.PUPPETEER_CONFIG
:value: >
   'PuppeteerConfigs(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PUPPETEER_CONFIG
```

````

````{py:data} LIB_DIR_BROWSERS
:canonical: archivebox.plugins_pkg.puppeteer.apps.LIB_DIR_BROWSERS
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.LIB_DIR_BROWSERS
```

````

`````{py:class} PuppeteerBinary(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinary

Bases: {py:obj}`abx.archivebox.base_binary.BaseBinary`

````{py:attribute} name
:canonical: archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinary.name
:type: pydantic_pkgr.BinName
:value: >
   'puppeteer'

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinary.binproviders_supported
```

````

`````

````{py:data} PUPPETEER_BINARY
:canonical: archivebox.plugins_pkg.puppeteer.apps.PUPPETEER_BINARY
:value: >
   'PuppeteerBinary(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PUPPETEER_BINARY
```

````

`````{py:class} PuppeteerBinProvider(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider

Bases: {py:obj}`abx.archivebox.base_binary.BaseBinProvider`

````{py:attribute} name
:canonical: archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider.name
:type: pydantic_pkgr.BinProviderName
:value: >
   'puppeteer'

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider.name
```

````

````{py:attribute} INSTALLER_BIN
:canonical: archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider.INSTALLER_BIN
:type: pydantic_pkgr.BinName
:value: >
   'npx'

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider.INSTALLER_BIN
```

````

````{py:attribute} PATH
:canonical: archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider.PATH
:type: pydantic_pkgr.PATHStr
:value: >
   'str(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider.PATH
```

````

````{py:attribute} puppeteer_browsers_dir
:canonical: archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider.puppeteer_browsers_dir
:type: typing.Optional[pathlib.Path]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider.puppeteer_browsers_dir
```

````

````{py:attribute} puppeteer_install_args
:canonical: archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider.puppeteer_install_args
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider.puppeteer_install_args
```

````

````{py:attribute} packages_handler
:canonical: archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider.packages_handler
:type: pydantic_pkgr.ProviderLookupDict
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider.packages_handler
```

````

````{py:attribute} _browser_abspaths
:canonical: archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider._browser_abspaths
:type: typing.ClassVar[typing.Dict[str, pydantic_pkgr.HostBinPath]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider._browser_abspaths
```

````

````{py:method} setup() -> None
:canonical: archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider.setup

````

````{py:method} installed_browser_bins(browser_name: str = '*') -> typing.List[pathlib.Path]
:canonical: archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider.installed_browser_bins

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider.installed_browser_bins
```

````

````{py:method} on_get_abspath(bin_name: pydantic_pkgr.BinName, **context) -> typing.Optional[pydantic_pkgr.HostBinPath]
:canonical: archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider.on_get_abspath

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider.on_get_abspath
```

````

````{py:method} on_install(bin_name: str, packages: typing.Optional[pydantic_pkgr.InstallArgs] = None, **context) -> str
:canonical: archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider.on_install

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PuppeteerBinProvider.on_install
```

````

`````

````{py:data} PUPPETEER_BINPROVIDER
:canonical: archivebox.plugins_pkg.puppeteer.apps.PUPPETEER_BINPROVIDER
:value: >
   'PuppeteerBinProvider(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PUPPETEER_BINPROVIDER
```

````

`````{py:class} PuppeteerPlugin(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.puppeteer.apps.PuppeteerPlugin

Bases: {py:obj}`abx.archivebox.base_plugin.BasePlugin`

````{py:attribute} app_label
:canonical: archivebox.plugins_pkg.puppeteer.apps.PuppeteerPlugin.app_label
:type: str
:value: >
   'puppeteer'

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PuppeteerPlugin.app_label
```

````

````{py:attribute} verbose_name
:canonical: archivebox.plugins_pkg.puppeteer.apps.PuppeteerPlugin.verbose_name
:type: str
:value: >
   'Puppeteer (NPM)'

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PuppeteerPlugin.verbose_name
```

````

````{py:attribute} hooks
:canonical: archivebox.plugins_pkg.puppeteer.apps.PuppeteerPlugin.hooks
:type: typing.List[pydantic.InstanceOf[abx.archivebox.base_hook.BaseHook]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PuppeteerPlugin.hooks
```

````

`````

````{py:data} PLUGIN
:canonical: archivebox.plugins_pkg.puppeteer.apps.PLUGIN
:value: >
   'PuppeteerPlugin(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.PLUGIN
```

````

````{py:data} DJANGO_APP
:canonical: archivebox.plugins_pkg.puppeteer.apps.DJANGO_APP
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.puppeteer.apps.DJANGO_APP
```

````
