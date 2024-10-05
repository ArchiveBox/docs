# {py:mod}`archivebox.api.v1_cli`

```{py:module} archivebox.api.v1_cli
```

```{autodoc2-docstring} archivebox.api.v1_cli
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CLICommandResponseSchema <archivebox.api.v1_cli.CLICommandResponseSchema>`
  -
* - {py:obj}`FilterTypeChoices <archivebox.api.v1_cli.FilterTypeChoices>`
  -
* - {py:obj}`StatusChoices <archivebox.api.v1_cli.StatusChoices>`
  -
* - {py:obj}`AddCommandSchema <archivebox.api.v1_cli.AddCommandSchema>`
  -
* - {py:obj}`UpdateCommandSchema <archivebox.api.v1_cli.UpdateCommandSchema>`
  -
* - {py:obj}`ScheduleCommandSchema <archivebox.api.v1_cli.ScheduleCommandSchema>`
  -
* - {py:obj}`ListCommandSchema <archivebox.api.v1_cli.ListCommandSchema>`
  -
* - {py:obj}`RemoveCommandSchema <archivebox.api.v1_cli.RemoveCommandSchema>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`cli_add <archivebox.api.v1_cli.cli_add>`
  - ```{autodoc2-docstring} archivebox.api.v1_cli.cli_add
    :summary:
    ```
* - {py:obj}`cli_update <archivebox.api.v1_cli.cli_update>`
  - ```{autodoc2-docstring} archivebox.api.v1_cli.cli_update
    :summary:
    ```
* - {py:obj}`cli_schedule <archivebox.api.v1_cli.cli_schedule>`
  - ```{autodoc2-docstring} archivebox.api.v1_cli.cli_schedule
    :summary:
    ```
* - {py:obj}`cli_list <archivebox.api.v1_cli.cli_list>`
  - ```{autodoc2-docstring} archivebox.api.v1_cli.cli_list
    :summary:
    ```
* - {py:obj}`cli_remove <archivebox.api.v1_cli.cli_remove>`
  - ```{autodoc2-docstring} archivebox.api.v1_cli.cli_remove
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.api.v1_cli.__package__>`
  - ```{autodoc2-docstring} archivebox.api.v1_cli.__package__
    :summary:
    ```
* - {py:obj}`router <archivebox.api.v1_cli.router>`
  - ```{autodoc2-docstring} archivebox.api.v1_cli.router
    :summary:
    ```
* - {py:obj}`JSONType <archivebox.api.v1_cli.JSONType>`
  - ```{autodoc2-docstring} archivebox.api.v1_cli.JSONType
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.api.v1_cli.__package__
:value: >
   'archivebox.api'

```{autodoc2-docstring} archivebox.api.v1_cli.__package__
```

````

````{py:data} router
:canonical: archivebox.api.v1_cli.router
:value: >
   'Router(...)'

```{autodoc2-docstring} archivebox.api.v1_cli.router
```

````

````{py:data} JSONType
:canonical: archivebox.api.v1_cli.JSONType
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_cli.JSONType
```

````

`````{py:class} CLICommandResponseSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_cli.CLICommandResponseSchema

Bases: {py:obj}`ninja.Schema`

````{py:attribute} success
:canonical: archivebox.api.v1_cli.CLICommandResponseSchema.success
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_cli.CLICommandResponseSchema.success
```

````

````{py:attribute} errors
:canonical: archivebox.api.v1_cli.CLICommandResponseSchema.errors
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_cli.CLICommandResponseSchema.errors
```

````

````{py:attribute} result
:canonical: archivebox.api.v1_cli.CLICommandResponseSchema.result
:type: archivebox.api.v1_cli.JSONType
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_cli.CLICommandResponseSchema.result
```

````

````{py:attribute} stdout
:canonical: archivebox.api.v1_cli.CLICommandResponseSchema.stdout
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_cli.CLICommandResponseSchema.stdout
```

````

````{py:attribute} stderr
:canonical: archivebox.api.v1_cli.CLICommandResponseSchema.stderr
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_cli.CLICommandResponseSchema.stderr
```

````

`````

