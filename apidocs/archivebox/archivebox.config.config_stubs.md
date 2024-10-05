# {py:mod}`archivebox.config.config_stubs`

```{py:module} archivebox.config.config_stubs
```

```{autodoc2-docstring} archivebox.config.config_stubs
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseConfig <archivebox.config.config_stubs.BaseConfig>`
  -
* - {py:obj}`ConfigDict <archivebox.config.config_stubs.ConfigDict>`
  - ```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SimpleConfigValue <archivebox.config.config_stubs.SimpleConfigValue>`
  - ```{autodoc2-docstring} archivebox.config.config_stubs.SimpleConfigValue
    :summary:
    ```
* - {py:obj}`SimpleConfigValueDict <archivebox.config.config_stubs.SimpleConfigValueDict>`
  - ```{autodoc2-docstring} archivebox.config.config_stubs.SimpleConfigValueDict
    :summary:
    ```
* - {py:obj}`SimpleConfigValueGetter <archivebox.config.config_stubs.SimpleConfigValueGetter>`
  - ```{autodoc2-docstring} archivebox.config.config_stubs.SimpleConfigValueGetter
    :summary:
    ```
* - {py:obj}`ConfigValue <archivebox.config.config_stubs.ConfigValue>`
  - ```{autodoc2-docstring} archivebox.config.config_stubs.ConfigValue
    :summary:
    ```
* - {py:obj}`ConfigDefaultValueGetter <archivebox.config.config_stubs.ConfigDefaultValueGetter>`
  - ```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDefaultValueGetter
    :summary:
    ```
* - {py:obj}`ConfigDefaultValue <archivebox.config.config_stubs.ConfigDefaultValue>`
  - ```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDefaultValue
    :summary:
    ```
* - {py:obj}`ConfigDefault <archivebox.config.config_stubs.ConfigDefault>`
  - ```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDefault
    :summary:
    ```
* - {py:obj}`ConfigDefaultDict <archivebox.config.config_stubs.ConfigDefaultDict>`
  - ```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDefaultDict
    :summary:
    ```
````

### API

````{py:data} SimpleConfigValue
:canonical: archivebox.config.config_stubs.SimpleConfigValue
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.SimpleConfigValue
```

````

````{py:data} SimpleConfigValueDict
:canonical: archivebox.config.config_stubs.SimpleConfigValueDict
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.SimpleConfigValueDict
```

````

````{py:data} SimpleConfigValueGetter
:canonical: archivebox.config.config_stubs.SimpleConfigValueGetter
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.SimpleConfigValueGetter
```

````

````{py:data} ConfigValue
:canonical: archivebox.config.config_stubs.ConfigValue
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigValue
```

````

```{py:class} BaseConfig()
:canonical: archivebox.config.config_stubs.BaseConfig

Bases: {py:obj}`mypy_extensions.TypedDict`

```

`````{py:class} ConfigDict()
:canonical: archivebox.config.config_stubs.ConfigDict

Bases: {py:obj}`archivebox.config.config_stubs.BaseConfig`, {py:obj}`benedict.benedict`

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.__init__
```

````{py:attribute} IS_TTY
:canonical: archivebox.config.config_stubs.ConfigDict.IS_TTY
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.IS_TTY
```

````

````{py:attribute} USE_COLOR
:canonical: archivebox.config.config_stubs.ConfigDict.USE_COLOR
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.USE_COLOR
```

````

````{py:attribute} SHOW_PROGRESS
:canonical: archivebox.config.config_stubs.ConfigDict.SHOW_PROGRESS
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.SHOW_PROGRESS
```

````

````{py:attribute} IN_DOCKER
:canonical: archivebox.config.config_stubs.ConfigDict.IN_DOCKER
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.IN_DOCKER
```

````

````{py:attribute} PACKAGE_DIR
:canonical: archivebox.config.config_stubs.ConfigDict.PACKAGE_DIR
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.PACKAGE_DIR
```

````

````{py:attribute} CONFIG_FILE
:canonical: archivebox.config.config_stubs.ConfigDict.CONFIG_FILE
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.CONFIG_FILE
```

