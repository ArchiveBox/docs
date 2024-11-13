# {py:mod}`abx_plugin_chrome.config`

```{py:module} abx_plugin_chrome.config
```

```{autodoc2-docstring} abx_plugin_chrome.config
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ChromeConfig <abx_plugin_chrome.config.ChromeConfig>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`autodetect_system_chrome_install <abx_plugin_chrome.config.autodetect_system_chrome_install>`
  - ```{autodoc2-docstring} abx_plugin_chrome.config.autodetect_system_chrome_install
    :summary:
    ```
* - {py:obj}`create_macos_app_symlink <abx_plugin_chrome.config.create_macos_app_symlink>`
  - ```{autodoc2-docstring} abx_plugin_chrome.config.create_macos_app_symlink
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CHROMIUM_BINARY_NAMES_LINUX <abx_plugin_chrome.config.CHROMIUM_BINARY_NAMES_LINUX>`
  - ```{autodoc2-docstring} abx_plugin_chrome.config.CHROMIUM_BINARY_NAMES_LINUX
    :summary:
    ```
* - {py:obj}`CHROMIUM_BINARY_NAMES_MACOS <abx_plugin_chrome.config.CHROMIUM_BINARY_NAMES_MACOS>`
  - ```{autodoc2-docstring} abx_plugin_chrome.config.CHROMIUM_BINARY_NAMES_MACOS
    :summary:
    ```
* - {py:obj}`CHROMIUM_BINARY_NAMES <abx_plugin_chrome.config.CHROMIUM_BINARY_NAMES>`
  - ```{autodoc2-docstring} abx_plugin_chrome.config.CHROMIUM_BINARY_NAMES
    :summary:
    ```
* - {py:obj}`CHROME_BINARY_NAMES_LINUX <abx_plugin_chrome.config.CHROME_BINARY_NAMES_LINUX>`
  - ```{autodoc2-docstring} abx_plugin_chrome.config.CHROME_BINARY_NAMES_LINUX
    :summary:
    ```
* - {py:obj}`CHROME_BINARY_NAMES_MACOS <abx_plugin_chrome.config.CHROME_BINARY_NAMES_MACOS>`
  - ```{autodoc2-docstring} abx_plugin_chrome.config.CHROME_BINARY_NAMES_MACOS
    :summary:
    ```
* - {py:obj}`CHROME_BINARY_NAMES <abx_plugin_chrome.config.CHROME_BINARY_NAMES>`
  - ```{autodoc2-docstring} abx_plugin_chrome.config.CHROME_BINARY_NAMES
    :summary:
    ```
* - {py:obj}`APT_DEPENDENCIES <abx_plugin_chrome.config.APT_DEPENDENCIES>`
  - ```{autodoc2-docstring} abx_plugin_chrome.config.APT_DEPENDENCIES
    :summary:
    ```
* - {py:obj}`CHROME_CONFIG <abx_plugin_chrome.config.CHROME_CONFIG>`
  - ```{autodoc2-docstring} abx_plugin_chrome.config.CHROME_CONFIG
    :summary:
    ```
````

### API

````{py:data} CHROMIUM_BINARY_NAMES_LINUX
:canonical: abx_plugin_chrome.config.CHROMIUM_BINARY_NAMES_LINUX
:value: >
   ['chromium', 'chromium-browser', 'chromium-browser-beta', 'chromium-browser-unstable', 'chromium-bro...

```{autodoc2-docstring} abx_plugin_chrome.config.CHROMIUM_BINARY_NAMES_LINUX
```

````

````{py:data} CHROMIUM_BINARY_NAMES_MACOS
:canonical: abx_plugin_chrome.config.CHROMIUM_BINARY_NAMES_MACOS
:value: >
   ['/Applications/Chromium.app/Contents/MacOS/Chromium']

```{autodoc2-docstring} abx_plugin_chrome.config.CHROMIUM_BINARY_NAMES_MACOS
```

````

````{py:data} CHROMIUM_BINARY_NAMES
:canonical: abx_plugin_chrome.config.CHROMIUM_BINARY_NAMES
:value: >
   None

```{autodoc2-docstring} abx_plugin_chrome.config.CHROMIUM_BINARY_NAMES
```

````

````{py:data} CHROME_BINARY_NAMES_LINUX
:canonical: abx_plugin_chrome.config.CHROME_BINARY_NAMES_LINUX
:value: >
   ['google-chrome', 'google-chrome-stable', 'google-chrome-beta', 'google-chrome-canary', 'google-chro...

```{autodoc2-docstring} abx_plugin_chrome.config.CHROME_BINARY_NAMES_LINUX
```

````

````{py:data} CHROME_BINARY_NAMES_MACOS
:canonical: abx_plugin_chrome.config.CHROME_BINARY_NAMES_MACOS
:value: >
   ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/Applications/Google Chrome Canary...

```{autodoc2-docstring} abx_plugin_chrome.config.CHROME_BINARY_NAMES_MACOS
```

````

````{py:data} CHROME_BINARY_NAMES
:canonical: abx_plugin_chrome.config.CHROME_BINARY_NAMES
:value: >
   None

```{autodoc2-docstring} abx_plugin_chrome.config.CHROME_BINARY_NAMES
```

````

````{py:data} APT_DEPENDENCIES
:canonical: abx_plugin_chrome.config.APT_DEPENDENCIES
:value: >
   ['apt-transport-https', 'at-spi2-common', 'chromium-browser', 'fontconfig', 'fonts-freefont-ttf', 'f...

```{autodoc2-docstring} abx_plugin_chrome.config.APT_DEPENDENCIES
```

````

````{py:function} autodetect_system_chrome_install(PATH=None) -> typing.Optional[pathlib.Path]
:canonical: abx_plugin_chrome.config.autodetect_system_chrome_install

```{autodoc2-docstring} abx_plugin_chrome.config.autodetect_system_chrome_install
```
````

````{py:function} create_macos_app_symlink(target: pathlib.Path, shortcut: pathlib.Path)
:canonical: abx_plugin_chrome.config.create_macos_app_symlink

```{autodoc2-docstring} abx_plugin_chrome.config.create_macos_app_symlink
```
````

`````{py:class} ChromeConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | None = None, _cli_ignore_unknown_args: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: abx_plugin_chrome.config.ChromeConfig

