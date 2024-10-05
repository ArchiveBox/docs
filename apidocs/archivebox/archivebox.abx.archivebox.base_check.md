# {py:mod}`archivebox.abx.archivebox.base_check`

```{py:module} archivebox.abx.archivebox.base_check
```

```{autodoc2-docstring} archivebox.abx.archivebox.base_check
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseCheck <archivebox.abx.archivebox.base_check.BaseCheck>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.abx.archivebox.base_check.__package__>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_check.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.abx.archivebox.base_check.__package__
:value: >
   'abx.archivebox'

```{autodoc2-docstring} archivebox.abx.archivebox.base_check.__package__
```

````

`````{py:class} BaseCheck(/, **data: typing.Any)
:canonical: archivebox.abx.archivebox.base_check.BaseCheck

Bases: {py:obj}`archivebox.abx.archivebox.base_hook.BaseHook`

````{py:attribute} hook_type
:canonical: archivebox.abx.archivebox.base_check.BaseCheck.hook_type
:type: archivebox.abx.archivebox.base_hook.HookType
:value: >
   'CHECK'

```{autodoc2-docstring} archivebox.abx.archivebox.base_check.BaseCheck.hook_type
```

````

````{py:attribute} tag
:canonical: archivebox.abx.archivebox.base_check.BaseCheck.tag
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.abx.archivebox.base_check.BaseCheck.tag
```

````

````{py:method} check(settings, logger) -> typing.List[django.core.checks.Warning]
:canonical: archivebox.abx.archivebox.base_check.BaseCheck.check
:staticmethod:

```{autodoc2-docstring} archivebox.abx.archivebox.base_check.BaseCheck.check
```

````

````{py:method} get_CHECKS()
:canonical: archivebox.abx.archivebox.base_check.BaseCheck.get_CHECKS

```{autodoc2-docstring} archivebox.abx.archivebox.base_check.BaseCheck.get_CHECKS
```

````

````{py:method} register_checks()
:canonical: archivebox.abx.archivebox.base_check.BaseCheck.register_checks

```{autodoc2-docstring} archivebox.abx.archivebox.base_check.BaseCheck.register_checks
```

````

`````
