# {py:mod}`archivebox.abx.archivebox.use`

```{py:module} archivebox.abx.archivebox.use
```

```{autodoc2-docstring} archivebox.abx.archivebox.use
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_PLUGINS <archivebox.abx.archivebox.use.get_PLUGINS>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.use.get_PLUGINS
    :summary:
    ```
* - {py:obj}`get_HOOKS <archivebox.abx.archivebox.use.get_HOOKS>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.use.get_HOOKS
    :summary:
    ```
* - {py:obj}`get_CONFIGS <archivebox.abx.archivebox.use.get_CONFIGS>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.use.get_CONFIGS
    :summary:
    ```
* - {py:obj}`get_FLAT_CONFIG <archivebox.abx.archivebox.use.get_FLAT_CONFIG>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.use.get_FLAT_CONFIG
    :summary:
    ```
* - {py:obj}`get_BINPROVIDERS <archivebox.abx.archivebox.use.get_BINPROVIDERS>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.use.get_BINPROVIDERS
    :summary:
    ```
* - {py:obj}`get_BINARIES <archivebox.abx.archivebox.use.get_BINARIES>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.use.get_BINARIES
    :summary:
    ```
* - {py:obj}`get_EXTRACTORS <archivebox.abx.archivebox.use.get_EXTRACTORS>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.use.get_EXTRACTORS
    :summary:
    ```
* - {py:obj}`get_REPLAYERS <archivebox.abx.archivebox.use.get_REPLAYERS>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.use.get_REPLAYERS
    :summary:
    ```
* - {py:obj}`get_CHECKS <archivebox.abx.archivebox.use.get_CHECKS>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.use.get_CHECKS
    :summary:
    ```
* - {py:obj}`get_ADMINDATAVIEWS <archivebox.abx.archivebox.use.get_ADMINDATAVIEWS>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.use.get_ADMINDATAVIEWS
    :summary:
    ```
* - {py:obj}`get_QUEUES <archivebox.abx.archivebox.use.get_QUEUES>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.use.get_QUEUES
    :summary:
    ```
* - {py:obj}`get_SEARCHBACKENDS <archivebox.abx.archivebox.use.get_SEARCHBACKENDS>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.use.get_SEARCHBACKENDS
    :summary:
    ```
* - {py:obj}`register_all_hooks <archivebox.abx.archivebox.use.register_all_hooks>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.use.register_all_hooks
    :summary:
    ```
* - {py:obj}`extract <archivebox.abx.archivebox.use.extract>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.use.extract
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.abx.archivebox.use.__package__>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.use.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.abx.archivebox.use.__package__
:value: >
   'abx.archivebox'

```{autodoc2-docstring} archivebox.abx.archivebox.use.__package__
```

````

````{py:function} get_PLUGINS()
:canonical: archivebox.abx.archivebox.use.get_PLUGINS

```{autodoc2-docstring} archivebox.abx.archivebox.use.get_PLUGINS
```
````

````{py:function} get_HOOKS(PLUGINS) -> typing.Dict[str, archivebox.abx.archivebox.base_hook.BaseHook]
:canonical: archivebox.abx.archivebox.use.get_HOOKS

```{autodoc2-docstring} archivebox.abx.archivebox.use.get_HOOKS
```
````

````{py:function} get_CONFIGS() -> typing.Dict[str, archivebox.abx.archivebox.base_configset.BaseConfigSet]
:canonical: archivebox.abx.archivebox.use.get_CONFIGS

```{autodoc2-docstring} archivebox.abx.archivebox.use.get_CONFIGS
```
````

````{py:function} get_FLAT_CONFIG() -> typing.Dict[str, typing.Any]
:canonical: archivebox.abx.archivebox.use.get_FLAT_CONFIG

```{autodoc2-docstring} archivebox.abx.archivebox.use.get_FLAT_CONFIG
```
````

````{py:function} get_BINPROVIDERS() -> typing.Dict[str, archivebox.abx.archivebox.base_binary.BaseBinProvider]
:canonical: archivebox.abx.archivebox.use.get_BINPROVIDERS

```{autodoc2-docstring} archivebox.abx.archivebox.use.get_BINPROVIDERS
```
````

````{py:function} get_BINARIES() -> typing.Dict[str, archivebox.abx.archivebox.base_binary.BaseBinary]
:canonical: archivebox.abx.archivebox.use.get_BINARIES

```{autodoc2-docstring} archivebox.abx.archivebox.use.get_BINARIES
```
````

````{py:function} get_EXTRACTORS() -> typing.Dict[str, archivebox.abx.archivebox.base_extractor.BaseExtractor]
:canonical: archivebox.abx.archivebox.use.get_EXTRACTORS

```{autodoc2-docstring} archivebox.abx.archivebox.use.get_EXTRACTORS
```
````

````{py:function} get_REPLAYERS() -> typing.Dict[str, archivebox.abx.archivebox.base_replayer.BaseReplayer]
:canonical: archivebox.abx.archivebox.use.get_REPLAYERS

```{autodoc2-docstring} archivebox.abx.archivebox.use.get_REPLAYERS
```
````

````{py:function} get_CHECKS() -> typing.Dict[str, archivebox.abx.archivebox.base_check.BaseCheck]
:canonical: archivebox.abx.archivebox.use.get_CHECKS

```{autodoc2-docstring} archivebox.abx.archivebox.use.get_CHECKS
```
````

````{py:function} get_ADMINDATAVIEWS() -> typing.Dict[str, archivebox.abx.archivebox.base_admindataview.BaseAdminDataView]
:canonical: archivebox.abx.archivebox.use.get_ADMINDATAVIEWS

```{autodoc2-docstring} archivebox.abx.archivebox.use.get_ADMINDATAVIEWS
```
````

````{py:function} get_QUEUES() -> typing.Dict[str, archivebox.abx.archivebox.base_queue.BaseQueue]
:canonical: archivebox.abx.archivebox.use.get_QUEUES

```{autodoc2-docstring} archivebox.abx.archivebox.use.get_QUEUES
```
````

````{py:function} get_SEARCHBACKENDS() -> typing.Dict[str, archivebox.abx.archivebox.base_searchbackend.BaseSearchBackend]
:canonical: archivebox.abx.archivebox.use.get_SEARCHBACKENDS

```{autodoc2-docstring} archivebox.abx.archivebox.use.get_SEARCHBACKENDS
```
````

````{py:function} register_all_hooks(settings)
:canonical: archivebox.abx.archivebox.use.register_all_hooks

```{autodoc2-docstring} archivebox.abx.archivebox.use.register_all_hooks
```
````

````{py:function} extract(url_or_snapshot_id)
:canonical: archivebox.abx.archivebox.use.extract

```{autodoc2-docstring} archivebox.abx.archivebox.use.extract
```
````