`````{py:class} FilterTypeChoices()
:canonical: archivebox.api.v1_cli.FilterTypeChoices

Bases: {py:obj}`str`, {py:obj}`enum.Enum`

````{py:attribute} exact
:canonical: archivebox.api.v1_cli.FilterTypeChoices.exact
:value: >
   'exact'

```{autodoc2-docstring} archivebox.api.v1_cli.FilterTypeChoices.exact
```

````

````{py:attribute} substring
:canonical: archivebox.api.v1_cli.FilterTypeChoices.substring
:value: >
   'substring'

```{autodoc2-docstring} archivebox.api.v1_cli.FilterTypeChoices.substring
```

````

````{py:attribute} regex
:canonical: archivebox.api.v1_cli.FilterTypeChoices.regex
:value: >
   'regex'

```{autodoc2-docstring} archivebox.api.v1_cli.FilterTypeChoices.regex
```

````

````{py:attribute} domain
:canonical: archivebox.api.v1_cli.FilterTypeChoices.domain
:value: >
   'domain'

```{autodoc2-docstring} archivebox.api.v1_cli.FilterTypeChoices.domain
```

````

````{py:attribute} tag
:canonical: archivebox.api.v1_cli.FilterTypeChoices.tag
:value: >
   'tag'

```{autodoc2-docstring} archivebox.api.v1_cli.FilterTypeChoices.tag
```

````

````{py:attribute} timestamp
:canonical: archivebox.api.v1_cli.FilterTypeChoices.timestamp
:value: >
   'timestamp'

```{autodoc2-docstring} archivebox.api.v1_cli.FilterTypeChoices.timestamp
```

````

`````

`````{py:class} StatusChoices()
:canonical: archivebox.api.v1_cli.StatusChoices

Bases: {py:obj}`str`, {py:obj}`enum.Enum`

````{py:attribute} indexed
:canonical: archivebox.api.v1_cli.StatusChoices.indexed
:value: >
   'indexed'

```{autodoc2-docstring} archivebox.api.v1_cli.StatusChoices.indexed
```

````

````{py:attribute} archived
:canonical: archivebox.api.v1_cli.StatusChoices.archived
:value: >
   'archived'

```{autodoc2-docstring} archivebox.api.v1_cli.StatusChoices.archived
```

````

````{py:attribute} unarchived
:canonical: archivebox.api.v1_cli.StatusChoices.unarchived
:value: >
   'unarchived'

```{autodoc2-docstring} archivebox.api.v1_cli.StatusChoices.unarchived
```

````

````{py:attribute} present
:canonical: archivebox.api.v1_cli.StatusChoices.present
:value: >
   'present'

```{autodoc2-docstring} archivebox.api.v1_cli.StatusChoices.present
```

````

````{py:attribute} valid
:canonical: archivebox.api.v1_cli.StatusChoices.valid
:value: >
   'valid'

```{autodoc2-docstring} archivebox.api.v1_cli.StatusChoices.valid
```

````

````{py:attribute} invalid
:canonical: archivebox.api.v1_cli.StatusChoices.invalid
:value: >
   'invalid'

```{autodoc2-docstring} archivebox.api.v1_cli.StatusChoices.invalid
```

````

````{py:attribute} duplicate
:canonical: archivebox.api.v1_cli.StatusChoices.duplicate
:value: >
   'duplicate'

```{autodoc2-docstring} archivebox.api.v1_cli.StatusChoices.duplicate
```

````

````{py:attribute} orphaned
:canonical: archivebox.api.v1_cli.StatusChoices.orphaned
:value: >
   'orphaned'

```{autodoc2-docstring} archivebox.api.v1_cli.StatusChoices.orphaned
```

````

````{py:attribute} corrupted
:canonical: archivebox.api.v1_cli.StatusChoices.corrupted
:value: >
   'corrupted'

```{autodoc2-docstring} archivebox.api.v1_cli.StatusChoices.corrupted
```

````

````{py:attribute} unrecognized
:canonical: archivebox.api.v1_cli.StatusChoices.unrecognized
:value: >
   'unrecognized'

```{autodoc2-docstring} archivebox.api.v1_cli.StatusChoices.unrecognized
```

````

`````