````

````{py:attribute} ONLY_NEW
:canonical: archivebox.config.config_stubs.ConfigDict.ONLY_NEW
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.ONLY_NEW
```

````

````{py:attribute} TIMEOUT
:canonical: archivebox.config.config_stubs.ConfigDict.TIMEOUT
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.TIMEOUT
```

````

````{py:attribute} MEDIA_TIMEOUT
:canonical: archivebox.config.config_stubs.ConfigDict.MEDIA_TIMEOUT
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.MEDIA_TIMEOUT
```

````

````{py:attribute} OUTPUT_PERMISSIONS
:canonical: archivebox.config.config_stubs.ConfigDict.OUTPUT_PERMISSIONS
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.OUTPUT_PERMISSIONS
```

````

````{py:attribute} RESTRICT_FILE_NAMES
:canonical: archivebox.config.config_stubs.ConfigDict.RESTRICT_FILE_NAMES
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.RESTRICT_FILE_NAMES
```

````

````{py:attribute} URL_DENYLIST
:canonical: archivebox.config.config_stubs.ConfigDict.URL_DENYLIST
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.URL_DENYLIST
```

````

````{py:attribute} SECRET_KEY
:canonical: archivebox.config.config_stubs.ConfigDict.SECRET_KEY
:type: typing.Optional[str]
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.SECRET_KEY
```

````

````{py:attribute} BIND_ADDR
:canonical: archivebox.config.config_stubs.ConfigDict.BIND_ADDR
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.BIND_ADDR
```

````

````{py:attribute} ALLOWED_HOSTS
:canonical: archivebox.config.config_stubs.ConfigDict.ALLOWED_HOSTS
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.ALLOWED_HOSTS
```

````

````{py:attribute} DEBUG
:canonical: archivebox.config.config_stubs.ConfigDict.DEBUG
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.DEBUG
```

````

````{py:attribute} PUBLIC_INDEX
:canonical: archivebox.config.config_stubs.ConfigDict.PUBLIC_INDEX
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.PUBLIC_INDEX
```

````

````{py:attribute} PUBLIC_SNAPSHOTS
:canonical: archivebox.config.config_stubs.ConfigDict.PUBLIC_SNAPSHOTS
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.PUBLIC_SNAPSHOTS
```

````

````{py:attribute} FOOTER_INFO
:canonical: archivebox.config.config_stubs.ConfigDict.FOOTER_INFO
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.FOOTER_INFO
```

````

````{py:attribute} SAVE_TITLE
:canonical: archivebox.config.config_stubs.ConfigDict.SAVE_TITLE
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.SAVE_TITLE
```

````

````{py:attribute} SAVE_FAVICON
:canonical: archivebox.config.config_stubs.ConfigDict.SAVE_FAVICON
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.SAVE_FAVICON
```

````

````{py:attribute} SAVE_WGET
:canonical: archivebox.config.config_stubs.ConfigDict.SAVE_WGET
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.SAVE_WGET
```

````

````{py:attribute} SAVE_WGET_REQUISITES
:canonical: archivebox.config.config_stubs.ConfigDict.SAVE_WGET_REQUISITES
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.SAVE_WGET_REQUISITES
```

````

````{py:attribute} SAVE_SINGLEFILE
:canonical: archivebox.config.config_stubs.ConfigDict.SAVE_SINGLEFILE
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.SAVE_SINGLEFILE
```

````

````{py:attribute} SAVE_READABILITY
:canonical: archivebox.config.config_stubs.ConfigDict.SAVE_READABILITY
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.SAVE_READABILITY
```

````

````{py:attribute} SAVE_MERCURY
:canonical: archivebox.config.config_stubs.ConfigDict.SAVE_MERCURY
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.SAVE_MERCURY
```

````

