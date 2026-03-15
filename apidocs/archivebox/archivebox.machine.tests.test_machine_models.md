# {py:mod}`archivebox.machine.tests.test_machine_models`

```{py:module} archivebox.machine.tests.test_machine_models
```

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestMachineModel <archivebox.machine.tests.test_machine_models.TestMachineModel>`
  - ```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestMachineModel
    :summary:
    ```
* - {py:obj}`TestNetworkInterfaceModel <archivebox.machine.tests.test_machine_models.TestNetworkInterfaceModel>`
  - ```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestNetworkInterfaceModel
    :summary:
    ```
* - {py:obj}`TestBinaryModel <archivebox.machine.tests.test_machine_models.TestBinaryModel>`
  - ```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestBinaryModel
    :summary:
    ```
* - {py:obj}`TestBinaryStateMachine <archivebox.machine.tests.test_machine_models.TestBinaryStateMachine>`
  - ```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestBinaryStateMachine
    :summary:
    ```
* - {py:obj}`TestProcessModel <archivebox.machine.tests.test_machine_models.TestProcessModel>`
  - ```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessModel
    :summary:
    ```
* - {py:obj}`TestProcessCurrent <archivebox.machine.tests.test_machine_models.TestProcessCurrent>`
  - ```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessCurrent
    :summary:
    ```
* - {py:obj}`TestProcessHierarchy <archivebox.machine.tests.test_machine_models.TestProcessHierarchy>`
  - ```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessHierarchy
    :summary:
    ```
* - {py:obj}`TestProcessLifecycle <archivebox.machine.tests.test_machine_models.TestProcessLifecycle>`
  - ```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessLifecycle
    :summary:
    ```
* - {py:obj}`TestProcessClassMethods <archivebox.machine.tests.test_machine_models.TestProcessClassMethods>`
  - ```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessClassMethods
    :summary:
    ```
* - {py:obj}`TestProcessStateMachine <archivebox.machine.tests.test_machine_models.TestProcessStateMachine>`
  - ```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessStateMachine
    :summary:
    ```
````

### API

`````{py:class} TestMachineModel(methodName='runTest')
:canonical: archivebox.machine.tests.test_machine_models.TestMachineModel

Bases: {py:obj}`django.test.TestCase`

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestMachineModel
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestMachineModel.__init__
```

````{py:method} setUp()
:canonical: archivebox.machine.tests.test_machine_models.TestMachineModel.setUp

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestMachineModel.setUp
```

````

````{py:method} test_machine_current_creates_machine()
:canonical: archivebox.machine.tests.test_machine_models.TestMachineModel.test_machine_current_creates_machine

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestMachineModel.test_machine_current_creates_machine
```

````

````{py:method} test_machine_current_returns_cached()
:canonical: archivebox.machine.tests.test_machine_models.TestMachineModel.test_machine_current_returns_cached

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestMachineModel.test_machine_current_returns_cached
```

````

````{py:method} test_machine_current_refreshes_after_interval()
:canonical: archivebox.machine.tests.test_machine_models.TestMachineModel.test_machine_current_refreshes_after_interval

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestMachineModel.test_machine_current_refreshes_after_interval
```

````

````{py:method} test_machine_from_jsonl_update()
:canonical: archivebox.machine.tests.test_machine_models.TestMachineModel.test_machine_from_jsonl_update

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestMachineModel.test_machine_from_jsonl_update
```

````

````{py:method} test_machine_from_jsonl_invalid()
:canonical: archivebox.machine.tests.test_machine_models.TestMachineModel.test_machine_from_jsonl_invalid

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestMachineModel.test_machine_from_jsonl_invalid
```

````

````{py:method} test_machine_manager_current()
:canonical: archivebox.machine.tests.test_machine_models.TestMachineModel.test_machine_manager_current

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestMachineModel.test_machine_manager_current
```

````

`````

`````{py:class} TestNetworkInterfaceModel(methodName='runTest')
:canonical: archivebox.machine.tests.test_machine_models.TestNetworkInterfaceModel

Bases: {py:obj}`django.test.TestCase`

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestNetworkInterfaceModel
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestNetworkInterfaceModel.__init__
```

````{py:method} setUp()
:canonical: archivebox.machine.tests.test_machine_models.TestNetworkInterfaceModel.setUp

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestNetworkInterfaceModel.setUp
```

````

````{py:method} test_networkinterface_current_creates_interface()
:canonical: archivebox.machine.tests.test_machine_models.TestNetworkInterfaceModel.test_networkinterface_current_creates_interface

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestNetworkInterfaceModel.test_networkinterface_current_creates_interface
```

````

````{py:method} test_networkinterface_current_returns_cached()
:canonical: archivebox.machine.tests.test_machine_models.TestNetworkInterfaceModel.test_networkinterface_current_returns_cached

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestNetworkInterfaceModel.test_networkinterface_current_returns_cached
```

