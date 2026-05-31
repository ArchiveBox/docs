# {py:mod}`archivebox.core.forms`

```{py:module} archivebox.core.forms
```

```{autodoc2-docstring} archivebox.core.forms
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PluginConfigFormMixin <archivebox.core.forms.PluginConfigFormMixin>`
  - ```{autodoc2-docstring} archivebox.core.forms.PluginConfigFormMixin
    :summary:
    ```
* - {py:obj}`AddLinkForm <archivebox.core.forms.AddLinkForm>`
  -
* - {py:obj}`TagWidget <archivebox.core.forms.TagWidget>`
  -
* - {py:obj}`TagField <archivebox.core.forms.TagField>`
  - ```{autodoc2-docstring} archivebox.core.forms.TagField
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_plugin_choices <archivebox.core.forms.get_plugin_choices>`
  - ```{autodoc2-docstring} archivebox.core.forms.get_plugin_choices
    :summary:
    ```
* - {py:obj}`get_plugin_choice_label <archivebox.core.forms.get_plugin_choice_label>`
  - ```{autodoc2-docstring} archivebox.core.forms.get_plugin_choice_label
    :summary:
    ```
* - {py:obj}`get_choice_field <archivebox.core.forms.get_choice_field>`
  - ```{autodoc2-docstring} archivebox.core.forms.get_choice_field
    :summary:
    ```
* - {py:obj}`_plugin_config_input_name <archivebox.core.forms._plugin_config_input_name>`
  - ```{autodoc2-docstring} archivebox.core.forms._plugin_config_input_name
    :summary:
    ```
* - {py:obj}`_schema_types <archivebox.core.forms._schema_types>`
  - ```{autodoc2-docstring} archivebox.core.forms._schema_types
    :summary:
    ```
* - {py:obj}`_jsonish <archivebox.core.forms._jsonish>`
  - ```{autodoc2-docstring} archivebox.core.forms._jsonish
    :summary:
    ```
* - {py:obj}`_same_config_value <archivebox.core.forms._same_config_value>`
  - ```{autodoc2-docstring} archivebox.core.forms._same_config_value
    :summary:
    ```
* - {py:obj}`_coerce_plugin_config_value <archivebox.core.forms._coerce_plugin_config_value>`
  - ```{autodoc2-docstring} archivebox.core.forms._coerce_plugin_config_value
    :summary:
    ```
* - {py:obj}`_resolve_required_binary_name <archivebox.core.forms._resolve_required_binary_name>`
  - ```{autodoc2-docstring} archivebox.core.forms._resolve_required_binary_name
    :summary:
    ```
* - {py:obj}`_iter_required_binary_names <archivebox.core.forms._iter_required_binary_names>`
  - ```{autodoc2-docstring} archivebox.core.forms._iter_required_binary_names
    :summary:
    ```
* - {py:obj}`_build_required_binary_url_lookup <archivebox.core.forms._build_required_binary_url_lookup>`
  - ```{autodoc2-docstring} archivebox.core.forms._build_required_binary_url_lookup
    :summary:
    ```
* - {py:obj}`_build_required_binary_links <archivebox.core.forms._build_required_binary_links>`
  - ```{autodoc2-docstring} archivebox.core.forms._build_required_binary_links
    :summary:
    ```
* - {py:obj}`get_plugin_config_binary_urls <archivebox.core.forms.get_plugin_config_binary_urls>`
  - ```{autodoc2-docstring} archivebox.core.forms.get_plugin_config_binary_urls
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DEPTH_CHOICES <archivebox.core.forms.DEPTH_CHOICES>`
  - ```{autodoc2-docstring} archivebox.core.forms.DEPTH_CHOICES
    :summary:
    ```
* - {py:obj}`PLUGIN_CONFIG_FIELD_PREFIX <archivebox.core.forms.PLUGIN_CONFIG_FIELD_PREFIX>`
  - ```{autodoc2-docstring} archivebox.core.forms.PLUGIN_CONFIG_FIELD_PREFIX
    :summary:
    ```
