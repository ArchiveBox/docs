# {py:mod}`archivebox.tests.test_cli_add`

```{py:module} archivebox.tests.test_cli_add
```

```{autodoc2-docstring} archivebox.tests.test_cli_add
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`test_add_single_url_creates_snapshot_in_db <archivebox.tests.test_cli_add.test_add_single_url_creates_snapshot_in_db>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_single_url_creates_snapshot_in_db
    :summary:
    ```
* - {py:obj}`test_add_creates_crawl_record <archivebox.tests.test_cli_add.test_add_creates_crawl_record>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_creates_crawl_record
    :summary:
    ```
* - {py:obj}`test_add_creates_source_file <archivebox.tests.test_cli_add.test_add_creates_source_file>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_creates_source_file
    :summary:
    ```
* - {py:obj}`test_add_multiple_urls_single_command <archivebox.tests.test_cli_add.test_add_multiple_urls_single_command>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_multiple_urls_single_command
    :summary:
    ```
* - {py:obj}`test_add_from_file <archivebox.tests.test_cli_add.test_add_from_file>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_from_file
    :summary:
    ```
* - {py:obj}`test_add_with_depth_0_flag <archivebox.tests.test_cli_add.test_add_with_depth_0_flag>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_with_depth_0_flag
    :summary:
    ```
* - {py:obj}`test_add_with_depth_1_flag <archivebox.tests.test_cli_add.test_add_with_depth_1_flag>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_with_depth_1_flag
    :summary:
    ```
* - {py:obj}`test_add_with_tags <archivebox.tests.test_cli_add.test_add_with_tags>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_with_tags
    :summary:
    ```
* - {py:obj}`test_add_duplicate_url_creates_separate_crawls <archivebox.tests.test_cli_add.test_add_duplicate_url_creates_separate_crawls>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_duplicate_url_creates_separate_crawls
    :summary:
    ```
* - {py:obj}`test_add_with_overwrite_flag <archivebox.tests.test_cli_add.test_add_with_overwrite_flag>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_with_overwrite_flag
    :summary:
    ```
* - {py:obj}`test_add_creates_archive_subdirectory <archivebox.tests.test_cli_add.test_add_creates_archive_subdirectory>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_creates_archive_subdirectory
    :summary:
    ```
* - {py:obj}`test_add_index_only_skips_extraction <archivebox.tests.test_cli_add.test_add_index_only_skips_extraction>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_index_only_skips_extraction
    :summary:
    ```
* - {py:obj}`test_add_links_snapshot_to_crawl <archivebox.tests.test_cli_add.test_add_links_snapshot_to_crawl>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_links_snapshot_to_crawl
    :summary:
    ```
* - {py:obj}`test_add_sets_snapshot_timestamp <archivebox.tests.test_cli_add.test_add_sets_snapshot_timestamp>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_sets_snapshot_timestamp
    :summary:
    ```
````

### API

````{py:function} test_add_single_url_creates_snapshot_in_db(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_cli_add.test_add_single_url_creates_snapshot_in_db

```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_single_url_creates_snapshot_in_db
```
````

````{py:function} test_add_creates_crawl_record(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_cli_add.test_add_creates_crawl_record

```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_creates_crawl_record
```
````

````{py:function} test_add_creates_source_file(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_cli_add.test_add_creates_source_file

```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_creates_source_file
```
````

````{py:function} test_add_multiple_urls_single_command(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_cli_add.test_add_multiple_urls_single_command

```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_multiple_urls_single_command
```
````

````{py:function} test_add_from_file(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_cli_add.test_add_from_file

```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_from_file
```
````

````{py:function} test_add_with_depth_0_flag(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_cli_add.test_add_with_depth_0_flag

```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_with_depth_0_flag
```
````

````{py:function} test_add_with_depth_1_flag(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_cli_add.test_add_with_depth_1_flag

```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_with_depth_1_flag
```
````

````{py:function} test_add_with_tags(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_cli_add.test_add_with_tags

```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_with_tags
```
````

````{py:function} test_add_duplicate_url_creates_separate_crawls(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_cli_add.test_add_duplicate_url_creates_separate_crawls

```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_duplicate_url_creates_separate_crawls
```
````

````{py:function} test_add_with_overwrite_flag(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_cli_add.test_add_with_overwrite_flag

```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_with_overwrite_flag
```
````

````{py:function} test_add_creates_archive_subdirectory(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_cli_add.test_add_creates_archive_subdirectory

```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_creates_archive_subdirectory
```
````

````{py:function} test_add_index_only_skips_extraction(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_cli_add.test_add_index_only_skips_extraction

```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_index_only_skips_extraction
```
````

````{py:function} test_add_links_snapshot_to_crawl(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_cli_add.test_add_links_snapshot_to_crawl

```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_links_snapshot_to_crawl
```
````

````{py:function} test_add_sets_snapshot_timestamp(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_cli_add.test_add_sets_snapshot_timestamp

```{autodoc2-docstring} archivebox.tests.test_cli_add.test_add_sets_snapshot_timestamp
```
````
