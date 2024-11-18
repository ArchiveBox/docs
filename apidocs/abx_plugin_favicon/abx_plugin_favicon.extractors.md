# {py:mod}`abx_plugin_favicon.extractors`

```{py:module} abx_plugin_favicon.extractors
```

```{autodoc2-docstring} abx_plugin_favicon.extractors
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`FaviconExtractor <abx_plugin_favicon.extractors.FaviconExtractor>`
  - ```{autodoc2-docstring} abx_plugin_favicon.extractors.FaviconExtractor
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`FAVICON_EXTRACTOR <abx_plugin_favicon.extractors.FAVICON_EXTRACTOR>`
  - ```{autodoc2-docstring} abx_plugin_favicon.extractors.FAVICON_EXTRACTOR
    :summary:
    ```
````

### API

`````{py:class} FaviconExtractor
:canonical: abx_plugin_favicon.extractors.FaviconExtractor

Bases: {py:obj}`abx_spec_extractor.BaseExtractor`

```{autodoc2-docstring} abx_plugin_favicon.extractors.FaviconExtractor
```

````{py:attribute} name
:canonical: abx_plugin_favicon.extractors.FaviconExtractor.name
:type: abx_spec_extractor.ExtractorName
:value: >
   'favicon'

```{autodoc2-docstring} abx_plugin_favicon.extractors.FaviconExtractor.name
```

````

````{py:attribute} binary
:canonical: abx_plugin_favicon.extractors.FaviconExtractor.binary
:type: abx_pkg.BinName
:value: >
   None

```{autodoc2-docstring} abx_plugin_favicon.extractors.FaviconExtractor.binary
```

````

````{py:method} get_output_path(snapshot) -> pathlib.Path | None
:canonical: abx_plugin_favicon.extractors.FaviconExtractor.get_output_path

```{autodoc2-docstring} abx_plugin_favicon.extractors.FaviconExtractor.get_output_path
```

````

`````

````{py:data} FAVICON_EXTRACTOR
:canonical: abx_plugin_favicon.extractors.FAVICON_EXTRACTOR
:value: >
   'FaviconExtractor(...)'

```{autodoc2-docstring} abx_plugin_favicon.extractors.FAVICON_EXTRACTOR
```

````
