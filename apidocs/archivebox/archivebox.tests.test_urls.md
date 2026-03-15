# {py:mod}`archivebox.tests.test_urls`

```{py:module} archivebox.tests.test_urls
```

```{autodoc2-docstring} archivebox.tests.test_urls
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestUrlRouting <archivebox.tests.test_urls.TestUrlRouting>`
  - ```{autodoc2-docstring} archivebox.tests.test_urls.TestUrlRouting
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_merge_pythonpath <archivebox.tests.test_urls._merge_pythonpath>`
  - ```{autodoc2-docstring} archivebox.tests.test_urls._merge_pythonpath
    :summary:
    ```
* - {py:obj}`_run_python <archivebox.tests.test_urls._run_python>`
  - ```{autodoc2-docstring} archivebox.tests.test_urls._run_python
    :summary:
    ```
* - {py:obj}`_build_script <archivebox.tests.test_urls._build_script>`
  - ```{autodoc2-docstring} archivebox.tests.test_urls._build_script
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`REPO_ROOT <archivebox.tests.test_urls.REPO_ROOT>`
  - ```{autodoc2-docstring} archivebox.tests.test_urls.REPO_ROOT
    :summary:
    ```
````

### API

````{py:data} REPO_ROOT
:canonical: archivebox.tests.test_urls.REPO_ROOT
:value: >
   None

```{autodoc2-docstring} archivebox.tests.test_urls.REPO_ROOT
```

````

````{py:function} _merge_pythonpath(env: dict[str, str]) -> dict[str, str]
:canonical: archivebox.tests.test_urls._merge_pythonpath

```{autodoc2-docstring} archivebox.tests.test_urls._merge_pythonpath
```
````

````{py:function} _run_python(script: str, cwd: pathlib.Path, timeout: int = 60) -> subprocess.CompletedProcess
:canonical: archivebox.tests.test_urls._run_python

```{autodoc2-docstring} archivebox.tests.test_urls._run_python
```
````

````{py:function} _build_script(body: str) -> str
:canonical: archivebox.tests.test_urls._build_script

```{autodoc2-docstring} archivebox.tests.test_urls._build_script
```
````

`````{py:class} TestUrlRouting
:canonical: archivebox.tests.test_urls.TestUrlRouting

```{autodoc2-docstring} archivebox.tests.test_urls.TestUrlRouting
```

````{py:attribute} data_dir
:canonical: archivebox.tests.test_urls.TestUrlRouting.data_dir
:type: pathlib.Path
:value: >
   None

```{autodoc2-docstring} archivebox.tests.test_urls.TestUrlRouting.data_dir
```

````

````{py:method} _run(body: str, timeout: int = 120) -> None
:canonical: archivebox.tests.test_urls.TestUrlRouting._run

```{autodoc2-docstring} archivebox.tests.test_urls.TestUrlRouting._run
```

````

````{py:method} test_host_utils_and_public_redirect() -> None
:canonical: archivebox.tests.test_urls.TestUrlRouting.test_host_utils_and_public_redirect

```{autodoc2-docstring} archivebox.tests.test_urls.TestUrlRouting.test_host_utils_and_public_redirect
```

````

````{py:method} test_web_admin_routing() -> None
:canonical: archivebox.tests.test_urls.TestUrlRouting.test_web_admin_routing

```{autodoc2-docstring} archivebox.tests.test_urls.TestUrlRouting.test_web_admin_routing
```

````

````{py:method} test_snapshot_routing_and_hosts() -> None
:canonical: archivebox.tests.test_urls.TestUrlRouting.test_snapshot_routing_and_hosts

```{autodoc2-docstring} archivebox.tests.test_urls.TestUrlRouting.test_snapshot_routing_and_hosts
```

````

````{py:method} test_template_and_admin_links() -> None
:canonical: archivebox.tests.test_urls.TestUrlRouting.test_template_and_admin_links

```{autodoc2-docstring} archivebox.tests.test_urls.TestUrlRouting.test_template_and_admin_links
```

````

````{py:method} test_api_available_on_admin_and_api_hosts() -> None
:canonical: archivebox.tests.test_urls.TestUrlRouting.test_api_available_on_admin_and_api_hosts

```{autodoc2-docstring} archivebox.tests.test_urls.TestUrlRouting.test_api_available_on_admin_and_api_hosts
```

````

````{py:method} test_api_post_with_token_on_admin_and_api_hosts() -> None
:canonical: archivebox.tests.test_urls.TestUrlRouting.test_api_post_with_token_on_admin_and_api_hosts

```{autodoc2-docstring} archivebox.tests.test_urls.TestUrlRouting.test_api_post_with_token_on_admin_and_api_hosts
```

````

`````
