# {py:mod}`archivebox.misc.system`

```{py:module} archivebox.misc.system
```

```{autodoc2-docstring} archivebox.misc.system
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`suppress_output <archivebox.misc.system.suppress_output>`
  - ```{autodoc2-docstring} archivebox.misc.system.suppress_output
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`run <archivebox.misc.system.run>`
  - ```{autodoc2-docstring} archivebox.misc.system.run
    :summary:
    ```
* - {py:obj}`atomic_write <archivebox.misc.system.atomic_write>`
  - ```{autodoc2-docstring} archivebox.misc.system.atomic_write
    :summary:
    ```
* - {py:obj}`chmod_file <archivebox.misc.system.chmod_file>`
  - ```{autodoc2-docstring} archivebox.misc.system.chmod_file
    :summary:
    ```
* - {py:obj}`copy_and_overwrite <archivebox.misc.system.copy_and_overwrite>`
  - ```{autodoc2-docstring} archivebox.misc.system.copy_and_overwrite
    :summary:
    ```
* - {py:obj}`get_dir_size <archivebox.misc.system.get_dir_size>`
  - ```{autodoc2-docstring} archivebox.misc.system.get_dir_size
    :summary:
    ```
* - {py:obj}`dedupe_cron_jobs <archivebox.misc.system.dedupe_cron_jobs>`
  - ```{autodoc2-docstring} archivebox.misc.system.dedupe_cron_jobs
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CRON_COMMENT <archivebox.misc.system.CRON_COMMENT>`
  - ```{autodoc2-docstring} archivebox.misc.system.CRON_COMMENT
    :summary:
    ```
````

### API

````{py:function} run(cmd, *args, input=None, capture_output=True, timeout=None, check=False, text=False, start_new_session=True, **kwargs)
:canonical: archivebox.misc.system.run

```{autodoc2-docstring} archivebox.misc.system.run
```
````

````{py:function} atomic_write(path: typing.Union[pathlib.Path, str], contents: typing.Union[dict, str, bytes], overwrite: bool = True) -> None
:canonical: archivebox.misc.system.atomic_write

```{autodoc2-docstring} archivebox.misc.system.atomic_write
```
````

````{py:function} chmod_file(path: str, cwd: str = '') -> None
:canonical: archivebox.misc.system.chmod_file

```{autodoc2-docstring} archivebox.misc.system.chmod_file
```
````

````{py:function} copy_and_overwrite(from_path: typing.Union[str, pathlib.Path], to_path: typing.Union[str, pathlib.Path])
:canonical: archivebox.misc.system.copy_and_overwrite

```{autodoc2-docstring} archivebox.misc.system.copy_and_overwrite
```
````

````{py:function} get_dir_size(path: typing.Union[str, pathlib.Path], recursive: bool = True, pattern: typing.Optional[str] = None) -> typing.Tuple[int, int, int]
:canonical: archivebox.misc.system.get_dir_size

```{autodoc2-docstring} archivebox.misc.system.get_dir_size
```
````

````{py:data} CRON_COMMENT
:canonical: archivebox.misc.system.CRON_COMMENT
:value: >
   'archivebox_schedule'

```{autodoc2-docstring} archivebox.misc.system.CRON_COMMENT
```

````

````{py:function} dedupe_cron_jobs(cron: crontab.CronTab) -> crontab.CronTab
:canonical: archivebox.misc.system.dedupe_cron_jobs

```{autodoc2-docstring} archivebox.misc.system.dedupe_cron_jobs
```
````

`````{py:class} suppress_output(stdout=True, stderr=True)
:canonical: archivebox.misc.system.suppress_output

Bases: {py:obj}`object`

```{autodoc2-docstring} archivebox.misc.system.suppress_output
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.misc.system.suppress_output.__init__
```

````{py:method} __enter__()
:canonical: archivebox.misc.system.suppress_output.__enter__

```{autodoc2-docstring} archivebox.misc.system.suppress_output.__enter__
```

````

````{py:method} __exit__(*_)
:canonical: archivebox.misc.system.suppress_output.__exit__

```{autodoc2-docstring} archivebox.misc.system.suppress_output.__exit__
```

````

`````
