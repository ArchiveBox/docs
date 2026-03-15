# {py:mod}`archivebox.tests.test_hooks`

```{py:module} archivebox.tests.test_hooks
```

```{autodoc2-docstring} archivebox.tests.test_hooks
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestBackgroundHookDetection <archivebox.tests.test_hooks.TestBackgroundHookDetection>`
  - ```{autodoc2-docstring} archivebox.tests.test_hooks.TestBackgroundHookDetection
    :summary:
    ```
* - {py:obj}`TestJSONLParsing <archivebox.tests.test_hooks.TestJSONLParsing>`
  - ```{autodoc2-docstring} archivebox.tests.test_hooks.TestJSONLParsing
    :summary:
    ```
* - {py:obj}`TestInstallHookEnvVarHandling <archivebox.tests.test_hooks.TestInstallHookEnvVarHandling>`
  - ```{autodoc2-docstring} archivebox.tests.test_hooks.TestInstallHookEnvVarHandling
    :summary:
    ```
* - {py:obj}`TestHookDiscovery <archivebox.tests.test_hooks.TestHookDiscovery>`
  - ```{autodoc2-docstring} archivebox.tests.test_hooks.TestHookDiscovery
    :summary:
    ```
* - {py:obj}`TestGetExtractorName <archivebox.tests.test_hooks.TestGetExtractorName>`
  - ```{autodoc2-docstring} archivebox.tests.test_hooks.TestGetExtractorName
    :summary:
    ```
* - {py:obj}`TestHookExecution <archivebox.tests.test_hooks.TestHookExecution>`
  - ```{autodoc2-docstring} archivebox.tests.test_hooks.TestHookExecution
    :summary:
    ```
* - {py:obj}`TestInstallHookOutput <archivebox.tests.test_hooks.TestInstallHookOutput>`
  - ```{autodoc2-docstring} archivebox.tests.test_hooks.TestInstallHookOutput
    :summary:
    ```
* - {py:obj}`TestSnapshotHookOutput <archivebox.tests.test_hooks.TestSnapshotHookOutput>`
  - ```{autodoc2-docstring} archivebox.tests.test_hooks.TestSnapshotHookOutput
    :summary:
    ```
* - {py:obj}`TestPluginMetadata <archivebox.tests.test_hooks.TestPluginMetadata>`
  - ```{autodoc2-docstring} archivebox.tests.test_hooks.TestPluginMetadata
    :summary:
    ```
````

### API

`````{py:class} TestBackgroundHookDetection(methodName='runTest')
:canonical: archivebox.tests.test_hooks.TestBackgroundHookDetection

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.tests.test_hooks.TestBackgroundHookDetection
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.tests.test_hooks.TestBackgroundHookDetection.__init__
```

````{py:method} test_bg_js_suffix_detected()
:canonical: archivebox.tests.test_hooks.TestBackgroundHookDetection.test_bg_js_suffix_detected

```{autodoc2-docstring} archivebox.tests.test_hooks.TestBackgroundHookDetection.test_bg_js_suffix_detected
```

````

````{py:method} test_bg_py_suffix_detected()
:canonical: archivebox.tests.test_hooks.TestBackgroundHookDetection.test_bg_py_suffix_detected

```{autodoc2-docstring} archivebox.tests.test_hooks.TestBackgroundHookDetection.test_bg_py_suffix_detected
```

````

````{py:method} test_bg_sh_suffix_detected()
:canonical: archivebox.tests.test_hooks.TestBackgroundHookDetection.test_bg_sh_suffix_detected

```{autodoc2-docstring} archivebox.tests.test_hooks.TestBackgroundHookDetection.test_bg_sh_suffix_detected
```

````

````{py:method} test_legacy_background_suffix_detected()
:canonical: archivebox.tests.test_hooks.TestBackgroundHookDetection.test_legacy_background_suffix_detected

```{autodoc2-docstring} archivebox.tests.test_hooks.TestBackgroundHookDetection.test_legacy_background_suffix_detected
```

````

````{py:method} test_foreground_hook_not_detected()
:canonical: archivebox.tests.test_hooks.TestBackgroundHookDetection.test_foreground_hook_not_detected

