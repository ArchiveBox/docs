# {py:mod}`archivebox.main`

```{py:module} archivebox.main
```

```{autodoc2-docstring} archivebox.main
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`help <archivebox.main.help>`
  - ```{autodoc2-docstring} archivebox.main.help
    :summary:
    ```
* - {py:obj}`version <archivebox.main.version>`
  - ```{autodoc2-docstring} archivebox.main.version
    :summary:
    ```
* - {py:obj}`run <archivebox.main.run>`
  - ```{autodoc2-docstring} archivebox.main.run
    :summary:
    ```
* - {py:obj}`init <archivebox.main.init>`
  - ```{autodoc2-docstring} archivebox.main.init
    :summary:
    ```
* - {py:obj}`status <archivebox.main.status>`
  - ```{autodoc2-docstring} archivebox.main.status
    :summary:
    ```
* - {py:obj}`oneshot <archivebox.main.oneshot>`
  - ```{autodoc2-docstring} archivebox.main.oneshot
    :summary:
    ```
* - {py:obj}`add <archivebox.main.add>`
  - ```{autodoc2-docstring} archivebox.main.add
    :summary:
    ```
* - {py:obj}`remove <archivebox.main.remove>`
  - ```{autodoc2-docstring} archivebox.main.remove
    :summary:
    ```
* - {py:obj}`update <archivebox.main.update>`
  - ```{autodoc2-docstring} archivebox.main.update
    :summary:
    ```
* - {py:obj}`list_all <archivebox.main.list_all>`
  - ```{autodoc2-docstring} archivebox.main.list_all
    :summary:
    ```
* - {py:obj}`list_links <archivebox.main.list_links>`
  - ```{autodoc2-docstring} archivebox.main.list_links
    :summary:
    ```
* - {py:obj}`list_folders <archivebox.main.list_folders>`
  - ```{autodoc2-docstring} archivebox.main.list_folders
    :summary:
    ```
* - {py:obj}`install <archivebox.main.install>`
  - ```{autodoc2-docstring} archivebox.main.install
    :summary:
    ```
* - {py:obj}`config <archivebox.main.config>`
  - ```{autodoc2-docstring} archivebox.main.config
    :summary:
    ```
* - {py:obj}`schedule <archivebox.main.schedule>`
  - ```{autodoc2-docstring} archivebox.main.schedule
    :summary:
    ```
* - {py:obj}`server <archivebox.main.server>`
  - ```{autodoc2-docstring} archivebox.main.server
    :summary:
    ```
* - {py:obj}`manage <archivebox.main.manage>`
  - ```{autodoc2-docstring} archivebox.main.manage
    :summary:
    ```
* - {py:obj}`shell <archivebox.main.shell>`
  - ```{autodoc2-docstring} archivebox.main.shell
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.main.__package__>`
  - ```{autodoc2-docstring} archivebox.main.__package__
    :summary:
    ```
* - {py:obj}`setup <archivebox.main.setup>`
  - ```{autodoc2-docstring} archivebox.main.setup
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.main.__package__
:value: >
   'archivebox'

```{autodoc2-docstring} archivebox.main.__package__
```

````

````{py:function} help(out_dir: pathlib.Path = DATA_DIR) -> None
:canonical: archivebox.main.help

```{autodoc2-docstring} archivebox.main.help
```
````

````{py:function} version(quiet: bool = False, out_dir: pathlib.Path = DATA_DIR) -> None
:canonical: archivebox.main.version

```{autodoc2-docstring} archivebox.main.version
```
````

````{py:function} run(subcommand: str, subcommand_args: typing.Optional[typing.List[str]], stdin: typing.Optional[typing.IO] = None, out_dir: pathlib.Path = DATA_DIR) -> None
:canonical: archivebox.main.run

```{autodoc2-docstring} archivebox.main.run
```
````

````{py:function} init(force: bool = False, quick: bool = False, install: bool = False, out_dir: pathlib.Path = DATA_DIR) -> None
:canonical: archivebox.main.init

```{autodoc2-docstring} archivebox.main.init
```
````

````{py:function} status(out_dir: pathlib.Path = DATA_DIR) -> None
:canonical: archivebox.main.status

```{autodoc2-docstring} archivebox.main.status
```
````

````{py:function} oneshot(url: str, extractors: str = '', out_dir: pathlib.Path = DATA_DIR, created_by_id: int | None = None) -> typing.List[archivebox.index.schema.Link]
:canonical: archivebox.main.oneshot

```{autodoc2-docstring} archivebox.main.oneshot
```
````

````{py:function} add(urls: typing.Union[str, typing.List[str]], tag: str = '', depth: int = 0, update: bool = not ARCHIVING_CONFIG.ONLY_NEW, update_all: bool = False, index_only: bool = False, overwrite: bool = False, init: bool = False, extractors: str = '', parser: str = 'auto', created_by_id: int | None = None, out_dir: pathlib.Path = DATA_DIR) -> typing.List[archivebox.index.schema.Link]
:canonical: archivebox.main.add

