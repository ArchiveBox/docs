# {py:mod}`abx_plugin_chrome.binaries`

```{py:module} abx_plugin_chrome.binaries
```

```{autodoc2-docstring} abx_plugin_chrome.binaries
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ChromeBinary <abx_plugin_chrome.binaries.ChromeBinary>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`autodetect_system_chrome_install <abx_plugin_chrome.binaries.autodetect_system_chrome_install>`
  - ```{autodoc2-docstring} abx_plugin_chrome.binaries.autodetect_system_chrome_install
    :summary:
    ```
* - {py:obj}`create_macos_app_symlink <abx_plugin_chrome.binaries.create_macos_app_symlink>`
  - ```{autodoc2-docstring} abx_plugin_chrome.binaries.create_macos_app_symlink
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CHROMIUM_BINARY_NAMES_LINUX <abx_plugin_chrome.binaries.CHROMIUM_BINARY_NAMES_LINUX>`
  - ```{autodoc2-docstring} abx_plugin_chrome.binaries.CHROMIUM_BINARY_NAMES_LINUX
    :summary:
    ```
* - {py:obj}`CHROMIUM_BINARY_NAMES_MACOS <abx_plugin_chrome.binaries.CHROMIUM_BINARY_NAMES_MACOS>`
  - ```{autodoc2-docstring} abx_plugin_chrome.binaries.CHROMIUM_BINARY_NAMES_MACOS
    :summary:
    ```
* - {py:obj}`CHROMIUM_BINARY_NAMES <abx_plugin_chrome.binaries.CHROMIUM_BINARY_NAMES>`
  - ```{autodoc2-docstring} abx_plugin_chrome.binaries.CHROMIUM_BINARY_NAMES
    :summary:
    ```
* - {py:obj}`CHROME_BINARY_NAMES_LINUX <abx_plugin_chrome.binaries.CHROME_BINARY_NAMES_LINUX>`
  - ```{autodoc2-docstring} abx_plugin_chrome.binaries.CHROME_BINARY_NAMES_LINUX
    :summary:
    ```
* - {py:obj}`CHROME_BINARY_NAMES_MACOS <abx_plugin_chrome.binaries.CHROME_BINARY_NAMES_MACOS>`
  - ```{autodoc2-docstring} abx_plugin_chrome.binaries.CHROME_BINARY_NAMES_MACOS
    :summary:
    ```
* - {py:obj}`CHROME_BINARY_NAMES <abx_plugin_chrome.binaries.CHROME_BINARY_NAMES>`
  - ```{autodoc2-docstring} abx_plugin_chrome.binaries.CHROME_BINARY_NAMES
    :summary:
    ```
* - {py:obj}`CHROME_APT_DEPENDENCIES <abx_plugin_chrome.binaries.CHROME_APT_DEPENDENCIES>`
  - ```{autodoc2-docstring} abx_plugin_chrome.binaries.CHROME_APT_DEPENDENCIES
    :summary:
    ```
* - {py:obj}`CHROME_BINARY <abx_plugin_chrome.binaries.CHROME_BINARY>`
  - ```{autodoc2-docstring} abx_plugin_chrome.binaries.CHROME_BINARY
    :summary:
    ```
````

### API

````{py:data} CHROMIUM_BINARY_NAMES_LINUX
:canonical: abx_plugin_chrome.binaries.CHROMIUM_BINARY_NAMES_LINUX
:value: >
   ['chromium', 'chromium-browser', 'chromium-browser-beta', 'chromium-browser-unstable', 'chromium-bro...

```{autodoc2-docstring} abx_plugin_chrome.binaries.CHROMIUM_BINARY_NAMES_LINUX
```

````

````{py:data} CHROMIUM_BINARY_NAMES_MACOS
:canonical: abx_plugin_chrome.binaries.CHROMIUM_BINARY_NAMES_MACOS
:value: >
   ['/Applications/Chromium.app/Contents/MacOS/Chromium']

```{autodoc2-docstring} abx_plugin_chrome.binaries.CHROMIUM_BINARY_NAMES_MACOS
```

````

````{py:data} CHROMIUM_BINARY_NAMES
:canonical: abx_plugin_chrome.binaries.CHROMIUM_BINARY_NAMES
:value: >
   None

```{autodoc2-docstring} abx_plugin_chrome.binaries.CHROMIUM_BINARY_NAMES
```

````

````{py:data} CHROME_BINARY_NAMES_LINUX
:canonical: abx_plugin_chrome.binaries.CHROME_BINARY_NAMES_LINUX
:value: >
   ['google-chrome', 'google-chrome-stable', 'google-chrome-beta', 'google-chrome-canary', 'google-chro...

```{autodoc2-docstring} abx_plugin_chrome.binaries.CHROME_BINARY_NAMES_LINUX
```

````

````{py:data} CHROME_BINARY_NAMES_MACOS
:canonical: abx_plugin_chrome.binaries.CHROME_BINARY_NAMES_MACOS
:value: >
   ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/Applications/Google Chrome Canary...

```{autodoc2-docstring} abx_plugin_chrome.binaries.CHROME_BINARY_NAMES_MACOS
```

````

````{py:data} CHROME_BINARY_NAMES
:canonical: abx_plugin_chrome.binaries.CHROME_BINARY_NAMES
:value: >
   None

```{autodoc2-docstring} abx_plugin_chrome.binaries.CHROME_BINARY_NAMES
```

````

````{py:data} CHROME_APT_DEPENDENCIES
:canonical: abx_plugin_chrome.binaries.CHROME_APT_DEPENDENCIES
:value: >
   ['apt-transport-https', 'at-spi2-common', 'fontconfig', 'fonts-freefont-ttf', 'fonts-ipafont-gothic'...

```{autodoc2-docstring} abx_plugin_chrome.binaries.CHROME_APT_DEPENDENCIES
```

````

````{py:function} autodetect_system_chrome_install(PATH=None) -> typing.Optional[pathlib.Path]
:canonical: abx_plugin_chrome.binaries.autodetect_system_chrome_install

```{autodoc2-docstring} abx_plugin_chrome.binaries.autodetect_system_chrome_install
```
````

````{py:function} create_macos_app_symlink(target: pathlib.Path, shortcut: pathlib.Path)
:canonical: abx_plugin_chrome.binaries.create_macos_app_symlink

```{autodoc2-docstring} abx_plugin_chrome.binaries.create_macos_app_symlink
```
````

`````{py:class} ChromeBinary(/, **data: typing.Any)
:canonical: abx_plugin_chrome.binaries.ChromeBinary

