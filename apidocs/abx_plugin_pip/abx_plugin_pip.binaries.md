# {py:mod}`abx_plugin_pip.binaries`

```{py:module} abx_plugin_pip.binaries
```

```{autodoc2-docstring} abx_plugin_pip.binaries
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ArchiveboxBinary <abx_plugin_pip.binaries.ArchiveboxBinary>`
  -
* - {py:obj}`PythonBinary <abx_plugin_pip.binaries.PythonBinary>`
  -
* - {py:obj}`SqliteBinary <abx_plugin_pip.binaries.SqliteBinary>`
  -
* - {py:obj}`DjangoBinary <abx_plugin_pip.binaries.DjangoBinary>`
  -
* - {py:obj}`PipBinary <abx_plugin_pip.binaries.PipBinary>`
  -
* - {py:obj}`PipxBinary <abx_plugin_pip.binaries.PipxBinary>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_archivebox_version <abx_plugin_pip.binaries.get_archivebox_version>`
  - ```{autodoc2-docstring} abx_plugin_pip.binaries.get_archivebox_version
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ARCHIVEBOX_BINARY <abx_plugin_pip.binaries.ARCHIVEBOX_BINARY>`
  - ```{autodoc2-docstring} abx_plugin_pip.binaries.ARCHIVEBOX_BINARY
    :summary:
    ```
* - {py:obj}`PYTHON_BINARY <abx_plugin_pip.binaries.PYTHON_BINARY>`
  - ```{autodoc2-docstring} abx_plugin_pip.binaries.PYTHON_BINARY
    :summary:
    ```
* - {py:obj}`LOADED_SQLITE_PATH <abx_plugin_pip.binaries.LOADED_SQLITE_PATH>`
  - ```{autodoc2-docstring} abx_plugin_pip.binaries.LOADED_SQLITE_PATH
    :summary:
    ```
* - {py:obj}`LOADED_SQLITE_VERSION <abx_plugin_pip.binaries.LOADED_SQLITE_VERSION>`
  - ```{autodoc2-docstring} abx_plugin_pip.binaries.LOADED_SQLITE_VERSION
    :summary:
    ```
* - {py:obj}`LOADED_SQLITE_FROM_VENV <abx_plugin_pip.binaries.LOADED_SQLITE_FROM_VENV>`
  - ```{autodoc2-docstring} abx_plugin_pip.binaries.LOADED_SQLITE_FROM_VENV
    :summary:
    ```
* - {py:obj}`SQLITE_BINARY <abx_plugin_pip.binaries.SQLITE_BINARY>`
  - ```{autodoc2-docstring} abx_plugin_pip.binaries.SQLITE_BINARY
    :summary:
    ```
* - {py:obj}`LOADED_DJANGO_PATH <abx_plugin_pip.binaries.LOADED_DJANGO_PATH>`
  - ```{autodoc2-docstring} abx_plugin_pip.binaries.LOADED_DJANGO_PATH
    :summary:
    ```
* - {py:obj}`LOADED_DJANGO_VERSION <abx_plugin_pip.binaries.LOADED_DJANGO_VERSION>`
  - ```{autodoc2-docstring} abx_plugin_pip.binaries.LOADED_DJANGO_VERSION
    :summary:
    ```
* - {py:obj}`LOADED_DJANGO_FROM_VENV <abx_plugin_pip.binaries.LOADED_DJANGO_FROM_VENV>`
  - ```{autodoc2-docstring} abx_plugin_pip.binaries.LOADED_DJANGO_FROM_VENV
    :summary:
    ```
* - {py:obj}`DJANGO_BINARY <abx_plugin_pip.binaries.DJANGO_BINARY>`
  - ```{autodoc2-docstring} abx_plugin_pip.binaries.DJANGO_BINARY
    :summary:
    ```
* - {py:obj}`PIP_BINARY <abx_plugin_pip.binaries.PIP_BINARY>`
  - ```{autodoc2-docstring} abx_plugin_pip.binaries.PIP_BINARY
    :summary:
    ```
* - {py:obj}`PIPX_BINARY <abx_plugin_pip.binaries.PIPX_BINARY>`
  - ```{autodoc2-docstring} abx_plugin_pip.binaries.PIPX_BINARY
    :summary:
    ```
````

### API

````{py:function} get_archivebox_version()
:canonical: abx_plugin_pip.binaries.get_archivebox_version

```{autodoc2-docstring} abx_plugin_pip.binaries.get_archivebox_version
```
````

