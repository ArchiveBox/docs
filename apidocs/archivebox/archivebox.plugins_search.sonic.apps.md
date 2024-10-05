# {py:mod}`archivebox.plugins_search.sonic.apps`

```{py:module} archivebox.plugins_search.sonic.apps
```

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SonicConfig <archivebox.plugins_search.sonic.apps.SonicConfig>`
  -
* - {py:obj}`SonicBinary <archivebox.plugins_search.sonic.apps.SonicBinary>`
  -
* - {py:obj}`SonicSearchBackend <archivebox.plugins_search.sonic.apps.SonicSearchBackend>`
  -
* - {py:obj}`SonicSearchPlugin <archivebox.plugins_search.sonic.apps.SonicSearchPlugin>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.plugins_search.sonic.apps.__package__>`
  - ```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.__package__
    :summary:
    ```
* - {py:obj}`SONIC_LIB <archivebox.plugins_search.sonic.apps.SONIC_LIB>`
  - ```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SONIC_LIB
    :summary:
    ```
* - {py:obj}`SONIC_CONFIG <archivebox.plugins_search.sonic.apps.SONIC_CONFIG>`
  - ```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SONIC_CONFIG
    :summary:
    ```
* - {py:obj}`SONIC_BINARY <archivebox.plugins_search.sonic.apps.SONIC_BINARY>`
  - ```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SONIC_BINARY
    :summary:
    ```
* - {py:obj}`SONIC_SEARCH_BACKEND <archivebox.plugins_search.sonic.apps.SONIC_SEARCH_BACKEND>`
  - ```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SONIC_SEARCH_BACKEND
    :summary:
    ```
* - {py:obj}`PLUGIN <archivebox.plugins_search.sonic.apps.PLUGIN>`
  - ```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.PLUGIN
    :summary:
    ```
* - {py:obj}`DJANGO_APP <archivebox.plugins_search.sonic.apps.DJANGO_APP>`
  - ```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.DJANGO_APP
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.plugins_search.sonic.apps.__package__
:value: >
   'archivebox.plugins_search.sonic'

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.__package__
```

````

````{py:data} SONIC_LIB
:canonical: archivebox.plugins_search.sonic.apps.SONIC_LIB
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SONIC_LIB
```

````

`````{py:class} SonicConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_implicit_flags: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.plugins_search.sonic.apps.SonicConfig

Bases: {py:obj}`abx.archivebox.base_configset.BaseConfigSet`

````{py:attribute} SONIC_BINARY
:canonical: archivebox.plugins_search.sonic.apps.SonicConfig.SONIC_BINARY
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SonicConfig.SONIC_BINARY
```

````

````{py:attribute} SONIC_HOST
:canonical: archivebox.plugins_search.sonic.apps.SonicConfig.SONIC_HOST
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SonicConfig.SONIC_HOST
```

````

````{py:attribute} SONIC_PORT
:canonical: archivebox.plugins_search.sonic.apps.SonicConfig.SONIC_PORT
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SonicConfig.SONIC_PORT
```

````

````{py:attribute} SONIC_PASSWORD
:canonical: archivebox.plugins_search.sonic.apps.SonicConfig.SONIC_PASSWORD
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SonicConfig.SONIC_PASSWORD
```

````

````{py:attribute} SONIC_COLLECTION
:canonical: archivebox.plugins_search.sonic.apps.SonicConfig.SONIC_COLLECTION
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SonicConfig.SONIC_COLLECTION
```

````

````{py:attribute} SONIC_BUCKET
:canonical: archivebox.plugins_search.sonic.apps.SonicConfig.SONIC_BUCKET
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SonicConfig.SONIC_BUCKET
```

````

````{py:attribute} SONIC_MAX_CHUNK_LENGTH
:canonical: archivebox.plugins_search.sonic.apps.SonicConfig.SONIC_MAX_CHUNK_LENGTH
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SonicConfig.SONIC_MAX_CHUNK_LENGTH
```

````

````{py:attribute} SONIC_MAX_TEXT_LENGTH
:canonical: archivebox.plugins_search.sonic.apps.SonicConfig.SONIC_MAX_TEXT_LENGTH
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SonicConfig.SONIC_MAX_TEXT_LENGTH
```

````

````{py:attribute} SONIC_MAX_RETRIES
:canonical: archivebox.plugins_search.sonic.apps.SonicConfig.SONIC_MAX_RETRIES
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SonicConfig.SONIC_MAX_RETRIES
```

