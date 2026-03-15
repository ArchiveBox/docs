# {py:mod}`archivebox.tests.test_cli_run`

```{py:module} archivebox.tests.test_cli_run
```

```{autodoc2-docstring} archivebox.tests.test_cli_run
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestRunWithCrawl <archivebox.tests.test_cli_run.TestRunWithCrawl>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunWithCrawl
    :summary:
    ```
* - {py:obj}`TestRunWithSnapshot <archivebox.tests.test_cli_run.TestRunWithSnapshot>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunWithSnapshot
    :summary:
    ```
* - {py:obj}`TestRunWithArchiveResult <archivebox.tests.test_cli_run.TestRunWithArchiveResult>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunWithArchiveResult
    :summary:
    ```
* - {py:obj}`TestRunPassThrough <archivebox.tests.test_cli_run.TestRunPassThrough>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunPassThrough
    :summary:
    ```
* - {py:obj}`TestRunMixedInput <archivebox.tests.test_cli_run.TestRunMixedInput>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunMixedInput
    :summary:
    ```
* - {py:obj}`TestRunEmpty <archivebox.tests.test_cli_run.TestRunEmpty>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunEmpty
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`RUN_TEST_ENV <archivebox.tests.test_cli_run.RUN_TEST_ENV>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_run.RUN_TEST_ENV
    :summary:
    ```
````

### API

````{py:data} RUN_TEST_ENV
:canonical: archivebox.tests.test_cli_run.RUN_TEST_ENV
:value: >
   None

```{autodoc2-docstring} archivebox.tests.test_cli_run.RUN_TEST_ENV
```

````

`````{py:class} TestRunWithCrawl
:canonical: archivebox.tests.test_cli_run.TestRunWithCrawl

```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunWithCrawl
```

````{py:method} test_run_with_new_crawl(initialized_archive)
:canonical: archivebox.tests.test_cli_run.TestRunWithCrawl.test_run_with_new_crawl

```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunWithCrawl.test_run_with_new_crawl
```

````

````{py:method} test_run_with_existing_crawl(initialized_archive)
:canonical: archivebox.tests.test_cli_run.TestRunWithCrawl.test_run_with_existing_crawl

```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunWithCrawl.test_run_with_existing_crawl
```

````

`````

`````{py:class} TestRunWithSnapshot
:canonical: archivebox.tests.test_cli_run.TestRunWithSnapshot

```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunWithSnapshot
```

````{py:method} test_run_with_new_snapshot(initialized_archive)
:canonical: archivebox.tests.test_cli_run.TestRunWithSnapshot.test_run_with_new_snapshot

```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunWithSnapshot.test_run_with_new_snapshot
```

````

````{py:method} test_run_with_existing_snapshot(initialized_archive)
:canonical: archivebox.tests.test_cli_run.TestRunWithSnapshot.test_run_with_existing_snapshot

```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunWithSnapshot.test_run_with_existing_snapshot
```

````

````{py:method} test_run_with_plain_url(initialized_archive)
:canonical: archivebox.tests.test_cli_run.TestRunWithSnapshot.test_run_with_plain_url

```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunWithSnapshot.test_run_with_plain_url
```

````

`````

`````{py:class} TestRunWithArchiveResult
:canonical: archivebox.tests.test_cli_run.TestRunWithArchiveResult

```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunWithArchiveResult
```

````{py:method} test_run_requeues_failed_archiveresult(initialized_archive)
:canonical: archivebox.tests.test_cli_run.TestRunWithArchiveResult.test_run_requeues_failed_archiveresult

```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunWithArchiveResult.test_run_requeues_failed_archiveresult
```

````

`````

`````{py:class} TestRunPassThrough
:canonical: archivebox.tests.test_cli_run.TestRunPassThrough

```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunPassThrough
```

````{py:method} test_run_passes_through_unknown_types(initialized_archive)
:canonical: archivebox.tests.test_cli_run.TestRunPassThrough.test_run_passes_through_unknown_types

```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunPassThrough.test_run_passes_through_unknown_types
```

````

````{py:method} test_run_outputs_all_processed_records(initialized_archive)
:canonical: archivebox.tests.test_cli_run.TestRunPassThrough.test_run_outputs_all_processed_records

```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunPassThrough.test_run_outputs_all_processed_records
```

````

`````

`````{py:class} TestRunMixedInput
:canonical: archivebox.tests.test_cli_run.TestRunMixedInput

```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunMixedInput
```

````{py:method} test_run_handles_mixed_types(initialized_archive)
:canonical: archivebox.tests.test_cli_run.TestRunMixedInput.test_run_handles_mixed_types

```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunMixedInput.test_run_handles_mixed_types
```

````

`````

`````{py:class} TestRunEmpty
:canonical: archivebox.tests.test_cli_run.TestRunEmpty

```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunEmpty
```

````{py:method} test_run_empty_stdin(initialized_archive)
:canonical: archivebox.tests.test_cli_run.TestRunEmpty.test_run_empty_stdin

```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunEmpty.test_run_empty_stdin
```

````

````{py:method} test_run_no_records_to_process(initialized_archive)
:canonical: archivebox.tests.test_cli_run.TestRunEmpty.test_run_no_records_to_process

```{autodoc2-docstring} archivebox.tests.test_cli_run.TestRunEmpty.test_run_no_records_to_process
```

````

`````