`````{py:class} ArchiveboxBinary(/, **data: typing.Any)
:canonical: abx_plugin_pip.binaries.ArchiveboxBinary

Bases: {py:obj}`pydantic_pkgr.Binary`

````{py:attribute} name
:canonical: abx_plugin_pip.binaries.ArchiveboxBinary.name
:type: pydantic_pkgr.BinName
:value: >
   'archivebox'

```{autodoc2-docstring} abx_plugin_pip.binaries.ArchiveboxBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: abx_plugin_pip.binaries.ArchiveboxBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} abx_plugin_pip.binaries.ArchiveboxBinary.binproviders_supported
```

````

````{py:attribute} overrides
:canonical: abx_plugin_pip.binaries.ArchiveboxBinary.overrides
:type: pydantic_pkgr.BinaryOverrides
:value: >
   None

```{autodoc2-docstring} abx_plugin_pip.binaries.ArchiveboxBinary.overrides
```

````

````{py:method} install(**kwargs)
:canonical: abx_plugin_pip.binaries.ArchiveboxBinary.install

```{autodoc2-docstring} abx_plugin_pip.binaries.ArchiveboxBinary.install
```

````

````{py:method} load_or_install(**kwargs)
:canonical: abx_plugin_pip.binaries.ArchiveboxBinary.load_or_install

```{autodoc2-docstring} abx_plugin_pip.binaries.ArchiveboxBinary.load_or_install
```

````

`````

````{py:data} ARCHIVEBOX_BINARY
:canonical: abx_plugin_pip.binaries.ARCHIVEBOX_BINARY
:value: >
   'ArchiveboxBinary(...)'

```{autodoc2-docstring} abx_plugin_pip.binaries.ARCHIVEBOX_BINARY
```

````

`````{py:class} PythonBinary(/, **data: typing.Any)
:canonical: abx_plugin_pip.binaries.PythonBinary

Bases: {py:obj}`pydantic_pkgr.Binary`

````{py:attribute} name
:canonical: abx_plugin_pip.binaries.PythonBinary.name
:type: pydantic_pkgr.BinName
:value: >
   'python'

```{autodoc2-docstring} abx_plugin_pip.binaries.PythonBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: abx_plugin_pip.binaries.PythonBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} abx_plugin_pip.binaries.PythonBinary.binproviders_supported
```

````

````{py:attribute} overrides
:canonical: abx_plugin_pip.binaries.PythonBinary.overrides
:type: pydantic_pkgr.BinaryOverrides
:value: >
   None

```{autodoc2-docstring} abx_plugin_pip.binaries.PythonBinary.overrides
```

````

````{py:method} install(**kwargs)
:canonical: abx_plugin_pip.binaries.PythonBinary.install

```{autodoc2-docstring} abx_plugin_pip.binaries.PythonBinary.install
```

````

````{py:method} load_or_install(**kwargs)
:canonical: abx_plugin_pip.binaries.PythonBinary.load_or_install

```{autodoc2-docstring} abx_plugin_pip.binaries.PythonBinary.load_or_install
```

````

`````

````{py:data} PYTHON_BINARY
:canonical: abx_plugin_pip.binaries.PYTHON_BINARY
:value: >
   'PythonBinary(...)'

```{autodoc2-docstring} abx_plugin_pip.binaries.PYTHON_BINARY
```

````

````{py:data} LOADED_SQLITE_PATH
:canonical: abx_plugin_pip.binaries.LOADED_SQLITE_PATH
:value: >
   'Path(...)'

```{autodoc2-docstring} abx_plugin_pip.binaries.LOADED_SQLITE_PATH
```

````

````{py:data} LOADED_SQLITE_VERSION
:canonical: abx_plugin_pip.binaries.LOADED_SQLITE_VERSION
:value: >
   'SemVer(...)'

```{autodoc2-docstring} abx_plugin_pip.binaries.LOADED_SQLITE_VERSION
```

````

````{py:data} LOADED_SQLITE_FROM_VENV
:canonical: abx_plugin_pip.binaries.LOADED_SQLITE_FROM_VENV
:value: >
   'startswith(...)'

```{autodoc2-docstring} abx_plugin_pip.binaries.LOADED_SQLITE_FROM_VENV
```

````

`````{py:class} SqliteBinary(/, **data: typing.Any)
:canonical: abx_plugin_pip.binaries.SqliteBinary

Bases: {py:obj}`pydantic_pkgr.Binary`

````{py:attribute} name
:canonical: abx_plugin_pip.binaries.SqliteBinary.name
:type: pydantic_pkgr.BinName
:value: >
   'sqlite'

```{autodoc2-docstring} abx_plugin_pip.binaries.SqliteBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: abx_plugin_pip.binaries.SqliteBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_pip.binaries.SqliteBinary.binproviders_supported
```

````

````{py:attribute} overrides
:canonical: abx_plugin_pip.binaries.SqliteBinary.overrides
:type: pydantic_pkgr.BinaryOverrides
:value: >
   None

```{autodoc2-docstring} abx_plugin_pip.binaries.SqliteBinary.overrides
```

````

````{py:method} validate_json_extension_is_available()
:canonical: abx_plugin_pip.binaries.SqliteBinary.validate_json_extension_is_available

```{autodoc2-docstring} abx_plugin_pip.binaries.SqliteBinary.validate_json_extension_is_available
```

````

````{py:method} install(**kwargs)
:canonical: abx_plugin_pip.binaries.SqliteBinary.install

```{autodoc2-docstring} abx_plugin_pip.binaries.SqliteBinary.install
```

````

````{py:method} load_or_install(**kwargs)
:canonical: abx_plugin_pip.binaries.SqliteBinary.load_or_install

```{autodoc2-docstring} abx_plugin_pip.binaries.SqliteBinary.load_or_install
```

````

`````

