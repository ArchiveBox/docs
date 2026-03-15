# {py:mod}`archivebox.tests.test_cli_run_binary_worker`

```{py:module} archivebox.tests.test_cli_run_binary_worker
```

```{autodoc2-docstring} archivebox.tests.test_cli_run_binary_worker
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestBinaryWorkerSpawning <archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerSpawning>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerSpawning
    :summary:
    ```
* - {py:obj}`TestBinaryWorkerHooks <archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerHooks>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerHooks
    :summary:
    ```
* - {py:obj}`TestBinaryWorkerEdgeCases <archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerEdgeCases>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerEdgeCases
    :summary:
    ```
````

### API

`````{py:class} TestBinaryWorkerSpawning
:canonical: archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerSpawning

```{autodoc2-docstring} archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerSpawning
```

````{py:method} test_binary_worker_spawns_when_binary_queued(initialized_archive)
:canonical: archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerSpawning.test_binary_worker_spawns_when_binary_queued

```{autodoc2-docstring} archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerSpawning.test_binary_worker_spawns_when_binary_queued
```

````

````{py:method} test_binary_hooks_actually_run(initialized_archive)
:canonical: archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerSpawning.test_binary_hooks_actually_run

```{autodoc2-docstring} archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerSpawning.test_binary_hooks_actually_run
```

````

````{py:method} test_binary_status_transitions(initialized_archive)
:canonical: archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerSpawning.test_binary_status_transitions

```{autodoc2-docstring} archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerSpawning.test_binary_status_transitions
```

````

`````

`````{py:class} TestBinaryWorkerHooks
:canonical: archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerHooks

```{autodoc2-docstring} archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerHooks
```

````{py:method} test_env_provider_hook_detects_system_binary(initialized_archive)
:canonical: archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerHooks.test_env_provider_hook_detects_system_binary

```{autodoc2-docstring} archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerHooks.test_env_provider_hook_detects_system_binary
```

````

````{py:method} test_multiple_binaries_processed_in_batch(initialized_archive)
:canonical: archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerHooks.test_multiple_binaries_processed_in_batch

```{autodoc2-docstring} archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerHooks.test_multiple_binaries_processed_in_batch
```

````

````{py:method} test_puppeteer_binary_sets_skip_download_for_hooks(initialized_archive)
:canonical: archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerHooks.test_puppeteer_binary_sets_skip_download_for_hooks

```{autodoc2-docstring} archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerHooks.test_puppeteer_binary_sets_skip_download_for_hooks
```

````

`````

`````{py:class} TestBinaryWorkerEdgeCases
:canonical: archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerEdgeCases

```{autodoc2-docstring} archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerEdgeCases
```

````{py:method} test_nonexistent_binary_stays_queued(initialized_archive)
:canonical: archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerEdgeCases.test_nonexistent_binary_stays_queued

```{autodoc2-docstring} archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerEdgeCases.test_nonexistent_binary_stays_queued
```

````

````{py:method} test_binary_worker_respects_machine_isolation(initialized_archive)
:canonical: archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerEdgeCases.test_binary_worker_respects_machine_isolation

```{autodoc2-docstring} archivebox.tests.test_cli_run_binary_worker.TestBinaryWorkerEdgeCases.test_binary_worker_respects_machine_isolation
```

````

`````
