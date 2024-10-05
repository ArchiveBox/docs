# {py:mod}`archivebox.logging_util`

```{py:module} archivebox.logging_util
```

```{autodoc2-docstring} archivebox.logging_util
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`RuntimeStats <archivebox.logging_util.RuntimeStats>`
  - ```{autodoc2-docstring} archivebox.logging_util.RuntimeStats
    :summary:
    ```
* - {py:obj}`SmartFormatter <archivebox.logging_util.SmartFormatter>`
  - ```{autodoc2-docstring} archivebox.logging_util.SmartFormatter
    :summary:
    ```
* - {py:obj}`TimedProgress <archivebox.logging_util.TimedProgress>`
  - ```{autodoc2-docstring} archivebox.logging_util.TimedProgress
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`debug_dict_summary <archivebox.logging_util.debug_dict_summary>`
  - ```{autodoc2-docstring} archivebox.logging_util.debug_dict_summary
    :summary:
    ```
* - {py:obj}`get_fd_info <archivebox.logging_util.get_fd_info>`
  - ```{autodoc2-docstring} archivebox.logging_util.get_fd_info
    :summary:
    ```
* - {py:obj}`reject_stdin <archivebox.logging_util.reject_stdin>`
  - ```{autodoc2-docstring} archivebox.logging_util.reject_stdin
    :summary:
    ```
* - {py:obj}`accept_stdin <archivebox.logging_util.accept_stdin>`
  - ```{autodoc2-docstring} archivebox.logging_util.accept_stdin
    :summary:
    ```
* - {py:obj}`progress_bar <archivebox.logging_util.progress_bar>`
  - ```{autodoc2-docstring} archivebox.logging_util.progress_bar
    :summary:
    ```
* - {py:obj}`log_cli_command <archivebox.logging_util.log_cli_command>`
  - ```{autodoc2-docstring} archivebox.logging_util.log_cli_command
    :summary:
    ```
* - {py:obj}`log_importing_started <archivebox.logging_util.log_importing_started>`
  - ```{autodoc2-docstring} archivebox.logging_util.log_importing_started
    :summary:
    ```
* - {py:obj}`log_source_saved <archivebox.logging_util.log_source_saved>`
  - ```{autodoc2-docstring} archivebox.logging_util.log_source_saved
    :summary:
    ```
* - {py:obj}`log_parsing_finished <archivebox.logging_util.log_parsing_finished>`
  - ```{autodoc2-docstring} archivebox.logging_util.log_parsing_finished
    :summary:
    ```
* - {py:obj}`log_deduping_finished <archivebox.logging_util.log_deduping_finished>`
  - ```{autodoc2-docstring} archivebox.logging_util.log_deduping_finished
    :summary:
    ```
* - {py:obj}`log_crawl_started <archivebox.logging_util.log_crawl_started>`
  - ```{autodoc2-docstring} archivebox.logging_util.log_crawl_started
    :summary:
    ```
* - {py:obj}`log_indexing_process_started <archivebox.logging_util.log_indexing_process_started>`
  - ```{autodoc2-docstring} archivebox.logging_util.log_indexing_process_started
    :summary:
    ```
* - {py:obj}`log_indexing_process_finished <archivebox.logging_util.log_indexing_process_finished>`
  - ```{autodoc2-docstring} archivebox.logging_util.log_indexing_process_finished
    :summary:
    ```
* - {py:obj}`log_indexing_started <archivebox.logging_util.log_indexing_started>`
  - ```{autodoc2-docstring} archivebox.logging_util.log_indexing_started
    :summary:
    ```
* - {py:obj}`log_indexing_finished <archivebox.logging_util.log_indexing_finished>`
  - ```{autodoc2-docstring} archivebox.logging_util.log_indexing_finished
    :summary:
    ```
* - {py:obj}`log_archiving_started <archivebox.logging_util.log_archiving_started>`
  - ```{autodoc2-docstring} archivebox.logging_util.log_archiving_started
    :summary:
    ```
* - {py:obj}`log_archiving_paused <archivebox.logging_util.log_archiving_paused>`
  - ```{autodoc2-docstring} archivebox.logging_util.log_archiving_paused
    :summary:
    ```
* - {py:obj}`log_archiving_finished <archivebox.logging_util.log_archiving_finished>`
  - ```{autodoc2-docstring} archivebox.logging_util.log_archiving_finished
    :summary:
    ```
* - {py:obj}`log_link_archiving_started <archivebox.logging_util.log_link_archiving_started>`
  - ```{autodoc2-docstring} archivebox.logging_util.log_link_archiving_started
    :summary:
    ```
* - {py:obj}`log_link_archiving_finished <archivebox.logging_util.log_link_archiving_finished>`
  - ```{autodoc2-docstring} archivebox.logging_util.log_link_archiving_finished
    :summary:
    ```
