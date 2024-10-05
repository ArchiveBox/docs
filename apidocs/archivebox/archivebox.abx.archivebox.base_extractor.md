# {py:mod}`archivebox.abx.archivebox.base_extractor`

```{py:module} archivebox.abx.archivebox.base_extractor
```

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseExtractor <archivebox.abx.archivebox.base_extractor.BaseExtractor>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`no_empty_args <archivebox.abx.archivebox.base_extractor.no_empty_args>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.no_empty_args
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.abx.archivebox.base_extractor.__package__>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.__package__
    :summary:
    ```
* - {py:obj}`ExtractorName <archivebox.abx.archivebox.base_extractor.ExtractorName>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.ExtractorName
    :summary:
    ```
* - {py:obj}`HandlerFuncStr <archivebox.abx.archivebox.base_extractor.HandlerFuncStr>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.HandlerFuncStr
    :summary:
    ```
* - {py:obj}`CmdArgsList <archivebox.abx.archivebox.base_extractor.CmdArgsList>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.CmdArgsList
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.abx.archivebox.base_extractor.__package__
:value: >
   'abx.archivebox'

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.__package__
```

````

````{py:function} no_empty_args(args: typing.List[str]) -> typing.List[str]
:canonical: archivebox.abx.archivebox.base_extractor.no_empty_args

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.no_empty_args
```
````

````{py:data} ExtractorName
:canonical: archivebox.abx.archivebox.base_extractor.ExtractorName
:value: >
   None

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.ExtractorName
```

````

````{py:data} HandlerFuncStr
:canonical: archivebox.abx.archivebox.base_extractor.HandlerFuncStr
:value: >
   None

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.HandlerFuncStr
```

````

````{py:data} CmdArgsList
:canonical: archivebox.abx.archivebox.base_extractor.CmdArgsList
:value: >
   None

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.CmdArgsList
```

````

`````{py:class} BaseExtractor(/, **data: typing.Any)
:canonical: archivebox.abx.archivebox.base_extractor.BaseExtractor

Bases: {py:obj}`archivebox.abx.archivebox.base_hook.BaseHook`

````{py:attribute} hook_type
:canonical: archivebox.abx.archivebox.base_extractor.BaseExtractor.hook_type
:type: archivebox.abx.archivebox.base_hook.HookType
:value: >
   'EXTRACTOR'

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.BaseExtractor.hook_type
```

````

````{py:attribute} name
:canonical: archivebox.abx.archivebox.base_extractor.BaseExtractor.name
:type: archivebox.abx.archivebox.base_extractor.ExtractorName
:value: >
   None

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.BaseExtractor.name
```

````

````{py:attribute} binary
:canonical: archivebox.abx.archivebox.base_extractor.BaseExtractor.binary
:type: pydantic_pkgr.BinName
:value: >
   None

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.BaseExtractor.binary
```

````

````{py:attribute} output_path_func
:canonical: archivebox.abx.archivebox.base_extractor.BaseExtractor.output_path_func
:type: archivebox.abx.archivebox.base_extractor.HandlerFuncStr
:value: >
   'self.get_output_path'

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.BaseExtractor.output_path_func
```

````

````{py:attribute} should_extract_func
:canonical: archivebox.abx.archivebox.base_extractor.BaseExtractor.should_extract_func
:type: archivebox.abx.archivebox.base_extractor.HandlerFuncStr
:value: >
   'self.should_extract'

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.BaseExtractor.should_extract_func
```

````

````{py:attribute} extract_func
:canonical: archivebox.abx.archivebox.base_extractor.BaseExtractor.extract_func
:type: archivebox.abx.archivebox.base_extractor.HandlerFuncStr
:value: >
   'self.extract'

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.BaseExtractor.extract_func
```

````

````{py:attribute} exec_func
:canonical: archivebox.abx.archivebox.base_extractor.BaseExtractor.exec_func
:type: archivebox.abx.archivebox.base_extractor.HandlerFuncStr
:value: >
   'self.exec'

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.BaseExtractor.exec_func
```

````

````{py:attribute} default_args
:canonical: archivebox.abx.archivebox.base_extractor.BaseExtractor.default_args
:type: archivebox.abx.archivebox.base_extractor.CmdArgsList
:value: >
   []

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.BaseExtractor.default_args
```

````

````{py:attribute} extra_args
:canonical: archivebox.abx.archivebox.base_extractor.BaseExtractor.extra_args
:type: archivebox.abx.archivebox.base_extractor.CmdArgsList
:value: >
   []

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.BaseExtractor.extra_args
```

````

````{py:attribute} args
:canonical: archivebox.abx.archivebox.base_extractor.BaseExtractor.args
:type: typing.Optional[archivebox.abx.archivebox.base_extractor.CmdArgsList]
:value: >
   None

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.BaseExtractor.args
```

````

````{py:method} validate_model() -> typing_extensions.Self
:canonical: archivebox.abx.archivebox.base_extractor.BaseExtractor.validate_model

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.BaseExtractor.validate_model
```

````

````{py:method} get_output_path(snapshot) -> pathlib.Path
:canonical: archivebox.abx.archivebox.base_extractor.BaseExtractor.get_output_path

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.BaseExtractor.get_output_path
```

````

````{py:method} should_extract(snapshot) -> bool
:canonical: archivebox.abx.archivebox.base_extractor.BaseExtractor.should_extract

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.BaseExtractor.should_extract
```

````

````{py:method} extract(snapshot_id: str) -> typing.Dict[str, typing.Any]
:canonical: archivebox.abx.archivebox.base_extractor.BaseExtractor.extract

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.BaseExtractor.extract
```

````

````{py:method} exec(args: archivebox.abx.archivebox.base_extractor.CmdArgsList = (), cwd: typing.Optional[pathlib.Path] = None, installed_binary=None)
:canonical: archivebox.abx.archivebox.base_extractor.BaseExtractor.exec

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.BaseExtractor.exec
```

````

````{py:method} BINARY() -> archivebox.abx.archivebox.base_binary.BaseBinary
:canonical: archivebox.abx.archivebox.base_extractor.BaseExtractor.BINARY

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.BaseExtractor.BINARY
```

````

````{py:method} detect_installed_binary()
:canonical: archivebox.abx.archivebox.base_extractor.BaseExtractor.detect_installed_binary

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.BaseExtractor.detect_installed_binary
```

````

````{py:method} load_binary(installed_binary=None) -> archivebox.abx.archivebox.base_binary.BaseBinary
:canonical: archivebox.abx.archivebox.base_extractor.BaseExtractor.load_binary

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.BaseExtractor.load_binary
```

````

````{py:method} detect_network_interface()
:canonical: archivebox.abx.archivebox.base_extractor.BaseExtractor.detect_network_interface

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.BaseExtractor.detect_network_interface
```

````

````{py:method} get_EXTRACTORS()
:canonical: archivebox.abx.archivebox.base_extractor.BaseExtractor.get_EXTRACTORS

```{autodoc2-docstring} archivebox.abx.archivebox.base_extractor.BaseExtractor.get_EXTRACTORS
```

````

`````
