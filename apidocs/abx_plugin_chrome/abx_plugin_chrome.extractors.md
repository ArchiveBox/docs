# {py:mod}`abx_plugin_chrome.extractors`

```{py:module} abx_plugin_chrome.extractors
```

```{autodoc2-docstring} abx_plugin_chrome.extractors
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PDFExtractor <abx_plugin_chrome.extractors.PDFExtractor>`
  - ```{autodoc2-docstring} abx_plugin_chrome.extractors.PDFExtractor
    :summary:
    ```
* - {py:obj}`ScreenshotExtractor <abx_plugin_chrome.extractors.ScreenshotExtractor>`
  - ```{autodoc2-docstring} abx_plugin_chrome.extractors.ScreenshotExtractor
    :summary:
    ```
* - {py:obj}`DOMExtractor <abx_plugin_chrome.extractors.DOMExtractor>`
  - ```{autodoc2-docstring} abx_plugin_chrome.extractors.DOMExtractor
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PDF_EXTRACTOR <abx_plugin_chrome.extractors.PDF_EXTRACTOR>`
  - ```{autodoc2-docstring} abx_plugin_chrome.extractors.PDF_EXTRACTOR
    :summary:
    ```
* - {py:obj}`SCREENSHOT_EXTRACTOR <abx_plugin_chrome.extractors.SCREENSHOT_EXTRACTOR>`
  - ```{autodoc2-docstring} abx_plugin_chrome.extractors.SCREENSHOT_EXTRACTOR
    :summary:
    ```
* - {py:obj}`DOM_EXTRACTOR <abx_plugin_chrome.extractors.DOM_EXTRACTOR>`
  - ```{autodoc2-docstring} abx_plugin_chrome.extractors.DOM_EXTRACTOR
    :summary:
    ```
````

### API

`````{py:class} PDFExtractor
:canonical: abx_plugin_chrome.extractors.PDFExtractor

Bases: {py:obj}`abx_spec_extractor.BaseExtractor`

```{autodoc2-docstring} abx_plugin_chrome.extractors.PDFExtractor
```

````{py:attribute} name
:canonical: abx_plugin_chrome.extractors.PDFExtractor.name
:type: abx_spec_extractor.ExtractorName
:value: >
   'pdf'

```{autodoc2-docstring} abx_plugin_chrome.extractors.PDFExtractor.name
```

````

````{py:attribute} binary
:canonical: abx_plugin_chrome.extractors.PDFExtractor.binary
:type: abx_pkg.BinName
:value: >
   None

```{autodoc2-docstring} abx_plugin_chrome.extractors.PDFExtractor.binary
```

````

`````

````{py:data} PDF_EXTRACTOR
:canonical: abx_plugin_chrome.extractors.PDF_EXTRACTOR
:value: >
   'PDFExtractor(...)'

```{autodoc2-docstring} abx_plugin_chrome.extractors.PDF_EXTRACTOR
```

````

`````{py:class} ScreenshotExtractor
:canonical: abx_plugin_chrome.extractors.ScreenshotExtractor

Bases: {py:obj}`abx_spec_extractor.BaseExtractor`

```{autodoc2-docstring} abx_plugin_chrome.extractors.ScreenshotExtractor
```

````{py:attribute} name
:canonical: abx_plugin_chrome.extractors.ScreenshotExtractor.name
:type: abx_spec_extractor.ExtractorName
:value: >
   'screenshot'

```{autodoc2-docstring} abx_plugin_chrome.extractors.ScreenshotExtractor.name
```

````

````{py:attribute} binary
:canonical: abx_plugin_chrome.extractors.ScreenshotExtractor.binary
:type: abx_pkg.BinName
:value: >
   None

```{autodoc2-docstring} abx_plugin_chrome.extractors.ScreenshotExtractor.binary
```

````

`````

````{py:data} SCREENSHOT_EXTRACTOR
:canonical: abx_plugin_chrome.extractors.SCREENSHOT_EXTRACTOR
:value: >
   'ScreenshotExtractor(...)'

```{autodoc2-docstring} abx_plugin_chrome.extractors.SCREENSHOT_EXTRACTOR
```

````

`````{py:class} DOMExtractor
:canonical: abx_plugin_chrome.extractors.DOMExtractor

Bases: {py:obj}`abx_spec_extractor.BaseExtractor`

```{autodoc2-docstring} abx_plugin_chrome.extractors.DOMExtractor
```

````{py:attribute} name
:canonical: abx_plugin_chrome.extractors.DOMExtractor.name
:type: abx_spec_extractor.ExtractorName
:value: >
   'dom'

```{autodoc2-docstring} abx_plugin_chrome.extractors.DOMExtractor.name
```

````

````{py:attribute} binary
:canonical: abx_plugin_chrome.extractors.DOMExtractor.binary
:type: abx_pkg.BinName
:value: >
   None

```{autodoc2-docstring} abx_plugin_chrome.extractors.DOMExtractor.binary
```

````

`````

````{py:data} DOM_EXTRACTOR
:canonical: abx_plugin_chrome.extractors.DOM_EXTRACTOR
:value: >
   'DOMExtractor(...)'

```{autodoc2-docstring} abx_plugin_chrome.extractors.DOM_EXTRACTOR
```

````
