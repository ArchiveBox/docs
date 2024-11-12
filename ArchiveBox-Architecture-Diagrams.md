# ArchiveBox Architecture Diagrams

## High-Level System Execution Flow

```mermaid
stateDiagram-v2
    archivebox.cli.main(sys.argv)
    state Supervisord {
        Scheduler
        state Orchestrator {
            [*] --> TICK
            TICK --> SPAWN_ACTORS: queued > 0
            SPAWN_ACTORS --> TICK
            TICK --> IDLE: queued == 0
            IDLE --> TICK: 1s
        }
    }

    note left of archivebox.cli.main(sys.argv)
        archivebox entrypoint
    end note

    state "archivebox.cli.SUBCOMMAND" as MAIN_THREAD

    archivebox.cli.main(sys.argv) --> run_subcommand(sys.argv)
    run_subcommand(sys.argv) --> setup_django()
    setup_django() --> Supervisord: spawns in background
    setup_django() --> MAIN_THREAD: runs in foreground   

    MAIN_THREAD --> archivebox.main.SUBCOMMAND
    archivebox.main.SUBCOMMAND --> Storage: add_to_queue()

    state Actors {
        CrawlActor --> Crawl: tick()
        SnapshotActor --> Snapshot: tick()
        ArchiveResultActors --> ArchiveResult: tick()
    }

    state "State Machines" as JOBS {

        state Crawl {
            state "QUEUED" as CRAWL_QUEUED
            state "STARTED" as CRAWL_STARTED
            state "SEALED" as CRAWL_SEALED
            CRAWL_QUEUED --> CRAWL_STARTED: create_root_snapshot()
            CRAWL_STARTED --> CRAWL_SEALED: is_finished
        }

        state Snapshot {
            state "QUEUED" as SNAP_QUEUED
            state "STARTED" as SNAP_STARTED
            state "SEALED" as SNAP_SEALED
            SNAP_QUEUED --> SNAP_STARTED: create_pending_archiveresults()
            SNAP_STARTED --> SNAP_SEALED: is_finished
        }

        state ArchiveResult {
            QUEUED --> STARTED: run_extractor()
            STARTED --> BACKOFF: is_temp_error
            BACKOFF --> STARTED: is_retry_past
            STARTED --> FAILED: is_fatal_error
            STARTED --> SUCCEEDED: is_succeded
        }
        
        
        note right of ArchiveResult
            exec_crome()
        end note
        
        note right of ArchiveResult
            exec_wget()
        end note
        
        note right of ArchiveResult
            exec_curl()
        end note
        
        note right of ArchiveResult
            ... other extractor subprocesses ...
        end note
    }
    
    state Storage {
        state "DB" as SQLITE_DB
        sources/
        archive/
        state "index.json" as INDEX_JSONS
    }

    Storage: Storage

    Orchestrator --> Actors: spawns subprocesses
    
    Crawl --> Snapshot: create_root_snapshot()
    Snapshot --> ArchiveResult: create_pending_archiveresults()
    
    Crawl --> Storage: .save()
    Snapshot --> Storage: .save()
    ArchiveResult --> Storage: .save()
    
    Storage --> Actors: get_queue()


```

---

## State Diagrams for Main Models


### `Crawl`

- `crawls/models.py`: `Crawl`
- `crawls/statemachines.py`: `CrawlMachine`

```mermaid
stateDiagram-v2
    STARTED --> SEALED: tick [is_finished]
    STARTED --> STARTED: tick [!is_finished]    
    QUEUED --> STARTED: tick [can_start]
    QUEUED --> QUEUED: tick [!can_start]

    
    note left of QUEUED
        Crawl created
    end note
    
    note right of STARTED
        create_root_snapshot()
        crawl.retry_at = now + 5s
    end note
```


## `Snapshot`

- `core/models.py`: `Snapshot`
- `core/statemachines.py`: `SnapshotMachine`

```mermaid
stateDiagram-v2
    STARTED --> SEALED: tick [is_finished]
    STARTED --> STARTED: tick [!is_finished]
    QUEUED --> STARTED: tick [can_start]
    QUEUED --> QUEUED: tick [!can_start]
    
    note left of QUEUED
        Snapshot created
    end note
    
    note right of STARTED
        create_pending_archiveresults(extractors)
        snapshot.retry_at = now + 60s
    end note
```


### `ArchiveResult`

- `core/models.py`: `ArchiveResult`
- `core/statemachines.py`: `ArchiveResultMachine`

```mermaid
stateDiagram-v2
    QUEUED --> QUEUED: tick [!can_start]
    QUEUED --> STARTED: tick [can_start]
    STARTED --> STARTED: tick [!is_finished]
    STARTED --> BACKOFF: tick [is_backoff]
    STARTED --> FAILED: tick [is_failed]
    STARTED --> SUCCEEDED: tick [is_succeeded]
    BACKOFF --> BACKOFF: tick [!can_start]
    BACKOFF --> STARTED: tick [can_start]
    
    note left of QUEUED
        ArchiveResult created
    end note
    
    note left of STARTED
        start_ts = now
        retry_at = now + 60s
        create_output_dir()
        run_extractor()
    end note
    
    note right of BACKOFF
        retry_at = now + 60s
    end note
    
    note right of SUCCEEDED
        end_ts = now
        retry_at = None
    end note
    
    note right of FAILED
        end_ts = now
        retry_at = None
    end note
```