````{py:data} SQLITE_BINARY
:canonical: abx_plugin_pip.binaries.SQLITE_BINARY
:value: >
   'SqliteBinary(...)'

```{autodoc2-docstring} abx_plugin_pip.binaries.SQLITE_BINARY
```

````

````{py:data} LOADED_DJANGO_PATH
:canonical: abx_plugin_pip.binaries.LOADED_DJANGO_PATH
:value: >
   'Path(...)'

```{autodoc2-docstring} abx_plugin_pip.binaries.LOADED_DJANGO_PATH
```

````

````{py:data} LOADED_DJANGO_VERSION
:canonical: abx_plugin_pip.binaries.LOADED_DJANGO_VERSION
:value: >
   'SemVer(...)'

```{autodoc2-docstring} abx_plugin_pip.binaries.LOADED_DJANGO_VERSION
```

````

````{py:data} LOADED_DJANGO_FROM_VENV
:canonical: abx_plugin_pip.binaries.LOADED_DJANGO_FROM_VENV
:value: >
   'startswith(...)'

```{autodoc2-docstring} abx_plugin_pip.binaries.LOADED_DJANGO_FROM_VENV
```

````

`````{py:class} DjangoBinary(/, **data: typing.Any)
:canonical: abx_plugin_pip.binaries.DjangoBinary

Bases: {py:obj}`pydantic_pkgr.Binary`

````{py:attribute} name
:canonical: abx_plugin_pip.binaries.DjangoBinary.name
:type: pydantic_pkgr.BinName
:value: >
   'django'

```{autodoc2-docstring} abx_plugin_pip.binaries.DjangoBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: abx_plugin_pip.binaries.DjangoBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_pip.binaries.DjangoBinary.binproviders_supported
```

````

````{py:attribute} overrides
:canonical: abx_plugin_pip.binaries.DjangoBinary.overrides
:type: pydantic_pkgr.BinaryOverrides
:value: >
   None

```{autodoc2-docstring} abx_plugin_pip.binaries.DjangoBinary.overrides
```

````

````{py:method} install(**kwargs)
:canonical: abx_plugin_pip.binaries.DjangoBinary.install

```{autodoc2-docstring} abx_plugin_pip.binaries.DjangoBinary.install
```

````

````{py:method} load_or_install(**kwargs)
:canonical: abx_plugin_pip.binaries.DjangoBinary.load_or_install

```{autodoc2-docstring} abx_plugin_pip.binaries.DjangoBinary.load_or_install
```

````

`````

````{py:data} DJANGO_BINARY
:canonical: abx_plugin_pip.binaries.DJANGO_BINARY
:value: >
   'DjangoBinary(...)'

```{autodoc2-docstring} abx_plugin_pip.binaries.DJANGO_BINARY
```

````

`````{py:class} PipBinary(/, **data: typing.Any)
:canonical: abx_plugin_pip.binaries.PipBinary

Bases: {py:obj}`pydantic_pkgr.Binary`

````{py:attribute} name
:canonical: abx_plugin_pip.binaries.PipBinary.name
:type: pydantic_pkgr.BinName
:value: >
   'pip'

```{autodoc2-docstring} abx_plugin_pip.binaries.PipBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: abx_plugin_pip.binaries.PipBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} abx_plugin_pip.binaries.PipBinary.binproviders_supported
```

````

````{py:method} install(**kwargs)
:canonical: abx_plugin_pip.binaries.PipBinary.install

```{autodoc2-docstring} abx_plugin_pip.binaries.PipBinary.install
```

````

````{py:method} load_or_install(**kwargs)
:canonical: abx_plugin_pip.binaries.PipBinary.load_or_install

```{autodoc2-docstring} abx_plugin_pip.binaries.PipBinary.load_or_install
```

````

`````

````{py:data} PIP_BINARY
:canonical: abx_plugin_pip.binaries.PIP_BINARY
:value: >
   'PipBinary(...)'

```{autodoc2-docstring} abx_plugin_pip.binaries.PIP_BINARY
```

````

`````{py:class} PipxBinary(/, **data: typing.Any)
:canonical: abx_plugin_pip.binaries.PipxBinary

Bases: {py:obj}`pydantic_pkgr.Binary`

````{py:attribute} name
:canonical: abx_plugin_pip.binaries.PipxBinary.name
:type: pydantic_pkgr.BinName
:value: >
   'pipx'

```{autodoc2-docstring} abx_plugin_pip.binaries.PipxBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: abx_plugin_pip.binaries.PipxBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} abx_plugin_pip.binaries.PipxBinary.binproviders_supported
```

````

`````

````{py:data} PIPX_BINARY
:canonical: abx_plugin_pip.binaries.PIPX_BINARY
:value: >
   'PipxBinary(...)'

```{autodoc2-docstring} abx_plugin_pip.binaries.PIPX_BINARY
```

````
