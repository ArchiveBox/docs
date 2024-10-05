# {py:mod}`archivebox.plugins_search.ripgrep.apps`

```{py:module} archivebox.plugins_search.ripgrep.apps
```

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`RipgrepConfig <archivebox.plugins_search.ripgrep.apps.RipgrepConfig>`
  -
* - {py:obj}`RipgrepBinary <archivebox.plugins_search.ripgrep.apps.RipgrepBinary>`
  -
* - {py:obj}`RipgrepSearchBackend <archivebox.plugins_search.ripgrep.apps.RipgrepSearchBackend>`
  -
* - {py:obj}`RipgrepSearchPlugin <archivebox.plugins_search.ripgrep.apps.RipgrepSearchPlugin>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.plugins_search.ripgrep.apps.__package__>`
  - ```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.__package__
    :summary:
    ```
* - {py:obj}`RIPGREP_CONFIG <archivebox.plugins_search.ripgrep.apps.RIPGREP_CONFIG>`
  - ```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.RIPGREP_CONFIG
    :summary:
    ```
* - {py:obj}`RIPGREP_BINARY <archivebox.plugins_search.ripgrep.apps.RIPGREP_BINARY>`
  - ```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.RIPGREP_BINARY
    :summary:
    ```
* - {py:obj}`TIMESTAMP_REGEX <archivebox.plugins_search.ripgrep.apps.TIMESTAMP_REGEX>`
  - ```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.TIMESTAMP_REGEX
    :summary:
    ```
* - {py:obj}`RIPGREP_SEARCH_BACKEND <archivebox.plugins_search.ripgrep.apps.RIPGREP_SEARCH_BACKEND>`
  - ```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.RIPGREP_SEARCH_BACKEND
    :summary:
    ```
* - {py:obj}`PLUGIN <archivebox.plugins_search.ripgrep.apps.PLUGIN>`
  - ```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.PLUGIN
    :summary:
    ```
* - {py:obj}`DJANGO_APP <archivebox.plugins_search.ripgrep.apps.DJANGO_APP>`
  - ```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.DJANGO_APP
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.plugins_search.ripgrep.apps.__package__
:value: >
   'archivebox.plugins_search.ripgrep'

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.__package__
```

````

`````{py:class} RipgrepConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_implicit_flags: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.plugins_search.ripgrep.apps.RipgrepConfig

Bases: {py:obj}`abx.archivebox.base_configset.BaseConfigSet`

````{py:attribute} RIPGREP_BINARY
:canonical: archivebox.plugins_search.ripgrep.apps.RipgrepConfig.RIPGREP_BINARY
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.RipgrepConfig.RIPGREP_BINARY
```

````

````{py:attribute} RIPGREP_IGNORE_EXTENSIONS
:canonical: archivebox.plugins_search.ripgrep.apps.RipgrepConfig.RIPGREP_IGNORE_EXTENSIONS
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.RipgrepConfig.RIPGREP_IGNORE_EXTENSIONS
```

````

````{py:attribute} RIPGREP_ARGS_DEFAULT
:canonical: archivebox.plugins_search.ripgrep.apps.RipgrepConfig.RIPGREP_ARGS_DEFAULT
:type: typing.List[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.RipgrepConfig.RIPGREP_ARGS_DEFAULT
```

````

````{py:attribute} RIPGREP_SEARCH_DIR
:canonical: archivebox.plugins_search.ripgrep.apps.RipgrepConfig.RIPGREP_SEARCH_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.RipgrepConfig.RIPGREP_SEARCH_DIR
```

````

`````

````{py:data} RIPGREP_CONFIG
:canonical: archivebox.plugins_search.ripgrep.apps.RIPGREP_CONFIG
:value: >
   'RipgrepConfig(...)'

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.RIPGREP_CONFIG
```

````

`````{py:class} RipgrepBinary(/, **data: typing.Any)
:canonical: archivebox.plugins_search.ripgrep.apps.RipgrepBinary

Bases: {py:obj}`abx.archivebox.base_binary.BaseBinary`