`````{py:class} AddCommandSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_cli.AddCommandSchema

Bases: {py:obj}`ninja.Schema`

````{py:attribute} urls
:canonical: archivebox.api.v1_cli.AddCommandSchema.urls
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_cli.AddCommandSchema.urls
```

````

````{py:attribute} tag
:canonical: archivebox.api.v1_cli.AddCommandSchema.tag
:type: str
:value: <Multiline-String>

```{autodoc2-docstring} archivebox.api.v1_cli.AddCommandSchema.tag
```

````

````{py:attribute} depth
:canonical: archivebox.api.v1_cli.AddCommandSchema.depth
:type: int
:value: >
   0

```{autodoc2-docstring} archivebox.api.v1_cli.AddCommandSchema.depth
```

````

````{py:attribute} update
:canonical: archivebox.api.v1_cli.AddCommandSchema.update
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_cli.AddCommandSchema.update
```

````

````{py:attribute} update_all
:canonical: archivebox.api.v1_cli.AddCommandSchema.update_all
:type: bool
:value: >
   False

```{autodoc2-docstring} archivebox.api.v1_cli.AddCommandSchema.update_all
```

````

````{py:attribute} index_only
:canonical: archivebox.api.v1_cli.AddCommandSchema.index_only
:type: bool
:value: >
   False

```{autodoc2-docstring} archivebox.api.v1_cli.AddCommandSchema.index_only
```

````

````{py:attribute} overwrite
:canonical: archivebox.api.v1_cli.AddCommandSchema.overwrite
:type: bool
:value: >
   False

```{autodoc2-docstring} archivebox.api.v1_cli.AddCommandSchema.overwrite
```

````

````{py:attribute} init
:canonical: archivebox.api.v1_cli.AddCommandSchema.init
:type: bool
:value: >
   False

```{autodoc2-docstring} archivebox.api.v1_cli.AddCommandSchema.init
```

````

````{py:attribute} extractors
:canonical: archivebox.api.v1_cli.AddCommandSchema.extractors
:type: str
:value: <Multiline-String>

```{autodoc2-docstring} archivebox.api.v1_cli.AddCommandSchema.extractors
```

````

````{py:attribute} parser
:canonical: archivebox.api.v1_cli.AddCommandSchema.parser
:type: str
:value: >
   'auto'

```{autodoc2-docstring} archivebox.api.v1_cli.AddCommandSchema.parser
```

````

`````

`````{py:class} UpdateCommandSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_cli.UpdateCommandSchema

Bases: {py:obj}`ninja.Schema`

````{py:attribute} resume
:canonical: archivebox.api.v1_cli.UpdateCommandSchema.resume
:type: typing.Optional[float]
:value: >
   0

```{autodoc2-docstring} archivebox.api.v1_cli.UpdateCommandSchema.resume
```

````

````{py:attribute} only_new
:canonical: archivebox.api.v1_cli.UpdateCommandSchema.only_new
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_cli.UpdateCommandSchema.only_new
```

````

````{py:attribute} index_only
:canonical: archivebox.api.v1_cli.UpdateCommandSchema.index_only
:type: bool
:value: >
   False

```{autodoc2-docstring} archivebox.api.v1_cli.UpdateCommandSchema.index_only
```

````

````{py:attribute} overwrite
:canonical: archivebox.api.v1_cli.UpdateCommandSchema.overwrite
:type: bool
:value: >
   False

```{autodoc2-docstring} archivebox.api.v1_cli.UpdateCommandSchema.overwrite
```

````

````{py:attribute} after
:canonical: archivebox.api.v1_cli.UpdateCommandSchema.after
:type: typing.Optional[float]
:value: >
   0

```{autodoc2-docstring} archivebox.api.v1_cli.UpdateCommandSchema.after
```

````

````{py:attribute} before
:canonical: archivebox.api.v1_cli.UpdateCommandSchema.before
:type: typing.Optional[float]
:value: >
   999999999999999

```{autodoc2-docstring} archivebox.api.v1_cli.UpdateCommandSchema.before
```

````

