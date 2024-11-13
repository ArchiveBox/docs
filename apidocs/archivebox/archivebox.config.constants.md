# {py:mod}`archivebox.config.constants`

```{py:module} archivebox.config.constants
```

```{autodoc2-docstring} archivebox.config.constants
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ConstantsDict <archivebox.config.constants.ConstantsDict>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.config.constants.__package__>`
  - ```{autodoc2-docstring} archivebox.config.constants.__package__
    :summary:
    ```
* - {py:obj}`CONSTANTS <archivebox.config.constants.CONSTANTS>`
  - ```{autodoc2-docstring} archivebox.config.constants.CONSTANTS
    :summary:
    ```
* - {py:obj}`CONSTANTS_CONFIG <archivebox.config.constants.CONSTANTS_CONFIG>`
  - ```{autodoc2-docstring} archivebox.config.constants.CONSTANTS_CONFIG
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.config.constants.__package__
:value: >
   'archivebox.config'

```{autodoc2-docstring} archivebox.config.constants.__package__
```

````

`````{py:class} ConstantsDict
:canonical: archivebox.config.constants.ConstantsDict

Bases: {py:obj}`collections.abc.Mapping`

````{py:attribute} PACKAGE_DIR
:canonical: archivebox.config.constants.ConstantsDict.PACKAGE_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.PACKAGE_DIR
```

````

````{py:attribute} DATA_DIR
:canonical: archivebox.config.constants.ConstantsDict.DATA_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.DATA_DIR
```

````

````{py:attribute} ARCHIVE_DIR
:canonical: archivebox.config.constants.ConstantsDict.ARCHIVE_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.ARCHIVE_DIR
```

````

````{py:attribute} MACHINE_TYPE
:canonical: archivebox.config.constants.ConstantsDict.MACHINE_TYPE
:type: str
:value: >
   'get_machine_type(...)'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.MACHINE_TYPE
```

````

````{py:attribute} MACHINE_ID
:canonical: archivebox.config.constants.ConstantsDict.MACHINE_ID
:type: str
:value: >
   'get_machine_id(...)'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.MACHINE_ID
```

````

````{py:attribute} COLLECTION_ID
:canonical: archivebox.config.constants.ConstantsDict.COLLECTION_ID
:type: str
:value: >
   'get_collection_id(...)'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.COLLECTION_ID
```

````

````{py:attribute} VERSION
:canonical: archivebox.config.constants.ConstantsDict.VERSION
:type: str
:value: >
   'detect_installed_version(...)'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.VERSION
```

````

````{py:attribute} IN_DOCKER
:canonical: archivebox.config.constants.ConstantsDict.IN_DOCKER
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.IN_DOCKER
```

````

````{py:attribute} IS_ROOT
:canonical: archivebox.config.constants.ConstantsDict.IS_ROOT
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.IS_ROOT
```

````

````{py:attribute} ARCHIVEBOX_USER
:canonical: archivebox.config.constants.ConstantsDict.ARCHIVEBOX_USER
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.ARCHIVEBOX_USER
```

````

````{py:attribute} ARCHIVEBOX_GROUP
:canonical: archivebox.config.constants.ConstantsDict.ARCHIVEBOX_GROUP
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.ARCHIVEBOX_GROUP
```

````

````{py:attribute} RUNNING_AS_UID
:canonical: archivebox.config.constants.ConstantsDict.RUNNING_AS_UID
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.RUNNING_AS_UID
```

````

````{py:attribute} RUNNING_AS_GID
:canonical: archivebox.config.constants.ConstantsDict.RUNNING_AS_GID
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.RUNNING_AS_GID
```

````

````{py:attribute} DEFAULT_PUID
:canonical: archivebox.config.constants.ConstantsDict.DEFAULT_PUID
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.DEFAULT_PUID
```

````

````{py:attribute} DEFAULT_PGID
:canonical: archivebox.config.constants.ConstantsDict.DEFAULT_PGID
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.DEFAULT_PGID
```

````

````{py:attribute} IS_INSIDE_VENV
:canonical: archivebox.config.constants.ConstantsDict.IS_INSIDE_VENV
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.IS_INSIDE_VENV
```

````

````{py:attribute} PACKAGE_DIR_NAME
:canonical: archivebox.config.constants.ConstantsDict.PACKAGE_DIR_NAME
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.PACKAGE_DIR_NAME
```

````

````{py:attribute} TEMPLATES_DIR_NAME
:canonical: archivebox.config.constants.ConstantsDict.TEMPLATES_DIR_NAME
:type: str
:value: >
   'templates'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.TEMPLATES_DIR_NAME
```

````

````{py:attribute} TEMPLATES_DIR
:canonical: archivebox.config.constants.ConstantsDict.TEMPLATES_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.TEMPLATES_DIR
```

````

````{py:attribute} STATIC_DIR_NAME
:canonical: archivebox.config.constants.ConstantsDict.STATIC_DIR_NAME
:type: str
:value: >
   'static'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.STATIC_DIR_NAME
```

