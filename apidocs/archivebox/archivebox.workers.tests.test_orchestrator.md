# {py:mod}`archivebox.workers.tests.test_orchestrator`

```{py:module} archivebox.workers.tests.test_orchestrator
```

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestOrchestratorUnit <archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit>`
  - ```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit
    :summary:
    ```
* - {py:obj}`TestOrchestratorWithProcess <archivebox.workers.tests.test_orchestrator.TestOrchestratorWithProcess>`
  - ```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorWithProcess
    :summary:
    ```
* - {py:obj}`TestProcessBasedWorkerTracking <archivebox.workers.tests.test_orchestrator.TestProcessBasedWorkerTracking>`
  - ```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestProcessBasedWorkerTracking
    :summary:
    ```
* - {py:obj}`TestProcessLifecycle <archivebox.workers.tests.test_orchestrator.TestProcessLifecycle>`
  - ```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestProcessLifecycle
    :summary:
    ```
````

### API

`````{py:class} TestOrchestratorUnit(methodName='runTest')
:canonical: archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit

Bases: {py:obj}`django.test.TestCase`

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.__init__
```

````{py:method} test_orchestrator_creation()
:canonical: archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_orchestrator_creation

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_orchestrator_creation
```

````

````{py:method} test_orchestrator_repr()
:canonical: archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_orchestrator_repr

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_orchestrator_repr
```

````

````{py:method} test_has_pending_work()
:canonical: archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_has_pending_work

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_has_pending_work
```

````

````{py:method} test_should_exit_not_exit_on_idle()
:canonical: archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_should_exit_not_exit_on_idle

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_should_exit_not_exit_on_idle
```

````

````{py:method} test_should_exit_pending_work()
:canonical: archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_should_exit_pending_work

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_should_exit_pending_work
```

````

````{py:method} test_should_exit_running_workers(mock_has_workers)
:canonical: archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_should_exit_running_workers

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_should_exit_running_workers
```

````

````{py:method} test_should_exit_idle_timeout(mock_future, mock_workers)
:canonical: archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_should_exit_idle_timeout

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_should_exit_idle_timeout
```

````

````{py:method} test_should_exit_below_idle_timeout(mock_future, mock_workers)
:canonical: archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_should_exit_below_idle_timeout

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_should_exit_below_idle_timeout
```

````

````{py:method} test_should_spawn_worker_no_queue()
:canonical: archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_should_spawn_worker_no_queue

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_should_spawn_worker_no_queue
```

````

````{py:method} test_should_spawn_worker_at_limit()
:canonical: archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_should_spawn_worker_at_limit

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_should_spawn_worker_at_limit
```

````

````{py:method} test_should_spawn_worker_at_total_limit(mock_total)
:canonical: archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_should_spawn_worker_at_total_limit

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_should_spawn_worker_at_total_limit
```

````

````{py:method} test_should_spawn_worker_success(mock_total)
:canonical: archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_should_spawn_worker_success

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_should_spawn_worker_success
```

````

````{py:method} test_should_spawn_worker_enough_workers(mock_total)
:canonical: archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_should_spawn_worker_enough_workers

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorUnit.test_should_spawn_worker_enough_workers
```

````

`````

`````{py:class} TestOrchestratorWithProcess(methodName='runTest')
:canonical: archivebox.workers.tests.test_orchestrator.TestOrchestratorWithProcess

Bases: {py:obj}`django.test.TestCase`

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorWithProcess
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorWithProcess.__init__
```

````{py:method} setUp()
:canonical: archivebox.workers.tests.test_orchestrator.TestOrchestratorWithProcess.setUp

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorWithProcess.setUp
```

````

````{py:method} test_is_running_no_orchestrator()
:canonical: archivebox.workers.tests.test_orchestrator.TestOrchestratorWithProcess.test_is_running_no_orchestrator

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorWithProcess.test_is_running_no_orchestrator
```

````

````{py:method} test_is_running_with_orchestrator_process()
:canonical: archivebox.workers.tests.test_orchestrator.TestOrchestratorWithProcess.test_is_running_with_orchestrator_process

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorWithProcess.test_is_running_with_orchestrator_process
```

````

