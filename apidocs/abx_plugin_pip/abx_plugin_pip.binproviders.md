# {py:mod}`abx_plugin_pip.binproviders`

```{py:module} abx_plugin_pip.binproviders
```

```{autodoc2-docstring} abx_plugin_pip.binproviders
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SystemPipBinProvider <abx_plugin_pip.binproviders.SystemPipBinProvider>`
  -
* - {py:obj}`SystemPipxBinProvider <abx_plugin_pip.binproviders.SystemPipxBinProvider>`
  -
* - {py:obj}`VenvPipBinProvider <abx_plugin_pip.binproviders.VenvPipBinProvider>`
  -
* - {py:obj}`LibPipBinProvider <abx_plugin_pip.binproviders.LibPipBinProvider>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DEFAULT_BINPROVIDERS <abx_plugin_pip.binproviders.DEFAULT_BINPROVIDERS>`
  - ```{autodoc2-docstring} abx_plugin_pip.binproviders.DEFAULT_BINPROVIDERS
    :summary:
    ```
* - {py:obj}`env <abx_plugin_pip.binproviders.env>`
  - ```{autodoc2-docstring} abx_plugin_pip.binproviders.env
    :summary:
    ```
* - {py:obj}`apt <abx_plugin_pip.binproviders.apt>`
  - ```{autodoc2-docstring} abx_plugin_pip.binproviders.apt
    :summary:
    ```
* - {py:obj}`brew <abx_plugin_pip.binproviders.brew>`
  - ```{autodoc2-docstring} abx_plugin_pip.binproviders.brew
    :summary:
    ```
* - {py:obj}`IS_INSIDE_VENV <abx_plugin_pip.binproviders.IS_INSIDE_VENV>`
  - ```{autodoc2-docstring} abx_plugin_pip.binproviders.IS_INSIDE_VENV
    :summary:
    ```
* - {py:obj}`SYS_PIP_BINPROVIDER <abx_plugin_pip.binproviders.SYS_PIP_BINPROVIDER>`
  - ```{autodoc2-docstring} abx_plugin_pip.binproviders.SYS_PIP_BINPROVIDER
    :summary:
    ```
* - {py:obj}`PIPX_PIP_BINPROVIDER <abx_plugin_pip.binproviders.PIPX_PIP_BINPROVIDER>`
  - ```{autodoc2-docstring} abx_plugin_pip.binproviders.PIPX_PIP_BINPROVIDER
    :summary:
    ```
* - {py:obj}`VENV_PIP_BINPROVIDER <abx_plugin_pip.binproviders.VENV_PIP_BINPROVIDER>`
  - ```{autodoc2-docstring} abx_plugin_pip.binproviders.VENV_PIP_BINPROVIDER
    :summary:
    ```
* - {py:obj}`LIB_PIP_BINPROVIDER <abx_plugin_pip.binproviders.LIB_PIP_BINPROVIDER>`
  - ```{autodoc2-docstring} abx_plugin_pip.binproviders.LIB_PIP_BINPROVIDER
    :summary:
    ```
* - {py:obj}`pip <abx_plugin_pip.binproviders.pip>`
  - ```{autodoc2-docstring} abx_plugin_pip.binproviders.pip
    :summary:
    ```
* - {py:obj}`site_packages_dir <abx_plugin_pip.binproviders.site_packages_dir>`
  - ```{autodoc2-docstring} abx_plugin_pip.binproviders.site_packages_dir
    :summary:
    ```
* - {py:obj}`LIB_SITE_PACKAGES <abx_plugin_pip.binproviders.LIB_SITE_PACKAGES>`
  - ```{autodoc2-docstring} abx_plugin_pip.binproviders.LIB_SITE_PACKAGES
    :summary:
    ```
* - {py:obj}`VENV_SITE_PACKAGES <abx_plugin_pip.binproviders.VENV_SITE_PACKAGES>`
  - ```{autodoc2-docstring} abx_plugin_pip.binproviders.VENV_SITE_PACKAGES
    :summary:
    ```
* - {py:obj}`USER_SITE_PACKAGES <abx_plugin_pip.binproviders.USER_SITE_PACKAGES>`
  - ```{autodoc2-docstring} abx_plugin_pip.binproviders.USER_SITE_PACKAGES
    :summary:
    ```
* - {py:obj}`SYS_SITE_PACKAGES <abx_plugin_pip.binproviders.SYS_SITE_PACKAGES>`
  - ```{autodoc2-docstring} abx_plugin_pip.binproviders.SYS_SITE_PACKAGES
    :summary:
    ```
* - {py:obj}`ALL_SITE_PACKAGES <abx_plugin_pip.binproviders.ALL_SITE_PACKAGES>`
  - ```{autodoc2-docstring} abx_plugin_pip.binproviders.ALL_SITE_PACKAGES
    :summary:
    ```
````

### API

