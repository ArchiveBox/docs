# {py:mod}`archivebox.actors.views`

```{py:module} archivebox.actors.views
```

```{autodoc2-docstring} archivebox.actors.views
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`JobsDashboardView <archivebox.actors.views.JobsDashboardView>`
  -
````

### API

`````{py:class} JobsDashboardView(**kwargs)
:canonical: archivebox.actors.views.JobsDashboardView

Bases: {py:obj}`django.contrib.auth.mixins.UserPassesTestMixin`, {py:obj}`django.views.generic.TemplateView`

````{py:attribute} template_name
:canonical: archivebox.actors.views.JobsDashboardView.template_name
:value: >
   'jobs_dashboard.html'

```{autodoc2-docstring} archivebox.actors.views.JobsDashboardView.template_name
```

````

````{py:method} test_func()
:canonical: archivebox.actors.views.JobsDashboardView.test_func

```{autodoc2-docstring} archivebox.actors.views.JobsDashboardView.test_func
```

````

````{py:method} get_context_data(**kwargs)
:canonical: archivebox.actors.views.JobsDashboardView.get_context_data

```{autodoc2-docstring} archivebox.actors.views.JobsDashboardView.get_context_data
```

````

`````
