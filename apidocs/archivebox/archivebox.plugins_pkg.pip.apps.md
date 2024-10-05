# {py:mod}`archivebox.plugins_pkg.pip.apps`

```{py:module} archivebox.plugins_pkg.pip.apps
```

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PipDependencyConfigs <archivebox.plugins_pkg.pip.apps.PipDependencyConfigs>`
  -
* - {py:obj}`SystemPipBinProvider <archivebox.plugins_pkg.pip.apps.SystemPipBinProvider>`
  -
* - {py:obj}`SystemPipxBinProvider <archivebox.plugins_pkg.pip.apps.SystemPipxBinProvider>`
  -
* - {py:obj}`VenvPipBinProvider <archivebox.plugins_pkg.pip.apps.VenvPipBinProvider>`
  -
* - {py:obj}`LibPipBinProvider <archivebox.plugins_pkg.pip.apps.LibPipBinProvider>`
  -
* - {py:obj}`ArchiveboxBinary <archivebox.plugins_pkg.pip.apps.ArchiveboxBinary>`
  -
* - {py:obj}`PythonBinary <archivebox.plugins_pkg.pip.apps.PythonBinary>`
  -
* - {py:obj}`SqliteBinary <archivebox.plugins_pkg.pip.apps.SqliteBinary>`
  -
* - {py:obj}`DjangoBinary <archivebox.plugins_pkg.pip.apps.DjangoBinary>`
  -
* - {py:obj}`PipBinary <archivebox.plugins_pkg.pip.apps.PipBinary>`
  -
* - {py:obj}`CheckUserIsNotRoot <archivebox.plugins_pkg.pip.apps.CheckUserIsNotRoot>`
  -
* - {py:obj}`CheckPipEnvironment <archivebox.plugins_pkg.pip.apps.CheckPipEnvironment>`
  -
* - {py:obj}`PipPlugin <archivebox.plugins_pkg.pip.apps.PipPlugin>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`register_django_checks <archivebox.plugins_pkg.pip.apps.register_django_checks>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.register_django_checks
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.plugins_pkg.pip.apps.__package__>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.__package__
    :summary:
    ```
* - {py:obj}`DEFAULT_GLOBAL_CONFIG <archivebox.plugins_pkg.pip.apps.DEFAULT_GLOBAL_CONFIG>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.DEFAULT_GLOBAL_CONFIG
    :summary:
    ```
* - {py:obj}`PIP_CONFIG <archivebox.plugins_pkg.pip.apps.PIP_CONFIG>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PIP_CONFIG
    :summary:
    ```
* - {py:obj}`SYS_PIP_BINPROVIDER <archivebox.plugins_pkg.pip.apps.SYS_PIP_BINPROVIDER>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.SYS_PIP_BINPROVIDER
    :summary:
    ```
* - {py:obj}`PIPX_PIP_BINPROVIDER <archivebox.plugins_pkg.pip.apps.PIPX_PIP_BINPROVIDER>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PIPX_PIP_BINPROVIDER
    :summary:
    ```
* - {py:obj}`VENV_PIP_BINPROVIDER <archivebox.plugins_pkg.pip.apps.VENV_PIP_BINPROVIDER>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.VENV_PIP_BINPROVIDER
    :summary:
    ```
* - {py:obj}`LIB_PIP_BINPROVIDER <archivebox.plugins_pkg.pip.apps.LIB_PIP_BINPROVIDER>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.LIB_PIP_BINPROVIDER
    :summary:
    ```
* - {py:obj}`pip <archivebox.plugins_pkg.pip.apps.pip>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.pip
    :summary:
    ```
* - {py:obj}`ARCHIVEBOX_BINARY <archivebox.plugins_pkg.pip.apps.ARCHIVEBOX_BINARY>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.ARCHIVEBOX_BINARY
    :summary:
    ```
* - {py:obj}`PYTHON_BINARY <archivebox.plugins_pkg.pip.apps.PYTHON_BINARY>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PYTHON_BINARY
    :summary:
    ```
* - {py:obj}`SQLITE_BINARY <archivebox.plugins_pkg.pip.apps.SQLITE_BINARY>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.SQLITE_BINARY
    :summary:
    ```
* - {py:obj}`DJANGO_BINARY <archivebox.plugins_pkg.pip.apps.DJANGO_BINARY>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.DJANGO_BINARY
    :summary:
    ```
