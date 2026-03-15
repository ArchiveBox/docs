# {py:mod}`archivebox.cli.archivebox_persona`

```{py:module} archivebox.cli.archivebox_persona
```

```{autodoc2-docstring} archivebox.cli.archivebox_persona
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_chrome_user_data_dir <archivebox.cli.archivebox_persona.get_chrome_user_data_dir>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona.get_chrome_user_data_dir
    :summary:
    ```
* - {py:obj}`get_brave_user_data_dir <archivebox.cli.archivebox_persona.get_brave_user_data_dir>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona.get_brave_user_data_dir
    :summary:
    ```
* - {py:obj}`get_edge_user_data_dir <archivebox.cli.archivebox_persona.get_edge_user_data_dir>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona.get_edge_user_data_dir
    :summary:
    ```
* - {py:obj}`get_browser_binary <archivebox.cli.archivebox_persona.get_browser_binary>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona.get_browser_binary
    :summary:
    ```
* - {py:obj}`_parse_netscape_cookies <archivebox.cli.archivebox_persona._parse_netscape_cookies>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona._parse_netscape_cookies
    :summary:
    ```
* - {py:obj}`_write_netscape_cookies <archivebox.cli.archivebox_persona._write_netscape_cookies>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona._write_netscape_cookies
    :summary:
    ```
* - {py:obj}`_merge_netscape_cookies <archivebox.cli.archivebox_persona._merge_netscape_cookies>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona._merge_netscape_cookies
    :summary:
    ```
* - {py:obj}`extract_cookies_via_cdp <archivebox.cli.archivebox_persona.extract_cookies_via_cdp>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona.extract_cookies_via_cdp
    :summary:
    ```
* - {py:obj}`validate_persona_name <archivebox.cli.archivebox_persona.validate_persona_name>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona.validate_persona_name
    :summary:
    ```
* - {py:obj}`ensure_path_within_personas_dir <archivebox.cli.archivebox_persona.ensure_path_within_personas_dir>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona.ensure_path_within_personas_dir
    :summary:
    ```
* - {py:obj}`create_personas <archivebox.cli.archivebox_persona.create_personas>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona.create_personas
    :summary:
    ```
* - {py:obj}`list_personas <archivebox.cli.archivebox_persona.list_personas>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona.list_personas
    :summary:
    ```
* - {py:obj}`update_personas <archivebox.cli.archivebox_persona.update_personas>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona.update_personas
    :summary:
    ```
* - {py:obj}`delete_personas <archivebox.cli.archivebox_persona.delete_personas>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona.delete_personas
    :summary:
    ```
* - {py:obj}`main <archivebox.cli.archivebox_persona.main>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona.main
    :summary:
    ```
* - {py:obj}`create_cmd <archivebox.cli.archivebox_persona.create_cmd>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona.create_cmd
    :summary:
    ```
* - {py:obj}`list_cmd <archivebox.cli.archivebox_persona.list_cmd>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona.list_cmd
    :summary:
    ```
* - {py:obj}`update_cmd <archivebox.cli.archivebox_persona.update_cmd>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona.update_cmd
    :summary:
    ```
* - {py:obj}`delete_cmd <archivebox.cli.archivebox_persona.delete_cmd>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona.delete_cmd
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__command__ <archivebox.cli.archivebox_persona.__command__>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona.__command__
    :summary:
    ```
* - {py:obj}`BROWSER_PROFILE_FINDERS <archivebox.cli.archivebox_persona.BROWSER_PROFILE_FINDERS>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona.BROWSER_PROFILE_FINDERS
    :summary:
    ```
* - {py:obj}`CHROMIUM_BROWSERS <archivebox.cli.archivebox_persona.CHROMIUM_BROWSERS>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona.CHROMIUM_BROWSERS
    :summary:
    ```
* - {py:obj}`NETSCAPE_COOKIE_HEADER <archivebox.cli.archivebox_persona.NETSCAPE_COOKIE_HEADER>`
  - ```{autodoc2-docstring} archivebox.cli.archivebox_persona.NETSCAPE_COOKIE_HEADER
    :summary:
    ```
````

### API

````{py:data} __command__
:canonical: archivebox.cli.archivebox_persona.__command__
:value: >
   'archivebox persona'

```{autodoc2-docstring} archivebox.cli.archivebox_persona.__command__
```

````

````{py:function} get_chrome_user_data_dir() -> typing.Optional[pathlib.Path]
:canonical: archivebox.cli.archivebox_persona.get_chrome_user_data_dir

```{autodoc2-docstring} archivebox.cli.archivebox_persona.get_chrome_user_data_dir
```
````

````{py:function} get_brave_user_data_dir() -> typing.Optional[pathlib.Path]
:canonical: archivebox.cli.archivebox_persona.get_brave_user_data_dir

```{autodoc2-docstring} archivebox.cli.archivebox_persona.get_brave_user_data_dir
```
````

````{py:function} get_edge_user_data_dir() -> typing.Optional[pathlib.Path]
:canonical: archivebox.cli.archivebox_persona.get_edge_user_data_dir

```{autodoc2-docstring} archivebox.cli.archivebox_persona.get_edge_user_data_dir
```
````

````{py:function} get_browser_binary(browser: str) -> typing.Optional[str]
:canonical: archivebox.cli.archivebox_persona.get_browser_binary

