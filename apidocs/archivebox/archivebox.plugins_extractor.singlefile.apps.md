# {py:mod}`archivebox.plugins_extractor.singlefile.apps`

```{py:module} archivebox.plugins_extractor.singlefile.apps
```

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SinglefileConfig <archivebox.plugins_extractor.singlefile.apps.SinglefileConfig>`
  -
* - {py:obj}`SinglefileBinary <archivebox.plugins_extractor.singlefile.apps.SinglefileBinary>`
  -
* - {py:obj}`SinglefileExtractor <archivebox.plugins_extractor.singlefile.apps.SinglefileExtractor>`
  -
* - {py:obj}`SinglefileQueue <archivebox.plugins_extractor.singlefile.apps.SinglefileQueue>`
  -
* - {py:obj}`SinglefilePlugin <archivebox.plugins_extractor.singlefile.apps.SinglefilePlugin>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.plugins_extractor.singlefile.apps.__package__>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.__package__
    :summary:
    ```
* - {py:obj}`SINGLEFILE_CONFIG <archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_CONFIG>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_CONFIG
    :summary:
    ```
* - {py:obj}`SINGLEFILE_MIN_VERSION <archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_MIN_VERSION>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_MIN_VERSION
    :summary:
    ```
* - {py:obj}`SINGLEFILE_MAX_VERSION <archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_MAX_VERSION>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_MAX_VERSION
    :summary:
    ```
* - {py:obj}`SINGLEFILE_BINARY <archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_BINARY>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_BINARY
    :summary:
    ```
* - {py:obj}`PLUGIN_BINARIES <archivebox.plugins_extractor.singlefile.apps.PLUGIN_BINARIES>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.PLUGIN_BINARIES
    :summary:
    ```
* - {py:obj}`SINGLEFILE_EXTRACTOR <archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_EXTRACTOR>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_EXTRACTOR
    :summary:
    ```
* - {py:obj}`SINGLEFILE_QUEUE <archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_QUEUE>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_QUEUE
    :summary:
    ```
* - {py:obj}`PLUGIN <archivebox.plugins_extractor.singlefile.apps.PLUGIN>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.PLUGIN
    :summary:
    ```
* - {py:obj}`DJANGO_APP <archivebox.plugins_extractor.singlefile.apps.DJANGO_APP>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.DJANGO_APP
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.plugins_extractor.singlefile.apps.__package__
:value: >
   'archivebox.plugins_extractor.singlefile'

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.__package__
```

````

`````{py:class} SinglefileConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_implicit_flags: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefileConfig

Bases: {py:obj}`abx.archivebox.base_configset.BaseConfigSet`

````{py:attribute} SAVE_SINGLEFILE
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefileConfig.SAVE_SINGLEFILE
:type: bool
:value: >
   True

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SinglefileConfig.SAVE_SINGLEFILE
```

````

````{py:attribute} SINGLEFILE_USER_AGENT
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefileConfig.SINGLEFILE_USER_AGENT
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SinglefileConfig.SINGLEFILE_USER_AGENT
```

````

````{py:attribute} SINGLEFILE_TIMEOUT
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefileConfig.SINGLEFILE_TIMEOUT
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SinglefileConfig.SINGLEFILE_TIMEOUT
```

````

````{py:attribute} SINGLEFILE_CHECK_SSL_VALIDITY
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefileConfig.SINGLEFILE_CHECK_SSL_VALIDITY
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SinglefileConfig.SINGLEFILE_CHECK_SSL_VALIDITY
```

````

````{py:attribute} SINGLEFILE_COOKIES_FILE
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefileConfig.SINGLEFILE_COOKIES_FILE
:type: typing.Optional[pathlib.Path]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SinglefileConfig.SINGLEFILE_COOKIES_FILE
```

````

````{py:attribute} SINGLEFILE_BINARY
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefileConfig.SINGLEFILE_BINARY
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SinglefileConfig.SINGLEFILE_BINARY
```

````

````{py:attribute} SINGLEFILE_EXTRA_ARGS
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefileConfig.SINGLEFILE_EXTRA_ARGS
:type: typing.List[str]
:value: >
   []

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SinglefileConfig.SINGLEFILE_EXTRA_ARGS
```

````

`````

````{py:data} SINGLEFILE_CONFIG
:canonical: archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_CONFIG
:value: >
   'SinglefileConfig(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_CONFIG
