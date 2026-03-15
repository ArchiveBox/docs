# {py:mod}`archivebox.cli.tests_piping`

```{py:module} archivebox.cli.tests_piping
```

```{autodoc2-docstring} archivebox.cli.tests_piping
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestJSONLParsing <archivebox.cli.tests_piping.TestJSONLParsing>`
  - ```{autodoc2-docstring} archivebox.cli.tests_piping.TestJSONLParsing
    :summary:
    ```
* - {py:obj}`TestReadArgsOrStdin <archivebox.cli.tests_piping.TestReadArgsOrStdin>`
  - ```{autodoc2-docstring} archivebox.cli.tests_piping.TestReadArgsOrStdin
    :summary:
    ```
* - {py:obj}`TestCrawlCommand <archivebox.cli.tests_piping.TestCrawlCommand>`
  - ```{autodoc2-docstring} archivebox.cli.tests_piping.TestCrawlCommand
    :summary:
    ```
* - {py:obj}`TestSnapshotCommand <archivebox.cli.tests_piping.TestSnapshotCommand>`
  - ```{autodoc2-docstring} archivebox.cli.tests_piping.TestSnapshotCommand
    :summary:
    ```
* - {py:obj}`TestArchiveResultCommand <archivebox.cli.tests_piping.TestArchiveResultCommand>`
  - ```{autodoc2-docstring} archivebox.cli.tests_piping.TestArchiveResultCommand
    :summary:
    ```
* - {py:obj}`TestURLCollection <archivebox.cli.tests_piping.TestURLCollection>`
  - ```{autodoc2-docstring} archivebox.cli.tests_piping.TestURLCollection
    :summary:
    ```
* - {py:obj}`TestPipingWorkflowIntegration <archivebox.cli.tests_piping.TestPipingWorkflowIntegration>`
  - ```{autodoc2-docstring} archivebox.cli.tests_piping.TestPipingWorkflowIntegration
    :summary:
    ```
* - {py:obj}`TestDepthWorkflows <archivebox.cli.tests_piping.TestDepthWorkflows>`
  - ```{autodoc2-docstring} archivebox.cli.tests_piping.TestDepthWorkflows
    :summary:
    ```
* - {py:obj}`TestParserPluginWorkflows <archivebox.cli.tests_piping.TestParserPluginWorkflows>`
  - ```{autodoc2-docstring} archivebox.cli.tests_piping.TestParserPluginWorkflows
    :summary:
    ```
* - {py:obj}`TestEdgeCases <archivebox.cli.tests_piping.TestEdgeCases>`
  - ```{autodoc2-docstring} archivebox.cli.tests_piping.TestEdgeCases
    :summary:
    ```
* - {py:obj}`TestPassThroughBehavior <archivebox.cli.tests_piping.TestPassThroughBehavior>`
  - ```{autodoc2-docstring} archivebox.cli.tests_piping.TestPassThroughBehavior
    :summary:
    ```
* - {py:obj}`TestPipelineAccumulation <archivebox.cli.tests_piping.TestPipelineAccumulation>`
  - ```{autodoc2-docstring} archivebox.cli.tests_piping.TestPipelineAccumulation
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TEST_CONFIG <archivebox.cli.tests_piping.TEST_CONFIG>`
  - ```{autodoc2-docstring} archivebox.cli.tests_piping.TEST_CONFIG
    :summary:
    ```
````

### API

````{py:data} TEST_CONFIG
:canonical: archivebox.cli.tests_piping.TEST_CONFIG
:value: >
   None

```{autodoc2-docstring} archivebox.cli.tests_piping.TEST_CONFIG
```

````

`````{py:class} TestJSONLParsing(methodName='runTest')
:canonical: archivebox.cli.tests_piping.TestJSONLParsing

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.cli.tests_piping.TestJSONLParsing
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.cli.tests_piping.TestJSONLParsing.__init__
```

````{py:method} test_parse_plain_url()
:canonical: archivebox.cli.tests_piping.TestJSONLParsing.test_parse_plain_url

```{autodoc2-docstring} archivebox.cli.tests_piping.TestJSONLParsing.test_parse_plain_url
```

