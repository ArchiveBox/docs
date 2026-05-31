# {py:mod}`archivebox.cli.archivebox_run`

```{py:module} archivebox.cli.archivebox_run
```

```{autodoc2-docstring} archivebox.cli.archivebox_run
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`process_stdin_records <archivebox.cli.archivebox_run.process_stdin_records>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_run.process_stdin_records
    :summary:
    ```
* - {py:obj}`run_runner <archivebox.cli.archivebox_run.run_runner>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_run.run_runner
    :summary:
    ```
* - {py:obj}`main <archivebox.cli.archivebox_run.main>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_run.main
    :summary:
    ```
* - {py:obj}`run_snapshot_worker <archivebox.cli.archivebox_run.run_snapshot_worker>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_run.run_snapshot_worker
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__command__ <archivebox.cli.archivebox_run.__command__>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_run.__command__
    :summary:
    ```
````

### API

````{py:data} __command__
:canonical: archivebox.cli.archivebox_run.__command__
:value: >
   'archivebox run'

```{autodoc2-docstring} archivebox.cli.archivebox_run.__command__
```

````

````{py:function} process_stdin_records() -> int
:canonical: archivebox.cli.archivebox_run.process_stdin_records

```{autodoc2-docstring} archivebox.cli.archivebox_run.process_stdin_records
```
````

````{py:function} run_runner(daemon: bool = False, crawl_id: str | None = None, maintenance_only: bool = False) -> int
:canonical: archivebox.cli.archivebox_run.run_runner

```{autodoc2-docstring} archivebox.cli.archivebox_run.run_runner
```
````

````{py:function} main(daemon: bool, crawl_id: str, snapshot_id: str, binary_id: str, maintenance_only: bool)
:canonical: archivebox.cli.archivebox_run.main

```{autodoc2-docstring} archivebox.cli.archivebox_run.main
```
````

````{py:function} run_snapshot_worker(snapshot_id: str) -> int
:canonical: archivebox.cli.archivebox_run.run_snapshot_worker

```{autodoc2-docstring} archivebox.cli.archivebox_run.run_snapshot_worker
```
````
