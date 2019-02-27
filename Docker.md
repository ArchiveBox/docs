# Overview

Make sure you have Docker installed and set up on your machine before following these instructions.

If you don't already have Docker installed, follow the official install instructions for Linux, macOS, or Windows here: https://docs.docker.com/install/#supported-platforms.

- [Overview](#)
- [Docker Compose](#docker-compose)
  + [Setup](#setup)
  + [Usage](#usage)
  + [Accessing the data](#accessing-the-data)
  + [Configuration](#configuration)
- [Plain Docker](#docker)
  + [Setup](#setup-1)
  + [Usage](#usage-1)
  + [Accessing the data](#accessing-the-data-1)
  + [Configuration](#configuration-1)

# Docker Compose

An example [`docker-compose.yml`](https://github.com/pirate/ArchiveBox/blob/master/docker-compose.yml) config is included in the project root.  You can edit it as you see fit, or just run the default setup with ArchiveBox + Nginx as it comes out of the box.

## Setup

```bash
git clone https://github.com/pirate/ArchiveBox && cd ArchiveBox
mkdir data && chmod 777 data
docker-compose up -d
```

Then open [`http://127.0.0.1:8098`](http://127.0.0.1:8098) to view the archive (HTTP, not HTTPS).

## Usage

First make sure you're `cd`'ed into the same folder as your `docker-compose.yml` file (e.g. the project root) and that your containers have been started with `docker-compose up -d`.

To add new URLs, you can use docker-compose just like the normal `./archive` CLI.

To add an individual link or list of links, pass in URLs via stdin.
```bash
echo "https://example.com" | docker-compose exec -T archivebox /bin/archive
```

To pull in links from a feed or list of links, pass the URL or path to the feed as an argument.
```bash
docker-compose exec archivebox /bin/archive https://example.com/some/feed.rss
```
To import links from a file you can either `cat` the file and pass it via stdin like above, or move it into your data folder so that ArchiveBox can access it from within the container.
```bash
mv ~/Downloads/bookmarks.html data/sources/bookmarks.html
docker-compose exec archivebox /bin/archive /data/sources/bookmarks.html
```

## Accessing the data

The outputted archive data is stored in `data/` (relative to the project root), or whatever folder path you specified in `docker-compose.yml`.

To access your archive, you can open `data/index.html` directly, or you can use the provided nginx server running inside docker on [`http://127.0.0.1:8098`](http://127.0.0.1:8098).

## Configuration

There are a number of easy ways to pass in environment variables for configuring ArchiveBox.

You can edit the `environment:` section in `docker-compose.yml` directly or you can add a `env_file: ./path/to/ArchiveBox.conf` line before `environment:` to import variables from an env file.

You can also specify an env file via CLI when running compose using `docker-compose --env-file=/path/to/config.env ...` although you must specify the variables in the `environment:` section that you want to have passed down to the ArchiveBox container from the passed env file.

If you want to access your archive server with HTTPS, put a reverse proxy like Nginx or Caddy in front of `127.0.0.1:8098` to do SSL termination.

# Docker

Docker-compose is the recommended way to run ArchiveBox with docker, as it's a much easier CLI interface and more of the setup is taken care of by docker-compose using the single yaml config file as opposed to CLI flags.  The docker-compose setup also provides an nginx webserver to serve the archive right out of the box, whereas you have to set that up manually if you use plain docker.

If you want to continue and use raw docker (below) instead of docker-compose (above), follow these steps.

## Setup

1. Fetch and build the ArchiveBox Docker image.
```bash
docker build github.com/pirate/ArchiveBox -t archivebox
```

2. Create a volume to hold your ArchiveBox data (optional).
```bash
docker volume create archivebox-data
```
You can also mount a local directory in later steps instead of using a named Docker volume (see the [Accessing the data](#) section for details).

3. Run ArchiveBox with `docker run` to add links to your archive.  See the Usage section below for details depending on how you want to add links.

## Usage

To add a single URL to the archive or a list of links from a file, pipe them in via stdin.  This will archive each link passed in.
```bash
echo 'https://example.com' | docker run -i -v archivebox-data:/data archivebox /bin/archive
# or
cat bookmarks.html | docker run -i -v archivebox-data:/data archivebox /bin/archive
```

Add a list of pages via feed URL or path. Passing a URL as an argument here does not archive the specified URL, it downloads it and archives the links *inside* of it, so only use it for RSS feeds or other *lists of links* you want to add.  To add an individual link use the instruction above and pass via stdin instead of by argument.
```bash
docker run -v archivebox-data:/data archivebox /bin/archive 'https://example.com/some/rss/feed.xml'
```

## Accessing the data
If you used the named docker volume `archivebox-data` as shown in the examples above, you can access the data here:  
`/var/lib/docker/volumes/archivebox-data/_data`

If you want to use a local folder for data instead of using a named docker volume, replace the `-v archivebox-data:/data` flag in the commands above with `--mount type=bind,source=/your/data/folder/on/host,target=/data`.

## Configuration
To pass configuration parameters, you can use the env command.
```bash
echo 'https://example.com' | docker run -i -v archivebox-data:/data archivebox env FETCH_SCREENSHOT=False /bin/archive
```

Or you can create an `ArchiveBox.env` file (copy from the default `etc/ArchiveBox.conf.default`) and pass it in like so:
```bash
docker run -i -v --env-file=ArchiveBox.env archivebox /bin/archive ...
```