* - {py:obj}`log_archive_method_started <archivebox.logging_util.log_archive_method_started>`
  - ```{autodoc2-docstring} archivebox.logging_util.log_archive_method_started
    :summary:
    ```
* - {py:obj}`log_archive_method_finished <archivebox.logging_util.log_archive_method_finished>`
  - ```{autodoc2-docstring} archivebox.logging_util.log_archive_method_finished
    :summary:
    ```
* - {py:obj}`log_list_started <archivebox.logging_util.log_list_started>`
  - ```{autodoc2-docstring} archivebox.logging_util.log_list_started
    :summary:
    ```
* - {py:obj}`log_list_finished <archivebox.logging_util.log_list_finished>`
  - ```{autodoc2-docstring} archivebox.logging_util.log_list_finished
    :summary:
    ```
* - {py:obj}`log_removal_started <archivebox.logging_util.log_removal_started>`
  - ```{autodoc2-docstring} archivebox.logging_util.log_removal_started
    :summary:
    ```
* - {py:obj}`log_removal_finished <archivebox.logging_util.log_removal_finished>`
  - ```{autodoc2-docstring} archivebox.logging_util.log_removal_finished
    :summary:
    ```
* - {py:obj}`pretty_path <archivebox.logging_util.pretty_path>`
  - ```{autodoc2-docstring} archivebox.logging_util.pretty_path
    :summary:
    ```
* - {py:obj}`printable_filesize <archivebox.logging_util.printable_filesize>`
  - ```{autodoc2-docstring} archivebox.logging_util.printable_filesize
    :summary:
    ```
* - {py:obj}`printable_folders <archivebox.logging_util.printable_folders>`
  - ```{autodoc2-docstring} archivebox.logging_util.printable_folders
    :summary:
    ```
* - {py:obj}`printable_config <archivebox.logging_util.printable_config>`
  - ```{autodoc2-docstring} archivebox.logging_util.printable_config
    :summary:
    ```
* - {py:obj}`printable_folder_status <archivebox.logging_util.printable_folder_status>`
  - ```{autodoc2-docstring} archivebox.logging_util.printable_folder_status
    :summary:
    ```
* - {py:obj}`printable_dependency_version <archivebox.logging_util.printable_dependency_version>`
  - ```{autodoc2-docstring} archivebox.logging_util.printable_dependency_version
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.logging_util.__package__>`
  - ```{autodoc2-docstring} archivebox.logging_util.__package__
    :summary:
    ```
* - {py:obj}`_LAST_RUN_STATS <archivebox.logging_util._LAST_RUN_STATS>`
  - ```{autodoc2-docstring} archivebox.logging_util._LAST_RUN_STATS
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.logging_util.__package__
:value: >
   'archivebox'

```{autodoc2-docstring} archivebox.logging_util.__package__
```

````

`````{py:class} RuntimeStats
:canonical: archivebox.logging_util.RuntimeStats

```{autodoc2-docstring} archivebox.logging_util.RuntimeStats
```

````{py:attribute} skipped
:canonical: archivebox.logging_util.RuntimeStats.skipped
:type: int
:value: >
   0

```{autodoc2-docstring} archivebox.logging_util.RuntimeStats.skipped
```

````

````{py:attribute} succeeded
:canonical: archivebox.logging_util.RuntimeStats.succeeded
:type: int
:value: >
   0

```{autodoc2-docstring} archivebox.logging_util.RuntimeStats.succeeded
```

````

````{py:attribute} failed
:canonical: archivebox.logging_util.RuntimeStats.failed
:type: int
:value: >
   0

```{autodoc2-docstring} archivebox.logging_util.RuntimeStats.failed
```

````

````{py:attribute} parse_start_ts
:canonical: archivebox.logging_util.RuntimeStats.parse_start_ts
:type: typing.Optional[datetime.datetime]
:value: >
   None

```{autodoc2-docstring} archivebox.logging_util.RuntimeStats.parse_start_ts
```

````

````{py:attribute} parse_end_ts
:canonical: archivebox.logging_util.RuntimeStats.parse_end_ts
:type: typing.Optional[datetime.datetime]
:value: >
   None

```{autodoc2-docstring} archivebox.logging_util.RuntimeStats.parse_end_ts
```

````

````{py:attribute} index_start_ts
:canonical: archivebox.logging_util.RuntimeStats.index_start_ts
:type: typing.Optional[datetime.datetime]
:value: >
   None

```{autodoc2-docstring} archivebox.logging_util.RuntimeStats.index_start_ts
```

````

````{py:attribute} index_end_ts
:canonical: archivebox.logging_util.RuntimeStats.index_end_ts
:type: typing.Optional[datetime.datetime]
:value: >
   None