```{autodoc2-docstring} archivebox.cli.archivebox_persona.get_browser_binary
```
````

````{py:data} BROWSER_PROFILE_FINDERS
:canonical: archivebox.cli.archivebox_persona.BROWSER_PROFILE_FINDERS
:value: >
   None

```{autodoc2-docstring} archivebox.cli.archivebox_persona.BROWSER_PROFILE_FINDERS
```

````

````{py:data} CHROMIUM_BROWSERS
:canonical: archivebox.cli.archivebox_persona.CHROMIUM_BROWSERS
:value: >
   None

```{autodoc2-docstring} archivebox.cli.archivebox_persona.CHROMIUM_BROWSERS
```

````

````{py:data} NETSCAPE_COOKIE_HEADER
:canonical: archivebox.cli.archivebox_persona.NETSCAPE_COOKIE_HEADER
:value: >
   ['# Netscape HTTP Cookie File', '# https://curl.se/docs/http-cookies.html', '# This file was generat...

```{autodoc2-docstring} archivebox.cli.archivebox_persona.NETSCAPE_COOKIE_HEADER
```

````

````{py:function} _parse_netscape_cookies(path: pathlib.Path) -> OrderedDict[tuple[str, str, str], tuple[str, str, str, str, str, str, str]]
:canonical: archivebox.cli.archivebox_persona._parse_netscape_cookies

```{autodoc2-docstring} archivebox.cli.archivebox_persona._parse_netscape_cookies
```
````

````{py:function} _write_netscape_cookies(path: pathlib.Path, cookies: OrderedDict[tuple[str, str, str], tuple[str, str, str, str, str, str, str]]) -> None
:canonical: archivebox.cli.archivebox_persona._write_netscape_cookies

```{autodoc2-docstring} archivebox.cli.archivebox_persona._write_netscape_cookies
```
````

````{py:function} _merge_netscape_cookies(existing_file: pathlib.Path, new_file: pathlib.Path) -> None
:canonical: archivebox.cli.archivebox_persona._merge_netscape_cookies

```{autodoc2-docstring} archivebox.cli.archivebox_persona._merge_netscape_cookies
```
````

````{py:function} extract_cookies_via_cdp(user_data_dir: pathlib.Path, output_file: pathlib.Path, profile_dir: str | None = None, chrome_binary: str | None = None) -> bool
:canonical: archivebox.cli.archivebox_persona.extract_cookies_via_cdp

```{autodoc2-docstring} archivebox.cli.archivebox_persona.extract_cookies_via_cdp
```
````

````{py:function} validate_persona_name(name: str) -> tuple[bool, str]
:canonical: archivebox.cli.archivebox_persona.validate_persona_name

```{autodoc2-docstring} archivebox.cli.archivebox_persona.validate_persona_name
```
````

````{py:function} ensure_path_within_personas_dir(persona_path: pathlib.Path) -> bool
:canonical: archivebox.cli.archivebox_persona.ensure_path_within_personas_dir

```{autodoc2-docstring} archivebox.cli.archivebox_persona.ensure_path_within_personas_dir
```
````

````{py:function} create_personas(names: typing.Iterable[str], import_from: typing.Optional[str] = None, profile: typing.Optional[str] = None) -> int
:canonical: archivebox.cli.archivebox_persona.create_personas

```{autodoc2-docstring} archivebox.cli.archivebox_persona.create_personas
```
````

````{py:function} list_personas(name: typing.Optional[str] = None, name__icontains: typing.Optional[str] = None, limit: typing.Optional[int] = None) -> int
:canonical: archivebox.cli.archivebox_persona.list_personas

```{autodoc2-docstring} archivebox.cli.archivebox_persona.list_personas
```
````

````{py:function} update_personas(name: typing.Optional[str] = None) -> int
:canonical: archivebox.cli.archivebox_persona.update_personas

```{autodoc2-docstring} archivebox.cli.archivebox_persona.update_personas
```
````

````{py:function} delete_personas(yes: bool = False, dry_run: bool = False) -> int
:canonical: archivebox.cli.archivebox_persona.delete_personas

```{autodoc2-docstring} archivebox.cli.archivebox_persona.delete_personas
```
````

````{py:function} main()
:canonical: archivebox.cli.archivebox_persona.main

```{autodoc2-docstring} archivebox.cli.archivebox_persona.main
```
````

````{py:function} create_cmd(names: tuple, import_from: typing.Optional[str], profile: typing.Optional[str])
:canonical: archivebox.cli.archivebox_persona.create_cmd

```{autodoc2-docstring} archivebox.cli.archivebox_persona.create_cmd
```
````

````{py:function} list_cmd(name: typing.Optional[str], name__icontains: typing.Optional[str], limit: typing.Optional[int])
:canonical: archivebox.cli.archivebox_persona.list_cmd

```{autodoc2-docstring} archivebox.cli.archivebox_persona.list_cmd
```
````

````{py:function} update_cmd(name: typing.Optional[str])
:canonical: archivebox.cli.archivebox_persona.update_cmd

```{autodoc2-docstring} archivebox.cli.archivebox_persona.update_cmd
```
````

````{py:function} delete_cmd(yes: bool, dry_run: bool)
:canonical: archivebox.cli.archivebox_persona.delete_cmd

```{autodoc2-docstring} archivebox.cli.archivebox_persona.delete_cmd
```
````
