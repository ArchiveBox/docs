# {py:mod}`archivebox.tests.test_cli_crawl`

```{py:module} archivebox.tests.test_cli_crawl
```

```{autodoc2-docstring} archivebox.tests.test_cli_crawl
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestCrawlCreate <archivebox.tests.test_cli_crawl.TestCrawlCreate>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_crawl.TestCrawlCreate
    :summary:
    ```
* - {py:obj}`TestCrawlList <archivebox.tests.test_cli_crawl.TestCrawlList>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_crawl.TestCrawlList
    :summary:
    ```
* - {py:obj}`TestCrawlUpdate <archivebox.tests.test_cli_crawl.TestCrawlUpdate>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_crawl.TestCrawlUpdate
    :summary:
    ```
* - {py:obj}`TestCrawlDelete <archivebox.tests.test_cli_crawl.TestCrawlDelete>`
  - ```{autodoc2-docstring} archivebox.tests.test_cli_crawl.TestCrawlDelete
    :summary:
    ```
````

### API

`````{py:class} TestCrawlCreate
:canonical: archivebox.tests.test_cli_crawl.TestCrawlCreate

```{autodoc2-docstring} archivebox.tests.test_cli_crawl.TestCrawlCreate
```

````{py:method} test_create_from_url_args(initialized_archive)
:canonical: archivebox.tests.test_cli_crawl.TestCrawlCreate.test_create_from_url_args

```{autodoc2-docstring} archivebox.tests.test_cli_crawl.TestCrawlCreate.test_create_from_url_args
```

````

````{py:method} test_create_from_stdin_urls(initialized_archive)
:canonical: archivebox.tests.test_cli_crawl.TestCrawlCreate.test_create_from_stdin_urls

```{autodoc2-docstring} archivebox.tests.test_cli_crawl.TestCrawlCreate.test_create_from_stdin_urls
```

````

````{py:method} test_create_with_depth(initialized_archive)
:canonical: archivebox.tests.test_cli_crawl.TestCrawlCreate.test_create_with_depth

```{autodoc2-docstring} archivebox.tests.test_cli_crawl.TestCrawlCreate.test_create_with_depth
```

````

````{py:method} test_create_with_tag(initialized_archive)
:canonical: archivebox.tests.test_cli_crawl.TestCrawlCreate.test_create_with_tag

```{autodoc2-docstring} archivebox.tests.test_cli_crawl.TestCrawlCreate.test_create_with_tag
```

````

````{py:method} test_create_pass_through_other_types(initialized_archive)
:canonical: archivebox.tests.test_cli_crawl.TestCrawlCreate.test_create_pass_through_other_types

```{autodoc2-docstring} archivebox.tests.test_cli_crawl.TestCrawlCreate.test_create_pass_through_other_types
```

````

````{py:method} test_create_pass_through_existing_crawl(initialized_archive)
:canonical: archivebox.tests.test_cli_crawl.TestCrawlCreate.test_create_pass_through_existing_crawl

```{autodoc2-docstring} archivebox.tests.test_cli_crawl.TestCrawlCreate.test_create_pass_through_existing_crawl
```

````

`````

`````{py:class} TestCrawlList
:canonical: archivebox.tests.test_cli_crawl.TestCrawlList

```{autodoc2-docstring} archivebox.tests.test_cli_crawl.TestCrawlList
```

````{py:method} test_list_empty(initialized_archive)
:canonical: archivebox.tests.test_cli_crawl.TestCrawlList.test_list_empty

```{autodoc2-docstring} archivebox.tests.test_cli_crawl.TestCrawlList.test_list_empty
```

````

````{py:method} test_list_returns_created(initialized_archive)
:canonical: archivebox.tests.test_cli_crawl.TestCrawlList.test_list_returns_created

```{autodoc2-docstring} archivebox.tests.test_cli_crawl.TestCrawlList.test_list_returns_created
```

````

````{py:method} test_list_filter_by_status(initialized_archive)
:canonical: archivebox.tests.test_cli_crawl.TestCrawlList.test_list_filter_by_status

```{autodoc2-docstring} archivebox.tests.test_cli_crawl.TestCrawlList.test_list_filter_by_status
```

````

````{py:method} test_list_with_limit(initialized_archive)
:canonical: archivebox.tests.test_cli_crawl.TestCrawlList.test_list_with_limit

```{autodoc2-docstring} archivebox.tests.test_cli_crawl.TestCrawlList.test_list_with_limit
```

````

`````

`````{py:class} TestCrawlUpdate
:canonical: archivebox.tests.test_cli_crawl.TestCrawlUpdate

```{autodoc2-docstring} archivebox.tests.test_cli_crawl.TestCrawlUpdate
```

````{py:method} test_update_status(initialized_archive)
:canonical: archivebox.tests.test_cli_crawl.TestCrawlUpdate.test_update_status

```{autodoc2-docstring} archivebox.tests.test_cli_crawl.TestCrawlUpdate.test_update_status
```

````

`````

`````{py:class} TestCrawlDelete
:canonical: archivebox.tests.test_cli_crawl.TestCrawlDelete

```{autodoc2-docstring} archivebox.tests.test_cli_crawl.TestCrawlDelete
```

````{py:method} test_delete_requires_yes(initialized_archive)
:canonical: archivebox.tests.test_cli_crawl.TestCrawlDelete.test_delete_requires_yes

```{autodoc2-docstring} archivebox.tests.test_cli_crawl.TestCrawlDelete.test_delete_requires_yes
```

````

````{py:method} test_delete_with_yes(initialized_archive)
:canonical: archivebox.tests.test_cli_crawl.TestCrawlDelete.test_delete_with_yes

```{autodoc2-docstring} archivebox.tests.test_cli_crawl.TestCrawlDelete.test_delete_with_yes
```

````

````{py:method} test_delete_dry_run(initialized_archive)
:canonical: archivebox.tests.test_cli_crawl.TestCrawlDelete.test_delete_dry_run

```{autodoc2-docstring} archivebox.tests.test_cli_crawl.TestCrawlDelete.test_delete_dry_run
```

````

`````
