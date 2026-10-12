# Merging Collections

Import completed snapshots by copying their archive files into the destination collection and rescanning. Recorded snapshot UUIDs and dates are preserved; the source database is not needed.

Use a current ArchiveBox version and back up both collections before starting. Run these commands with the collections stopped:

```bash
mkdir -p /path/to/destination/data
cd /path/to/destination/data
archivebox init

rsync -a --ignore-existing /path/to/source/data/archive/ ./archive/
archivebox update --rescan --migrate-only
archivebox status
```

Keep each snapshot's saved files and `index.jsonl` (or legacy `index.json`) together at their original relative path under `archive/`. This works with both `archive/users/<user>/snapshots/<date>/<domain>/<uuid>/` and legacy `archive/<timestamp>/` directories.

Open the destination's web UI to browse the imported snapshots. To make their saved content searchable, run:

```bash
archivebox update --index-only
```

For multiple source collections, repeat the copy and rescan steps, keeping distinct captures in separate snapshot directories. You can also import into an existing destination. Rerunning the rescan reuses snapshots already imported.

For Docker Compose, replace `archivebox` with `docker compose run --rm archivebox` and copy the files into the destination's mounted data directory.
