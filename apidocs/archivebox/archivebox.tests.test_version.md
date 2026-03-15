# {py:mod}`archivebox.tests.test_version`

```{py:module} archivebox.tests.test_version
```

```{autodoc2-docstring} archivebox.tests.test_version
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestVersionQuiet <archivebox.tests.test_version.TestVersionQuiet>`
  - ```{autodoc2-docstring} archivebox.tests.test_version.TestVersionQuiet
    :summary:
    ```
* - {py:obj}`TestVersionFull <archivebox.tests.test_version.TestVersionFull>`
  - ```{autodoc2-docstring} archivebox.tests.test_version.TestVersionFull
    :summary:
    ```
* - {py:obj}`TestVersionWithBinaries <archivebox.tests.test_version.TestVersionWithBinaries>`
  - ```{autodoc2-docstring} archivebox.tests.test_version.TestVersionWithBinaries
    :summary:
    ```
* - {py:obj}`TestVersionCLI <archivebox.tests.test_version.TestVersionCLI>`
  - ```{autodoc2-docstring} archivebox.tests.test_version.TestVersionCLI
    :summary:
    ```
````

### API

`````{py:class} TestVersionQuiet
:canonical: archivebox.tests.test_version.TestVersionQuiet

```{autodoc2-docstring} archivebox.tests.test_version.TestVersionQuiet
```

````{py:method} test_version_prints_version_number(tmp_path)
:canonical: archivebox.tests.test_version.TestVersionQuiet.test_version_prints_version_number

```{autodoc2-docstring} archivebox.tests.test_version.TestVersionQuiet.test_version_prints_version_number
```

````

````{py:method} test_version_flag_prints_version_number(tmp_path)
:canonical: archivebox.tests.test_version.TestVersionQuiet.test_version_flag_prints_version_number

```{autodoc2-docstring} archivebox.tests.test_version.TestVersionQuiet.test_version_flag_prints_version_number
```

````

`````

`````{py:class} TestVersionFull
:canonical: archivebox.tests.test_version.TestVersionFull

```{autodoc2-docstring} archivebox.tests.test_version.TestVersionFull
```

````{py:method} test_version_shows_system_info(tmp_path, process)
:canonical: archivebox.tests.test_version.TestVersionFull.test_version_shows_system_info

```{autodoc2-docstring} archivebox.tests.test_version.TestVersionFull.test_version_shows_system_info
```

````

````{py:method} test_version_shows_binary_section(tmp_path, process)
:canonical: archivebox.tests.test_version.TestVersionFull.test_version_shows_binary_section

```{autodoc2-docstring} archivebox.tests.test_version.TestVersionFull.test_version_shows_binary_section
```

````

````{py:method} test_version_shows_data_locations(tmp_path, process)
:canonical: archivebox.tests.test_version.TestVersionFull.test_version_shows_data_locations

```{autodoc2-docstring} archivebox.tests.test_version.TestVersionFull.test_version_shows_data_locations
```

````

`````

`````{py:class} TestVersionWithBinaries
:canonical: archivebox.tests.test_version.TestVersionWithBinaries

```{autodoc2-docstring} archivebox.tests.test_version.TestVersionWithBinaries
```

````{py:method} test_version_shows_binary_status(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_version.TestVersionWithBinaries.test_version_shows_binary_status

```{autodoc2-docstring} archivebox.tests.test_version.TestVersionWithBinaries.test_version_shows_binary_status
```

````

`````

`````{py:class} TestVersionCLI
:canonical: archivebox.tests.test_version.TestVersionCLI

```{autodoc2-docstring} archivebox.tests.test_version.TestVersionCLI
```

````{py:method} test_cli_help(tmp_path)
:canonical: archivebox.tests.test_version.TestVersionCLI.test_cli_help

```{autodoc2-docstring} archivebox.tests.test_version.TestVersionCLI.test_cli_help
```

````

````{py:method} test_cli_invalid_option(tmp_path)
:canonical: archivebox.tests.test_version.TestVersionCLI.test_cli_invalid_option

```{autodoc2-docstring} archivebox.tests.test_version.TestVersionCLI.test_cli_invalid_option
```

````

`````