````

````{py:method} test_parse_jsonl_snapshot()
:canonical: archivebox.cli.tests_piping.TestJSONLParsing.test_parse_jsonl_snapshot

```{autodoc2-docstring} archivebox.cli.tests_piping.TestJSONLParsing.test_parse_jsonl_snapshot
```

````

````{py:method} test_parse_jsonl_crawl()
:canonical: archivebox.cli.tests_piping.TestJSONLParsing.test_parse_jsonl_crawl

```{autodoc2-docstring} archivebox.cli.tests_piping.TestJSONLParsing.test_parse_jsonl_crawl
```

````

````{py:method} test_parse_jsonl_with_id()
:canonical: archivebox.cli.tests_piping.TestJSONLParsing.test_parse_jsonl_with_id

```{autodoc2-docstring} archivebox.cli.tests_piping.TestJSONLParsing.test_parse_jsonl_with_id
```

````

````{py:method} test_parse_uuid_as_snapshot_id()
:canonical: archivebox.cli.tests_piping.TestJSONLParsing.test_parse_uuid_as_snapshot_id

```{autodoc2-docstring} archivebox.cli.tests_piping.TestJSONLParsing.test_parse_uuid_as_snapshot_id
```

````

````{py:method} test_parse_empty_line()
:canonical: archivebox.cli.tests_piping.TestJSONLParsing.test_parse_empty_line

```{autodoc2-docstring} archivebox.cli.tests_piping.TestJSONLParsing.test_parse_empty_line
```

````

````{py:method} test_parse_comment_line()
:canonical: archivebox.cli.tests_piping.TestJSONLParsing.test_parse_comment_line

```{autodoc2-docstring} archivebox.cli.tests_piping.TestJSONLParsing.test_parse_comment_line
```

````

````{py:method} test_parse_invalid_url()
:canonical: archivebox.cli.tests_piping.TestJSONLParsing.test_parse_invalid_url

```{autodoc2-docstring} archivebox.cli.tests_piping.TestJSONLParsing.test_parse_invalid_url
```

````

````{py:method} test_parse_file_url()
:canonical: archivebox.cli.tests_piping.TestJSONLParsing.test_parse_file_url

```{autodoc2-docstring} archivebox.cli.tests_piping.TestJSONLParsing.test_parse_file_url
```

````

`````

`````{py:class} TestReadArgsOrStdin(methodName='runTest')
:canonical: archivebox.cli.tests_piping.TestReadArgsOrStdin

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.cli.tests_piping.TestReadArgsOrStdin
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.cli.tests_piping.TestReadArgsOrStdin.__init__
```

````{py:method} test_read_from_args()
:canonical: archivebox.cli.tests_piping.TestReadArgsOrStdin.test_read_from_args

```{autodoc2-docstring} archivebox.cli.tests_piping.TestReadArgsOrStdin.test_read_from_args
```

````

````{py:method} test_read_from_stdin()
:canonical: archivebox.cli.tests_piping.TestReadArgsOrStdin.test_read_from_stdin

```{autodoc2-docstring} archivebox.cli.tests_piping.TestReadArgsOrStdin.test_read_from_stdin
```

````

````{py:method} test_read_jsonl_from_stdin()
:canonical: archivebox.cli.tests_piping.TestReadArgsOrStdin.test_read_jsonl_from_stdin

```{autodoc2-docstring} archivebox.cli.tests_piping.TestReadArgsOrStdin.test_read_jsonl_from_stdin
```

````

````{py:method} test_read_crawl_jsonl_from_stdin()
:canonical: archivebox.cli.tests_piping.TestReadArgsOrStdin.test_read_crawl_jsonl_from_stdin

```{autodoc2-docstring} archivebox.cli.tests_piping.TestReadArgsOrStdin.test_read_crawl_jsonl_from_stdin
```

````

````{py:method} test_skip_tty_stdin()
:canonical: archivebox.cli.tests_piping.TestReadArgsOrStdin.test_skip_tty_stdin

```{autodoc2-docstring} archivebox.cli.tests_piping.TestReadArgsOrStdin.test_skip_tty_stdin
```

````

`````