* - {py:obj}`PIP_BINARY <archivebox.plugins_pkg.pip.apps.PIP_BINARY>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PIP_BINARY
    :summary:
    ```
* - {py:obj}`USER_IS_NOT_ROOT_CHECK <archivebox.plugins_pkg.pip.apps.USER_IS_NOT_ROOT_CHECK>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.USER_IS_NOT_ROOT_CHECK
    :summary:
    ```
* - {py:obj}`PIP_ENVIRONMENT_CHECK <archivebox.plugins_pkg.pip.apps.PIP_ENVIRONMENT_CHECK>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PIP_ENVIRONMENT_CHECK
    :summary:
    ```
* - {py:obj}`PLUGIN <archivebox.plugins_pkg.pip.apps.PLUGIN>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PLUGIN
    :summary:
    ```
* - {py:obj}`DJANGO_APP <archivebox.plugins_pkg.pip.apps.DJANGO_APP>`
  - ```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.DJANGO_APP
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.plugins_pkg.pip.apps.__package__
:value: >
   'archivebox.plugins_pkg.pip'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.__package__
```

````

`````{py:class} PipDependencyConfigs(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_implicit_flags: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.plugins_pkg.pip.apps.PipDependencyConfigs

Bases: {py:obj}`abx.archivebox.base_configset.BaseConfigSet`

````{py:attribute} USE_PIP
:canonical: archivebox.plugins_pkg.pip.apps.PipDependencyConfigs.USE_PIP
:type: bool
:value: >
   True

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PipDependencyConfigs.USE_PIP
```

````

````{py:attribute} PIP_BINARY
:canonical: archivebox.plugins_pkg.pip.apps.PipDependencyConfigs.PIP_BINARY
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PipDependencyConfigs.PIP_BINARY
```

````

````{py:attribute} PIP_ARGS
:canonical: archivebox.plugins_pkg.pip.apps.PipDependencyConfigs.PIP_ARGS
:type: typing.Optional[typing.List[str]]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PipDependencyConfigs.PIP_ARGS
```

````

````{py:attribute} PIP_EXTRA_ARGS
:canonical: archivebox.plugins_pkg.pip.apps.PipDependencyConfigs.PIP_EXTRA_ARGS
:type: typing.List[str]
:value: >
   []

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PipDependencyConfigs.PIP_EXTRA_ARGS
```

````

````{py:attribute} PIP_DEFAULT_ARGS
:canonical: archivebox.plugins_pkg.pip.apps.PipDependencyConfigs.PIP_DEFAULT_ARGS
:type: typing.List[str]
:value: >
   []

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PipDependencyConfigs.PIP_DEFAULT_ARGS
```

````

`````

````{py:data} DEFAULT_GLOBAL_CONFIG
:canonical: archivebox.plugins_pkg.pip.apps.DEFAULT_GLOBAL_CONFIG
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.DEFAULT_GLOBAL_CONFIG
```

````

````{py:data} PIP_CONFIG
:canonical: archivebox.plugins_pkg.pip.apps.PIP_CONFIG
:value: >
   'PipDependencyConfigs(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PIP_CONFIG