````

````{py:attribute} STATIC_DIR
:canonical: archivebox.config.constants.ConstantsDict.STATIC_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.STATIC_DIR
```

````

````{py:attribute} ARCHIVE_DIR_NAME
:canonical: archivebox.config.constants.ConstantsDict.ARCHIVE_DIR_NAME
:type: str
:value: >
   'archive'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.ARCHIVE_DIR_NAME
```

````

````{py:attribute} SOURCES_DIR_NAME
:canonical: archivebox.config.constants.ConstantsDict.SOURCES_DIR_NAME
:type: str
:value: >
   'sources'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.SOURCES_DIR_NAME
```

````

````{py:attribute} PERSONAS_DIR_NAME
:canonical: archivebox.config.constants.ConstantsDict.PERSONAS_DIR_NAME
:type: str
:value: >
   'personas'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.PERSONAS_DIR_NAME
```

````

````{py:attribute} CRONTABS_DIR_NAME
:canonical: archivebox.config.constants.ConstantsDict.CRONTABS_DIR_NAME
:type: str
:value: >
   'crontabs'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.CRONTABS_DIR_NAME
```

````

````{py:attribute} CACHE_DIR_NAME
:canonical: archivebox.config.constants.ConstantsDict.CACHE_DIR_NAME
:type: str
:value: >
   'cache'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.CACHE_DIR_NAME
```

````

````{py:attribute} LOGS_DIR_NAME
:canonical: archivebox.config.constants.ConstantsDict.LOGS_DIR_NAME
:type: str
:value: >
   'logs'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.LOGS_DIR_NAME
```

````

````{py:attribute} USER_PLUGINS_DIR_NAME
:canonical: archivebox.config.constants.ConstantsDict.USER_PLUGINS_DIR_NAME
:type: str
:value: >
   'user_plugins'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.USER_PLUGINS_DIR_NAME
```

````

````{py:attribute} CUSTOM_TEMPLATES_DIR_NAME
:canonical: archivebox.config.constants.ConstantsDict.CUSTOM_TEMPLATES_DIR_NAME
:type: str
:value: >
   'user_templates'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.CUSTOM_TEMPLATES_DIR_NAME
```

````

````{py:attribute} SOURCES_DIR
:canonical: archivebox.config.constants.ConstantsDict.SOURCES_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.SOURCES_DIR
```

````

````{py:attribute} PERSONAS_DIR
:canonical: archivebox.config.constants.ConstantsDict.PERSONAS_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.PERSONAS_DIR
```

````

````{py:attribute} LOGS_DIR
:canonical: archivebox.config.constants.ConstantsDict.LOGS_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.LOGS_DIR
```

````

````{py:attribute} CACHE_DIR
:canonical: archivebox.config.constants.ConstantsDict.CACHE_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.CACHE_DIR
```

````

````{py:attribute} CUSTOM_TEMPLATES_DIR
:canonical: archivebox.config.constants.ConstantsDict.CUSTOM_TEMPLATES_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.CUSTOM_TEMPLATES_DIR
```

````

````{py:attribute} USER_PLUGINS_DIR
:canonical: archivebox.config.constants.ConstantsDict.USER_PLUGINS_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.USER_PLUGINS_DIR
```

````

````{py:attribute} CONFIG_FILENAME
:canonical: archivebox.config.constants.ConstantsDict.CONFIG_FILENAME
:type: str
:value: >
   'ArchiveBox.conf'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.CONFIG_FILENAME
```

````

````{py:attribute} SQL_INDEX_FILENAME
:canonical: archivebox.config.constants.ConstantsDict.SQL_INDEX_FILENAME
:type: str
:value: >
   'index.sqlite3'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.SQL_INDEX_FILENAME
```

````

````{py:attribute} QUEUE_DATABASE_FILENAME
:canonical: archivebox.config.constants.ConstantsDict.QUEUE_DATABASE_FILENAME
:type: str
:value: >
   'queue.sqlite3'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.QUEUE_DATABASE_FILENAME
```

````

````{py:attribute} CONFIG_FILE
:canonical: archivebox.config.constants.ConstantsDict.CONFIG_FILE
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.CONFIG_FILE
```

````

````{py:attribute} DATABASE_FILE
:canonical: archivebox.config.constants.ConstantsDict.DATABASE_FILE
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.DATABASE_FILE
```

````

````{py:attribute} QUEUE_DATABASE_FILE
:canonical: archivebox.config.constants.ConstantsDict.QUEUE_DATABASE_FILE
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.QUEUE_DATABASE_FILE
```

````

````{py:attribute} JSON_INDEX_FILENAME
:canonical: archivebox.config.constants.ConstantsDict.JSON_INDEX_FILENAME
:type: str
:value: >
   'index.json'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.JSON_INDEX_FILENAME
```