````{py:attribute} SAVE_PDF
:canonical: archivebox.config.config_stubs.ConfigDict.SAVE_PDF
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.SAVE_PDF
```

````

````{py:attribute} SAVE_SCREENSHOT
:canonical: archivebox.config.config_stubs.ConfigDict.SAVE_SCREENSHOT
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.SAVE_SCREENSHOT
```

````

````{py:attribute} SAVE_DOM
:canonical: archivebox.config.config_stubs.ConfigDict.SAVE_DOM
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.SAVE_DOM
```

````

````{py:attribute} SAVE_WARC
:canonical: archivebox.config.config_stubs.ConfigDict.SAVE_WARC
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.SAVE_WARC
```

````

````{py:attribute} SAVE_GIT
:canonical: archivebox.config.config_stubs.ConfigDict.SAVE_GIT
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.SAVE_GIT
```

````

````{py:attribute} SAVE_MEDIA
:canonical: archivebox.config.config_stubs.ConfigDict.SAVE_MEDIA
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.SAVE_MEDIA
```

````

````{py:attribute} SAVE_ARCHIVE_DOT_ORG
:canonical: archivebox.config.config_stubs.ConfigDict.SAVE_ARCHIVE_DOT_ORG
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.SAVE_ARCHIVE_DOT_ORG
```

````

````{py:attribute} RESOLUTION
:canonical: archivebox.config.config_stubs.ConfigDict.RESOLUTION
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.RESOLUTION
```

````

````{py:attribute} GIT_DOMAINS
:canonical: archivebox.config.config_stubs.ConfigDict.GIT_DOMAINS
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.GIT_DOMAINS
```

````

````{py:attribute} CHECK_SSL_VALIDITY
:canonical: archivebox.config.config_stubs.ConfigDict.CHECK_SSL_VALIDITY
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.CHECK_SSL_VALIDITY
```

````

````{py:attribute} CURL_USER_AGENT
:canonical: archivebox.config.config_stubs.ConfigDict.CURL_USER_AGENT
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.CURL_USER_AGENT
```

````

````{py:attribute} WGET_USER_AGENT
:canonical: archivebox.config.config_stubs.ConfigDict.WGET_USER_AGENT
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.WGET_USER_AGENT
```

````

````{py:attribute} CHROME_USER_AGENT
:canonical: archivebox.config.config_stubs.ConfigDict.CHROME_USER_AGENT
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.CHROME_USER_AGENT
```

````

````{py:attribute} COOKIES_FILE
:canonical: archivebox.config.config_stubs.ConfigDict.COOKIES_FILE
:type: typing.Union[str, pathlib.Path, None]
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.COOKIES_FILE
```

````

````{py:attribute} CHROME_USER_DATA_DIR
:canonical: archivebox.config.config_stubs.ConfigDict.CHROME_USER_DATA_DIR
:type: typing.Union[str, pathlib.Path, None]
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.CHROME_USER_DATA_DIR
```

````

````{py:attribute} CHROME_TIMEOUT
:canonical: archivebox.config.config_stubs.ConfigDict.CHROME_TIMEOUT
:type: int
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.CHROME_TIMEOUT
```

````

````{py:attribute} CHROME_HEADLESS
:canonical: archivebox.config.config_stubs.ConfigDict.CHROME_HEADLESS
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.CHROME_HEADLESS
```

````

````{py:attribute} CHROME_SANDBOX
:canonical: archivebox.config.config_stubs.ConfigDict.CHROME_SANDBOX
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.CHROME_SANDBOX
```

````

````{py:attribute} USE_CURL
:canonical: archivebox.config.config_stubs.ConfigDict.USE_CURL
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.USE_CURL
```

````

````{py:attribute} USE_WGET
:canonical: archivebox.config.config_stubs.ConfigDict.USE_WGET
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.USE_WGET
```

````

````{py:attribute} USE_SINGLEFILE
:canonical: archivebox.config.config_stubs.ConfigDict.USE_SINGLEFILE
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.USE_SINGLEFILE
```

````

````{py:attribute} USE_READABILITY
:canonical: archivebox.config.config_stubs.ConfigDict.USE_READABILITY
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.USE_READABILITY
```

