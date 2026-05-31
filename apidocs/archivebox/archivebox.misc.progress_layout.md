# {py:mod}`archivebox.misc.progress_layout`

```{py:module} archivebox.misc.progress_layout
```

```{autodoc2-docstring} archivebox.misc.progress_layout
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CrawlQueuePanel <archivebox.misc.progress_layout.CrawlQueuePanel>`
  - ```{autodoc2-docstring} archivebox.misc.progress_layout.CrawlQueuePanel
    :summary:
    ```
* - {py:obj}`ProcessLogPanel <archivebox.misc.progress_layout.ProcessLogPanel>`
  - ```{autodoc2-docstring} archivebox.misc.progress_layout.ProcessLogPanel
    :summary:
    ```
* - {py:obj}`WorkerLogPanel <archivebox.misc.progress_layout.WorkerLogPanel>`
  - ```{autodoc2-docstring} archivebox.misc.progress_layout.WorkerLogPanel
    :summary:
    ```
* - {py:obj}`CrawlQueueTreePanel <archivebox.misc.progress_layout.CrawlQueueTreePanel>`
  - ```{autodoc2-docstring} archivebox.misc.progress_layout.CrawlQueueTreePanel
    :summary:
    ```
* - {py:obj}`ArchiveBoxProgressLayout <archivebox.misc.progress_layout.ArchiveBoxProgressLayout>`
  - ```{autodoc2-docstring} archivebox.misc.progress_layout.ArchiveBoxProgressLayout
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_strip_rich <archivebox.misc.progress_layout._strip_rich>`
  - ```{autodoc2-docstring} archivebox.misc.progress_layout._strip_rich
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_RICH_TAG_RE <archivebox.misc.progress_layout._RICH_TAG_RE>`
  - ```{autodoc2-docstring} archivebox.misc.progress_layout._RICH_TAG_RE
    :summary:
    ```
````

### API

````{py:data} _RICH_TAG_RE
:canonical: archivebox.misc.progress_layout._RICH_TAG_RE
:value: >
   'compile(...)'

```{autodoc2-docstring} archivebox.misc.progress_layout._RICH_TAG_RE
```

````

````{py:function} _strip_rich(text: str) -> str
:canonical: archivebox.misc.progress_layout._strip_rich

```{autodoc2-docstring} archivebox.misc.progress_layout._strip_rich
```
````

`````{py:class} CrawlQueuePanel()
:canonical: archivebox.misc.progress_layout.CrawlQueuePanel

```{autodoc2-docstring} archivebox.misc.progress_layout.CrawlQueuePanel
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.misc.progress_layout.CrawlQueuePanel.__init__
```

````{py:method} __rich__() -> rich.panel.Panel
:canonical: archivebox.misc.progress_layout.CrawlQueuePanel.__rich__

```{autodoc2-docstring} archivebox.misc.progress_layout.CrawlQueuePanel.__rich__
```

````

`````

