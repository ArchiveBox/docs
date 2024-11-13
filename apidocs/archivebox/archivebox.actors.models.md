# {py:mod}`archivebox.actors.models`

```{py:module} archivebox.actors.models
```

```{autodoc2-docstring} archivebox.actors.models
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DefaultStatusChoices <archivebox.actors.models.DefaultStatusChoices>`
  -
* - {py:obj}`BaseModelWithStateMachine <archivebox.actors.models.BaseModelWithStateMachine>`
  -
* - {py:obj}`ModelWithStateMachine <archivebox.actors.models.ModelWithStateMachine>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`default_status_field <archivebox.actors.models.default_status_field>`
  - ```{autodoc2-docstring} archivebox.actors.models.default_status_field
    :summary:
    ```
* - {py:obj}`default_retry_at_field <archivebox.actors.models.default_retry_at_field>`
  - ```{autodoc2-docstring} archivebox.actors.models.default_retry_at_field
    :summary:
    ```
* - {py:obj}`ObjectState <archivebox.actors.models.ObjectState>`
  - ```{autodoc2-docstring} archivebox.actors.models.ObjectState
    :summary:
    ```
* - {py:obj}`ObjectStateList <archivebox.actors.models.ObjectStateList>`
  - ```{autodoc2-docstring} archivebox.actors.models.ObjectStateList
    :summary:
    ```
````

### API

`````{py:class} DefaultStatusChoices(*args, **kwds)
:canonical: archivebox.actors.models.DefaultStatusChoices

Bases: {py:obj}`django.db.models.TextChoices`

````{py:attribute} QUEUED
:canonical: archivebox.actors.models.DefaultStatusChoices.QUEUED
:value: >
   ('queued', 'Queued')

```{autodoc2-docstring} archivebox.actors.models.DefaultStatusChoices.QUEUED
```

````

````{py:attribute} STARTED
:canonical: archivebox.actors.models.DefaultStatusChoices.STARTED
:value: >
   ('started', 'Started')

```{autodoc2-docstring} archivebox.actors.models.DefaultStatusChoices.STARTED
```

````

````{py:attribute} SEALED
:canonical: archivebox.actors.models.DefaultStatusChoices.SEALED
:value: >
   ('sealed', 'Sealed')

```{autodoc2-docstring} archivebox.actors.models.DefaultStatusChoices.SEALED
```

````

`````

````{py:data} default_status_field
:canonical: archivebox.actors.models.default_status_field
:type: django.db.models.CharField
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.actors.models.default_status_field
```

````

````{py:data} default_retry_at_field
:canonical: archivebox.actors.models.default_retry_at_field
:type: django.db.models.DateTimeField
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.actors.models.default_retry_at_field
```

````

````{py:data} ObjectState
:canonical: archivebox.actors.models.ObjectState
:value: >
   None

```{autodoc2-docstring} archivebox.actors.models.ObjectState
```

````

````{py:data} ObjectStateList
:canonical: archivebox.actors.models.ObjectStateList
:value: >
   None

```{autodoc2-docstring} archivebox.actors.models.ObjectStateList
```

````

``````{py:class} BaseModelWithStateMachine(*args, **kwargs)
:canonical: archivebox.actors.models.BaseModelWithStateMachine

Bases: {py:obj}`django.db.models.Model`, {py:obj}`statemachine.mixins.MachineMixin`

````{py:attribute} id
:canonical: archivebox.actors.models.BaseModelWithStateMachine.id
:type: django.db.models.UUIDField
:value: >
   None

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine.id
```

````

````{py:attribute} StatusChoices
:canonical: archivebox.actors.models.BaseModelWithStateMachine.StatusChoices
:type: typing.ClassVar[typing.Type[django.db.models.TextChoices]]
:value: >
   None

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine.StatusChoices
```

````

````{py:attribute} state_machine_name
:canonical: archivebox.actors.models.BaseModelWithStateMachine.state_machine_name
:type: typing.ClassVar[str]
:value: >
   None

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine.state_machine_name
```

````

````{py:attribute} state_field_name
:canonical: archivebox.actors.models.BaseModelWithStateMachine.state_field_name
:type: typing.ClassVar[str]
:value: >
   None

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine.state_field_name
```

````

````{py:attribute} state_machine_attr
:canonical: archivebox.actors.models.BaseModelWithStateMachine.state_machine_attr
:type: typing.ClassVar[str]
:value: >
   'sm'

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine.state_machine_attr
```

````

````{py:attribute} bind_events_as_methods
:canonical: archivebox.actors.models.BaseModelWithStateMachine.bind_events_as_methods
:type: typing.ClassVar[bool]
:value: >
   True

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine.bind_events_as_methods
```

````

````{py:attribute} active_state
:canonical: archivebox.actors.models.BaseModelWithStateMachine.active_state
:type: typing.ClassVar[archivebox.actors.models.ObjectState]
:value: >
   None

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine.active_state
```

````

````{py:attribute} retry_at_field_name
:canonical: archivebox.actors.models.BaseModelWithStateMachine.retry_at_field_name
:type: typing.ClassVar[str]
:value: >
   None

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine.retry_at_field_name
```

````

`````{py:class} Meta
:canonical: archivebox.actors.models.BaseModelWithStateMachine.Meta

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine.Meta
```

````{py:attribute} abstract
:canonical: archivebox.actors.models.BaseModelWithStateMachine.Meta.abstract
:value: >
   True

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine.Meta.abstract
```

````

`````

````{py:method} check(sender=None, **kwargs)
:canonical: archivebox.actors.models.BaseModelWithStateMachine.check
:classmethod:

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine.check
```

````

