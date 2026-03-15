# {py:mod}`archivebox.tests.test_cli_archiveresult`

```{py:module} archivebox.tests.test_cli_archiveresult
```

```{autodoc2-docstring} archivebox.tests.test_cli_archiveresult
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestArchiveResultCreate <archivebox.tests.test_cli_archiveresult.TestArchiveResultCreate>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_archiveresult.TestArchiveResultCreate
    :summary:
    ```
* - {py:obj}`TestArchiveResultList <archivebox.tests.test_cli_archiveresult.TestArchiveResultList>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_archiveresult.TestArchiveResultList
    :summary:
    ```
* - {py:obj}`TestArchiveResultUpdate <archivebox.tests.test_cli_archiveresult.TestArchiveResultUpdate>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_archiveresult.TestArchiveResultUpdate
    :summary:
    ```
* - {py:obj}`TestArchiveResultDelete <archivebox.tests.test_cli_archiveresult.TestArchiveResultDelete>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_archiveresult.TestArchiveResultDelete
    :summary:
    ```
````

### API

`````{py:class} TestArchiveResultCreate
:canonical: archivebox.tests.test_cli_archiveresult.TestArchiveResultCreate

```{autodoc2-docstring} archivebox.tests.test_cli_archiveresult.TestArchiveResultCreate
```

````{py:method} test_create_from_snapshot_jsonl(initialized_archive)
:canonical: archivebox.tests.test_cli_archiveresult.TestArchiveResultCreate.test_create_from_snapshot_jsonl

```{autodoc2-docstring} archivebox.tests.test_cli_archiveresult.TestArchiveResultCreate.test_create_from_snapshot_jsonl
```

````

````{py:method} test_create_with_specific_plugin(initialized_archive)
:canonical: archivebox.tests.test_cli_archiveresult.TestArchiveResultCreate.test_create_with_specific_plugin

```{autodoc2-docstring} archivebox.tests.test_cli_archiveresult.TestArchiveResultCreate.test_create_with_specific_plugin
```

````

````{py:method} test_create_pass_through_crawl(initialized_archive)
:canonical: archivebox.tests.test_cli_archiveresult.TestArchiveResultCreate.test_create_pass_through_crawl

```{autodoc2-docstring} archivebox.tests.test_cli_archiveresult.TestArchiveResultCreate.test_create_pass_through_crawl
```

````

````{py:method} test_create_pass_through_only_when_no_snapshots(initialized_archive)
:canonical: archivebox.tests.test_cli_archiveresult.TestArchiveResultCreate.test_create_pass_through_only_when_no_snapshots

```{autodoc2-docstring} archivebox.tests.test_cli_archiveresult.TestArchiveResultCreate.test_create_pass_through_only_when_no_snapshots
```

````

`````

`````{py:class} TestArchiveResultList
:canonical: archivebox.tests.test_cli_archiveresult.TestArchiveResultList

```{autodoc2-docstring} archivebox.tests.test_cli_archiveresult.TestArchiveResultList
```

````{py:method} test_list_empty(initialized_archive)
:canonical: archivebox.tests.test_cli_archiveresult.TestArchiveResultList.test_list_empty

```{autodoc2-docstring} archivebox.tests.test_cli_archiveresult.TestArchiveResultList.test_list_empty
```

````

````{py:method} test_list_filter_by_status(initialized_archive)
:canonical: archivebox.tests.test_cli_archiveresult.TestArchiveResultList.test_list_filter_by_status

```{autodoc2-docstring} archivebox.tests.test_cli_archiveresult.TestArchiveResultList.test_list_filter_by_status
```

````

````{py:method} test_list_filter_by_plugin(initialized_archive)
:canonical: archivebox.tests.test_cli_archiveresult.TestArchiveResultList.test_list_filter_by_plugin

```{autodoc2-docstring} archivebox.tests.test_cli_archiveresult.TestArchiveResultList.test_list_filter_by_plugin
```

````

````{py:method} test_list_with_limit(initialized_archive)
:canonical: archivebox.tests.test_cli_archiveresult.TestArchiveResultList.test_list_with_limit

```{autodoc2-docstring} archivebox.tests.test_cli_archiveresult.TestArchiveResultList.test_list_with_limit
```

````

`````

`````{py:class} TestArchiveResultUpdate
:canonical: archivebox.tests.test_cli_archiveresult.TestArchiveResultUpdate

```{autodoc2-docstring} archivebox.tests.test_cli_archiveresult.TestArchiveResultUpdate
```

````{py:method} test_update_status(initialized_archive)
:canonical: archivebox.tests.test_cli_archiveresult.TestArchiveResultUpdate.test_update_status

```{autodoc2-docstring} archivebox.tests.test_cli_archiveresult.TestArchiveResultUpdate.test_update_status
```

````

`````

`````{py:class} TestArchiveResultDelete
:canonical: archivebox.tests.test_cli_archiveresult.TestArchiveResultDelete

```{autodoc2-docstring} archivebox.tests.test_cli_archiveresult.TestArchiveResultDelete
```

````{py:method} test_delete_requires_yes(initialized_archive)
:canonical: archivebox.tests.test_cli_archiveresult.TestArchiveResultDelete.test_delete_requires_yes

```{autodoc2-docstring} archivebox.tests.test_cli_archiveresult.TestArchiveResultDelete.test_delete_requires_yes
```

````

````{py:method} test_delete_with_yes(initialized_archive)
:canonical: archivebox.tests.test_cli_archiveresult.TestArchiveResultDelete.test_delete_with_yes

```{autodoc2-docstring} archivebox.tests.test_cli_archiveresult.TestArchiveResultDelete.test_delete_with_yes
```

````

`````