````{py:data} DEFAULT_BINPROVIDERS
:canonical: abx_plugin_pip.binproviders.DEFAULT_BINPROVIDERS
:value: >
   'benedict(...)'

```{autodoc2-docstring} abx_plugin_pip.binproviders.DEFAULT_BINPROVIDERS
```

````

````{py:data} env
:canonical: abx_plugin_pip.binproviders.env
:value: >
   None

```{autodoc2-docstring} abx_plugin_pip.binproviders.env
```

````

````{py:data} apt
:canonical: abx_plugin_pip.binproviders.apt
:value: >
   None

```{autodoc2-docstring} abx_plugin_pip.binproviders.apt
```

````

````{py:data} brew
:canonical: abx_plugin_pip.binproviders.brew
:value: >
   None

```{autodoc2-docstring} abx_plugin_pip.binproviders.brew
```

````

`````{py:class} SystemPipBinProvider(/, **data: typing.Any)
:canonical: abx_plugin_pip.binproviders.SystemPipBinProvider

Bases: {py:obj}`pydantic_pkgr.PipProvider`

````{py:attribute} name
:canonical: abx_plugin_pip.binproviders.SystemPipBinProvider.name
:type: pydantic_pkgr.BinProviderName
:value: >
   'sys_pip'

```{autodoc2-docstring} abx_plugin_pip.binproviders.SystemPipBinProvider.name
```

````

````{py:attribute} INSTALLER_BIN
:canonical: abx_plugin_pip.binproviders.SystemPipBinProvider.INSTALLER_BIN
:type: pydantic_pkgr.BinName
:value: >
   'pip'

```{autodoc2-docstring} abx_plugin_pip.binproviders.SystemPipBinProvider.INSTALLER_BIN
```

````

````{py:attribute} pip_venv
:canonical: abx_plugin_pip.binproviders.SystemPipBinProvider.pip_venv
:type: typing.Optional[pathlib.Path]
:value: >
   None

```{autodoc2-docstring} abx_plugin_pip.binproviders.SystemPipBinProvider.pip_venv
```

````

````{py:method} on_install(bin_name: str, **kwargs)
:canonical: abx_plugin_pip.binproviders.SystemPipBinProvider.on_install

```{autodoc2-docstring} abx_plugin_pip.binproviders.SystemPipBinProvider.on_install
```

````

`````

`````{py:class} SystemPipxBinProvider(/, **data: typing.Any)
:canonical: abx_plugin_pip.binproviders.SystemPipxBinProvider

Bases: {py:obj}`pydantic_pkgr.PipProvider`

````{py:attribute} name
:canonical: abx_plugin_pip.binproviders.SystemPipxBinProvider.name
:type: pydantic_pkgr.BinProviderName
:value: >
   'pipx'

```{autodoc2-docstring} abx_plugin_pip.binproviders.SystemPipxBinProvider.name
```

````

````{py:attribute} INSTALLER_BIN
:canonical: abx_plugin_pip.binproviders.SystemPipxBinProvider.INSTALLER_BIN
:type: pydantic_pkgr.BinName
:value: >
   'pipx'

```{autodoc2-docstring} abx_plugin_pip.binproviders.SystemPipxBinProvider.INSTALLER_BIN
```

````

````{py:attribute} pip_venv
:canonical: abx_plugin_pip.binproviders.SystemPipxBinProvider.pip_venv
:type: typing.Optional[pathlib.Path]
:value: >
   None

```{autodoc2-docstring} abx_plugin_pip.binproviders.SystemPipxBinProvider.pip_venv
```

````

`````

````{py:data} IS_INSIDE_VENV
:canonical: abx_plugin_pip.binproviders.IS_INSIDE_VENV
:value: >
   None

```{autodoc2-docstring} abx_plugin_pip.binproviders.IS_INSIDE_VENV
```

````

`````{py:class} VenvPipBinProvider(/, **data: typing.Any)
:canonical: abx_plugin_pip.binproviders.VenvPipBinProvider

Bases: {py:obj}`pydantic_pkgr.PipProvider`

````{py:attribute} name
:canonical: abx_plugin_pip.binproviders.VenvPipBinProvider.name
:type: pydantic_pkgr.BinProviderName
:value: >
   'venv_pip'

```{autodoc2-docstring} abx_plugin_pip.binproviders.VenvPipBinProvider.name
```

````

````{py:attribute} INSTALLER_BIN
:canonical: abx_plugin_pip.binproviders.VenvPipBinProvider.INSTALLER_BIN
:type: pydantic_pkgr.BinName
:value: >
   'pip'

```{autodoc2-docstring} abx_plugin_pip.binproviders.VenvPipBinProvider.INSTALLER_BIN
```

````

````{py:attribute} pip_venv
:canonical: abx_plugin_pip.binproviders.VenvPipBinProvider.pip_venv
:type: typing.Optional[pathlib.Path]
:value: >
   'Path(...)'

```{autodoc2-docstring} abx_plugin_pip.binproviders.VenvPipBinProvider.pip_venv
```

````

````{py:method} setup()
:canonical: abx_plugin_pip.binproviders.VenvPipBinProvider.setup

```{autodoc2-docstring} abx_plugin_pip.binproviders.VenvPipBinProvider.setup
```

````

`````

