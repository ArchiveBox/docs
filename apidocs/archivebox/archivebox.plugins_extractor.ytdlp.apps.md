# {py:mod}`archivebox.plugins_extractor.ytdlp.apps`

```{py:module} archivebox.plugins_extractor.ytdlp.apps
```

```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`YtdlpConfig <archivebox.plugins_extractor.ytdlp.apps.YtdlpConfig>`
  -
* - {py:obj}`YtdlpBinary <archivebox.plugins_extractor.ytdlp.apps.YtdlpBinary>`
  -
* - {py:obj}`FfmpegBinary <archivebox.plugins_extractor.ytdlp.apps.FfmpegBinary>`
  -
* - {py:obj}`YtdlpPlugin <archivebox.plugins_extractor.ytdlp.apps.YtdlpPlugin>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`YTDLP_CONFIG <archivebox.plugins_extractor.ytdlp.apps.YTDLP_CONFIG>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.YTDLP_CONFIG
    :summary:
    ```
* - {py:obj}`YTDLP_BINARY <archivebox.plugins_extractor.ytdlp.apps.YTDLP_BINARY>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.YTDLP_BINARY
    :summary:
    ```
* - {py:obj}`FFMPEG_BINARY <archivebox.plugins_extractor.ytdlp.apps.FFMPEG_BINARY>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.FFMPEG_BINARY
    :summary:
    ```
* - {py:obj}`PLUGIN <archivebox.plugins_extractor.ytdlp.apps.PLUGIN>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.PLUGIN
    :summary:
    ```
* - {py:obj}`DJANGO_APP <archivebox.plugins_extractor.ytdlp.apps.DJANGO_APP>`
  - ```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.DJANGO_APP
    :summary:
    ```
````

### API

`````{py:class} YtdlpConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_implicit_flags: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.plugins_extractor.ytdlp.apps.YtdlpConfig

Bases: {py:obj}`abx.archivebox.base_configset.BaseConfigSet`

````{py:attribute} USE_YTDLP
:canonical: archivebox.plugins_extractor.ytdlp.apps.YtdlpConfig.USE_YTDLP
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.YtdlpConfig.USE_YTDLP
```

````

````{py:attribute} YTDLP_BINARY
:canonical: archivebox.plugins_extractor.ytdlp.apps.YtdlpConfig.YTDLP_BINARY
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.YtdlpConfig.YTDLP_BINARY
```

````

````{py:attribute} YTDLP_EXTRA_ARGS
:canonical: archivebox.plugins_extractor.ytdlp.apps.YtdlpConfig.YTDLP_EXTRA_ARGS
:type: typing.List[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.YtdlpConfig.YTDLP_EXTRA_ARGS
```

````

````{py:attribute} YTDLP_CHECK_SSL_VALIDITY
:canonical: archivebox.plugins_extractor.ytdlp.apps.YtdlpConfig.YTDLP_CHECK_SSL_VALIDITY
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.YtdlpConfig.YTDLP_CHECK_SSL_VALIDITY
```

````

````{py:attribute} YTDLP_TIMEOUT
:canonical: archivebox.plugins_extractor.ytdlp.apps.YtdlpConfig.YTDLP_TIMEOUT
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.YtdlpConfig.YTDLP_TIMEOUT
```

````

````{py:method} validate_use_ytdlp()
:canonical: archivebox.plugins_extractor.ytdlp.apps.YtdlpConfig.validate_use_ytdlp

```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.YtdlpConfig.validate_use_ytdlp
```

````

`````

````{py:data} YTDLP_CONFIG
:canonical: archivebox.plugins_extractor.ytdlp.apps.YTDLP_CONFIG
:value: >
   'YtdlpConfig(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.YTDLP_CONFIG
```

````

`````{py:class} YtdlpBinary(/, **data: typing.Any)
:canonical: archivebox.plugins_extractor.ytdlp.apps.YtdlpBinary

Bases: {py:obj}`abx.archivebox.base_binary.BaseBinary`

````{py:attribute} name
:canonical: archivebox.plugins_extractor.ytdlp.apps.YtdlpBinary.name
:type: pydantic_pkgr.BinName
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.YtdlpBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: archivebox.plugins_extractor.ytdlp.apps.YtdlpBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.YtdlpBinary.binproviders_supported
```

````

`````

````{py:data} YTDLP_BINARY
:canonical: archivebox.plugins_extractor.ytdlp.apps.YTDLP_BINARY
:value: >
   'YtdlpBinary(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.YTDLP_BINARY
```

````

`````{py:class} FfmpegBinary(/, **data: typing.Any)
:canonical: archivebox.plugins_extractor.ytdlp.apps.FfmpegBinary

Bases: {py:obj}`abx.archivebox.base_binary.BaseBinary`

````{py:attribute} name
:canonical: archivebox.plugins_extractor.ytdlp.apps.FfmpegBinary.name
:type: pydantic_pkgr.BinName
:value: >
   'ffmpeg'

```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.FfmpegBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: archivebox.plugins_extractor.ytdlp.apps.FfmpegBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.FfmpegBinary.binproviders_supported
```

````

````{py:attribute} provider_overrides
:canonical: archivebox.plugins_extractor.ytdlp.apps.FfmpegBinary.provider_overrides
:type: typing.Dict[pydantic_pkgr.BinProviderName, pydantic_pkgr.ProviderLookupDict]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.FfmpegBinary.provider_overrides
```

````

`````

````{py:data} FFMPEG_BINARY
:canonical: archivebox.plugins_extractor.ytdlp.apps.FFMPEG_BINARY
:value: >
   'FfmpegBinary(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.FFMPEG_BINARY
```

````

`````{py:class} YtdlpPlugin(/, **data: typing.Any)
:canonical: archivebox.plugins_extractor.ytdlp.apps.YtdlpPlugin

Bases: {py:obj}`abx.archivebox.base_plugin.BasePlugin`

````{py:attribute} app_label
:canonical: archivebox.plugins_extractor.ytdlp.apps.YtdlpPlugin.app_label
:type: str
:value: >
   'ytdlp'

```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.YtdlpPlugin.app_label
```

````

````{py:attribute} verbose_name
:canonical: archivebox.plugins_extractor.ytdlp.apps.YtdlpPlugin.verbose_name
:type: str
:value: >
   'YT-DLP'

```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.YtdlpPlugin.verbose_name
```

````

````{py:attribute} docs_url
:canonical: archivebox.plugins_extractor.ytdlp.apps.YtdlpPlugin.docs_url
:type: str
:value: >
   'https://github.com/yt-dlp/yt-dlp'

```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.YtdlpPlugin.docs_url
```

````

````{py:attribute} hooks
:canonical: archivebox.plugins_extractor.ytdlp.apps.YtdlpPlugin.hooks
:type: typing.List[pydantic.InstanceOf[abx.archivebox.base_hook.BaseHook]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.YtdlpPlugin.hooks
```

````

`````

````{py:data} PLUGIN
:canonical: archivebox.plugins_extractor.ytdlp.apps.PLUGIN
:value: >
   'YtdlpPlugin(...)'

```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.PLUGIN
```

````

````{py:data} DJANGO_APP
:canonical: archivebox.plugins_extractor.ytdlp.apps.DJANGO_APP
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_extractor.ytdlp.apps.DJANGO_APP
```

````