* - {py:obj}`PLUGIN_GROUP_DEFINITIONS <archivebox.core.forms.PLUGIN_GROUP_DEFINITIONS>`
  - ```{autodoc2-docstring} archivebox.core.forms.PLUGIN_GROUP_DEFINITIONS
    :summary:
    ```
* - {py:obj}`HIDDEN_PLUGIN_CONFIG_UI_PLUGINS <archivebox.core.forms.HIDDEN_PLUGIN_CONFIG_UI_PLUGINS>`
  - ```{autodoc2-docstring} archivebox.core.forms.HIDDEN_PLUGIN_CONFIG_UI_PLUGINS
    :summary:
    ```
* - {py:obj}`TIMEOUT_INPUT_PATTERN <archivebox.core.forms.TIMEOUT_INPUT_PATTERN>`
  - ```{autodoc2-docstring} archivebox.core.forms.TIMEOUT_INPUT_PATTERN
    :summary:
    ```
* - {py:obj}`_BINARY_TEMPLATE_PATTERN <archivebox.core.forms._BINARY_TEMPLATE_PATTERN>`
  - ```{autodoc2-docstring} archivebox.core.forms._BINARY_TEMPLATE_PATTERN
    :summary:
    ```
````

### API

````{py:data} DEPTH_CHOICES
:canonical: archivebox.core.forms.DEPTH_CHOICES
:value: >
   (('0', 'depth = 0 (archive just these URLs)'), ('1', 'depth = 1 (+ URLs one hop away)'), ('2', 'dept...

```{autodoc2-docstring} archivebox.core.forms.DEPTH_CHOICES
```

````

````{py:data} PLUGIN_CONFIG_FIELD_PREFIX
:canonical: archivebox.core.forms.PLUGIN_CONFIG_FIELD_PREFIX
:value: >
   'plugin_config__'

```{autodoc2-docstring} archivebox.core.forms.PLUGIN_CONFIG_FIELD_PREFIX
```

````

````{py:data} PLUGIN_GROUP_DEFINITIONS
:canonical: archivebox.core.forms.PLUGIN_GROUP_DEFINITIONS
:value: >
   (('main_plugins', 'Main', '', '', '', ('dom', 'screenshot', 'pdf', 'singlefile', 'wget', 'archivedot...

```{autodoc2-docstring} archivebox.core.forms.PLUGIN_GROUP_DEFINITIONS
```

````

````{py:data} HIDDEN_PLUGIN_CONFIG_UI_PLUGINS
:canonical: archivebox.core.forms.HIDDEN_PLUGIN_CONFIG_UI_PLUGINS
:value: >
   None

```{autodoc2-docstring} archivebox.core.forms.HIDDEN_PLUGIN_CONFIG_UI_PLUGINS
```

````

````{py:data} TIMEOUT_INPUT_PATTERN
:canonical: archivebox.core.forms.TIMEOUT_INPUT_PATTERN
:value: >
   '(0|[1-9][0-9]*|[0-9]+(?:\\.[0-9]+)?\\s*(?:s|sec|secs|second|seconds|m|min|mins|minute|minutes|h|hr|hrs...'

```{autodoc2-docstring} archivebox.core.forms.TIMEOUT_INPUT_PATTERN
```

````

````{py:function} get_plugin_choices()
:canonical: archivebox.core.forms.get_plugin_choices

```{autodoc2-docstring} archivebox.core.forms.get_plugin_choices
```
````

````{py:function} get_plugin_choice_label(plugin_name: str, plugin_configs: dict[str, dict]) -> str
:canonical: archivebox.core.forms.get_plugin_choice_label

```{autodoc2-docstring} archivebox.core.forms.get_plugin_choice_label
```
````

````{py:function} get_choice_field(form: django.forms.Form, name: str) -> django.forms.ChoiceField
:canonical: archivebox.core.forms.get_choice_field

```{autodoc2-docstring} archivebox.core.forms.get_choice_field
```
````

````{py:function} _plugin_config_input_name(plugin_name: str, config_key: str) -> str
:canonical: archivebox.core.forms._plugin_config_input_name

```{autodoc2-docstring} archivebox.core.forms._plugin_config_input_name
```
````

````{py:function} _schema_types(schema: collections.abc.Mapping[str, typing.Any]) -> list[str]
:canonical: archivebox.core.forms._schema_types

```{autodoc2-docstring} archivebox.core.forms._schema_types
```
````

````{py:function} _jsonish(value: typing.Any) -> str
:canonical: archivebox.core.forms._jsonish

```{autodoc2-docstring} archivebox.core.forms._jsonish
```
````

````{py:function} _same_config_value(left: typing.Any, right: typing.Any) -> bool
:canonical: archivebox.core.forms._same_config_value

```{autodoc2-docstring} archivebox.core.forms._same_config_value
```
````

````{py:function} _coerce_plugin_config_value(raw_value: typing.Any, schema: collections.abc.Mapping[str, typing.Any]) -> typing.Any
:canonical: archivebox.core.forms._coerce_plugin_config_value

```{autodoc2-docstring} archivebox.core.forms._coerce_plugin_config_value
```
````

`````{py:class} PluginConfigFormMixin
:canonical: archivebox.core.forms.PluginConfigFormMixin

```{autodoc2-docstring} archivebox.core.forms.PluginConfigFormMixin
```

````{py:attribute} plugin_groups
:canonical: archivebox.core.forms.PluginConfigFormMixin.plugin_groups
:type: list[dict[str, typing.Any]]
:value: >
   None

```{autodoc2-docstring} archivebox.core.forms.PluginConfigFormMixin.plugin_groups
```

````

````{py:method} build_plugin_groups(runtime_config: collections.abc.Mapping[str, typing.Any] | None = None) -> None
:canonical: archivebox.core.forms.PluginConfigFormMixin.build_plugin_groups

```{autodoc2-docstring} archivebox.core.forms.PluginConfigFormMixin.build_plugin_groups
```

````

````{py:method} _build_plugin_cards(field_name: str, plugin_names: collections.abc.Iterable[str], plugin_configs: dict[str, dict[str, typing.Any]], runtime_config: collections.abc.Mapping[str, typing.Any], binary_url_lookup: collections.abc.Mapping[str, str] | None = None) -> list[dict[str, typing.Any]]
:canonical: archivebox.core.forms.PluginConfigFormMixin._build_plugin_cards

```{autodoc2-docstring} archivebox.core.forms.PluginConfigFormMixin._build_plugin_cards
```

````

````{py:method} _build_plugin_config_field(plugin_name: str, config_key: str, prop_schema: collections.abc.Mapping[str, typing.Any], runtime_config: collections.abc.Mapping[str, typing.Any]) -> dict[str, typing.Any]
:canonical: archivebox.core.forms.PluginConfigFormMixin._build_plugin_config_field

```{autodoc2-docstring} archivebox.core.forms.PluginConfigFormMixin._build_plugin_config_field
```

````

````{py:method} clean_plugin_config_overrides(effective_config: collections.abc.Mapping[str, typing.Any] | None = None) -> dict[str, typing.Any]
:canonical: archivebox.core.forms.PluginConfigFormMixin.clean_plugin_config_overrides

```{autodoc2-docstring} archivebox.core.forms.PluginConfigFormMixin.clean_plugin_config_overrides
```

````

````{py:method} plugin_config_keys() -> set[str]
:canonical: archivebox.core.forms.PluginConfigFormMixin.plugin_config_keys

```{autodoc2-docstring} archivebox.core.forms.PluginConfigFormMixin.plugin_config_keys
```

````

`````

````{py:data} _BINARY_TEMPLATE_PATTERN
:canonical: archivebox.core.forms._BINARY_TEMPLATE_PATTERN
:value: >
   'compile(...)'

```{autodoc2-docstring} archivebox.core.forms._BINARY_TEMPLATE_PATTERN
```

````

````{py:function} _resolve_required_binary_name(template_name: str, runtime_config: collections.abc.Mapping[str, typing.Any]) -> str
:canonical: archivebox.core.forms._resolve_required_binary_name

```{autodoc2-docstring} archivebox.core.forms._resolve_required_binary_name
```
````

````{py:function} _iter_required_binary_names(required_binaries: collections.abc.Iterable[typing.Any], runtime_config: collections.abc.Mapping[str, typing.Any]) -> collections.abc.Iterable[str]
:canonical: archivebox.core.forms._iter_required_binary_names

```{autodoc2-docstring} archivebox.core.forms._iter_required_binary_names
```
````

````{py:function} _build_required_binary_url_lookup(plugin_configs: collections.abc.Mapping[str, dict[str, typing.Any]], runtime_config: collections.abc.Mapping[str, typing.Any]) -> dict[str, str]
:canonical: archivebox.core.forms._build_required_binary_url_lookup

```{autodoc2-docstring} archivebox.core.forms._build_required_binary_url_lookup
```
````

````{py:function} _build_required_binary_links(required_binaries: list[dict[str, typing.Any]], runtime_config: collections.abc.Mapping[str, typing.Any], binary_url_lookup: collections.abc.Mapping[str, str] | None = None) -> list[dict[str, str]]
:canonical: archivebox.core.forms._build_required_binary_links

```{autodoc2-docstring} archivebox.core.forms._build_required_binary_links
```
````

````{py:function} get_plugin_config_binary_urls(runtime_config: collections.abc.Mapping[str, typing.Any]) -> dict[str, str]
:canonical: archivebox.core.forms.get_plugin_config_binary_urls

```{autodoc2-docstring} archivebox.core.forms.get_plugin_config_binary_urls
```
````

`````{py:class} AddLinkForm(*args, **kwargs)
:canonical: archivebox.core.forms.AddLinkForm

Bases: {py:obj}`archivebox.core.forms.PluginConfigFormMixin`, {py:obj}`django.forms.Form`

````{py:attribute} url
:canonical: archivebox.core.forms.AddLinkForm.url
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.url
```

````

````{py:attribute} tag
:canonical: archivebox.core.forms.AddLinkForm.tag
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.tag
```

````

````{py:attribute} depth
:canonical: archivebox.core.forms.AddLinkForm.depth
:value: >
   'ChoiceField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.depth
```

````

````{py:attribute} max_urls
:canonical: archivebox.core.forms.AddLinkForm.max_urls
:value: >
   'IntegerField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.max_urls
```

````

````{py:attribute} crawl_max_size
:canonical: archivebox.core.forms.AddLinkForm.crawl_max_size
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.crawl_max_size
```

````

````{py:attribute} crawl_timeout
:canonical: archivebox.core.forms.AddLinkForm.crawl_timeout
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.crawl_timeout
```

````

````{py:attribute} timeout
:canonical: archivebox.core.forms.AddLinkForm.timeout
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.timeout
```

````

````{py:attribute} snapshot_max_size
:canonical: archivebox.core.forms.AddLinkForm.snapshot_max_size
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.snapshot_max_size
```

````

````{py:attribute} delete_after
:canonical: archivebox.core.forms.AddLinkForm.delete_after
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.delete_after
```

````

````{py:attribute} crawl_max_concurrent_snapshots
:canonical: archivebox.core.forms.AddLinkForm.crawl_max_concurrent_snapshots
:value: >
   'IntegerField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.crawl_max_concurrent_snapshots
```

````

````{py:attribute} notes
:canonical: archivebox.core.forms.AddLinkForm.notes
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.notes
```

````

````{py:attribute} url_filters
:canonical: archivebox.core.forms.AddLinkForm.url_filters
:value: >
   'Field(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.url_filters
```

````

````{py:attribute} main_plugins
:canonical: archivebox.core.forms.AddLinkForm.main_plugins
:value: >
   'MultipleChoiceField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.main_plugins
```

````

````{py:attribute} page_setup_plugins
:canonical: archivebox.core.forms.AddLinkForm.page_setup_plugins
:value: >
   'MultipleChoiceField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.page_setup_plugins
```

````

````{py:attribute} media_plugins
:canonical: archivebox.core.forms.AddLinkForm.media_plugins
:value: >
   'MultipleChoiceField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.media_plugins
```

````

````{py:attribute} text_plugins
:canonical: archivebox.core.forms.AddLinkForm.text_plugins
:value: >
   'MultipleChoiceField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.text_plugins
```

````

````{py:attribute} metadata_plugins
:canonical: archivebox.core.forms.AddLinkForm.metadata_plugins
:value: >
   'MultipleChoiceField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.metadata_plugins
```

````

````{py:attribute} postprocessing_plugins
:canonical: archivebox.core.forms.AddLinkForm.postprocessing_plugins
:value: >
   'MultipleChoiceField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.postprocessing_plugins
```

````

````{py:attribute} other_plugins
:canonical: archivebox.core.forms.AddLinkForm.other_plugins
:value: >
   'MultipleChoiceField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.other_plugins
```

````

````{py:attribute} schedule
:canonical: archivebox.core.forms.AddLinkForm.schedule
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.schedule
```

````

````{py:attribute} persona
:canonical: archivebox.core.forms.AddLinkForm.persona
:value: >
   'ModelChoiceField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.persona
```

````

````{py:attribute} permissions
:canonical: archivebox.core.forms.AddLinkForm.permissions
:value: >
   'ChoiceField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.permissions
```

````

````{py:attribute} start_paused
:canonical: archivebox.core.forms.AddLinkForm.start_paused
:value: >
   'BooleanField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.start_paused
```

````

````{py:attribute} config
:canonical: archivebox.core.forms.AddLinkForm.config
:value: >
   'JSONField(...)'

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.config
```

````

````{py:method} clean()
:canonical: archivebox.core.forms.AddLinkForm.clean

````

````{py:method} clean_url()
:canonical: archivebox.core.forms.AddLinkForm.clean_url

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.clean_url
```

````

````{py:method} clean_url_filters()
:canonical: archivebox.core.forms.AddLinkForm.clean_url_filters

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.clean_url_filters
```

````

````{py:method} clean_max_urls()
:canonical: archivebox.core.forms.AddLinkForm.clean_max_urls

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.clean_max_urls
```

````

````{py:method} clean_crawl_max_size()
:canonical: archivebox.core.forms.AddLinkForm.clean_crawl_max_size

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.clean_crawl_max_size
```

````

````{py:method} clean_crawl_timeout()
:canonical: archivebox.core.forms.AddLinkForm.clean_crawl_timeout

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.clean_crawl_timeout
```

````

````{py:method} clean_timeout()
:canonical: archivebox.core.forms.AddLinkForm.clean_timeout

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.clean_timeout
```

````

````{py:method} _clean_timeout_seconds(raw_value, field_label: str, *, blank_value)
:canonical: archivebox.core.forms.AddLinkForm._clean_timeout_seconds

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm._clean_timeout_seconds
```

````

````{py:method} clean_snapshot_max_size()
:canonical: archivebox.core.forms.AddLinkForm.clean_snapshot_max_size

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.clean_snapshot_max_size
```

````

````{py:method} clean_delete_after()
:canonical: archivebox.core.forms.AddLinkForm.clean_delete_after

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.clean_delete_after
```

````

````{py:method} clean_crawl_max_concurrent_snapshots()
:canonical: archivebox.core.forms.AddLinkForm.clean_crawl_max_concurrent_snapshots

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.clean_crawl_max_concurrent_snapshots
```

````

````{py:method} clean_schedule()
:canonical: archivebox.core.forms.AddLinkForm.clean_schedule

```{autodoc2-docstring} archivebox.core.forms.AddLinkForm.clean_schedule
```

````

`````

`````{py:class} TagWidget(attrs=None)
:canonical: archivebox.core.forms.TagWidget

Bases: {py:obj}`django.forms.TextInput`

````{py:method} format_value(value)
:canonical: archivebox.core.forms.TagWidget.format_value

````

`````

`````{py:class} TagField(*, max_length=None, min_length=None, strip=True, empty_value='', **kwargs)
:canonical: archivebox.core.forms.TagField

Bases: {py:obj}`django.forms.CharField`

```{autodoc2-docstring} archivebox.core.forms.TagField
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.core.forms.TagField.__init__
```

````{py:attribute} widget
:canonical: archivebox.core.forms.TagField.widget
:value: >
   None

```{autodoc2-docstring} archivebox.core.forms.TagField.widget
```

````

````{py:method} clean(value)
:canonical: archivebox.core.forms.TagField.clean

````

````{py:method} has_changed(initial, data)
:canonical: archivebox.core.forms.TagField.has_changed

````

`````
