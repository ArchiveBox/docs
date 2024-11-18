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

### API

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

````{py:method} on_transition(event, state)
:canonical: archivebox.core.statemachines.SnapshotMachine.on_transition

```{autodoc2-docstring} archivebox.core.statemachines.SnapshotMachine.on_transition
```

````

````{py:method} enter_queued()
:canonical: archivebox.core.statemachines.SnapshotMachine.enter_queued

```{autodoc2-docstring} archivebox.core.statemachines.SnapshotMachine.enter_queued
```

````

````{py:method} enter_started()
:canonical: archivebox.core.statemachines.SnapshotMachine.enter_started

```{autodoc2-docstring} archivebox.core.statemachines.SnapshotMachine.enter_started
```

````

````{py:method} enter_sealed()
:canonical: archivebox.core.statemachines.SnapshotMachine.enter_sealed

```{autodoc2-docstring} archivebox.core.statemachines.SnapshotMachine.enter_sealed
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

````{py:method} enter_queued()
:canonical: archivebox.core.statemachines.ArchiveResultMachine.enter_queued

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.enter_queued
```

````

````{py:method} enter_started()
:canonical: archivebox.core.statemachines.ArchiveResultMachine.enter_started

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.enter_started
```

````

````{py:method} enter_backoff()
:canonical: archivebox.core.statemachines.ArchiveResultMachine.enter_backoff

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.enter_backoff
```

````

````{py:method} enter_succeeded()
:canonical: archivebox.core.statemachines.ArchiveResultMachine.enter_succeeded

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.enter_succeeded
```

````

````{py:method} enter_failed()
:canonical: archivebox.core.statemachines.ArchiveResultMachine.enter_failed

```{autodoc2-docstring} archivebox.core.statemachines.ArchiveResultMachine.enter_failed
```

````

`````
