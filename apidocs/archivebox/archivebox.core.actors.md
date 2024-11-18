# {py:mod}`archivebox.core.actors`

```{py:module} archivebox.core.actors
```

```{autodoc2-docstring} archivebox.core.actors
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SnapshotActor <archivebox.core.actors.SnapshotActor>`
  - ```{autodoc2-docstring} archivebox.core.actors.SnapshotActor
    :summary:
    ```
* - {py:obj}`ArchiveResultActor <archivebox.core.actors.ArchiveResultActor>`
  - ```{autodoc2-docstring} archivebox.core.actors.ArchiveResultActor
    :summary:
    ```
````

### API

`````{py:class} SnapshotActor(mode: typing.Literal[thread, process] | None = None, **launch_kwargs: actors.actor.LaunchKwargs)
:canonical: archivebox.core.actors.SnapshotActor

Bases: {py:obj}`actors.actor.ActorType`\[{py:obj}`core.models.Snapshot`\]

```{autodoc2-docstring} archivebox.core.actors.SnapshotActor
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.core.actors.SnapshotActor.__init__
```

````{py:attribute} Model
:canonical: archivebox.core.actors.SnapshotActor.Model
:value: >
   None

```{autodoc2-docstring} archivebox.core.actors.SnapshotActor.Model
```

````

````{py:attribute} StateMachineClass
:canonical: archivebox.core.actors.SnapshotActor.StateMachineClass
:value: >
   None

```{autodoc2-docstring} archivebox.core.actors.SnapshotActor.StateMachineClass
```

````

````{py:attribute} ACTIVE_STATE
:canonical: archivebox.core.actors.SnapshotActor.ACTIVE_STATE
:type: typing.ClassVar[statemachine.State]
:value: >
   None

```{autodoc2-docstring} archivebox.core.actors.SnapshotActor.ACTIVE_STATE
```

````

````{py:attribute} FINAL_STATES
:canonical: archivebox.core.actors.SnapshotActor.FINAL_STATES
:type: typing.ClassVar[list[statemachine.State]]
:value: >
   None

```{autodoc2-docstring} archivebox.core.actors.SnapshotActor.FINAL_STATES
```

````

````{py:attribute} STATE_FIELD_NAME
:canonical: archivebox.core.actors.SnapshotActor.STATE_FIELD_NAME
:type: typing.ClassVar[str]
:value: >
   None

```{autodoc2-docstring} archivebox.core.actors.SnapshotActor.STATE_FIELD_NAME
```

````

````{py:attribute} MAX_CONCURRENT_ACTORS
:canonical: archivebox.core.actors.SnapshotActor.MAX_CONCURRENT_ACTORS
:type: typing.ClassVar[int]
:value: >
   1

```{autodoc2-docstring} archivebox.core.actors.SnapshotActor.MAX_CONCURRENT_ACTORS
```

````

````{py:attribute} MAX_TICK_TIME
:canonical: archivebox.core.actors.SnapshotActor.MAX_TICK_TIME
:type: typing.ClassVar[int]
:value: >
   10

```{autodoc2-docstring} archivebox.core.actors.SnapshotActor.MAX_TICK_TIME
```

````

````{py:attribute} CLAIM_FROM_TOP_N
:canonical: archivebox.core.actors.SnapshotActor.CLAIM_FROM_TOP_N
:type: typing.ClassVar[int]
:value: >
   None

```{autodoc2-docstring} archivebox.core.actors.SnapshotActor.CLAIM_FROM_TOP_N
```

````

`````

`````{py:class} ArchiveResultActor(mode: typing.Literal[thread, process] | None = None, **launch_kwargs: actors.actor.LaunchKwargs)
:canonical: archivebox.core.actors.ArchiveResultActor

Bases: {py:obj}`actors.actor.ActorType`\[{py:obj}`core.models.ArchiveResult`\]

```{autodoc2-docstring} archivebox.core.actors.ArchiveResultActor
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.core.actors.ArchiveResultActor.__init__
```

````{py:attribute} Model
:canonical: archivebox.core.actors.ArchiveResultActor.Model
:value: >
   None

```{autodoc2-docstring} archivebox.core.actors.ArchiveResultActor.Model
```

````

````{py:attribute} StateMachineClass
:canonical: archivebox.core.actors.ArchiveResultActor.StateMachineClass
:value: >
   None

```{autodoc2-docstring} archivebox.core.actors.ArchiveResultActor.StateMachineClass
```

````

````{py:attribute} ACTIVE_STATE
:canonical: archivebox.core.actors.ArchiveResultActor.ACTIVE_STATE
:type: typing.ClassVar[statemachine.State]
:value: >
   None

```{autodoc2-docstring} archivebox.core.actors.ArchiveResultActor.ACTIVE_STATE
```

````

````{py:attribute} FINAL_STATES
:canonical: archivebox.core.actors.ArchiveResultActor.FINAL_STATES
:type: typing.ClassVar[list[statemachine.State]]
:value: >
   None

```{autodoc2-docstring} archivebox.core.actors.ArchiveResultActor.FINAL_STATES
```

````

````{py:attribute} STATE_FIELD_NAME
:canonical: archivebox.core.actors.ArchiveResultActor.STATE_FIELD_NAME
:type: typing.ClassVar[str]
:value: >
   None

```{autodoc2-docstring} archivebox.core.actors.ArchiveResultActor.STATE_FIELD_NAME
```

````

````{py:attribute} MAX_CONCURRENT_ACTORS
:canonical: archivebox.core.actors.ArchiveResultActor.MAX_CONCURRENT_ACTORS
:type: typing.ClassVar[int]
:value: >
   1

```{autodoc2-docstring} archivebox.core.actors.ArchiveResultActor.MAX_CONCURRENT_ACTORS
```

````

````{py:attribute} MAX_TICK_TIME
:canonical: archivebox.core.actors.ArchiveResultActor.MAX_TICK_TIME
:type: typing.ClassVar[int]
:value: >
   60

```{autodoc2-docstring} archivebox.core.actors.ArchiveResultActor.MAX_TICK_TIME
```

````

````{py:attribute} CLAIM_FROM_TOP_N
:canonical: archivebox.core.actors.ArchiveResultActor.CLAIM_FROM_TOP_N
:type: typing.ClassVar[int]
:value: >
   None

```{autodoc2-docstring} archivebox.core.actors.ArchiveResultActor.CLAIM_FROM_TOP_N
```

````

`````
