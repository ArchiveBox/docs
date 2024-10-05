# {py:mod}`archivebox.monkey_patches`

```{py:module} archivebox.monkey_patches
```

```{autodoc2-docstring} archivebox.monkey_patches
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ModifiedAccessLogGenerator <archivebox.monkey_patches.ModifiedAccessLogGenerator>`
  - ```{autodoc2-docstring} archivebox.monkey_patches.ModifiedAccessLogGenerator
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.monkey_patches.__package__>`
  - ```{autodoc2-docstring} archivebox.monkey_patches.__package__
    :summary:
    ```
* - {py:obj}`TERM_WIDTH <archivebox.monkey_patches.TERM_WIDTH>`
  - ```{autodoc2-docstring} archivebox.monkey_patches.TERM_WIDTH
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.monkey_patches.__package__
:value: >
   'archivebox'

```{autodoc2-docstring} archivebox.monkey_patches.__package__
```

````

````{py:data} TERM_WIDTH
:canonical: archivebox.monkey_patches.TERM_WIDTH
:value: >
   None

```{autodoc2-docstring} archivebox.monkey_patches.TERM_WIDTH
```

````

`````{py:class} ModifiedAccessLogGenerator(stream)
:canonical: archivebox.monkey_patches.ModifiedAccessLogGenerator

Bases: {py:obj}`daphne.access.AccessLogGenerator`

```{autodoc2-docstring} archivebox.monkey_patches.ModifiedAccessLogGenerator
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.monkey_patches.ModifiedAccessLogGenerator.__init__
```

````{py:method} write_entry(host, date, request, status=None, length=None, ident=None, user=None)
:canonical: archivebox.monkey_patches.ModifiedAccessLogGenerator.write_entry

````

`````
