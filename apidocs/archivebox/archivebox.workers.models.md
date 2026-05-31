# {py:mod}`archivebox.workers.models`

```{py:module} archivebox.workers.models
```

```{autodoc2-docstring} archivebox.workers.models
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DefaultStatusChoices <archivebox.workers.models.DefaultStatusChoices>`
  -
* - {py:obj}`BaseModelWithStateMachine <archivebox.workers.models.BaseModelWithStateMachine>`
  -
* - {py:obj}`ModelWithStateMachine <archivebox.workers.models.ModelWithStateMachine>`
  -
* - {py:obj}`BaseStateMachine <archivebox.workers.models.BaseStateMachine>`
  - ```{autodoc2-docstring} archivebox.workers.models.BaseStateMachine
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`default_status_field <archivebox.workers.models.default_status_field>`
  - ```{autodoc2-docstring} archivebox.workers.models.default_status_field
    :summary:
    ```
* - {py:obj}`default_retry_at_field <archivebox.workers.models.default_retry_at_field>`
  - ```{autodoc2-docstring} archivebox.workers.models.default_retry_at_field
    :summary:
    ```
* - {py:obj}`ObjectState <archivebox.workers.models.ObjectState>`
  - ```{autodoc2-docstring} archivebox.workers.models.ObjectState
    :summary:
    ```
* - {py:obj}`ObjectStateList <archivebox.workers.models.ObjectStateList>`
  - ```{autodoc2-docstring} archivebox.workers.models.ObjectStateList
    :summary:
    ```
````

### API

`````{py:class} DefaultStatusChoices()
:canonical: archivebox.workers.models.DefaultStatusChoices

Bases: {py:obj}`django.db.models.TextChoices`

````{py:attribute} QUEUED
:canonical: archivebox.workers.models.DefaultStatusChoices.QUEUED
:value: >
   ('queued', 'Queued')

```{autodoc2-docstring} archivebox.workers.models.DefaultStatusChoices.QUEUED
```

````

````{py:attribute} STARTED
:canonical: archivebox.workers.models.DefaultStatusChoices.STARTED
:value: >
   ('started', 'Started')

```{autodoc2-docstring} archivebox.workers.models.DefaultStatusChoices.STARTED
```

````

````{py:attribute} SEALED
:canonical: archivebox.workers.models.DefaultStatusChoices.SEALED
:value: >
   ('sealed', 'Sealed')

```{autodoc2-docstring} archivebox.workers.models.DefaultStatusChoices.SEALED
```

````

`````

````{py:data} default_status_field
:canonical: archivebox.workers.models.default_status_field
:type: django.db.models.CharField
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.workers.models.default_status_field
```

````

````{py:data} default_retry_at_field
:canonical: archivebox.workers.models.default_retry_at_field
:type: django.db.models.DateTimeField
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.workers.models.default_retry_at_field
```

````

````{py:data} ObjectState
:canonical: archivebox.workers.models.ObjectState
:value: >
   None

```{autodoc2-docstring} archivebox.workers.models.ObjectState
```

````

````{py:data} ObjectStateList
:canonical: archivebox.workers.models.ObjectStateList
:value: >
   None

```{autodoc2-docstring} archivebox.workers.models.ObjectStateList
```

````

``````{py:class} BaseModelWithStateMachine(*args, **kwargs)
:canonical: archivebox.workers.models.BaseModelWithStateMachine

Bases: {py:obj}`django.db.models.Model`, {py:obj}`statemachine.mixins.MachineMixin`

````{py:attribute} id
:canonical: archivebox.workers.models.BaseModelWithStateMachine.id
:type: django.db.models.UUIDField
:value: >
   None

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.id
```

````

````{py:attribute} StatusChoices
:canonical: archivebox.workers.models.BaseModelWithStateMachine.StatusChoices
:type: typing.ClassVar[typing.Type[django.db.models.TextChoices]]
:value: >
   None

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.StatusChoices
```

````

````{py:attribute} state_machine_name
:canonical: archivebox.workers.models.BaseModelWithStateMachine.state_machine_name
:type: typing.ClassVar[str]
:value: >
   None

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.state_machine_name
```

````

````{py:attribute} state_field_name
:canonical: archivebox.workers.models.BaseModelWithStateMachine.state_field_name
:type: typing.ClassVar[str]
:value: >
   None

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.state_field_name
```

````

````{py:attribute} state_machine_attr
:canonical: archivebox.workers.models.BaseModelWithStateMachine.state_machine_attr
:type: typing.ClassVar[str]
:value: >
   'sm'

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.state_machine_attr
```