````

````{py:attribute} HTML_INDEX_FILENAME
:canonical: archivebox.config.constants.ConstantsDict.HTML_INDEX_FILENAME
:type: str
:value: >
   'index.html'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.HTML_INDEX_FILENAME
```

````

````{py:attribute} ROBOTS_TXT_FILENAME
:canonical: archivebox.config.constants.ConstantsDict.ROBOTS_TXT_FILENAME
:type: str
:value: >
   'robots.txt'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.ROBOTS_TXT_FILENAME
```

````

````{py:attribute} FAVICON_FILENAME
:canonical: archivebox.config.constants.ConstantsDict.FAVICON_FILENAME
:type: str
:value: >
   'favicon.ico'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.FAVICON_FILENAME
```

````

````{py:attribute} TMP_DIR_NAME
:canonical: archivebox.config.constants.ConstantsDict.TMP_DIR_NAME
:type: str
:value: >
   'tmp'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.TMP_DIR_NAME
```

````

````{py:attribute} DEFAULT_TMP_DIR
:canonical: archivebox.config.constants.ConstantsDict.DEFAULT_TMP_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.DEFAULT_TMP_DIR
```

````

````{py:attribute} LIB_DIR_NAME
:canonical: archivebox.config.constants.ConstantsDict.LIB_DIR_NAME
:type: str
:value: >
   'lib'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.LIB_DIR_NAME
```

````

````{py:attribute} DEFAULT_LIB_DIR
:canonical: archivebox.config.constants.ConstantsDict.DEFAULT_LIB_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.DEFAULT_LIB_DIR
```

````

````{py:attribute} TIMEZONE
:canonical: archivebox.config.constants.ConstantsDict.TIMEZONE
:type: str
:value: >
   'UTC'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.TIMEZONE
```

````

````{py:attribute} DEFAULT_CLI_COLORS
:canonical: archivebox.config.constants.ConstantsDict.DEFAULT_CLI_COLORS
:type: typing.Dict[str, str]
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.DEFAULT_CLI_COLORS
```

````

````{py:attribute} DISABLED_CLI_COLORS
:canonical: archivebox.config.constants.ConstantsDict.DISABLED_CLI_COLORS
:type: typing.Dict[str, str]
:value: >
   'benedict(...)'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.DISABLED_CLI_COLORS
```

````

````{py:attribute} ALLOWDENYLIST_REGEX_FLAGS
:canonical: archivebox.config.constants.ConstantsDict.ALLOWDENYLIST_REGEX_FLAGS
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.ALLOWDENYLIST_REGEX_FLAGS
```

````

````{py:attribute} STATICFILE_EXTENSIONS
:canonical: archivebox.config.constants.ConstantsDict.STATICFILE_EXTENSIONS
:type: frozenset[str]
:value: >
   'frozenset(...)'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.STATICFILE_EXTENSIONS
```

````

````{py:attribute} PIP_RELATED_NAMES
:canonical: archivebox.config.constants.ConstantsDict.PIP_RELATED_NAMES
:type: frozenset[str]
:value: >
   'frozenset(...)'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.PIP_RELATED_NAMES
```

````

````{py:attribute} NPM_RELATED_NAMES
:canonical: archivebox.config.constants.ConstantsDict.NPM_RELATED_NAMES
:type: frozenset[str]
:value: >
   'frozenset(...)'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.NPM_RELATED_NAMES
```

````

````{py:attribute} ALLOWED_IN_DATA_DIR
:canonical: archivebox.config.constants.ConstantsDict.ALLOWED_IN_DATA_DIR
:type: frozenset[str]
:value: >
   'frozenset(...)'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.ALLOWED_IN_DATA_DIR
```

````

````{py:method} __getitem__(key: str)
:canonical: archivebox.config.constants.ConstantsDict.__getitem__
:classmethod:

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.__getitem__
```

````

````{py:method} __benedict__()
:canonical: archivebox.config.constants.ConstantsDict.__benedict__
:classmethod:

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.__benedict__
```

````

````{py:method} __len__()
:canonical: archivebox.config.constants.ConstantsDict.__len__
:classmethod:

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.__len__
```

````

````{py:method} __iter__()
:canonical: archivebox.config.constants.ConstantsDict.__iter__
:classmethod:

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.__iter__
```

````

`````

````{py:data} CONSTANTS
:canonical: archivebox.config.constants.CONSTANTS
:value: >
   'ConstantsDict(...)'

```{autodoc2-docstring} archivebox.config.constants.CONSTANTS
```

````

````{py:data} CONSTANTS_CONFIG
:canonical: archivebox.config.constants.CONSTANTS_CONFIG
:value: >
   '__benedict__(...)'

```{autodoc2-docstring} archivebox.config.constants.CONSTANTS_CONFIG
```

````
