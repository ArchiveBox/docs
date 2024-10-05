# {py:mod}`archivebox.index.sql`

```{py:module} archivebox.index.sql
```

```{autodoc2-docstring} archivebox.index.sql
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`parse_sql_main_index <archivebox.index.sql.parse_sql_main_index>`
  - ```{autodoc2-docstring} archivebox.index.sql.parse_sql_main_index
    :summary:
    ```
* - {py:obj}`remove_from_sql_main_index <archivebox.index.sql.remove_from_sql_main_index>`
  - ```{autodoc2-docstring} archivebox.index.sql.remove_from_sql_main_index
    :summary:
    ```
* - {py:obj}`write_link_to_sql_index <archivebox.index.sql.write_link_to_sql_index>`
  - ```{autodoc2-docstring} archivebox.index.sql.write_link_to_sql_index
    :summary:
    ```
* - {py:obj}`write_sql_main_index <archivebox.index.sql.write_sql_main_index>`
  - ```{autodoc2-docstring} archivebox.index.sql.write_sql_main_index
    :summary:
    ```
* - {py:obj}`write_sql_link_details <archivebox.index.sql.write_sql_link_details>`
  - ```{autodoc2-docstring} archivebox.index.sql.write_sql_link_details
    :summary:
    ```
* - {py:obj}`list_migrations <archivebox.index.sql.list_migrations>`
  - ```{autodoc2-docstring} archivebox.index.sql.list_migrations
    :summary:
    ```
* - {py:obj}`apply_migrations <archivebox.index.sql.apply_migrations>`
  - ```{autodoc2-docstring} archivebox.index.sql.apply_migrations
    :summary:
    ```
* - {py:obj}`get_admins <archivebox.index.sql.get_admins>`
  - ```{autodoc2-docstring} archivebox.index.sql.get_admins
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.index.sql.__package__>`
  - ```{autodoc2-docstring} archivebox.index.sql.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.index.sql.__package__
:value: >
   'archivebox.index'

```{autodoc2-docstring} archivebox.index.sql.__package__
```

````

````{py:function} parse_sql_main_index(out_dir: pathlib.Path = DATA_DIR) -> typing.Iterator[archivebox.index.schema.Link]
:canonical: archivebox.index.sql.parse_sql_main_index

```{autodoc2-docstring} archivebox.index.sql.parse_sql_main_index
```
````

````{py:function} remove_from_sql_main_index(snapshots: django.db.models.QuerySet, atomic: bool = False, out_dir: pathlib.Path = DATA_DIR) -> None
:canonical: archivebox.index.sql.remove_from_sql_main_index

```{autodoc2-docstring} archivebox.index.sql.remove_from_sql_main_index
```
````

````{py:function} write_link_to_sql_index(link: archivebox.index.schema.Link, created_by_id: int | None = None)
:canonical: archivebox.index.sql.write_link_to_sql_index

```{autodoc2-docstring} archivebox.index.sql.write_link_to_sql_index
```
````

````{py:function} write_sql_main_index(links: typing.List[archivebox.index.schema.Link], out_dir: pathlib.Path = DATA_DIR, created_by_id: int | None = None) -> None
:canonical: archivebox.index.sql.write_sql_main_index

```{autodoc2-docstring} archivebox.index.sql.write_sql_main_index
```
````

````{py:function} write_sql_link_details(link: archivebox.index.schema.Link, out_dir: pathlib.Path = DATA_DIR, created_by_id: int | None = None) -> None
:canonical: archivebox.index.sql.write_sql_link_details

```{autodoc2-docstring} archivebox.index.sql.write_sql_link_details
```
````

````{py:function} list_migrations(out_dir: pathlib.Path = DATA_DIR) -> typing.List[typing.Tuple[bool, str]]
:canonical: archivebox.index.sql.list_migrations

```{autodoc2-docstring} archivebox.index.sql.list_migrations
```
````

````{py:function} apply_migrations(out_dir: pathlib.Path = DATA_DIR) -> typing.List[str]
:canonical: archivebox.index.sql.apply_migrations

```{autodoc2-docstring} archivebox.index.sql.apply_migrations
```
````

````{py:function} get_admins(out_dir: pathlib.Path = DATA_DIR) -> typing.List[str]
:canonical: archivebox.index.sql.get_admins

```{autodoc2-docstring} archivebox.index.sql.get_admins
```
````
