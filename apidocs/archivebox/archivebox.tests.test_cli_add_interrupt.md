# {py:mod}`archivebox.tests.test_cli_add_interrupt`

```{py:module} archivebox.tests.test_cli_add_interrupt
```

```{autodoc2-docstring} archivebox.tests.test_cli_add_interrupt
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_run <archivebox.tests.test_cli_add_interrupt._run>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_add_interrupt._run
    :summary:
    ```
* - {py:obj}`_make_env <archivebox.tests.test_cli_add_interrupt._make_env>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_add_interrupt._make_env
    :summary:
    ```
* - {py:obj}`_count_running_processes <archivebox.tests.test_cli_add_interrupt._count_running_processes>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_add_interrupt._count_running_processes
    :summary:
    ```
* - {py:obj}`_wait_for_count <archivebox.tests.test_cli_add_interrupt._wait_for_count>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_add_interrupt._wait_for_count
    :summary:
    ```
* - {py:obj}`test_add_parents_workers_to_orchestrator <archivebox.tests.test_cli_add_interrupt.test_add_parents_workers_to_orchestrator>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_add_interrupt.test_add_parents_workers_to_orchestrator
    :summary:
    ```
* - {py:obj}`test_add_interrupt_cleans_orphaned_processes <archivebox.tests.test_cli_add_interrupt.test_add_interrupt_cleans_orphaned_processes>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_add_interrupt.test_add_interrupt_cleans_orphaned_processes
    :summary:
    ```
````

### API

````{py:function} _run(cmd, data_dir: pathlib.Path, env: dict, timeout: int = 120)
:canonical: archivebox.tests.test_cli_add_interrupt._run

```{autodoc2-docstring} archivebox.tests.test_cli_add_interrupt._run
```
````

````{py:function} _make_env(data_dir: pathlib.Path) -> dict
:canonical: archivebox.tests.test_cli_add_interrupt._make_env

```{autodoc2-docstring} archivebox.tests.test_cli_add_interrupt._make_env
```
````

````{py:function} _count_running_processes(db_path: pathlib.Path, where: str) -> int
:canonical: archivebox.tests.test_cli_add_interrupt._count_running_processes

```{autodoc2-docstring} archivebox.tests.test_cli_add_interrupt._count_running_processes
```
````

````{py:function} _wait_for_count(db_path: pathlib.Path, where: str, target: int, timeout: int = 20) -> bool
:canonical: archivebox.tests.test_cli_add_interrupt._wait_for_count

```{autodoc2-docstring} archivebox.tests.test_cli_add_interrupt._wait_for_count
```
````

````{py:function} test_add_parents_workers_to_orchestrator(tmp_path)
:canonical: archivebox.tests.test_cli_add_interrupt.test_add_parents_workers_to_orchestrator

```{autodoc2-docstring} archivebox.tests.test_cli_add_interrupt.test_add_parents_workers_to_orchestrator
```
````

````{py:function} test_add_interrupt_cleans_orphaned_processes(tmp_path)
:canonical: archivebox.tests.test_cli_add_interrupt.test_add_interrupt_cleans_orphaned_processes

```{autodoc2-docstring} archivebox.tests.test_cli_add_interrupt.test_add_interrupt_cleans_orphaned_processes
```
````
