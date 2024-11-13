# {py:mod}`abx_plugin_npm.binproviders`

```{py:module} abx_plugin_npm.binproviders
```

```{autodoc2-docstring} abx_plugin_npm.binproviders
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SystemNpmBinProvider <abx_plugin_npm.binproviders.SystemNpmBinProvider>`
  -
* - {py:obj}`LibNpmBinProvider <abx_plugin_npm.binproviders.LibNpmBinProvider>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DEFAULT_LIB_NPM_DIR <abx_plugin_npm.binproviders.DEFAULT_LIB_NPM_DIR>`
  - ```{autodoc2-docstring} abx_plugin_npm.binproviders.DEFAULT_LIB_NPM_DIR
    :summary:
    ```
* - {py:obj}`OLD_NODE_BIN_PATH <abx_plugin_npm.binproviders.OLD_NODE_BIN_PATH>`
  - ```{autodoc2-docstring} abx_plugin_npm.binproviders.OLD_NODE_BIN_PATH
    :summary:
    ```
* - {py:obj}`NEW_NODE_BIN_PATH <abx_plugin_npm.binproviders.NEW_NODE_BIN_PATH>`
  - ```{autodoc2-docstring} abx_plugin_npm.binproviders.NEW_NODE_BIN_PATH
    :summary:
    ```
* - {py:obj}`SYS_NPM_BINPROVIDER <abx_plugin_npm.binproviders.SYS_NPM_BINPROVIDER>`
  - ```{autodoc2-docstring} abx_plugin_npm.binproviders.SYS_NPM_BINPROVIDER
    :summary:
    ```
* - {py:obj}`LIB_NPM_BINPROVIDER <abx_plugin_npm.binproviders.LIB_NPM_BINPROVIDER>`
  - ```{autodoc2-docstring} abx_plugin_npm.binproviders.LIB_NPM_BINPROVIDER
    :summary:
    ```
* - {py:obj}`npm <abx_plugin_npm.binproviders.npm>`
  - ```{autodoc2-docstring} abx_plugin_npm.binproviders.npm
    :summary:
    ```
````

### API

````{py:data} DEFAULT_LIB_NPM_DIR
:canonical: abx_plugin_npm.binproviders.DEFAULT_LIB_NPM_DIR
:value: >
   'Path(...)'

```{autodoc2-docstring} abx_plugin_npm.binproviders.DEFAULT_LIB_NPM_DIR
```

````

````{py:data} OLD_NODE_BIN_PATH
:canonical: abx_plugin_npm.binproviders.OLD_NODE_BIN_PATH
:value: >
   None

```{autodoc2-docstring} abx_plugin_npm.binproviders.OLD_NODE_BIN_PATH
```

````

````{py:data} NEW_NODE_BIN_PATH
:canonical: abx_plugin_npm.binproviders.NEW_NODE_BIN_PATH
:value: >
   None

```{autodoc2-docstring} abx_plugin_npm.binproviders.NEW_NODE_BIN_PATH
```

````

`````{py:class} SystemNpmBinProvider(/, **data: typing.Any)
:canonical: abx_plugin_npm.binproviders.SystemNpmBinProvider

Bases: {py:obj}`pydantic_pkgr.NpmProvider`

````{py:attribute} name
:canonical: abx_plugin_npm.binproviders.SystemNpmBinProvider.name
:type: pydantic_pkgr.BinProviderName
:value: >
   'sys_npm'

```{autodoc2-docstring} abx_plugin_npm.binproviders.SystemNpmBinProvider.name
```

````

````{py:attribute} npm_prefix
:canonical: abx_plugin_npm.binproviders.SystemNpmBinProvider.npm_prefix
:type: typing.Optional[pathlib.Path]
:value: >
   None

```{autodoc2-docstring} abx_plugin_npm.binproviders.SystemNpmBinProvider.npm_prefix
```

````

`````

`````{py:class} LibNpmBinProvider(/, **data: typing.Any)
:canonical: abx_plugin_npm.binproviders.LibNpmBinProvider

Bases: {py:obj}`pydantic_pkgr.NpmProvider`

````{py:attribute} name
:canonical: abx_plugin_npm.binproviders.LibNpmBinProvider.name
:type: pydantic_pkgr.BinProviderName
:value: >
   'lib_npm'

```{autodoc2-docstring} abx_plugin_npm.binproviders.LibNpmBinProvider.name
```

````

````{py:attribute} PATH
:canonical: abx_plugin_npm.binproviders.LibNpmBinProvider.PATH
:type: pydantic_pkgr.PATHStr
:value: >
   None

```{autodoc2-docstring} abx_plugin_npm.binproviders.LibNpmBinProvider.PATH
```

````

````{py:attribute} npm_prefix
:canonical: abx_plugin_npm.binproviders.LibNpmBinProvider.npm_prefix
:type: typing.Optional[pathlib.Path]
:value: >
   None

```{autodoc2-docstring} abx_plugin_npm.binproviders.LibNpmBinProvider.npm_prefix
```

````

````{py:method} setup() -> None
:canonical: abx_plugin_npm.binproviders.LibNpmBinProvider.setup

````

`````

````{py:data} SYS_NPM_BINPROVIDER
:canonical: abx_plugin_npm.binproviders.SYS_NPM_BINPROVIDER
:value: >
   'SystemNpmBinProvider(...)'

```{autodoc2-docstring} abx_plugin_npm.binproviders.SYS_NPM_BINPROVIDER
```

````

````{py:data} LIB_NPM_BINPROVIDER
:canonical: abx_plugin_npm.binproviders.LIB_NPM_BINPROVIDER
:value: >
   'LibNpmBinProvider(...)'

```{autodoc2-docstring} abx_plugin_npm.binproviders.LIB_NPM_BINPROVIDER
```

````

````{py:data} npm
:canonical: abx_plugin_npm.binproviders.npm
:value: >
   None

```{autodoc2-docstring} abx_plugin_npm.binproviders.npm
```

````
