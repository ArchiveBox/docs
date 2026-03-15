# {py:mod}`archivebox.tests.conftest`

```{py:module} archivebox.tests.conftest
```

```{autodoc2-docstring} archivebox.tests.conftest
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`run_archivebox_cmd <archivebox.tests.conftest.run_archivebox_cmd>`
  - ```{autodoc2-docstring} archivebox.tests.conftest.run_archivebox_cmd
    :summary:
    ```
* - {py:obj}`isolated_data_dir <archivebox.tests.conftest.isolated_data_dir>`
  - ```{autodoc2-docstring} archivebox.tests.conftest.isolated_data_dir
    :summary:
    ```
* - {py:obj}`initialized_archive <archivebox.tests.conftest.initialized_archive>`
  - ```{autodoc2-docstring} archivebox.tests.conftest.initialized_archive
    :summary:
    ```
* - {py:obj}`run_archivebox_cmd_cwd <archivebox.tests.conftest.run_archivebox_cmd_cwd>`
  - ```{autodoc2-docstring} archivebox.tests.conftest.run_archivebox_cmd_cwd
    :summary:
    ```
* - {py:obj}`stop_process <archivebox.tests.conftest.stop_process>`
  - ```{autodoc2-docstring} archivebox.tests.conftest.stop_process
    :summary:
    ```
* - {py:obj}`run_python_cwd <archivebox.tests.conftest.run_python_cwd>`
  - ```{autodoc2-docstring} archivebox.tests.conftest.run_python_cwd
    :summary:
    ```
* - {py:obj}`wait_for_archive_outputs <archivebox.tests.conftest.wait_for_archive_outputs>`
  - ```{autodoc2-docstring} archivebox.tests.conftest.wait_for_archive_outputs
    :summary:
    ```
* - {py:obj}`_get_machine_type <archivebox.tests.conftest._get_machine_type>`
  - ```{autodoc2-docstring} archivebox.tests.conftest._get_machine_type
    :summary:
    ```
* - {py:obj}`_find_cached_chromium <archivebox.tests.conftest._find_cached_chromium>`
  - ```{autodoc2-docstring} archivebox.tests.conftest._find_cached_chromium
    :summary:
    ```
* - {py:obj}`_find_system_browser <archivebox.tests.conftest._find_system_browser>`
  - ```{autodoc2-docstring} archivebox.tests.conftest._find_system_browser
    :summary:
    ```
* - {py:obj}`_ensure_puppeteer <archivebox.tests.conftest._ensure_puppeteer>`
  - ```{autodoc2-docstring} archivebox.tests.conftest._ensure_puppeteer
    :summary:
    ```
* - {py:obj}`real_archive_with_example <archivebox.tests.conftest.real_archive_with_example>`
  - ```{autodoc2-docstring} archivebox.tests.conftest.real_archive_with_example
    :summary:
    ```
* - {py:obj}`parse_jsonl_output <archivebox.tests.conftest.parse_jsonl_output>`
  - ```{autodoc2-docstring} archivebox.tests.conftest.parse_jsonl_output
    :summary:
    ```
* - {py:obj}`assert_jsonl_contains_type <archivebox.tests.conftest.assert_jsonl_contains_type>`
  - ```{autodoc2-docstring} archivebox.tests.conftest.assert_jsonl_contains_type
    :summary:
    ```
* - {py:obj}`assert_jsonl_pass_through <archivebox.tests.conftest.assert_jsonl_pass_through>`
  - ```{autodoc2-docstring} archivebox.tests.conftest.assert_jsonl_pass_through
    :summary:
    ```
* - {py:obj}`assert_record_has_fields <archivebox.tests.conftest.assert_record_has_fields>`
  - ```{autodoc2-docstring} archivebox.tests.conftest.assert_record_has_fields
    :summary:
    ```
* - {py:obj}`create_test_url <archivebox.tests.conftest.create_test_url>`
  - ```{autodoc2-docstring} archivebox.tests.conftest.create_test_url
    :summary:
    ```
* - {py:obj}`create_test_crawl_json <archivebox.tests.conftest.create_test_crawl_json>`
  - ```{autodoc2-docstring} archivebox.tests.conftest.create_test_crawl_json
    :summary:
    ```
* - {py:obj}`create_test_snapshot_json <archivebox.tests.conftest.create_test_snapshot_json>`
  - ```{autodoc2-docstring} archivebox.tests.conftest.create_test_snapshot_json
    :summary:
    ```
````

### API

````{py:function} run_archivebox_cmd(args: typing.List[str], data_dir: pathlib.Path, stdin: typing.Optional[str] = None, timeout: int = 60, env: typing.Optional[typing.Dict[str, str]] = None) -> typing.Tuple[str, str, int]
:canonical: archivebox.tests.conftest.run_archivebox_cmd

```{autodoc2-docstring} archivebox.tests.conftest.run_archivebox_cmd
```
````

````{py:function} isolated_data_dir(tmp_path)
:canonical: archivebox.tests.conftest.isolated_data_dir

```{autodoc2-docstring} archivebox.tests.conftest.isolated_data_dir
```
````

````{py:function} initialized_archive(isolated_data_dir)
:canonical: archivebox.tests.conftest.initialized_archive

```{autodoc2-docstring} archivebox.tests.conftest.initialized_archive
```
````

````{py:function} run_archivebox_cmd_cwd(args: typing.List[str], cwd: pathlib.Path, stdin: typing.Optional[str] = None, timeout: int = 60, env: typing.Optional[typing.Dict[str, str]] = None) -> typing.Tuple[str, str, int]
:canonical: archivebox.tests.conftest.run_archivebox_cmd_cwd

```{autodoc2-docstring} archivebox.tests.conftest.run_archivebox_cmd_cwd
```
````

````{py:function} stop_process(proc: subprocess.Popen[str]) -> typing.Tuple[str, str]
:canonical: archivebox.tests.conftest.stop_process

```{autodoc2-docstring} archivebox.tests.conftest.stop_process
```
````

````{py:function} run_python_cwd(script: str, cwd: pathlib.Path, timeout: int = 60) -> typing.Tuple[str, str, int]
:canonical: archivebox.tests.conftest.run_python_cwd

```{autodoc2-docstring} archivebox.tests.conftest.run_python_cwd
```
````

````{py:function} wait_for_archive_outputs(cwd: pathlib.Path, url: str, timeout: int = 120, interval: float = 1.0) -> bool
:canonical: archivebox.tests.conftest.wait_for_archive_outputs

```{autodoc2-docstring} archivebox.tests.conftest.wait_for_archive_outputs
```
````

````{py:function} _get_machine_type() -> str
:canonical: archivebox.tests.conftest._get_machine_type

```{autodoc2-docstring} archivebox.tests.conftest._get_machine_type
```
````

````{py:function} _find_cached_chromium(lib_dir: pathlib.Path) -> typing.Optional[pathlib.Path]
:canonical: archivebox.tests.conftest._find_cached_chromium

```{autodoc2-docstring} archivebox.tests.conftest._find_cached_chromium
```
````

````{py:function} _find_system_browser() -> typing.Optional[pathlib.Path]
:canonical: archivebox.tests.conftest._find_system_browser

```{autodoc2-docstring} archivebox.tests.conftest._find_system_browser
```
````

````{py:function} _ensure_puppeteer(shared_lib: pathlib.Path) -> None
:canonical: archivebox.tests.conftest._ensure_puppeteer

```{autodoc2-docstring} archivebox.tests.conftest._ensure_puppeteer
```
````

````{py:function} real_archive_with_example(tmp_path_factory, request)
:canonical: archivebox.tests.conftest.real_archive_with_example

```{autodoc2-docstring} archivebox.tests.conftest.real_archive_with_example
```
````

````{py:function} parse_jsonl_output(stdout: str) -> typing.List[typing.Dict[str, typing.Any]]
:canonical: archivebox.tests.conftest.parse_jsonl_output

```{autodoc2-docstring} archivebox.tests.conftest.parse_jsonl_output
```
````

````{py:function} assert_jsonl_contains_type(stdout: str, record_type: str, min_count: int = 1)
:canonical: archivebox.tests.conftest.assert_jsonl_contains_type

```{autodoc2-docstring} archivebox.tests.conftest.assert_jsonl_contains_type
```
````

````{py:function} assert_jsonl_pass_through(stdout: str, input_records: typing.List[typing.Dict[str, typing.Any]])
:canonical: archivebox.tests.conftest.assert_jsonl_pass_through

```{autodoc2-docstring} archivebox.tests.conftest.assert_jsonl_pass_through
```
````

````{py:function} assert_record_has_fields(record: typing.Dict[str, typing.Any], required_fields: typing.List[str])
:canonical: archivebox.tests.conftest.assert_record_has_fields

```{autodoc2-docstring} archivebox.tests.conftest.assert_record_has_fields
```
````

````{py:function} create_test_url(domain: str = 'example.com', path: str = None) -> str
:canonical: archivebox.tests.conftest.create_test_url

```{autodoc2-docstring} archivebox.tests.conftest.create_test_url
```
````

````{py:function} create_test_crawl_json(urls: typing.List[str] = None, **kwargs) -> typing.Dict[str, typing.Any]
:canonical: archivebox.tests.conftest.create_test_crawl_json

```{autodoc2-docstring} archivebox.tests.conftest.create_test_crawl_json
```
````

````{py:function} create_test_snapshot_json(url: str = None, **kwargs) -> typing.Dict[str, typing.Any]
:canonical: archivebox.tests.conftest.create_test_snapshot_json

```{autodoc2-docstring} archivebox.tests.conftest.create_test_snapshot_json
```
````
