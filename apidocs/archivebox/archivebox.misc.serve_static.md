# {py:mod}`archivebox.misc.serve_static`

```{py:module} archivebox.misc.serve_static
```

```{autodoc2-docstring} archivebox.misc.serve_static
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`RangedFileReader <archivebox.misc.serve_static.RangedFileReader>`
  - ```{autodoc2-docstring} archivebox.misc.serve_static.RangedFileReader
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_load_hash_map <archivebox.misc.serve_static._load_hash_map>`
  - ```{autodoc2-docstring} archivebox.misc.serve_static._load_hash_map
    :summary:
    ```
* - {py:obj}`_hash_for_path <archivebox.misc.serve_static._hash_for_path>`
  - ```{autodoc2-docstring} archivebox.misc.serve_static._hash_for_path
    :summary:
    ```
* - {py:obj}`_cache_policy <archivebox.misc.serve_static._cache_policy>`
  - ```{autodoc2-docstring} archivebox.misc.serve_static._cache_policy
    :summary:
    ```
* - {py:obj}`_extract_markdown_candidate <archivebox.misc.serve_static._extract_markdown_candidate>`
  - ```{autodoc2-docstring} archivebox.misc.serve_static._extract_markdown_candidate
    :summary:
    ```
* - {py:obj}`_looks_like_markdown <archivebox.misc.serve_static._looks_like_markdown>`
  - ```{autodoc2-docstring} archivebox.misc.serve_static._looks_like_markdown
    :summary:
    ```
* - {py:obj}`_render_markdown_fallback <archivebox.misc.serve_static._render_markdown_fallback>`
  - ```{autodoc2-docstring} archivebox.misc.serve_static._render_markdown_fallback
    :summary:
    ```
* - {py:obj}`_render_markdown_document <archivebox.misc.serve_static._render_markdown_document>`
  - ```{autodoc2-docstring} archivebox.misc.serve_static._render_markdown_document
    :summary:
    ```
* - {py:obj}`serve_static_with_byterange_support <archivebox.misc.serve_static.serve_static_with_byterange_support>`
  - ```{autodoc2-docstring} archivebox.misc.serve_static.serve_static_with_byterange_support
    :summary:
    ```
* - {py:obj}`serve_static <archivebox.misc.serve_static.serve_static>`
  - ```{autodoc2-docstring} archivebox.misc.serve_static.serve_static
    :summary:
    ```
* - {py:obj}`parse_range_header <archivebox.misc.serve_static.parse_range_header>`
  - ```{autodoc2-docstring} archivebox.misc.serve_static.parse_range_header
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_HASHES_CACHE <archivebox.misc.serve_static._HASHES_CACHE>`
  - ```{autodoc2-docstring} archivebox.misc.serve_static._HASHES_CACHE
    :summary:
    ```
* - {py:obj}`MARKDOWN_INLINE_LINK_RE <archivebox.misc.serve_static.MARKDOWN_INLINE_LINK_RE>`
  - ```{autodoc2-docstring} archivebox.misc.serve_static.MARKDOWN_INLINE_LINK_RE
    :summary:
    ```
* - {py:obj}`MARKDOWN_INLINE_IMAGE_RE <archivebox.misc.serve_static.MARKDOWN_INLINE_IMAGE_RE>`
  - ```{autodoc2-docstring} archivebox.misc.serve_static.MARKDOWN_INLINE_IMAGE_RE
    :summary:
    ```
* - {py:obj}`MARKDOWN_BOLD_RE <archivebox.misc.serve_static.MARKDOWN_BOLD_RE>`
  - ```{autodoc2-docstring} archivebox.misc.serve_static.MARKDOWN_BOLD_RE
    :summary:
    ```
* - {py:obj}`MARKDOWN_ITALIC_RE <archivebox.misc.serve_static.MARKDOWN_ITALIC_RE>`
  - ```{autodoc2-docstring} archivebox.misc.serve_static.MARKDOWN_ITALIC_RE
    :summary:
    ```
* - {py:obj}`HTML_TAG_RE <archivebox.misc.serve_static.HTML_TAG_RE>`
  - ```{autodoc2-docstring} archivebox.misc.serve_static.HTML_TAG_RE
    :summary:
    ```
* - {py:obj}`HTML_BODY_RE <archivebox.misc.serve_static.HTML_BODY_RE>`
  - ```{autodoc2-docstring} archivebox.misc.serve_static.HTML_BODY_RE
    :summary:
    ```
````

### API

````{py:data} _HASHES_CACHE
:canonical: archivebox.misc.serve_static._HASHES_CACHE
:type: dict[pathlib.Path, tuple[float, dict[str, str]]]
:value: >
   None

```{autodoc2-docstring} archivebox.misc.serve_static._HASHES_CACHE
```

````

````{py:function} _load_hash_map(snapshot_dir: pathlib.Path) -> dict[str, str] | None
:canonical: archivebox.misc.serve_static._load_hash_map

```{autodoc2-docstring} archivebox.misc.serve_static._load_hash_map
```
````

````{py:function} _hash_for_path(document_root: pathlib.Path, rel_path: str) -> str | None
:canonical: archivebox.misc.serve_static._hash_for_path

```{autodoc2-docstring} archivebox.misc.serve_static._hash_for_path
```
````

````{py:function} _cache_policy() -> str
:canonical: archivebox.misc.serve_static._cache_policy

```{autodoc2-docstring} archivebox.misc.serve_static._cache_policy
```
````

````{py:data} MARKDOWN_INLINE_LINK_RE
:canonical: archivebox.misc.serve_static.MARKDOWN_INLINE_LINK_RE
:value: >
   'compile(...)'

```{autodoc2-docstring} archivebox.misc.serve_static.MARKDOWN_INLINE_LINK_RE
```

````

````{py:data} MARKDOWN_INLINE_IMAGE_RE
:canonical: archivebox.misc.serve_static.MARKDOWN_INLINE_IMAGE_RE
:value: >
   'compile(...)'

```{autodoc2-docstring} archivebox.misc.serve_static.MARKDOWN_INLINE_IMAGE_RE
```

````

````{py:data} MARKDOWN_BOLD_RE
:canonical: archivebox.misc.serve_static.MARKDOWN_BOLD_RE
:value: >
   'compile(...)'

```{autodoc2-docstring} archivebox.misc.serve_static.MARKDOWN_BOLD_RE
```

````

````{py:data} MARKDOWN_ITALIC_RE
:canonical: archivebox.misc.serve_static.MARKDOWN_ITALIC_RE
:value: >
   'compile(...)'

```{autodoc2-docstring} archivebox.misc.serve_static.MARKDOWN_ITALIC_RE
```

````

````{py:data} HTML_TAG_RE
:canonical: archivebox.misc.serve_static.HTML_TAG_RE
:value: >
   'compile(...)'

```{autodoc2-docstring} archivebox.misc.serve_static.HTML_TAG_RE
```

````

````{py:data} HTML_BODY_RE
:canonical: archivebox.misc.serve_static.HTML_BODY_RE
:value: >
   'compile(...)'

```{autodoc2-docstring} archivebox.misc.serve_static.HTML_BODY_RE
```

````

````{py:function} _extract_markdown_candidate(text: str) -> str
:canonical: archivebox.misc.serve_static._extract_markdown_candidate

```{autodoc2-docstring} archivebox.misc.serve_static._extract_markdown_candidate
```
````

````{py:function} _looks_like_markdown(text: str) -> bool
:canonical: archivebox.misc.serve_static._looks_like_markdown

```{autodoc2-docstring} archivebox.misc.serve_static._looks_like_markdown
```
````

````{py:function} _render_markdown_fallback(text: str) -> str
:canonical: archivebox.misc.serve_static._render_markdown_fallback

```{autodoc2-docstring} archivebox.misc.serve_static._render_markdown_fallback
```
````

````{py:function} _render_markdown_document(markdown_text: str) -> str
:canonical: archivebox.misc.serve_static._render_markdown_document

```{autodoc2-docstring} archivebox.misc.serve_static._render_markdown_document
```
````

````{py:function} serve_static_with_byterange_support(request, path, document_root=None, show_indexes=False)
:canonical: archivebox.misc.serve_static.serve_static_with_byterange_support

```{autodoc2-docstring} archivebox.misc.serve_static.serve_static_with_byterange_support
```
````

````{py:function} serve_static(request, path, **kwargs)
:canonical: archivebox.misc.serve_static.serve_static

```{autodoc2-docstring} archivebox.misc.serve_static.serve_static
```
````

````{py:function} parse_range_header(header, resource_size)
:canonical: archivebox.misc.serve_static.parse_range_header

```{autodoc2-docstring} archivebox.misc.serve_static.parse_range_header
```
````

`````{py:class} RangedFileReader(file_like, start=0, stop=float('inf'), block_size=None)
:canonical: archivebox.misc.serve_static.RangedFileReader

```{autodoc2-docstring} archivebox.misc.serve_static.RangedFileReader
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.misc.serve_static.RangedFileReader.__init__
```

````{py:attribute} block_size
:canonical: archivebox.misc.serve_static.RangedFileReader.block_size
:value: >
   8192

```{autodoc2-docstring} archivebox.misc.serve_static.RangedFileReader.block_size
```

````

````{py:method} __iter__()
:canonical: archivebox.misc.serve_static.RangedFileReader.__iter__

```{autodoc2-docstring} archivebox.misc.serve_static.RangedFileReader.__iter__
```

````

`````
