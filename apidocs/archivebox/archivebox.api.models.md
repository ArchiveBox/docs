# {py:mod}`archivebox.api.models`

```{py:module} archivebox.api.models
```

```{autodoc2-docstring} archivebox.api.models
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`APIToken <archivebox.api.models.APIToken>`
  - ```{autodoc2-docstring} archivebox.api.models.APIToken
    :summary:
    ```
* - {py:obj}`OutboundWebhook <archivebox.api.models.OutboundWebhook>`
  - ```{autodoc2-docstring} archivebox.api.models.OutboundWebhook
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`generate_secret_token <archivebox.api.models.generate_secret_token>`
  - ```{autodoc2-docstring} archivebox.api.models.generate_secret_token
    :summary:
    ```
````

### API

````{py:function} generate_secret_token() -> str
:canonical: archivebox.api.models.generate_secret_token

```{autodoc2-docstring} archivebox.api.models.generate_secret_token
```
````

``````{py:class} APIToken(*args: typing.Any, **kwargs: typing.Any)
:canonical: archivebox.api.models.APIToken

Bases: {py:obj}`abid_utils.models.ABIDModel`

```{autodoc2-docstring} archivebox.api.models.APIToken
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.api.models.APIToken.__init__
```

````{py:attribute} abid_prefix
:canonical: archivebox.api.models.APIToken.abid_prefix
:value: >
   'apt_'

```{autodoc2-docstring} archivebox.api.models.APIToken.abid_prefix
```

````

````{py:attribute} abid_ts_src
:canonical: archivebox.api.models.APIToken.abid_ts_src
:value: >
   'self.created_at'

```{autodoc2-docstring} archivebox.api.models.APIToken.abid_ts_src
```

````

````{py:attribute} abid_uri_src
:canonical: archivebox.api.models.APIToken.abid_uri_src
:value: >
   'self.created_by_id'

```{autodoc2-docstring} archivebox.api.models.APIToken.abid_uri_src
```

````

````{py:attribute} abid_subtype_src
:canonical: archivebox.api.models.APIToken.abid_subtype_src
:value: >
   '"01"'

```{autodoc2-docstring} archivebox.api.models.APIToken.abid_subtype_src
```

````

````{py:attribute} abid_rand_src
:canonical: archivebox.api.models.APIToken.abid_rand_src
:value: >
   'self.id'

```{autodoc2-docstring} archivebox.api.models.APIToken.abid_rand_src
```

````

````{py:attribute} abid_drift_allowed
:canonical: archivebox.api.models.APIToken.abid_drift_allowed
:value: >
   True

```{autodoc2-docstring} archivebox.api.models.APIToken.abid_drift_allowed
```

````

````{py:attribute} id
:canonical: archivebox.api.models.APIToken.id
:value: >
   'UUIDField(...)'

```{autodoc2-docstring} archivebox.api.models.APIToken.id
```

````

````{py:attribute} abid
:canonical: archivebox.api.models.APIToken.abid
:value: >
   'ABIDField(...)'

```{autodoc2-docstring} archivebox.api.models.APIToken.abid
```

````

````{py:attribute} created_by
:canonical: archivebox.api.models.APIToken.created_by
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.api.models.APIToken.created_by
```

````

````{py:attribute} created_at
:canonical: archivebox.api.models.APIToken.created_at
:value: >
   'AutoDateTimeField(...)'

```{autodoc2-docstring} archivebox.api.models.APIToken.created_at
```

````

````{py:attribute} modified_at
:canonical: archivebox.api.models.APIToken.modified_at
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.api.models.APIToken.modified_at
```

````

````{py:attribute} token
:canonical: archivebox.api.models.APIToken.token
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.api.models.APIToken.token
```

````

````{py:attribute} expires
:canonical: archivebox.api.models.APIToken.expires
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.api.models.APIToken.expires
```

````

`````{py:class} Meta
:canonical: archivebox.api.models.APIToken.Meta

Bases: {py:obj}`django_stubs_ext.db.models.TypedModelMeta`

````{py:attribute} verbose_name
:canonical: archivebox.api.models.APIToken.Meta.verbose_name
:value: >
   'API Key'

```{autodoc2-docstring} archivebox.api.models.APIToken.Meta.verbose_name
```

````

````{py:attribute} verbose_name_plural
:canonical: archivebox.api.models.APIToken.Meta.verbose_name_plural
:value: >
   'API Keys'

```{autodoc2-docstring} archivebox.api.models.APIToken.Meta.verbose_name_plural
```

````

`````

````{py:method} __str__() -> str
:canonical: archivebox.api.models.APIToken.__str__

