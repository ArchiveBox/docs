# {py:mod}`archivebox.misc.monkey_patches`

```{py:module} archivebox.misc.monkey_patches
```

```{autodoc2-docstring} archivebox.misc.monkey_patches
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ModifiedAccessLogGenerator <archivebox.misc.monkey_patches.ModifiedAccessLogGenerator>`
  - ```{autodoc2-docstring} archivebox.misc.monkey_patches.ModifiedAccessLogGenerator
    :summary:
    ```
````

### API

`````{py:class} ModifiedAccessLogGenerator(stream)
:canonical: archivebox.misc.monkey_patches.ModifiedAccessLogGenerator

Bases: {py:obj}`daphne.access.AccessLogGenerator`

```{autodoc2-docstring} archivebox.misc.monkey_patches.ModifiedAccessLogGenerator
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.misc.monkey_patches.ModifiedAccessLogGenerator.__init__
```

````{py:method} write_entry(host, date, request, status=None, length=None, ident=None, user=None)
:canonical: archivebox.misc.monkey_patches.ModifiedAccessLogGenerator.write_entry

````

`````
