# {py:mod}`archivebox.abid_utils.models`

```{py:module} archivebox.abid_utils.models
```

```{autodoc2-docstring} archivebox.abid_utils.models
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AutoDateTimeField <archivebox.abid_utils.models.AutoDateTimeField>`
  -
* - {py:obj}`ABIDModel <archivebox.abid_utils.models.ABIDModel>`
  - ```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel
    :summary:
    ```
* - {py:obj}`ModelWithHealthStats <archivebox.abid_utils.models.ModelWithHealthStats>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_or_create_system_user_pk <archivebox.abid_utils.models.get_or_create_system_user_pk>`
  - ```{autodoc2-docstring} archivebox.abid_utils.models.get_or_create_system_user_pk
    :summary:
    ```
* - {py:obj}`find_all_abid_prefixes <archivebox.abid_utils.models.find_all_abid_prefixes>`
  - ```{autodoc2-docstring} archivebox.abid_utils.models.find_all_abid_prefixes
    :summary:
    ```
* - {py:obj}`find_prefix_for_abid <archivebox.abid_utils.models.find_prefix_for_abid>`
  - ```{autodoc2-docstring} archivebox.abid_utils.models.find_prefix_for_abid
    :summary:
    ```
* - {py:obj}`find_model_from_abid_prefix <archivebox.abid_utils.models.find_model_from_abid_prefix>`
  - ```{autodoc2-docstring} archivebox.abid_utils.models.find_model_from_abid_prefix
    :summary:
    ```
* - {py:obj}`find_model_from_abid <archivebox.abid_utils.models.find_model_from_abid>`
  - ```{autodoc2-docstring} archivebox.abid_utils.models.find_model_from_abid
    :summary:
    ```
* - {py:obj}`find_obj_from_abid_rand <archivebox.abid_utils.models.find_obj_from_abid_rand>`
  - ```{autodoc2-docstring} archivebox.abid_utils.models.find_obj_from_abid_rand
    :summary:
    ```
* - {py:obj}`find_obj_from_abid <archivebox.abid_utils.models.find_obj_from_abid>`
  - ```{autodoc2-docstring} archivebox.abid_utils.models.find_obj_from_abid
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ABIDField <archivebox.abid_utils.models.ABIDField>`
  - ```{autodoc2-docstring} archivebox.abid_utils.models.ABIDField
    :summary:
    ```
````

### API

````{py:data} ABIDField
:canonical: archivebox.abid_utils.models.ABIDField
:value: >
   'partial(...)'

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDField
```

````

````{py:function} get_or_create_system_user_pk(username='system')
:canonical: archivebox.abid_utils.models.get_or_create_system_user_pk

```{autodoc2-docstring} archivebox.abid_utils.models.get_or_create_system_user_pk
```
````

```{py:class} AutoDateTimeField(verbose_name=None, name=None, auto_now=False, auto_now_add=False, **kwargs)
:canonical: archivebox.abid_utils.models.AutoDateTimeField

Bases: {py:obj}`django.db.models.DateTimeField`

```

```{py:exception} ABIDError()
:canonical: archivebox.abid_utils.models.ABIDError

Bases: {py:obj}`Exception`

```

``````{py:class} ABIDModel(*args: typing.Any, **kwargs: typing.Any)
:canonical: archivebox.abid_utils.models.ABIDModel

Bases: {py:obj}`django.db.models.Model`

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel.__init__
```

````{py:attribute} abid_prefix
:canonical: archivebox.abid_utils.models.ABIDModel.abid_prefix
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel.abid_prefix
```

````

````{py:attribute} abid_ts_src
:canonical: archivebox.abid_utils.models.ABIDModel.abid_ts_src
:value: >
   'self.created_at'

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel.abid_ts_src
```

````

````{py:attribute} abid_uri_src
:canonical: archivebox.abid_utils.models.ABIDModel.abid_uri_src
:value: >
   'None'

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel.abid_uri_src
```

````

````{py:attribute} abid_subtype_src
:canonical: archivebox.abid_utils.models.ABIDModel.abid_subtype_src
:value: >
   'self.__class__.__name__'

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel.abid_subtype_src
```