````

````{py:method} test_networkinterface_manager_current()
:canonical: archivebox.machine.tests.test_machine_models.TestNetworkInterfaceModel.test_networkinterface_manager_current

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestNetworkInterfaceModel.test_networkinterface_manager_current
```

````

`````

`````{py:class} TestBinaryModel(methodName='runTest')
:canonical: archivebox.machine.tests.test_machine_models.TestBinaryModel

Bases: {py:obj}`django.test.TestCase`

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestBinaryModel
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestBinaryModel.__init__
```

````{py:method} setUp()
:canonical: archivebox.machine.tests.test_machine_models.TestBinaryModel.setUp

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestBinaryModel.setUp
```

````

````{py:method} test_binary_creation()
:canonical: archivebox.machine.tests.test_machine_models.TestBinaryModel.test_binary_creation

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestBinaryModel.test_binary_creation
```

````

````{py:method} test_binary_is_valid()
:canonical: archivebox.machine.tests.test_machine_models.TestBinaryModel.test_binary_is_valid

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestBinaryModel.test_binary_is_valid
```

````

````{py:method} test_binary_manager_get_valid_binary()
:canonical: archivebox.machine.tests.test_machine_models.TestBinaryModel.test_binary_manager_get_valid_binary

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestBinaryModel.test_binary_manager_get_valid_binary
```

````

````{py:method} test_binary_update_and_requeue()
:canonical: archivebox.machine.tests.test_machine_models.TestBinaryModel.test_binary_update_and_requeue

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestBinaryModel.test_binary_update_and_requeue
```

````

````{py:method} test_binary_from_json_preserves_install_args_overrides()
:canonical: archivebox.machine.tests.test_machine_models.TestBinaryModel.test_binary_from_json_preserves_install_args_overrides

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestBinaryModel.test_binary_from_json_preserves_install_args_overrides
```

````

````{py:method} test_binary_from_json_does_not_coerce_legacy_override_shapes()
:canonical: archivebox.machine.tests.test_machine_models.TestBinaryModel.test_binary_from_json_does_not_coerce_legacy_override_shapes

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestBinaryModel.test_binary_from_json_does_not_coerce_legacy_override_shapes
```

````

````{py:method} test_binary_from_json_prefers_published_readability_package()
:canonical: archivebox.machine.tests.test_machine_models.TestBinaryModel.test_binary_from_json_prefers_published_readability_package

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestBinaryModel.test_binary_from_json_prefers_published_readability_package
```

````

`````

`````{py:class} TestBinaryStateMachine(methodName='runTest')
:canonical: archivebox.machine.tests.test_machine_models.TestBinaryStateMachine

Bases: {py:obj}`django.test.TestCase`

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestBinaryStateMachine
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestBinaryStateMachine.__init__
```

````{py:method} setUp()
:canonical: archivebox.machine.tests.test_machine_models.TestBinaryStateMachine.setUp

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestBinaryStateMachine.setUp
```

````

````{py:method} test_binary_state_machine_initial_state()
:canonical: archivebox.machine.tests.test_machine_models.TestBinaryStateMachine.test_binary_state_machine_initial_state

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestBinaryStateMachine.test_binary_state_machine_initial_state
```

````

````{py:method} test_binary_state_machine_can_start()
:canonical: archivebox.machine.tests.test_machine_models.TestBinaryStateMachine.test_binary_state_machine_can_start

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestBinaryStateMachine.test_binary_state_machine_can_start
```

````

`````

`````{py:class} TestProcessModel(methodName='runTest')
:canonical: archivebox.machine.tests.test_machine_models.TestProcessModel

Bases: {py:obj}`django.test.TestCase`

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessModel
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessModel.__init__
```

````{py:method} setUp()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessModel.setUp

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessModel.setUp
```

````

````{py:method} test_process_creation()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessModel.test_process_creation

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessModel.test_process_creation
```

````

````{py:method} test_process_to_jsonl()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessModel.test_process_to_jsonl

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessModel.test_process_to_jsonl
```

````

````{py:method} test_process_update_and_requeue()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessModel.test_process_update_and_requeue

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessModel.test_process_update_and_requeue
```

````

`````

`````{py:class} TestProcessCurrent(methodName='runTest')
:canonical: archivebox.machine.tests.test_machine_models.TestProcessCurrent

Bases: {py:obj}`django.test.TestCase`

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessCurrent
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessCurrent.__init__
```

