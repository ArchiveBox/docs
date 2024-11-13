# {py:mod}`archivebox.seeds.models`

```{py:module} archivebox.seeds.models
```

```{autodoc2-docstring} archivebox.seeds.models
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Seed <archivebox.seeds.models.Seed>`
  - ```{autodoc2-docstring} archivebox.seeds.models.Seed
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.seeds.models.__package__>`
  - ```{autodoc2-docstring} archivebox.seeds.models.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.seeds.models.__package__
:value: >
   'archivebox.seeds'

```{autodoc2-docstring} archivebox.seeds.models.__package__
```

````

``````{py:class} Seed(*args: typing.Any, **kwargs: typing.Any)
:canonical: archivebox.seeds.models.Seed

Bases: {py:obj}`abid_utils.models.ABIDModel`, {py:obj}`abid_utils.models.ModelWithHealthStats`

```{autodoc2-docstring} archivebox.seeds.models.Seed
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.seeds.models.Seed.__init__
```

````{py:attribute} abid_prefix
:canonical: archivebox.seeds.models.Seed.abid_prefix
:value: >
   'src_'

```{autodoc2-docstring} archivebox.seeds.models.Seed.abid_prefix
```

````

````{py:attribute} abid_ts_src
:canonical: archivebox.seeds.models.Seed.abid_ts_src
:value: >
   'self.created_at'

```{autodoc2-docstring} archivebox.seeds.models.Seed.abid_ts_src
```

````

````{py:attribute} abid_uri_src
:canonical: archivebox.seeds.models.Seed.abid_uri_src
:value: >
   'self.uri'

```{autodoc2-docstring} archivebox.seeds.models.Seed.abid_uri_src
```

````

````{py:attribute} abid_subtype_src
:canonical: archivebox.seeds.models.Seed.abid_subtype_src
:value: >
   'self.extractor'

```{autodoc2-docstring} archivebox.seeds.models.Seed.abid_subtype_src
```

````

````{py:attribute} abid_rand_src
:canonical: archivebox.seeds.models.Seed.abid_rand_src
:value: >
   'self.id'

```{autodoc2-docstring} archivebox.seeds.models.Seed.abid_rand_src
```

````

````{py:attribute} abid_drift_allowed
:canonical: archivebox.seeds.models.Seed.abid_drift_allowed
:value: >
   True

```{autodoc2-docstring} archivebox.seeds.models.Seed.abid_drift_allowed
```

````

````{py:attribute} id
:canonical: archivebox.seeds.models.Seed.id
:value: >
   'UUIDField(...)'

```{autodoc2-docstring} archivebox.seeds.models.Seed.id
```

````

````{py:attribute} abid
:canonical: archivebox.seeds.models.Seed.abid
:value: >
   'ABIDField(...)'

```{autodoc2-docstring} archivebox.seeds.models.Seed.abid
```

````

````{py:attribute} uri
:canonical: archivebox.seeds.models.Seed.uri
:value: >
   'URLField(...)'

```{autodoc2-docstring} archivebox.seeds.models.Seed.uri
```

````

````{py:attribute} extractor
:canonical: archivebox.seeds.models.Seed.extractor
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.seeds.models.Seed.extractor
```

````

````{py:attribute} tags_str
:canonical: archivebox.seeds.models.Seed.tags_str
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.seeds.models.Seed.tags_str
```

````

````{py:attribute} config
:canonical: archivebox.seeds.models.Seed.config
:value: >
   'JSONField(...)'

```{autodoc2-docstring} archivebox.seeds.models.Seed.config
```

````

````{py:attribute} created_at
:canonical: archivebox.seeds.models.Seed.created_at
:value: >
   'AutoDateTimeField(...)'

```{autodoc2-docstring} archivebox.seeds.models.Seed.created_at
```

````

````{py:attribute} modified_at
:canonical: archivebox.seeds.models.Seed.modified_at
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.seeds.models.Seed.modified_at
```

````

````{py:attribute} created_by
:canonical: archivebox.seeds.models.Seed.created_by
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.seeds.models.Seed.created_by
```

````

````{py:property} source_type
:canonical: archivebox.seeds.models.Seed.source_type

```{autodoc2-docstring} archivebox.seeds.models.Seed.source_type
```

````

`````{py:class} Meta
:canonical: archivebox.seeds.models.Seed.Meta

```{autodoc2-docstring} archivebox.seeds.models.Seed.Meta
```

````{py:attribute} verbose_name
:canonical: archivebox.seeds.models.Seed.Meta.verbose_name
:value: >
   'Seed'

```{autodoc2-docstring} archivebox.seeds.models.Seed.Meta.verbose_name
```

````

````{py:attribute} verbose_name_plural
:canonical: archivebox.seeds.models.Seed.Meta.verbose_name_plural
:value: >
   'Seeds'

```{autodoc2-docstring} archivebox.seeds.models.Seed.Meta.verbose_name_plural
```

````

````{py:attribute} unique_together
:canonical: archivebox.seeds.models.Seed.Meta.unique_together
:value: >
   (('created_by', 'uri', 'extractor'),)

```{autodoc2-docstring} archivebox.seeds.models.Seed.Meta.unique_together
```

````

`````

``````
