# {py:mod}`archivebox.abx.archivebox.base_replayer`

```{py:module} archivebox.abx.archivebox.base_replayer
```

```{autodoc2-docstring} archivebox.abx.archivebox.base_replayer
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseReplayer <archivebox.abx.archivebox.base_replayer.BaseReplayer>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_replayer.BaseReplayer
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.abx.archivebox.base_replayer.__package__>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_replayer.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.abx.archivebox.base_replayer.__package__
:value: >
   'abx.archivebox'

```{autodoc2-docstring} archivebox.abx.archivebox.base_replayer.__package__
```

````

`````{py:class} BaseReplayer(/, **data: typing.Any)
:canonical: archivebox.abx.archivebox.base_replayer.BaseReplayer

Bases: {py:obj}`archivebox.abx.archivebox.base_hook.BaseHook`

```{autodoc2-docstring} archivebox.abx.archivebox.base_replayer.BaseReplayer
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.abx.archivebox.base_replayer.BaseReplayer.__init__
```

````{py:attribute} hook_type
:canonical: archivebox.abx.archivebox.base_replayer.BaseReplayer.hook_type
:type: archivebox.abx.archivebox.base_hook.HookType
:value: >
   'REPLAYER'

```{autodoc2-docstring} archivebox.abx.archivebox.base_replayer.BaseReplayer.hook_type
```

````

````{py:attribute} url_pattern
:canonical: archivebox.abx.archivebox.base_replayer.BaseReplayer.url_pattern
:type: str
:value: >
   '*'

```{autodoc2-docstring} archivebox.abx.archivebox.base_replayer.BaseReplayer.url_pattern
```

````

````{py:attribute} row_template
:canonical: archivebox.abx.archivebox.base_replayer.BaseReplayer.row_template
:type: str
:value: >
   'plugins/generic_replayer/templates/row.html'

```{autodoc2-docstring} archivebox.abx.archivebox.base_replayer.BaseReplayer.row_template
```

````

````{py:attribute} embed_template
:canonical: archivebox.abx.archivebox.base_replayer.BaseReplayer.embed_template
:type: str
:value: >
   'plugins/generic_replayer/templates/embed.html'

```{autodoc2-docstring} archivebox.abx.archivebox.base_replayer.BaseReplayer.embed_template
```

````

````{py:attribute} fullpage_template
:canonical: archivebox.abx.archivebox.base_replayer.BaseReplayer.fullpage_template
:type: str
:value: >
   'plugins/generic_replayer/templates/fullpage.html'

```{autodoc2-docstring} archivebox.abx.archivebox.base_replayer.BaseReplayer.fullpage_template
```

````

````{py:method} get_REPLAYERS()
:canonical: archivebox.abx.archivebox.base_replayer.BaseReplayer.get_REPLAYERS

```{autodoc2-docstring} archivebox.abx.archivebox.base_replayer.BaseReplayer.get_REPLAYERS
```

````

`````