`````{py:class} TestCrawlCommand(methodName='runTest')
:canonical: archivebox.cli.tests_piping.TestCrawlCommand

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.cli.tests_piping.TestCrawlCommand
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.cli.tests_piping.TestCrawlCommand.__init__
```

````{py:method} setUp()
:canonical: archivebox.cli.tests_piping.TestCrawlCommand.setUp

```{autodoc2-docstring} archivebox.cli.tests_piping.TestCrawlCommand.setUp
```

````

````{py:method} tearDown()
:canonical: archivebox.cli.tests_piping.TestCrawlCommand.tearDown

```{autodoc2-docstring} archivebox.cli.tests_piping.TestCrawlCommand.tearDown
```

````

````{py:method} test_crawl_accepts_url()
:canonical: archivebox.cli.tests_piping.TestCrawlCommand.test_crawl_accepts_url

```{autodoc2-docstring} archivebox.cli.tests_piping.TestCrawlCommand.test_crawl_accepts_url
```

````

````{py:method} test_crawl_output_format()
:canonical: archivebox.cli.tests_piping.TestCrawlCommand.test_crawl_output_format

```{autodoc2-docstring} archivebox.cli.tests_piping.TestCrawlCommand.test_crawl_output_format
```

````

`````

`````{py:class} TestSnapshotCommand(methodName='runTest')
:canonical: archivebox.cli.tests_piping.TestSnapshotCommand

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.cli.tests_piping.TestSnapshotCommand
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.cli.tests_piping.TestSnapshotCommand.__init__
```

````{py:method} setUp()
:canonical: archivebox.cli.tests_piping.TestSnapshotCommand.setUp

```{autodoc2-docstring} archivebox.cli.tests_piping.TestSnapshotCommand.setUp
```

````

````{py:method} tearDown()
:canonical: archivebox.cli.tests_piping.TestSnapshotCommand.tearDown

```{autodoc2-docstring} archivebox.cli.tests_piping.TestSnapshotCommand.tearDown
```

````

````{py:method} test_snapshot_accepts_url()
:canonical: archivebox.cli.tests_piping.TestSnapshotCommand.test_snapshot_accepts_url

```{autodoc2-docstring} archivebox.cli.tests_piping.TestSnapshotCommand.test_snapshot_accepts_url
```

````

````{py:method} test_snapshot_accepts_crawl_jsonl()
:canonical: archivebox.cli.tests_piping.TestSnapshotCommand.test_snapshot_accepts_crawl_jsonl

```{autodoc2-docstring} archivebox.cli.tests_piping.TestSnapshotCommand.test_snapshot_accepts_crawl_jsonl
```

````

````{py:method} test_snapshot_accepts_jsonl_with_metadata()
:canonical: archivebox.cli.tests_piping.TestSnapshotCommand.test_snapshot_accepts_jsonl_with_metadata

```{autodoc2-docstring} archivebox.cli.tests_piping.TestSnapshotCommand.test_snapshot_accepts_jsonl_with_metadata
```

````

`````

`````{py:class} TestArchiveResultCommand(methodName='runTest')
:canonical: archivebox.cli.tests_piping.TestArchiveResultCommand

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.cli.tests_piping.TestArchiveResultCommand
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.cli.tests_piping.TestArchiveResultCommand.__init__
```

````{py:method} setUp()
:canonical: archivebox.cli.tests_piping.TestArchiveResultCommand.setUp

```{autodoc2-docstring} archivebox.cli.tests_piping.TestArchiveResultCommand.setUp
```

````

````{py:method} tearDown()
:canonical: archivebox.cli.tests_piping.TestArchiveResultCommand.tearDown

```{autodoc2-docstring} archivebox.cli.tests_piping.TestArchiveResultCommand.tearDown
```

````

````{py:method} test_archiveresult_accepts_snapshot_id()
:canonical: archivebox.cli.tests_piping.TestArchiveResultCommand.test_archiveresult_accepts_snapshot_id

```{autodoc2-docstring} archivebox.cli.tests_piping.TestArchiveResultCommand.test_archiveresult_accepts_snapshot_id
```

