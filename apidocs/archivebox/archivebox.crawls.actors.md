# {py:mod}`archivebox.crawls.actors`

```{py:module} archivebox.crawls.actors
```

```{autodoc2-docstring} archivebox.crawls.actors
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CrawlActor <archivebox.crawls.actors.CrawlActor>`
  - ```{autodoc2-docstring} archivebox.crawls.actors.CrawlActor
    :summary:
    ```
````

### API

`````{py:class} CrawlActor(mode: typing.Literal[thread, process] | None = None, **launch_kwargs: actors.actor.LaunchKwargs)
:canonical: archivebox.crawls.actors.CrawlActor

Bases: {py:obj}`actors.actor.ActorType`\[{py:obj}`crawls.models.Crawl`\]

```{autodoc2-docstring} archivebox.crawls.actors.CrawlActor
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.crawls.actors.CrawlActor.__init__
```

````{py:attribute} Model
:canonical: archivebox.crawls.actors.CrawlActor.Model
:value: >
   None

```{autodoc2-docstring} archivebox.crawls.actors.CrawlActor.Model
```

````

````{py:attribute} StateMachineClass
:canonical: archivebox.crawls.actors.CrawlActor.StateMachineClass
:value: >
   None

```{autodoc2-docstring} archivebox.crawls.actors.CrawlActor.StateMachineClass
```

````

````{py:attribute} ACTIVE_STATE
:canonical: archivebox.crawls.actors.CrawlActor.ACTIVE_STATE
:type: typing.ClassVar[actors.actor.State]
:value: >
   None

```{autodoc2-docstring} archivebox.crawls.actors.CrawlActor.ACTIVE_STATE
```

````

````{py:attribute} FINAL_STATES
:canonical: archivebox.crawls.actors.CrawlActor.FINAL_STATES
:type: typing.ClassVar[list[actors.actor.State]]
:value: >
   None

```{autodoc2-docstring} archivebox.crawls.actors.CrawlActor.FINAL_STATES
```

````

````{py:attribute} STATE_FIELD_NAME
:canonical: archivebox.crawls.actors.CrawlActor.STATE_FIELD_NAME
:type: typing.ClassVar[str]
:value: >
   None

```{autodoc2-docstring} archivebox.crawls.actors.CrawlActor.STATE_FIELD_NAME
```

````

````{py:attribute} MAX_CONCURRENT_ACTORS
:canonical: archivebox.crawls.actors.CrawlActor.MAX_CONCURRENT_ACTORS
:type: typing.ClassVar[int]
:value: >
   3

```{autodoc2-docstring} archivebox.crawls.actors.CrawlActor.MAX_CONCURRENT_ACTORS
```

````

````{py:attribute} MAX_TICK_TIME
:canonical: archivebox.crawls.actors.CrawlActor.MAX_TICK_TIME
:type: typing.ClassVar[int]
:value: >
   10

```{autodoc2-docstring} archivebox.crawls.actors.CrawlActor.MAX_TICK_TIME
```

````

````{py:attribute} CLAIM_FROM_TOP_N
:canonical: archivebox.crawls.actors.CrawlActor.CLAIM_FROM_TOP_N
:type: typing.ClassVar[int]
:value: >
   None

```{autodoc2-docstring} archivebox.crawls.actors.CrawlActor.CLAIM_FROM_TOP_N
```

````

`````
