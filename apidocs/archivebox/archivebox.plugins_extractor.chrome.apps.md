# {py:mod}`archivebox.plugins_extractor.chrome.apps`

```{py:module} archivebox.plugins_extractor.chrome.apps
```

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ChromeConfig <archivebox.plugins_extractor.chrome.apps.ChromeConfig>`
  -
* - {py:obj}`ChromeBinary <archivebox.plugins_extractor.chrome.apps.ChromeBinary>`
  -
* - {py:obj}`ChromePlugin <archivebox.plugins_extractor.chrome.apps.ChromePlugin>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`autodetect_system_chrome_install <archivebox.plugins_extractor.chrome.apps.autodetect_system_chrome_install>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.autodetect_system_chrome_install
    :summary:
    ```
* - {py:obj}`create_macos_app_symlink <archivebox.plugins_extractor.chrome.apps.create_macos_app_symlink>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.create_macos_app_symlink
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.plugins_extractor.chrome.apps.__package__>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.__package__
    :summary:
    ```
* - {py:obj}`CHROMIUM_BINARY_NAMES_LINUX <archivebox.plugins_extractor.chrome.apps.CHROMIUM_BINARY_NAMES_LINUX>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.CHROMIUM_BINARY_NAMES_LINUX
    :summary:
    ```
* - {py:obj}`CHROMIUM_BINARY_NAMES_MACOS <archivebox.plugins_extractor.chrome.apps.CHROMIUM_BINARY_NAMES_MACOS>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.CHROMIUM_BINARY_NAMES_MACOS
    :summary:
    ```
* - {py:obj}`CHROMIUM_BINARY_NAMES <archivebox.plugins_extractor.chrome.apps.CHROMIUM_BINARY_NAMES>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.CHROMIUM_BINARY_NAMES
    :summary:
    ```
* - {py:obj}`CHROME_BINARY_NAMES_LINUX <archivebox.plugins_extractor.chrome.apps.CHROME_BINARY_NAMES_LINUX>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.CHROME_BINARY_NAMES_LINUX
    :summary:
    ```
* - {py:obj}`CHROME_BINARY_NAMES_MACOS <archivebox.plugins_extractor.chrome.apps.CHROME_BINARY_NAMES_MACOS>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.CHROME_BINARY_NAMES_MACOS
    :summary:
    ```
* - {py:obj}`CHROME_BINARY_NAMES <archivebox.plugins_extractor.chrome.apps.CHROME_BINARY_NAMES>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.CHROME_BINARY_NAMES
    :summary:
    ```
* - {py:obj}`CHROME_CONFIG <archivebox.plugins_extractor.chrome.apps.CHROME_CONFIG>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.CHROME_CONFIG
    :summary:
    ```
* - {py:obj}`CHROME_BINARY <archivebox.plugins_extractor.chrome.apps.CHROME_BINARY>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.CHROME_BINARY
    :summary:
    ```
* - {py:obj}`PLUGIN <archivebox.plugins_extractor.chrome.apps.PLUGIN>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.PLUGIN
    :summary:
    ```
* - {py:obj}`DJANGO_APP <archivebox.plugins_extractor.chrome.apps.DJANGO_APP>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.DJANGO_APP
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.plugins_extractor.chrome.apps.__package__
:value: >
   'archivebox.plugins_extractor.chrome'

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.__package__
```

````