```{autodoc2-docstring} archivebox.logging_util.RuntimeStats.index_end_ts
```

````

````{py:attribute} archiving_start_ts
:canonical: archivebox.logging_util.RuntimeStats.archiving_start_ts
:type: typing.Optional[datetime.datetime]
:value: >
   None

```{autodoc2-docstring} archivebox.logging_util.RuntimeStats.archiving_start_ts
```

````

````{py:attribute} archiving_end_ts
:canonical: archivebox.logging_util.RuntimeStats.archiving_end_ts
:type: typing.Optional[datetime.datetime]
:value: >
   None

```{autodoc2-docstring} archivebox.logging_util.RuntimeStats.archiving_end_ts
```

````

`````

````{py:data} _LAST_RUN_STATS
:canonical: archivebox.logging_util._LAST_RUN_STATS
:value: >
   'RuntimeStats(...)'

```{autodoc2-docstring} archivebox.logging_util._LAST_RUN_STATS
```

````

````{py:function} debug_dict_summary(obj: typing.Dict[typing.Any, typing.Any]) -> None
:canonical: archivebox.logging_util.debug_dict_summary

```{autodoc2-docstring} archivebox.logging_util.debug_dict_summary
```
````

````{py:function} get_fd_info(fd) -> typing.Dict[str, typing.Any]
:canonical: archivebox.logging_util.get_fd_info

```{autodoc2-docstring} archivebox.logging_util.get_fd_info
```
````

`````{py:class} SmartFormatter(prog, indent_increment=2, max_help_position=24, width=None)
:canonical: archivebox.logging_util.SmartFormatter

Bases: {py:obj}`django.core.management.base.DjangoHelpFormatter`, {py:obj}`rich_argparse.RichHelpFormatter`

```{autodoc2-docstring} archivebox.logging_util.SmartFormatter
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.logging_util.SmartFormatter.__init__
```

````{py:method} _split_lines(text, width)
:canonical: archivebox.logging_util.SmartFormatter._split_lines

```{autodoc2-docstring} archivebox.logging_util.SmartFormatter._split_lines
```

````

`````

````{py:function} reject_stdin(caller: str, stdin: typing.Optional[typing.IO] = sys.stdin) -> None
:canonical: archivebox.logging_util.reject_stdin

```{autodoc2-docstring} archivebox.logging_util.reject_stdin
```
````

````{py:function} accept_stdin(stdin: typing.Optional[typing.IO] = sys.stdin) -> typing.Optional[str]
:canonical: archivebox.logging_util.accept_stdin

```{autodoc2-docstring} archivebox.logging_util.accept_stdin
```
````

`````{py:class} TimedProgress(seconds, prefix='')
:canonical: archivebox.logging_util.TimedProgress

```{autodoc2-docstring} archivebox.logging_util.TimedProgress
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.logging_util.TimedProgress.__init__
```

````{py:method} end()
:canonical: archivebox.logging_util.TimedProgress.end

```{autodoc2-docstring} archivebox.logging_util.TimedProgress.end
```

````