```{autodoc2-docstring} archivebox.tests.test_hooks.TestBackgroundHookDetection.test_foreground_hook_not_detected
```

````

````{py:method} test_foreground_py_hook_not_detected()
:canonical: archivebox.tests.test_hooks.TestBackgroundHookDetection.test_foreground_py_hook_not_detected

```{autodoc2-docstring} archivebox.tests.test_hooks.TestBackgroundHookDetection.test_foreground_py_hook_not_detected
```

````

`````

`````{py:class} TestJSONLParsing(methodName='runTest')
:canonical: archivebox.tests.test_hooks.TestJSONLParsing

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.tests.test_hooks.TestJSONLParsing
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.tests.test_hooks.TestJSONLParsing.__init__
```

````{py:method} test_parse_clean_jsonl()
:canonical: archivebox.tests.test_hooks.TestJSONLParsing.test_parse_clean_jsonl

```{autodoc2-docstring} archivebox.tests.test_hooks.TestJSONLParsing.test_parse_clean_jsonl
```

````

````{py:method} test_parse_multiple_jsonl_records()
:canonical: archivebox.tests.test_hooks.TestJSONLParsing.test_parse_multiple_jsonl_records

```{autodoc2-docstring} archivebox.tests.test_hooks.TestJSONLParsing.test_parse_multiple_jsonl_records
```

````

````{py:method} test_parse_jsonl_with_log_output()
:canonical: archivebox.tests.test_hooks.TestJSONLParsing.test_parse_jsonl_with_log_output

```{autodoc2-docstring} archivebox.tests.test_hooks.TestJSONLParsing.test_parse_jsonl_with_log_output
```

````

````{py:method} test_ignore_invalid_json()
:canonical: archivebox.tests.test_hooks.TestJSONLParsing.test_ignore_invalid_json

```{autodoc2-docstring} archivebox.tests.test_hooks.TestJSONLParsing.test_ignore_invalid_json
```

````

````{py:method} test_json_without_type_ignored()
:canonical: archivebox.tests.test_hooks.TestJSONLParsing.test_json_without_type_ignored

```{autodoc2-docstring} archivebox.tests.test_hooks.TestJSONLParsing.test_json_without_type_ignored
```

````

`````

`````{py:class} TestInstallHookEnvVarHandling(methodName='runTest')
:canonical: archivebox.tests.test_hooks.TestInstallHookEnvVarHandling

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.tests.test_hooks.TestInstallHookEnvVarHandling
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.tests.test_hooks.TestInstallHookEnvVarHandling.__init__
```

````{py:method} setUp()
:canonical: archivebox.tests.test_hooks.TestInstallHookEnvVarHandling.setUp

```{autodoc2-docstring} archivebox.tests.test_hooks.TestInstallHookEnvVarHandling.setUp
```

````

````{py:method} tearDown()
:canonical: archivebox.tests.test_hooks.TestInstallHookEnvVarHandling.tearDown

```{autodoc2-docstring} archivebox.tests.test_hooks.TestInstallHookEnvVarHandling.tearDown
```

````

````{py:method} test_binary_env_var_absolute_path_handling()
:canonical: archivebox.tests.test_hooks.TestInstallHookEnvVarHandling.test_binary_env_var_absolute_path_handling

```{autodoc2-docstring} archivebox.tests.test_hooks.TestInstallHookEnvVarHandling.test_binary_env_var_absolute_path_handling
```

````

````{py:method} test_binary_env_var_name_only_handling()
:canonical: archivebox.tests.test_hooks.TestInstallHookEnvVarHandling.test_binary_env_var_name_only_handling

```{autodoc2-docstring} archivebox.tests.test_hooks.TestInstallHookEnvVarHandling.test_binary_env_var_name_only_handling
```

````

````{py:method} test_binary_env_var_empty_default()
:canonical: archivebox.tests.test_hooks.TestInstallHookEnvVarHandling.test_binary_env_var_empty_default

```{autodoc2-docstring} archivebox.tests.test_hooks.TestInstallHookEnvVarHandling.test_binary_env_var_empty_default
```

````