````

````{py:method} test_archiveresult_accepts_jsonl_snapshot()
:canonical: archivebox.cli.tests_piping.TestArchiveResultCommand.test_archiveresult_accepts_jsonl_snapshot

```{autodoc2-docstring} archivebox.cli.tests_piping.TestArchiveResultCommand.test_archiveresult_accepts_jsonl_snapshot
```

````

````{py:method} test_archiveresult_gathers_snapshot_ids()
:canonical: archivebox.cli.tests_piping.TestArchiveResultCommand.test_archiveresult_gathers_snapshot_ids

```{autodoc2-docstring} archivebox.cli.tests_piping.TestArchiveResultCommand.test_archiveresult_gathers_snapshot_ids
```

````

`````

`````{py:class} TestURLCollection(methodName='runTest')
:canonical: archivebox.cli.tests_piping.TestURLCollection

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.cli.tests_piping.TestURLCollection
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.cli.tests_piping.TestURLCollection.__init__
```

````{py:method} setUp()
:canonical: archivebox.cli.tests_piping.TestURLCollection.setUp

```{autodoc2-docstring} archivebox.cli.tests_piping.TestURLCollection.setUp
```

````

````{py:method} tearDown()
:canonical: archivebox.cli.tests_piping.TestURLCollection.tearDown

```{autodoc2-docstring} archivebox.cli.tests_piping.TestURLCollection.tearDown
```

````

````{py:method} test_collect_urls_from_plugins()
:canonical: archivebox.cli.tests_piping.TestURLCollection.test_collect_urls_from_plugins

```{autodoc2-docstring} archivebox.cli.tests_piping.TestURLCollection.test_collect_urls_from_plugins
```

````

````{py:method} test_collect_urls_preserves_metadata()
:canonical: archivebox.cli.tests_piping.TestURLCollection.test_collect_urls_preserves_metadata

```{autodoc2-docstring} archivebox.cli.tests_piping.TestURLCollection.test_collect_urls_preserves_metadata
```

````

````{py:method} test_collect_urls_empty_dir()
:canonical: archivebox.cli.tests_piping.TestURLCollection.test_collect_urls_empty_dir

```{autodoc2-docstring} archivebox.cli.tests_piping.TestURLCollection.test_collect_urls_empty_dir
```

````

`````

`````{py:class} TestPipingWorkflowIntegration(methodName='runTest')
:canonical: archivebox.cli.tests_piping.TestPipingWorkflowIntegration

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.cli.tests_piping.TestPipingWorkflowIntegration
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.cli.tests_piping.TestPipingWorkflowIntegration.__init__
```

````{py:method} setUpClass()
:canonical: archivebox.cli.tests_piping.TestPipingWorkflowIntegration.setUpClass
:classmethod:

```{autodoc2-docstring} archivebox.cli.tests_piping.TestPipingWorkflowIntegration.setUpClass
```

````

````{py:method} tearDownClass()
:canonical: archivebox.cli.tests_piping.TestPipingWorkflowIntegration.tearDownClass
:classmethod:

```{autodoc2-docstring} archivebox.cli.tests_piping.TestPipingWorkflowIntegration.tearDownClass
```

````

````{py:method} test_crawl_creates_and_outputs_jsonl()
:canonical: archivebox.cli.tests_piping.TestPipingWorkflowIntegration.test_crawl_creates_and_outputs_jsonl

```{autodoc2-docstring} archivebox.cli.tests_piping.TestPipingWorkflowIntegration.test_crawl_creates_and_outputs_jsonl
```

````

````{py:method} test_snapshot_accepts_crawl_jsonl()
:canonical: archivebox.cli.tests_piping.TestPipingWorkflowIntegration.test_snapshot_accepts_crawl_jsonl

```{autodoc2-docstring} archivebox.cli.tests_piping.TestPipingWorkflowIntegration.test_snapshot_accepts_crawl_jsonl
```

````

````{py:method} test_snapshot_creates_and_outputs_jsonl()
:canonical: archivebox.cli.tests_piping.TestPipingWorkflowIntegration.test_snapshot_creates_and_outputs_jsonl

