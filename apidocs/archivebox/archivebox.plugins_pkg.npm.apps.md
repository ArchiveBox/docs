# {py:mod}`archivebox.plugins_pkg.npm.apps`

```{py:module} archivebox.plugins_pkg.npm.apps
```

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`NpmDependencyConfigs <archivebox.plugins_pkg.npm.apps.NpmDependencyConfigs>`
  -
* - {py:obj}`SystemNpmProvider <archivebox.plugins_pkg.npm.apps.SystemNpmProvider>`
  -
* - {py:obj}`LibNpmProvider <archivebox.plugins_pkg.npm.apps.LibNpmProvider>`
  -
* - {py:obj}`NpmBinary <archivebox.plugins_pkg.npm.apps.NpmBinary>`
  -
* - {py:obj}`NodeBinary <archivebox.plugins_pkg.npm.apps.NodeBinary>`
  -
* - {py:obj}`NpmPlugin <archivebox.plugins_pkg.npm.apps.NpmPlugin>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.plugins_pkg.npm.apps.__package__>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.__package__
    :summary:
    ```
* - {py:obj}`DEFAULT_GLOBAL_CONFIG <archivebox.plugins_pkg.npm.apps.DEFAULT_GLOBAL_CONFIG>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.DEFAULT_GLOBAL_CONFIG
    :summary:
    ```
* - {py:obj}`NPM_CONFIG <archivebox.plugins_pkg.npm.apps.NPM_CONFIG>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.NPM_CONFIG
    :summary:
    ```
* - {py:obj}`OLD_NODE_BIN_PATH <archivebox.plugins_pkg.npm.apps.OLD_NODE_BIN_PATH>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.OLD_NODE_BIN_PATH
    :summary:
    ```
* - {py:obj}`NEW_NODE_BIN_PATH <archivebox.plugins_pkg.npm.apps.NEW_NODE_BIN_PATH>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.NEW_NODE_BIN_PATH
    :summary:
    ```
* - {py:obj}`SYS_NPM_BINPROVIDER <archivebox.plugins_pkg.npm.apps.SYS_NPM_BINPROVIDER>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.SYS_NPM_BINPROVIDER
    :summary:
    ```
* - {py:obj}`LIB_NPM_BINPROVIDER <archivebox.plugins_pkg.npm.apps.LIB_NPM_BINPROVIDER>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.LIB_NPM_BINPROVIDER
    :summary:
    ```
* - {py:obj}`npm <archivebox.plugins_pkg.npm.apps.npm>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.npm
    :summary:
    ```
* - {py:obj}`NPM_BINARY <archivebox.plugins_pkg.npm.apps.NPM_BINARY>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.NPM_BINARY
    :summary:
    ```
* - {py:obj}`NODE_BINARY <archivebox.plugins_pkg.npm.apps.NODE_BINARY>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.NODE_BINARY
    :summary:
    ```
* - {py:obj}`PLUGIN <archivebox.plugins_pkg.npm.apps.PLUGIN>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.PLUGIN
    :summary:
    ```
* - {py:obj}`DJANGO_APP <archivebox.plugins_pkg.npm.apps.DJANGO_APP>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.DJANGO_APP
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.plugins_pkg.npm.apps.__package__
:value: >
   'archivebox.plugins_pkg.npm'

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.__package__
```

````

```{py:class} NpmDependencyConfigs(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_implicit_flags: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.plugins_pkg.npm.apps.NpmDependencyConfigs

Bases: {py:obj}`abx.archivebox.base_configset.BaseConfigSet`

```

````{py:data} DEFAULT_GLOBAL_CONFIG
:canonical: archivebox.plugins_pkg.npm.apps.DEFAULT_GLOBAL_CONFIG
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.DEFAULT_GLOBAL_CONFIG
```

````

````{py:data} NPM_CONFIG
:canonical: archivebox.plugins_pkg.npm.apps.NPM_CONFIG
:value: >
   'NpmDependencyConfigs(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.NPM_CONFIG
```

````

````{py:data} OLD_NODE_BIN_PATH
:canonical: archivebox.plugins_pkg.npm.apps.OLD_NODE_BIN_PATH
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.OLD_NODE_BIN_PATH
```

````

````{py:data} NEW_NODE_BIN_PATH
:canonical: archivebox.plugins_pkg.npm.apps.NEW_NODE_BIN_PATH
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.NEW_NODE_BIN_PATH
```

````

`````{py:class} SystemNpmProvider(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.npm.apps.SystemNpmProvider

Bases: {py:obj}`pydantic_pkgr.NpmProvider`, {py:obj}`abx.archivebox.base_binary.BaseBinProvider`

````{py:attribute} name
:canonical: archivebox.plugins_pkg.npm.apps.SystemNpmProvider.name
:type: pydantic_pkgr.BinProviderName
:value: >
   'sys_npm'

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.SystemNpmProvider.name
```

