# Docker

## Overview

Running ArchiveBox with Docker allows you to manage it in a container without exposing it to the rest of your system. Usage with Docker is similar to usage of ArchiveBox normally, with a few small differences.

Make sure you have Docker installed and set up on your machine before following these instructions. If you don't already have Docker installed, follow the official install instructions for Linux, macOS, or Windows here: https://docs.docker.com/install/#supported-platforms.

<img src="https://i.imgur.com/qFAPRwC.png" width="20%" align="right">

- [Overview](#)
- [Docker Compose](#docker-compose) (recommended way)
  - [Setup](#setup)
  - [Usage](#usage)
  - [Accessing the data](#accessing-the-data)
  - [Configuration](#configuration)
- [Plain Docker](#docker)
  - [Setup](#setup-1)
  - [Usage](#usage-1)
  - [Accessing the data](#accessing-the-data-1)
  - [Configuration](#configuration-1)

**Official Docker Hub image:**  
https://hub.docker.com/r/nikisweeting/archivebox

**Usage:**
```bash
docker run -v $PWD:/data nikisweeting/archivebox init
docker run -v $PWD:/data nikisweeting/archivebox add 'https://example.com'
docker run -v $PWD:/data -it nikisweeting/archivebox manage createsuperuser
docker run -v $PWD:/data -p 8000:8000 nikisweeting/archivebox server 0.0.0.0:8000
```

---

<img src="https://i.imgur.com/knwOtky.png" height="40px" align="right">

## Docker Compose

An example [`docker-compose.yml`](https://github.com/pirate/ArchiveBox/blob/master/docker-compose.yml) config with ArchiveBox and an Nginx server to serve the archive is included in the project root. You can edit it as you see fit, or just run it as it comes out-of-the-box.

Just make sure you have a Docker version that's [new enough](https://docs.docker.com/compose/compose-file/) to support `version: 3` format:

```bash
docker --version
Docker version 18.09.1, build 4c52b90    # must be >= 17.04.0
```

### Setup

```bash
git clone https://github.com/pirate/ArchiveBox && cd ArchiveBox
mkdir data && chmod 777 data
docker-compose up -d
docker-compose run archivebox init
```

### Usage

First, make sure you're `cd`'ed into the same folder as your `docker-compose.yml` file (e.g. the project root) and that your containers have been started with `docker-compose up -d`.

Then open [`http://127.0.0.1:8000`](http://127.0.0.1:8000) or `data/index.html` to view the archive (HTTP, not HTTPS).

To add new URLs, you can use docker-compose just like the normal `./archive` CLI.

**To add an individual link or list of links**, pass in URLs via stdin.

```bash
echo "https://example.com" | docker-compose run -T archivebox add
```

**To import links from a file** you can either `cat` the file and pass it via stdin like above, or move it into your data folder so that ArchiveBox can access it from within the container.

```bash
mv ~/Downloads/bookmarks.html data/sources/bookmarks.html
docker-compose run archivebox add /data/sources/bookmarks.html
docker-compose run archivebox add < data/sources/bookmarks.html
```

**To pull in links from a feed or remote file**, pass the URL or path to the feed as an argument.

```bash
docker-compose run archivebox add --depth=1 https://example.com/some/feed.rss
```

The `depth` argument controls if you want to save the links contained in that URL, or only the specified URL.

### Accessing the data

The outputted archive data is stored in `data/` (relative to the project root), or whatever folder path you specified in the `docker-compose.yml` `volumes:` section. Make sure the `data/` folder on the host has permissions initially set to `777` so that the ArchiveBox command is able to set it to the specified `OUTPUT_PERMISSIONS` config setting on the first run.

To access your archive, you can open `data/index.html` directly, or you can use the provided Django development server running inside docker on [`http://127.0.0.1:8000`](http://127.0.0.1:8000).

### Configuration

ArchiveBox running with docker-compose accepts all the same environment variables as normal, see the full list on the [[Configuration]] page.

The recommended way to pass in config variables is to edit the `environment:` section in `docker-compose.yml` directly or add an `env_file: ./path/to/ArchiveBox.conf` line before `environment:` to import variables from an env file.

Example of adding config options to `docker-compose.yml`:

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

You can also specify an env file via CLI when running compose using `docker-compose --env-file=/path/to/config.env ...` although you must specify the variables in the `environment:` section that you want to have passed down to the ArchiveBox container from the passed env file.

If you want to access your archive server with HTTPS, put a reverse proxy like Nginx or Caddy in front of `http://127.0.0.1:8098` to do SSL termination. You can find many instructions to do this online if you search "SSL reverse proxy".

---

## Docker

### Setup

Fetch and run the ArchiveBox Docker image to create your initial archive.

```bash
echo 'https://example.com' | docker run -i -v ~/ArchiveBox:/data nikisweeting/archivebox
```

Replace `~/ArchiveBox` in the command above with the full path to a folder to use to store your archive on the host, or name of a Docker data volume.

Make sure the data folder you use host is either a new, uncreated path, or if it already exists make sure it has permissions initially set to `777` so that the ArchiveBox command is able to set it to the specified `OUTPUT_PERMISSIONS` config setting on the first run.

### Usage

**To add a single URL to the archive** or a list of links from a file, pipe them in via stdin. This will archive each link passed in.

```bash
echo 'https://example.com' | docker run -i -v ~/ArchiveBox:/data nikisweeting/archivebox add
# or
cat bookmarks.html | docker run -i -v ~/ArchiveBox:/data nikisweeting/archivebox add
```

**To add a list of pages via feed URL or remote file,** pass the URL of the feed as an argument.

```bash
docker run -v ~/ArchiveBox:/data nikisweeting/archivebox add 'https://example.com/some/rss/feed.xml'
```

The `depth` argument controls if you want to save the links contained in that URL, or only the specified URL.

### Accessing the data

#### Using a bind folder

Use the flag:

```bash
-v /full/path/to/folder/on/host:/data
```

This will use the folder `/full/path/to/folder/on/host` on your host to store the ArchiveBox output.

#### Using a named Docker data volume

```bash
docker volume create archivebox-data
```

Then use the flag:

```bash
-v archivebox-data:/data
```

You can mount your data volume using standard docker tools, or access the contents directly here:  
`/var/lib/docker/volumes/archivebox-data/_data` (on most Linux systems)

On a Mac you'll have to enter the base Docker Linux VM first to access the volume data:

```bash
screen ~/Library/Containers/com.docker.docker/Data/vms/0/tty
cd /var/lib/docker/volumes/archivebox-data/_data
```

### Configuration

ArchiveBox in Docker accepts all the same environment variables as normal, see the list on the [[Configuration]] page.

To pass environment variables when running, you can use the `env` command or `-e`.

```bash
echo 'https://example.com' | docker run -it -v $PWD:/data -e FETCH_SCREENSHOT=False nikisweeting/archivebox add
```

Or you can create an `ArchiveBox.env` file (copy from the default `etc/ArchiveBox.conf.default`) and pass it in like so:

```bash
docker run -i -v --env-file=ArchiveBox.env nikisweeting/archivebox
```
