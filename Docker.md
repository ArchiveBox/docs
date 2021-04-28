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
https://hub.docker.com/r/archivebox/archivebox

**Usage:**
```bash
docker run -v $PWD:/data -it archivebox/archivebox init --setup
docker run -v $PWD:/data -it archivebox/archivebox add 'https://example.com'
docker run -v $PWD:/data -p 8000:8000 archivebox/archivebox server 0.0.0.0:8000
```

---

<img src="https://i.imgur.com/knwOtky.png" height="40px" align="right">

## Docker Compose

An example [`docker-compose.yml`](https://github.com/ArchiveBox/ArchiveBox/blob/master/docker-compose.yml) config with ArchiveBox and an Nginx server to serve the archive is included in the project root. You can edit it as you see fit, or just run it as it comes out-of-the-box.

Just make sure you have a Docker version that's [new enough](https://docs.docker.com/compose/compose-file/) to support `version: 3` format:

```bash
docker --version
Docker version 18.09.1, build 4c52b90    # must be >= 17.04.0
```

### Setup

```bash
mkdir archivebox && cd archivebox
curl -O https://raw.githubusercontent.com/ArchiveBox/ArchiveBox/master/docker-compose.yml
docker-compose run archivebox init --setup
docker-compose run archivebox add 'https://example.com'
docker-compose up
```

If you want to use sonic for full text search, download the sonic config file uncomment the sonic service in your `docker-compose.yml` file:
```bash
curl https://raw.githubusercontent.com/ArchiveBox/ArchiveBox/master/etc/config.cfg > sonic.cfg
# then uncomment the sonic block in docker-compose.yml

# to backfill previously added snapshots into the full text index, run:
docker-compose run archivebox update --index-only
```

### Usage

First, make sure you're `cd`'ed into the same folder as your `docker-compose.yml` file (e.g. the project root) and that your containers have been started with `docker-compose up -d`.

Then open [`http://127.0.0.1:8000`](http://127.0.0.1:8000) or browse `./data/archive` in the filesystem to view the archive.

To add new URLs, you can use docker-compose just like the normal `archivebox <subcommand> [args]` CLI.

**To add an individual link or list of links**, pass in URLs via stdin.

```bash
echo "https://example.com" | docker-compose run archivebox add
```

**To import links from a file** you can either `cat` the file and pass it via stdin like above, or move it into your data folder so that ArchiveBox can access it from within the container.

```bash
docker-compose run archivebox add 'https://exmaple.com/some/url/here'
docker-compose run archivebox add < ~/Downloads/bookmarks.html
curl https://example.com/some/rss/feed.xml | docker-compose run archivebox add
```

**To ingest a feed or remote file and archive all the URLs within**, pass the URL or path to the feed or page as an argument using depth=1.

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
echo 'https://example.com' | docker run -it -v $PWD:/data archivebox/archivebox add
```

Replace `~/ArchiveBox` in the command above with the full path to a folder to use to store your archive on the host, or name of a Docker data volume.

Make sure the data folder you use host is either a new, uncreated path, or if it already exists make sure it has permissions initially set to `777` so that the ArchiveBox command is able to set it to the specified `OUTPUT_PERMISSIONS` config setting on the first run.

### Usage

**To add a single URL to the archive** or a list of links from a file, pipe them in via stdin. This will archive each link passed in.

```bash
echo 'https://example.com' | docker run -it -v $PWD:/data archivebox/archivebox add
# or
docker run -it -v $PWD:/data archivebox/archivebox add < bookmarks.html
```

**To add a list of pages via feed URL or remote file,** pass the URL of the feed as an argument.

```bash
docker run -it -v $PWD:/data archivebox/archivebox add --depth=1 'https://example.com/some/rss/feed.xml'
```

The `depth` argument controls if you want to save the links contained in that URL, or only the specified URL.

### Accessing the data

#### Using a bind folder

Use the flag:

```bash
-v /full/path/to/folder/on/host:/data
```

This will use the folder `/full/path/to/folder/on/host` on your host to store the ArchiveBox output.

### Configuration

The easiest way is to use the a `.env` file or add your config to your `docker-compose.yml` `environment:` section.

The next easiest way to get/set config is using the archivebox CLI:
```bash
docker-compose run archivebox config --get RESOLUTION
docker-compose run archivebox config --set RESOLUTION=1440,900
# or
docker run -it -v $PWD:/data archivebox/archivebox config --set MEDIA_TIMEOUT=120
```

ArchiveBox in Docker accepts all the same environment variables as normal, see the list on the [[Configuration]] page.

To set environment variables for a single run, you can use the `env KEY=VAL ...` command, `-e KEY=VAL`, or `--env-file=somefile.env`.

```bash
echo 'https://example.com' | docker run -it -v $PWD:/data -e FETCH_SCREENSHOT=False archivebox/archivebox add
```
```bash
docker run -i -v --env-file=ArchiveBox.env archivebox/archivebox
```

You can also edit the `data/ArchiveBox.conf` file directly and the changes will take effect on the next run.