````{py:attribute} status
:canonical: archivebox.api.v1_cli.UpdateCommandSchema.status
:type: typing.Optional[archivebox.api.v1_cli.StatusChoices]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_cli.UpdateCommandSchema.status
```

````

````{py:attribute} filter_type
:canonical: archivebox.api.v1_cli.UpdateCommandSchema.filter_type
:type: typing.Optional[str]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_cli.UpdateCommandSchema.filter_type
```

````

````{py:attribute} filter_patterns
:canonical: archivebox.api.v1_cli.UpdateCommandSchema.filter_patterns
:type: typing.Optional[typing.List[str]]
:value: >
   ['https://example.com']

```{autodoc2-docstring} archivebox.api.v1_cli.UpdateCommandSchema.filter_patterns
```

````

````{py:attribute} extractors
:canonical: archivebox.api.v1_cli.UpdateCommandSchema.extractors
:type: typing.Optional[str]
:value: <Multiline-String>

```{autodoc2-docstring} archivebox.api.v1_cli.UpdateCommandSchema.extractors
```

````

`````

`````{py:class} ScheduleCommandSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_cli.ScheduleCommandSchema

Bases: {py:obj}`ninja.Schema`

````{py:attribute} import_path
:canonical: archivebox.api.v1_cli.ScheduleCommandSchema.import_path
:type: typing.Optional[str]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_cli.ScheduleCommandSchema.import_path
```

````

````{py:attribute} add
:canonical: archivebox.api.v1_cli.ScheduleCommandSchema.add
:type: bool
:value: >
   False

```{autodoc2-docstring} archivebox.api.v1_cli.ScheduleCommandSchema.add
```

````

````{py:attribute} every
:canonical: archivebox.api.v1_cli.ScheduleCommandSchema.every
:type: typing.Optional[str]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_cli.ScheduleCommandSchema.every
```

````

````{py:attribute} tag
:canonical: archivebox.api.v1_cli.ScheduleCommandSchema.tag
:type: str
:value: <Multiline-String>

```{autodoc2-docstring} archivebox.api.v1_cli.ScheduleCommandSchema.tag
```

````

````{py:attribute} depth
:canonical: archivebox.api.v1_cli.ScheduleCommandSchema.depth
:type: int
:value: >
   0

```{autodoc2-docstring} archivebox.api.v1_cli.ScheduleCommandSchema.depth
```

````

````{py:attribute} overwrite
:canonical: archivebox.api.v1_cli.ScheduleCommandSchema.overwrite
:type: bool
:value: >
   False

```{autodoc2-docstring} archivebox.api.v1_cli.ScheduleCommandSchema.overwrite
```

````

````{py:attribute} update
:canonical: archivebox.api.v1_cli.ScheduleCommandSchema.update
:type: bool
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_cli.ScheduleCommandSchema.update
```

````

````{py:attribute} clear
:canonical: archivebox.api.v1_cli.ScheduleCommandSchema.clear
:type: bool
:value: >
   False

```{autodoc2-docstring} archivebox.api.v1_cli.ScheduleCommandSchema.clear
```

````

`````

`````{py:class} ListCommandSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_cli.ListCommandSchema

Bases: {py:obj}`ninja.Schema`

````{py:attribute} filter_patterns
:canonical: archivebox.api.v1_cli.ListCommandSchema.filter_patterns
:type: typing.Optional[typing.List[str]]
:value: >
   ['https://example.com']

```{autodoc2-docstring} archivebox.api.v1_cli.ListCommandSchema.filter_patterns
```

````

````{py:attribute} filter_type
:canonical: archivebox.api.v1_cli.ListCommandSchema.filter_type
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_cli.ListCommandSchema.filter_type
```

````

