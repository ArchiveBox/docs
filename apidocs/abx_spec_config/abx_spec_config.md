# {py:mod}`abx_spec_config`

```{py:module} abx_spec_config
```

```{autodoc2-docstring} abx_spec_config
:allowtitles:
```

## Submodules

```{toctree}
:titlesonly:
:maxdepth: 1

abx_spec_config.base_configset
abx_spec_config.toml_util
```

## Package Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ConfigPluginSpec <abx_spec_config.ConfigPluginSpec>`
  - ```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec
    :summary:
    ```
* - {py:obj}`ExpectedPluginSpec <abx_spec_config.ExpectedPluginSpec>`
  - ```{autodoc2-docstring} abx_spec_config.ExpectedPluginSpec
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__order__ <abx_spec_config.__order__>`
  - ```{autodoc2-docstring} abx_spec_config.__order__
    :summary:
    ```
* - {py:obj}`PLUGIN_SPEC <abx_spec_config.PLUGIN_SPEC>`
  - ```{autodoc2-docstring} abx_spec_config.PLUGIN_SPEC
    :summary:
    ```
* - {py:obj}`TypedPluginManager <abx_spec_config.TypedPluginManager>`
  - ```{autodoc2-docstring} abx_spec_config.TypedPluginManager
    :summary:
    ```
* - {py:obj}`pm <abx_spec_config.pm>`
  - ```{autodoc2-docstring} abx_spec_config.pm
    :summary:
    ```
````

### API

````{py:data} __order__
:canonical: abx_spec_config.__order__
:value: >
   100

```{autodoc2-docstring} abx_spec_config.__order__
```

````

`````{py:class} ConfigPluginSpec
:canonical: abx_spec_config.ConfigPluginSpec

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec
```

````{py:method} get_collection_config_path() -> pathlib.Path
:canonical: abx_spec_config.ConfigPluginSpec.get_collection_config_path

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_collection_config_path
```

````

````{py:method} get_system_config_path() -> pathlib.Path
:canonical: abx_spec_config.ConfigPluginSpec.get_system_config_path

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_system_config_path
```

````

````{py:method} get_CONFIG() -> typing.Dict[abx.PluginId, abx_spec_config.base_configset.BaseConfigSet]
:canonical: abx_spec_config.ConfigPluginSpec.get_CONFIG

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_CONFIG
```

````

````{py:method} get_CONFIGS() -> typing.Dict[abx.PluginId, abx_spec_config.base_configset.BaseConfigSet]
:canonical: abx_spec_config.ConfigPluginSpec.get_CONFIGS

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_CONFIGS
```

````

````{py:method} get_FLAT_CONFIG() -> typing.Dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.ConfigPluginSpec.get_FLAT_CONFIG

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_FLAT_CONFIG
```

````

````{py:method} get_SCOPE_CONFIG(extra=None, archiveresult=None, snapshot=None, crawl=None, user=None, collection=..., environment=..., machine=..., default=...) -> typing.Dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.ConfigPluginSpec.get_SCOPE_CONFIG

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_SCOPE_CONFIG
```

````

````{py:method} get_archiveresult_config(archiveresult) -> typing.Dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.ConfigPluginSpec.get_archiveresult_config

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_archiveresult_config
```

````

````{py:method} get_snapshot_config(snapshot) -> typing.Dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.ConfigPluginSpec.get_snapshot_config

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_snapshot_config
```

````

````{py:method} get_crawl_config(crawl) -> typing.Dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.ConfigPluginSpec.get_crawl_config

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_crawl_config
```

````

````{py:method} get_user_config(user=None) -> typing.Dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.ConfigPluginSpec.get_user_config

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_user_config
```

````

````{py:method} get_collection_config(collection=...) -> typing.Dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.ConfigPluginSpec.get_collection_config

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_collection_config
```

````

````{py:method} get_environment_config(environment=...) -> typing.Dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.ConfigPluginSpec.get_environment_config

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_environment_config
```

````

````{py:method} get_default_config(default=...) -> typing.Dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.ConfigPluginSpec.get_default_config

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_default_config
```

````

`````

````{py:data} PLUGIN_SPEC
:canonical: abx_spec_config.PLUGIN_SPEC
:value: >
   None

```{autodoc2-docstring} abx_spec_config.PLUGIN_SPEC
```

````

````{py:class} ExpectedPluginSpec
:canonical: abx_spec_config.ExpectedPluginSpec

Bases: {py:obj}`abx_spec_config.ConfigPluginSpec`

```{autodoc2-docstring} abx_spec_config.ExpectedPluginSpec
```

````

````{py:data} TypedPluginManager
:canonical: abx_spec_config.TypedPluginManager
:value: >
   None

```{autodoc2-docstring} abx_spec_config.TypedPluginManager
```

````

````{py:data} pm
:canonical: abx_spec_config.pm
:value: >
   'cast(...)'

```{autodoc2-docstring} abx_spec_config.pm
```

````
