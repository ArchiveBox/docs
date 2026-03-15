# {py:mod}`archivebox.tests.test_cli_init`

```{py:module} archivebox.tests.test_cli_init
```

```{autodoc2-docstring} archivebox.tests.test_cli_init
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`test_init_creates_database_file <archivebox.tests.test_cli_init.test_init_creates_database_file>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_creates_database_file
    :summary:
    ```
* - {py:obj}`test_init_creates_archive_directory <archivebox.tests.test_cli_init.test_init_creates_archive_directory>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_creates_archive_directory
    :summary:
    ```
* - {py:obj}`test_init_creates_sources_directory <archivebox.tests.test_cli_init.test_init_creates_sources_directory>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_creates_sources_directory
    :summary:
    ```
* - {py:obj}`test_init_creates_logs_directory <archivebox.tests.test_cli_init.test_init_creates_logs_directory>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_creates_logs_directory
    :summary:
    ```
* - {py:obj}`test_init_creates_config_file <archivebox.tests.test_cli_init.test_init_creates_config_file>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_creates_config_file
    :summary:
    ```
* - {py:obj}`test_init_runs_migrations <archivebox.tests.test_cli_init.test_init_runs_migrations>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_runs_migrations
    :summary:
    ```
* - {py:obj}`test_init_creates_core_snapshot_table <archivebox.tests.test_cli_init.test_init_creates_core_snapshot_table>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_creates_core_snapshot_table
    :summary:
    ```
* - {py:obj}`test_init_creates_crawls_crawl_table <archivebox.tests.test_cli_init.test_init_creates_crawls_crawl_table>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_creates_crawls_crawl_table
    :summary:
    ```
* - {py:obj}`test_init_creates_core_archiveresult_table <archivebox.tests.test_cli_init.test_init_creates_core_archiveresult_table>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_creates_core_archiveresult_table
    :summary:
    ```
* - {py:obj}`test_init_sets_correct_file_permissions <archivebox.tests.test_cli_init.test_init_sets_correct_file_permissions>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_sets_correct_file_permissions
    :summary:
    ```
* - {py:obj}`test_init_is_idempotent <archivebox.tests.test_cli_init.test_init_is_idempotent>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_is_idempotent
    :summary:
    ```
* - {py:obj}`test_init_with_existing_data_preserves_snapshots <archivebox.tests.test_cli_init.test_init_with_existing_data_preserves_snapshots>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_with_existing_data_preserves_snapshots
    :summary:
    ```
* - {py:obj}`test_init_quick_flag_skips_checks <archivebox.tests.test_cli_init.test_init_quick_flag_skips_checks>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_quick_flag_skips_checks
    :summary:
    ```
* - {py:obj}`test_init_creates_machine_table <archivebox.tests.test_cli_init.test_init_creates_machine_table>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_creates_machine_table
    :summary:
    ```
* - {py:obj}`test_init_output_shows_collection_info <archivebox.tests.test_cli_init.test_init_output_shows_collection_info>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_output_shows_collection_info
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DIR_PERMISSIONS <archivebox.tests.test_cli_init.DIR_PERMISSIONS>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_init.DIR_PERMISSIONS
    :summary:
    ```
````

### API

````{py:data} DIR_PERMISSIONS
:canonical: archivebox.tests.test_cli_init.DIR_PERMISSIONS
:value: >
   'replace(...)'

```{autodoc2-docstring} archivebox.tests.test_cli_init.DIR_PERMISSIONS
```

````

````{py:function} test_init_creates_database_file(tmp_path)
:canonical: archivebox.tests.test_cli_init.test_init_creates_database_file

```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_creates_database_file
```
````

````{py:function} test_init_creates_archive_directory(tmp_path)
:canonical: archivebox.tests.test_cli_init.test_init_creates_archive_directory

```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_creates_archive_directory
```
````

````{py:function} test_init_creates_sources_directory(tmp_path)
:canonical: archivebox.tests.test_cli_init.test_init_creates_sources_directory

```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_creates_sources_directory
```
````

````{py:function} test_init_creates_logs_directory(tmp_path)
:canonical: archivebox.tests.test_cli_init.test_init_creates_logs_directory

```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_creates_logs_directory
```
````

````{py:function} test_init_creates_config_file(tmp_path)
:canonical: archivebox.tests.test_cli_init.test_init_creates_config_file

```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_creates_config_file
```
````

````{py:function} test_init_runs_migrations(tmp_path)
:canonical: archivebox.tests.test_cli_init.test_init_runs_migrations

```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_runs_migrations
```
````

````{py:function} test_init_creates_core_snapshot_table(tmp_path)
:canonical: archivebox.tests.test_cli_init.test_init_creates_core_snapshot_table

```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_creates_core_snapshot_table
```
````

````{py:function} test_init_creates_crawls_crawl_table(tmp_path)
:canonical: archivebox.tests.test_cli_init.test_init_creates_crawls_crawl_table

```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_creates_crawls_crawl_table
```
````

````{py:function} test_init_creates_core_archiveresult_table(tmp_path)
:canonical: archivebox.tests.test_cli_init.test_init_creates_core_archiveresult_table

```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_creates_core_archiveresult_table
```
````

````{py:function} test_init_sets_correct_file_permissions(tmp_path)
:canonical: archivebox.tests.test_cli_init.test_init_sets_correct_file_permissions

```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_sets_correct_file_permissions
```
````

````{py:function} test_init_is_idempotent(tmp_path)
:canonical: archivebox.tests.test_cli_init.test_init_is_idempotent

```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_is_idempotent
```
````

````{py:function} test_init_with_existing_data_preserves_snapshots(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_cli_init.test_init_with_existing_data_preserves_snapshots

```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_with_existing_data_preserves_snapshots
```
````

````{py:function} test_init_quick_flag_skips_checks(tmp_path)
:canonical: archivebox.tests.test_cli_init.test_init_quick_flag_skips_checks

```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_quick_flag_skips_checks
```
````

````{py:function} test_init_creates_machine_table(tmp_path)
:canonical: archivebox.tests.test_cli_init.test_init_creates_machine_table

```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_creates_machine_table
```
````

````{py:function} test_init_output_shows_collection_info(tmp_path)
:canonical: archivebox.tests.test_cli_init.test_init_output_shows_collection_info

```{autodoc2-docstring} archivebox.tests.test_cli_init.test_init_output_shows_collection_info
```
````
