# {py:mod}`archivebox.tests.test_admin_views`

```{py:module} archivebox.tests.test_admin_views
```

```{autodoc2-docstring} archivebox.tests.test_admin_views
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestSnapshotProgressStats <archivebox.tests.test_admin_views.TestSnapshotProgressStats>`
  - ```{autodoc2-docstring} archivebox.tests.test_admin_views.TestSnapshotProgressStats
    :summary:
    ```
* - {py:obj}`TestAdminSnapshotListView <archivebox.tests.test_admin_views.TestAdminSnapshotListView>`
  - ```{autodoc2-docstring} archivebox.tests.test_admin_views.TestAdminSnapshotListView
    :summary:
    ```
* - {py:obj}`TestAdminSnapshotSearch <archivebox.tests.test_admin_views.TestAdminSnapshotSearch>`
  - ```{autodoc2-docstring} archivebox.tests.test_admin_views.TestAdminSnapshotSearch
    :summary:
    ```
* - {py:obj}`TestPublicIndexSearch <archivebox.tests.test_admin_views.TestPublicIndexSearch>`
  - ```{autodoc2-docstring} archivebox.tests.test_admin_views.TestPublicIndexSearch
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`admin_user <archivebox.tests.test_admin_views.admin_user>`
  - ```{autodoc2-docstring} archivebox.tests.test_admin_views.admin_user
    :summary:
    ```
* - {py:obj}`crawl <archivebox.tests.test_admin_views.crawl>`
  - ```{autodoc2-docstring} archivebox.tests.test_admin_views.crawl
    :summary:
    ```
* - {py:obj}`snapshot <archivebox.tests.test_admin_views.snapshot>`
  - ```{autodoc2-docstring} archivebox.tests.test_admin_views.snapshot
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`pytestmark <archivebox.tests.test_admin_views.pytestmark>`
  - ```{autodoc2-docstring} archivebox.tests.test_admin_views.pytestmark
    :summary:
    ```
* - {py:obj}`User <archivebox.tests.test_admin_views.User>`
  - ```{autodoc2-docstring} archivebox.tests.test_admin_views.User
    :summary:
    ```
* - {py:obj}`ADMIN_HOST <archivebox.tests.test_admin_views.ADMIN_HOST>`
  - ```{autodoc2-docstring} archivebox.tests.test_admin_views.ADMIN_HOST
    :summary:
    ```
* - {py:obj}`PUBLIC_HOST <archivebox.tests.test_admin_views.PUBLIC_HOST>`
  - ```{autodoc2-docstring} archivebox.tests.test_admin_views.PUBLIC_HOST
    :summary:
    ```
````

### API

````{py:data} pytestmark
:canonical: archivebox.tests.test_admin_views.pytestmark
:value: >
   None

```{autodoc2-docstring} archivebox.tests.test_admin_views.pytestmark
```

````

````{py:data} User
:canonical: archivebox.tests.test_admin_views.User
:value: >
   'get_user_model(...)'

```{autodoc2-docstring} archivebox.tests.test_admin_views.User
```

````

````{py:data} ADMIN_HOST
:canonical: archivebox.tests.test_admin_views.ADMIN_HOST
:value: >
   'admin.archivebox.localhost:8000'

```{autodoc2-docstring} archivebox.tests.test_admin_views.ADMIN_HOST
```

````

````{py:data} PUBLIC_HOST
:canonical: archivebox.tests.test_admin_views.PUBLIC_HOST
:value: >
   'public.archivebox.localhost:8000'

```{autodoc2-docstring} archivebox.tests.test_admin_views.PUBLIC_HOST
```

````

````{py:function} admin_user(db)
:canonical: archivebox.tests.test_admin_views.admin_user

```{autodoc2-docstring} archivebox.tests.test_admin_views.admin_user
```
````

````{py:function} crawl(admin_user, db)
:canonical: archivebox.tests.test_admin_views.crawl

```{autodoc2-docstring} archivebox.tests.test_admin_views.crawl
```
````

````{py:function} snapshot(crawl, db)
:canonical: archivebox.tests.test_admin_views.snapshot

```{autodoc2-docstring} archivebox.tests.test_admin_views.snapshot
```
````

`````{py:class} TestSnapshotProgressStats
:canonical: archivebox.tests.test_admin_views.TestSnapshotProgressStats

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestSnapshotProgressStats
```

````{py:method} test_get_progress_stats_empty(snapshot)
:canonical: archivebox.tests.test_admin_views.TestSnapshotProgressStats.test_get_progress_stats_empty

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestSnapshotProgressStats.test_get_progress_stats_empty
```

````

````{py:method} test_get_progress_stats_with_results(snapshot, db)
:canonical: archivebox.tests.test_admin_views.TestSnapshotProgressStats.test_get_progress_stats_with_results

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestSnapshotProgressStats.test_get_progress_stats_with_results
```