````{py:data} CHROMIUM_BINARY_NAMES_LINUX
:canonical: archivebox.plugins_extractor.chrome.apps.CHROMIUM_BINARY_NAMES_LINUX
:value: >
   ['chromium', 'chromium-browser', 'chromium-browser-beta', 'chromium-browser-unstable', 'chromium-bro...

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.CHROMIUM_BINARY_NAMES_LINUX
```

````

````{py:data} CHROMIUM_BINARY_NAMES_MACOS
:canonical: archivebox.plugins_extractor.chrome.apps.CHROMIUM_BINARY_NAMES_MACOS
:value: >
   ['/Applications/Chromium.app/Contents/MacOS/Chromium']

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.CHROMIUM_BINARY_NAMES_MACOS
```

````

````{py:data} CHROMIUM_BINARY_NAMES
:canonical: archivebox.plugins_extractor.chrome.apps.CHROMIUM_BINARY_NAMES
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.CHROMIUM_BINARY_NAMES
```

````

````{py:data} CHROME_BINARY_NAMES_LINUX
:canonical: archivebox.plugins_extractor.chrome.apps.CHROME_BINARY_NAMES_LINUX
:value: >
   ['google-chrome', 'google-chrome-stable', 'google-chrome-beta', 'google-chrome-canary', 'google-chro...

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.CHROME_BINARY_NAMES_LINUX
```

````

````{py:data} CHROME_BINARY_NAMES_MACOS
:canonical: archivebox.plugins_extractor.chrome.apps.CHROME_BINARY_NAMES_MACOS
:value: >
   ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/Applications/Google Chrome Canary...

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.CHROME_BINARY_NAMES_MACOS
```

````

````{py:data} CHROME_BINARY_NAMES
:canonical: archivebox.plugins_extractor.chrome.apps.CHROME_BINARY_NAMES
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.CHROME_BINARY_NAMES
```

````

````{py:function} autodetect_system_chrome_install(PATH=None) -> typing.Optional[pathlib.Path]
:canonical: archivebox.plugins_extractor.chrome.apps.autodetect_system_chrome_install

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.autodetect_system_chrome_install
```
````

````{py:function} create_macos_app_symlink(target: pathlib.Path, shortcut: pathlib.Path)
:canonical: archivebox.plugins_extractor.chrome.apps.create_macos_app_symlink

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.create_macos_app_symlink
```
````

`````{py:class} ChromeConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_implicit_flags: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeConfig

Bases: {py:obj}`abx.archivebox.base_configset.BaseConfigSet`

````{py:attribute} USE_CHROME
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeConfig.USE_CHROME
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromeConfig.USE_CHROME
```

````

````{py:attribute} CHROME_BINARY
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeConfig.CHROME_BINARY
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromeConfig.CHROME_BINARY
```

````

````{py:attribute} CHROME_DEFAULT_ARGS
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeConfig.CHROME_DEFAULT_ARGS
:type: typing.List[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromeConfig.CHROME_DEFAULT_ARGS
```

````

````{py:attribute} CHROME_EXTRA_ARGS
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeConfig.CHROME_EXTRA_ARGS
:type: typing.List[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromeConfig.CHROME_EXTRA_ARGS
```

````

````{py:attribute} CHROME_TIMEOUT
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeConfig.CHROME_TIMEOUT
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromeConfig.CHROME_TIMEOUT
```

````

````{py:attribute} CHROME_HEADLESS
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeConfig.CHROME_HEADLESS
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromeConfig.CHROME_HEADLESS
```

````

````{py:attribute} CHROME_SANDBOX
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeConfig.CHROME_SANDBOX
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromeConfig.CHROME_SANDBOX
```

````

````{py:attribute} CHROME_RESOLUTION
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeConfig.CHROME_RESOLUTION
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromeConfig.CHROME_RESOLUTION
```

````

````{py:attribute} CHROME_CHECK_SSL_VALIDITY
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeConfig.CHROME_CHECK_SSL_VALIDITY
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromeConfig.CHROME_CHECK_SSL_VALIDITY
```

````

````{py:attribute} CHROME_USER_AGENT
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeConfig.CHROME_USER_AGENT
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromeConfig.CHROME_USER_AGENT
```

````

````{py:attribute} CHROME_USER_DATA_DIR
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeConfig.CHROME_USER_DATA_DIR
:type: pathlib.Path | None
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromeConfig.CHROME_USER_DATA_DIR
```

````

````{py:attribute} CHROME_PROFILE_NAME
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeConfig.CHROME_PROFILE_NAME
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromeConfig.CHROME_PROFILE_NAME
```

````

````{py:attribute} SAVE_SCREENSHOT
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeConfig.SAVE_SCREENSHOT
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromeConfig.SAVE_SCREENSHOT
```

````

````{py:attribute} SAVE_DOM
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeConfig.SAVE_DOM
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromeConfig.SAVE_DOM
```

````

````{py:attribute} SAVE_PDF
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeConfig.SAVE_PDF
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromeConfig.SAVE_PDF
```

````

````{py:method} validate_use_chrome()
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeConfig.validate_use_chrome

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromeConfig.validate_use_chrome
```

````

````{py:method} chrome_args(**options) -> typing.List[str]
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeConfig.chrome_args

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromeConfig.chrome_args
```

````

`````

````{py:data} CHROME_CONFIG
:canonical: archivebox.plugins_extractor.chrome.apps.CHROME_CONFIG
:value: >
   'ChromeConfig(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.CHROME_CONFIG
```

````

`````{py:class} ChromeBinary(/, **data: typing.Any)
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeBinary

Bases: {py:obj}`abx.archivebox.base_binary.BaseBinary`

````{py:attribute} name
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeBinary.name
:type: pydantic_pkgr.BinName
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromeBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromeBinary.binproviders_supported
```

````

````{py:attribute} provider_overrides
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeBinary.provider_overrides
:type: typing.Dict[pydantic_pkgr.BinProviderName, pydantic_pkgr.ProviderLookupDict]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromeBinary.provider_overrides
```

````

````{py:method} symlink_to_lib(binary, bin_dir=CONSTANTS.LIB_BIN_DIR) -> None
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeBinary.symlink_to_lib
:staticmethod:

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromeBinary.symlink_to_lib
```

````

````{py:method} chrome_cleanup_lockfile()
:canonical: archivebox.plugins_extractor.chrome.apps.ChromeBinary.chrome_cleanup_lockfile
:staticmethod:

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromeBinary.chrome_cleanup_lockfile
```

````

`````

````{py:data} CHROME_BINARY
:canonical: archivebox.plugins_extractor.chrome.apps.CHROME_BINARY
:value: >
   'ChromeBinary(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.CHROME_BINARY
```

````

`````{py:class} ChromePlugin(/, **data: typing.Any)
:canonical: archivebox.plugins_extractor.chrome.apps.ChromePlugin

Bases: {py:obj}`abx.archivebox.base_plugin.BasePlugin`

````{py:attribute} app_label
:canonical: archivebox.plugins_extractor.chrome.apps.ChromePlugin.app_label
:type: str
:value: >
   'chrome'

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromePlugin.app_label
```

````

````{py:attribute} verbose_name
:canonical: archivebox.plugins_extractor.chrome.apps.ChromePlugin.verbose_name
:type: str
:value: >
   'Chrome Browser'

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromePlugin.verbose_name
```

````

````{py:attribute} hooks
:canonical: archivebox.plugins_extractor.chrome.apps.ChromePlugin.hooks
:type: typing.List[pydantic.InstanceOf[abx.archivebox.base_hook.BaseHook]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.ChromePlugin.hooks
```

````

`````

````{py:data} PLUGIN
:canonical: archivebox.plugins_extractor.chrome.apps.PLUGIN
:value: >
   'ChromePlugin(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.PLUGIN
```

````

````{py:data} DJANGO_APP
:canonical: archivebox.plugins_extractor.chrome.apps.DJANGO_APP
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_extractor.chrome.apps.DJANGO_APP
```

````