````

````{py:attribute} USE_MERCURY
:canonical: archivebox.config.config_stubs.ConfigDict.USE_MERCURY
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.USE_MERCURY
```

````

````{py:attribute} USE_GIT
:canonical: archivebox.config.config_stubs.ConfigDict.USE_GIT
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.USE_GIT
```

````

````{py:attribute} USE_CHROME
:canonical: archivebox.config.config_stubs.ConfigDict.USE_CHROME
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.USE_CHROME
```

````

````{py:attribute} USE_YOUTUBEDL
:canonical: archivebox.config.config_stubs.ConfigDict.USE_YOUTUBEDL
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.USE_YOUTUBEDL
```

````

````{py:attribute} CURL_BINARY
:canonical: archivebox.config.config_stubs.ConfigDict.CURL_BINARY
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.CURL_BINARY
```

````

````{py:attribute} GIT_BINARY
:canonical: archivebox.config.config_stubs.ConfigDict.GIT_BINARY
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.GIT_BINARY
```

````

````{py:attribute} WGET_BINARY
:canonical: archivebox.config.config_stubs.ConfigDict.WGET_BINARY
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.WGET_BINARY
```

````

````{py:attribute} SINGLEFILE_BINARY
:canonical: archivebox.config.config_stubs.ConfigDict.SINGLEFILE_BINARY
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.SINGLEFILE_BINARY
```

````

````{py:attribute} READABILITY_BINARY
:canonical: archivebox.config.config_stubs.ConfigDict.READABILITY_BINARY
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.READABILITY_BINARY
```

````

````{py:attribute} MERCURY_BINARY
:canonical: archivebox.config.config_stubs.ConfigDict.MERCURY_BINARY
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.MERCURY_BINARY
```

````

````{py:attribute} YOUTUBEDL_BINARY
:canonical: archivebox.config.config_stubs.ConfigDict.YOUTUBEDL_BINARY
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.YOUTUBEDL_BINARY
```

````

````{py:attribute} CHROME_BINARY
:canonical: archivebox.config.config_stubs.ConfigDict.CHROME_BINARY
:type: typing.Optional[str]
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.CHROME_BINARY
```

````

````{py:attribute} YOUTUBEDL_ARGS
:canonical: archivebox.config.config_stubs.ConfigDict.YOUTUBEDL_ARGS
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.YOUTUBEDL_ARGS
```

````

````{py:attribute} WGET_ARGS
:canonical: archivebox.config.config_stubs.ConfigDict.WGET_ARGS
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.WGET_ARGS
```

````

````{py:attribute} CURL_ARGS
:canonical: archivebox.config.config_stubs.ConfigDict.CURL_ARGS
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.CURL_ARGS
```

````

````{py:attribute} GIT_ARGS
:canonical: archivebox.config.config_stubs.ConfigDict.GIT_ARGS
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.GIT_ARGS
```

````

````{py:attribute} TAG_SEPARATOR_PATTERN
:canonical: archivebox.config.config_stubs.ConfigDict.TAG_SEPARATOR_PATTERN
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDict.TAG_SEPARATOR_PATTERN
```

````

`````

````{py:data} ConfigDefaultValueGetter
:canonical: archivebox.config.config_stubs.ConfigDefaultValueGetter
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDefaultValueGetter
```

````

````{py:data} ConfigDefaultValue
:canonical: archivebox.config.config_stubs.ConfigDefaultValue
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDefaultValue
```

````

````{py:data} ConfigDefault
:canonical: archivebox.config.config_stubs.ConfigDefault
:value: >
   'TypedDict(...)'

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDefault
```

````

````{py:data} ConfigDefaultDict
:canonical: archivebox.config.config_stubs.ConfigDefaultDict
:value: >
   None

```{autodoc2-docstring} archivebox.config.config_stubs.ConfigDefaultDict
```

````
