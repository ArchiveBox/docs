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

* - {py:obj}`GIT_BINARY <abx_plugin_git.binaries.GIT_BINARY>`
  - ```{autodoc2-docstring} abx_plugin_git.binaries.GIT_BINARY
    :summary:
    ```
````

### API

`````{py:class} GitBinary(/, **data: typing.Any)
:canonical: abx_plugin_git.binaries.GitBinary

Bases: {py:obj}`abx_pkg.Binary`

````{py:attribute} name
:canonical: abx_plugin_git.binaries.GitBinary.name
:type: abx_pkg.BinName
:value: >
   None

```{autodoc2-docstring} abx_plugin_git.binaries.GitBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: abx_plugin_git.binaries.GitBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[abx_pkg.BinProvider]]
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
