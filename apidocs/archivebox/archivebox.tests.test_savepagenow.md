# {py:mod}`archivebox.tests.test_savepagenow`

```{py:module} archivebox.tests.test_savepagenow
```

```{autodoc2-docstring} archivebox.tests.test_savepagenow
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_run_savepagenow_script <archivebox.tests.test_savepagenow._run_savepagenow_script>`
  - ```{autodoc2-docstring} archivebox.tests.test_savepagenow._run_savepagenow_script
    :summary:
    ```
* - {py:obj}`_run_savepagenow_not_found_script <archivebox.tests.test_savepagenow._run_savepagenow_not_found_script>`
  - ```{autodoc2-docstring} archivebox.tests.test_savepagenow._run_savepagenow_not_found_script
    :summary:
    ```
* - {py:obj}`_run_savepagenow_existing_snapshot_script <archivebox.tests.test_savepagenow._run_savepagenow_existing_snapshot_script>`
  - ```{autodoc2-docstring} archivebox.tests.test_savepagenow._run_savepagenow_existing_snapshot_script
    :summary:
    ```
* - {py:obj}`test_web_add_creates_and_reuses_snapshot_logged_in <archivebox.tests.test_savepagenow.test_web_add_creates_and_reuses_snapshot_logged_in>`
  - ```{autodoc2-docstring} archivebox.tests.test_savepagenow.test_web_add_creates_and_reuses_snapshot_logged_in
    :summary:
    ```
* - {py:obj}`test_web_add_creates_and_reuses_snapshot_public <archivebox.tests.test_savepagenow.test_web_add_creates_and_reuses_snapshot_public>`
  - ```{autodoc2-docstring} archivebox.tests.test_savepagenow.test_web_add_creates_and_reuses_snapshot_public
    :summary:
    ```
* - {py:obj}`test_web_add_requires_login_when_public_off <archivebox.tests.test_savepagenow.test_web_add_requires_login_when_public_off>`
  - ```{autodoc2-docstring} archivebox.tests.test_savepagenow.test_web_add_requires_login_when_public_off
    :summary:
    ```
* - {py:obj}`test_web_add_redirects_existing_snapshot_when_public_off <archivebox.tests.test_savepagenow.test_web_add_redirects_existing_snapshot_when_public_off>`
  - ```{autodoc2-docstring} archivebox.tests.test_savepagenow.test_web_add_redirects_existing_snapshot_when_public_off
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ADMIN_HOST <archivebox.tests.test_savepagenow.ADMIN_HOST>`
  - ```{autodoc2-docstring} archivebox.tests.test_savepagenow.ADMIN_HOST
    :summary:
    ```
````

### API

````{py:data} ADMIN_HOST
:canonical: archivebox.tests.test_savepagenow.ADMIN_HOST
:value: >
   'admin.archivebox.localhost:8000'

```{autodoc2-docstring} archivebox.tests.test_savepagenow.ADMIN_HOST
```

````

````{py:function} _run_savepagenow_script(initialized_archive: pathlib.Path, request_url: str, expected_url: str, *, login: bool, public_add_view: bool, host: str)
:canonical: archivebox.tests.test_savepagenow._run_savepagenow_script

```{autodoc2-docstring} archivebox.tests.test_savepagenow._run_savepagenow_script
```
````

````{py:function} _run_savepagenow_not_found_script(initialized_archive: pathlib.Path, request_url: str)
:canonical: archivebox.tests.test_savepagenow._run_savepagenow_not_found_script

```{autodoc2-docstring} archivebox.tests.test_savepagenow._run_savepagenow_not_found_script
```
````

````{py:function} _run_savepagenow_existing_snapshot_script(initialized_archive: pathlib.Path, request_url: str, stored_url: str)
:canonical: archivebox.tests.test_savepagenow._run_savepagenow_existing_snapshot_script

```{autodoc2-docstring} archivebox.tests.test_savepagenow._run_savepagenow_existing_snapshot_script
```
````

````{py:function} test_web_add_creates_and_reuses_snapshot_logged_in(initialized_archive)
:canonical: archivebox.tests.test_savepagenow.test_web_add_creates_and_reuses_snapshot_logged_in

```{autodoc2-docstring} archivebox.tests.test_savepagenow.test_web_add_creates_and_reuses_snapshot_logged_in
```
````

````{py:function} test_web_add_creates_and_reuses_snapshot_public(initialized_archive)
:canonical: archivebox.tests.test_savepagenow.test_web_add_creates_and_reuses_snapshot_public

```{autodoc2-docstring} archivebox.tests.test_savepagenow.test_web_add_creates_and_reuses_snapshot_public
```
````

````{py:function} test_web_add_requires_login_when_public_off(initialized_archive)
:canonical: archivebox.tests.test_savepagenow.test_web_add_requires_login_when_public_off

```{autodoc2-docstring} archivebox.tests.test_savepagenow.test_web_add_requires_login_when_public_off
```
````

````{py:function} test_web_add_redirects_existing_snapshot_when_public_off(initialized_archive)
:canonical: archivebox.tests.test_savepagenow.test_web_add_redirects_existing_snapshot_when_public_off

```{autodoc2-docstring} archivebox.tests.test_savepagenow.test_web_add_redirects_existing_snapshot_when_public_off
```
````
