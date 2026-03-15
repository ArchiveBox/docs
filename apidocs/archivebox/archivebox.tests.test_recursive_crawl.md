# {py:mod}`archivebox.tests.test_recursive_crawl`

```{py:module} archivebox.tests.test_recursive_crawl
```

```{autodoc2-docstring} archivebox.tests.test_recursive_crawl
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`wait_for_db_condition <archivebox.tests.test_recursive_crawl.wait_for_db_condition>`
  - ```{autodoc2-docstring} archivebox.tests.test_recursive_crawl.wait_for_db_condition
    :summary:
    ```
* - {py:obj}`stop_process <archivebox.tests.test_recursive_crawl.stop_process>`
  - ```{autodoc2-docstring} archivebox.tests.test_recursive_crawl.stop_process
    :summary:
    ```
* - {py:obj}`run_add_until <archivebox.tests.test_recursive_crawl.run_add_until>`
  - ```{autodoc2-docstring} archivebox.tests.test_recursive_crawl.run_add_until
    :summary:
    ```
* - {py:obj}`test_background_hooks_dont_block_parser_extractors <archivebox.tests.test_recursive_crawl.test_background_hooks_dont_block_parser_extractors>`
  - ```{autodoc2-docstring} archivebox.tests.test_recursive_crawl.test_background_hooks_dont_block_parser_extractors
    :summary:
    ```
* - {py:obj}`test_parser_extractors_emit_snapshot_jsonl <archivebox.tests.test_recursive_crawl.test_parser_extractors_emit_snapshot_jsonl>`
  - ```{autodoc2-docstring} archivebox.tests.test_recursive_crawl.test_parser_extractors_emit_snapshot_jsonl
    :summary:
    ```
* - {py:obj}`test_recursive_crawl_creates_child_snapshots <archivebox.tests.test_recursive_crawl.test_recursive_crawl_creates_child_snapshots>`
  - ```{autodoc2-docstring} archivebox.tests.test_recursive_crawl.test_recursive_crawl_creates_child_snapshots
    :summary:
    ```
* - {py:obj}`test_recursive_crawl_respects_depth_limit <archivebox.tests.test_recursive_crawl.test_recursive_crawl_respects_depth_limit>`
  - ```{autodoc2-docstring} archivebox.tests.test_recursive_crawl.test_recursive_crawl_respects_depth_limit
    :summary:
    ```
* - {py:obj}`test_crawl_snapshot_has_parent_snapshot_field <archivebox.tests.test_recursive_crawl.test_crawl_snapshot_has_parent_snapshot_field>`
  - ```{autodoc2-docstring} archivebox.tests.test_recursive_crawl.test_crawl_snapshot_has_parent_snapshot_field
    :summary:
    ```
* - {py:obj}`test_snapshot_depth_field_exists <archivebox.tests.test_recursive_crawl.test_snapshot_depth_field_exists>`
  - ```{autodoc2-docstring} archivebox.tests.test_recursive_crawl.test_snapshot_depth_field_exists
    :summary:
    ```
* - {py:obj}`test_root_snapshot_has_depth_zero <archivebox.tests.test_recursive_crawl.test_root_snapshot_has_depth_zero>`
  - ```{autodoc2-docstring} archivebox.tests.test_recursive_crawl.test_root_snapshot_has_depth_zero
    :summary:
    ```
* - {py:obj}`test_archiveresult_worker_queue_filters_by_foreground_extractors <archivebox.tests.test_recursive_crawl.test_archiveresult_worker_queue_filters_by_foreground_extractors>`
  - ```{autodoc2-docstring} archivebox.tests.test_recursive_crawl.test_archiveresult_worker_queue_filters_by_foreground_extractors
    :summary:
    ```
````

### API

````{py:function} wait_for_db_condition(timeout, condition, interval=0.5)
:canonical: archivebox.tests.test_recursive_crawl.wait_for_db_condition

```{autodoc2-docstring} archivebox.tests.test_recursive_crawl.wait_for_db_condition
```
````

````{py:function} stop_process(proc)
:canonical: archivebox.tests.test_recursive_crawl.stop_process

```{autodoc2-docstring} archivebox.tests.test_recursive_crawl.stop_process
```
````

````{py:function} run_add_until(args, env, condition, timeout=120)
:canonical: archivebox.tests.test_recursive_crawl.run_add_until

```{autodoc2-docstring} archivebox.tests.test_recursive_crawl.run_add_until
```
````

````{py:function} test_background_hooks_dont_block_parser_extractors(tmp_path, process, recursive_test_site)
:canonical: archivebox.tests.test_recursive_crawl.test_background_hooks_dont_block_parser_extractors

```{autodoc2-docstring} archivebox.tests.test_recursive_crawl.test_background_hooks_dont_block_parser_extractors
```
````

````{py:function} test_parser_extractors_emit_snapshot_jsonl(tmp_path, process, recursive_test_site)
:canonical: archivebox.tests.test_recursive_crawl.test_parser_extractors_emit_snapshot_jsonl

```{autodoc2-docstring} archivebox.tests.test_recursive_crawl.test_parser_extractors_emit_snapshot_jsonl
```
````

````{py:function} test_recursive_crawl_creates_child_snapshots(tmp_path, process, recursive_test_site)
:canonical: archivebox.tests.test_recursive_crawl.test_recursive_crawl_creates_child_snapshots

```{autodoc2-docstring} archivebox.tests.test_recursive_crawl.test_recursive_crawl_creates_child_snapshots
```
````

````{py:function} test_recursive_crawl_respects_depth_limit(tmp_path, process, disable_extractors_dict, recursive_test_site)
:canonical: archivebox.tests.test_recursive_crawl.test_recursive_crawl_respects_depth_limit

```{autodoc2-docstring} archivebox.tests.test_recursive_crawl.test_recursive_crawl_respects_depth_limit
```
````

````{py:function} test_crawl_snapshot_has_parent_snapshot_field(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_recursive_crawl.test_crawl_snapshot_has_parent_snapshot_field

```{autodoc2-docstring} archivebox.tests.test_recursive_crawl.test_crawl_snapshot_has_parent_snapshot_field
```
````

````{py:function} test_snapshot_depth_field_exists(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_recursive_crawl.test_snapshot_depth_field_exists

```{autodoc2-docstring} archivebox.tests.test_recursive_crawl.test_snapshot_depth_field_exists
```
````

````{py:function} test_root_snapshot_has_depth_zero(tmp_path, process, disable_extractors_dict, recursive_test_site)
:canonical: archivebox.tests.test_recursive_crawl.test_root_snapshot_has_depth_zero

```{autodoc2-docstring} archivebox.tests.test_recursive_crawl.test_root_snapshot_has_depth_zero
```
````

````{py:function} test_archiveresult_worker_queue_filters_by_foreground_extractors(tmp_path, process, recursive_test_site)
:canonical: archivebox.tests.test_recursive_crawl.test_archiveresult_worker_queue_filters_by_foreground_extractors

```{autodoc2-docstring} archivebox.tests.test_recursive_crawl.test_archiveresult_worker_queue_filters_by_foreground_extractors
```
````
