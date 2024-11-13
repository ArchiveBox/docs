# {py:mod}`archivebox.misc.logging`

```{py:module} archivebox.misc.logging
```

```{autodoc2-docstring} archivebox.misc.logging
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`RainbowHighlighter <archivebox.misc.logging.RainbowHighlighter>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`stdout <archivebox.misc.logging.stdout>`
  - ```{autodoc2-docstring} archivebox.misc.logging.stdout
    :summary:
    ```
* - {py:obj}`stderr <archivebox.misc.logging.stderr>`
  - ```{autodoc2-docstring} archivebox.misc.logging.stderr
    :summary:
    ```
* - {py:obj}`hint <archivebox.misc.logging.hint>`
  - ```{autodoc2-docstring} archivebox.misc.logging.hint
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CONSOLE <archivebox.misc.logging.CONSOLE>`
  - ```{autodoc2-docstring} archivebox.misc.logging.CONSOLE
    :summary:
    ```
* - {py:obj}`STDERR <archivebox.misc.logging.STDERR>`
  - ```{autodoc2-docstring} archivebox.misc.logging.STDERR
    :summary:
    ```
* - {py:obj}`IS_TTY <archivebox.misc.logging.IS_TTY>`
  - ```{autodoc2-docstring} archivebox.misc.logging.IS_TTY
    :summary:
    ```
* - {py:obj}`rainbow <archivebox.misc.logging.rainbow>`
  - ```{autodoc2-docstring} archivebox.misc.logging.rainbow
    :summary:
    ```
* - {py:obj}`DEFAULT_CLI_COLORS <archivebox.misc.logging.DEFAULT_CLI_COLORS>`
  - ```{autodoc2-docstring} archivebox.misc.logging.DEFAULT_CLI_COLORS
    :summary:
    ```
* - {py:obj}`ANSI <archivebox.misc.logging.ANSI>`
  - ```{autodoc2-docstring} archivebox.misc.logging.ANSI
    :summary:
    ```
* - {py:obj}`COLOR_DICT <archivebox.misc.logging.COLOR_DICT>`
  - ```{autodoc2-docstring} archivebox.misc.logging.COLOR_DICT
    :summary:
    ```
````

### API

````{py:data} CONSOLE
:canonical: archivebox.misc.logging.CONSOLE
:value: >
   'Console(...)'

```{autodoc2-docstring} archivebox.misc.logging.CONSOLE
```

````

````{py:data} STDERR
:canonical: archivebox.misc.logging.STDERR
:value: >
   'Console(...)'

```{autodoc2-docstring} archivebox.misc.logging.STDERR
```

````

````{py:data} IS_TTY
:canonical: archivebox.misc.logging.IS_TTY
:value: >
   None

```{autodoc2-docstring} archivebox.misc.logging.IS_TTY
```

````

`````{py:class} RainbowHighlighter
:canonical: archivebox.misc.logging.RainbowHighlighter

Bases: {py:obj}`rich.highlighter.Highlighter`

````{py:method} highlight(text)
:canonical: archivebox.misc.logging.RainbowHighlighter.highlight

````

`````

````{py:data} rainbow
:canonical: archivebox.misc.logging.rainbow
:value: >
   'RainbowHighlighter(...)'

```{autodoc2-docstring} archivebox.misc.logging.rainbow
```

````

````{py:data} DEFAULT_CLI_COLORS
:canonical: archivebox.misc.logging.DEFAULT_CLI_COLORS
:value: >
   'benedict(...)'

```{autodoc2-docstring} archivebox.misc.logging.DEFAULT_CLI_COLORS
```

````

````{py:data} ANSI
:canonical: archivebox.misc.logging.ANSI
:value: >
   'benedict(...)'

```{autodoc2-docstring} archivebox.misc.logging.ANSI
```

````

````{py:data} COLOR_DICT
:canonical: archivebox.misc.logging.COLOR_DICT
:value: >
   'defaultdict(...)'

```{autodoc2-docstring} archivebox.misc.logging.COLOR_DICT
```

````

````{py:function} stdout(*args, color: typing.Optional[str] = None, prefix: str = '', config: typing.Optional[benedict.benedict] = None) -> None
:canonical: archivebox.misc.logging.stdout

```{autodoc2-docstring} archivebox.misc.logging.stdout
```
````

````{py:function} stderr(*args, color: typing.Optional[str] = None, prefix: str = '', config: typing.Optional[benedict.benedict] = None) -> None
:canonical: archivebox.misc.logging.stderr

```{autodoc2-docstring} archivebox.misc.logging.stderr
```
````

````{py:function} hint(text: typing.Union[typing.Tuple[str, ...], typing.List[str], str], prefix='    ', config: typing.Optional[benedict.benedict] = None) -> None
:canonical: archivebox.misc.logging.hint

```{autodoc2-docstring} archivebox.misc.logging.hint
```
````