````

````{py:attribute} abid_rand_src
:canonical: archivebox.abid_utils.models.ABIDModel.abid_rand_src
:value: >
   'self.id'

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel.abid_rand_src
```

````

````{py:attribute} abid_salt
:canonical: archivebox.abid_utils.models.ABIDModel.abid_salt
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel.abid_salt
```

````

````{py:attribute} abid_drift_allowed
:canonical: archivebox.abid_utils.models.ABIDModel.abid_drift_allowed
:type: bool
:value: >
   False

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel.abid_drift_allowed
```

````

````{py:attribute} _prefetched_objects_cache
:canonical: archivebox.abid_utils.models.ABIDModel._prefetched_objects_cache
:type: typing.Dict[str, typing.Any]
:value: >
   None

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel._prefetched_objects_cache
```

````

`````{py:class} Meta
:canonical: archivebox.abid_utils.models.ABIDModel.Meta

Bases: {py:obj}`django_stubs_ext.db.models.TypedModelMeta`

````{py:attribute} abstract
:canonical: archivebox.abid_utils.models.ABIDModel.Meta.abstract
:value: >
   True

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel.Meta.abstract
```

````

`````

````{py:method} __str__() -> str
:canonical: archivebox.abid_utils.models.ABIDModel.__str__

````

````{py:method} clean(abid_drift_allowed: bool | None = None) -> None
:canonical: archivebox.abid_utils.models.ABIDModel.clean

````

````{py:method} save(*args: typing.Any, abid_drift_allowed: bool | None = None, **kwargs: typing.Any) -> None
:canonical: archivebox.abid_utils.models.ABIDModel.save

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel.save
```

````

````{py:method} id_from_abid(abid: str) -> str
:canonical: archivebox.abid_utils.models.ABIDModel.id_from_abid
:classmethod:

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel.id_from_abid
```

````

````{py:property} ABID_SOURCES
:canonical: archivebox.abid_utils.models.ABIDModel.ABID_SOURCES
:type: typing.Dict[str, str]

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel.ABID_SOURCES
```

````

````{py:property} ABID_FRESH_VALUES
:canonical: archivebox.abid_utils.models.ABIDModel.ABID_FRESH_VALUES
:type: typing.Dict[str, typing.Any]

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel.ABID_FRESH_VALUES
```

````

````{py:property} ABID_FRESH_HASHES
:canonical: archivebox.abid_utils.models.ABIDModel.ABID_FRESH_HASHES
:type: typing.Dict[str, str]

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel.ABID_FRESH_HASHES
```

````

````{py:property} ABID_FRESH_DIFFS
:canonical: archivebox.abid_utils.models.ABIDModel.ABID_FRESH_DIFFS
:type: typing.Dict[str, typing.Dict[str, typing.Any]]

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel.ABID_FRESH_DIFFS
```

````

````{py:method} issue_new_abid(overwrite=False) -> archivebox.abid_utils.abid.ABID
:canonical: archivebox.abid_utils.models.ABIDModel.issue_new_abid

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel.issue_new_abid
```

````

````{py:property} ABID
:canonical: archivebox.abid_utils.models.ABIDModel.ABID
:type: archivebox.abid_utils.abid.ABID

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel.ABID
```

````

````{py:property} api_url
:canonical: archivebox.abid_utils.models.ABIDModel.api_url
:type: str

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel.api_url
```

````

````{py:property} api_docs_url
:canonical: archivebox.abid_utils.models.ABIDModel.api_docs_url
:type: str

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel.api_docs_url
```

````

````{py:property} admin_change_url
:canonical: archivebox.abid_utils.models.ABIDModel.admin_change_url
:type: str

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel.admin_change_url
```

````

````{py:method} get_absolute_url()
:canonical: archivebox.abid_utils.models.ABIDModel.get_absolute_url

```{autodoc2-docstring} archivebox.abid_utils.models.ABIDModel.get_absolute_url
```

````

``````

``````{py:class} ModelWithHealthStats(*args, **kwargs)
:canonical: archivebox.abid_utils.models.ModelWithHealthStats

