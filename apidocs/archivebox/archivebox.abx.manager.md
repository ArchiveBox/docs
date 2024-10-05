# {py:mod}`archivebox.abx.manager`

```{py:module} archivebox.abx.manager
```

```{autodoc2-docstring} archivebox.abx.manager
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PluginManager <archivebox.abx.manager.PluginManager>`
  - ```{autodoc2-docstring} archivebox.abx.manager.PluginManager
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`pm <archivebox.abx.manager.pm>`
  - ```{autodoc2-docstring} archivebox.abx.manager.pm
    :summary:
    ```
````

### API

`````{py:class} PluginManager(project_name: str)
:canonical: archivebox.abx.manager.PluginManager

Bases: {py:obj}`pluggy.PluginManager`

```{autodoc2-docstring} archivebox.abx.manager.PluginManager
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.abx.manager.PluginManager.__init__
```

````{py:method} parse_hookimpl_opts(plugin, name: str) -> pluggy.HookimplOpts | None
:canonical: archivebox.abx.manager.PluginManager.parse_hookimpl_opts

````

`````

````{py:data} pm
:canonical: archivebox.abx.manager.pm
:value: >
   'PluginManager(...)'

```{autodoc2-docstring} archivebox.abx.manager.pm
```

````