````{py:attribute} name
:canonical: archivebox.plugins_search.ripgrep.apps.RipgrepBinary.name
:type: pydantic_pkgr.BinName
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.RipgrepBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: archivebox.plugins_search.ripgrep.apps.RipgrepBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.RipgrepBinary.binproviders_supported
```

````

````{py:attribute} provider_overrides
:canonical: archivebox.plugins_search.ripgrep.apps.RipgrepBinary.provider_overrides
:type: typing.Dict[pydantic_pkgr.BinProviderName, pydantic_pkgr.ProviderLookupDict]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.RipgrepBinary.provider_overrides
```

````

`````

````{py:data} RIPGREP_BINARY
:canonical: archivebox.plugins_search.ripgrep.apps.RIPGREP_BINARY
:value: >
   'RipgrepBinary(...)'

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.RIPGREP_BINARY
```

````

````{py:data} TIMESTAMP_REGEX
:canonical: archivebox.plugins_search.ripgrep.apps.TIMESTAMP_REGEX
:value: >
   'compile(...)'

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.TIMESTAMP_REGEX
```

````

`````{py:class} RipgrepSearchBackend(/, **data: typing.Any)
:canonical: archivebox.plugins_search.ripgrep.apps.RipgrepSearchBackend

Bases: {py:obj}`abx.archivebox.base_searchbackend.BaseSearchBackend`

````{py:attribute} name
:canonical: archivebox.plugins_search.ripgrep.apps.RipgrepSearchBackend.name
:type: str
:value: >
   'ripgrep'

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.RipgrepSearchBackend.name
```

````

````{py:attribute} docs_url
:canonical: archivebox.plugins_search.ripgrep.apps.RipgrepSearchBackend.docs_url
:type: str
:value: >
   'https://github.com/BurntSushi/ripgrep'

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.RipgrepSearchBackend.docs_url
```

````

````{py:method} index(snapshot_id: str, texts: typing.List[str])
:canonical: archivebox.plugins_search.ripgrep.apps.RipgrepSearchBackend.index
:staticmethod:

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.RipgrepSearchBackend.index
```

````

````{py:method} flush(snapshot_ids: typing.Iterable[str])
:canonical: archivebox.plugins_search.ripgrep.apps.RipgrepSearchBackend.flush
:staticmethod:

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.RipgrepSearchBackend.flush
```

````

````{py:method} search(text: str) -> typing.List[str]
:canonical: archivebox.plugins_search.ripgrep.apps.RipgrepSearchBackend.search
:staticmethod:

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.RipgrepSearchBackend.search
```

````

`````

````{py:data} RIPGREP_SEARCH_BACKEND
:canonical: archivebox.plugins_search.ripgrep.apps.RIPGREP_SEARCH_BACKEND
:value: >
   'RipgrepSearchBackend(...)'

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.RIPGREP_SEARCH_BACKEND
```

````

`````{py:class} RipgrepSearchPlugin(/, **data: typing.Any)
:canonical: archivebox.plugins_search.ripgrep.apps.RipgrepSearchPlugin

Bases: {py:obj}`abx.archivebox.base_plugin.BasePlugin`

````{py:attribute} app_label
:canonical: archivebox.plugins_search.ripgrep.apps.RipgrepSearchPlugin.app_label
:type: str
:value: >
   'ripgrep'

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.RipgrepSearchPlugin.app_label
```

````

````{py:attribute} verbose_name
:canonical: archivebox.plugins_search.ripgrep.apps.RipgrepSearchPlugin.verbose_name
:type: str
:value: >
   'Ripgrep'

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.RipgrepSearchPlugin.verbose_name
```

````

````{py:attribute} hooks
:canonical: archivebox.plugins_search.ripgrep.apps.RipgrepSearchPlugin.hooks
:type: typing.List[pydantic.InstanceOf[abx.archivebox.base_hook.BaseHook]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.RipgrepSearchPlugin.hooks
```

````

`````

````{py:data} PLUGIN
:canonical: archivebox.plugins_search.ripgrep.apps.PLUGIN
:value: >
   'RipgrepSearchPlugin(...)'

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.PLUGIN
```

````

````{py:data} DJANGO_APP
:canonical: archivebox.plugins_search.ripgrep.apps.DJANGO_APP
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_search.ripgrep.apps.DJANGO_APP
```

````
