Make sure you have Docker installed and set up:

If you don't already have docker installed, follow the official install instructions for Linux, macOS, or Windows https://docs.docker.com/install/#supported-platforms.

# Docker Compose

```bash
cd /path/to/ArchiveBox
docker compose up -d
```

To add new URLs to your archive:
```bash
echo bookmarks.html | docker-compose exec archivebox archive
```

Then open https://127.0.0.1:8098 to view the archive.

# Docker

1. Fetch and build the ArchiveBox Docker image:
```bash
docker build github.com/pirate/ArchiveBox -t archivebox
```

2. Create a volume to hold your ArchiveBox data:
```bash
docker volume create archivebox-data
```

2. Run ArchiveBox with `docker run` to add links to your archive:

To add a list of pages via URL of a feed.
```bash
docker run -v archivebox-data:/data archivebox 'https://example.com/some/rss/feed.xml'
```

To add a single link or a list of links from a file, pipe them in via stdin.
```bash
echo 'https://example.com' | docker run -i -v archivebox-data:/data archivebox
# or
cat bookmarks.html | docker run -i -v archivebox-data:/data archivebox
```