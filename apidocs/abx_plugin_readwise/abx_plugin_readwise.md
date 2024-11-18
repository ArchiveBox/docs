# {py:mod}`abx_plugin_readwise`

```{py:module} abx_plugin_readwise
```

```{autodoc2-docstring} abx_plugin_readwise
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ReadwiseConfig <abx_plugin_readwise.ReadwiseConfig>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_CONFIG <abx_plugin_readwise.get_CONFIG>`
  - ```{autodoc2-docstring} abx_plugin_readwise.get_CONFIG
    :summary:
    ```
* - {py:obj}`ready <abx_plugin_readwise.ready>`
  - ```{autodoc2-docstring} abx_plugin_readwise.ready
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__id__ <abx_plugin_readwise.__id__>`
  - ```{autodoc2-docstring} abx_plugin_readwise.__id__
    :summary:
    ```
* - {py:obj}`__label__ <abx_plugin_readwise.__label__>`
  - ```{autodoc2-docstring} abx_plugin_readwise.__label__
    :summary:
    ```
* - {py:obj}`__version__ <abx_plugin_readwise.__version__>`
  - ```{autodoc2-docstring} abx_plugin_readwise.__version__
    :summary:
    ```
* - {py:obj}`__author__ <abx_plugin_readwise.__author__>`
  - ```{autodoc2-docstring} abx_plugin_readwise.__author__
    :summary:
    ```
* - {py:obj}`__homepage__ <abx_plugin_readwise.__homepage__>`
  - ```{autodoc2-docstring} abx_plugin_readwise.__homepage__
    :summary:
    ```
* - {py:obj}`__dependencies__ <abx_plugin_readwise.__dependencies__>`
  - ```{autodoc2-docstring} abx_plugin_readwise.__dependencies__
    :summary:
    ```
* - {py:obj}`SOURCES_DIR <abx_plugin_readwise.SOURCES_DIR>`
  - ```{autodoc2-docstring} abx_plugin_readwise.SOURCES_DIR
    :summary:
    ```
````

### API

````{py:data} __id__
:canonical: abx_plugin_readwise.__id__
:value: >
   'abx_plugin_readwise_extractor'

```{autodoc2-docstring} abx_plugin_readwise.__id__
```

````

````{py:data} __label__
:canonical: abx_plugin_readwise.__label__
:value: >
   'Readwise API'

```{autodoc2-docstring} abx_plugin_readwise.__label__
```

````

````{py:data} __version__
:canonical: abx_plugin_readwise.__version__
:value: >
   '2024.10.27'

```{autodoc2-docstring} abx_plugin_readwise.__version__
```

````

````{py:data} __author__
:canonical: abx_plugin_readwise.__author__
:value: >
   'ArchiveBox'

```{autodoc2-docstring} abx_plugin_readwise.__author__
```

````

````{py:data} __homepage__
:canonical: abx_plugin_readwise.__homepage__
:value: >
   'https://github.com/ArchiveBox/ArchiveBox/tree/dev/archivebox/pkgs/abx-plugin-readwise-extractor'

```{autodoc2-docstring} abx_plugin_readwise.__homepage__
```

````

````{py:data} __dependencies__
:canonical: abx_plugin_readwise.__dependencies__
:value: >
   []

```{autodoc2-docstring} abx_plugin_readwise.__dependencies__
```

````

````{py:data} SOURCES_DIR
:canonical: abx_plugin_readwise.SOURCES_DIR
:value: >
   None

```{autodoc2-docstring} abx_plugin_readwise.SOURCES_DIR
```

````

`````{py:class} ReadwiseConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | None = None, _cli_ignore_unknown_args: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: abx_plugin_readwise.ReadwiseConfig

Bases: {py:obj}`abx_spec_config.base_configset.BaseConfigSet`

````{py:attribute} READWISE_DB_PATH
:canonical: abx_plugin_readwise.ReadwiseConfig.READWISE_DB_PATH
:type: pathlib.Path
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_readwise.ReadwiseConfig.READWISE_DB_PATH
```

````

````{py:attribute} READWISE_READER_TOKENS
:canonical: abx_plugin_readwise.ReadwiseConfig.READWISE_READER_TOKENS
:type: typing.Dict[str, str]
:value: >
   'Field(...)'

```{autodoc2-docstring} abx_plugin_readwise.ReadwiseConfig.READWISE_READER_TOKENS
```

````

`````

````{py:function} get_CONFIG()
:canonical: abx_plugin_readwise.get_CONFIG

```{autodoc2-docstring} abx_plugin_readwise.get_CONFIG
```
````

````{py:function} ready()
:canonical: abx_plugin_readwise.ready

```{autodoc2-docstring} abx_plugin_readwise.ready
```
````