Bases: {py:obj}`abx_spec_config.base_configset.BaseConfigSet`

````{py:attribute} USE_CHROME
:canonical: abx_plugin_chrome.config.ChromeConfig.USE_CHROME
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_chrome.config.ChromeConfig.USE_CHROME
```

````

````{py:attribute} CHROME_BINARY
:canonical: abx_plugin_chrome.config.ChromeConfig.CHROME_BINARY
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_chrome.config.ChromeConfig.CHROME_BINARY
```

````

````{py:attribute} CHROME_DEFAULT_ARGS
:canonical: abx_plugin_chrome.config.ChromeConfig.CHROME_DEFAULT_ARGS
:type: typing.List[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_chrome.config.ChromeConfig.CHROME_DEFAULT_ARGS
```

````

````{py:attribute} CHROME_EXTRA_ARGS
:canonical: abx_plugin_chrome.config.ChromeConfig.CHROME_EXTRA_ARGS
:type: typing.List[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_chrome.config.ChromeConfig.CHROME_EXTRA_ARGS
```

````

````{py:attribute} CHROME_TIMEOUT
:canonical: abx_plugin_chrome.config.ChromeConfig.CHROME_TIMEOUT
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_chrome.config.ChromeConfig.CHROME_TIMEOUT
```

````

````{py:attribute} CHROME_HEADLESS
:canonical: abx_plugin_chrome.config.ChromeConfig.CHROME_HEADLESS
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_chrome.config.ChromeConfig.CHROME_HEADLESS
```

````

````{py:attribute} CHROME_SANDBOX
:canonical: abx_plugin_chrome.config.ChromeConfig.CHROME_SANDBOX
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_chrome.config.ChromeConfig.CHROME_SANDBOX
```

````

````{py:attribute} CHROME_RESOLUTION
:canonical: abx_plugin_chrome.config.ChromeConfig.CHROME_RESOLUTION
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_chrome.config.ChromeConfig.CHROME_RESOLUTION
```

````

````{py:attribute} CHROME_CHECK_SSL_VALIDITY
:canonical: abx_plugin_chrome.config.ChromeConfig.CHROME_CHECK_SSL_VALIDITY
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_chrome.config.ChromeConfig.CHROME_CHECK_SSL_VALIDITY
```

````

````{py:attribute} CHROME_USER_AGENT
:canonical: abx_plugin_chrome.config.ChromeConfig.CHROME_USER_AGENT
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_chrome.config.ChromeConfig.CHROME_USER_AGENT
```

````

````{py:attribute} CHROME_USER_DATA_DIR
:canonical: abx_plugin_chrome.config.ChromeConfig.CHROME_USER_DATA_DIR
:type: pathlib.Path | None
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_chrome.config.ChromeConfig.CHROME_USER_DATA_DIR
```

````

````{py:attribute} CHROME_PROFILE_NAME
:canonical: abx_plugin_chrome.config.ChromeConfig.CHROME_PROFILE_NAME
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_chrome.config.ChromeConfig.CHROME_PROFILE_NAME
```

````

````{py:attribute} SAVE_SCREENSHOT
:canonical: abx_plugin_chrome.config.ChromeConfig.SAVE_SCREENSHOT
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_chrome.config.ChromeConfig.SAVE_SCREENSHOT
```

````

````{py:attribute} SAVE_DOM
:canonical: abx_plugin_chrome.config.ChromeConfig.SAVE_DOM
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_chrome.config.ChromeConfig.SAVE_DOM
```

````

````{py:attribute} SAVE_PDF
:canonical: abx_plugin_chrome.config.ChromeConfig.SAVE_PDF
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_chrome.config.ChromeConfig.SAVE_PDF
```

````

````{py:method} validate()
:canonical: abx_plugin_chrome.config.ChromeConfig.validate

````

````{py:method} chrome_args(**options) -> typing.List[str]
:canonical: abx_plugin_chrome.config.ChromeConfig.chrome_args

```{autodoc2-docstring} abx_plugin_chrome.config.ChromeConfig.chrome_args
```

````

`````

````{py:data} CHROME_CONFIG
:canonical: abx_plugin_chrome.config.CHROME_CONFIG
:value: >
   'ChromeConfig(...)'

```{autodoc2-docstring} abx_plugin_chrome.config.CHROME_CONFIG
```

````
