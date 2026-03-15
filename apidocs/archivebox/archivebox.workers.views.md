# {py:mod}`archivebox.workers.views`

```{py:module} archivebox.workers.views
```

```{autodoc2-docstring} archivebox.workers.views
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`JobsDashboardView <archivebox.workers.views.JobsDashboardView>`
  -
````

### API

`````{py:class} JobsDashboardView(**kwargs)
:canonical: archivebox.workers.views.JobsDashboardView

Bases: {py:obj}`django.contrib.auth.mixins.UserPassesTestMixin`, {py:obj}`django.views.generic.TemplateView`

````{py:attribute} template_name
:canonical: archivebox.workers.views.JobsDashboardView.template_name
:value: >
   'jobs_dashboard.html'

```{autodoc2-docstring} archivebox.workers.views.JobsDashboardView.template_name
```

````

````{py:method} test_func()
:canonical: archivebox.workers.views.JobsDashboardView.test_func

```{autodoc2-docstring} archivebox.workers.views.JobsDashboardView.test_func
```

````

````{py:method} get_context_data(**kwargs)
:canonical: archivebox.workers.views.JobsDashboardView.get_context_data

```{autodoc2-docstring} archivebox.workers.views.JobsDashboardView.get_context_data
```

````

`````