`````{py:class} LibPipBinProvider(/, **data: typing.Any)
:canonical: abx_plugin_pip.binproviders.LibPipBinProvider

Bases: {py:obj}`pydantic_pkgr.PipProvider`

````{py:attribute} name
:canonical: abx_plugin_pip.binproviders.LibPipBinProvider.name
:type: pydantic_pkgr.BinProviderName
:value: >
   'lib_pip'

```{autodoc2-docstring} abx_plugin_pip.binproviders.LibPipBinProvider.name
```

````

````{py:attribute} INSTALLER_BIN
:canonical: abx_plugin_pip.binproviders.LibPipBinProvider.INSTALLER_BIN
:type: pydantic_pkgr.BinName
:value: >
   'pip'

```{autodoc2-docstring} abx_plugin_pip.binproviders.LibPipBinProvider.INSTALLER_BIN
```

````

````{py:attribute} pip_venv
:canonical: abx_plugin_pip.binproviders.LibPipBinProvider.pip_venv
:type: typing.Optional[pathlib.Path]
:value: >
   'Path(...)'

```{autodoc2-docstring} abx_plugin_pip.binproviders.LibPipBinProvider.pip_venv
```

````

````{py:method} setup() -> None
:canonical: abx_plugin_pip.binproviders.LibPipBinProvider.setup

````

`````

````{py:data} SYS_PIP_BINPROVIDER
:canonical: abx_plugin_pip.binproviders.SYS_PIP_BINPROVIDER
:value: >
   'SystemPipBinProvider(...)'

```{autodoc2-docstring} abx_plugin_pip.binproviders.SYS_PIP_BINPROVIDER
```

````

````{py:data} PIPX_PIP_BINPROVIDER
:canonical: abx_plugin_pip.binproviders.PIPX_PIP_BINPROVIDER
:value: >
   'SystemPipxBinProvider(...)'

```{autodoc2-docstring} abx_plugin_pip.binproviders.PIPX_PIP_BINPROVIDER
```

````

````{py:data} VENV_PIP_BINPROVIDER
:canonical: abx_plugin_pip.binproviders.VENV_PIP_BINPROVIDER
:value: >
   'VenvPipBinProvider(...)'

```{autodoc2-docstring} abx_plugin_pip.binproviders.VENV_PIP_BINPROVIDER
```

````

````{py:data} LIB_PIP_BINPROVIDER
:canonical: abx_plugin_pip.binproviders.LIB_PIP_BINPROVIDER
:value: >
   'LibPipBinProvider(...)'

```{autodoc2-docstring} abx_plugin_pip.binproviders.LIB_PIP_BINPROVIDER
```

````

````{py:data} pip
:canonical: abx_plugin_pip.binproviders.pip
:value: >
   None

```{autodoc2-docstring} abx_plugin_pip.binproviders.pip
```

````

````{py:data} site_packages_dir
:canonical: abx_plugin_pip.binproviders.site_packages_dir
:value: >
   None

```{autodoc2-docstring} abx_plugin_pip.binproviders.site_packages_dir
```

````

````{py:data} LIB_SITE_PACKAGES
:canonical: abx_plugin_pip.binproviders.LIB_SITE_PACKAGES
:value: >
   ()

```{autodoc2-docstring} abx_plugin_pip.binproviders.LIB_SITE_PACKAGES
```

````

````{py:data} VENV_SITE_PACKAGES
:canonical: abx_plugin_pip.binproviders.VENV_SITE_PACKAGES
:value: >
   ()

```{autodoc2-docstring} abx_plugin_pip.binproviders.VENV_SITE_PACKAGES
```

````

````{py:data} USER_SITE_PACKAGES
:canonical: abx_plugin_pip.binproviders.USER_SITE_PACKAGES
:value: >
   'getusersitepackages(...)'

```{autodoc2-docstring} abx_plugin_pip.binproviders.USER_SITE_PACKAGES
```

````

````{py:data} SYS_SITE_PACKAGES
:canonical: abx_plugin_pip.binproviders.SYS_SITE_PACKAGES
:value: >
   'getsitepackages(...)'

```{autodoc2-docstring} abx_plugin_pip.binproviders.SYS_SITE_PACKAGES
```

````

````{py:data} ALL_SITE_PACKAGES
:canonical: abx_plugin_pip.binproviders.ALL_SITE_PACKAGES
:value: >
   ()

```{autodoc2-docstring} abx_plugin_pip.binproviders.ALL_SITE_PACKAGES
```

````
