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
:staticmethod:

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_collection_config_path
```

````

````{py:method} get_system_config_path() -> pathlib.Path
:canonical: abx_spec_config.ConfigPluginSpec.get_system_config_path
:staticmethod:

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_system_config_path
```

````

````{py:method} get_CONFIG() -> dict[abx.PluginId, BaseConfigSet | ConstantsDict]
:canonical: abx_spec_config.ConfigPluginSpec.get_CONFIG
:staticmethod:

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_CONFIG
```

````

````{py:method} get_CONFIGS() -> dict[abx.PluginId, abx_spec_config.base_configset.BaseConfigSet]
:canonical: abx_spec_config.ConfigPluginSpec.get_CONFIGS
:staticmethod:

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_CONFIGS
```

````

````{py:method} get_FLAT_CONFIG() -> dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.ConfigPluginSpec.get_FLAT_CONFIG
:staticmethod:

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_FLAT_CONFIG
```

````

````{py:method} get_SCOPE_CONFIG(extra=None, archiveresult=None, snapshot=None, crawl=None, user=None, collection=..., environment=..., machine=..., default=...) -> dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.ConfigPluginSpec.get_SCOPE_CONFIG
:staticmethod:

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_SCOPE_CONFIG
```

````

````{py:method} get_archiveresult_config(archiveresult) -> dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.ConfigPluginSpec.get_archiveresult_config
:staticmethod:

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_archiveresult_config
```

````

````{py:method} get_snapshot_config(snapshot) -> dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.ConfigPluginSpec.get_snapshot_config
:staticmethod:

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_snapshot_config
```

````

````{py:method} get_crawl_config(crawl) -> dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.ConfigPluginSpec.get_crawl_config
:staticmethod:

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_crawl_config
```

````

````{py:method} get_user_config(user=None) -> dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.ConfigPluginSpec.get_user_config
:staticmethod:

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_user_config
```

````

````{py:method} get_collection_config(collection=...) -> dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.ConfigPluginSpec.get_collection_config
:staticmethod:

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_collection_config
```

````

````{py:method} get_environment_config(environment=...) -> dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.ConfigPluginSpec.get_environment_config
:staticmethod:

```{autodoc2-docstring} abx_spec_config.ConfigPluginSpec.get_environment_config
```

````

````{py:method} get_default_config(default=...) -> dict[abx_spec_config.base_configset.ConfigKeyStr, typing.Any]
:canonical: abx_spec_config.ConfigPluginSpec.get_default_config
:staticmethod:

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