```{autodoc2-docstring} archivebox.main.add
```
````

````{py:function} remove(filter_str: typing.Optional[str] = None, filter_patterns: typing.Optional[typing.List[str]] = None, filter_type: str = 'exact', snapshots: typing.Optional[django.db.models.QuerySet] = None, after: typing.Optional[float] = None, before: typing.Optional[float] = None, yes: bool = False, delete: bool = False, out_dir: pathlib.Path = DATA_DIR) -> typing.List[archivebox.index.schema.Link]
:canonical: archivebox.main.remove

```{autodoc2-docstring} archivebox.main.remove
```
````

````{py:function} update(resume: typing.Optional[float] = None, only_new: bool = ARCHIVING_CONFIG.ONLY_NEW, index_only: bool = False, overwrite: bool = False, filter_patterns_str: typing.Optional[str] = None, filter_patterns: typing.Optional[typing.List[str]] = None, filter_type: typing.Optional[str] = None, status: typing.Optional[str] = None, after: typing.Optional[str] = None, before: typing.Optional[str] = None, extractors: str = '', out_dir: pathlib.Path = DATA_DIR) -> typing.List[archivebox.index.schema.Link]
:canonical: archivebox.main.update

```{autodoc2-docstring} archivebox.main.update
```
````

````{py:function} list_all(filter_patterns_str: typing.Optional[str] = None, filter_patterns: typing.Optional[typing.List[str]] = None, filter_type: str = 'exact', status: typing.Optional[str] = None, after: typing.Optional[float] = None, before: typing.Optional[float] = None, sort: typing.Optional[str] = None, csv: typing.Optional[str] = None, json: bool = False, html: bool = False, with_headers: bool = False, out_dir: pathlib.Path = DATA_DIR) -> typing.Iterable[archivebox.index.schema.Link]
:canonical: archivebox.main.list_all

```{autodoc2-docstring} archivebox.main.list_all
```
````

````{py:function} list_links(snapshots: typing.Optional[django.db.models.QuerySet] = None, filter_patterns: typing.Optional[typing.List[str]] = None, filter_type: str = 'exact', after: typing.Optional[float] = None, before: typing.Optional[float] = None, out_dir: pathlib.Path = DATA_DIR) -> typing.Iterable[archivebox.index.schema.Link]
:canonical: archivebox.main.list_links

```{autodoc2-docstring} archivebox.main.list_links
```
````

````{py:function} list_folders(links: typing.List[archivebox.index.schema.Link], status: str, out_dir: pathlib.Path = DATA_DIR) -> typing.Dict[str, typing.Optional[archivebox.index.schema.Link]]
:canonical: archivebox.main.list_folders

```{autodoc2-docstring} archivebox.main.list_folders
```
````

````{py:function} install(out_dir: pathlib.Path = DATA_DIR) -> None
:canonical: archivebox.main.install

```{autodoc2-docstring} archivebox.main.install
```
````

````{py:data} setup
:canonical: archivebox.main.setup
:value: >
   None

```{autodoc2-docstring} archivebox.main.setup
```

````

````{py:function} config(config_options_str: typing.Optional[str] = None, config_options: typing.Optional[typing.List[str]] = None, get: bool = False, set: bool = False, reset: bool = False, out_dir: pathlib.Path = DATA_DIR) -> None
:canonical: archivebox.main.config

```{autodoc2-docstring} archivebox.main.config
```
````

````{py:function} schedule(add: bool = False, show: bool = False, clear: bool = False, foreground: bool = False, run_all: bool = False, quiet: bool = False, every: typing.Optional[str] = None, tag: str = '', depth: int = 0, overwrite: bool = False, update: bool = not ARCHIVING_CONFIG.ONLY_NEW, import_path: typing.Optional[str] = None, out_dir: pathlib.Path = DATA_DIR)
:canonical: archivebox.main.schedule

```{autodoc2-docstring} archivebox.main.schedule
```
````

````{py:function} server(runserver_args: typing.Optional[typing.List[str]] = None, reload: bool = False, debug: bool = False, init: bool = False, quick_init: bool = False, createsuperuser: bool = False, daemonize: bool = False, out_dir: pathlib.Path = DATA_DIR) -> None
:canonical: archivebox.main.server

```{autodoc2-docstring} archivebox.main.server
```
````

````{py:function} manage(args: typing.Optional[typing.List[str]] = None, out_dir: pathlib.Path = DATA_DIR) -> None
:canonical: archivebox.main.manage

```{autodoc2-docstring} archivebox.main.manage
```
````

````{py:function} shell(out_dir: pathlib.Path = DATA_DIR) -> None
:canonical: archivebox.main.shell

```{autodoc2-docstring} archivebox.main.shell
```
````