Bases: {py:obj}`django.db.models.Model`

````{py:attribute} num_uses_failed
:canonical: archivebox.abid_utils.models.ModelWithHealthStats.num_uses_failed
:value: >
   'PositiveIntegerField(...)'

```{autodoc2-docstring} archivebox.abid_utils.models.ModelWithHealthStats.num_uses_failed
```

````

````{py:attribute} num_uses_succeeded
:canonical: archivebox.abid_utils.models.ModelWithHealthStats.num_uses_succeeded
:value: >
   'PositiveIntegerField(...)'

```{autodoc2-docstring} archivebox.abid_utils.models.ModelWithHealthStats.num_uses_succeeded
```

````

`````{py:class} Meta
:canonical: archivebox.abid_utils.models.ModelWithHealthStats.Meta

```{autodoc2-docstring} archivebox.abid_utils.models.ModelWithHealthStats.Meta
```

````{py:attribute} abstract
:canonical: archivebox.abid_utils.models.ModelWithHealthStats.Meta.abstract
:value: >
   True

```{autodoc2-docstring} archivebox.abid_utils.models.ModelWithHealthStats.Meta.abstract
```

````

`````

````{py:method} record_health_failure() -> None
:canonical: archivebox.abid_utils.models.ModelWithHealthStats.record_health_failure

```{autodoc2-docstring} archivebox.abid_utils.models.ModelWithHealthStats.record_health_failure
```

````

````{py:method} record_health_success() -> None
:canonical: archivebox.abid_utils.models.ModelWithHealthStats.record_health_success

```{autodoc2-docstring} archivebox.abid_utils.models.ModelWithHealthStats.record_health_success
```

````

````{py:method} reset_health() -> None
:canonical: archivebox.abid_utils.models.ModelWithHealthStats.reset_health

```{autodoc2-docstring} archivebox.abid_utils.models.ModelWithHealthStats.reset_health
```

````

````{py:property} health
:canonical: archivebox.abid_utils.models.ModelWithHealthStats.health
:type: int

```{autodoc2-docstring} archivebox.abid_utils.models.ModelWithHealthStats.health
```

````

``````

````{py:function} find_all_abid_prefixes() -> typing.Dict[str, type[django.db.models.Model]]
:canonical: archivebox.abid_utils.models.find_all_abid_prefixes

```{autodoc2-docstring} archivebox.abid_utils.models.find_all_abid_prefixes
```
````

````{py:function} find_prefix_for_abid(abid: archivebox.abid_utils.abid.ABID) -> str
:canonical: archivebox.abid_utils.models.find_prefix_for_abid

```{autodoc2-docstring} archivebox.abid_utils.models.find_prefix_for_abid
```
````

````{py:function} find_model_from_abid_prefix(prefix: str) -> type[archivebox.abid_utils.models.ABIDModel] | None
:canonical: archivebox.abid_utils.models.find_model_from_abid_prefix

```{autodoc2-docstring} archivebox.abid_utils.models.find_model_from_abid_prefix
```
````

````{py:function} find_model_from_abid(abid: archivebox.abid_utils.abid.ABID) -> type[django.db.models.Model] | None
:canonical: archivebox.abid_utils.models.find_model_from_abid

```{autodoc2-docstring} archivebox.abid_utils.models.find_model_from_abid
```
````

````{py:function} find_obj_from_abid_rand(rand: typing.Union[archivebox.abid_utils.abid.ABID, str], model=None) -> typing.List[archivebox.abid_utils.models.ABIDModel]
:canonical: archivebox.abid_utils.models.find_obj_from_abid_rand

```{autodoc2-docstring} archivebox.abid_utils.models.find_obj_from_abid_rand
```
````

````{py:function} find_obj_from_abid(abid: archivebox.abid_utils.abid.ABID, model=None, fuzzy=False) -> typing.Any
:canonical: archivebox.abid_utils.models.find_obj_from_abid

```{autodoc2-docstring} archivebox.abid_utils.models.find_obj_from_abid
```
````
