# {py:mod}`archivebox.plugins_search.sqlite.apps`

```{py:module} archivebox.plugins_search.sqlite.apps
```

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SqliteftsConfig <archivebox.plugins_search.sqlite.apps.SqliteftsConfig>`
  -
* - {py:obj}`SqliteftsSearchBackend <archivebox.plugins_search.sqlite.apps.SqliteftsSearchBackend>`
  -
* - {py:obj}`SqliteftsSearchPlugin <archivebox.plugins_search.sqlite.apps.SqliteftsSearchPlugin>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_escape_sqlite3 <archivebox.plugins_search.sqlite.apps._escape_sqlite3>`
  - ```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps._escape_sqlite3
    :summary:
    ```
* - {py:obj}`_escape_sqlite3_value <archivebox.plugins_search.sqlite.apps._escape_sqlite3_value>`
  - ```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps._escape_sqlite3_value
    :summary:
    ```
* - {py:obj}`_escape_sqlite3_identifier <archivebox.plugins_search.sqlite.apps._escape_sqlite3_identifier>`
  - ```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps._escape_sqlite3_identifier
    :summary:
    ```
* - {py:obj}`_create_tables <archivebox.plugins_search.sqlite.apps._create_tables>`
  - ```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps._create_tables
    :summary:
    ```
* - {py:obj}`_handle_query_exception <archivebox.plugins_search.sqlite.apps._handle_query_exception>`
  - ```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps._handle_query_exception
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.plugins_search.sqlite.apps.__package__>`
  - ```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.__package__
    :summary:
    ```
* - {py:obj}`SQLITEFTS_CONFIG <archivebox.plugins_search.sqlite.apps.SQLITEFTS_CONFIG>`
  - ```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SQLITEFTS_CONFIG
    :summary:
    ```
* - {py:obj}`SQLITEFTS_SEARCH_BACKEND <archivebox.plugins_search.sqlite.apps.SQLITEFTS_SEARCH_BACKEND>`
  - ```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SQLITEFTS_SEARCH_BACKEND
    :summary:
    ```
* - {py:obj}`PLUGIN <archivebox.plugins_search.sqlite.apps.PLUGIN>`
  - ```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.PLUGIN
    :summary:
    ```
* - {py:obj}`DJANGO_APP <archivebox.plugins_search.sqlite.apps.DJANGO_APP>`
  - ```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.DJANGO_APP
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.plugins_search.sqlite.apps.__package__
:value: >
   'archivebox.plugins_search.sqlite'

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.__package__
```

````

`````{py:class} SqliteftsConfig(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[typing.Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_implicit_flags: bool | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, **values: typing.Any)
:canonical: archivebox.plugins_search.sqlite.apps.SqliteftsConfig

Bases: {py:obj}`abx.archivebox.base_configset.BaseConfigSet`

````{py:attribute} SQLITEFTS_SEPARATE_DATABASE
:canonical: archivebox.plugins_search.sqlite.apps.SqliteftsConfig.SQLITEFTS_SEPARATE_DATABASE
:type: bool
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SqliteftsConfig.SQLITEFTS_SEPARATE_DATABASE
```

````

````{py:attribute} SQLITEFTS_TOKENIZERS
:canonical: archivebox.plugins_search.sqlite.apps.SqliteftsConfig.SQLITEFTS_TOKENIZERS
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SqliteftsConfig.SQLITEFTS_TOKENIZERS
```

````

````{py:attribute} SQLITEFTS_MAX_LENGTH
:canonical: archivebox.plugins_search.sqlite.apps.SqliteftsConfig.SQLITEFTS_MAX_LENGTH
:type: int
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SqliteftsConfig.SQLITEFTS_MAX_LENGTH
```

````

````{py:attribute} SQLITEFTS_DB
:canonical: archivebox.plugins_search.sqlite.apps.SqliteftsConfig.SQLITEFTS_DB
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SqliteftsConfig.SQLITEFTS_DB
```

````

````{py:attribute} SQLITEFTS_TABLE
:canonical: archivebox.plugins_search.sqlite.apps.SqliteftsConfig.SQLITEFTS_TABLE
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SqliteftsConfig.SQLITEFTS_TABLE
```

````

````{py:attribute} SQLITEFTS_ID_TABLE
:canonical: archivebox.plugins_search.sqlite.apps.SqliteftsConfig.SQLITEFTS_ID_TABLE
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SqliteftsConfig.SQLITEFTS_ID_TABLE
```

````

````{py:attribute} SQLITEFTS_COLUMN
:canonical: archivebox.plugins_search.sqlite.apps.SqliteftsConfig.SQLITEFTS_COLUMN
:type: str
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SqliteftsConfig.SQLITEFTS_COLUMN
```

````

````{py:method} validate_fts_separate_database()
:canonical: archivebox.plugins_search.sqlite.apps.SqliteftsConfig.validate_fts_separate_database

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SqliteftsConfig.validate_fts_separate_database
```

````

````{py:property} get_connection
:canonical: archivebox.plugins_search.sqlite.apps.SqliteftsConfig.get_connection
:type: typing.Callable[[], sqlite3.Connection]

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SqliteftsConfig.get_connection
```

````

````{py:property} SQLITE_BIND
:canonical: archivebox.plugins_search.sqlite.apps.SqliteftsConfig.SQLITE_BIND
:type: str

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SqliteftsConfig.SQLITE_BIND
```

````

````{py:property} SQLITE_LIMIT_LENGTH
:canonical: archivebox.plugins_search.sqlite.apps.SqliteftsConfig.SQLITE_LIMIT_LENGTH
:type: int

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SqliteftsConfig.SQLITE_LIMIT_LENGTH
```

````

`````

````{py:data} SQLITEFTS_CONFIG
:canonical: archivebox.plugins_search.sqlite.apps.SQLITEFTS_CONFIG
:value: >
   'SqliteftsConfig(...)'

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SQLITEFTS_CONFIG
```

````

````{py:function} _escape_sqlite3(value: str, *, quote: str, errors='strict') -> str
:canonical: archivebox.plugins_search.sqlite.apps._escape_sqlite3

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps._escape_sqlite3
```
````

````{py:function} _escape_sqlite3_value(value: str, errors='strict') -> str
:canonical: archivebox.plugins_search.sqlite.apps._escape_sqlite3_value

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps._escape_sqlite3_value
```
````

````{py:function} _escape_sqlite3_identifier(value: str) -> str
:canonical: archivebox.plugins_search.sqlite.apps._escape_sqlite3_identifier

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps._escape_sqlite3_identifier
```
````

````{py:function} _create_tables()
:canonical: archivebox.plugins_search.sqlite.apps._create_tables

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps._create_tables
```
````

````{py:function} _handle_query_exception(exc: Exception)
:canonical: archivebox.plugins_search.sqlite.apps._handle_query_exception

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps._handle_query_exception
```
````

`````{py:class} SqliteftsSearchBackend(/, **data: typing.Any)
:canonical: archivebox.plugins_search.sqlite.apps.SqliteftsSearchBackend

Bases: {py:obj}`abx.archivebox.base_searchbackend.BaseSearchBackend`

````{py:attribute} name
:canonical: archivebox.plugins_search.sqlite.apps.SqliteftsSearchBackend.name
:type: str
:value: >
   'sqlite'

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SqliteftsSearchBackend.name
```

````

````{py:attribute} docs_url
:canonical: archivebox.plugins_search.sqlite.apps.SqliteftsSearchBackend.docs_url
:type: str
:value: >
   'https://www.sqlite.org/fts5.html'

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SqliteftsSearchBackend.docs_url
```

````

````{py:method} index(snapshot_id: str, texts: typing.List[str])
:canonical: archivebox.plugins_search.sqlite.apps.SqliteftsSearchBackend.index
:staticmethod:

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SqliteftsSearchBackend.index
```

````

````{py:method} search(text: str) -> typing.List[str]
:canonical: archivebox.plugins_search.sqlite.apps.SqliteftsSearchBackend.search
:staticmethod:

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SqliteftsSearchBackend.search
```

````

````{py:method} flush(snapshot_ids: typing.Iterable[str])
:canonical: archivebox.plugins_search.sqlite.apps.SqliteftsSearchBackend.flush
:staticmethod:

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SqliteftsSearchBackend.flush
```

````

`````

````{py:data} SQLITEFTS_SEARCH_BACKEND
:canonical: archivebox.plugins_search.sqlite.apps.SQLITEFTS_SEARCH_BACKEND
:value: >
   'SqliteftsSearchBackend(...)'

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SQLITEFTS_SEARCH_BACKEND
```

````

`````{py:class} SqliteftsSearchPlugin(/, **data: typing.Any)
:canonical: archivebox.plugins_search.sqlite.apps.SqliteftsSearchPlugin

Bases: {py:obj}`abx.archivebox.base_plugin.BasePlugin`

````{py:attribute} app_label
:canonical: archivebox.plugins_search.sqlite.apps.SqliteftsSearchPlugin.app_label
:type: str
:value: >
   'sqlitefts'

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SqliteftsSearchPlugin.app_label
```

````

````{py:attribute} verbose_name
:canonical: archivebox.plugins_search.sqlite.apps.SqliteftsSearchPlugin.verbose_name
:type: str
:value: >
   'SQLite FTS5 Search'

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SqliteftsSearchPlugin.verbose_name
```

````

````{py:attribute} hooks
:canonical: archivebox.plugins_search.sqlite.apps.SqliteftsSearchPlugin.hooks
:type: typing.List[pydantic.InstanceOf[abx.archivebox.base_hook.BaseHook]]
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.SqliteftsSearchPlugin.hooks
```

````

`````

````{py:data} PLUGIN
:canonical: archivebox.plugins_search.sqlite.apps.PLUGIN
:value: >
   'SqliteftsSearchPlugin(...)'

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.PLUGIN
```

````

````{py:data} DJANGO_APP
:canonical: archivebox.plugins_search.sqlite.apps.DJANGO_APP
:value: >
   None

```{autodoc2-docstring} archivebox.plugins_search.sqlite.apps.DJANGO_APP
```

````
