# {py:mod}`archivebox.extractors.archive_org`

```{py:module} archivebox.extractors.archive_org
```

```{autodoc2-docstring} archivebox.extractors.archive_org
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_output_path <archivebox.extractors.archive_org.get_output_path>`
  - ```{autodoc2-docstring} archivebox.extractors.archive_org.get_output_path
    :summary:
    ```
* - {py:obj}`should_save_archive_dot_org <archivebox.extractors.archive_org.should_save_archive_dot_org>`
  - ```{autodoc2-docstring} archivebox.extractors.archive_org.should_save_archive_dot_org
    :summary:
    ```
* - {py:obj}`save_archive_dot_org <archivebox.extractors.archive_org.save_archive_dot_org>`
  - ```{autodoc2-docstring} archivebox.extractors.archive_org.save_archive_dot_org
    :summary:
    ```
* - {py:obj}`parse_archive_dot_org_response <archivebox.extractors.archive_org.parse_archive_dot_org_response>`
  - ```{autodoc2-docstring} archivebox.extractors.archive_org.parse_archive_dot_org_response
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.extractors.archive_org.__package__>`
  - ```{autodoc2-docstring} archivebox.extractors.archive_org.__package__
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.extractors.archive_org.__package__
:value: >
   'archivebox.extractors'

```{autodoc2-docstring} archivebox.extractors.archive_org.__package__
```

````

````{py:function} get_output_path()
:canonical: archivebox.extractors.archive_org.get_output_path

```{autodoc2-docstring} archivebox.extractors.archive_org.get_output_path
```
````

````{py:function} should_save_archive_dot_org(link: archivebox.index.schema.Link, out_dir: typing.Optional[pathlib.Path] = None, overwrite: typing.Optional[bool] = False) -> bool
:canonical: archivebox.extractors.archive_org.should_save_archive_dot_org

```{autodoc2-docstring} archivebox.extractors.archive_org.should_save_archive_dot_org
```
````

````{py:function} save_archive_dot_org(link: archivebox.index.schema.Link, out_dir: typing.Optional[pathlib.Path] = None, timeout: int = CURL_CONFIG.CURL_TIMEOUT) -> archivebox.index.schema.ArchiveResult
:canonical: archivebox.extractors.archive_org.save_archive_dot_org

```{autodoc2-docstring} archivebox.extractors.archive_org.save_archive_dot_org
```
````

````{py:function} parse_archive_dot_org_response(response: str) -> typing.Tuple[typing.List[str], typing.List[str]]
:canonical: archivebox.extractors.archive_org.parse_archive_dot_org_response

```{autodoc2-docstring} archivebox.extractors.archive_org.parse_archive_dot_org_response
```
````
