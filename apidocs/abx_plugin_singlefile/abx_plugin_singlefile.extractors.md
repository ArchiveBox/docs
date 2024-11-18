# {py:mod}`abx_plugin_singlefile.extractors`

```{py:module} abx_plugin_singlefile.extractors
```

```{autodoc2-docstring} abx_plugin_singlefile.extractors
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SinglefileExtractor <abx_plugin_singlefile.extractors.SinglefileExtractor>`
  - ```{autodoc2-docstring} abx_plugin_singlefile.extractors.SinglefileExtractor
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SINGLEFILE_EXTRACTOR <abx_plugin_singlefile.extractors.SINGLEFILE_EXTRACTOR>`
  - ```{autodoc2-docstring} abx_plugin_singlefile.extractors.SINGLEFILE_EXTRACTOR
    :summary:
    ```
````

### API

`````{py:class} SinglefileExtractor
:canonical: abx_plugin_singlefile.extractors.SinglefileExtractor

Bases: {py:obj}`abx_spec_extractor.BaseExtractor`

```{autodoc2-docstring} abx_plugin_singlefile.extractors.SinglefileExtractor
```

````{py:attribute} name
:canonical: abx_plugin_singlefile.extractors.SinglefileExtractor.name
:type: abx_spec_extractor.ExtractorName
:value: >
   'singlefile'

```{autodoc2-docstring} abx_plugin_singlefile.extractors.SinglefileExtractor.name
```

````

````{py:attribute} binary
:canonical: abx_plugin_singlefile.extractors.SinglefileExtractor.binary
:type: abx_pkg.BinName
:value: >
   None

```{autodoc2-docstring} abx_plugin_singlefile.extractors.SinglefileExtractor.binary
```

````

````{py:method} get_output_path(snapshot) -> pathlib.Path
:canonical: abx_plugin_singlefile.extractors.SinglefileExtractor.get_output_path

```{autodoc2-docstring} abx_plugin_singlefile.extractors.SinglefileExtractor.get_output_path
```

````

`````

````{py:data} SINGLEFILE_EXTRACTOR
:canonical: abx_plugin_singlefile.extractors.SINGLEFILE_EXTRACTOR
:value: >
   'SinglefileExtractor(...)'

```{autodoc2-docstring} abx_plugin_singlefile.extractors.SINGLEFILE_EXTRACTOR
```

````
