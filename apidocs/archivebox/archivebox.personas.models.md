# {py:mod}`archivebox.personas.models`

```{py:module} archivebox.personas.models
```

```{autodoc2-docstring} archivebox.personas.models
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Persona <archivebox.personas.models.Persona>`
  - ```{autodoc2-docstring} archivebox.personas.models.Persona
    :summary:
    ```
````

### API

``````{py:class} Persona(*args, **kwargs)
:canonical: archivebox.personas.models.Persona

Bases: {py:obj}`archivebox.base_models.models.ModelWithConfig`

```{autodoc2-docstring} archivebox.personas.models.Persona
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.personas.models.Persona.__init__
```

````{py:attribute} id
:canonical: archivebox.personas.models.Persona.id
:value: >
   'UUIDField(...)'

```{autodoc2-docstring} archivebox.personas.models.Persona.id
```

````

````{py:attribute} name
:canonical: archivebox.personas.models.Persona.name
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.personas.models.Persona.name
```

````

````{py:attribute} created_at
:canonical: archivebox.personas.models.Persona.created_at
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.personas.models.Persona.created_at
```

````

````{py:attribute} created_by
:canonical: archivebox.personas.models.Persona.created_by
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.personas.models.Persona.created_by
```

````

`````{py:class} Meta
:canonical: archivebox.personas.models.Persona.Meta

```{autodoc2-docstring} archivebox.personas.models.Persona.Meta
```

````{py:attribute} app_label
:canonical: archivebox.personas.models.Persona.Meta.app_label
:value: >
   'personas'

```{autodoc2-docstring} archivebox.personas.models.Persona.Meta.app_label
```

````

`````

````{py:method} __str__() -> str
:canonical: archivebox.personas.models.Persona.__str__

````

````{py:property} path
:canonical: archivebox.personas.models.Persona.path
:type: pathlib.Path

```{autodoc2-docstring} archivebox.personas.models.Persona.path
```

````

````{py:property} CHROME_USER_DATA_DIR
:canonical: archivebox.personas.models.Persona.CHROME_USER_DATA_DIR
:type: str

```{autodoc2-docstring} archivebox.personas.models.Persona.CHROME_USER_DATA_DIR
```

````

````{py:property} CHROME_EXTENSIONS_DIR
:canonical: archivebox.personas.models.Persona.CHROME_EXTENSIONS_DIR
:type: str

```{autodoc2-docstring} archivebox.personas.models.Persona.CHROME_EXTENSIONS_DIR
```

````

````{py:property} CHROME_DOWNLOADS_DIR
:canonical: archivebox.personas.models.Persona.CHROME_DOWNLOADS_DIR
:type: str

```{autodoc2-docstring} archivebox.personas.models.Persona.CHROME_DOWNLOADS_DIR
```

````

````{py:property} COOKIES_FILE
:canonical: archivebox.personas.models.Persona.COOKIES_FILE
:type: str

```{autodoc2-docstring} archivebox.personas.models.Persona.COOKIES_FILE
```

````

````{py:method} get_derived_config() -> dict
:canonical: archivebox.personas.models.Persona.get_derived_config

```{autodoc2-docstring} archivebox.personas.models.Persona.get_derived_config
```

````

````{py:method} ensure_dirs() -> None
:canonical: archivebox.personas.models.Persona.ensure_dirs

```{autodoc2-docstring} archivebox.personas.models.Persona.ensure_dirs
```

````

````{py:method} cleanup_chrome() -> bool
:canonical: archivebox.personas.models.Persona.cleanup_chrome

```{autodoc2-docstring} archivebox.personas.models.Persona.cleanup_chrome
```

````

````{py:method} get_or_create_default() -> archivebox.personas.models.Persona
:canonical: archivebox.personas.models.Persona.get_or_create_default
:classmethod:

```{autodoc2-docstring} archivebox.personas.models.Persona.get_or_create_default
```

````

````{py:method} cleanup_chrome_all() -> int
:canonical: archivebox.personas.models.Persona.cleanup_chrome_all
:classmethod:

```{autodoc2-docstring} archivebox.personas.models.Persona.cleanup_chrome_all
```

````

``````
