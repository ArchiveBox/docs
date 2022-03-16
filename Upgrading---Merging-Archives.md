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