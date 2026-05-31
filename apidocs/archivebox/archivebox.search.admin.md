# {py:mod}`archivebox.search.admin`

```{py:module} archivebox.search.admin
```

```{autodoc2-docstring} archivebox.search.admin
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SearchResultsChangeList <archivebox.search.admin.SearchResultsChangeList>`
  - ```{autodoc2-docstring} archivebox.search.admin.SearchResultsChangeList
    :summary:
    ```
* - {py:obj}`SearchResultsAdminMixin <archivebox.search.admin.SearchResultsAdminMixin>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_admin_search_cache_key <archivebox.search.admin.get_admin_search_cache_key>`
  - ```{autodoc2-docstring} archivebox.search.admin.get_admin_search_cache_key
    :summary:
    ```
* - {py:obj}`get_cached_admin_search_ids <archivebox.search.admin.get_cached_admin_search_ids>`
  - ```{autodoc2-docstring} archivebox.search.admin.get_cached_admin_search_ids
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SEARCH_RESULT_CACHE_TTL <archivebox.search.admin.SEARCH_RESULT_CACHE_TTL>`
  - ```{autodoc2-docstring} archivebox.search.admin.SEARCH_RESULT_CACHE_TTL
    :summary:
    ```
````

### API

````{py:data} SEARCH_RESULT_CACHE_TTL
:canonical: archivebox.search.admin.SEARCH_RESULT_CACHE_TTL
:value: >
   60

```{autodoc2-docstring} archivebox.search.admin.SEARCH_RESULT_CACHE_TTL
```

````

````{py:function} get_admin_search_cache_key(request, url: str | None = None) -> str
:canonical: archivebox.search.admin.get_admin_search_cache_key

```{autodoc2-docstring} archivebox.search.admin.get_admin_search_cache_key
```
````

````{py:function} get_cached_admin_search_ids(request) -> list[str] | None
:canonical: archivebox.search.admin.get_cached_admin_search_ids

```{autodoc2-docstring} archivebox.search.admin.get_cached_admin_search_ids
```
````

`````{py:class} SearchResultsChangeList(request, *args, **kwargs)
:canonical: archivebox.search.admin.SearchResultsChangeList

Bases: {py:obj}`django.contrib.admin.views.main.ChangeList`

```{autodoc2-docstring} archivebox.search.admin.SearchResultsChangeList
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.search.admin.SearchResultsChangeList.__init__
```

````{py:method} get_results(request)
:canonical: archivebox.search.admin.SearchResultsChangeList.get_results

```{autodoc2-docstring} archivebox.search.admin.SearchResultsChangeList.get_results
```

````

````{py:method} get_filters_params(params=None)
:canonical: archivebox.search.admin.SearchResultsChangeList.get_filters_params

````

`````

`````{py:class} SearchResultsAdminMixin(model, admin_site)
:canonical: archivebox.search.admin.SearchResultsAdminMixin

Bases: {py:obj}`django.contrib.admin.ModelAdmin`

````{py:attribute} show_search_mode_selector
:canonical: archivebox.search.admin.SearchResultsAdminMixin.show_search_mode_selector
:value: >
   True

```{autodoc2-docstring} archivebox.search.admin.SearchResultsAdminMixin.show_search_mode_selector
```

````

````{py:method} get_changelist(request, **kwargs)
:canonical: archivebox.search.admin.SearchResultsAdminMixin.get_changelist

````

````{py:method} get_default_search_mode()
:canonical: archivebox.search.admin.SearchResultsAdminMixin.get_default_search_mode

```{autodoc2-docstring} archivebox.search.admin.SearchResultsAdminMixin.get_default_search_mode
```

````

````{py:method} get_search_mode_options()
:canonical: archivebox.search.admin.SearchResultsAdminMixin.get_search_mode_options

```{autodoc2-docstring} archivebox.search.admin.SearchResultsAdminMixin.get_search_mode_options
```

````

````{py:method} get_search_results(request, queryset, search_term: str)
:canonical: archivebox.search.admin.SearchResultsAdminMixin.get_search_results

```{autodoc2-docstring} archivebox.search.admin.SearchResultsAdminMixin.get_search_results
```

````

`````
