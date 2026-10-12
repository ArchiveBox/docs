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

After you've confirmed your Snapshots are present in the new index, the old `index.sqlite3`, `index.json`, `index.html`, etc. main index files from the old archives can be safely deleted. You can optionally merge the contents of `ArchiveBox.conf` (your ArchiveBox config options), `sources/` (copies of all URLs imported in their original format), `logs/` (ArchiveBox error logs and debug info), and other root-level items yourself if that data is important to you.

For more information about why Snapshot index files are usually updated lazily, see: https://github.com/ArchiveBox/ArchiveBox/issues/962

---

## Modify the ArchiveBox SQLite3 DB directly

If you need to automate changes to the ArchiveBox DB (for example adding a User from an Ansible script), you can modify the SQLite3 DB directly.

Note, this is often unnecessary for modifying ArchiveBox on a host that doesn't have the CLI installed, as you can also copy the `index.sqlite3` to a local machine that has it, do the modifications locally, then copy the modified db back into place on the host. (Docker/CLI/GUI/Web ArchiveBox all share the same DB schema/format)

```bash
cd ~/archivebox/data    # cd into your archivebox collection dir
sqlite3 index.sqlite3   # open the db with sqlite3 shell
```

#### Example: Modifying an existing user's email

```sql
UPDATE auth_user
SET email = 'someNewEmail@example.com', is_superuser = 1
WHERE username = 'someUsernameHere';
```

#### Example: Adding a new user with a hashed password

*Note: this is just an example to demonstrate direct database usage. For initial setup, open the Admin UI and create the first admin there.*

1. First, generate the hashed password in a Python shell using Django's `make_password` function.

Use the Django version bundled with the ArchiveBox installation that owns the collection:
  ```bash
  archivebox shell -c "from django.contrib.auth.hashers import make_password; print(make_password('somePasswordHere', 'someSaltHere', 'pbkdf2_sha256'))"
  ```
```python3
>>> from django.contrib.auth.hashers import make_password
>>> make_password('somePasswordHere', 'someSaltHere', 'pbkdf2_sha256')         # choose a password and a salt (can be anything 12 chars long)
'pbkdf2_sha256$...$someSaltHere$...'
```
2. Use the generated hashed password to insert a new User row in the SQLite3 database directly:
  ```bash
cd ~/archivebox/data    # cd into your archivebox collection dir
sqlite3 index.sqlite3   # open the db with sqlite3 shell
```
```sql
INSERT INTO "auth_user" ("password", "last_login", "is_superuser", "username", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined")
VALUES ('GENERATED_PASSWORD_HASH', NULL, 0, 'someUsername', '', '', 'someEmail@example.com', 0, 1, '2022-03-22 23:34:02.333042')
```
  Replace the values above with the desired username, email, and password hash from python output^.

3. Log in using the new generated user to confirm it works
    http://admin.archivebox.localhost:5797/admin/login/ user: `someUsername` pass:`somePasswordHere`

More info:
- https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#python-shell-usage
- https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#sql-shell-usage

---

## Database Troubleshooting

See here [Troubleshooting: Database](https://github.com/ArchiveBox/ArchiveBox/wiki/Troubleshooting#database)...

---

## Related Documents

- https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#disk-layout
- https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#large-archives
- https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview#output-folder
- https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#python-shell-usage
- https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#sql-shell-usage
