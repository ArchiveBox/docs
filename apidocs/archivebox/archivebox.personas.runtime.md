# {py:mod}`archivebox.personas.runtime`

```{py:module} archivebox.personas.runtime
```

```{autodoc2-docstring} archivebox.personas.runtime
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`crawl_persona_lock <archivebox.personas.runtime.crawl_persona_lock>`
  - ```{autodoc2-docstring} archivebox.personas.runtime.crawl_persona_lock
    :summary:
    ```
* - {py:obj}`_remove_volatile_profile_state <archivebox.personas.runtime._remove_volatile_profile_state>`
  - ```{autodoc2-docstring} archivebox.personas.runtime._remove_volatile_profile_state
    :summary:
    ```
* - {py:obj}`_copy_profile_template <archivebox.personas.runtime._copy_profile_template>`
  - ```{autodoc2-docstring} archivebox.personas.runtime._copy_profile_template
    :summary:
    ```
* - {py:obj}`prepare_crawl_persona_runtime <archivebox.personas.runtime.prepare_crawl_persona_runtime>`
  - ```{autodoc2-docstring} archivebox.personas.runtime.prepare_crawl_persona_runtime
    :summary:
    ```
* - {py:obj}`cleanup_crawl_persona_runtime <archivebox.personas.runtime.cleanup_crawl_persona_runtime>`
  - ```{autodoc2-docstring} archivebox.personas.runtime.cleanup_crawl_persona_runtime
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`VOLATILE_PROFILE_DIR_NAMES <archivebox.personas.runtime.VOLATILE_PROFILE_DIR_NAMES>`
  - ```{autodoc2-docstring} archivebox.personas.runtime.VOLATILE_PROFILE_DIR_NAMES
    :summary:
    ```
* - {py:obj}`VOLATILE_PROFILE_FILE_NAMES <archivebox.personas.runtime.VOLATILE_PROFILE_FILE_NAMES>`
  - ```{autodoc2-docstring} archivebox.personas.runtime.VOLATILE_PROFILE_FILE_NAMES
    :summary:
    ```
````

### API

````{py:data} VOLATILE_PROFILE_DIR_NAMES
:canonical: archivebox.personas.runtime.VOLATILE_PROFILE_DIR_NAMES
:value: >
   None

```{autodoc2-docstring} archivebox.personas.runtime.VOLATILE_PROFILE_DIR_NAMES
```

````

````{py:data} VOLATILE_PROFILE_FILE_NAMES
:canonical: archivebox.personas.runtime.VOLATILE_PROFILE_FILE_NAMES
:value: >
   None

```{autodoc2-docstring} archivebox.personas.runtime.VOLATILE_PROFILE_FILE_NAMES
```

````

````{py:function} crawl_persona_lock(persona_path: pathlib.Path)
:canonical: archivebox.personas.runtime.crawl_persona_lock

```{autodoc2-docstring} archivebox.personas.runtime.crawl_persona_lock
```
````

````{py:function} _remove_volatile_profile_state(profile_dir: pathlib.Path) -> None
:canonical: archivebox.personas.runtime._remove_volatile_profile_state

```{autodoc2-docstring} archivebox.personas.runtime._remove_volatile_profile_state
```
````

````{py:function} _copy_profile_template(source_dir: pathlib.Path, destination_dir: pathlib.Path) -> None
:canonical: archivebox.personas.runtime._copy_profile_template

```{autodoc2-docstring} archivebox.personas.runtime._copy_profile_template
```
````

````{py:function} prepare_crawl_persona_runtime(crawl, persona, chrome_binary: str = '') -> dict[str, str]
:canonical: archivebox.personas.runtime.prepare_crawl_persona_runtime

```{autodoc2-docstring} archivebox.personas.runtime.prepare_crawl_persona_runtime
```
````

````{py:function} cleanup_crawl_persona_runtime(crawl) -> None
:canonical: archivebox.personas.runtime.cleanup_crawl_persona_runtime

```{autodoc2-docstring} archivebox.personas.runtime.cleanup_crawl_persona_runtime
```
````
