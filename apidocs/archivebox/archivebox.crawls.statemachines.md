# {py:mod}`archivebox.crawls.statemachines`

```{py:module} archivebox.crawls.statemachines
```

```{autodoc2-docstring} archivebox.crawls.statemachines
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CrawlMachine <archivebox.crawls.statemachines.CrawlMachine>`
  - ```{autodoc2-docstring} archivebox.crawls.statemachines.CrawlMachine
    :summary:
    ```
````

### API

`````{py:class} CrawlMachine(crawl, *args, **kwargs)
:canonical: archivebox.crawls.statemachines.CrawlMachine

Bases: {py:obj}`statemachine.StateMachine`

```{autodoc2-docstring} archivebox.crawls.statemachines.CrawlMachine
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.crawls.statemachines.CrawlMachine.__init__
```

````{py:attribute} model
:canonical: archivebox.crawls.statemachines.CrawlMachine.model
:type: crawls.models.Crawl
:value: >
   None

```{autodoc2-docstring} archivebox.crawls.statemachines.CrawlMachine.model
```

````

````{py:attribute} queued
:canonical: archivebox.crawls.statemachines.CrawlMachine.queued
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.crawls.statemachines.CrawlMachine.queued
```

````

````{py:attribute} started
:canonical: archivebox.crawls.statemachines.CrawlMachine.started
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.crawls.statemachines.CrawlMachine.started
```

````

````{py:attribute} sealed
:canonical: archivebox.crawls.statemachines.CrawlMachine.sealed
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.crawls.statemachines.CrawlMachine.sealed
```

````

````{py:attribute} tick
:canonical: archivebox.crawls.statemachines.CrawlMachine.tick
:value: >
   None

```{autodoc2-docstring} archivebox.crawls.statemachines.CrawlMachine.tick
```

````

````{py:method} can_start() -> bool
:canonical: archivebox.crawls.statemachines.CrawlMachine.can_start

```{autodoc2-docstring} archivebox.crawls.statemachines.CrawlMachine.can_start
```

````

````{py:method} is_finished() -> bool
:canonical: archivebox.crawls.statemachines.CrawlMachine.is_finished

```{autodoc2-docstring} archivebox.crawls.statemachines.CrawlMachine.is_finished
```

````

````{py:method} on_started()
:canonical: archivebox.crawls.statemachines.CrawlMachine.on_started

```{autodoc2-docstring} archivebox.crawls.statemachines.CrawlMachine.on_started
```

````

````{py:method} on_sealed()
:canonical: archivebox.crawls.statemachines.CrawlMachine.on_sealed

```{autodoc2-docstring} archivebox.crawls.statemachines.CrawlMachine.on_sealed
```

````

`````