````

````{py:method} validate_sonic_port()
:canonical: archivebox.plugins_search.sonic.apps.SonicConfig.validate_sonic_port

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SonicConfig.validate_sonic_port
```

````

`````

````{py:data} SONIC_CONFIG
:canonical: archivebox.plugins_search.sonic.apps.SONIC_CONFIG
:value: >
   'SonicConfig(...)'

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SONIC_CONFIG
```

````

`````{py:class} SonicBinary(/, **data: typing.Any)
:canonical: archivebox.plugins_search.sonic.apps.SonicBinary

Bases: {py:obj}`abx.archivebox.base_binary.BaseBinary`

````{py:attribute} name
:canonical: archivebox.plugins_search.sonic.apps.SonicBinary.name
:type: pydantic_pkgr.BinName
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SonicBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: archivebox.plugins_search.sonic.apps.SonicBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SonicBinary.binproviders_supported
```

````

````{py:attribute} provider_overrides
:canonical: archivebox.plugins_search.sonic.apps.SonicBinary.provider_overrides
:type: typing.Dict[pydantic_pkgr.BinProviderName, pydantic_pkgr.ProviderLookupDict]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SonicBinary.provider_overrides
```

````

`````

````{py:data} SONIC_BINARY
:canonical: archivebox.plugins_search.sonic.apps.SONIC_BINARY
:value: >
   'SonicBinary(...)'

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SONIC_BINARY
```

````

`````{py:class} SonicSearchBackend(/, **data: typing.Any)
:canonical: archivebox.plugins_search.sonic.apps.SonicSearchBackend

Bases: {py:obj}`abx.archivebox.base_searchbackend.BaseSearchBackend`

````{py:attribute} name
:canonical: archivebox.plugins_search.sonic.apps.SonicSearchBackend.name
:type: str
:value: >
   'sonic'

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SonicSearchBackend.name
```

````

````{py:attribute} docs_url
:canonical: archivebox.plugins_search.sonic.apps.SonicSearchBackend.docs_url
:type: str
:value: >
   'https://github.com/valeriansaliou/sonic'

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SonicSearchBackend.docs_url
```

````

````{py:method} index(snapshot_id: str, texts: typing.List[str])
:canonical: archivebox.plugins_search.sonic.apps.SonicSearchBackend.index
:staticmethod:

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SonicSearchBackend.index
```

````

````{py:method} flush(snapshot_ids: typing.Generator[str, None, None])
:canonical: archivebox.plugins_search.sonic.apps.SonicSearchBackend.flush
:staticmethod:

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SonicSearchBackend.flush
```

````

````{py:method} search(text: str) -> typing.List[str]
:canonical: archivebox.plugins_search.sonic.apps.SonicSearchBackend.search
:staticmethod:

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SonicSearchBackend.search
```

````

`````

````{py:data} SONIC_SEARCH_BACKEND
:canonical: archivebox.plugins_search.sonic.apps.SONIC_SEARCH_BACKEND
:value: >
   'SonicSearchBackend(...)'

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SONIC_SEARCH_BACKEND
```

````

`````{py:class} SonicSearchPlugin(/, **data: typing.Any)
:canonical: archivebox.plugins_search.sonic.apps.SonicSearchPlugin

Bases: {py:obj}`abx.archivebox.base_plugin.BasePlugin`

````{py:attribute} app_label
:canonical: archivebox.plugins_search.sonic.apps.SonicSearchPlugin.app_label
:type: str
:value: >
   'sonic'

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SonicSearchPlugin.app_label
```

````

````{py:attribute} verbose_name
:canonical: archivebox.plugins_search.sonic.apps.SonicSearchPlugin.verbose_name
:type: str
:value: >
   'Sonic'

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SonicSearchPlugin.verbose_name
```

````

````{py:attribute} hooks
:canonical: archivebox.plugins_search.sonic.apps.SonicSearchPlugin.hooks
:type: typing.List[pydantic.InstanceOf[abx.archivebox.base_hook.BaseHook]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.SonicSearchPlugin.hooks
```

````

`````

````{py:data} PLUGIN
:canonical: archivebox.plugins_search.sonic.apps.PLUGIN
:value: >
   'SonicSearchPlugin(...)'

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.PLUGIN
```

````

````{py:data} DJANGO_APP
:canonical: archivebox.plugins_search.sonic.apps.DJANGO_APP
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_search.sonic.apps.DJANGO_APP
```

````
