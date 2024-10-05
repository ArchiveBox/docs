# {py:mod}`archivebox.abx.archivebox.base_binary`

```{py:module} archivebox.abx.archivebox.base_binary
```

```{autodoc2-docstring} archivebox.abx.archivebox.base_binary
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseBinProvider <archivebox.abx.archivebox.base_binary.BaseBinProvider>`
  -
* - {py:obj}`BaseBinary <archivebox.abx.archivebox.base_binary.BaseBinary>`
  -
* - {py:obj}`AptBinProvider <archivebox.abx.archivebox.base_binary.AptBinProvider>`
  -
* - {py:obj}`BrewBinProvider <archivebox.abx.archivebox.base_binary.BrewBinProvider>`
  -
* - {py:obj}`EnvBinProvider <archivebox.abx.archivebox.base_binary.EnvBinProvider>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.abx.archivebox.base_binary.__package__>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.__package__
    :summary:
    ```
* - {py:obj}`apt <archivebox.abx.archivebox.base_binary.apt>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.apt
    :summary:
    ```
* - {py:obj}`brew <archivebox.abx.archivebox.base_binary.brew>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.brew
    :summary:
    ```
* - {py:obj}`env <archivebox.abx.archivebox.base_binary.env>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.env
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.abx.archivebox.base_binary.__package__
:value: >
   'abx.archivebox'

```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.__package__
```

````

`````{py:class} BaseBinProvider(/, **data: typing.Any)
:canonical: archivebox.abx.archivebox.base_binary.BaseBinProvider

Bases: {py:obj}`archivebox.abx.archivebox.base_hook.BaseHook`, {py:obj}`pydantic_pkgr.BinProvider`

````{py:attribute} hook_type
:canonical: archivebox.abx.archivebox.base_binary.BaseBinProvider.hook_type
:type: archivebox.abx.archivebox.base_hook.HookType
:value: >
   'BINPROVIDER'

```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.BaseBinProvider.hook_type
```

````

````{py:property} admin_url
:canonical: archivebox.abx.archivebox.base_binary.BaseBinProvider.admin_url
:type: str

```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.BaseBinProvider.admin_url
```

````

````{py:method} get_BINPROVIDERS()
:canonical: archivebox.abx.archivebox.base_binary.BaseBinProvider.get_BINPROVIDERS

```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.BaseBinProvider.get_BINPROVIDERS
```

````

`````

`````{py:class} BaseBinary(/, **data: typing.Any)
:canonical: archivebox.abx.archivebox.base_binary.BaseBinary

Bases: {py:obj}`archivebox.abx.archivebox.base_hook.BaseHook`, {py:obj}`pydantic_pkgr.Binary`

````{py:attribute} hook_type
:canonical: archivebox.abx.archivebox.base_binary.BaseBinary.hook_type
:type: archivebox.abx.archivebox.base_hook.HookType
:value: >
   'BINARY'

```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.BaseBinary.hook_type
```

````

````{py:attribute} binproviders_supported
:canonical: archivebox.abx.archivebox.base_binary.BaseBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.BaseBinary.binproviders_supported
```

````

````{py:attribute} provider_overrides
:canonical: archivebox.abx.archivebox.base_binary.BaseBinary.provider_overrides
:type: typing.Dict[pydantic_pkgr.BinProviderName, pydantic_pkgr.ProviderLookupDict]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.BaseBinary.provider_overrides
```

````

````{py:method} symlink_to_lib(binary, bin_dir=None) -> None
:canonical: archivebox.abx.archivebox.base_binary.BaseBinary.symlink_to_lib
:staticmethod:

```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.BaseBinary.symlink_to_lib
```

````

````{py:method} load(fresh=False, **kwargs) -> typing_extensions.Self
:canonical: archivebox.abx.archivebox.base_binary.BaseBinary.load

```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.BaseBinary.load
```

````

````{py:method} install(**kwargs) -> typing_extensions.Self
:canonical: archivebox.abx.archivebox.base_binary.BaseBinary.install

```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.BaseBinary.install
```

````

````{py:method} load_or_install(**kwargs) -> typing_extensions.Self
:canonical: archivebox.abx.archivebox.base_binary.BaseBinary.load_or_install

```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.BaseBinary.load_or_install
```

````

````{py:property} admin_url
:canonical: archivebox.abx.archivebox.base_binary.BaseBinary.admin_url
:type: str

```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.BaseBinary.admin_url
```

````

````{py:method} get_BINARIES()
:canonical: archivebox.abx.archivebox.base_binary.BaseBinary.get_BINARIES

```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.BaseBinary.get_BINARIES
```

````

`````

`````{py:class} AptBinProvider(/, **data: typing.Any)
:canonical: archivebox.abx.archivebox.base_binary.AptBinProvider

Bases: {py:obj}`pydantic_pkgr.AptProvider`, {py:obj}`archivebox.abx.archivebox.base_binary.BaseBinProvider`

````{py:attribute} name
:canonical: archivebox.abx.archivebox.base_binary.AptBinProvider.name
:type: pydantic_pkgr.BinProviderName
:value: >
   'apt'

```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.AptBinProvider.name
```

````

`````

`````{py:class} BrewBinProvider(/, **data: typing.Any)
:canonical: archivebox.abx.archivebox.base_binary.BrewBinProvider

Bases: {py:obj}`pydantic_pkgr.BrewProvider`, {py:obj}`archivebox.abx.archivebox.base_binary.BaseBinProvider`

````{py:attribute} name
:canonical: archivebox.abx.archivebox.base_binary.BrewBinProvider.name
:type: pydantic_pkgr.BinProviderName
:value: >
   'brew'

```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.BrewBinProvider.name
```

````

`````

`````{py:class} EnvBinProvider(/, **data: typing.Any)
:canonical: archivebox.abx.archivebox.base_binary.EnvBinProvider

Bases: {py:obj}`pydantic_pkgr.EnvProvider`, {py:obj}`archivebox.abx.archivebox.base_binary.BaseBinProvider`

````{py:attribute} name
:canonical: archivebox.abx.archivebox.base_binary.EnvBinProvider.name
:type: pydantic_pkgr.BinProviderName
:value: >
   'env'

```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.EnvBinProvider.name
```

````

`````

````{py:data} apt
:canonical: archivebox.abx.archivebox.base_binary.apt
:value: >
   'AptBinProvider(...)'

```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.apt
```

````

````{py:data} brew
:canonical: archivebox.abx.archivebox.base_binary.brew
:value: >
   'BrewBinProvider(...)'

```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.brew
```

````

````{py:data} env
:canonical: archivebox.abx.archivebox.base_binary.env
:value: >
   'EnvBinProvider(...)'

```{autodoc2-docstring} archivebox.abx.archivebox.base_binary.env
```

````
