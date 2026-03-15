# {py:mod}`archivebox.tests.test_cli_status`

```{py:module} archivebox.tests.test_cli_status
```

```{autodoc2-docstring} archivebox.tests.test_cli_status
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`test_status_runs_successfully <archivebox.tests.test_cli_status.test_status_runs_successfully>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_status.test_status_runs_successfully
    :summary:
    ```
* - {py:obj}`test_status_shows_zero_snapshots_in_empty_archive <archivebox.tests.test_cli_status.test_status_shows_zero_snapshots_in_empty_archive>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_status.test_status_shows_zero_snapshots_in_empty_archive
    :summary:
    ```
* - {py:obj}`test_status_shows_correct_snapshot_count <archivebox.tests.test_cli_status.test_status_shows_correct_snapshot_count>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_status.test_status_shows_correct_snapshot_count
    :summary:
    ```
* - {py:obj}`test_status_shows_archived_count <archivebox.tests.test_cli_status.test_status_shows_archived_count>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_status.test_status_shows_archived_count
    :summary:
    ```
* - {py:obj}`test_status_shows_archive_directory_size <archivebox.tests.test_cli_status.test_status_shows_archive_directory_size>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_status.test_status_shows_archive_directory_size
    :summary:
    ```
* - {py:obj}`test_status_counts_archive_directories <archivebox.tests.test_cli_status.test_status_counts_archive_directories>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_status.test_status_counts_archive_directories
    :summary:
    ```
* - {py:obj}`test_status_detects_orphaned_directories <archivebox.tests.test_cli_status.test_status_detects_orphaned_directories>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_status.test_status_detects_orphaned_directories
    :summary:
    ```
* - {py:obj}`test_status_shows_user_info <archivebox.tests.test_cli_status.test_status_shows_user_info>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_status.test_status_shows_user_info
    :summary:
    ```
* - {py:obj}`test_status_reads_from_db_not_filesystem <archivebox.tests.test_cli_status.test_status_reads_from_db_not_filesystem>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_status.test_status_reads_from_db_not_filesystem
    :summary:
    ```
* - {py:obj}`test_status_shows_index_file_info <archivebox.tests.test_cli_status.test_status_shows_index_file_info>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_status.test_status_shows_index_file_info
    :summary:
    ```
````

### API

````{py:function} test_status_runs_successfully(tmp_path, process)
:canonical: archivebox.tests.test_cli_status.test_status_runs_successfully

```{autodoc2-docstring} archivebox.tests.test_cli_status.test_status_runs_successfully
```
````

````{py:function} test_status_shows_zero_snapshots_in_empty_archive(tmp_path, process)
:canonical: archivebox.tests.test_cli_status.test_status_shows_zero_snapshots_in_empty_archive

```{autodoc2-docstring} archivebox.tests.test_cli_status.test_status_shows_zero_snapshots_in_empty_archive
```
````

````{py:function} test_status_shows_correct_snapshot_count(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_cli_status.test_status_shows_correct_snapshot_count

```{autodoc2-docstring} archivebox.tests.test_cli_status.test_status_shows_correct_snapshot_count
```
````

````{py:function} test_status_shows_archived_count(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_cli_status.test_status_shows_archived_count

```{autodoc2-docstring} archivebox.tests.test_cli_status.test_status_shows_archived_count
```
````

````{py:function} test_status_shows_archive_directory_size(tmp_path, process)
:canonical: archivebox.tests.test_cli_status.test_status_shows_archive_directory_size

```{autodoc2-docstring} archivebox.tests.test_cli_status.test_status_shows_archive_directory_size
```
````

````{py:function} test_status_counts_archive_directories(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_cli_status.test_status_counts_archive_directories

```{autodoc2-docstring} archivebox.tests.test_cli_status.test_status_counts_archive_directories
```
````

````{py:function} test_status_detects_orphaned_directories(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_cli_status.test_status_detects_orphaned_directories

```{autodoc2-docstring} archivebox.tests.test_cli_status.test_status_detects_orphaned_directories
```
````

````{py:function} test_status_shows_user_info(tmp_path, process)
:canonical: archivebox.tests.test_cli_status.test_status_shows_user_info

```{autodoc2-docstring} archivebox.tests.test_cli_status.test_status_shows_user_info
```
````

````{py:function} test_status_reads_from_db_not_filesystem(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_cli_status.test_status_reads_from_db_not_filesystem

```{autodoc2-docstring} archivebox.tests.test_cli_status.test_status_reads_from_db_not_filesystem
```
````

````{py:function} test_status_shows_index_file_info(tmp_path, process)
:canonical: archivebox.tests.test_cli_status.test_status_shows_index_file_info

```{autodoc2-docstring} archivebox.tests.test_cli_status.test_status_shows_index_file_info
```
````
