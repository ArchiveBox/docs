# {py:mod}`abx_spec_abx_pkg`

```{py:module} abx_spec_abx_pkg
```

```{autodoc2-docstring} abx_spec_abx_pkg
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AbxPkgPluginSpec <abx_spec_abx_pkg.AbxPkgPluginSpec>`
  - ```{autodoc2-docstring} abx_spec_abx_pkg.AbxPkgPluginSpec
    :summary:
    ```
* - {py:obj}`RequiredSpecsAvailable <abx_spec_abx_pkg.RequiredSpecsAvailable>`
  - ```{autodoc2-docstring} abx_spec_abx_pkg.RequiredSpecsAvailable
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PLUGIN_SPEC <abx_spec_abx_pkg.PLUGIN_SPEC>`
  - ```{autodoc2-docstring} abx_spec_abx_pkg.PLUGIN_SPEC
    :summary:
    ```
* - {py:obj}`TypedPluginManager <abx_spec_abx_pkg.TypedPluginManager>`
  - ```{autodoc2-docstring} abx_spec_abx_pkg.TypedPluginManager
    :summary:
    ```
* - {py:obj}`pm <abx_spec_abx_pkg.pm>`
  - ```{autodoc2-docstring} abx_spec_abx_pkg.pm
    :summary:
    ```
````

### API

`````{py:class} AbxPkgPluginSpec
:canonical: abx_spec_abx_pkg.AbxPkgPluginSpec

```{autodoc2-docstring} abx_spec_abx_pkg.AbxPkgPluginSpec
```

````{py:attribute} __order__
:canonical: abx_spec_abx_pkg.AbxPkgPluginSpec.__order__
:value: >
   10

```{autodoc2-docstring} abx_spec_abx_pkg.AbxPkgPluginSpec.__order__
```

````

````{py:method} get_LIB_DIR() -> pathlib.Path
:canonical: abx_spec_abx_pkg.AbxPkgPluginSpec.get_LIB_DIR
:staticmethod:

```{autodoc2-docstring} abx_spec_abx_pkg.AbxPkgPluginSpec.get_LIB_DIR
```

````

````{py:method} get_BIN_DIR() -> pathlib.Path
:canonical: abx_spec_abx_pkg.AbxPkgPluginSpec.get_BIN_DIR
:staticmethod:

```{autodoc2-docstring} abx_spec_abx_pkg.AbxPkgPluginSpec.get_BIN_DIR
```

````

````{py:method} get_BINPROVIDERS() -> typing.Dict[str, abx_pkg.BinProvider]
:canonical: abx_spec_abx_pkg.AbxPkgPluginSpec.get_BINPROVIDERS
:staticmethod:

```{autodoc2-docstring} abx_spec_abx_pkg.AbxPkgPluginSpec.get_BINPROVIDERS
```

````

````{py:method} get_BINARIES() -> typing.Dict[str, abx_pkg.Binary]
:canonical: abx_spec_abx_pkg.AbxPkgPluginSpec.get_BINARIES
:staticmethod:

```{autodoc2-docstring} abx_spec_abx_pkg.AbxPkgPluginSpec.get_BINARIES
```

````

````{py:method} get_BINPROVIDER(binprovider_name: str) -> abx_pkg.BinProvider
:canonical: abx_spec_abx_pkg.AbxPkgPluginSpec.get_BINPROVIDER
:staticmethod:

```{autodoc2-docstring} abx_spec_abx_pkg.AbxPkgPluginSpec.get_BINPROVIDER
```

````

````{py:method} get_BINARY(bin_name: str) -> abx_pkg.Binary
:canonical: abx_spec_abx_pkg.AbxPkgPluginSpec.get_BINARY
:staticmethod:

```{autodoc2-docstring} abx_spec_abx_pkg.AbxPkgPluginSpec.get_BINARY
```

````

````{py:method} binary_load(binary: abx_pkg.Binary, **kwargs) -> abx_pkg.Binary
:canonical: abx_spec_abx_pkg.AbxPkgPluginSpec.binary_load
:staticmethod:

```{autodoc2-docstring} abx_spec_abx_pkg.AbxPkgPluginSpec.binary_load
```

````

````{py:method} binary_install(binary: abx_pkg.Binary, **kwargs) -> abx_pkg.Binary
:canonical: abx_spec_abx_pkg.AbxPkgPluginSpec.binary_install
:staticmethod:

```{autodoc2-docstring} abx_spec_abx_pkg.AbxPkgPluginSpec.binary_install
```

````

````{py:method} binary_load_or_install(binary: abx_pkg.Binary, **kwargs) -> abx_pkg.Binary
:canonical: abx_spec_abx_pkg.AbxPkgPluginSpec.binary_load_or_install
:staticmethod:

```{autodoc2-docstring} abx_spec_abx_pkg.AbxPkgPluginSpec.binary_load_or_install
```

````

````{py:method} binary_symlink_to_bin_dir(binary: abx_pkg.Binary, bin_dir: pathlib.Path | None = None)
:canonical: abx_spec_abx_pkg.AbxPkgPluginSpec.binary_symlink_to_bin_dir
:staticmethod:

```{autodoc2-docstring} abx_spec_abx_pkg.AbxPkgPluginSpec.binary_symlink_to_bin_dir
```

````

`````

````{py:data} PLUGIN_SPEC
:canonical: abx_spec_abx_pkg.PLUGIN_SPEC
:value: >
   None

```{autodoc2-docstring} abx_spec_abx_pkg.PLUGIN_SPEC
```

````

````{py:class} RequiredSpecsAvailable
:canonical: abx_spec_abx_pkg.RequiredSpecsAvailable

Bases: {py:obj}`abx_spec_config.ConfigPluginSpec`, {py:obj}`abx_spec_abx_pkg.AbxPkgPluginSpec`

```{autodoc2-docstring} abx_spec_abx_pkg.RequiredSpecsAvailable
```

````

````{py:data} TypedPluginManager
:canonical: abx_spec_abx_pkg.TypedPluginManager
:value: >
   None

```{autodoc2-docstring} abx_spec_abx_pkg.TypedPluginManager
```

````

````{py:data} pm
:canonical: abx_spec_abx_pkg.pm
:value: >
   'cast(...)'

```{autodoc2-docstring} abx_spec_abx_pkg.pm
```

````
