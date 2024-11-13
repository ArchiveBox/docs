# {py:mod}`archivebox.cli`

```{py:module} archivebox.cli
```

```{autodoc2-docstring} archivebox.cli
:allowtitles:
```

## Submodules

```{toctree}
:titlesonly:
:maxdepth: 1

archivebox.cli.archivebox_shell
archivebox.cli.archivebox_schedule
archivebox.cli.archivebox_list
archivebox.cli.archivebox_config
archivebox.cli.archivebox_server
archivebox.cli.archivebox_update
archivebox.cli.archivebox_remove
archivebox.cli.archivebox_install
archivebox.cli.archivebox_version
archivebox.cli.archivebox_add
archivebox.cli.archivebox_status
archivebox.cli.archivebox_init
archivebox.cli.archivebox_oneshot
archivebox.cli.archivebox_help
archivebox.cli.archivebox_manage
```

## Package Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`LazySubcommands <archivebox.cli.LazySubcommands>`
  -
* - {py:obj}`NotProvided <archivebox.cli.NotProvided>`
  - ```{autodoc2-docstring} archivebox.cli.NotProvided
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`wait_for_bg_threads_to_exit <archivebox.cli.wait_for_bg_threads_to_exit>`
  - ```{autodoc2-docstring} archivebox.cli.wait_for_bg_threads_to_exit
    :summary:
    ```
* - {py:obj}`run_subcommand <archivebox.cli.run_subcommand>`
  - ```{autodoc2-docstring} archivebox.cli.run_subcommand
    :summary:
    ```
* - {py:obj}`main <archivebox.cli.main>`
  - ```{autodoc2-docstring} archivebox.cli.main
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.cli.__package__>`
  - ```{autodoc2-docstring} archivebox.cli.__package__
    :summary:
    ```
* - {py:obj}`__command__ <archivebox.cli.__command__>`
  - ```{autodoc2-docstring} archivebox.cli.__command__
    :summary:
    ```
* - {py:obj}`BUILTIN_LIST <archivebox.cli.BUILTIN_LIST>`
  - ```{autodoc2-docstring} archivebox.cli.BUILTIN_LIST
    :summary:
    ```
* - {py:obj}`CLI_DIR <archivebox.cli.CLI_DIR>`
  - ```{autodoc2-docstring} archivebox.cli.CLI_DIR
    :summary:
    ```
* - {py:obj}`SUBCOMMAND_MODULES <archivebox.cli.SUBCOMMAND_MODULES>`
  - ```{autodoc2-docstring} archivebox.cli.SUBCOMMAND_MODULES
    :summary:
    ```
* - {py:obj}`required_attrs <archivebox.cli.required_attrs>`
  - ```{autodoc2-docstring} archivebox.cli.required_attrs
    :summary:
    ```
* - {py:obj}`is_cli_module <archivebox.cli.is_cli_module>`
  - ```{autodoc2-docstring} archivebox.cli.is_cli_module
    :summary:
    ```
* - {py:obj}`is_valid_cli_module <archivebox.cli.is_valid_cli_module>`
  - ```{autodoc2-docstring} archivebox.cli.is_valid_cli_module
    :summary:
    ```
* - {py:obj}`CLI_SUBCOMMANDS <archivebox.cli.CLI_SUBCOMMANDS>`
  - ```{autodoc2-docstring} archivebox.cli.CLI_SUBCOMMANDS
    :summary:
    ```
* - {py:obj}`meta_cmds <archivebox.cli.meta_cmds>`
  - ```{autodoc2-docstring} archivebox.cli.meta_cmds
    :summary:
    ```
* - {py:obj}`setup_cmds <archivebox.cli.setup_cmds>`
  - ```{autodoc2-docstring} archivebox.cli.setup_cmds
    :summary:
    ```
* - {py:obj}`archive_cmds <archivebox.cli.archive_cmds>`
  - ```{autodoc2-docstring} archivebox.cli.archive_cmds
    :summary:
    ```
* - {py:obj}`fake_db <archivebox.cli.fake_db>`
  - ```{autodoc2-docstring} archivebox.cli.fake_db
    :summary:
    ```
* - {py:obj}`display_first <archivebox.cli.display_first>`
  - ```{autodoc2-docstring} archivebox.cli.display_first
    :summary:
    ```
* - {py:obj}`IGNORED_BG_THREADS <archivebox.cli.IGNORED_BG_THREADS>`
  - ```{autodoc2-docstring} archivebox.cli.IGNORED_BG_THREADS
    :summary:
    ```
* - {py:obj}`Omitted <archivebox.cli.Omitted>`
  - ```{autodoc2-docstring} archivebox.cli.Omitted
    :summary:
    ```
* - {py:obj}`OMITTED <archivebox.cli.OMITTED>`
  - ```{autodoc2-docstring} archivebox.cli.OMITTED
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.cli.__package__
:value: >
   'archivebox.cli'

```{autodoc2-docstring} archivebox.cli.__package__
```

````

````{py:data} __command__
:canonical: archivebox.cli.__command__
:value: >
   'archivebox'

```{autodoc2-docstring} archivebox.cli.__command__
```

````

````{py:data} BUILTIN_LIST
:canonical: archivebox.cli.BUILTIN_LIST
:value: >
   None

```{autodoc2-docstring} archivebox.cli.BUILTIN_LIST
```

````

````{py:data} CLI_DIR
:canonical: archivebox.cli.CLI_DIR
:value: >
   None

```{autodoc2-docstring} archivebox.cli.CLI_DIR
```