````

````{py:method} __repr__() -> str
:canonical: archivebox.api.models.APIToken.__repr__

````

````{py:method} __json__() -> dict
:canonical: archivebox.api.models.APIToken.__json__

```{autodoc2-docstring} archivebox.api.models.APIToken.__json__
```

````

````{py:property} expires_as_iso8601
:canonical: archivebox.api.models.APIToken.expires_as_iso8601

```{autodoc2-docstring} archivebox.api.models.APIToken.expires_as_iso8601
```

````

````{py:property} token_redacted
:canonical: archivebox.api.models.APIToken.token_redacted

```{autodoc2-docstring} archivebox.api.models.APIToken.token_redacted
```

````

````{py:method} is_valid(for_date=None)
:canonical: archivebox.api.models.APIToken.is_valid

```{autodoc2-docstring} archivebox.api.models.APIToken.is_valid
```

````

``````

``````{py:class} OutboundWebhook(*args: typing.Any, **kwargs: typing.Any)
:canonical: archivebox.api.models.OutboundWebhook

Bases: {py:obj}`abid_utils.models.ABIDModel`, {py:obj}`signal_webhooks.models.WebhookBase`

```{autodoc2-docstring} archivebox.api.models.OutboundWebhook
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.api.models.OutboundWebhook.__init__
```

````{py:attribute} abid_prefix
:canonical: archivebox.api.models.OutboundWebhook.abid_prefix
:value: >
   'whk_'

```{autodoc2-docstring} archivebox.api.models.OutboundWebhook.abid_prefix
```

````

````{py:attribute} abid_ts_src
:canonical: archivebox.api.models.OutboundWebhook.abid_ts_src
:value: >
   'self.created_at'

```{autodoc2-docstring} archivebox.api.models.OutboundWebhook.abid_ts_src
```

````

````{py:attribute} abid_uri_src
:canonical: archivebox.api.models.OutboundWebhook.abid_uri_src
:value: >
   'self.endpoint'

```{autodoc2-docstring} archivebox.api.models.OutboundWebhook.abid_uri_src
```

````

````{py:attribute} abid_subtype_src
:canonical: archivebox.api.models.OutboundWebhook.abid_subtype_src
:value: >
   'self.ref'

```{autodoc2-docstring} archivebox.api.models.OutboundWebhook.abid_subtype_src
```

````

````{py:attribute} abid_rand_src
:canonical: archivebox.api.models.OutboundWebhook.abid_rand_src
:value: >
   'self.id'

```{autodoc2-docstring} archivebox.api.models.OutboundWebhook.abid_rand_src
```

````

````{py:attribute} abid_drift_allowed
:canonical: archivebox.api.models.OutboundWebhook.abid_drift_allowed
:value: >
   True

```{autodoc2-docstring} archivebox.api.models.OutboundWebhook.abid_drift_allowed
```

````

````{py:attribute} id
:canonical: archivebox.api.models.OutboundWebhook.id
:value: >
   'UUIDField(...)'

```{autodoc2-docstring} archivebox.api.models.OutboundWebhook.id
```

````

````{py:attribute} abid
:canonical: archivebox.api.models.OutboundWebhook.abid
:value: >
   'ABIDField(...)'

```{autodoc2-docstring} archivebox.api.models.OutboundWebhook.abid
```

````

````{py:attribute} created_by
:canonical: archivebox.api.models.OutboundWebhook.created_by
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.api.models.OutboundWebhook.created_by
```

````

````{py:attribute} created_at
:canonical: archivebox.api.models.OutboundWebhook.created_at
:value: >
   'AutoDateTimeField(...)'

```{autodoc2-docstring} archivebox.api.models.OutboundWebhook.created_at
```

````

````{py:attribute} modified_at
:canonical: archivebox.api.models.OutboundWebhook.modified_at
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.api.models.OutboundWebhook.modified_at
```

````

`````{py:class} Meta
:canonical: archivebox.api.models.OutboundWebhook.Meta

Bases: {py:obj}`signal_webhooks.models.WebhookBase.Meta`

```{autodoc2-docstring} archivebox.api.models.OutboundWebhook.Meta
```

````{py:attribute} verbose_name
:canonical: archivebox.api.models.OutboundWebhook.Meta.verbose_name
:value: >
   'API Outbound Webhook'

```{autodoc2-docstring} archivebox.api.models.OutboundWebhook.Meta.verbose_name
```

````

`````

````{py:method} __str__() -> str
:canonical: archivebox.api.models.OutboundWebhook.__str__

````

``````
