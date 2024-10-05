# {py:mod}`archivebox.extractors.favicon`

```{py:module} archivebox.extractors.favicon
```

```{autodoc2-docstring} archivebox.extractors.favicon
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`should_save_favicon <archivebox.extractors.favicon.should_save_favicon>`
  - ```{autodoc2-docstring} archivebox.extractors.favicon.should_save_favicon
    :summary:
    ```
* - {py:obj}`get_output_path <archivebox.extractors.favicon.get_output_path>`
  - ```{autodoc2-docstring} archivebox.extractors.favicon.get_output_path
    :summary:
    ```
* - {py:obj}`save_favicon <archivebox.extractors.favicon.save_favicon>`
  - ```{autodoc2-docstring} archivebox.extractors.favicon.save_favicon
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.extractors.favicon.__package__>`
  - ```{autodoc2-docstring} archivebox.extractors.favicon.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.extractors.favicon.__package__
:value: >
   'archivebox.extractors'

```{autodoc2-docstring} archivebox.extractors.favicon.__package__
```

````

````{py:function} should_save_favicon(link: archivebox.index.schema.Link, out_dir: str | pathlib.Path | None = None, overwrite: bool = False) -> bool
:canonical: archivebox.extractors.favicon.should_save_favicon

```{autodoc2-docstring} archivebox.extractors.favicon.should_save_favicon
```
````

````{py:function} get_output_path()
:canonical: archivebox.extractors.favicon.get_output_path

```{autodoc2-docstring} archivebox.extractors.favicon.get_output_path
```
````

````{py:function} save_favicon(link: archivebox.index.schema.Link, out_dir: str | pathlib.Path | None = None, timeout: int = CURL_CONFIG.CURL_TIMEOUT) -> archivebox.index.schema.ArchiveResult
:canonical: archivebox.extractors.favicon.save_favicon

```{autodoc2-docstring} archivebox.extractors.favicon.save_favicon
```
````