`````{py:class} ProcessLogPanel(process: typing.Any, max_lines: int = 8, compact: bool | None = None, bg_terminating: bool = False)
:canonical: archivebox.misc.progress_layout.ProcessLogPanel

```{autodoc2-docstring} archivebox.misc.progress_layout.ProcessLogPanel
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.misc.progress_layout.ProcessLogPanel.__init__
```

````{py:method} __rich__() -> rich.panel.Panel
:canonical: archivebox.misc.progress_layout.ProcessLogPanel.__rich__

```{autodoc2-docstring} archivebox.misc.progress_layout.ProcessLogPanel.__rich__
```

````

````{py:method} plain_lines() -> list[str]
:canonical: archivebox.misc.progress_layout.ProcessLogPanel.plain_lines

```{autodoc2-docstring} archivebox.misc.progress_layout.ProcessLogPanel.plain_lines
```

````

````{py:method} _title() -> str
:canonical: archivebox.misc.progress_layout.ProcessLogPanel._title

```{autodoc2-docstring} archivebox.misc.progress_layout.ProcessLogPanel._title
```

````

````{py:method} _is_background_hook() -> bool
:canonical: archivebox.misc.progress_layout.ProcessLogPanel._is_background_hook

```{autodoc2-docstring} archivebox.misc.progress_layout.ProcessLogPanel._is_background_hook
```

````

````{py:method} _is_pending() -> bool
:canonical: archivebox.misc.progress_layout.ProcessLogPanel._is_pending

```{autodoc2-docstring} archivebox.misc.progress_layout.ProcessLogPanel._is_pending
```

````

````{py:method} _completed_ok() -> bool
:canonical: archivebox.misc.progress_layout.ProcessLogPanel._completed_ok

```{autodoc2-docstring} archivebox.misc.progress_layout.ProcessLogPanel._completed_ok
```

````

````{py:method} _completed_output_line() -> str
:canonical: archivebox.misc.progress_layout.ProcessLogPanel._completed_output_line

```{autodoc2-docstring} archivebox.misc.progress_layout.ProcessLogPanel._completed_output_line
```

````

````{py:method} _has_output_files() -> bool
:canonical: archivebox.misc.progress_layout.ProcessLogPanel._has_output_files

```{autodoc2-docstring} archivebox.misc.progress_layout.ProcessLogPanel._has_output_files
```

````

````{py:method} _border_style(is_pending: bool) -> str
:canonical: archivebox.misc.progress_layout.ProcessLogPanel._border_style

```{autodoc2-docstring} archivebox.misc.progress_layout.ProcessLogPanel._border_style
```

````

````{py:method} _worker_label(worker_type: str) -> tuple[str, str]
:canonical: archivebox.misc.progress_layout.ProcessLogPanel._worker_label

```{autodoc2-docstring} archivebox.misc.progress_layout.ProcessLogPanel._worker_label
```

````

````{py:method} _extract_arg(cmd: list[str], key: str) -> str | None
:canonical: archivebox.misc.progress_layout.ProcessLogPanel._extract_arg
:staticmethod:

```{autodoc2-docstring} archivebox.misc.progress_layout.ProcessLogPanel._extract_arg
```

````

````{py:method} _abbrev_urls(urls: list[str], max_len: int = 48) -> str
:canonical: archivebox.misc.progress_layout.ProcessLogPanel._abbrev_urls

```{autodoc2-docstring} archivebox.misc.progress_layout.ProcessLogPanel._abbrev_urls
```

````

````{py:method} _extract_url() -> str
:canonical: archivebox.misc.progress_layout.ProcessLogPanel._extract_url

```{autodoc2-docstring} archivebox.misc.progress_layout.ProcessLogPanel._extract_url
```

````

````{py:method} _abbrev_url(url: str, max_len: int = 48) -> str
:canonical: archivebox.misc.progress_layout.ProcessLogPanel._abbrev_url

```{autodoc2-docstring} archivebox.misc.progress_layout.ProcessLogPanel._abbrev_url
```

````

````{py:method} _chrome_launch_line(stderr_lines: list[str], stdout_lines: list[str]) -> str
:canonical: archivebox.misc.progress_layout.ProcessLogPanel._chrome_launch_line

```{autodoc2-docstring} archivebox.misc.progress_layout.ProcessLogPanel._chrome_launch_line
```

````

````{py:method} _elapsed_suffix() -> str
:canonical: archivebox.misc.progress_layout.ProcessLogPanel._elapsed_suffix

```{autodoc2-docstring} archivebox.misc.progress_layout.ProcessLogPanel._elapsed_suffix
```

````

````{py:method} _output_line() -> str
:canonical: archivebox.misc.progress_layout.ProcessLogPanel._output_line

```{autodoc2-docstring} archivebox.misc.progress_layout.ProcessLogPanel._output_line
```

````

`````

`````{py:class} WorkerLogPanel(title: str, empty_message: str, running_message: str, max_lines: int = 8)
:canonical: archivebox.misc.progress_layout.WorkerLogPanel

```{autodoc2-docstring} archivebox.misc.progress_layout.WorkerLogPanel
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.misc.progress_layout.WorkerLogPanel.__init__
```

````{py:method} update_from_process(process: typing.Any)
:canonical: archivebox.misc.progress_layout.WorkerLogPanel.update_from_process

```{autodoc2-docstring} archivebox.misc.progress_layout.WorkerLogPanel.update_from_process
```

````

````{py:method} __rich__() -> rich.panel.Panel
:canonical: archivebox.misc.progress_layout.WorkerLogPanel.__rich__

```{autodoc2-docstring} archivebox.misc.progress_layout.WorkerLogPanel.__rich__
```

````

`````

