# {py:mod}`archivebox.abid_utils.abid`

```{py:module} archivebox.abid_utils.abid
```

```{autodoc2-docstring} archivebox.abid_utils.abid
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ABID <archivebox.abid_utils.abid.ABID>`
  - ```{autodoc2-docstring} archivebox.abid_utils.abid.ABID
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`uri_hash <archivebox.abid_utils.abid.uri_hash>`
  - ```{autodoc2-docstring} archivebox.abid_utils.abid.uri_hash
    :summary:
    ```
* - {py:obj}`abid_part_from_prefix <archivebox.abid_utils.abid.abid_part_from_prefix>`
  - ```{autodoc2-docstring} archivebox.abid_utils.abid.abid_part_from_prefix
    :summary:
    ```
* - {py:obj}`abid_part_from_uri <archivebox.abid_utils.abid.abid_part_from_uri>`
  - ```{autodoc2-docstring} archivebox.abid_utils.abid.abid_part_from_uri
    :summary:
    ```
* - {py:obj}`abid_part_from_ts <archivebox.abid_utils.abid.abid_part_from_ts>`
  - ```{autodoc2-docstring} archivebox.abid_utils.abid.abid_part_from_ts
    :summary:
    ```
* - {py:obj}`ts_from_abid <archivebox.abid_utils.abid.ts_from_abid>`
  - ```{autodoc2-docstring} archivebox.abid_utils.abid.ts_from_abid
    :summary:
    ```
* - {py:obj}`abid_part_from_subtype <archivebox.abid_utils.abid.abid_part_from_subtype>`
  - ```{autodoc2-docstring} archivebox.abid_utils.abid.abid_part_from_subtype
    :summary:
    ```
* - {py:obj}`abid_part_from_rand <archivebox.abid_utils.abid.abid_part_from_rand>`
  - ```{autodoc2-docstring} archivebox.abid_utils.abid.abid_part_from_rand
    :summary:
    ```
* - {py:obj}`abid_hashes_from_values <archivebox.abid_utils.abid.abid_hashes_from_values>`
  - ```{autodoc2-docstring} archivebox.abid_utils.abid.abid_hashes_from_values
    :summary:
    ```
* - {py:obj}`abid_from_values <archivebox.abid_utils.abid.abid_from_values>`
  - ```{autodoc2-docstring} archivebox.abid_utils.abid.abid_from_values
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <archivebox.abid_utils.abid.__package__>`
  - ```{autodoc2-docstring} archivebox.abid_utils.abid.__package__
    :summary:
    ```
* - {py:obj}`ABID_PREFIX_LEN <archivebox.abid_utils.abid.ABID_PREFIX_LEN>`
  - ```{autodoc2-docstring} archivebox.abid_utils.abid.ABID_PREFIX_LEN
    :summary:
    ```
* - {py:obj}`ABID_SUFFIX_LEN <archivebox.abid_utils.abid.ABID_SUFFIX_LEN>`
  - ```{autodoc2-docstring} archivebox.abid_utils.abid.ABID_SUFFIX_LEN
    :summary:
    ```
* - {py:obj}`ABID_LEN <archivebox.abid_utils.abid.ABID_LEN>`
  - ```{autodoc2-docstring} archivebox.abid_utils.abid.ABID_LEN
    :summary:
    ```
* - {py:obj}`ABID_TS_LEN <archivebox.abid_utils.abid.ABID_TS_LEN>`
  - ```{autodoc2-docstring} archivebox.abid_utils.abid.ABID_TS_LEN
    :summary:
    ```
* - {py:obj}`ABID_URI_LEN <archivebox.abid_utils.abid.ABID_URI_LEN>`
  - ```{autodoc2-docstring} archivebox.abid_utils.abid.ABID_URI_LEN
    :summary:
    ```
* - {py:obj}`ABID_SUBTYPE_LEN <archivebox.abid_utils.abid.ABID_SUBTYPE_LEN>`
  - ```{autodoc2-docstring} archivebox.abid_utils.abid.ABID_SUBTYPE_LEN
    :summary:
    ```
* - {py:obj}`ABID_RAND_LEN <archivebox.abid_utils.abid.ABID_RAND_LEN>`
  - ```{autodoc2-docstring} archivebox.abid_utils.abid.ABID_RAND_LEN
    :summary:
    ```
* - {py:obj}`DEFAULT_ABID_PREFIX <archivebox.abid_utils.abid.DEFAULT_ABID_PREFIX>`
  - ```{autodoc2-docstring} archivebox.abid_utils.abid.DEFAULT_ABID_PREFIX
    :summary:
    ```
* - {py:obj}`DEFAULT_ABID_URI_SALT <archivebox.abid_utils.abid.DEFAULT_ABID_URI_SALT>`
  - ```{autodoc2-docstring} archivebox.abid_utils.abid.DEFAULT_ABID_URI_SALT
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: archivebox.abid_utils.abid.__package__
:value: >
   'archivebox.abid_utils'

