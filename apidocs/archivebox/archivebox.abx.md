# {py:mod}`archivebox.abx`

```{py:module} archivebox.abx
```

```{autodoc2-docstring} archivebox.abx
:allowtitles:
```

## Subpackages

```{toctree}
:titlesonly:
:maxdepth: 3

archivebox.abx.pydantic_pkgr
archivebox.abx.django
archivebox.abx.archivebox
```

## Submodules

```{toctree}
:titlesonly:
:maxdepth: 1

archivebox.abx.hookspec
archivebox.abx.manager
```

## Package Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`register_hookspecs <archivebox.abx.register_hookspecs>`
  - ```{autodoc2-docstring} archivebox.abx.register_hookspecs
    :summary:
    ```
* - {py:obj}`find_plugins_in_dir <archivebox.abx.find_plugins_in_dir>`
  - ```{autodoc2-docstring} archivebox.abx.find_plugins_in_dir
    :summary:
    ```
* - {py:obj}`get_pip_installed_plugins <archivebox.abx.get_pip_installed_plugins>`
  - ```{autodoc2-docstring} archivebox.abx.get_pip_installed_plugins
    :summary:
    ```
* - {py:obj}`get_plugins_in_dirs <archivebox.abx.get_plugins_in_dirs>`
  - ```{autodoc2-docstring} archivebox.abx.get_plugins_in_dirs
    :summary:
    ```
* - {py:obj}`load_plugins <archivebox.abx.load_plugins>`
  - ```{autodoc2-docstring} archivebox.abx.load_plugins
    :summary:
    ```
* - {py:obj}`get_registered_plugins <archivebox.abx.get_registered_plugins>`
  - ```{autodoc2-docstring} archivebox.abx.get_registered_plugins
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.abx.__package__>`
  - ```{autodoc2-docstring} archivebox.abx.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.abx.__package__
:value: >
   'abx'

```{autodoc2-docstring} archivebox.abx.__package__
```

````

````{py:function} register_hookspecs(hookspecs)
:canonical: archivebox.abx.register_hookspecs

```{autodoc2-docstring} archivebox.abx.register_hookspecs
```
````

````{py:function} find_plugins_in_dir(plugins_dir: pathlib.Path, prefix: str) -> typing.Dict[str, pathlib.Path]
:canonical: archivebox.abx.find_plugins_in_dir

```{autodoc2-docstring} archivebox.abx.find_plugins_in_dir
```
````

````{py:function} get_pip_installed_plugins(group='abx')
:canonical: archivebox.abx.get_pip_installed_plugins

```{autodoc2-docstring} archivebox.abx.get_pip_installed_plugins
```
````

````{py:function} get_plugins_in_dirs(plugin_dirs: typing.Dict[str, pathlib.Path])
:canonical: archivebox.abx.get_plugins_in_dirs

```{autodoc2-docstring} archivebox.abx.get_plugins_in_dirs
```
````

````{py:function} load_plugins(plugins_dict: typing.Dict[str, pathlib.Path])
:canonical: archivebox.abx.load_plugins

```{autodoc2-docstring} archivebox.abx.load_plugins
```
````

````{py:function} get_registered_plugins()
:canonical: archivebox.abx.get_registered_plugins

```{autodoc2-docstring} archivebox.abx.get_registered_plugins
```
````
