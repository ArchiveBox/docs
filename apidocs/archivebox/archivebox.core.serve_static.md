# {py:mod}`archivebox.core.serve_static`

```{py:module} archivebox.core.serve_static
```

```{autodoc2-docstring} archivebox.core.serve_static
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`RangedFileReader <archivebox.core.serve_static.RangedFileReader>`
  - ```{autodoc2-docstring} archivebox.core.serve_static.RangedFileReader
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`serve_static_with_byterange_support <archivebox.core.serve_static.serve_static_with_byterange_support>`
  - ```{autodoc2-docstring} archivebox.core.serve_static.serve_static_with_byterange_support
    :summary:
    ```
* - {py:obj}`serve_static <archivebox.core.serve_static.serve_static>`
  - ```{autodoc2-docstring} archivebox.core.serve_static.serve_static
    :summary:
    ```
* - {py:obj}`parse_range_header <archivebox.core.serve_static.parse_range_header>`
  - ```{autodoc2-docstring} archivebox.core.serve_static.parse_range_header
    :summary:
    ```
````

### API

````{py:function} serve_static_with_byterange_support(request, path, document_root=None, show_indexes=False)
:canonical: archivebox.core.serve_static.serve_static_with_byterange_support

```{autodoc2-docstring} archivebox.core.serve_static.serve_static_with_byterange_support
```
````

````{py:function} serve_static(request, path, **kwargs)
:canonical: archivebox.core.serve_static.serve_static

```{autodoc2-docstring} archivebox.core.serve_static.serve_static
```
````

````{py:function} parse_range_header(header, resource_size)
:canonical: archivebox.core.serve_static.parse_range_header

```{autodoc2-docstring} archivebox.core.serve_static.parse_range_header
```
````

`````{py:class} RangedFileReader(file_like, start=0, stop=float('inf'), block_size=None)
:canonical: archivebox.core.serve_static.RangedFileReader

```{autodoc2-docstring} archivebox.core.serve_static.RangedFileReader
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.core.serve_static.RangedFileReader.__init__
```

````{py:attribute} block_size
:canonical: archivebox.core.serve_static.RangedFileReader.block_size
:value: >
   8192

```{autodoc2-docstring} archivebox.core.serve_static.RangedFileReader.block_size
```

````

````{py:method} __iter__()
:canonical: archivebox.core.serve_static.RangedFileReader.__iter__

```{autodoc2-docstring} archivebox.core.serve_static.RangedFileReader.__iter__
```

````

`````
