# {py:mod}`archivebox.misc.paginators`

```{py:module} archivebox.misc.paginators
```

```{autodoc2-docstring} archivebox.misc.paginators
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CountlessPage <archivebox.misc.paginators.CountlessPage>`
  -
* - {py:obj}`CountlessPaginator <archivebox.misc.paginators.CountlessPaginator>`
  - ```{autodoc2-docstring} archivebox.misc.paginators.CountlessPaginator
    :summary:
    ```
* - {py:obj}`AcceleratedPaginator <archivebox.misc.paginators.AcceleratedPaginator>`
  - ```{autodoc2-docstring} archivebox.misc.paginators.AcceleratedPaginator
    :summary:
    ```
````

### API

`````{py:class} CountlessPage(object_list, number, paginator, has_next_page=False)
:canonical: archivebox.misc.paginators.CountlessPage

Bases: {py:obj}`django.core.paginator.Page`

````{py:method} has_next()
:canonical: archivebox.misc.paginators.CountlessPage.has_next

```{autodoc2-docstring} archivebox.misc.paginators.CountlessPage.has_next
```

````

`````

`````{py:class} CountlessPaginator(object_list, per_page, orphans=0, allow_empty_first_page=True, error_messages=None)
:canonical: archivebox.misc.paginators.CountlessPaginator

Bases: {py:obj}`django.core.paginator.Paginator`

```{autodoc2-docstring} archivebox.misc.paginators.CountlessPaginator
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.misc.paginators.CountlessPaginator.__init__
```

````{py:attribute} has_exact_count
:canonical: archivebox.misc.paginators.CountlessPaginator.has_exact_count
:value: >
   False

```{autodoc2-docstring} archivebox.misc.paginators.CountlessPaginator.has_exact_count
```

````

````{py:method} count()
:canonical: archivebox.misc.paginators.CountlessPaginator.count

````

````{py:method} num_pages()
:canonical: archivebox.misc.paginators.CountlessPaginator.num_pages

````

````{py:method} validate_number(number)
:canonical: archivebox.misc.paginators.CountlessPaginator.validate_number

```{autodoc2-docstring} archivebox.misc.paginators.CountlessPaginator.validate_number
```

````

````{py:method} page(number)
:canonical: archivebox.misc.paginators.CountlessPaginator.page

````

`````

`````{py:class} AcceleratedPaginator(object_list, per_page, orphans=0, allow_empty_first_page=True, error_messages=None)
:canonical: archivebox.misc.paginators.AcceleratedPaginator

Bases: {py:obj}`django.core.paginator.Paginator`

```{autodoc2-docstring} archivebox.misc.paginators.AcceleratedPaginator
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.misc.paginators.AcceleratedPaginator.__init__
```

````{py:method} count()
:canonical: archivebox.misc.paginators.AcceleratedPaginator.count

````

`````
