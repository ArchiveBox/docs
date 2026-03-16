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
archivebox.cli.archivebox_list
archivebox.cli.archivebox_archiveresult
archivebox.cli.archivebox_process
archivebox.cli.archivebox_tag
archivebox.cli.archivebox_config
archivebox.cli.cli_utils
archivebox.cli.archivebox_server
archivebox.cli.tests_piping
archivebox.cli.archivebox_binary
archivebox.cli.archivebox_snapshot
archivebox.cli.archivebox_pluginmap
archivebox.cli.archivebox_crawl_compat
archivebox.cli.archivebox_machine
archivebox.cli.archivebox_update
archivebox.cli.archivebox_extract
archivebox.cli.archivebox_crawl
archivebox.cli.archivebox_remove
archivebox.cli.archivebox_install
archivebox.cli.archivebox_mcp
archivebox.cli.archivebox_search
archivebox.cli.archivebox_version
archivebox.cli.archivebox_persona
archivebox.cli.archivebox_snapshot_compat
archivebox.cli.archivebox_add
archivebox.cli.archivebox_status
archivebox.cli.archivebox_run
archivebox.cli.archivebox_init
archivebox.cli.archivebox_help
archivebox.cli.archivebox_manage
```

## Package Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ArchiveBoxGroup <archivebox.cli.ArchiveBoxGroup>`
  - ```{autodoc2-docstring} archivebox.cli.ArchiveBoxGroup
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`cli <archivebox.cli.cli>`
  - ```{autodoc2-docstring} archivebox.cli.cli
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

* - {py:obj}`__command__ <archivebox.cli.__command__>`
  - ```{autodoc2-docstring} archivebox.cli.__command__
    :summary:
    ```
````

### API

````{py:data} __command__
:canonical: archivebox.cli.__command__
:value: >
   'archivebox'

```{autodoc2-docstring} archivebox.cli.__command__
```

````

`````{py:class} ArchiveBoxGroup(name: str | None = None, commands: collections.abc.MutableMapping[str, click.core.Command] | collections.abc.Sequence[click.core.Command] | None = None, invoke_without_command: bool = False, no_args_is_help: bool | None = None, subcommand_metavar: str | None = None, chain: bool = False, result_callback: typing.Callable[..., typing.Any] | None = None, **kwargs: typing.Any)
:canonical: archivebox.cli.ArchiveBoxGroup

Bases: {py:obj}`rich_click.Group`

```{autodoc2-docstring} archivebox.cli.ArchiveBoxGroup
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.cli.ArchiveBoxGroup.__init__
```

````{py:attribute} meta_commands
:canonical: archivebox.cli.ArchiveBoxGroup.meta_commands
:value: >
   None

```{autodoc2-docstring} archivebox.cli.ArchiveBoxGroup.meta_commands
```

````

````{py:attribute} setup_commands
:canonical: archivebox.cli.ArchiveBoxGroup.setup_commands
:value: >
   None

```{autodoc2-docstring} archivebox.cli.ArchiveBoxGroup.setup_commands
```

````

````{py:attribute} model_commands
:canonical: archivebox.cli.ArchiveBoxGroup.model_commands
:value: >
   None

```{autodoc2-docstring} archivebox.cli.ArchiveBoxGroup.model_commands
```

````

````{py:attribute} archive_commands
:canonical: archivebox.cli.ArchiveBoxGroup.archive_commands
:value: >
   None

```{autodoc2-docstring} archivebox.cli.ArchiveBoxGroup.archive_commands
```

````

````{py:attribute} legacy_model_commands
:canonical: archivebox.cli.ArchiveBoxGroup.legacy_model_commands
:value: >
   None

```{autodoc2-docstring} archivebox.cli.ArchiveBoxGroup.legacy_model_commands
```

````

````{py:attribute} all_subcommands
:canonical: archivebox.cli.ArchiveBoxGroup.all_subcommands
:value: >
   None

```{autodoc2-docstring} archivebox.cli.ArchiveBoxGroup.all_subcommands
```

````

````{py:attribute} renamed_commands
:canonical: archivebox.cli.ArchiveBoxGroup.renamed_commands
:value: >
   None

```{autodoc2-docstring} archivebox.cli.ArchiveBoxGroup.renamed_commands
```

````

````{py:attribute} legacy_model_subcommands
:canonical: archivebox.cli.ArchiveBoxGroup.legacy_model_subcommands
:value: >
   None

```{autodoc2-docstring} archivebox.cli.ArchiveBoxGroup.legacy_model_subcommands
```

````

````{py:method} get_canonical_name(cmd_name)
:canonical: archivebox.cli.ArchiveBoxGroup.get_canonical_name
:classmethod:

```{autodoc2-docstring} archivebox.cli.ArchiveBoxGroup.get_canonical_name
```

````

````{py:method} _should_use_legacy_model_command(cmd_name: str) -> bool
:canonical: archivebox.cli.ArchiveBoxGroup._should_use_legacy_model_command
:classmethod:

```{autodoc2-docstring} archivebox.cli.ArchiveBoxGroup._should_use_legacy_model_command
```

````

````{py:method} get_command(ctx, cmd_name)
:canonical: archivebox.cli.ArchiveBoxGroup.get_command

````

````{py:method} _lazy_load(cmd_name_or_path)
:canonical: archivebox.cli.ArchiveBoxGroup._lazy_load
:classmethod:

```{autodoc2-docstring} archivebox.cli.ArchiveBoxGroup._lazy_load
```

````

`````

````{py:function} cli(ctx, help=False)
:canonical: archivebox.cli.cli

```{autodoc2-docstring} archivebox.cli.cli
```
````

````{py:function} main(args=None, prog_name=None, stdin=None)
:canonical: archivebox.cli.main

```{autodoc2-docstring} archivebox.cli.main
```
````
