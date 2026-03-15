# {py:mod}`archivebox.tests.test_cli_snapshot`

```{py:module} archivebox.tests.test_cli_snapshot
```

```{autodoc2-docstring} archivebox.tests.test_cli_snapshot
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestSnapshotCreate <archivebox.tests.test_cli_snapshot.TestSnapshotCreate>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotCreate
    :summary:
    ```
* - {py:obj}`TestSnapshotList <archivebox.tests.test_cli_snapshot.TestSnapshotList>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotList
    :summary:
    ```
* - {py:obj}`TestSnapshotUpdate <archivebox.tests.test_cli_snapshot.TestSnapshotUpdate>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotUpdate
    :summary:
    ```
* - {py:obj}`TestSnapshotDelete <archivebox.tests.test_cli_snapshot.TestSnapshotDelete>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotDelete
    :summary:
    ```
````

### API

`````{py:class} TestSnapshotCreate
:canonical: archivebox.tests.test_cli_snapshot.TestSnapshotCreate

```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotCreate
```

````{py:method} test_create_from_url_args(initialized_archive)
:canonical: archivebox.tests.test_cli_snapshot.TestSnapshotCreate.test_create_from_url_args

```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotCreate.test_create_from_url_args
```

````

````{py:method} test_create_from_crawl_jsonl(initialized_archive)
:canonical: archivebox.tests.test_cli_snapshot.TestSnapshotCreate.test_create_from_crawl_jsonl

```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotCreate.test_create_from_crawl_jsonl
```

````

````{py:method} test_create_with_tag(initialized_archive)
:canonical: archivebox.tests.test_cli_snapshot.TestSnapshotCreate.test_create_with_tag

```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotCreate.test_create_with_tag
```

````

````{py:method} test_create_pass_through_other_types(initialized_archive)
:canonical: archivebox.tests.test_cli_snapshot.TestSnapshotCreate.test_create_pass_through_other_types

```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotCreate.test_create_pass_through_other_types
```

````

````{py:method} test_create_multiple_urls(initialized_archive)
:canonical: archivebox.tests.test_cli_snapshot.TestSnapshotCreate.test_create_multiple_urls

```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotCreate.test_create_multiple_urls
```

````

`````

`````{py:class} TestSnapshotList
:canonical: archivebox.tests.test_cli_snapshot.TestSnapshotList

```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotList
```

````{py:method} test_list_empty(initialized_archive)
:canonical: archivebox.tests.test_cli_snapshot.TestSnapshotList.test_list_empty

```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotList.test_list_empty
```

````

````{py:method} test_list_returns_created(initialized_archive)
:canonical: archivebox.tests.test_cli_snapshot.TestSnapshotList.test_list_returns_created

```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotList.test_list_returns_created
```

````

````{py:method} test_list_filter_by_status(initialized_archive)
:canonical: archivebox.tests.test_cli_snapshot.TestSnapshotList.test_list_filter_by_status

```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotList.test_list_filter_by_status
```

````

````{py:method} test_list_filter_by_url_contains(initialized_archive)
:canonical: archivebox.tests.test_cli_snapshot.TestSnapshotList.test_list_filter_by_url_contains

```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotList.test_list_filter_by_url_contains
```

````

````{py:method} test_list_with_limit(initialized_archive)
:canonical: archivebox.tests.test_cli_snapshot.TestSnapshotList.test_list_with_limit

```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotList.test_list_with_limit
```

````

`````

`````{py:class} TestSnapshotUpdate
:canonical: archivebox.tests.test_cli_snapshot.TestSnapshotUpdate

```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotUpdate
```

````{py:method} test_update_status(initialized_archive)
:canonical: archivebox.tests.test_cli_snapshot.TestSnapshotUpdate.test_update_status

```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotUpdate.test_update_status
```

````

````{py:method} test_update_add_tag(initialized_archive)
:canonical: archivebox.tests.test_cli_snapshot.TestSnapshotUpdate.test_update_add_tag

```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotUpdate.test_update_add_tag
```

````

`````

`````{py:class} TestSnapshotDelete
:canonical: archivebox.tests.test_cli_snapshot.TestSnapshotDelete

```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotDelete
```

````{py:method} test_delete_requires_yes(initialized_archive)
:canonical: archivebox.tests.test_cli_snapshot.TestSnapshotDelete.test_delete_requires_yes

```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotDelete.test_delete_requires_yes
```

````

````{py:method} test_delete_with_yes(initialized_archive)
:canonical: archivebox.tests.test_cli_snapshot.TestSnapshotDelete.test_delete_with_yes

```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotDelete.test_delete_with_yes
```

````

````{py:method} test_delete_dry_run(initialized_archive)
:canonical: archivebox.tests.test_cli_snapshot.TestSnapshotDelete.test_delete_dry_run

```{autodoc2-docstring} archivebox.tests.test_cli_snapshot.TestSnapshotDelete.test_delete_dry_run
```

````

`````