````

````{py:attribute} npm_prefix
:canonical: archivebox.plugins_pkg.npm.apps.SystemNpmProvider.npm_prefix
:type: typing.Optional[pathlib.Path]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.SystemNpmProvider.npm_prefix
```

````

`````

`````{py:class} LibNpmProvider(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.npm.apps.LibNpmProvider

Bases: {py:obj}`pydantic_pkgr.NpmProvider`, {py:obj}`abx.archivebox.base_binary.BaseBinProvider`

````{py:attribute} name
:canonical: archivebox.plugins_pkg.npm.apps.LibNpmProvider.name
:type: pydantic_pkgr.BinProviderName
:value: >
   'lib_npm'

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.LibNpmProvider.name
```

````

````{py:attribute} PATH
:canonical: archivebox.plugins_pkg.npm.apps.LibNpmProvider.PATH
:type: pydantic_pkgr.PATHStr
:value: >
   'str(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.LibNpmProvider.PATH
```

````

````{py:attribute} npm_prefix
:canonical: archivebox.plugins_pkg.npm.apps.LibNpmProvider.npm_prefix
:type: typing.Optional[pathlib.Path]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.LibNpmProvider.npm_prefix
```

````

````{py:method} validate_path()
:canonical: archivebox.plugins_pkg.npm.apps.LibNpmProvider.validate_path

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.LibNpmProvider.validate_path
```

````

`````

````{py:data} SYS_NPM_BINPROVIDER
:canonical: archivebox.plugins_pkg.npm.apps.SYS_NPM_BINPROVIDER
:value: >
   'SystemNpmProvider(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.SYS_NPM_BINPROVIDER
```

````

````{py:data} LIB_NPM_BINPROVIDER
:canonical: archivebox.plugins_pkg.npm.apps.LIB_NPM_BINPROVIDER
:value: >
   'LibNpmProvider(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.LIB_NPM_BINPROVIDER
```

````

````{py:data} npm
:canonical: archivebox.plugins_pkg.npm.apps.npm
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.npm
```

````

`````{py:class} NpmBinary(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.npm.apps.NpmBinary

Bases: {py:obj}`abx.archivebox.base_binary.BaseBinary`

````{py:attribute} name
:canonical: archivebox.plugins_pkg.npm.apps.NpmBinary.name
:type: pydantic_pkgr.BinName
:value: >
   'npm'

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.NpmBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: archivebox.plugins_pkg.npm.apps.NpmBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.NpmBinary.binproviders_supported
```

````

`````

````{py:data} NPM_BINARY
:canonical: archivebox.plugins_pkg.npm.apps.NPM_BINARY
:value: >
   'NpmBinary(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.NPM_BINARY
```

````

`````{py:class} NodeBinary(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.npm.apps.NodeBinary

Bases: {py:obj}`abx.archivebox.base_binary.BaseBinary`

````{py:attribute} name
:canonical: archivebox.plugins_pkg.npm.apps.NodeBinary.name
:type: pydantic_pkgr.BinName
:value: >
   'node'

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.NodeBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: archivebox.plugins_pkg.npm.apps.NodeBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.NodeBinary.binproviders_supported
```

````

`````

````{py:data} NODE_BINARY
:canonical: archivebox.plugins_pkg.npm.apps.NODE_BINARY
:value: >
   'NodeBinary(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.NODE_BINARY
```

````

`````{py:class} NpmPlugin(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.npm.apps.NpmPlugin

Bases: {py:obj}`abx.archivebox.base_plugin.BasePlugin`

````{py:attribute} app_label
:canonical: archivebox.plugins_pkg.npm.apps.NpmPlugin.app_label
:type: str
:value: >
   'npm'

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.NpmPlugin.app_label
```

````

````{py:attribute} verbose_name
:canonical: archivebox.plugins_pkg.npm.apps.NpmPlugin.verbose_name
:type: str
:value: >
   'NPM'

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.NpmPlugin.verbose_name
```

````

````{py:attribute} hooks
:canonical: archivebox.plugins_pkg.npm.apps.NpmPlugin.hooks
:type: typing.List[pydantic.InstanceOf[abx.archivebox.base_hook.BaseHook]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.NpmPlugin.hooks
```

````

`````

````{py:data} PLUGIN
:canonical: archivebox.plugins_pkg.npm.apps.PLUGIN
:value: >
   'NpmPlugin(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.PLUGIN
```

````

````{py:data} DJANGO_APP
:canonical: archivebox.plugins_pkg.npm.apps.DJANGO_APP
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.npm.apps.DJANGO_APP
```

````