````

````{py:data} SUBCOMMAND_MODULES
:canonical: archivebox.cli.SUBCOMMAND_MODULES
:value: >
   None

```{autodoc2-docstring} archivebox.cli.SUBCOMMAND_MODULES
```

````

````{py:data} required_attrs
:canonical: archivebox.cli.required_attrs
:value: >
   ('__package__', '__command__', 'main')

```{autodoc2-docstring} archivebox.cli.required_attrs
```

````

````{py:data} is_cli_module
:canonical: archivebox.cli.is_cli_module
:value: >
   None

```{autodoc2-docstring} archivebox.cli.is_cli_module
```

````

````{py:data} is_valid_cli_module
:canonical: archivebox.cli.is_valid_cli_module
:value: >
   None

```{autodoc2-docstring} archivebox.cli.is_valid_cli_module
```

````

`````{py:class} LazySubcommands
:canonical: archivebox.cli.LazySubcommands

Bases: {py:obj}`collections.abc.Mapping`

````{py:method} keys()
:canonical: archivebox.cli.LazySubcommands.keys

````

````{py:method} values()
:canonical: archivebox.cli.LazySubcommands.values

````

````{py:method} items()
:canonical: archivebox.cli.LazySubcommands.items

````

````{py:method} __getitem__(key)
:canonical: archivebox.cli.LazySubcommands.__getitem__

```{autodoc2-docstring} archivebox.cli.LazySubcommands.__getitem__
```

````

````{py:method} __iter__()
:canonical: archivebox.cli.LazySubcommands.__iter__

```{autodoc2-docstring} archivebox.cli.LazySubcommands.__iter__
```

````

````{py:method} __len__()
:canonical: archivebox.cli.LazySubcommands.__len__

```{autodoc2-docstring} archivebox.cli.LazySubcommands.__len__
```

````

`````

````{py:data} CLI_SUBCOMMANDS
:canonical: archivebox.cli.CLI_SUBCOMMANDS
:value: >
   'LazySubcommands(...)'

```{autodoc2-docstring} archivebox.cli.CLI_SUBCOMMANDS
```

````

````{py:data} meta_cmds
:canonical: archivebox.cli.meta_cmds
:value: >
   ('help', 'version')

```{autodoc2-docstring} archivebox.cli.meta_cmds
```

````

````{py:data} setup_cmds
:canonical: archivebox.cli.setup_cmds
:value: >
   ('init', 'setup', 'install')

```{autodoc2-docstring} archivebox.cli.setup_cmds
```

````

````{py:data} archive_cmds
:canonical: archivebox.cli.archive_cmds
:value: >
   ('add', 'remove', 'update', 'list', 'status', 'schedule', 'server', 'shell', 'manage')

```{autodoc2-docstring} archivebox.cli.archive_cmds
```

````

````{py:data} fake_db
:canonical: archivebox.cli.fake_db
:value: >
   ('oneshot',)

```{autodoc2-docstring} archivebox.cli.fake_db
```

````

````{py:data} display_first
:canonical: archivebox.cli.display_first
:value: >
   ()

```{autodoc2-docstring} archivebox.cli.display_first
```

````

````{py:data} IGNORED_BG_THREADS
:canonical: archivebox.cli.IGNORED_BG_THREADS
:value: >
   ('MainThread', 'ThreadPoolExecutor', 'IPythonHistorySavingThread', 'Scheduler')

```{autodoc2-docstring} archivebox.cli.IGNORED_BG_THREADS
```

````

````{py:function} wait_for_bg_threads_to_exit(thread_names: typing.Iterable[str] = (), ignore_names: typing.Iterable[str] = IGNORED_BG_THREADS, timeout: int = 60) -> int
:canonical: archivebox.cli.wait_for_bg_threads_to_exit

```{autodoc2-docstring} archivebox.cli.wait_for_bg_threads_to_exit
```
````

````{py:function} run_subcommand(subcommand: str, subcommand_args: typing.List[str] | None = None, stdin: typing.Optional[typing.IO] = None, pwd: typing.Union[pathlib.Path, str, None] = None) -> None
:canonical: archivebox.cli.run_subcommand

```{autodoc2-docstring} archivebox.cli.run_subcommand
```
````

`````{py:class} NotProvided
:canonical: archivebox.cli.NotProvided

```{autodoc2-docstring} archivebox.cli.NotProvided
```

````{py:method} __len__()
:canonical: archivebox.cli.NotProvided.__len__

```{autodoc2-docstring} archivebox.cli.NotProvided.__len__
```

````

````{py:method} __bool__()
:canonical: archivebox.cli.NotProvided.__bool__

```{autodoc2-docstring} archivebox.cli.NotProvided.__bool__
```

````

````{py:method} __repr__()
:canonical: archivebox.cli.NotProvided.__repr__

````

`````

````{py:data} Omitted
:canonical: archivebox.cli.Omitted
:value: >
   None

```{autodoc2-docstring} archivebox.cli.Omitted
```

````

````{py:data} OMITTED
:canonical: archivebox.cli.OMITTED
:value: >
   'NotProvided(...)'

```{autodoc2-docstring} archivebox.cli.OMITTED
```

````

````{py:function} main(args: typing.List[str] | archivebox.cli.Omitted = OMITTED, stdin: typing.IO | archivebox.cli.Omitted = OMITTED, pwd: str | None = None) -> None
:canonical: archivebox.cli.main

```{autodoc2-docstring} archivebox.cli.main
```
````