```{autodoc2-docstring} archivebox.abid_utils.abid.__package__
```

````

````{py:data} ABID_PREFIX_LEN
:canonical: archivebox.abid_utils.abid.ABID_PREFIX_LEN
:value: >
   4

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID_PREFIX_LEN
```

````

````{py:data} ABID_SUFFIX_LEN
:canonical: archivebox.abid_utils.abid.ABID_SUFFIX_LEN
:value: >
   26

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID_SUFFIX_LEN
```

````

````{py:data} ABID_LEN
:canonical: archivebox.abid_utils.abid.ABID_LEN
:value: >
   30

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID_LEN
```

````

````{py:data} ABID_TS_LEN
:canonical: archivebox.abid_utils.abid.ABID_TS_LEN
:value: >
   10

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID_TS_LEN
```

````

````{py:data} ABID_URI_LEN
:canonical: archivebox.abid_utils.abid.ABID_URI_LEN
:value: >
   8

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID_URI_LEN
```

````

````{py:data} ABID_SUBTYPE_LEN
:canonical: archivebox.abid_utils.abid.ABID_SUBTYPE_LEN
:value: >
   2

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID_SUBTYPE_LEN
```

````

````{py:data} ABID_RAND_LEN
:canonical: archivebox.abid_utils.abid.ABID_RAND_LEN
:value: >
   6

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID_RAND_LEN
```

````

````{py:data} DEFAULT_ABID_PREFIX
:canonical: archivebox.abid_utils.abid.DEFAULT_ABID_PREFIX
:value: >
   'obj_'

```{autodoc2-docstring} archivebox.abid_utils.abid.DEFAULT_ABID_PREFIX
```

````

````{py:data} DEFAULT_ABID_URI_SALT
:canonical: archivebox.abid_utils.abid.DEFAULT_ABID_URI_SALT
:value: >
   '687c2fff14e3a7780faa5a40c237b19b5b51b089'

```{autodoc2-docstring} archivebox.abid_utils.abid.DEFAULT_ABID_URI_SALT
```

````

`````{py:class} ABID
:canonical: archivebox.abid_utils.abid.ABID

Bases: {py:obj}`typing.NamedTuple`

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID
```

````{py:attribute} prefix
:canonical: archivebox.abid_utils.abid.ABID.prefix
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID.prefix
```

````

````{py:attribute} ts
:canonical: archivebox.abid_utils.abid.ABID.ts
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID.ts
```

````

````{py:attribute} uri
:canonical: archivebox.abid_utils.abid.ABID.uri
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID.uri
```

````

````{py:attribute} subtype
:canonical: archivebox.abid_utils.abid.ABID.subtype
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID.subtype
```

````

````{py:attribute} rand
:canonical: archivebox.abid_utils.abid.ABID.rand
:type: str
:value: >
   None

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID.rand
```

````

````{py:method} __getattr__(attr: str) -> typing.Any
:canonical: archivebox.abid_utils.abid.ABID.__getattr__

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID.__getattr__
```

````

````{py:method} __eq__(other: typing.Any) -> bool
:canonical: archivebox.abid_utils.abid.ABID.__eq__

````

````{py:method} __str__() -> str
:canonical: archivebox.abid_utils.abid.ABID.__str__

````

````{py:method} __len__() -> int
:canonical: archivebox.abid_utils.abid.ABID.__len__

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID.__len__
```

````

