# {py:mod}`abx_plugin_git.extractors`

```{py:module} abx_plugin_git.extractors
```

```{autodoc2-docstring} abx_plugin_git.extractors
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`GitExtractor <abx_plugin_git.extractors.GitExtractor>`
  - ```{autodoc2-docstring} abx_plugin_git.extractors.GitExtractor
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`GIT_EXTRACTOR <abx_plugin_git.extractors.GIT_EXTRACTOR>`
  - ```{autodoc2-docstring} abx_plugin_git.extractors.GIT_EXTRACTOR
    :summary:
    ```
````

### API

`````{py:class} GitExtractor
:canonical: abx_plugin_git.extractors.GitExtractor

Bases: {py:obj}`abx_spec_extractor.BaseExtractor`

```{autodoc2-docstring} abx_plugin_git.extractors.GitExtractor
```

````{py:attribute} name
:canonical: abx_plugin_git.extractors.GitExtractor.name
:type: abx_spec_extractor.ExtractorName
:value: >
   'git'

```{autodoc2-docstring} abx_plugin_git.extractors.GitExtractor.name
```

````

````{py:attribute} binary
:canonical: abx_plugin_git.extractors.GitExtractor.binary
:type: abx_pkg.BinName
:value: >
   None

```{autodoc2-docstring} abx_plugin_git.extractors.GitExtractor.binary
```

````

````{py:method} get_output_path(snapshot) -> pathlib.Path | None
:canonical: abx_plugin_git.extractors.GitExtractor.get_output_path

```{autodoc2-docstring} abx_plugin_git.extractors.GitExtractor.get_output_path
```

````

`````

````{py:data} GIT_EXTRACTOR
:canonical: abx_plugin_git.extractors.GIT_EXTRACTOR
:value: >
   'GitExtractor(...)'

```{autodoc2-docstring} abx_plugin_git.extractors.GIT_EXTRACTOR
```

````
