# {py:mod}`archivebox.api.admin`

```{py:module} archivebox.api.admin
```

```{autodoc2-docstring} archivebox.api.admin
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`APITokenAdmin <archivebox.api.admin.APITokenAdmin>`
  -
* - {py:obj}`CustomWebhookAdmin <archivebox.api.admin.CustomWebhookAdmin>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`register_admin <archivebox.api.admin.register_admin>`
  - ```{autodoc2-docstring} archivebox.api.admin.register_admin
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.api.admin.__package__>`
  - ```{autodoc2-docstring} archivebox.api.admin.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.api.admin.__package__
:value: >
   'archivebox.api'

```{autodoc2-docstring} archivebox.api.admin.__package__
```

````

`````{py:class} APITokenAdmin(model, admin_site)
:canonical: archivebox.api.admin.APITokenAdmin

Bases: {py:obj}`abid_utils.admin.ABIDModelAdmin`

````{py:attribute} list_display
:canonical: archivebox.api.admin.APITokenAdmin.list_display
:value: >
   ('created_at', 'abid', 'created_by', 'token_redacted', 'expires')

```{autodoc2-docstring} archivebox.api.admin.APITokenAdmin.list_display
```

````

````{py:attribute} sort_fields
:canonical: archivebox.api.admin.APITokenAdmin.sort_fields
:value: >
   ('abid', 'created_at', 'created_by', 'expires')

```{autodoc2-docstring} archivebox.api.admin.APITokenAdmin.sort_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.api.admin.APITokenAdmin.readonly_fields
:value: >
   ('created_at', 'modified_at', 'abid_info')

```{autodoc2-docstring} archivebox.api.admin.APITokenAdmin.readonly_fields
```

````

````{py:attribute} search_fields
:canonical: archivebox.api.admin.APITokenAdmin.search_fields
:value: >
   ('id', 'abid', 'created_by__username', 'token')

```{autodoc2-docstring} archivebox.api.admin.APITokenAdmin.search_fields
```

````

````{py:attribute} fields
:canonical: archivebox.api.admin.APITokenAdmin.fields
:value: >
   ('created_by', 'token', 'expires')

```{autodoc2-docstring} archivebox.api.admin.APITokenAdmin.fields
```

````

````{py:attribute} list_filter
:canonical: archivebox.api.admin.APITokenAdmin.list_filter
:value: >
   ('created_by',)

```{autodoc2-docstring} archivebox.api.admin.APITokenAdmin.list_filter
```

````

````{py:attribute} ordering
:canonical: archivebox.api.admin.APITokenAdmin.ordering
:value: >
   ['-created_at']

```{autodoc2-docstring} archivebox.api.admin.APITokenAdmin.ordering
```

````

````{py:attribute} list_per_page
:canonical: archivebox.api.admin.APITokenAdmin.list_per_page
:value: >
   100

```{autodoc2-docstring} archivebox.api.admin.APITokenAdmin.list_per_page
```

````

`````

`````{py:class} CustomWebhookAdmin(model, admin_site)
:canonical: archivebox.api.admin.CustomWebhookAdmin

Bases: {py:obj}`signal_webhooks.admin.WebhookAdmin`, {py:obj}`abid_utils.admin.ABIDModelAdmin`

````{py:attribute} list_display
:canonical: archivebox.api.admin.CustomWebhookAdmin.list_display
:value: >
   ('created_at', 'created_by', 'abid')

```{autodoc2-docstring} archivebox.api.admin.CustomWebhookAdmin.list_display
```

````

````{py:attribute} sort_fields
:canonical: archivebox.api.admin.CustomWebhookAdmin.sort_fields
:value: >
   ('created_at', 'created_by', 'abid', 'referenced_model', 'endpoint', 'last_success', 'last_error')

```{autodoc2-docstring} archivebox.api.admin.CustomWebhookAdmin.sort_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.api.admin.CustomWebhookAdmin.readonly_fields
:value: >
   ('created_at', 'modified_at', 'abid_info')

```{autodoc2-docstring} archivebox.api.admin.CustomWebhookAdmin.readonly_fields
```

````

`````

````{py:function} register_admin(admin_site)
:canonical: archivebox.api.admin.register_admin

```{autodoc2-docstring} archivebox.api.admin.register_admin
```
````
