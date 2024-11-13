# {py:mod}`abx_spec_pydantic_pkgr`

```{py:module} abx_spec_pydantic_pkgr
```

```{autodoc2-docstring} abx_spec_pydantic_pkgr
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PydanticPkgrPluginSpec <abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec>`
  - ```{autodoc2-docstring} abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec
    :summary:
    ```
* - {py:obj}`RequiredSpecsAvailable <abx_spec_pydantic_pkgr.RequiredSpecsAvailable>`
  - ```{autodoc2-docstring} abx_spec_pydantic_pkgr.RequiredSpecsAvailable
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__order__ <abx_spec_pydantic_pkgr.__order__>`
  - ```{autodoc2-docstring} abx_spec_pydantic_pkgr.__order__
    :summary:
    ```
* - {py:obj}`PLUGIN_SPEC <abx_spec_pydantic_pkgr.PLUGIN_SPEC>`
  - ```{autodoc2-docstring} abx_spec_pydantic_pkgr.PLUGIN_SPEC
    :summary:
    ```
* - {py:obj}`TypedPluginManager <abx_spec_pydantic_pkgr.TypedPluginManager>`
  - ```{autodoc2-docstring} abx_spec_pydantic_pkgr.TypedPluginManager
    :summary:
    ```
* - {py:obj}`pm <abx_spec_pydantic_pkgr.pm>`
  - ```{autodoc2-docstring} abx_spec_pydantic_pkgr.pm
    :summary:
    ```
````

### API

````{py:data} __order__
:canonical: abx_spec_pydantic_pkgr.__order__
:value: >
   200

```{autodoc2-docstring} abx_spec_pydantic_pkgr.__order__
```

````

`````{py:class} PydanticPkgrPluginSpec
:canonical: abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec

```{autodoc2-docstring} abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec
```

````{py:method} get_LIB_DIR() -> pathlib.Path
:canonical: abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec.get_LIB_DIR

```{autodoc2-docstring} abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec.get_LIB_DIR
```

````

````{py:method} get_BIN_DIR() -> pathlib.Path
:canonical: abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec.get_BIN_DIR

```{autodoc2-docstring} abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec.get_BIN_DIR
```

````

````{py:method} get_BINPROVIDERS() -> typing.Dict[str, pydantic_pkgr.BinProvider]
:canonical: abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec.get_BINPROVIDERS

```{autodoc2-docstring} abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec.get_BINPROVIDERS
```

````

````{py:method} get_BINARIES() -> typing.Dict[str, pydantic_pkgr.Binary]
:canonical: abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec.get_BINARIES

```{autodoc2-docstring} abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec.get_BINARIES
```

````

````{py:method} get_BINPROVIDER(binprovider_name: str) -> pydantic_pkgr.BinProvider
:canonical: abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec.get_BINPROVIDER

```{autodoc2-docstring} abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec.get_BINPROVIDER
```

````

````{py:method} get_BINARY(bin_name: str) -> pydantic_pkgr.Binary
:canonical: abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec.get_BINARY

```{autodoc2-docstring} abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec.get_BINARY
```

````

````{py:method} binary_load(binary: pydantic_pkgr.Binary, **kwargs) -> pydantic_pkgr.Binary
:canonical: abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec.binary_load

```{autodoc2-docstring} abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec.binary_load
```

````

````{py:method} binary_install(binary: pydantic_pkgr.Binary, **kwargs) -> pydantic_pkgr.Binary
:canonical: abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec.binary_install

```{autodoc2-docstring} abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec.binary_install
```

````

````{py:method} binary_load_or_install(binary: pydantic_pkgr.Binary, **kwargs) -> pydantic_pkgr.Binary
:canonical: abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec.binary_load_or_install

```{autodoc2-docstring} abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec.binary_load_or_install
```

````

````{py:method} binary_symlink_to_bin_dir(binary: pydantic_pkgr.Binary, bin_dir: pathlib.Path | None = None)
:canonical: abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec.binary_symlink_to_bin_dir

```{autodoc2-docstring} abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec.binary_symlink_to_bin_dir
```

````

`````

````{py:data} PLUGIN_SPEC
:canonical: abx_spec_pydantic_pkgr.PLUGIN_SPEC
:value: >
   None

```{autodoc2-docstring} abx_spec_pydantic_pkgr.PLUGIN_SPEC
```

````

````{py:class} RequiredSpecsAvailable
:canonical: abx_spec_pydantic_pkgr.RequiredSpecsAvailable

Bases: {py:obj}`abx_spec_config.ConfigPluginSpec`, {py:obj}`abx_spec_pydantic_pkgr.PydanticPkgrPluginSpec`

```{autodoc2-docstring} abx_spec_pydantic_pkgr.RequiredSpecsAvailable
```

````

````{py:data} TypedPluginManager
:canonical: abx_spec_pydantic_pkgr.TypedPluginManager
:value: >
   None

```{autodoc2-docstring} abx_spec_pydantic_pkgr.TypedPluginManager
```

````

````{py:data} pm
:canonical: abx_spec_pydantic_pkgr.pm
:value: >
   'cast(...)'

```{autodoc2-docstring} abx_spec_pydantic_pkgr.pm
```

````
