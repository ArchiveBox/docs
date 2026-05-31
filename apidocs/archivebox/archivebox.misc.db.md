# {py:mod}`archivebox.misc.db`

```{py:module} archivebox.misc.db
```

```{autodoc2-docstring} archivebox.misc.db
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`list_migrations <archivebox.misc.db.list_migrations>`
  - ```{autodoc2-docstring} archivebox.misc.db.list_migrations
    :summary:
    ```
* - {py:obj}`apply_migrations <archivebox.misc.db.apply_migrations>`
  - ```{autodoc2-docstring} archivebox.misc.db.apply_migrations
    :summary:
    ```
* - {py:obj}`get_admins <archivebox.misc.db.get_admins>`
  - ```{autodoc2-docstring} archivebox.misc.db.get_admins
    :summary:
    ```
````

### API

````{py:function} list_migrations(out_dir: pathlib.Path = DATA_DIR) -> typing.List[typing.Tuple[bool, str]]
:canonical: archivebox.misc.db.list_migrations

```{autodoc2-docstring} archivebox.misc.db.list_migrations
```
````

````{py:function} apply_migrations(out_dir: pathlib.Path = DATA_DIR) -> typing.List[str]
:canonical: archivebox.misc.db.apply_migrations

```{autodoc2-docstring} archivebox.misc.db.apply_migrations
```
````

````{py:function} get_admins(out_dir: pathlib.Path = DATA_DIR) -> typing.List
:canonical: archivebox.misc.db.get_admins

```{autodoc2-docstring} archivebox.misc.db.get_admins
```
````
