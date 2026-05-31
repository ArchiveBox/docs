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
````

### API

````{py:data} __command__
:canonical: archivebox.cli.archivebox_add.__command__
:value: >
   'archivebox add'

```{autodoc2-docstring} archivebox.cli.archivebox_add.__command__
```

````

````{py:function} add(urls: str | list[str], depth: int | str = 0, tag: str = '', parser: str = 'auto', plugins: str = '', persona: str = 'Default', overwrite: bool = False, update: bool = not ARCHIVING_CONFIG.ONLY_NEW, index_only: bool = False, bg: bool = False, created_by_id: int | None = None) -> django.db.models.QuerySet[archivebox.core.models.Snapshot]
:canonical: archivebox.cli.archivebox_add.add

```{autodoc2-docstring} archivebox.cli.archivebox_add.add
```
````

````{py:function} main(**kwargs)
:canonical: archivebox.cli.archivebox_add.main

```{autodoc2-docstring} archivebox.cli.archivebox_add.main
```
````