````

````{py:attribute} bind_events_as_methods
:canonical: archivebox.workers.models.BaseModelWithStateMachine.bind_events_as_methods
:type: typing.ClassVar[bool]
:value: >
   True

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.bind_events_as_methods
```

````

````{py:attribute} active_state
:canonical: archivebox.workers.models.BaseModelWithStateMachine.active_state
:type: typing.ClassVar[archivebox.workers.models.ObjectState]
:value: >
   None

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.active_state
```

````

````{py:attribute} retry_at_field_name
:canonical: archivebox.workers.models.BaseModelWithStateMachine.retry_at_field_name
:type: typing.ClassVar[str]
:value: >
   None

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.retry_at_field_name
```

````

`````{py:class} Meta
:canonical: archivebox.workers.models.BaseModelWithStateMachine.Meta

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.Meta
```

````{py:attribute} app_label
:canonical: archivebox.workers.models.BaseModelWithStateMachine.Meta.app_label
:value: >
   'workers'

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.Meta.app_label
```

````

````{py:attribute} abstract
:canonical: archivebox.workers.models.BaseModelWithStateMachine.Meta.abstract
:value: >
   True

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.Meta.abstract
```

````

`````

````{py:method} check(sender=None, **kwargs)
:canonical: archivebox.workers.models.BaseModelWithStateMachine.check
:classmethod:

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.check
```

````

````{py:method} _state_to_str(state: archivebox.workers.models.ObjectState) -> str
:canonical: archivebox.workers.models.BaseModelWithStateMachine._state_to_str
:staticmethod:

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine._state_to_str
```

````

````{py:property} RETRY_AT
:canonical: archivebox.workers.models.BaseModelWithStateMachine.RETRY_AT
:type: datetime.datetime

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.RETRY_AT
```

````

````{py:property} STATE
:canonical: archivebox.workers.models.BaseModelWithStateMachine.STATE
:type: str

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.STATE
```

````

````{py:method} bump_retry_at(seconds: int = 10)
:canonical: archivebox.workers.models.BaseModelWithStateMachine.bump_retry_at

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.bump_retry_at
```

````

````{py:method} update_and_requeue(**kwargs) -> bool
:canonical: archivebox.workers.models.BaseModelWithStateMachine.update_and_requeue

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.update_and_requeue
```

````

````{py:method} get_queue()
:canonical: archivebox.workers.models.BaseModelWithStateMachine.get_queue
:classmethod:

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.get_queue
```

````

````{py:method} claim_for_worker(obj: archivebox.workers.models.BaseModelWithStateMachine, lock_seconds: int = 60) -> bool
:canonical: archivebox.workers.models.BaseModelWithStateMachine.claim_for_worker
:classmethod:

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.claim_for_worker
```

````

````{py:method} ACTIVE_STATE() -> str
:canonical: archivebox.workers.models.BaseModelWithStateMachine.ACTIVE_STATE

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.ACTIVE_STATE
```

````

````{py:method} INITIAL_STATE() -> str
:canonical: archivebox.workers.models.BaseModelWithStateMachine.INITIAL_STATE

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.INITIAL_STATE
```

````

````{py:method} FINAL_STATES() -> list[str]
:canonical: archivebox.workers.models.BaseModelWithStateMachine.FINAL_STATES

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.FINAL_STATES
```

````

````{py:method} FINAL_OR_ACTIVE_STATES() -> list[str]
:canonical: archivebox.workers.models.BaseModelWithStateMachine.FINAL_OR_ACTIVE_STATES

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.FINAL_OR_ACTIVE_STATES
```

````

````{py:method} extend_choices(base_choices: typing.Type[django.db.models.TextChoices])
:canonical: archivebox.workers.models.BaseModelWithStateMachine.extend_choices
:classmethod:

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.extend_choices
```

````

````{py:method} StatusField(**kwargs) -> django.db.models.CharField
:canonical: archivebox.workers.models.BaseModelWithStateMachine.StatusField
:classmethod:

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.StatusField
```

````