```

````

`````{py:class} SystemPipBinProvider(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.pip.apps.SystemPipBinProvider

Bases: {py:obj}`pydantic_pkgr.PipProvider`, {py:obj}`abx.archivebox.base_binary.BaseBinProvider`

````{py:attribute} name
:canonical: archivebox.plugins_pkg.pip.apps.SystemPipBinProvider.name
:type: pydantic_pkgr.BinProviderName
:value: >
   'sys_pip'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.SystemPipBinProvider.name
```

````

````{py:attribute} INSTALLER_BIN
:canonical: archivebox.plugins_pkg.pip.apps.SystemPipBinProvider.INSTALLER_BIN
:type: pydantic_pkgr.BinName
:value: >
   'pip'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.SystemPipBinProvider.INSTALLER_BIN
```

````

````{py:attribute} pip_venv
:canonical: archivebox.plugins_pkg.pip.apps.SystemPipBinProvider.pip_venv
:type: typing.Optional[pathlib.Path]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.SystemPipBinProvider.pip_venv
```

````

````{py:method} on_install(bin_name: str, **kwargs)
:canonical: archivebox.plugins_pkg.pip.apps.SystemPipBinProvider.on_install

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.SystemPipBinProvider.on_install
```

````

`````

`````{py:class} SystemPipxBinProvider(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.pip.apps.SystemPipxBinProvider

Bases: {py:obj}`pydantic_pkgr.PipProvider`, {py:obj}`abx.archivebox.base_binary.BaseBinProvider`

````{py:attribute} name
:canonical: archivebox.plugins_pkg.pip.apps.SystemPipxBinProvider.name
:type: pydantic_pkgr.BinProviderName
:value: >
   'pipx'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.SystemPipxBinProvider.name
```

````

````{py:attribute} INSTALLER_BIN
:canonical: archivebox.plugins_pkg.pip.apps.SystemPipxBinProvider.INSTALLER_BIN
:type: pydantic_pkgr.BinName
:value: >
   'pipx'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.SystemPipxBinProvider.INSTALLER_BIN
```

````

````{py:attribute} pip_venv
:canonical: archivebox.plugins_pkg.pip.apps.SystemPipxBinProvider.pip_venv
:type: typing.Optional[pathlib.Path]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.SystemPipxBinProvider.pip_venv
```

````

`````

`````{py:class} VenvPipBinProvider(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.pip.apps.VenvPipBinProvider

Bases: {py:obj}`pydantic_pkgr.PipProvider`, {py:obj}`abx.archivebox.base_binary.BaseBinProvider`

````{py:attribute} name
:canonical: archivebox.plugins_pkg.pip.apps.VenvPipBinProvider.name
:type: pydantic_pkgr.BinProviderName
:value: >
   'venv_pip'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.VenvPipBinProvider.name
```

````

````{py:attribute} INSTALLER_BIN
:canonical: archivebox.plugins_pkg.pip.apps.VenvPipBinProvider.INSTALLER_BIN
:type: pydantic_pkgr.BinName
:value: >
   'pip'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.VenvPipBinProvider.INSTALLER_BIN
```

````

````{py:attribute} pip_venv
:canonical: archivebox.plugins_pkg.pip.apps.VenvPipBinProvider.pip_venv
:type: typing.Optional[pathlib.Path]
:value: >
   'Path(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.VenvPipBinProvider.pip_venv
```

````

`````

`````{py:class} LibPipBinProvider(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.pip.apps.LibPipBinProvider

Bases: {py:obj}`pydantic_pkgr.PipProvider`, {py:obj}`abx.archivebox.base_binary.BaseBinProvider`

````{py:attribute} name
:canonical: archivebox.plugins_pkg.pip.apps.LibPipBinProvider.name
:type: pydantic_pkgr.BinProviderName
:value: >
   'lib_pip'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.LibPipBinProvider.name
```

````

````{py:attribute} INSTALLER_BIN
:canonical: archivebox.plugins_pkg.pip.apps.LibPipBinProvider.INSTALLER_BIN
:type: pydantic_pkgr.BinName
:value: >
   'pip'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.LibPipBinProvider.INSTALLER_BIN
```

````

````{py:attribute} pip_venv
:canonical: archivebox.plugins_pkg.pip.apps.LibPipBinProvider.pip_venv
:type: typing.Optional[pathlib.Path]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.LibPipBinProvider.pip_venv
```

````

`````

````{py:data} SYS_PIP_BINPROVIDER
:canonical: archivebox.plugins_pkg.pip.apps.SYS_PIP_BINPROVIDER
:value: >
   'SystemPipBinProvider(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.SYS_PIP_BINPROVIDER
```

````

````{py:data} PIPX_PIP_BINPROVIDER
:canonical: archivebox.plugins_pkg.pip.apps.PIPX_PIP_BINPROVIDER
:value: >
   'SystemPipxBinProvider(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PIPX_PIP_BINPROVIDER
```

````

````{py:data} VENV_PIP_BINPROVIDER
:canonical: archivebox.plugins_pkg.pip.apps.VENV_PIP_BINPROVIDER
:value: >
   'VenvPipBinProvider(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.VENV_PIP_BINPROVIDER
```

````

````{py:data} LIB_PIP_BINPROVIDER
:canonical: archivebox.plugins_pkg.pip.apps.LIB_PIP_BINPROVIDER
:value: >
   'LibPipBinProvider(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.LIB_PIP_BINPROVIDER
```

````

````{py:data} pip
:canonical: archivebox.plugins_pkg.pip.apps.pip
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.pip
```

````

`````{py:class} ArchiveboxBinary(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.pip.apps.ArchiveboxBinary

Bases: {py:obj}`abx.archivebox.base_binary.BaseBinary`

````{py:attribute} name
:canonical: archivebox.plugins_pkg.pip.apps.ArchiveboxBinary.name
:type: pydantic_pkgr.BinName
:value: >
   'archivebox'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.ArchiveboxBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: archivebox.plugins_pkg.pip.apps.ArchiveboxBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.ArchiveboxBinary.binproviders_supported
```

````

````{py:attribute} provider_overrides
:canonical: archivebox.plugins_pkg.pip.apps.ArchiveboxBinary.provider_overrides
:type: typing.Dict[pydantic_pkgr.BinProviderName, pydantic_pkgr.ProviderLookupDict]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.ArchiveboxBinary.provider_overrides
```

````

`````

````{py:data} ARCHIVEBOX_BINARY
:canonical: archivebox.plugins_pkg.pip.apps.ARCHIVEBOX_BINARY
:value: >
   'ArchiveboxBinary(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.ARCHIVEBOX_BINARY
```

````

`````{py:class} PythonBinary(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.pip.apps.PythonBinary

Bases: {py:obj}`abx.archivebox.base_binary.BaseBinary`

````{py:attribute} name
:canonical: archivebox.plugins_pkg.pip.apps.PythonBinary.name
:type: pydantic_pkgr.BinName
:value: >
   'python'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PythonBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: archivebox.plugins_pkg.pip.apps.PythonBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PythonBinary.binproviders_supported
```

````

````{py:attribute} provider_overrides
:canonical: archivebox.plugins_pkg.pip.apps.PythonBinary.provider_overrides
:type: typing.Dict[pydantic_pkgr.BinProviderName, pydantic_pkgr.ProviderLookupDict]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PythonBinary.provider_overrides
```

````

`````

````{py:data} PYTHON_BINARY
:canonical: archivebox.plugins_pkg.pip.apps.PYTHON_BINARY
:value: >
   'PythonBinary(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PYTHON_BINARY
```

````

`````{py:class} SqliteBinary(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.pip.apps.SqliteBinary

Bases: {py:obj}`abx.archivebox.base_binary.BaseBinary`

````{py:attribute} name
:canonical: archivebox.plugins_pkg.pip.apps.SqliteBinary.name
:type: pydantic_pkgr.BinName
:value: >
   'sqlite'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.SqliteBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: archivebox.plugins_pkg.pip.apps.SqliteBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[abx.archivebox.base_binary.BaseBinProvider]]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.SqliteBinary.binproviders_supported
```

````

````{py:attribute} provider_overrides
:canonical: archivebox.plugins_pkg.pip.apps.SqliteBinary.provider_overrides
:type: typing.Dict[pydantic_pkgr.BinProviderName, pydantic_pkgr.ProviderLookupDict]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.SqliteBinary.provider_overrides
```

````

````{py:method} validate_json_extension_is_available()
:canonical: archivebox.plugins_pkg.pip.apps.SqliteBinary.validate_json_extension_is_available

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.SqliteBinary.validate_json_extension_is_available
```

````

`````

````{py:data} SQLITE_BINARY
:canonical: archivebox.plugins_pkg.pip.apps.SQLITE_BINARY
:value: >
   'SqliteBinary(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.SQLITE_BINARY
```

````

`````{py:class} DjangoBinary(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.pip.apps.DjangoBinary

Bases: {py:obj}`abx.archivebox.base_binary.BaseBinary`

````{py:attribute} name
:canonical: archivebox.plugins_pkg.pip.apps.DjangoBinary.name
:type: pydantic_pkgr.BinName
:value: >
   'django'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.DjangoBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: archivebox.plugins_pkg.pip.apps.DjangoBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[abx.archivebox.base_binary.BaseBinProvider]]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.DjangoBinary.binproviders_supported
```

````

````{py:attribute} provider_overrides
:canonical: archivebox.plugins_pkg.pip.apps.DjangoBinary.provider_overrides
:type: typing.Dict[pydantic_pkgr.BinProviderName, pydantic_pkgr.ProviderLookupDict]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.DjangoBinary.provider_overrides
```

````

`````

````{py:data} DJANGO_BINARY
:canonical: archivebox.plugins_pkg.pip.apps.DJANGO_BINARY
:value: >
   'DjangoBinary(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.DJANGO_BINARY
```

````

`````{py:class} PipBinary(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.pip.apps.PipBinary

Bases: {py:obj}`abx.archivebox.base_binary.BaseBinary`

````{py:attribute} name
:canonical: archivebox.plugins_pkg.pip.apps.PipBinary.name
:type: pydantic_pkgr.BinName
:value: >
   'pip'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PipBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: archivebox.plugins_pkg.pip.apps.PipBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PipBinary.binproviders_supported
```

````

`````

````{py:data} PIP_BINARY
:canonical: archivebox.plugins_pkg.pip.apps.PIP_BINARY
:value: >
   'PipBinary(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PIP_BINARY
```

````

`````{py:class} CheckUserIsNotRoot(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.pip.apps.CheckUserIsNotRoot

Bases: {py:obj}`abx.archivebox.base_check.BaseCheck`

````{py:attribute} label
:canonical: archivebox.plugins_pkg.pip.apps.CheckUserIsNotRoot.label
:type: str
:value: >
   'CheckUserIsNotRoot'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.CheckUserIsNotRoot.label
```

````

````{py:attribute} tag
:canonical: archivebox.plugins_pkg.pip.apps.CheckUserIsNotRoot.tag
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.CheckUserIsNotRoot.tag
```

````

````{py:method} check(settings, logger) -> typing.List[Warning]
:canonical: archivebox.plugins_pkg.pip.apps.CheckUserIsNotRoot.check
:staticmethod:

````

`````

`````{py:class} CheckPipEnvironment(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.pip.apps.CheckPipEnvironment

Bases: {py:obj}`abx.archivebox.base_check.BaseCheck`

````{py:attribute} label
:canonical: archivebox.plugins_pkg.pip.apps.CheckPipEnvironment.label
:type: str
:value: >
   'CheckPipEnvironment'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.CheckPipEnvironment.label
```

````

````{py:attribute} tag
:canonical: archivebox.plugins_pkg.pip.apps.CheckPipEnvironment.tag
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.CheckPipEnvironment.tag
```

````

````{py:method} check(settings, logger) -> typing.List[Warning]
:canonical: archivebox.plugins_pkg.pip.apps.CheckPipEnvironment.check
:staticmethod:

````

`````

````{py:data} USER_IS_NOT_ROOT_CHECK
:canonical: archivebox.plugins_pkg.pip.apps.USER_IS_NOT_ROOT_CHECK
:value: >
   'CheckUserIsNotRoot(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.USER_IS_NOT_ROOT_CHECK
```

````

````{py:data} PIP_ENVIRONMENT_CHECK
:canonical: archivebox.plugins_pkg.pip.apps.PIP_ENVIRONMENT_CHECK
:value: >
   'CheckPipEnvironment(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PIP_ENVIRONMENT_CHECK
```

````

`````{py:class} PipPlugin(/, **data: typing.Any)
:canonical: archivebox.plugins_pkg.pip.apps.PipPlugin

Bases: {py:obj}`abx.archivebox.base_plugin.BasePlugin`

````{py:attribute} app_label
:canonical: archivebox.plugins_pkg.pip.apps.PipPlugin.app_label
:type: str
:value: >
   'pip'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PipPlugin.app_label
```

````

````{py:attribute} verbose_name
:canonical: archivebox.plugins_pkg.pip.apps.PipPlugin.verbose_name
:type: str
:value: >
   'PIP'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PipPlugin.verbose_name
```

````

````{py:attribute} hooks
:canonical: archivebox.plugins_pkg.pip.apps.PipPlugin.hooks
:type: typing.List[pydantic.InstanceOf[abx.archivebox.base_hook.BaseHook]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PipPlugin.hooks
```

````

`````

````{py:data} PLUGIN
:canonical: archivebox.plugins_pkg.pip.apps.PLUGIN
:value: >
   'PipPlugin(...)'

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.PLUGIN
```

````

````{py:data} DJANGO_APP
:canonical: archivebox.plugins_pkg.pip.apps.DJANGO_APP
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.DJANGO_APP
```

````

````{py:function} register_django_checks(settings)
:canonical: archivebox.plugins_pkg.pip.apps.register_django_checks

```{autodoc2-docstring} archivebox.plugins_pkg.pip.apps.register_django_checks
```
````
