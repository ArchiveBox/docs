# {py:mod}`abx_plugin_singlefile.actors`

```{py:module} abx_plugin_singlefile.actors
```

```{autodoc2-docstring} abx_plugin_singlefile.actors
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SinglefileActor <abx_plugin_singlefile.actors.SinglefileActor>`
  - ```{autodoc2-docstring} abx_plugin_singlefile.actors.SinglefileActor
    :summary:
    ```
````

### API

`````{py:class} SinglefileActor
:canonical: abx_plugin_singlefile.actors.SinglefileActor

Bases: {py:obj}`actors.actor.ActorType`\[{py:obj}`abx_plugin_singlefile.models.SinglefileResult`\]

```{autodoc2-docstring} abx_plugin_singlefile.actors.SinglefileActor
```

````{py:attribute} CLAIM_ORDER
:canonical: abx_plugin_singlefile.actors.SinglefileActor.CLAIM_ORDER
:type: typing.ClassVar[str]
:value: >
   'created_at DESC'

```{autodoc2-docstring} abx_plugin_singlefile.actors.SinglefileActor.CLAIM_ORDER
```

````

````{py:attribute} CLAIM_WHERE
:canonical: abx_plugin_singlefile.actors.SinglefileActor.CLAIM_WHERE
:type: typing.ClassVar[str]
:value: >
   'status = "queued" AND extractor = "favicon"'

```{autodoc2-docstring} abx_plugin_singlefile.actors.SinglefileActor.CLAIM_WHERE
```

````

````{py:attribute} CLAIM_SET
:canonical: abx_plugin_singlefile.actors.SinglefileActor.CLAIM_SET
:type: typing.ClassVar[str]
:value: >
   'status = "started"'

```{autodoc2-docstring} abx_plugin_singlefile.actors.SinglefileActor.CLAIM_SET
```

````

````{py:method} QUERYSET() -> django.db.models.QuerySet
:canonical: abx_plugin_singlefile.actors.SinglefileActor.QUERYSET

```{autodoc2-docstring} abx_plugin_singlefile.actors.SinglefileActor.QUERYSET
```

````

````{py:method} tick(obj: abx_plugin_singlefile.models.SinglefileResult)
:canonical: abx_plugin_singlefile.actors.SinglefileActor.tick

```{autodoc2-docstring} abx_plugin_singlefile.actors.SinglefileActor.tick
```

````

`````