```{autodoc2-docstring} archivebox.cli.tests_piping.TestPipingWorkflowIntegration.test_snapshot_creates_and_outputs_jsonl
```

````

````{py:method} test_extract_accepts_snapshot_from_previous_command()
:canonical: archivebox.cli.tests_piping.TestPipingWorkflowIntegration.test_extract_accepts_snapshot_from_previous_command

```{autodoc2-docstring} archivebox.cli.tests_piping.TestPipingWorkflowIntegration.test_extract_accepts_snapshot_from_previous_command
```

````

````{py:method} test_full_pipeline_crawl_snapshot_extract()
:canonical: archivebox.cli.tests_piping.TestPipingWorkflowIntegration.test_full_pipeline_crawl_snapshot_extract

```{autodoc2-docstring} archivebox.cli.tests_piping.TestPipingWorkflowIntegration.test_full_pipeline_crawl_snapshot_extract
```

````

`````

`````{py:class} TestDepthWorkflows(methodName='runTest')
:canonical: archivebox.cli.tests_piping.TestDepthWorkflows

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.cli.tests_piping.TestDepthWorkflows
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.cli.tests_piping.TestDepthWorkflows.__init__
```

````{py:method} setUpClass()
:canonical: archivebox.cli.tests_piping.TestDepthWorkflows.setUpClass
:classmethod:

```{autodoc2-docstring} archivebox.cli.tests_piping.TestDepthWorkflows.setUpClass
```

````

````{py:method} tearDownClass()
:canonical: archivebox.cli.tests_piping.TestDepthWorkflows.tearDownClass
:classmethod:

```{autodoc2-docstring} archivebox.cli.tests_piping.TestDepthWorkflows.tearDownClass
```

````

````{py:method} test_depth_0_workflow()
:canonical: archivebox.cli.tests_piping.TestDepthWorkflows.test_depth_0_workflow

```{autodoc2-docstring} archivebox.cli.tests_piping.TestDepthWorkflows.test_depth_0_workflow
```

````

````{py:method} test_depth_metadata_in_crawl()
:canonical: archivebox.cli.tests_piping.TestDepthWorkflows.test_depth_metadata_in_crawl

```{autodoc2-docstring} archivebox.cli.tests_piping.TestDepthWorkflows.test_depth_metadata_in_crawl
```

````

`````

`````{py:class} TestParserPluginWorkflows(methodName='runTest')
:canonical: archivebox.cli.tests_piping.TestParserPluginWorkflows

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.cli.tests_piping.TestParserPluginWorkflows
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.cli.tests_piping.TestParserPluginWorkflows.__init__
```

````{py:method} setUpClass()
:canonical: archivebox.cli.tests_piping.TestParserPluginWorkflows.setUpClass
:classmethod:

```{autodoc2-docstring} archivebox.cli.tests_piping.TestParserPluginWorkflows.setUpClass
```

````

````{py:method} tearDownClass()
:canonical: archivebox.cli.tests_piping.TestParserPluginWorkflows.tearDownClass
:classmethod:

```{autodoc2-docstring} archivebox.cli.tests_piping.TestParserPluginWorkflows.tearDownClass
```

````

````{py:method} test_html_parser_workflow()
:canonical: archivebox.cli.tests_piping.TestParserPluginWorkflows.test_html_parser_workflow

```{autodoc2-docstring} archivebox.cli.tests_piping.TestParserPluginWorkflows.test_html_parser_workflow
```

````

````{py:method} test_rss_parser_workflow()
:canonical: archivebox.cli.tests_piping.TestParserPluginWorkflows.test_rss_parser_workflow

```{autodoc2-docstring} archivebox.cli.tests_piping.TestParserPluginWorkflows.test_rss_parser_workflow
```

````

````{py:method} test_multiple_parsers_dedupe()
:canonical: archivebox.cli.tests_piping.TestParserPluginWorkflows.test_multiple_parsers_dedupe

```{autodoc2-docstring} archivebox.cli.tests_piping.TestParserPluginWorkflows.test_multiple_parsers_dedupe
```

````