````

````{py:method} test_get_progress_stats_sealed(snapshot)
:canonical: archivebox.tests.test_admin_views.TestSnapshotProgressStats.test_get_progress_stats_sealed

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestSnapshotProgressStats.test_get_progress_stats_sealed
```

````

`````

`````{py:class} TestAdminSnapshotListView
:canonical: archivebox.tests.test_admin_views.TestAdminSnapshotListView

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestAdminSnapshotListView
```

````{py:method} test_list_view_renders(client, admin_user)
:canonical: archivebox.tests.test_admin_views.TestAdminSnapshotListView.test_list_view_renders

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestAdminSnapshotListView.test_list_view_renders
```

````

````{py:method} test_list_view_with_snapshots(client, admin_user, snapshot)
:canonical: archivebox.tests.test_admin_views.TestAdminSnapshotListView.test_list_view_with_snapshots

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestAdminSnapshotListView.test_list_view_with_snapshots
```

````

````{py:method} test_list_view_avoids_legacy_title_fallbacks(client, admin_user, snapshot, monkeypatch)
:canonical: archivebox.tests.test_admin_views.TestAdminSnapshotListView.test_list_view_avoids_legacy_title_fallbacks

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestAdminSnapshotListView.test_list_view_avoids_legacy_title_fallbacks
```

````

````{py:method} test_grid_view_renders(client, admin_user)
:canonical: archivebox.tests.test_admin_views.TestAdminSnapshotListView.test_grid_view_renders

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestAdminSnapshotListView.test_grid_view_renders
```

````

````{py:method} test_view_mode_switcher_present(client, admin_user)
:canonical: archivebox.tests.test_admin_views.TestAdminSnapshotListView.test_view_mode_switcher_present

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestAdminSnapshotListView.test_view_mode_switcher_present
```

````

`````

`````{py:class} TestAdminSnapshotSearch
:canonical: archivebox.tests.test_admin_views.TestAdminSnapshotSearch

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestAdminSnapshotSearch
```

````{py:method} test_search_by_url(client, admin_user, snapshot)
:canonical: archivebox.tests.test_admin_views.TestAdminSnapshotSearch.test_search_by_url

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestAdminSnapshotSearch.test_search_by_url
```

````

````{py:method} test_search_by_title(client, admin_user, crawl, db)
:canonical: archivebox.tests.test_admin_views.TestAdminSnapshotSearch.test_search_by_title

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestAdminSnapshotSearch.test_search_by_title
```

````

````{py:method} test_search_by_tag(client, admin_user, snapshot, db)
:canonical: archivebox.tests.test_admin_views.TestAdminSnapshotSearch.test_search_by_tag

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestAdminSnapshotSearch.test_search_by_tag
```

````

````{py:method} test_empty_search(client, admin_user)
:canonical: archivebox.tests.test_admin_views.TestAdminSnapshotSearch.test_empty_search

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestAdminSnapshotSearch.test_empty_search
```

````

````{py:method} test_no_results_search(client, admin_user)
:canonical: archivebox.tests.test_admin_views.TestAdminSnapshotSearch.test_no_results_search

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestAdminSnapshotSearch.test_no_results_search
```

````

`````

`````{py:class} TestPublicIndexSearch
:canonical: archivebox.tests.test_admin_views.TestPublicIndexSearch

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestPublicIndexSearch
```

````{py:method} public_snapshot(crawl, db)
:canonical: archivebox.tests.test_admin_views.TestPublicIndexSearch.public_snapshot

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestPublicIndexSearch.public_snapshot
```

````

````{py:method} test_public_search_by_url(client, public_snapshot)
:canonical: archivebox.tests.test_admin_views.TestPublicIndexSearch.test_public_search_by_url

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestPublicIndexSearch.test_public_search_by_url
```

````

````{py:method} test_public_search_by_title(client, public_snapshot)
:canonical: archivebox.tests.test_admin_views.TestPublicIndexSearch.test_public_search_by_title

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestPublicIndexSearch.test_public_search_by_title
```

````

````{py:method} test_public_search_query_type_meta(client, public_snapshot)
:canonical: archivebox.tests.test_admin_views.TestPublicIndexSearch.test_public_search_query_type_meta

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestPublicIndexSearch.test_public_search_query_type_meta
```

````

````{py:method} test_public_search_query_type_url(client, public_snapshot)
:canonical: archivebox.tests.test_admin_views.TestPublicIndexSearch.test_public_search_query_type_url

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestPublicIndexSearch.test_public_search_query_type_url
```

````

````{py:method} test_public_search_query_type_title(client, public_snapshot)
:canonical: archivebox.tests.test_admin_views.TestPublicIndexSearch.test_public_search_query_type_title

```{autodoc2-docstring} archivebox.tests.test_admin_views.TestPublicIndexSearch.test_public_search_query_type_title
```

````

`````
