# {py:mod}`archivebox.cli.archivebox_tag`

```{py:module} archivebox.cli.archivebox_tag
```

```{autodoc2-docstring} archivebox.cli.archivebox_tag
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`create_tags <archivebox.cli.archivebox_tag.create_tags>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_tag.create_tags
    :summary:
    ```
* - {py:obj}`list_tags <archivebox.cli.archivebox_tag.list_tags>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_tag.list_tags
    :summary:
    ```
* - {py:obj}`update_tags <archivebox.cli.archivebox_tag.update_tags>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_tag.update_tags
    :summary:
    ```
* - {py:obj}`delete_tags <archivebox.cli.archivebox_tag.delete_tags>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_tag.delete_tags
    :summary:
    ```
* - {py:obj}`main <archivebox.cli.archivebox_tag.main>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_tag.main
    :summary:
    ```
* - {py:obj}`create_cmd <archivebox.cli.archivebox_tag.create_cmd>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_tag.create_cmd
    :summary:
    ```
* - {py:obj}`list_cmd <archivebox.cli.archivebox_tag.list_cmd>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_tag.list_cmd
    :summary:
    ```
* - {py:obj}`update_cmd <archivebox.cli.archivebox_tag.update_cmd>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_tag.update_cmd
    :summary:
    ```
* - {py:obj}`delete_cmd <archivebox.cli.archivebox_tag.delete_cmd>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_tag.delete_cmd
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__command__ <archivebox.cli.archivebox_tag.__command__>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_tag.__command__
    :summary:
    ```
````

### API

````{py:data} __command__
:canonical: archivebox.cli.archivebox_tag.__command__
:value: >
   'archivebox tag'

```{autodoc2-docstring} archivebox.cli.archivebox_tag.__command__
```

````

````{py:function} create_tags(names: typing.Iterable[str]) -> int
:canonical: archivebox.cli.archivebox_tag.create_tags

```{autodoc2-docstring} archivebox.cli.archivebox_tag.create_tags
```
````

````{py:function} list_tags(name: typing.Optional[str] = None, name__icontains: typing.Optional[str] = None, limit: typing.Optional[int] = None) -> int
:canonical: archivebox.cli.archivebox_tag.list_tags

```{autodoc2-docstring} archivebox.cli.archivebox_tag.list_tags
```
````

````{py:function} update_tags(name: typing.Optional[str] = None) -> int
:canonical: archivebox.cli.archivebox_tag.update_tags

```{autodoc2-docstring} archivebox.cli.archivebox_tag.update_tags
```
````

````{py:function} delete_tags(yes: bool = False, dry_run: bool = False) -> int
:canonical: archivebox.cli.archivebox_tag.delete_tags

```{autodoc2-docstring} archivebox.cli.archivebox_tag.delete_tags
```
````

````{py:function} main()
:canonical: archivebox.cli.archivebox_tag.main

```{autodoc2-docstring} archivebox.cli.archivebox_tag.main
```
````

````{py:function} create_cmd(names: tuple)
:canonical: archivebox.cli.archivebox_tag.create_cmd

```{autodoc2-docstring} archivebox.cli.archivebox_tag.create_cmd
```
````

````{py:function} list_cmd(name: typing.Optional[str], name__icontains: typing.Optional[str], limit: typing.Optional[int])
:canonical: archivebox.cli.archivebox_tag.list_cmd

```{autodoc2-docstring} archivebox.cli.archivebox_tag.list_cmd
```
````

````{py:function} update_cmd(name: typing.Optional[str])
:canonical: archivebox.cli.archivebox_tag.update_cmd

```{autodoc2-docstring} archivebox.cli.archivebox_tag.update_cmd
```
````

````{py:function} delete_cmd(yes: bool, dry_run: bool)
:canonical: archivebox.cli.archivebox_tag.delete_cmd

```{autodoc2-docstring} archivebox.cli.archivebox_tag.delete_cmd
```
````
