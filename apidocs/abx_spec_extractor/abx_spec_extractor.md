# {py:mod}`abx_spec_extractor`

```{py:module} abx_spec_extractor
```

```{autodoc2-docstring} abx_spec_extractor
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseExtractor <abx_spec_extractor.BaseExtractor>`
  - ```{autodoc2-docstring} abx_spec_extractor.BaseExtractor
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`assert_no_empty_args <abx_spec_extractor.assert_no_empty_args>`
  - ```{autodoc2-docstring} abx_spec_extractor.assert_no_empty_args
    :summary:
    ```
* - {py:obj}`get_EXTRACTORS <abx_spec_extractor.get_EXTRACTORS>`
  - ```{autodoc2-docstring} abx_spec_extractor.get_EXTRACTORS
    :summary:
    ```
* - {py:obj}`extract <abx_spec_extractor.extract>`
  - ```{autodoc2-docstring} abx_spec_extractor.extract
    :summary:
    ```
* - {py:obj}`should_extract <abx_spec_extractor.should_extract>`
  - ```{autodoc2-docstring} abx_spec_extractor.should_extract
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__order__ <abx_spec_extractor.__order__>`
  - ```{autodoc2-docstring} abx_spec_extractor.__order__
    :summary:
    ```
* - {py:obj}`ExtractorName <abx_spec_extractor.ExtractorName>`
  - ```{autodoc2-docstring} abx_spec_extractor.ExtractorName
    :summary:
    ```
* - {py:obj}`HandlerFuncStr <abx_spec_extractor.HandlerFuncStr>`
  - ```{autodoc2-docstring} abx_spec_extractor.HandlerFuncStr
    :summary:
    ```
* - {py:obj}`CmdArgsList <abx_spec_extractor.CmdArgsList>`
  - ```{autodoc2-docstring} abx_spec_extractor.CmdArgsList
    :summary:
    ```
````

### API

````{py:data} __order__
:canonical: abx_spec_extractor.__order__
:value: >
   10

```{autodoc2-docstring} abx_spec_extractor.__order__
```

````

````{py:function} assert_no_empty_args(args: typing.List[str]) -> typing.List[str]
:canonical: abx_spec_extractor.assert_no_empty_args

```{autodoc2-docstring} abx_spec_extractor.assert_no_empty_args
```
````

````{py:data} ExtractorName
:canonical: abx_spec_extractor.ExtractorName
:value: >
   None

```{autodoc2-docstring} abx_spec_extractor.ExtractorName
```

````

````{py:data} HandlerFuncStr
:canonical: abx_spec_extractor.HandlerFuncStr
:value: >
   None

```{autodoc2-docstring} abx_spec_extractor.HandlerFuncStr
```

````

````{py:data} CmdArgsList
:canonical: abx_spec_extractor.CmdArgsList
:value: >
   None

```{autodoc2-docstring} abx_spec_extractor.CmdArgsList
```

````

````{py:function} get_EXTRACTORS()
:canonical: abx_spec_extractor.get_EXTRACTORS

```{autodoc2-docstring} abx_spec_extractor.get_EXTRACTORS
```
````

````{py:function} extract(uri: str, config: dict | None = None)
:canonical: abx_spec_extractor.extract

```{autodoc2-docstring} abx_spec_extractor.extract
```
````

````{py:function} should_extract(uri: str, extractor: str, config: dict | None = None)
:canonical: abx_spec_extractor.should_extract

```{autodoc2-docstring} abx_spec_extractor.should_extract
```
````

`````{py:class} BaseExtractor
:canonical: abx_spec_extractor.BaseExtractor

```{autodoc2-docstring} abx_spec_extractor.BaseExtractor
```

````{py:attribute} name
:canonical: abx_spec_extractor.BaseExtractor.name
:type: abx_spec_extractor.ExtractorName
:value: >
   None

```{autodoc2-docstring} abx_spec_extractor.BaseExtractor.name
```

````

````{py:attribute} binary
:canonical: abx_spec_extractor.BaseExtractor.binary
:type: abx_pkg.BinName
:value: >
   None

```{autodoc2-docstring} abx_spec_extractor.BaseExtractor.binary
```

````

````{py:attribute} default_args
:canonical: abx_spec_extractor.BaseExtractor.default_args
:type: abx_spec_extractor.CmdArgsList
:value: >
   []

```{autodoc2-docstring} abx_spec_extractor.BaseExtractor.default_args
```

````

````{py:attribute} extra_args
:canonical: abx_spec_extractor.BaseExtractor.extra_args
:type: abx_spec_extractor.CmdArgsList
:value: >
   []

```{autodoc2-docstring} abx_spec_extractor.BaseExtractor.extra_args
```

````

````{py:method} get_output_path(snapshot) -> pathlib.Path
:canonical: abx_spec_extractor.BaseExtractor.get_output_path

```{autodoc2-docstring} abx_spec_extractor.BaseExtractor.get_output_path
```

````

````{py:method} should_extract(uri: str, config: dict | None = None) -> bool
:canonical: abx_spec_extractor.BaseExtractor.should_extract

```{autodoc2-docstring} abx_spec_extractor.BaseExtractor.should_extract
```

````

````{py:method} exec(args: abx_spec_extractor.CmdArgsList = (), cwd: typing.Optional[pathlib.Path] = None, installed_binary=None)
:canonical: abx_spec_extractor.BaseExtractor.exec

```{autodoc2-docstring} abx_spec_extractor.BaseExtractor.exec
```

````

````{py:property} BINARY
:canonical: abx_spec_extractor.BaseExtractor.BINARY

```{autodoc2-docstring} abx_spec_extractor.BaseExtractor.BINARY
```

````

````{py:method} detect_installed_binary()
:canonical: abx_spec_extractor.BaseExtractor.detect_installed_binary

```{autodoc2-docstring} abx_spec_extractor.BaseExtractor.detect_installed_binary
```

````

````{py:method} load_binary(installed_binary=None)
:canonical: abx_spec_extractor.BaseExtractor.load_binary

```{autodoc2-docstring} abx_spec_extractor.BaseExtractor.load_binary
```

````

`````
