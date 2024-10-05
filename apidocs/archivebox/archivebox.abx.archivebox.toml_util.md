# {py:mod}`archivebox.abx.archivebox.toml_util`

```{py:module} archivebox.abx.archivebox.toml_util
```

```{autodoc2-docstring} archivebox.abx.archivebox.toml_util
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`JSONSchemaWithLambdas <archivebox.abx.archivebox.toml_util.JSONSchemaWithLambdas>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.toml_util.JSONSchemaWithLambdas
    :summary:
    ```
* - {py:obj}`CustomTOMLEncoder <archivebox.abx.archivebox.toml_util.CustomTOMLEncoder>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.toml_util.CustomTOMLEncoder
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`load_ini_value <archivebox.abx.archivebox.toml_util.load_ini_value>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.toml_util.load_ini_value
    :summary:
    ```
* - {py:obj}`convert <archivebox.abx.archivebox.toml_util.convert>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.toml_util.convert
    :summary:
    ```
* - {py:obj}`better_toml_dump_str <archivebox.abx.archivebox.toml_util.better_toml_dump_str>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.toml_util.better_toml_dump_str
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`JSONValue <archivebox.abx.archivebox.toml_util.JSONValue>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.toml_util.JSONValue
    :summary:
    ```
* - {py:obj}`TOML_HEADER <archivebox.abx.archivebox.toml_util.TOML_HEADER>`
  - ```{autodoc2-docstring} archivebox.abx.archivebox.toml_util.TOML_HEADER
    :summary:
    ```
````

### API

````{py:data} JSONValue
:canonical: archivebox.abx.archivebox.toml_util.JSONValue
:value: >
   None

```{autodoc2-docstring} archivebox.abx.archivebox.toml_util.JSONValue
```

````

````{py:data} TOML_HEADER
:canonical: archivebox.abx.archivebox.toml_util.TOML_HEADER
:value: <Multiline-String>

```{autodoc2-docstring} archivebox.abx.archivebox.toml_util.TOML_HEADER
```

````

````{py:function} load_ini_value(val: str) -> archivebox.abx.archivebox.toml_util.JSONValue
:canonical: archivebox.abx.archivebox.toml_util.load_ini_value

```{autodoc2-docstring} archivebox.abx.archivebox.toml_util.load_ini_value
```
````

````{py:function} convert(ini_str: str) -> str
:canonical: archivebox.abx.archivebox.toml_util.convert

```{autodoc2-docstring} archivebox.abx.archivebox.toml_util.convert
```
````

`````{py:class} JSONSchemaWithLambdas(by_alias: bool = True, ref_template: str = DEFAULT_REF_TEMPLATE)
:canonical: archivebox.abx.archivebox.toml_util.JSONSchemaWithLambdas

Bases: {py:obj}`pydantic.json_schema.GenerateJsonSchema`

```{autodoc2-docstring} archivebox.abx.archivebox.toml_util.JSONSchemaWithLambdas
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.abx.archivebox.toml_util.JSONSchemaWithLambdas.__init__
```

````{py:method} encode_default(default: typing.Any) -> typing.Any
:canonical: archivebox.abx.archivebox.toml_util.JSONSchemaWithLambdas.encode_default

````

`````

````{py:function} better_toml_dump_str(val: typing.Any) -> str
:canonical: archivebox.abx.archivebox.toml_util.better_toml_dump_str

```{autodoc2-docstring} archivebox.abx.archivebox.toml_util.better_toml_dump_str
```
````

````{py:class} CustomTOMLEncoder(**kwargs)
:canonical: archivebox.abx.archivebox.toml_util.CustomTOMLEncoder

Bases: {py:obj}`toml.encoder.TomlEncoder`

```{autodoc2-docstring} archivebox.abx.archivebox.toml_util.CustomTOMLEncoder
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.abx.archivebox.toml_util.CustomTOMLEncoder.__init__
```

````