````{py:method} RetryAtField(**kwargs) -> django.db.models.DateTimeField
:canonical: archivebox.workers.models.BaseModelWithStateMachine.RetryAtField
:classmethod:

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.RetryAtField
```

````

````{py:method} StateMachineClass() -> typing.Type[statemachine.StateMachine]
:canonical: archivebox.workers.models.BaseModelWithStateMachine.StateMachineClass

```{autodoc2-docstring} archivebox.workers.models.BaseModelWithStateMachine.StateMachineClass
```

````

``````

``````{py:class} ModelWithStateMachine(*args, **kwargs)
:canonical: archivebox.workers.models.ModelWithStateMachine

Bases: {py:obj}`archivebox.workers.models.BaseModelWithStateMachine`

````{py:attribute} StatusChoices
:canonical: archivebox.workers.models.ModelWithStateMachine.StatusChoices
:type: typing.ClassVar[typing.Type[archivebox.workers.models.DefaultStatusChoices]]
:value: >
   None

```{autodoc2-docstring} archivebox.workers.models.ModelWithStateMachine.StatusChoices
```

````

````{py:attribute} status
:canonical: archivebox.workers.models.ModelWithStateMachine.status
:type: django.db.models.CharField
:value: >
   'StatusField(...)'

```{autodoc2-docstring} archivebox.workers.models.ModelWithStateMachine.status
```

````

````{py:attribute} retry_at
:canonical: archivebox.workers.models.ModelWithStateMachine.retry_at
:type: django.db.models.DateTimeField
:value: >
   'RetryAtField(...)'

```{autodoc2-docstring} archivebox.workers.models.ModelWithStateMachine.retry_at
```

````

````{py:attribute} state_machine_name
:canonical: archivebox.workers.models.ModelWithStateMachine.state_machine_name
:type: typing.ClassVar[str]
:value: >
   None

```{autodoc2-docstring} archivebox.workers.models.ModelWithStateMachine.state_machine_name
```

````

````{py:attribute} state_field_name
:canonical: archivebox.workers.models.ModelWithStateMachine.state_field_name
:type: typing.ClassVar[str]
:value: >
   'status'

```{autodoc2-docstring} archivebox.workers.models.ModelWithStateMachine.state_field_name
```

````

````{py:attribute} state_machine_attr
:canonical: archivebox.workers.models.ModelWithStateMachine.state_machine_attr
:type: typing.ClassVar[str]
:value: >
   'sm'

```{autodoc2-docstring} archivebox.workers.models.ModelWithStateMachine.state_machine_attr
```

````

````{py:attribute} bind_events_as_methods
:canonical: archivebox.workers.models.ModelWithStateMachine.bind_events_as_methods
:type: typing.ClassVar[bool]
:value: >
   True

```{autodoc2-docstring} archivebox.workers.models.ModelWithStateMachine.bind_events_as_methods
```

````

````{py:attribute} active_state
:canonical: archivebox.workers.models.ModelWithStateMachine.active_state
:type: typing.ClassVar[str]
:value: >
   None

```{autodoc2-docstring} archivebox.workers.models.ModelWithStateMachine.active_state
```

````

````{py:attribute} retry_at_field_name
:canonical: archivebox.workers.models.ModelWithStateMachine.retry_at_field_name
:type: typing.ClassVar[str]
:value: >
   'retry_at'

```{autodoc2-docstring} archivebox.workers.models.ModelWithStateMachine.retry_at_field_name
```

````

`````{py:class} Meta
:canonical: archivebox.workers.models.ModelWithStateMachine.Meta

```{autodoc2-docstring} archivebox.workers.models.ModelWithStateMachine.Meta
```

````{py:attribute} app_label
:canonical: archivebox.workers.models.ModelWithStateMachine.Meta.app_label
:value: >
   'workers'

```{autodoc2-docstring} archivebox.workers.models.ModelWithStateMachine.Meta.app_label
```

````

````{py:attribute} abstract
:canonical: archivebox.workers.models.ModelWithStateMachine.Meta.abstract
:value: >
   True

```{autodoc2-docstring} archivebox.workers.models.ModelWithStateMachine.Meta.abstract
```

````

`````

``````

`````{py:class} BaseStateMachine(obj, *args, **kwargs)
:canonical: archivebox.workers.models.BaseStateMachine

Bases: {py:obj}`statemachine.StateMachine`

```{autodoc2-docstring} archivebox.workers.models.BaseStateMachine
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.workers.models.BaseStateMachine.__init__
```

````{py:attribute} model_attr_name
:canonical: archivebox.workers.models.BaseStateMachine.model_attr_name
:type: str
:value: >
   'obj'

```{autodoc2-docstring} archivebox.workers.models.BaseStateMachine.model_attr_name
```

````

````{py:method} __repr__() -> str
:canonical: archivebox.workers.models.BaseStateMachine.__repr__

````

````{py:method} __str__() -> str
:canonical: archivebox.workers.models.BaseStateMachine.__str__

````

`````