`````

`````{py:class} TestEdgeCases(methodName='runTest')
:canonical: archivebox.cli.tests_piping.TestEdgeCases

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.cli.tests_piping.TestEdgeCases
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.cli.tests_piping.TestEdgeCases.__init__
```

````{py:method} test_empty_input()
:canonical: archivebox.cli.tests_piping.TestEdgeCases.test_empty_input

```{autodoc2-docstring} archivebox.cli.tests_piping.TestEdgeCases.test_empty_input
```

````

````{py:method} test_malformed_jsonl()
:canonical: archivebox.cli.tests_piping.TestEdgeCases.test_malformed_jsonl

```{autodoc2-docstring} archivebox.cli.tests_piping.TestEdgeCases.test_malformed_jsonl
```

````

````{py:method} test_mixed_input_formats()
:canonical: archivebox.cli.tests_piping.TestEdgeCases.test_mixed_input_formats

```{autodoc2-docstring} archivebox.cli.tests_piping.TestEdgeCases.test_mixed_input_formats
```

````

````{py:method} test_crawl_with_multiple_urls()
:canonical: archivebox.cli.tests_piping.TestEdgeCases.test_crawl_with_multiple_urls

```{autodoc2-docstring} archivebox.cli.tests_piping.TestEdgeCases.test_crawl_with_multiple_urls
```

````

`````

`````{py:class} TestPassThroughBehavior(methodName='runTest')
:canonical: archivebox.cli.tests_piping.TestPassThroughBehavior

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.cli.tests_piping.TestPassThroughBehavior
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.cli.tests_piping.TestPassThroughBehavior.__init__
```

````{py:method} test_crawl_passes_through_other_types()
:canonical: archivebox.cli.tests_piping.TestPassThroughBehavior.test_crawl_passes_through_other_types

```{autodoc2-docstring} archivebox.cli.tests_piping.TestPassThroughBehavior.test_crawl_passes_through_other_types
```

````

````{py:method} test_snapshot_passes_through_crawl()
:canonical: archivebox.cli.tests_piping.TestPassThroughBehavior.test_snapshot_passes_through_crawl

```{autodoc2-docstring} archivebox.cli.tests_piping.TestPassThroughBehavior.test_snapshot_passes_through_crawl
```

````

````{py:method} test_archiveresult_passes_through_snapshot()
:canonical: archivebox.cli.tests_piping.TestPassThroughBehavior.test_archiveresult_passes_through_snapshot

```{autodoc2-docstring} archivebox.cli.tests_piping.TestPassThroughBehavior.test_archiveresult_passes_through_snapshot
```

````

````{py:method} test_run_passes_through_unknown_types()
:canonical: archivebox.cli.tests_piping.TestPassThroughBehavior.test_run_passes_through_unknown_types

```{autodoc2-docstring} archivebox.cli.tests_piping.TestPassThroughBehavior.test_run_passes_through_unknown_types
```

````

`````

`````{py:class} TestPipelineAccumulation(methodName='runTest')
:canonical: archivebox.cli.tests_piping.TestPipelineAccumulation

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.cli.tests_piping.TestPipelineAccumulation
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.cli.tests_piping.TestPipelineAccumulation.__init__
```

````{py:method} test_full_pipeline_output_types()
:canonical: archivebox.cli.tests_piping.TestPipelineAccumulation.test_full_pipeline_output_types

```{autodoc2-docstring} archivebox.cli.tests_piping.TestPipelineAccumulation.test_full_pipeline_output_types
```

````

````{py:method} test_pipeline_preserves_ids()
:canonical: archivebox.cli.tests_piping.TestPipelineAccumulation.test_pipeline_preserves_ids

```{autodoc2-docstring} archivebox.cli.tests_piping.TestPipelineAccumulation.test_pipeline_preserves_ids
```

````

````{py:method} test_jq_transform_pattern()
:canonical: archivebox.cli.tests_piping.TestPipelineAccumulation.test_jq_transform_pattern

```{autodoc2-docstring} archivebox.cli.tests_piping.TestPipelineAccumulation.test_jq_transform_pattern
```

````

`````
