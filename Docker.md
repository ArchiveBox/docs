# Docker

## Overview

Running ArchiveBox with Docker allows you to manage it in a container without exposing it to the rest of your system. ArchiveBox generally works the same in Docker as it does outside Docker. You can even use `pip`-installed ArchiveBox and Docker ArchiveBox in tandem, as they both share the same data directory format.

<img src="https://imgur.zervice.io/qFAPRwC.png" width="20%" align="right"/>

- [Overview](#Overview)
- [Docker Compose](#docker-compose) ⭐️ (recommended)
  - [Setup](#setup)
  - [Upgrading](https://github.com/ArchiveBox/ArchiveBox/wiki/Upgrading-or-Merging-Archives#upgrading-with-docker-compose-%EF%B8%8F)
  - [Usage](#usage)
  - [Accessing the data](#accessing-the-data)
  - [Configuration](#configuration)
- [Plain Docker](#docker)
  - [Setup](#setup-1)
  - [Upgrading](https://github.com/ArchiveBox/ArchiveBox/wiki/Upgrading-or-Merging-Archives#upgrading-with-plain-docker)
  - [Usage](#usage-1)
  - [Accessing the data](#accessing-the-data-1)
  - [Configuration](#configuration-1)

<br/>

**Official Docker Hub image: [`hub.docker.com/r/archivebox/archivebox`](https://hub.docker.com/r/archivebox/archivebox)**
```bash
docker pull archivebox/archivebox:latest
```

- [`Dockerfile`](https://github.com/ArchiveBox/ArchiveBox/blob/dev/Dockerfile)
- [`docker-compose.yml`](https://github.com/ArchiveBox/ArchiveBox/blob/dev/docker-compose.yml)
- [`archivebox-kubernetes.yml`](https://github.com/ArchiveBox/docker-archivebox/blob/master/archivebox.yml)

Published [Docker tags](https://hub.docker.com/r/archivebox/archivebox/tags):
- `:latest`, `:stable` (latest stable release, the default)
- `:x.x` and `:x.x.x` for specific versions (e.g. `:0.7` or `:0.7.2`)
- `:dev` for unstable alpha builds (breaks often, only for developers and willing beta testers)
- `:sha-xxxxxxx` for builds of specific git commits (to test or pin specific PRs or commits)

<br/>

> [!IMPORTANT]
> *Make sure Docker is **[installed](https://docs.docker.com/install/#supported-platforms)** and up-to-date before following any instructions below!*  ➡️  
> To check installed version, run: `docker --version` (must be `>=17.04.0`)

<br/>

<img src="https://github.com/ArchiveBox/ArchiveBox/assets/511499/9e8658f7-7d00-452e-a10e-f7d22ef9365a" height="40px" align="right"/>

## Docker Compose

<br/>

### Setup

A full [`docker-compose.yml`](https://github.com/ArchiveBox/ArchiveBox/blob/dev/docker-compose.yml) file is provided with all the extras included.  
You can uncomment sections within it to enable extra features, or run the basic version as-is.


```bash
# create a folder to store your data (can be anywhere)
mkdir -p ~/archivebox/data && cd ~/archivebox

# download the compose file into the directory
curl -fsSL 'https://docker-compose.archivebox.io' > docker-compose.yml
# (shortcut for getting https://raw.githubusercontent.com/ArchiveBox/ArchiveBox/stable/docker-compose.yml)

# initialize your collection and create an admin user for the Web UI (or set ADMIN_USERNAME/ADMIN_PASSWORD env vars)
docker compose run archivebox init
docker compose run archivebox manage createsuperuser
```

To use [Sonic](https://github.com/valeriansaliou/sonic) for improved full-text search, download this config & uncomment the sonic service in `docker-compose.yml`:
```bash
# download the sonic config file into your data folder (e.g. ~/archivebox)
curl -fsSL 'https://raw.githubusercontent.com/ArchiveBox/ArchiveBox/dev/etc/sonic.cfg' > sonic.cfg

# then uncomment the sonic-related sections in docker-compose.yml
nano docker-compose.yml

# to backfill any existing archive data into the search index, run:
docker compose run archivebox update --index-only
```

<br/>

### Upgrading

See the wiki page on [Upgrading or Merging Archives: Upgrading with Docker Compose](https://github.com/ArchiveBox/ArchiveBox/wiki/Upgrading-or-Merging-Archives#upgrading-with-docker-compose-%EF%B8%8F) for instructions. ➡️

<br/>

### Usage

You can use `docker compose run archivebox [subcommand]` just like the non-Docker `archivebox [subcommand]` CLI.

First, make sure you're `cd`'ed into the same folder as your `docker-compose.yml` file (e.g. `~/archivebox`):
```bash
docker compose run archivebox help
```

To add an individual URL, pass it in as an arg or via stdin:
```bash
docker compose run archivebox add 'https://example.com'
# OR
echo 'https://example.com' | docker compose run -T archivebox add
```

To add multiple URLs at once, pipe them in via stdin, or place them in a file inside `./data/sources` so that ArchiveBox can access it from within the container:
```bash
# pipe URLs in from a file outside Docker
docker compose run -T archivebox add < ~/Downloads/example_urls.txt

# OR ingest URLs from a file mounted inside Docker
docker compose run archivebox add --depth=1 /data/sources/example_urls.txt

# OR pipe in URLs from a remote source
curl 'https://example.com/some/rss/feed.xml' | docker compose run archivebox add
docker compose run archivebox add --depth=1 'https://example.com/some/rss/feed.xml'
```

The `--depth=1` flag tells ArchiveBox to look inside the provided source and archive all the URLs within:
```bash
# this archives just the RSS file itself (probably not what you want)
docker compose run archivebox add 'https://example.com/some/feed.rss'

# this archives the RSS feed file + all the URLs mentioned inside of it
docker compose run archivebox add --depth=1 'https://example.com/some/feed.rss'
```

<br/>

### Accessing the data

The outputted archive data is stored in `data/` (relative to the project root), or whatever folder path you specified in the `docker-compose.yml` `volumes:` section. Make sure the `data/` folder on the host has permissions initially set to `777` so that the ArchiveBox command is able to set it to the specified `OUTPUT_PERMISSIONS` config setting on the first run.

To access the results directly via the filesystem, open `./data/archive/<timestamp>/index.html` (timestamp is shown in output of previous command).

Alternatively, to use the web UI, start the server with:
```bash
docker compose up         # add -d to run in the background
```

Then open [`http://127.0.0.1:8000`](http://127.0.0.1:8000).

<br/>

### Configuration

ArchiveBox running with `docker compose` accepts all the same config options as other ArchiveBox distributions, see the full list of options available on the [[Configuration]] page.

The recommended way configure ArchiveBox in Docker Compose is using `archivebox config --set ...` or by editing `ArchiveBox.conf`.
```bash
docker compose run archivebox config --set MEDIA_MAX_SIZE=750mb
# OR
echo 'MAX_MEDIA_SIZE=750mb' >> ./data/ArchiveBox.conf
```
This will apply the config to all containers or archivebox instances that access the collection.

If you're only running one container, or if you want to scope config options to only apply to a particular container, you can set them in that container's `environment:` section:

```yaml
...

services:
    archivebox:
        ...
        environment:
            - USE_COLOR=False
            - SHOW_PROGRESS=False
            - CHECK_SSL_VALIDITY=False
            - RESOLUTION=1900,1820
            - MEDIA_TIMEOUT=512000
        ...
```

You can also specify an env file via CLI when running compose using `docker compose --env-file=/path/to/config.env ...` although you must specify the variables in the `environment:` section that you want to have passed down to the ArchiveBox container from the passed env file.

If you want to access your archive server with HTTPS, put a reverse proxy like Nginx or Caddy in front of `http://127.0.0.1:8000` to do SSL termination. Here is an example [ArchiveBox nginx container](https://github.com/ArchiveBox/ArchiveBox/blob/dev/docker-compose.yml#:~:text=nginx) + [`nginx.conf`](https://github.com/ArchiveBox/ArchiveBox/blob/dev/etc/nginx.conf) that you can modify to add your preferred TLS settings.

<br/>

---

<br/>

## Docker

<br/>

### Setup

Fetch and run the ArchiveBox Docker image to create your initial archive.

```bash
docker pull archivebox/archivebox

mkdkir -p ~/archivebox/data && cd ~/archivebox/data
docker run -it -v $PWD:/data archivebox/archivebox init --setup
```

*(You can create a collection in any directory you want, `~/archivebox/data` is just used as an example here)*

If you encounter permissions issues, you may need configure user/group ownership explicitly with [`PUID`/`PGID`](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#puid--pgid).

<br/>

### Upgrading

See the wiki page on [Upgrading or Merging Archives: Upgrading with plain Docker](https://github.com/ArchiveBox/ArchiveBox/wiki/Upgrading-or-Merging-Archives#upgrading-with-plain-docker) for instructions. ➡️

<br/>

### Usage

The Docker CLI `docker run ... archivebox/archivebox [subcommand]` works just like the non-Docker `archivebox [subcommand]` CLI.

First, make sure you're `cd`'ed into your collection data folder (e.g. `~/archivebox/data`).

```bash
docker run -it -v $PWD:/data archivebox/archivebox help
```

To add a single URL, pass it as an arg or pipe it in via stdin:
```bash
docker run -it -v $PWD:/data archivebox/archivebox add 'https://example.com'
# OR
echo 'https://example.com' | docker run -i -v $PWD:/data archivebox/archivebox add
```

To archive multiple URLs at once, pass text containing URLs in via stdin:
```bash
docker run -i -v $PWD:/data archivebox/archivebox add < urls.txt
# OR
curl 'https://example.com/some/rss/feed.xml' | docker run -i -v $PWD:/data archivebox/archivebox add
```

You can also use the `--depth=1` flag to tell ArchiveBox to recursively archive the URLs within a provided source.
```bash
docker run -it -v $PWD:/data archivebox/archivebox add --depth=1 'https://example.com/some/rss/feed.xml'
```

<br/>

### Accessing the data

The `docker run` `-v /path/on/host:/path/inside/container` flag specifies where your data dir lives on the host.

For example to use a folder on an external USB drive (instead of the current directory `$PWD` or `~/archivebox/data`):
```bash
docker run -it -v /media/USB-DRIVE/archivebox/data:/data archivebox/archivebox ...
```

Then to view your data, you can look in the folder on the host `/media/USB-DRIVE/archivebox/data`, or use the Web UI:
```bash
docker run -it -v /media/USB_DRIVE/archivebox/data:/data -p 8000:8000 archivebox/archivebox
# then open https://127.0.0.1:8000
```

<br/>

### Configuration

The easiest way is to use `archivebox config --set KEY=value` or edit `./ArchiveBox.conf` (in your collection dir).

For example, this sets `MEDIA_TIMEOUT=120` as a persistent setting for the collection:
```bash
docker run -it -v $PWD:/data archivebox/archivebox config --set MEDIA_TIMEOUT=120
# OR
echo 'MEDIA_TIMEOUT=120' >> ./ArchiveBox.conf
```

ArchiveBox in Docker also accepts config as environment variables, see more on the [[Configuration]] page.

For example, this applies `FETCH_SCREENSHOT=False` to a single run (without persisting for other runs):
```bash
docker run -it -v $PWD:/data -e FETCH_SCREENSHOT=False archivebox/archivebox add 'https://example.com'
# OR
echo 'FETCH_SCREENSHOT=False' >> ./.env
docker run ... --env-file=./.env archivebox/archivebox ...
```