`````

`````{py:class} TestHookDiscovery(methodName='runTest')
:canonical: archivebox.tests.test_hooks.TestHookDiscovery

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.tests.test_hooks.TestHookDiscovery
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.tests.test_hooks.TestHookDiscovery.__init__
```

````{py:method} setUp()
:canonical: archivebox.tests.test_hooks.TestHookDiscovery.setUp

```{autodoc2-docstring} archivebox.tests.test_hooks.TestHookDiscovery.setUp
```

````

````{py:method} tearDown()
:canonical: archivebox.tests.test_hooks.TestHookDiscovery.tearDown

```{autodoc2-docstring} archivebox.tests.test_hooks.TestHookDiscovery.tearDown
```

````

````{py:method} test_discover_hooks_by_event()
:canonical: archivebox.tests.test_hooks.TestHookDiscovery.test_discover_hooks_by_event

```{autodoc2-docstring} archivebox.tests.test_hooks.TestHookDiscovery.test_discover_hooks_by_event
```

````

````{py:method} test_discover_hooks_sorted_by_name()
:canonical: archivebox.tests.test_hooks.TestHookDiscovery.test_discover_hooks_sorted_by_name

```{autodoc2-docstring} archivebox.tests.test_hooks.TestHookDiscovery.test_discover_hooks_sorted_by_name
```

````

````{py:method} test_get_plugins_includes_non_snapshot_plugin_dirs()
:canonical: archivebox.tests.test_hooks.TestHookDiscovery.test_get_plugins_includes_non_snapshot_plugin_dirs

```{autodoc2-docstring} archivebox.tests.test_hooks.TestHookDiscovery.test_get_plugins_includes_non_snapshot_plugin_dirs
```

````

````{py:method} test_discover_binary_hooks_ignores_plugins_whitelist()
:canonical: archivebox.tests.test_hooks.TestHookDiscovery.test_discover_binary_hooks_ignores_plugins_whitelist

```{autodoc2-docstring} archivebox.tests.test_hooks.TestHookDiscovery.test_discover_binary_hooks_ignores_plugins_whitelist
```

````

````{py:method} test_discover_crawl_hooks_only_include_declared_plugin_dependencies()
:canonical: archivebox.tests.test_hooks.TestHookDiscovery.test_discover_crawl_hooks_only_include_declared_plugin_dependencies

```{autodoc2-docstring} archivebox.tests.test_hooks.TestHookDiscovery.test_discover_crawl_hooks_only_include_declared_plugin_dependencies
```

````

`````

`````{py:class} TestGetExtractorName(methodName='runTest')
:canonical: archivebox.tests.test_hooks.TestGetExtractorName

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.tests.test_hooks.TestGetExtractorName
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.tests.test_hooks.TestGetExtractorName.__init__
```

````{py:method} test_strip_numeric_prefix()
:canonical: archivebox.tests.test_hooks.TestGetExtractorName.test_strip_numeric_prefix

```{autodoc2-docstring} archivebox.tests.test_hooks.TestGetExtractorName.test_strip_numeric_prefix
```

````

````{py:method} test_no_prefix_unchanged()
:canonical: archivebox.tests.test_hooks.TestGetExtractorName.test_no_prefix_unchanged

```{autodoc2-docstring} archivebox.tests.test_hooks.TestGetExtractorName.test_no_prefix_unchanged
```

````

`````

`````{py:class} TestHookExecution(methodName='runTest')
:canonical: archivebox.tests.test_hooks.TestHookExecution

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.tests.test_hooks.TestHookExecution
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.tests.test_hooks.TestHookExecution.__init__
```

````{py:method} setUp()
:canonical: archivebox.tests.test_hooks.TestHookExecution.setUp

```{autodoc2-docstring} archivebox.tests.test_hooks.TestHookExecution.setUp
```

````

````{py:method} tearDown()
:canonical: archivebox.tests.test_hooks.TestHookExecution.tearDown

```{autodoc2-docstring} archivebox.tests.test_hooks.TestHookExecution.tearDown
```

````

````{py:method} test_python_hook_execution()
:canonical: archivebox.tests.test_hooks.TestHookExecution.test_python_hook_execution

```{autodoc2-docstring} archivebox.tests.test_hooks.TestHookExecution.test_python_hook_execution
```

````

````{py:method} test_js_hook_execution()
:canonical: archivebox.tests.test_hooks.TestHookExecution.test_js_hook_execution

```{autodoc2-docstring} archivebox.tests.test_hooks.TestHookExecution.test_js_hook_execution
```

````

````{py:method} test_hook_receives_cli_args()
:canonical: archivebox.tests.test_hooks.TestHookExecution.test_hook_receives_cli_args

```{autodoc2-docstring} archivebox.tests.test_hooks.TestHookExecution.test_hook_receives_cli_args
```

````

`````

