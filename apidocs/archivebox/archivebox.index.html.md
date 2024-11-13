# {py:mod}`archivebox.index.html`

```{py:module} archivebox.index.html
```

```{autodoc2-docstring} archivebox.index.html
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`parse_html_main_index <archivebox.index.html.parse_html_main_index>`
  - ```{autodoc2-docstring} archivebox.index.html.parse_html_main_index
    :summary:
    ```
* - {py:obj}`generate_index_from_links <archivebox.index.html.generate_index_from_links>`
  - ```{autodoc2-docstring} archivebox.index.html.generate_index_from_links
    :summary:
    ```
* - {py:obj}`main_index_template <archivebox.index.html.main_index_template>`
  - ```{autodoc2-docstring} archivebox.index.html.main_index_template
    :summary:
    ```
* - {py:obj}`write_html_link_details <archivebox.index.html.write_html_link_details>`
  - ```{autodoc2-docstring} archivebox.index.html.write_html_link_details
    :summary:
    ```
* - {py:obj}`link_details_template <archivebox.index.html.link_details_template>`
  - ```{autodoc2-docstring} archivebox.index.html.link_details_template
    :summary:
    ```
* - {py:obj}`render_django_template <archivebox.index.html.render_django_template>`
  - ```{autodoc2-docstring} archivebox.index.html.render_django_template
    :summary:
    ```
* - {py:obj}`snapshot_icons <archivebox.index.html.snapshot_icons>`
  - ```{autodoc2-docstring} archivebox.index.html.snapshot_icons
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`MAIN_INDEX_TEMPLATE <archivebox.index.html.MAIN_INDEX_TEMPLATE>`
  - ```{autodoc2-docstring} archivebox.index.html.MAIN_INDEX_TEMPLATE
    :summary:
    ```
* - {py:obj}`MINIMAL_INDEX_TEMPLATE <archivebox.index.html.MINIMAL_INDEX_TEMPLATE>`
  - ```{autodoc2-docstring} archivebox.index.html.MINIMAL_INDEX_TEMPLATE
    :summary:
    ```
* - {py:obj}`LINK_DETAILS_TEMPLATE <archivebox.index.html.LINK_DETAILS_TEMPLATE>`
  - ```{autodoc2-docstring} archivebox.index.html.LINK_DETAILS_TEMPLATE
    :summary:
    ```
* - {py:obj}`TITLE_LOADING_MSG <archivebox.index.html.TITLE_LOADING_MSG>`
  - ```{autodoc2-docstring} archivebox.index.html.TITLE_LOADING_MSG
    :summary:
    ```
````

### API

````{py:data} MAIN_INDEX_TEMPLATE
:canonical: archivebox.index.html.MAIN_INDEX_TEMPLATE
:value: >
   'static_index.html'

```{autodoc2-docstring} archivebox.index.html.MAIN_INDEX_TEMPLATE
```

````

````{py:data} MINIMAL_INDEX_TEMPLATE
:canonical: archivebox.index.html.MINIMAL_INDEX_TEMPLATE
:value: >
   'minimal_index.html'

```{autodoc2-docstring} archivebox.index.html.MINIMAL_INDEX_TEMPLATE
```

````

````{py:data} LINK_DETAILS_TEMPLATE
:canonical: archivebox.index.html.LINK_DETAILS_TEMPLATE
:value: >
   'snapshot.html'

```{autodoc2-docstring} archivebox.index.html.LINK_DETAILS_TEMPLATE
```

````

````{py:data} TITLE_LOADING_MSG
:canonical: archivebox.index.html.TITLE_LOADING_MSG
:value: >
   'Not yet archived...'

```{autodoc2-docstring} archivebox.index.html.TITLE_LOADING_MSG
```

````

````{py:function} parse_html_main_index(out_dir: pathlib.Path = DATA_DIR) -> typing.Iterator[str]
:canonical: archivebox.index.html.parse_html_main_index

```{autodoc2-docstring} archivebox.index.html.parse_html_main_index
```
````

````{py:function} generate_index_from_links(links: typing.List[archivebox.index.schema.Link], with_headers: bool)
:canonical: archivebox.index.html.generate_index_from_links

```{autodoc2-docstring} archivebox.index.html.generate_index_from_links
```
````

````{py:function} main_index_template(links: typing.List[archivebox.index.schema.Link], template: str = MAIN_INDEX_TEMPLATE) -> str
:canonical: archivebox.index.html.main_index_template

```{autodoc2-docstring} archivebox.index.html.main_index_template
```
````

````{py:function} write_html_link_details(link: archivebox.index.schema.Link, out_dir: typing.Optional[str] = None) -> None
:canonical: archivebox.index.html.write_html_link_details

```{autodoc2-docstring} archivebox.index.html.write_html_link_details
```
````

````{py:function} link_details_template(link: archivebox.index.schema.Link) -> str
:canonical: archivebox.index.html.link_details_template

```{autodoc2-docstring} archivebox.index.html.link_details_template
```
````

````{py:function} render_django_template(template: str, context: typing.Mapping[str, str]) -> str
:canonical: archivebox.index.html.render_django_template

```{autodoc2-docstring} archivebox.index.html.render_django_template
```
````

````{py:function} snapshot_icons(snapshot) -> str
:canonical: archivebox.index.html.snapshot_icons

```{autodoc2-docstring} archivebox.index.html.snapshot_icons
```
````