`````

````{py:function} progress_bar(seconds: int, prefix: str = '', ANSI: typing.Dict[str, str] = ANSI) -> None
:canonical: archivebox.logging_util.progress_bar

```{autodoc2-docstring} archivebox.logging_util.progress_bar
```
````

````{py:function} log_cli_command(subcommand: str, subcommand_args: typing.List[str], stdin: typing.Optional[str | typing.IO], pwd: str = '.')
:canonical: archivebox.logging_util.log_cli_command

```{autodoc2-docstring} archivebox.logging_util.log_cli_command
```
````

````{py:function} log_importing_started(urls: typing.Union[str, typing.List[str]], depth: int, index_only: bool)
:canonical: archivebox.logging_util.log_importing_started

```{autodoc2-docstring} archivebox.logging_util.log_importing_started
```
````

````{py:function} log_source_saved(source_file: str)
:canonical: archivebox.logging_util.log_source_saved

```{autodoc2-docstring} archivebox.logging_util.log_source_saved
```
````

````{py:function} log_parsing_finished(num_parsed: int, parser_name: str)
:canonical: archivebox.logging_util.log_parsing_finished

```{autodoc2-docstring} archivebox.logging_util.log_parsing_finished
```
````

````{py:function} log_deduping_finished(num_new_links: int)
:canonical: archivebox.logging_util.log_deduping_finished

```{autodoc2-docstring} archivebox.logging_util.log_deduping_finished
```
````

````{py:function} log_crawl_started(new_links)
:canonical: archivebox.logging_util.log_crawl_started

```{autodoc2-docstring} archivebox.logging_util.log_crawl_started
```
````

````{py:function} log_indexing_process_started(num_links: int)
:canonical: archivebox.logging_util.log_indexing_process_started

```{autodoc2-docstring} archivebox.logging_util.log_indexing_process_started
```
````

````{py:function} log_indexing_process_finished()
:canonical: archivebox.logging_util.log_indexing_process_finished

```{autodoc2-docstring} archivebox.logging_util.log_indexing_process_finished
```
````

````{py:function} log_indexing_started(out_path: str)
:canonical: archivebox.logging_util.log_indexing_started

```{autodoc2-docstring} archivebox.logging_util.log_indexing_started
```
````

````{py:function} log_indexing_finished(out_path: str)
:canonical: archivebox.logging_util.log_indexing_finished

```{autodoc2-docstring} archivebox.logging_util.log_indexing_finished
```
````

````{py:function} log_archiving_started(num_links: int, resume: typing.Optional[float] = None)
:canonical: archivebox.logging_util.log_archiving_started

```{autodoc2-docstring} archivebox.logging_util.log_archiving_started
```
````

````{py:function} log_archiving_paused(num_links: int, idx: int, timestamp: str)
:canonical: archivebox.logging_util.log_archiving_paused

```{autodoc2-docstring} archivebox.logging_util.log_archiving_paused
```
````

````{py:function} log_archiving_finished(num_links: int)
:canonical: archivebox.logging_util.log_archiving_finished

```{autodoc2-docstring} archivebox.logging_util.log_archiving_finished
```
````

````{py:function} log_link_archiving_started(link: archivebox.index.schema.Link, link_dir: str, is_new: bool)
:canonical: archivebox.logging_util.log_link_archiving_started

```{autodoc2-docstring} archivebox.logging_util.log_link_archiving_started
```
````

````{py:function} log_link_archiving_finished(link: archivebox.index.schema.Link, link_dir: str, is_new: bool, stats: dict, start_ts: datetime.datetime)
:canonical: archivebox.logging_util.log_link_archiving_finished

```{autodoc2-docstring} archivebox.logging_util.log_link_archiving_finished
```
````

````{py:function} log_archive_method_started(method: str)
:canonical: archivebox.logging_util.log_archive_method_started

```{autodoc2-docstring} archivebox.logging_util.log_archive_method_started
```
````

````{py:function} log_archive_method_finished(result: archivebox.index.schema.ArchiveResult)
:canonical: archivebox.logging_util.log_archive_method_finished

```{autodoc2-docstring} archivebox.logging_util.log_archive_method_finished
```
````

````{py:function} log_list_started(filter_patterns: typing.Optional[typing.List[str]], filter_type: str)
:canonical: archivebox.logging_util.log_list_started

```{autodoc2-docstring} archivebox.logging_util.log_list_started
```
````

````{py:function} log_list_finished(links)
:canonical: archivebox.logging_util.log_list_finished

```{autodoc2-docstring} archivebox.logging_util.log_list_finished
```
````

````{py:function} log_removal_started(links: typing.List[archivebox.index.schema.Link], yes: bool, delete: bool)
:canonical: archivebox.logging_util.log_removal_started

```{autodoc2-docstring} archivebox.logging_util.log_removal_started
```
````

````{py:function} log_removal_finished(all_links: int, to_remove: int)
:canonical: archivebox.logging_util.log_removal_finished

```{autodoc2-docstring} archivebox.logging_util.log_removal_finished
```
````

````{py:function} pretty_path(path: typing.Union[pathlib.Path, str], pwd: typing.Union[pathlib.Path, str] = DATA_DIR) -> str
:canonical: archivebox.logging_util.pretty_path

```{autodoc2-docstring} archivebox.logging_util.pretty_path
```
````

````{py:function} printable_filesize(num_bytes: typing.Union[int, float]) -> str
:canonical: archivebox.logging_util.printable_filesize

```{autodoc2-docstring} archivebox.logging_util.printable_filesize
```
````

````{py:function} printable_folders(folders: typing.Dict[str, typing.Optional[archivebox.index.schema.Link]], with_headers: bool = False) -> str
:canonical: archivebox.logging_util.printable_folders

```{autodoc2-docstring} archivebox.logging_util.printable_folders
```
````

````{py:function} printable_config(config: dict, prefix: str = '') -> str
:canonical: archivebox.logging_util.printable_config

```{autodoc2-docstring} archivebox.logging_util.printable_config
```
````

````{py:function} printable_folder_status(name: str, folder: typing.Dict) -> str
:canonical: archivebox.logging_util.printable_folder_status

```{autodoc2-docstring} archivebox.logging_util.printable_folder_status
```
````

````{py:function} printable_dependency_version(name: str, dependency: typing.Dict) -> str
:canonical: archivebox.logging_util.printable_dependency_version

```{autodoc2-docstring} archivebox.logging_util.printable_dependency_version
```
````