`````{py:class} CrawlQueueTreePanel(max_crawls: int = 8, max_snapshots: int = 16)
:canonical: archivebox.misc.progress_layout.CrawlQueueTreePanel

```{autodoc2-docstring} archivebox.misc.progress_layout.CrawlQueueTreePanel
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.misc.progress_layout.CrawlQueueTreePanel.__init__
```

````{py:method} update_crawls(crawls: list[dict[str, typing.Any]]) -> None
:canonical: archivebox.misc.progress_layout.CrawlQueueTreePanel.update_crawls

```{autodoc2-docstring} archivebox.misc.progress_layout.CrawlQueueTreePanel.update_crawls
```

````

````{py:method} __rich__() -> rich.panel.Panel
:canonical: archivebox.misc.progress_layout.CrawlQueueTreePanel.__rich__

```{autodoc2-docstring} archivebox.misc.progress_layout.CrawlQueueTreePanel.__rich__
```

````

````{py:method} _status_icon(status: str) -> str
:canonical: archivebox.misc.progress_layout.CrawlQueueTreePanel._status_icon
:staticmethod:

```{autodoc2-docstring} archivebox.misc.progress_layout.CrawlQueueTreePanel._status_icon
```

````

````{py:method} _hook_style(status: str, is_bg: bool = False, is_running: bool = False, is_pending: bool = False) -> tuple[str, str]
:canonical: archivebox.misc.progress_layout.CrawlQueueTreePanel._hook_style
:staticmethod:

```{autodoc2-docstring} archivebox.misc.progress_layout.CrawlQueueTreePanel._hook_style
```

````

````{py:method} _hook_stats(size: str = '', elapsed: str = '', timeout: str = '', status: str = '') -> str
:canonical: archivebox.misc.progress_layout.CrawlQueueTreePanel._hook_stats
:staticmethod:

```{autodoc2-docstring} archivebox.misc.progress_layout.CrawlQueueTreePanel._hook_stats
```

````

````{py:method} _terminal_width() -> int
:canonical: archivebox.misc.progress_layout.CrawlQueueTreePanel._terminal_width
:staticmethod:

```{autodoc2-docstring} archivebox.misc.progress_layout.CrawlQueueTreePanel._terminal_width
```

````

````{py:method} _truncate_to_width(text: str, max_width: int) -> str
:canonical: archivebox.misc.progress_layout.CrawlQueueTreePanel._truncate_to_width
:staticmethod:

```{autodoc2-docstring} archivebox.misc.progress_layout.CrawlQueueTreePanel._truncate_to_width
```

````

````{py:method} _truncate_tail(text: str, max_width: int) -> str
:canonical: archivebox.misc.progress_layout.CrawlQueueTreePanel._truncate_tail
:staticmethod:

```{autodoc2-docstring} archivebox.misc.progress_layout.CrawlQueueTreePanel._truncate_tail
```

````

````{py:method} _available_width(left_text: str, indent: int = 0) -> int
:canonical: archivebox.misc.progress_layout.CrawlQueueTreePanel._available_width

```{autodoc2-docstring} archivebox.misc.progress_layout.CrawlQueueTreePanel._available_width
```

````

`````

`````{py:class} ArchiveBoxProgressLayout(crawl_id: typing.Optional[str] = None)
:canonical: archivebox.misc.progress_layout.ArchiveBoxProgressLayout

```{autodoc2-docstring} archivebox.misc.progress_layout.ArchiveBoxProgressLayout
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.misc.progress_layout.ArchiveBoxProgressLayout.__init__
```

````{py:method} _make_layout() -> rich.layout.Layout
:canonical: archivebox.misc.progress_layout.ArchiveBoxProgressLayout._make_layout

```{autodoc2-docstring} archivebox.misc.progress_layout.ArchiveBoxProgressLayout._make_layout
```

````

````{py:method} update_orchestrator_status(status: str, crawl_queue_count: int = 0, crawl_workers_count: int = 0, binary_queue_count: int = 0, binary_workers_count: int = 0, max_crawl_workers: int = 8)
:canonical: archivebox.misc.progress_layout.ArchiveBoxProgressLayout.update_orchestrator_status

```{autodoc2-docstring} archivebox.misc.progress_layout.ArchiveBoxProgressLayout.update_orchestrator_status
```

````

````{py:method} update_process_panels(processes: typing.List[typing.Any], pending: typing.Optional[typing.List[typing.Any]] = None) -> None
:canonical: archivebox.misc.progress_layout.ArchiveBoxProgressLayout.update_process_panels

```{autodoc2-docstring} archivebox.misc.progress_layout.ArchiveBoxProgressLayout.update_process_panels
```

````

````{py:method} update_crawl_tree(crawls: list[dict[str, typing.Any]]) -> None
:canonical: archivebox.misc.progress_layout.ArchiveBoxProgressLayout.update_crawl_tree

```{autodoc2-docstring} archivebox.misc.progress_layout.ArchiveBoxProgressLayout.update_crawl_tree
```

````

````{py:method} log_event(message: str, style: str = 'white') -> None
:canonical: archivebox.misc.progress_layout.ArchiveBoxProgressLayout.log_event

```{autodoc2-docstring} archivebox.misc.progress_layout.ArchiveBoxProgressLayout.log_event
```

````

````{py:method} get_layout() -> rich.layout.Layout
:canonical: archivebox.misc.progress_layout.ArchiveBoxProgressLayout.get_layout

```{autodoc2-docstring} archivebox.misc.progress_layout.ArchiveBoxProgressLayout.get_layout
```

````

````{py:method} plain_lines() -> list[tuple[str, str]]
:canonical: archivebox.misc.progress_layout.ArchiveBoxProgressLayout.plain_lines

```{autodoc2-docstring} archivebox.misc.progress_layout.ArchiveBoxProgressLayout.plain_lines
```

````

````{py:method} _has_log_lines(process: typing.Any) -> bool
:canonical: archivebox.misc.progress_layout.ArchiveBoxProgressLayout._has_log_lines
:staticmethod:

```{autodoc2-docstring} archivebox.misc.progress_layout.ArchiveBoxProgressLayout._has_log_lines
```

````

`````
