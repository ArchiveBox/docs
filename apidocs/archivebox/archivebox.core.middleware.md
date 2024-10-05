# {py:mod}`archivebox.core.middleware`

```{py:module} archivebox.core.middleware
```

```{autodoc2-docstring} archivebox.core.middleware
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ReverseProxyAuthMiddleware <archivebox.core.middleware.ReverseProxyAuthMiddleware>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`detect_timezone <archivebox.core.middleware.detect_timezone>`
  - ```{autodoc2-docstring} archivebox.core.middleware.detect_timezone
    :summary:
    ```
* - {py:obj}`TimezoneMiddleware <archivebox.core.middleware.TimezoneMiddleware>`
  - ```{autodoc2-docstring} archivebox.core.middleware.TimezoneMiddleware
    :summary:
    ```
* - {py:obj}`CacheControlMiddleware <archivebox.core.middleware.CacheControlMiddleware>`
  - ```{autodoc2-docstring} archivebox.core.middleware.CacheControlMiddleware
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.core.middleware.__package__>`
  - ```{autodoc2-docstring} archivebox.core.middleware.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.core.middleware.__package__
:value: >
   'archivebox.core'

```{autodoc2-docstring} archivebox.core.middleware.__package__
```

````

````{py:function} detect_timezone(request, activate: bool = True)
:canonical: archivebox.core.middleware.detect_timezone

```{autodoc2-docstring} archivebox.core.middleware.detect_timezone
```
````

````{py:function} TimezoneMiddleware(get_response)
:canonical: archivebox.core.middleware.TimezoneMiddleware

```{autodoc2-docstring} archivebox.core.middleware.TimezoneMiddleware
```
````

````{py:function} CacheControlMiddleware(get_response)
:canonical: archivebox.core.middleware.CacheControlMiddleware

```{autodoc2-docstring} archivebox.core.middleware.CacheControlMiddleware
```
````

`````{py:class} ReverseProxyAuthMiddleware(get_response)
:canonical: archivebox.core.middleware.ReverseProxyAuthMiddleware

Bases: {py:obj}`django.contrib.auth.middleware.RemoteUserMiddleware`

````{py:attribute} header
:canonical: archivebox.core.middleware.ReverseProxyAuthMiddleware.header
:value: >
   'format(...)'

```{autodoc2-docstring} archivebox.core.middleware.ReverseProxyAuthMiddleware.header
```

````

````{py:method} process_request(request)
:canonical: archivebox.core.middleware.ReverseProxyAuthMiddleware.process_request

```{autodoc2-docstring} archivebox.core.middleware.ReverseProxyAuthMiddleware.process_request
```

````

`````