````{py:method} setUp()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessCurrent.setUp

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessCurrent.setUp
```

````

````{py:method} test_process_current_creates_record()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessCurrent.test_process_current_creates_record

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessCurrent.test_process_current_creates_record
```

````

````{py:method} test_process_current_caches()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessCurrent.test_process_current_caches

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessCurrent.test_process_current_caches
```

````

````{py:method} test_process_detect_type_orchestrator()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessCurrent.test_process_detect_type_orchestrator

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessCurrent.test_process_detect_type_orchestrator
```

````

````{py:method} test_process_detect_type_cli()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessCurrent.test_process_detect_type_cli

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessCurrent.test_process_detect_type_cli
```

````

````{py:method} test_process_detect_type_worker()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessCurrent.test_process_detect_type_worker

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessCurrent.test_process_detect_type_worker
```

````

`````

`````{py:class} TestProcessHierarchy(methodName='runTest')
:canonical: archivebox.machine.tests.test_machine_models.TestProcessHierarchy

Bases: {py:obj}`django.test.TestCase`

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessHierarchy
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessHierarchy.__init__
```

````{py:method} setUp()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessHierarchy.setUp

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessHierarchy.setUp
```

````

````{py:method} test_process_parent_child()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessHierarchy.test_process_parent_child

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessHierarchy.test_process_parent_child
```

````

````{py:method} test_process_root()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessHierarchy.test_process_root

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessHierarchy.test_process_root
```

````

````{py:method} test_process_depth()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessHierarchy.test_process_depth

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessHierarchy.test_process_depth
```

````

`````

`````{py:class} TestProcessLifecycle(methodName='runTest')
:canonical: archivebox.machine.tests.test_machine_models.TestProcessLifecycle

Bases: {py:obj}`django.test.TestCase`

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessLifecycle
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessLifecycle.__init__
```

````{py:method} setUp()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessLifecycle.setUp

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessLifecycle.setUp
```

````

````{py:method} test_process_is_running_current_pid()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessLifecycle.test_process_is_running_current_pid

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessLifecycle.test_process_is_running_current_pid
```

````

````{py:method} test_process_is_running_fake_pid()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessLifecycle.test_process_is_running_fake_pid

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessLifecycle.test_process_is_running_fake_pid
```

````

````{py:method} test_process_poll_detects_exit()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessLifecycle.test_process_poll_detects_exit

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessLifecycle.test_process_poll_detects_exit
```

````

````{py:method} test_process_poll_normalizes_negative_exit_code()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessLifecycle.test_process_poll_normalizes_negative_exit_code

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessLifecycle.test_process_poll_normalizes_negative_exit_code
```

````

````{py:method} test_process_terminate_dead_process()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessLifecycle.test_process_terminate_dead_process

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessLifecycle.test_process_terminate_dead_process
```

````

`````

`````{py:class} TestProcessClassMethods(methodName='runTest')
:canonical: archivebox.machine.tests.test_machine_models.TestProcessClassMethods

Bases: {py:obj}`django.test.TestCase`

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessClassMethods
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessClassMethods.__init__
```

````{py:method} setUp()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessClassMethods.setUp

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessClassMethods.setUp
```

````

````{py:method} test_get_running()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessClassMethods.test_get_running

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessClassMethods.test_get_running
```

````

````{py:method} test_get_running_count()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessClassMethods.test_get_running_count

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessClassMethods.test_get_running_count
```

````

````{py:method} test_cleanup_stale_running()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessClassMethods.test_cleanup_stale_running

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessClassMethods.test_cleanup_stale_running
```

````

`````

`````{py:class} TestProcessStateMachine(methodName='runTest')
:canonical: archivebox.machine.tests.test_machine_models.TestProcessStateMachine

Bases: {py:obj}`django.test.TestCase`

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessStateMachine
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessStateMachine.__init__
```

````{py:method} setUp()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessStateMachine.setUp

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessStateMachine.setUp
```

````

````{py:method} test_process_state_machine_initial_state()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessStateMachine.test_process_state_machine_initial_state

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessStateMachine.test_process_state_machine_initial_state
```

````

````{py:method} test_process_state_machine_can_start()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessStateMachine.test_process_state_machine_can_start

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessStateMachine.test_process_state_machine_can_start
```

````

````{py:method} test_process_state_machine_is_exited()
:canonical: archivebox.machine.tests.test_machine_models.TestProcessStateMachine.test_process_state_machine_is_exited

```{autodoc2-docstring} archivebox.machine.tests.test_machine_models.TestProcessStateMachine.test_process_state_machine_is_exited
```

````

`````
