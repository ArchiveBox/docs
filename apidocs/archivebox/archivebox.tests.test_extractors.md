# {py:mod}`archivebox.tests.test_extractors`

```{py:module} archivebox.tests.test_extractors
```

```{autodoc2-docstring} archivebox.tests.test_extractors
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_find_snapshot_dir <archivebox.tests.test_extractors._find_snapshot_dir>`
  - ```{autodoc2-docstring} archivebox.tests.test_extractors._find_snapshot_dir
    :summary:
    ```
* - {py:obj}`_latest_snapshot_dir <archivebox.tests.test_extractors._latest_snapshot_dir>`
  - ```{autodoc2-docstring} archivebox.tests.test_extractors._latest_snapshot_dir
    :summary:
    ```
* - {py:obj}`_latest_plugin_result <archivebox.tests.test_extractors._latest_plugin_result>`
  - ```{autodoc2-docstring} archivebox.tests.test_extractors._latest_plugin_result
    :summary:
    ```
* - {py:obj}`_plugin_output_paths <archivebox.tests.test_extractors._plugin_output_paths>`
  - ```{autodoc2-docstring} archivebox.tests.test_extractors._plugin_output_paths
    :summary:
    ```
* - {py:obj}`_archivebox_env <archivebox.tests.test_extractors._archivebox_env>`
  - ```{autodoc2-docstring} archivebox.tests.test_extractors._archivebox_env
    :summary:
    ```
* - {py:obj}`test_singlefile_works <archivebox.tests.test_extractors.test_singlefile_works>`
  - ```{autodoc2-docstring} archivebox.tests.test_extractors.test_singlefile_works
    :summary:
    ```
* - {py:obj}`test_readability_works <archivebox.tests.test_extractors.test_readability_works>`
  - ```{autodoc2-docstring} archivebox.tests.test_extractors.test_readability_works
    :summary:
    ```
* - {py:obj}`test_htmltotext_works <archivebox.tests.test_extractors.test_htmltotext_works>`
  - ```{autodoc2-docstring} archivebox.tests.test_extractors.test_htmltotext_works
    :summary:
    ```
* - {py:obj}`test_use_node_false_disables_readability_and_singlefile <archivebox.tests.test_extractors.test_use_node_false_disables_readability_and_singlefile>`
  - ```{autodoc2-docstring} archivebox.tests.test_extractors.test_use_node_false_disables_readability_and_singlefile
    :summary:
    ```
* - {py:obj}`test_headers_retrieved <archivebox.tests.test_extractors.test_headers_retrieved>`
  - ```{autodoc2-docstring} archivebox.tests.test_extractors.test_headers_retrieved
    :summary:
    ```
````

### API

````{py:function} _find_snapshot_dir(data_dir: pathlib.Path, snapshot_id: str) -> pathlib.Path | None
:canonical: archivebox.tests.test_extractors._find_snapshot_dir

```{autodoc2-docstring} archivebox.tests.test_extractors._find_snapshot_dir
```
````

````{py:function} _latest_snapshot_dir(data_dir: pathlib.Path) -> pathlib.Path
:canonical: archivebox.tests.test_extractors._latest_snapshot_dir

```{autodoc2-docstring} archivebox.tests.test_extractors._latest_snapshot_dir
```
````

````{py:function} _latest_plugin_result(data_dir: pathlib.Path, plugin: str) -> tuple[str, str, dict]
:canonical: archivebox.tests.test_extractors._latest_plugin_result

```{autodoc2-docstring} archivebox.tests.test_extractors._latest_plugin_result
```
````

````{py:function} _plugin_output_paths(data_dir: pathlib.Path, plugin: str) -> list[pathlib.Path]
:canonical: archivebox.tests.test_extractors._plugin_output_paths

```{autodoc2-docstring} archivebox.tests.test_extractors._plugin_output_paths
```
````

````{py:function} _archivebox_env(base_env: dict, data_dir: pathlib.Path) -> dict
:canonical: archivebox.tests.test_extractors._archivebox_env

```{autodoc2-docstring} archivebox.tests.test_extractors._archivebox_env
```
````

````{py:function} test_singlefile_works(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_extractors.test_singlefile_works

```{autodoc2-docstring} archivebox.tests.test_extractors.test_singlefile_works
```
````

````{py:function} test_readability_works(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_extractors.test_readability_works

```{autodoc2-docstring} archivebox.tests.test_extractors.test_readability_works
```
````

````{py:function} test_htmltotext_works(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_extractors.test_htmltotext_works

```{autodoc2-docstring} archivebox.tests.test_extractors.test_htmltotext_works
```
````

````{py:function} test_use_node_false_disables_readability_and_singlefile(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_extractors.test_use_node_false_disables_readability_and_singlefile

```{autodoc2-docstring} archivebox.tests.test_extractors.test_use_node_false_disables_readability_and_singlefile
```
````

````{py:function} test_headers_retrieved(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_extractors.test_headers_retrieved

```{autodoc2-docstring} archivebox.tests.test_extractors.test_headers_retrieved
```
````