````{py:attribute} status
:canonical: archivebox.api.v1_cli.ListCommandSchema.status
:type: typing.Optional[archivebox.api.v1_cli.StatusChoices]
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_cli.ListCommandSchema.status
```

````

````{py:attribute} after
:canonical: archivebox.api.v1_cli.ListCommandSchema.after
:type: typing.Optional[float]
:value: >
   0

```{autodoc2-docstring} archivebox.api.v1_cli.ListCommandSchema.after
```

````

````{py:attribute} before
:canonical: archivebox.api.v1_cli.ListCommandSchema.before
:type: typing.Optional[float]
:value: >
   999999999999999

```{autodoc2-docstring} archivebox.api.v1_cli.ListCommandSchema.before
```

````

````{py:attribute} sort
:canonical: archivebox.api.v1_cli.ListCommandSchema.sort
:type: str
:value: >
   'bookmarked_at'

```{autodoc2-docstring} archivebox.api.v1_cli.ListCommandSchema.sort
```

````

````{py:attribute} as_json
:canonical: archivebox.api.v1_cli.ListCommandSchema.as_json
:type: bool
:value: >
   True

```{autodoc2-docstring} archivebox.api.v1_cli.ListCommandSchema.as_json
```

````

````{py:attribute} as_html
:canonical: archivebox.api.v1_cli.ListCommandSchema.as_html
:type: bool
:value: >
   False

```{autodoc2-docstring} archivebox.api.v1_cli.ListCommandSchema.as_html
```

````

````{py:attribute} as_csv
:canonical: archivebox.api.v1_cli.ListCommandSchema.as_csv
:type: str | bool
:value: >
   'timestamp,url'

```{autodoc2-docstring} archivebox.api.v1_cli.ListCommandSchema.as_csv
```

````

````{py:attribute} with_headers
:canonical: archivebox.api.v1_cli.ListCommandSchema.with_headers
:type: bool
:value: >
   False

```{autodoc2-docstring} archivebox.api.v1_cli.ListCommandSchema.with_headers
```

````

`````

`````{py:class} RemoveCommandSchema(/, **data: typing.Any)
:canonical: archivebox.api.v1_cli.RemoveCommandSchema

Bases: {py:obj}`ninja.Schema`

````{py:attribute} delete
:canonical: archivebox.api.v1_cli.RemoveCommandSchema.delete
:type: bool
:value: >
   True

```{autodoc2-docstring} archivebox.api.v1_cli.RemoveCommandSchema.delete
```

````

````{py:attribute} after
:canonical: archivebox.api.v1_cli.RemoveCommandSchema.after
:type: typing.Optional[float]
:value: >
   0

```{autodoc2-docstring} archivebox.api.v1_cli.RemoveCommandSchema.after
```

````

````{py:attribute} before
:canonical: archivebox.api.v1_cli.RemoveCommandSchema.before
:type: typing.Optional[float]
:value: >
   999999999999999

```{autodoc2-docstring} archivebox.api.v1_cli.RemoveCommandSchema.before
```

````

````{py:attribute} filter_type
:canonical: archivebox.api.v1_cli.RemoveCommandSchema.filter_type
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.api.v1_cli.RemoveCommandSchema.filter_type
```

````

````{py:attribute} filter_patterns
:canonical: archivebox.api.v1_cli.RemoveCommandSchema.filter_patterns
:type: typing.Optional[typing.List[str]]
:value: >
   ['https://example.com']

```{autodoc2-docstring} archivebox.api.v1_cli.RemoveCommandSchema.filter_patterns
```

````

`````

````{py:function} cli_add(request, args: archivebox.api.v1_cli.AddCommandSchema)
:canonical: archivebox.api.v1_cli.cli_add

```{autodoc2-docstring} archivebox.api.v1_cli.cli_add
```
````

````{py:function} cli_update(request, args: archivebox.api.v1_cli.UpdateCommandSchema)
:canonical: archivebox.api.v1_cli.cli_update

```{autodoc2-docstring} archivebox.api.v1_cli.cli_update
```
````

````{py:function} cli_schedule(request, args: archivebox.api.v1_cli.ScheduleCommandSchema)
:canonical: archivebox.api.v1_cli.cli_schedule

```{autodoc2-docstring} archivebox.api.v1_cli.cli_schedule
```
````

````{py:function} cli_list(request, args: archivebox.api.v1_cli.ListCommandSchema)
:canonical: archivebox.api.v1_cli.cli_list

```{autodoc2-docstring} archivebox.api.v1_cli.cli_list
```
````

````{py:function} cli_remove(request, args: archivebox.api.v1_cli.RemoveCommandSchema)
:canonical: archivebox.api.v1_cli.cli_remove

```{autodoc2-docstring} archivebox.api.v1_cli.cli_remove
```
````
