# {py:mod}`archivebox.tests.test_install`

```{py:module} archivebox.tests.test_install
```

```{autodoc2-docstring} archivebox.tests.test_install
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestInstallDryRun <archivebox.tests.test_install.TestInstallDryRun>`
  - ```{autodoc2-docstring} archivebox.tests.test_install.TestInstallDryRun
    :summary:
    ```
* - {py:obj}`TestInstallOutput <archivebox.tests.test_install.TestInstallOutput>`
  - ```{autodoc2-docstring} archivebox.tests.test_install.TestInstallOutput
    :summary:
    ```
* - {py:obj}`TestInstallCLI <archivebox.tests.test_install.TestInstallCLI>`
  - ```{autodoc2-docstring} archivebox.tests.test_install.TestInstallCLI
    :summary:
    ```
* - {py:obj}`TestInstallInitialization <archivebox.tests.test_install.TestInstallInitialization>`
  - ```{autodoc2-docstring} archivebox.tests.test_install.TestInstallInitialization
    :summary:
    ```
````

### API

`````{py:class} TestInstallDryRun
:canonical: archivebox.tests.test_install.TestInstallDryRun

```{autodoc2-docstring} archivebox.tests.test_install.TestInstallDryRun
```

````{py:method} test_dry_run_prints_message(tmp_path, process)
:canonical: archivebox.tests.test_install.TestInstallDryRun.test_dry_run_prints_message

```{autodoc2-docstring} archivebox.tests.test_install.TestInstallDryRun.test_dry_run_prints_message
```

````

````{py:method} test_dry_run_does_not_create_crawl(tmp_path, process)
:canonical: archivebox.tests.test_install.TestInstallDryRun.test_dry_run_does_not_create_crawl

```{autodoc2-docstring} archivebox.tests.test_install.TestInstallDryRun.test_dry_run_does_not_create_crawl
```

````

`````

`````{py:class} TestInstallOutput
:canonical: archivebox.tests.test_install.TestInstallOutput

```{autodoc2-docstring} archivebox.tests.test_install.TestInstallOutput
```

````{py:method} test_install_prints_detecting_message(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_install.TestInstallOutput.test_install_prints_detecting_message

```{autodoc2-docstring} archivebox.tests.test_install.TestInstallOutput.test_install_prints_detecting_message
```

````

`````

`````{py:class} TestInstallCLI
:canonical: archivebox.tests.test_install.TestInstallCLI

```{autodoc2-docstring} archivebox.tests.test_install.TestInstallCLI
```

````{py:method} test_cli_help(tmp_path)
:canonical: archivebox.tests.test_install.TestInstallCLI.test_cli_help

```{autodoc2-docstring} archivebox.tests.test_install.TestInstallCLI.test_cli_help
```

````

````{py:method} test_cli_invalid_option(tmp_path)
:canonical: archivebox.tests.test_install.TestInstallCLI.test_cli_invalid_option

```{autodoc2-docstring} archivebox.tests.test_install.TestInstallCLI.test_cli_invalid_option
```

````

`````

`````{py:class} TestInstallInitialization
:canonical: archivebox.tests.test_install.TestInstallInitialization

```{autodoc2-docstring} archivebox.tests.test_install.TestInstallInitialization
```

````{py:method} test_install_from_empty_dir(tmp_path)
:canonical: archivebox.tests.test_install.TestInstallInitialization.test_install_from_empty_dir

```{autodoc2-docstring} archivebox.tests.test_install.TestInstallInitialization.test_install_from_empty_dir
```

````

`````
