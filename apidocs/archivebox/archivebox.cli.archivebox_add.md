# {py:mod}`archivebox.cli.archivebox_add`

```{py:module} archivebox.cli.archivebox_add
```

```{autodoc2-docstring} archivebox.cli.archivebox_add
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`add <archivebox.cli.archivebox_add.add>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_add.add
    :summary:
    ```
* - {py:obj}`main <archivebox.cli.archivebox_add.main>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_add.main
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__command__ <archivebox.cli.archivebox_add.__command__>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_add.__command__
    :summary:
    ```
* - {py:obj}`ORCHESTRATOR <archivebox.cli.archivebox_add.ORCHESTRATOR>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_add.ORCHESTRATOR
    :summary:
    ```
````

### API

````{py:data} __command__
:canonical: archivebox.cli.archivebox_add.__command__
:value: >
   'archivebox add'

```{autodoc2-docstring} archivebox.cli.archivebox_add.__command__
```

````

````{py:data} ORCHESTRATOR
:canonical: archivebox.cli.archivebox_add.ORCHESTRATOR
:value: >
   None

```{autodoc2-docstring} archivebox.cli.archivebox_add.ORCHESTRATOR
```

````

````{py:function} add(urls: str | list[str], tag: str = '', depth: int = 0, update: bool = not ARCHIVING_CONFIG.ONLY_NEW, update_all: bool = False, index_only: bool = False, overwrite: bool = False, extractors: str = '', parser: str = 'auto', persona: str = 'Default', created_by_id: int | None = None) -> django.db.models.QuerySet[core.models.Snapshot]
:canonical: archivebox.cli.archivebox_add.add

```{autodoc2-docstring} archivebox.cli.archivebox_add.add
```
````

````{py:function} main(args: list[str] | None = None, stdin: typing.IO | None = None, pwd: str | None = None) -> None
:canonical: archivebox.cli.archivebox_add.main

```{autodoc2-docstring} archivebox.cli.archivebox_add.main
```
````
