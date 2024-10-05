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

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_detect_installed_version <archivebox.config.constants._detect_installed_version>`
  - ```{autodoc2-docstring} archivebox.config.constants._detect_installed_version
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.config.constants.__package__>`
  - ```{autodoc2-docstring} archivebox.config.constants.__package__
    :summary:
    ```
* - {py:obj}`PACKAGE_DIR <archivebox.config.constants.PACKAGE_DIR>`
  - ```{autodoc2-docstring} archivebox.config.constants.PACKAGE_DIR
    :summary:
    ```
* - {py:obj}`DATA_DIR <archivebox.config.constants.DATA_DIR>`
  - ```{autodoc2-docstring} archivebox.config.constants.DATA_DIR
    :summary:
    ```
* - {py:obj}`ARCHIVE_DIR <archivebox.config.constants.ARCHIVE_DIR>`
  - ```{autodoc2-docstring} archivebox.config.constants.ARCHIVE_DIR
    :summary:
    ```
* - {py:obj}`VERSION <archivebox.config.constants.VERSION>`
  - ```{autodoc2-docstring} archivebox.config.constants.VERSION
    :summary:
    ```
* - {py:obj}`DATA_DIR_TMP_DIR <archivebox.config.constants.DATA_DIR_TMP_DIR>`
  - ```{autodoc2-docstring} archivebox.config.constants.DATA_DIR_TMP_DIR
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

````{py:data} PACKAGE_DIR
:canonical: archivebox.config.constants.PACKAGE_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.PACKAGE_DIR
```

````

````{py:data} DATA_DIR
:canonical: archivebox.config.constants.DATA_DIR
:type: pathlib.Path
:value: >
   'resolve(...)'

```{autodoc2-docstring} archivebox.config.constants.DATA_DIR
```

````

````{py:data} ARCHIVE_DIR
:canonical: archivebox.config.constants.ARCHIVE_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ARCHIVE_DIR
```

````

````{py:function} _detect_installed_version(PACKAGE_DIR: pathlib.Path)
:canonical: archivebox.config.constants._detect_installed_version

```{autodoc2-docstring} archivebox.config.constants._detect_installed_version
```
````

````{py:data} VERSION
:canonical: archivebox.config.constants.VERSION
:type: str
:value: >
   '_detect_installed_version(...)'

```{autodoc2-docstring} archivebox.config.constants.VERSION
```

````

````{py:data} DATA_DIR_TMP_DIR
:canonical: archivebox.config.constants.DATA_DIR_TMP_DIR
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.DATA_DIR_TMP_DIR
```

````

`````{py:class} ConstantsDict
:canonical: archivebox.config.constants.ConstantsDict

Bases: {py:obj}`collections.abc.Mapping`

````{py:attribute} IN_DOCKER
:canonical: archivebox.config.constants.ConstantsDict.IN_DOCKER
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.IN_DOCKER
```

````

````{py:attribute} OS
:canonical: archivebox.config.constants.ConstantsDict.OS
:value: >
   'lower(...)'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.OS
```

````

````{py:attribute} ARCH
:canonical: archivebox.config.constants.ConstantsDict.ARCH
:value: >
   'lower(...)'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.ARCH
```

````

````{py:attribute} LIB_DIR_SCOPE
:canonical: archivebox.config.constants.ConstantsDict.LIB_DIR_SCOPE
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.LIB_DIR_SCOPE
```

````

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

````{py:attribute} VERSION
:canonical: archivebox.config.constants.ConstantsDict.VERSION
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.VERSION
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

````{py:attribute} STATIC_DIR
:canonical: archivebox.config.constants.ConstantsDict.STATIC_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.STATIC_DIR
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

````{py:attribute} LIB_DIR_NAME
:canonical: archivebox.config.constants.ConstantsDict.LIB_DIR_NAME
:type: str
:value: >
   'lib'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.LIB_DIR_NAME
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

````{py:attribute} SYSTEM_TMP_DIR
:canonical: archivebox.config.constants.ConstantsDict.SYSTEM_TMP_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.SYSTEM_TMP_DIR
```

````

````{py:attribute} DATA_DIR_TMP_DIR
:canonical: archivebox.config.constants.ConstantsDict.DATA_DIR_TMP_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.DATA_DIR_TMP_DIR
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

````{py:attribute} CACHE_DIR
:canonical: archivebox.config.constants.ConstantsDict.CACHE_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.CACHE_DIR
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

````{py:attribute} LIB_DIR
:canonical: archivebox.config.constants.ConstantsDict.LIB_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.LIB_DIR
```

````

````{py:attribute} TMP_DIR
:canonical: archivebox.config.constants.ConstantsDict.TMP_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.TMP_DIR
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

````{py:attribute} LIB_PIP_DIR
:canonical: archivebox.config.constants.ConstantsDict.LIB_PIP_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.LIB_PIP_DIR
```

````

````{py:attribute} LIB_NPM_DIR
:canonical: archivebox.config.constants.ConstantsDict.LIB_NPM_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.LIB_NPM_DIR
```

````

````{py:attribute} LIB_BROWSERS_DIR
:canonical: archivebox.config.constants.ConstantsDict.LIB_BROWSERS_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.LIB_BROWSERS_DIR
```

````

````{py:attribute} LIB_BIN_DIR
:canonical: archivebox.config.constants.ConstantsDict.LIB_BIN_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.LIB_BIN_DIR
```

````

````{py:attribute} BIN_DIR
:canonical: archivebox.config.constants.ConstantsDict.BIN_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.BIN_DIR
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

````{py:attribute} INGORED_PATHS
:canonical: archivebox.config.constants.ConstantsDict.INGORED_PATHS
:type: frozenset[str]
:value: >
   'frozenset(...)'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.INGORED_PATHS
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

````{py:attribute} DATA_DIR_NAMES
:canonical: archivebox.config.constants.ConstantsDict.DATA_DIR_NAMES
:type: frozenset[str]
:value: >
   'frozenset(...)'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.DATA_DIR_NAMES
```

````

````{py:attribute} DATA_DIRS
:canonical: archivebox.config.constants.ConstantsDict.DATA_DIRS
:type: frozenset[pathlib.Path]
:value: >
   'frozenset(...)'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.DATA_DIRS
```

````

````{py:attribute} DATA_FILE_NAMES
:canonical: archivebox.config.constants.ConstantsDict.DATA_FILE_NAMES
:type: frozenset[str]
:value: >
   'frozenset(...)'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.DATA_FILE_NAMES
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

````{py:attribute} CODE_LOCATIONS
:canonical: archivebox.config.constants.ConstantsDict.CODE_LOCATIONS
:value: >
   'benedict(...)'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.CODE_LOCATIONS
```

````

````{py:attribute} DATA_LOCATIONS
:canonical: archivebox.config.constants.ConstantsDict.DATA_LOCATIONS
:value: >
   'benedict(...)'

```{autodoc2-docstring} archivebox.config.constants.ConstantsDict.DATA_LOCATIONS
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
