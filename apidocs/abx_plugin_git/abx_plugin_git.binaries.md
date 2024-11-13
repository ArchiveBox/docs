# {py:mod}`abx_plugin_git.binaries`

```{py:module} abx_plugin_git.binaries
```

```{autodoc2-docstring} abx_plugin_git.binaries
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`GitBinary <abx_plugin_git.binaries.GitBinary>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <abx_plugin_git.binaries.__package__>`
  - ```{autodoc2-docstring} abx_plugin_git.binaries.__package__
    :summary:
    ```
* - {py:obj}`GIT_BINARY <abx_plugin_git.binaries.GIT_BINARY>`
  - ```{autodoc2-docstring} abx_plugin_git.binaries.GIT_BINARY
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: abx_plugin_git.binaries.__package__
:value: >
   'abx_plugin_git'

```{autodoc2-docstring} abx_plugin_git.binaries.__package__
```

````

`````{py:class} GitBinary(/, **data: typing.Any)
:canonical: abx_plugin_git.binaries.GitBinary

Bases: {py:obj}`pydantic_pkgr.Binary`

````{py:attribute} name
:canonical: abx_plugin_git.binaries.GitBinary.name
:type: pydantic_pkgr.BinName
:value: >
   None

```{autodoc2-docstring} abx_plugin_git.binaries.GitBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: abx_plugin_git.binaries.GitBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} abx_plugin_git.binaries.GitBinary.binproviders_supported
```

````

`````

````{py:data} GIT_BINARY
:canonical: abx_plugin_git.binaries.GIT_BINARY
:value: >
   'GitBinary(...)'

```{autodoc2-docstring} abx_plugin_git.binaries.GIT_BINARY
```

````
