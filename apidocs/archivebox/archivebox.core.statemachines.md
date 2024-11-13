# {py:mod}`archivebox.core.statemachines`

```{py:module} archivebox.core.statemachines
```

```{autodoc2-docstring} archivebox.core.statemachines
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SnapshotMachine <archivebox.core.statemachines.SnapshotMachine>`
  - ```{autodoc2-docstring} archivebox.core.statemachines.SnapshotMachine
    :summary:
    ```
* - {py:obj}`ArchiveResultMachine <archivebox.core.statemachines.ArchiveResultMachine>`
  - ```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.core.statemachines.__package__>`
  - ```{autodoc2-docstring} archivebox.core.statemachines.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.core.statemachines.__package__
:value: >
   'archivebox.snapshots'

```{autodoc2-docstring} archivebox.core.statemachines.__package__
```

````

`````{py:class} SnapshotMachine(snapshot, *args, **kwargs)
:canonical: archivebox.core.statemachines.SnapshotMachine

Bases: {py:obj}`statemachine.StateMachine`

```{autodoc2-docstring} archivebox.core.statemachines.SnapshotMachine
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.core.statemachines.SnapshotMachine.__init__
```

````{py:attribute} model
:canonical: archivebox.core.statemachines.SnapshotMachine.model
:type: core.models.Snapshot
:value: >
   None

```{autodoc2-docstring} archivebox.core.statemachines.SnapshotMachine.model
```

````

````{py:attribute} queued
:canonical: archivebox.core.statemachines.SnapshotMachine.queued
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.core.statemachines.SnapshotMachine.queued
```

````

````{py:attribute} started
:canonical: archivebox.core.statemachines.SnapshotMachine.started
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.core.statemachines.SnapshotMachine.started
```

````

````{py:attribute} sealed
:canonical: archivebox.core.statemachines.SnapshotMachine.sealed
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.core.statemachines.SnapshotMachine.sealed
```

````

````{py:attribute} tick
:canonical: archivebox.core.statemachines.SnapshotMachine.tick
:value: >
   None

```{autodoc2-docstring} archivebox.core.statemachines.SnapshotMachine.tick
```

````

````{py:method} can_start() -> bool
:canonical: archivebox.core.statemachines.SnapshotMachine.can_start

```{autodoc2-docstring} archivebox.core.statemachines.SnapshotMachine.can_start
```

````

````{py:method} is_finished() -> bool
:canonical: archivebox.core.statemachines.SnapshotMachine.is_finished

```{autodoc2-docstring} archivebox.core.statemachines.SnapshotMachine.is_finished
```

````

````{py:method} on_started()
:canonical: archivebox.core.statemachines.SnapshotMachine.on_started

```{autodoc2-docstring} archivebox.core.statemachines.SnapshotMachine.on_started
```

````

````{py:method} on_sealed()
:canonical: archivebox.core.statemachines.SnapshotMachine.on_sealed

```{autodoc2-docstring} archivebox.core.statemachines.SnapshotMachine.on_sealed
```

````

`````

`````{py:class} ArchiveResultMachine(archiveresult, *args, **kwargs)
:canonical: archivebox.core.statemachines.ArchiveResultMachine

Bases: {py:obj}`statemachine.StateMachine`

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.__init__
```

````{py:attribute} model
:canonical: archivebox.core.statemachines.ArchiveResultMachine.model
:type: core.models.ArchiveResult
:value: >
   None

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.model
```

````

````{py:attribute} queued
:canonical: archivebox.core.statemachines.ArchiveResultMachine.queued
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.queued
```

````

````{py:attribute} started
:canonical: archivebox.core.statemachines.ArchiveResultMachine.started
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.started
```

````

````{py:attribute} backoff
:canonical: archivebox.core.statemachines.ArchiveResultMachine.backoff
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.backoff
```

````

````{py:attribute} succeeded
:canonical: archivebox.core.statemachines.ArchiveResultMachine.succeeded
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.succeeded
```

````

````{py:attribute} failed
:canonical: archivebox.core.statemachines.ArchiveResultMachine.failed
:value: >
   'State(...)'

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.failed
```

````

````{py:attribute} tick
:canonical: archivebox.core.statemachines.ArchiveResultMachine.tick
:value: >
   None

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.tick
```

````

````{py:method} can_start() -> bool
:canonical: archivebox.core.statemachines.ArchiveResultMachine.can_start

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.can_start
```

````

````{py:method} is_succeeded() -> bool
:canonical: archivebox.core.statemachines.ArchiveResultMachine.is_succeeded

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.is_succeeded
```

````

````{py:method} is_failed() -> bool
:canonical: archivebox.core.statemachines.ArchiveResultMachine.is_failed

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.is_failed
```

````

````{py:method} is_backoff() -> bool
:canonical: archivebox.core.statemachines.ArchiveResultMachine.is_backoff

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.is_backoff
```

````

````{py:method} is_finished() -> bool
:canonical: archivebox.core.statemachines.ArchiveResultMachine.is_finished

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.is_finished
```

````

````{py:method} on_started()
:canonical: archivebox.core.statemachines.ArchiveResultMachine.on_started

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.on_started
```

````

````{py:method} on_backoff()
:canonical: archivebox.core.statemachines.ArchiveResultMachine.on_backoff

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.on_backoff
```

````

````{py:method} on_succeeded()
:canonical: archivebox.core.statemachines.ArchiveResultMachine.on_succeeded

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.on_succeeded
```

````

````{py:method} on_failed()
:canonical: archivebox.core.statemachines.ArchiveResultMachine.on_failed

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.on_failed
```

````

````{py:method} after_transition(event: str, source: statemachine.State, target: statemachine.State)
:canonical: archivebox.core.statemachines.ArchiveResultMachine.after_transition

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.after_transition
```

````

`````