`````{py:class} TestInstallHookOutput(methodName='runTest')
:canonical: archivebox.tests.test_hooks.TestInstallHookOutput

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.tests.test_hooks.TestInstallHookOutput
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.tests.test_hooks.TestInstallHookOutput.__init__
```

````{py:method} setUp()
:canonical: archivebox.tests.test_hooks.TestInstallHookOutput.setUp

```{autodoc2-docstring} archivebox.tests.test_hooks.TestInstallHookOutput.setUp
```

````

````{py:method} tearDown()
:canonical: archivebox.tests.test_hooks.TestInstallHookOutput.tearDown

```{autodoc2-docstring} archivebox.tests.test_hooks.TestInstallHookOutput.tearDown
```

````

````{py:method} test_install_hook_outputs_binary()
:canonical: archivebox.tests.test_hooks.TestInstallHookOutput.test_install_hook_outputs_binary

```{autodoc2-docstring} archivebox.tests.test_hooks.TestInstallHookOutput.test_install_hook_outputs_binary
```

````

````{py:method} test_install_hook_outputs_machine_config()
:canonical: archivebox.tests.test_hooks.TestInstallHookOutput.test_install_hook_outputs_machine_config

```{autodoc2-docstring} archivebox.tests.test_hooks.TestInstallHookOutput.test_install_hook_outputs_machine_config
```

````

`````

`````{py:class} TestSnapshotHookOutput(methodName='runTest')
:canonical: archivebox.tests.test_hooks.TestSnapshotHookOutput

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.tests.test_hooks.TestSnapshotHookOutput
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.tests.test_hooks.TestSnapshotHookOutput.__init__
```

````{py:method} test_snapshot_hook_basic_output()
:canonical: archivebox.tests.test_hooks.TestSnapshotHookOutput.test_snapshot_hook_basic_output

```{autodoc2-docstring} archivebox.tests.test_hooks.TestSnapshotHookOutput.test_snapshot_hook_basic_output
```

````

````{py:method} test_snapshot_hook_with_cmd()
:canonical: archivebox.tests.test_hooks.TestSnapshotHookOutput.test_snapshot_hook_with_cmd

```{autodoc2-docstring} archivebox.tests.test_hooks.TestSnapshotHookOutput.test_snapshot_hook_with_cmd
```

````

````{py:method} test_snapshot_hook_with_output_json()
:canonical: archivebox.tests.test_hooks.TestSnapshotHookOutput.test_snapshot_hook_with_output_json

```{autodoc2-docstring} archivebox.tests.test_hooks.TestSnapshotHookOutput.test_snapshot_hook_with_output_json
```

````

````{py:method} test_snapshot_hook_skipped_status()
:canonical: archivebox.tests.test_hooks.TestSnapshotHookOutput.test_snapshot_hook_skipped_status

```{autodoc2-docstring} archivebox.tests.test_hooks.TestSnapshotHookOutput.test_snapshot_hook_skipped_status
```

````

````{py:method} test_snapshot_hook_failed_status()
:canonical: archivebox.tests.test_hooks.TestSnapshotHookOutput.test_snapshot_hook_failed_status

```{autodoc2-docstring} archivebox.tests.test_hooks.TestSnapshotHookOutput.test_snapshot_hook_failed_status
```

````

`````

`````{py:class} TestPluginMetadata(methodName='runTest')
:canonical: archivebox.tests.test_hooks.TestPluginMetadata

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.tests.test_hooks.TestPluginMetadata
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.tests.test_hooks.TestPluginMetadata.__init__
```

````{py:method} test_plugin_name_added()
:canonical: archivebox.tests.test_hooks.TestPluginMetadata.test_plugin_name_added

```{autodoc2-docstring} archivebox.tests.test_hooks.TestPluginMetadata.test_plugin_name_added
```

````

`````
