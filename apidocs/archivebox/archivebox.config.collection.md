# {py:mod}`archivebox.config.collection`

```{py:module} archivebox.config.collection
```

```{autodoc2-docstring} archivebox.config.collection
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PluginConfigSection <archivebox.config.collection.PluginConfigSection>`
  - ```{autodoc2-docstring} archivebox.config.collection.PluginConfigSection
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_real_name <archivebox.config.collection.get_real_name>`
  - ```{autodoc2-docstring} archivebox.config.collection.get_real_name
    :summary:
    ```
* - {py:obj}`load_config_val <archivebox.config.collection.load_config_val>`
  - ```{autodoc2-docstring} archivebox.config.collection.load_config_val
    :summary:
    ```
* - {py:obj}`load_config_file <archivebox.config.collection.load_config_file>`
  - ```{autodoc2-docstring} archivebox.config.collection.load_config_file
    :summary:
    ```
* - {py:obj}`section_for_key <archivebox.config.collection.section_for_key>`
  - ```{autodoc2-docstring} archivebox.config.collection.section_for_key
    :summary:
    ```
* - {py:obj}`write_config_file <archivebox.config.collection.write_config_file>`
  - ```{autodoc2-docstring} archivebox.config.collection.write_config_file
    :summary:
    ```
* - {py:obj}`load_config <archivebox.config.collection.load_config>`
  - ```{autodoc2-docstring} archivebox.config.collection.load_config
    :summary:
    ```
* - {py:obj}`load_all_config <archivebox.config.collection.load_all_config>`
  - ```{autodoc2-docstring} archivebox.config.collection.load_all_config
    :summary:
    ```
````

### API

````{py:function} get_real_name(key: str) -> str
:canonical: archivebox.config.collection.get_real_name

```{autodoc2-docstring} archivebox.config.collection.get_real_name
```
````

````{py:function} load_config_val(key: str, default: typing.Any = None, type: typing.Optional[typing.Type] = None, aliases: typing.Optional[typing.Tuple[str, ...]] = None, config: typing.Optional[benedict.benedict] = None, env_vars: typing.Optional[os._Environ] = None, config_file_vars: typing.Optional[typing.Dict[str, str]] = None) -> typing.Any
:canonical: archivebox.config.collection.load_config_val

```{autodoc2-docstring} archivebox.config.collection.load_config_val
```
````

````{py:function} load_config_file() -> typing.Optional[benedict.benedict]
:canonical: archivebox.config.collection.load_config_file

```{autodoc2-docstring} archivebox.config.collection.load_config_file
```
````

`````{py:class} PluginConfigSection(key: str)
:canonical: archivebox.config.collection.PluginConfigSection

```{autodoc2-docstring} archivebox.config.collection.PluginConfigSection
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.config.collection.PluginConfigSection.__init__
```

````{py:attribute} toml_section_header
:canonical: archivebox.config.collection.PluginConfigSection.toml_section_header
:value: >
   'PLUGINS'

```{autodoc2-docstring} archivebox.config.collection.PluginConfigSection.toml_section_header
```

````

````{py:method} __getattr__(name: str) -> typing.Any
:canonical: archivebox.config.collection.PluginConfigSection.__getattr__

```{autodoc2-docstring} archivebox.config.collection.PluginConfigSection.__getattr__
```

````

````{py:method} update_in_place(warn: bool = True, persist: bool = False, **kwargs)
:canonical: archivebox.config.collection.PluginConfigSection.update_in_place

```{autodoc2-docstring} archivebox.config.collection.PluginConfigSection.update_in_place
```

````

`````

````{py:function} section_for_key(key: str) -> typing.Any
:canonical: archivebox.config.collection.section_for_key

```{autodoc2-docstring} archivebox.config.collection.section_for_key
```
````

````{py:function} write_config_file(config: typing.Dict[str, str]) -> benedict.benedict
:canonical: archivebox.config.collection.write_config_file

```{autodoc2-docstring} archivebox.config.collection.write_config_file
```
````

````{py:function} load_config(defaults: typing.Dict[str, typing.Any], config: typing.Optional[benedict.benedict] = None, out_dir: typing.Optional[str] = None, env_vars: typing.Optional[os._Environ] = None, config_file_vars: typing.Optional[typing.Dict[str, str]] = None) -> benedict.benedict
:canonical: archivebox.config.collection.load_config

```{autodoc2-docstring} archivebox.config.collection.load_config
```
````

````{py:function} load_all_config()
:canonical: archivebox.config.collection.load_all_config

```{autodoc2-docstring} archivebox.config.collection.load_all_config
```
````