````{py:method} _state_to_str(state: archivebox.actors.models.ObjectState) -> str
:canonical: archivebox.actors.models.BaseModelWithStateMachine._state_to_str
:staticmethod:

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine._state_to_str
```

````

````{py:property} RETRY_AT
:canonical: archivebox.actors.models.BaseModelWithStateMachine.RETRY_AT
:type: datetime.datetime

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine.RETRY_AT
```

````

````{py:property} STATE
:canonical: archivebox.actors.models.BaseModelWithStateMachine.STATE
:type: str

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine.STATE
```

````

````{py:method} bump_retry_at(seconds: int = 10)
:canonical: archivebox.actors.models.BaseModelWithStateMachine.bump_retry_at

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine.bump_retry_at
```

````

````{py:method} ACTIVE_STATE() -> str
:canonical: archivebox.actors.models.BaseModelWithStateMachine.ACTIVE_STATE

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine.ACTIVE_STATE
```

````

````{py:method} INITIAL_STATE() -> str
:canonical: archivebox.actors.models.BaseModelWithStateMachine.INITIAL_STATE

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine.INITIAL_STATE
```

````

````{py:method} FINAL_STATES() -> list[str]
:canonical: archivebox.actors.models.BaseModelWithStateMachine.FINAL_STATES

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine.FINAL_STATES
```

````

````{py:method} FINAL_OR_ACTIVE_STATES() -> list[str]
:canonical: archivebox.actors.models.BaseModelWithStateMachine.FINAL_OR_ACTIVE_STATES

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine.FINAL_OR_ACTIVE_STATES
```

````

````{py:method} extend_choices(base_choices: typing.Type[django.db.models.TextChoices])
:canonical: archivebox.actors.models.BaseModelWithStateMachine.extend_choices
:classmethod:

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine.extend_choices
```

````

````{py:method} StatusField(**kwargs) -> django.db.models.CharField
:canonical: archivebox.actors.models.BaseModelWithStateMachine.StatusField
:classmethod:

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine.StatusField
```

````

````{py:method} RetryAtField(**kwargs) -> django.db.models.DateTimeField
:canonical: archivebox.actors.models.BaseModelWithStateMachine.RetryAtField
:classmethod:

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine.RetryAtField
```

````

````{py:method} StateMachineClass() -> typing.Type[statemachine.StateMachine]
:canonical: archivebox.actors.models.BaseModelWithStateMachine.StateMachineClass

```{autodoc2-docstring} archivebox.actors.models.BaseModelWithStateMachine.StateMachineClass
```

````

``````

``````{py:class} ModelWithStateMachine(*args, **kwargs)
:canonical: archivebox.actors.models.ModelWithStateMachine

Bases: {py:obj}`archivebox.actors.models.BaseModelWithStateMachine`

````{py:attribute} StatusChoices
:canonical: archivebox.actors.models.ModelWithStateMachine.StatusChoices
:type: typing.ClassVar[typing.Type[archivebox.actors.models.DefaultStatusChoices]]
:value: >
   None

```{autodoc2-docstring} archivebox.actors.models.ModelWithStateMachine.StatusChoices
```

````

````{py:attribute} status
:canonical: archivebox.actors.models.ModelWithStateMachine.status
:type: django.db.models.CharField
:value: >
   'StatusField(...)'

```{autodoc2-docstring} archivebox.actors.models.ModelWithStateMachine.status
```

````

````{py:attribute} retry_at
:canonical: archivebox.actors.models.ModelWithStateMachine.retry_at
:type: django.db.models.DateTimeField
:value: >
   'RetryAtField(...)'

```{autodoc2-docstring} archivebox.actors.models.ModelWithStateMachine.retry_at
```

````

````{py:attribute} state_machine_name
:canonical: archivebox.actors.models.ModelWithStateMachine.state_machine_name
:type: typing.ClassVar[str]
:value: >
   None

```{autodoc2-docstring} archivebox.actors.models.ModelWithStateMachine.state_machine_name
```

````

````{py:attribute} state_field_name
:canonical: archivebox.actors.models.ModelWithStateMachine.state_field_name
:type: typing.ClassVar[str]
:value: >
   'status'

```{autodoc2-docstring} archivebox.actors.models.ModelWithStateMachine.state_field_name
```

````

````{py:attribute} state_machine_attr
:canonical: archivebox.actors.models.ModelWithStateMachine.state_machine_attr
:type: typing.ClassVar[str]
:value: >
   'sm'

```{autodoc2-docstring} archivebox.actors.models.ModelWithStateMachine.state_machine_attr
```

````

````{py:attribute} bind_events_as_methods
:canonical: archivebox.actors.models.ModelWithStateMachine.bind_events_as_methods
:type: typing.ClassVar[bool]
:value: >
   True

```{autodoc2-docstring} archivebox.actors.models.ModelWithStateMachine.bind_events_as_methods
```

````

````{py:attribute} active_state
:canonical: archivebox.actors.models.ModelWithStateMachine.active_state
:type: typing.ClassVar[str]
:value: >
   None

```{autodoc2-docstring} archivebox.actors.models.ModelWithStateMachine.active_state
```

````

````{py:attribute} retry_at_field_name
:canonical: archivebox.actors.models.ModelWithStateMachine.retry_at_field_name
:type: typing.ClassVar[str]
:value: >
   'retry_at'

```{autodoc2-docstring} archivebox.actors.models.ModelWithStateMachine.retry_at_field_name
```

````

`````{py:class} Meta
:canonical: archivebox.actors.models.ModelWithStateMachine.Meta

```{autodoc2-docstring} archivebox.actors.models.ModelWithStateMachine.Meta
```

````{py:attribute} abstract
:canonical: archivebox.actors.models.ModelWithStateMachine.Meta.abstract
:value: >
   True

```{autodoc2-docstring} archivebox.actors.models.ModelWithStateMachine.Meta.abstract
```

````

`````

``````
