## Upgrade your ArchiveBox collection to a new version

### With Docker Compose

```bash
cd ~/archivebox        # or wherever your data folder is
docker-compose down    # stop the currently running archivebox containers
docker-compose down    # run twice to clear stopped containers
docker-compose pull    # pull the latest image version from Docker Hub
docker-compose up      # collection will be automatically upgraded as it starts
```

### With plain Docker

```bash
docker ps -a -q  --filter ancestor=archivebox/archivebox  # find any currently running archivebox containers
docker kill <image>    # stop any currently running archivebox versions

docker pull archivebox/archivebox
docker run -v $PWD:/data -it archivebox/archivebox init --setup  # upgrade the collection to the latest version
# restart archivebox server container if needed
docker run -v $PWD:/data -it -p 8000:8000 archivebox/archivebox server
```

### With a package manager

```bash
cd ~/archivebox        # or wherever your data folder is
killall archivebox     # stop the currently running archivebox version

# upgrade ArchiveBox using the package manager you originally used to install it
pip install --upgrade archivebox
# or
brew upgrade archivebox
# or
apt install --upgrade archivebox
# or
curl -sSL 'https://get.archivebox.io' | sh

archivebox init        # run init to upgrade the collection to the latest version
```
*More detailed instructions here: https://github.com/ArchiveBox/ArchiveBox#-package-manager-setup*

---

## Merge two or more existing archives

1. Upgrade both old collections to the most recent ArchiveBox version (following instructions above)
  `pip install --upgrade archivebox # or docker pull if using docker; archivebox init`
2. Create a new empty archivebox collection in a new folder somewhere
  `mkdir ~/archivebox_new; cd ~/archivebox_new; archivebox init --setup` 
3. Drag everything under `archive/*` in each old collections into the new empty collection's `~/archiebox_new/archive/` folder
4. Run `archivebox init` in the new collection to regenerate the new index
5. The new collection should now contain all the entries from the old collections combined

---

## Modify the ArchiveBox SQLite3 DB directly

If you need to automate changes to the ArchiveBox DB (for example adding a User from an Ansible script), you can modify the SQLite3 DB directly.

**As an example, here's how to add a user row manually:**

1. First, generate the hashed password in a Python shell using Django's `make_password` function.

This can be done on any machine with Python 3+, it doesn't have to have ArchiveBox installed.
  ```bash
pip3 install django==3.1.3   # install the django version used by ArchiveBox
python3                      # open any python shell with django available, doesn't have to be the archivebox shell
```
```python3
>>> from django.contrib.auth.hashers import make_password
>>> make_password('somePasswordHere', 'someSaltHere', 'pbkdf2_sha256')         # choose a password and a salt (can be anything 12 chars long)
'pbkdf2_sha256$216000$someSaltHere$styW1Uoy8SHp3zbSwGRp20C9mPjOHVjP9rl5a8/UOVE='
```
2. Use the generated hashed password to insert a new User row in the SQLite3 database directly:
  ```bash
cd ~/archivebox         # cd into your archivebox collection dir
sqlite3 index.sqlite3   # open the db with sqlite3 shell
```
```sql
INSERT INTO "auth_user" ("password", "last_login", "is_superuser", "username", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined")
VALUES ('pbkdf2_sha256$216000$someSaltHere$+2beZufc3JUXnmn0tG+2peJEBh7MjxPYmT3YfIFzEl0=', NULL, 0, 'someUsername', '', '', 'someEmail@example.com', 0, 1, '2022-03-22 23:34:02.333042')
```
  Replace the values above with the desired username, email, and password hash from python output^.

3. Log in using the new generated user to confirm it works
    https://localhost:8000/admin/login/ user: `someUsername` pass:`somePasswordHere`