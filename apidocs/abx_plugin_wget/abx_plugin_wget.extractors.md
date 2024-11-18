# {py:mod}`abx_plugin_wget.extractors`

```{py:module} abx_plugin_wget.extractors
```

```{autodoc2-docstring} abx_plugin_wget.extractors
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`WgetExtractor <abx_plugin_wget.extractors.WgetExtractor>`
  - ```{autodoc2-docstring} abx_plugin_wget.extractors.WgetExtractor
    :summary:
    ```
* - {py:obj}`WarcExtractor <abx_plugin_wget.extractors.WarcExtractor>`
  - ```{autodoc2-docstring} abx_plugin_wget.extractors.WarcExtractor
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`WGET_EXTRACTOR <abx_plugin_wget.extractors.WGET_EXTRACTOR>`
  - ```{autodoc2-docstring} abx_plugin_wget.extractors.WGET_EXTRACTOR
    :summary:
    ```
* - {py:obj}`WARC_EXTRACTOR <abx_plugin_wget.extractors.WARC_EXTRACTOR>`
  - ```{autodoc2-docstring} abx_plugin_wget.extractors.WARC_EXTRACTOR
    :summary:
    ```
````

### API

`````{py:class} WgetExtractor
:canonical: abx_plugin_wget.extractors.WgetExtractor

Bases: {py:obj}`abx_spec_extractor.BaseExtractor`

```{autodoc2-docstring} abx_plugin_wget.extractors.WgetExtractor
```

````{py:attribute} name
:canonical: abx_plugin_wget.extractors.WgetExtractor.name
:type: abx_spec_extractor.ExtractorName
:value: >
   'wget'

```{autodoc2-docstring} abx_plugin_wget.extractors.WgetExtractor.name
```

````

````{py:attribute} binary
:canonical: abx_plugin_wget.extractors.WgetExtractor.binary
:type: abx_pkg.BinName
:value: >
   None

```{autodoc2-docstring} abx_plugin_wget.extractors.WgetExtractor.binary
```

````

````{py:method} get_output_path(snapshot) -> pathlib.Path | None
:canonical: abx_plugin_wget.extractors.WgetExtractor.get_output_path

```{autodoc2-docstring} abx_plugin_wget.extractors.WgetExtractor.get_output_path
```

````

`````

````{py:data} WGET_EXTRACTOR
:canonical: abx_plugin_wget.extractors.WGET_EXTRACTOR
:value: >
   'WgetExtractor(...)'

```{autodoc2-docstring} abx_plugin_wget.extractors.WGET_EXTRACTOR
```

````

`````{py:class} WarcExtractor
:canonical: abx_plugin_wget.extractors.WarcExtractor

Bases: {py:obj}`abx_spec_extractor.BaseExtractor`

```{autodoc2-docstring} abx_plugin_wget.extractors.WarcExtractor
```

````{py:attribute} name
:canonical: abx_plugin_wget.extractors.WarcExtractor.name
:type: abx_spec_extractor.ExtractorName
:value: >
   'warc'

```{autodoc2-docstring} abx_plugin_wget.extractors.WarcExtractor.name
```

````

````{py:attribute} binary
:canonical: abx_plugin_wget.extractors.WarcExtractor.binary
:type: abx_pkg.BinName
:value: >
   None

```{autodoc2-docstring} abx_plugin_wget.extractors.WarcExtractor.binary
```

````

````{py:method} get_output_path(snapshot) -> pathlib.Path | None
:canonical: abx_plugin_wget.extractors.WarcExtractor.get_output_path

```{autodoc2-docstring} abx_plugin_wget.extractors.WarcExtractor.get_output_path
```

````

`````

````{py:data} WARC_EXTRACTOR
:canonical: abx_plugin_wget.extractors.WARC_EXTRACTOR
:value: >
   'WarcExtractor(...)'

```{autodoc2-docstring} abx_plugin_wget.extractors.WARC_EXTRACTOR
```

````
