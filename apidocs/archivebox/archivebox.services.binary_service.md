# {py:mod}`archivebox.services.binary_service`

```{py:module} archivebox.services.binary_service
```

```{autodoc2-docstring} archivebox.services.binary_service
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BinaryService <archivebox.services.binary_service.BinaryService>`
  -
````

### API

`````{py:class} BinaryService(bus)
:canonical: archivebox.services.binary_service.BinaryService

Bases: {py:obj}`abx_dl.services.base.BaseService`

````{py:attribute} LISTENS_TO
:canonical: archivebox.services.binary_service.BinaryService.LISTENS_TO
:value: >
   None

```{autodoc2-docstring} archivebox.services.binary_service.BinaryService.LISTENS_TO
```

````

````{py:attribute} EMITS
:canonical: archivebox.services.binary_service.BinaryService.EMITS
:value: >
   []

```{autodoc2-docstring} archivebox.services.binary_service.BinaryService.EMITS
```

````

````{py:method} on_BinaryRequestEvent(event: abx_dl.events.BinaryRequestEvent) -> str | None
:canonical: archivebox.services.binary_service.BinaryService.on_BinaryRequestEvent
:async:

```{autodoc2-docstring} archivebox.services.binary_service.BinaryService.on_BinaryRequestEvent
```

````

````{py:method} on_BinaryEvent(event: abx_dl.events.BinaryEvent) -> None
:canonical: archivebox.services.binary_service.BinaryService.on_BinaryEvent
:async:

```{autodoc2-docstring} archivebox.services.binary_service.BinaryService.on_BinaryEvent
```

````

`````