Bases: {py:obj}`pydantic_pkgr.Binary`

````{py:attribute} name
:canonical: abx_plugin_chrome.binaries.ChromeBinary.name
:type: pydantic_pkgr.BinName
:value: >
   None

```{autodoc2-docstring} abx_plugin_chrome.binaries.ChromeBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: abx_plugin_chrome.binaries.ChromeBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} abx_plugin_chrome.binaries.ChromeBinary.binproviders_supported
```

````

````{py:attribute} overrides
:canonical: abx_plugin_chrome.binaries.ChromeBinary.overrides
:type: pydantic_pkgr.BinaryOverrides
:value: >
   None

```{autodoc2-docstring} abx_plugin_chrome.binaries.ChromeBinary.overrides
```

````

````{py:method} symlink_to_lib(binary, bin_dir=None) -> None
:canonical: abx_plugin_chrome.binaries.ChromeBinary.symlink_to_lib
:staticmethod:

```{autodoc2-docstring} abx_plugin_chrome.binaries.ChromeBinary.symlink_to_lib
```

````

````{py:method} chrome_cleanup_lockfile()
:canonical: abx_plugin_chrome.binaries.ChromeBinary.chrome_cleanup_lockfile
:staticmethod:

```{autodoc2-docstring} abx_plugin_chrome.binaries.ChromeBinary.chrome_cleanup_lockfile
```

````

`````

````{py:data} CHROME_BINARY
:canonical: abx_plugin_chrome.binaries.CHROME_BINARY
:value: >
   'ChromeBinary(...)'

```{autodoc2-docstring} abx_plugin_chrome.binaries.CHROME_BINARY
```

````