```

````

````{py:data} SINGLEFILE_MIN_VERSION
:canonical: archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_MIN_VERSION
:value: >
   '1.1.54'

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_MIN_VERSION
```

````

````{py:data} SINGLEFILE_MAX_VERSION
:canonical: archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_MAX_VERSION
:value: >
   '1.1.60'

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_MAX_VERSION
```

````

`````{py:class} SinglefileBinary(/, **data: typing.Any)
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefileBinary

Bases: {py:obj}`abx.archivebox.base_binary.BaseBinary`

````{py:attribute} name
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefileBinary.name
:type: pydantic_pkgr.BinName
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SinglefileBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefileBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SinglefileBinary.binproviders_supported
```

````

````{py:attribute} provider_overrides
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefileBinary.provider_overrides
:type: typing.Dict[pydantic_pkgr.BinProviderName, pydantic_pkgr.ProviderLookupDict]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SinglefileBinary.provider_overrides
```

````

````{py:method} install(binprovider_name: typing.Optional[pydantic_pkgr.BinProviderName] = None) -> pydantic_pkgr.ShallowBinary
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefileBinary.install

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SinglefileBinary.install
```

````

````{py:method} load_or_install(binprovider_name: typing.Optional[pydantic_pkgr.BinProviderName] = None) -> pydantic_pkgr.ShallowBinary
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefileBinary.load_or_install

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SinglefileBinary.load_or_install
```

````

`````

````{py:data} SINGLEFILE_BINARY
:canonical: archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_BINARY
:value: >
   'SinglefileBinary(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_BINARY
```

````

````{py:data} PLUGIN_BINARIES
:canonical: archivebox.plugins_extractor.singlefile.apps.PLUGIN_BINARIES
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.PLUGIN_BINARIES
```

````

`````{py:class} SinglefileExtractor(/, **data: typing.Any)
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefileExtractor

Bases: {py:obj}`abx.archivebox.base_extractor.BaseExtractor`

````{py:attribute} name
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefileExtractor.name
:type: str
:value: >
   'singlefile'

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SinglefileExtractor.name
```

````

````{py:attribute} binary
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefileExtractor.binary
:type: pydantic_pkgr.BinName
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SinglefileExtractor.binary
```

````

````{py:method} get_output_path(snapshot) -> pathlib.Path
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefileExtractor.get_output_path

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SinglefileExtractor.get_output_path
```

````

`````

````{py:data} SINGLEFILE_EXTRACTOR
:canonical: archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_EXTRACTOR
:value: >
   'SinglefileExtractor(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_EXTRACTOR
```

````

`````{py:class} SinglefileQueue(/, **data: typing.Any)
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefileQueue

Bases: {py:obj}`abx.archivebox.base_queue.BaseQueue`

````{py:attribute} name
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefileQueue.name
:type: str
:value: >
   'singlefile'

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SinglefileQueue.name
```

````

````{py:attribute} binaries
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefileQueue.binaries
:type: typing.List[pydantic.InstanceOf[abx.archivebox.base_binary.BaseBinary]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SinglefileQueue.binaries
```

````

`````

````{py:data} SINGLEFILE_QUEUE
:canonical: archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_QUEUE
:value: >
   'SinglefileQueue(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SINGLEFILE_QUEUE
```

````

`````{py:class} SinglefilePlugin(/, **data: typing.Any)
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefilePlugin

Bases: {py:obj}`abx.archivebox.base_plugin.BasePlugin`

````{py:attribute} app_label
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefilePlugin.app_label
:type: str
:value: >
   'singlefile'

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SinglefilePlugin.app_label
```

````

````{py:attribute} verbose_name
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefilePlugin.verbose_name
:type: str
:value: >
   'SingleFile'

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SinglefilePlugin.verbose_name
```

````

````{py:attribute} hooks
:canonical: archivebox.plugins_extractor.singlefile.apps.SinglefilePlugin.hooks
:type: typing.List[pydantic.InstanceOf[abx.archivebox.base_hook.BaseHook]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.SinglefilePlugin.hooks
```

````

`````

````{py:data} PLUGIN
:canonical: archivebox.plugins_extractor.singlefile.apps.PLUGIN
:value: >
   'SinglefilePlugin(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.PLUGIN
```

````

````{py:data} DJANGO_APP
:canonical: archivebox.plugins_extractor.singlefile.apps.DJANGO_APP
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_extractor.singlefile.apps.DJANGO_APP
```

````
