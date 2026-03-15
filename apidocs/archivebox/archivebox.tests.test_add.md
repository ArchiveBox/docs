# {py:mod}`archivebox.tests.test_add`

```{py:module} archivebox.tests.test_add
```

```{autodoc2-docstring} archivebox.tests.test_add
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestAddCLI <archivebox.tests.test_add.TestAddCLI>`
  - ```{autodoc2-docstring} archivebox.tests.test_add.TestAddCLI
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`test_depth_flag_is_accepted <archivebox.tests.test_add.test_depth_flag_is_accepted>`
  - ```{autodoc2-docstring} archivebox.tests.test_add.test_depth_flag_is_accepted
    :summary:
    ```
* - {py:obj}`test_depth_flag_fails_if_it_is_not_0_or_1 <archivebox.tests.test_add.test_depth_flag_fails_if_it_is_not_0_or_1>`
  - ```{autodoc2-docstring} archivebox.tests.test_add.test_depth_flag_fails_if_it_is_not_0_or_1
    :summary:
    ```
* - {py:obj}`test_depth_flag_0_creates_source_file <archivebox.tests.test_add.test_depth_flag_0_creates_source_file>`
  - ```{autodoc2-docstring} archivebox.tests.test_add.test_depth_flag_0_creates_source_file
    :summary:
    ```
* - {py:obj}`test_overwrite_flag_is_accepted <archivebox.tests.test_add.test_overwrite_flag_is_accepted>`
  - ```{autodoc2-docstring} archivebox.tests.test_add.test_overwrite_flag_is_accepted
    :summary:
    ```
* - {py:obj}`test_add_creates_crawl_in_database <archivebox.tests.test_add.test_add_creates_crawl_in_database>`
  - ```{autodoc2-docstring} archivebox.tests.test_add.test_add_creates_crawl_in_database
    :summary:
    ```
* - {py:obj}`test_add_with_tags <archivebox.tests.test_add.test_add_with_tags>`
  - ```{autodoc2-docstring} archivebox.tests.test_add.test_add_with_tags
    :summary:
    ```
* - {py:obj}`test_add_multiple_urls_single_call <archivebox.tests.test_add.test_add_multiple_urls_single_call>`
  - ```{autodoc2-docstring} archivebox.tests.test_add.test_add_multiple_urls_single_call
    :summary:
    ```
* - {py:obj}`test_add_from_file <archivebox.tests.test_add.test_add_from_file>`
  - ```{autodoc2-docstring} archivebox.tests.test_add.test_add_from_file
    :summary:
    ```
````

### API

````{py:function} test_depth_flag_is_accepted(process, disable_extractors_dict)
:canonical: archivebox.tests.test_add.test_depth_flag_is_accepted

```{autodoc2-docstring} archivebox.tests.test_add.test_depth_flag_is_accepted
```
````

````{py:function} test_depth_flag_fails_if_it_is_not_0_or_1(process, disable_extractors_dict)
:canonical: archivebox.tests.test_add.test_depth_flag_fails_if_it_is_not_0_or_1

```{autodoc2-docstring} archivebox.tests.test_add.test_depth_flag_fails_if_it_is_not_0_or_1
```
````

````{py:function} test_depth_flag_0_creates_source_file(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_add.test_depth_flag_0_creates_source_file

```{autodoc2-docstring} archivebox.tests.test_add.test_depth_flag_0_creates_source_file
```
````

````{py:function} test_overwrite_flag_is_accepted(process, disable_extractors_dict)
:canonical: archivebox.tests.test_add.test_overwrite_flag_is_accepted

```{autodoc2-docstring} archivebox.tests.test_add.test_overwrite_flag_is_accepted
```
````

````{py:function} test_add_creates_crawl_in_database(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_add.test_add_creates_crawl_in_database

```{autodoc2-docstring} archivebox.tests.test_add.test_add_creates_crawl_in_database
```
````

````{py:function} test_add_with_tags(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_add.test_add_with_tags

```{autodoc2-docstring} archivebox.tests.test_add.test_add_with_tags
```
````

````{py:function} test_add_multiple_urls_single_call(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_add.test_add_multiple_urls_single_call

```{autodoc2-docstring} archivebox.tests.test_add.test_add_multiple_urls_single_call
```
````

````{py:function} test_add_from_file(tmp_path, process, disable_extractors_dict)
:canonical: archivebox.tests.test_add.test_add_from_file

```{autodoc2-docstring} archivebox.tests.test_add.test_add_from_file
```
````

`````{py:class} TestAddCLI
:canonical: archivebox.tests.test_add.TestAddCLI

```{autodoc2-docstring} archivebox.tests.test_add.TestAddCLI
```

````{py:method} test_add_help(tmp_path, process)
:canonical: archivebox.tests.test_add.TestAddCLI.test_add_help

```{autodoc2-docstring} archivebox.tests.test_add.TestAddCLI.test_add_help
```

````

````{py:method} test_add_no_args_shows_help(tmp_path, process)
:canonical: archivebox.tests.test_add.TestAddCLI.test_add_no_args_shows_help

```{autodoc2-docstring} archivebox.tests.test_add.TestAddCLI.test_add_no_args_shows_help
```

````

`````
