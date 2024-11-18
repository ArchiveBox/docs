# {py:mod}`abx_plugin_mercury.extractors`

```{py:module} abx_plugin_mercury.extractors
```

```{autodoc2-docstring} abx_plugin_mercury.extractors
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`MercuryExtractor <abx_plugin_mercury.extractors.MercuryExtractor>`
  - ```{autodoc2-docstring} abx_plugin_mercury.extractors.MercuryExtractor
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`MERCURY_EXTRACTOR <abx_plugin_mercury.extractors.MERCURY_EXTRACTOR>`
  - ```{autodoc2-docstring} abx_plugin_mercury.extractors.MERCURY_EXTRACTOR
    :summary:
    ```
````

### API

`````{py:class} MercuryExtractor
:canonical: abx_plugin_mercury.extractors.MercuryExtractor

Bases: {py:obj}`abx_spec_extractor.BaseExtractor`

```{autodoc2-docstring} abx_plugin_mercury.extractors.MercuryExtractor
```

````{py:attribute} name
:canonical: abx_plugin_mercury.extractors.MercuryExtractor.name
:type: abx_spec_extractor.ExtractorName
:value: >
   'mercury'

```{autodoc2-docstring} abx_plugin_mercury.extractors.MercuryExtractor.name
```

````

````{py:attribute} binary
:canonical: abx_plugin_mercury.extractors.MercuryExtractor.binary
:type: abx_pkg.BinName
:value: >
   None

```{autodoc2-docstring} abx_plugin_mercury.extractors.MercuryExtractor.binary
```

````

````{py:method} get_output_path(snapshot) -> pathlib.Path | None
:canonical: abx_plugin_mercury.extractors.MercuryExtractor.get_output_path

```{autodoc2-docstring} abx_plugin_mercury.extractors.MercuryExtractor.get_output_path
```

````

`````

````{py:data} MERCURY_EXTRACTOR
:canonical: abx_plugin_mercury.extractors.MERCURY_EXTRACTOR
:value: >
   'MercuryExtractor(...)'

```{autodoc2-docstring} abx_plugin_mercury.extractors.MERCURY_EXTRACTOR
```

````