````{py:method} test_orchestrator_uses_process_for_is_running()
:canonical: archivebox.workers.tests.test_orchestrator.TestOrchestratorWithProcess.test_orchestrator_uses_process_for_is_running

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorWithProcess.test_orchestrator_uses_process_for_is_running
```

````

````{py:method} test_orchestrator_scoped_worker_count()
:canonical: archivebox.workers.tests.test_orchestrator.TestOrchestratorWithProcess.test_orchestrator_scoped_worker_count

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestOrchestratorWithProcess.test_orchestrator_scoped_worker_count
```

````

`````

`````{py:class} TestProcessBasedWorkerTracking(methodName='runTest')
:canonical: archivebox.workers.tests.test_orchestrator.TestProcessBasedWorkerTracking

Bases: {py:obj}`django.test.TestCase`

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestProcessBasedWorkerTracking
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestProcessBasedWorkerTracking.__init__
```

````{py:method} setUp()
:canonical: archivebox.workers.tests.test_orchestrator.TestProcessBasedWorkerTracking.setUp

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestProcessBasedWorkerTracking.setUp
```

````

````{py:method} test_process_current_creates_record()
:canonical: archivebox.workers.tests.test_orchestrator.TestProcessBasedWorkerTracking.test_process_current_creates_record

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestProcessBasedWorkerTracking.test_process_current_creates_record
```

````

````{py:method} test_process_current_caches_result()
:canonical: archivebox.workers.tests.test_orchestrator.TestProcessBasedWorkerTracking.test_process_current_caches_result

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestProcessBasedWorkerTracking.test_process_current_caches_result
```

````

````{py:method} test_process_get_running_count()
:canonical: archivebox.workers.tests.test_orchestrator.TestProcessBasedWorkerTracking.test_process_get_running_count

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestProcessBasedWorkerTracking.test_process_get_running_count
```

````

````{py:method} test_process_get_next_worker_id()
:canonical: archivebox.workers.tests.test_orchestrator.TestProcessBasedWorkerTracking.test_process_get_next_worker_id

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestProcessBasedWorkerTracking.test_process_get_next_worker_id
```

````

````{py:method} test_process_cleanup_stale_running()
:canonical: archivebox.workers.tests.test_orchestrator.TestProcessBasedWorkerTracking.test_process_cleanup_stale_running

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestProcessBasedWorkerTracking.test_process_cleanup_stale_running
```

````

````{py:method} test_process_get_running()
:canonical: archivebox.workers.tests.test_orchestrator.TestProcessBasedWorkerTracking.test_process_get_running

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestProcessBasedWorkerTracking.test_process_get_running
```

````

````{py:method} test_process_type_detection()
:canonical: archivebox.workers.tests.test_orchestrator.TestProcessBasedWorkerTracking.test_process_type_detection

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestProcessBasedWorkerTracking.test_process_type_detection
```

````

`````

`````{py:class} TestProcessLifecycle(methodName='runTest')
:canonical: archivebox.workers.tests.test_orchestrator.TestProcessLifecycle

Bases: {py:obj}`django.test.TestCase`

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestProcessLifecycle
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestProcessLifecycle.__init__
```

````{py:method} setUp()
:canonical: archivebox.workers.tests.test_orchestrator.TestProcessLifecycle.setUp

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestProcessLifecycle.setUp
```

````

````{py:method} test_process_is_running_property()
:canonical: archivebox.workers.tests.test_orchestrator.TestProcessLifecycle.test_process_is_running_property

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestProcessLifecycle.test_process_is_running_property
```

````

````{py:method} test_process_poll()
:canonical: archivebox.workers.tests.test_orchestrator.TestProcessLifecycle.test_process_poll

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestProcessLifecycle.test_process_poll
```

````

````{py:method} test_process_terminate_already_dead()
:canonical: archivebox.workers.tests.test_orchestrator.TestProcessLifecycle.test_process_terminate_already_dead

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestProcessLifecycle.test_process_terminate_already_dead
```

````

````{py:method} test_process_tree_traversal()
:canonical: archivebox.workers.tests.test_orchestrator.TestProcessLifecycle.test_process_tree_traversal

```{autodoc2-docstring} archivebox.workers.tests.test_orchestrator.TestProcessLifecycle.test_process_tree_traversal
```

````

`````