````{py:method} parse(buffer: typing.Union[str, uuid.UUID, ulid.ULID, typeid.TypeID, archivebox.abid_utils.abid.ABID], prefix=DEFAULT_ABID_PREFIX) -> archivebox.abid_utils.abid.ABID
:canonical: archivebox.abid_utils.abid.ABID.parse
:classmethod:

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID.parse
```

````

````{py:property} uri_salt
:canonical: archivebox.abid_utils.abid.ABID.uri_salt
:type: str

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID.uri_salt
```

````

````{py:property} suffix
:canonical: archivebox.abid_utils.abid.ABID.suffix

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID.suffix
```

````

````{py:property} ulid
:canonical: archivebox.abid_utils.abid.ABID.ulid
:type: ulid.ULID

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID.ulid
```

````

````{py:property} uuid
:canonical: archivebox.abid_utils.abid.ABID.uuid
:type: uuid.UUID

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID.uuid
```

````

````{py:property} uuid6
:canonical: archivebox.abid_utils.abid.ABID.uuid6
:type: uuid6.UUID

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID.uuid6
```

````

````{py:property} typeid
:canonical: archivebox.abid_utils.abid.ABID.typeid
:type: typeid.TypeID

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID.typeid
```

````

````{py:property} datetime
:canonical: archivebox.abid_utils.abid.ABID.datetime
:type: datetime.datetime

```{autodoc2-docstring} archivebox.abid_utils.abid.ABID.datetime
```

````

`````

````{py:function} uri_hash(uri: typing.Union[str, bytes], salt: str = DEFAULT_ABID_URI_SALT) -> str
:canonical: archivebox.abid_utils.abid.uri_hash

```{autodoc2-docstring} archivebox.abid_utils.abid.uri_hash
```
````

````{py:function} abid_part_from_prefix(prefix: str) -> str
:canonical: archivebox.abid_utils.abid.abid_part_from_prefix

```{autodoc2-docstring} archivebox.abid_utils.abid.abid_part_from_prefix
```
````

````{py:function} abid_part_from_uri(uri: typing.Any, salt: str = DEFAULT_ABID_URI_SALT) -> str
:canonical: archivebox.abid_utils.abid.abid_part_from_uri

```{autodoc2-docstring} archivebox.abid_utils.abid.abid_part_from_uri
```
````

````{py:function} abid_part_from_ts(ts: datetime.datetime) -> str
:canonical: archivebox.abid_utils.abid.abid_part_from_ts

```{autodoc2-docstring} archivebox.abid_utils.abid.abid_part_from_ts
```
````

````{py:function} ts_from_abid(abid: str) -> datetime.datetime
:canonical: archivebox.abid_utils.abid.ts_from_abid

```{autodoc2-docstring} archivebox.abid_utils.abid.ts_from_abid
```
````

````{py:function} abid_part_from_subtype(subtype: str | int) -> str
:canonical: archivebox.abid_utils.abid.abid_part_from_subtype

```{autodoc2-docstring} archivebox.abid_utils.abid.abid_part_from_subtype
```
````

````{py:function} abid_part_from_rand(rand: typing.Union[str, uuid.UUID, None, int]) -> str
:canonical: archivebox.abid_utils.abid.abid_part_from_rand

```{autodoc2-docstring} archivebox.abid_utils.abid.abid_part_from_rand
```
````

````{py:function} abid_hashes_from_values(prefix: str, ts: datetime.datetime, uri: typing.Any, subtype: str | int, rand: typing.Union[str, uuid.UUID, None, int], salt: str = DEFAULT_ABID_URI_SALT) -> typing.Dict[str, str]
:canonical: archivebox.abid_utils.abid.abid_hashes_from_values

```{autodoc2-docstring} archivebox.abid_utils.abid.abid_hashes_from_values
```
````

````{py:function} abid_from_values(prefix: str, ts: datetime.datetime, uri: str, subtype: str, rand: typing.Union[str, uuid.UUID, None, int], salt: str = DEFAULT_ABID_URI_SALT) -> archivebox.abid_utils.abid.ABID
:canonical: archivebox.abid_utils.abid.abid_from_values

```{autodoc2-docstring} archivebox.abid_utils.abid.abid_from_values
```
````
