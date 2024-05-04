# Publishing Your Archive

There are two ways to publish your archive: using the `archivebox server` or by exporting and hosting it as static HTML.

## 1. Use the built-in webserver

```bash
# set the permissions depending on how public/locked down you want it to be
archivebox config --set PUBLIC_INDEX=True
archivebox config --set PUBLIC_SNAPSHOTS=True
archivebox config --set PUBLIC_ADD_VIEW=True

# create an admin username and password for yourself
archivebox manage createsuperuser

# then start the webserver and open the web UI in your browser
archivebox server 0.0.0.0:8000
open http://127.0.0.1:8000
```

This server is enabled out-of-the-box if you're using `docker-compose` to run ArchiveBox,
and there is a commented-out example nginx config with SSL set up as well.

## 2. Export and host it as static HTML

```bash
archivebox list --html --with-headers > index.html
archivebox list --json --with-headers > index.json

# then upload the entire output folder containing index.html and archive/ somewhere
# e.g. github pages or another static hosting provider

# you can also serve it with the simple python HTTP server
python3 -m http.server --bind 0.0.0.0 --directory . 8000
open http://127.0.0.1:8000
```

Here's a sample nginx configuration that works to serve your static archive folder:

```nginx
location / {
    alias       /path/to/your/ArchiveBox/data/;
    index       index.html;
    autoindex   on;
    try_files   $uri $uri/ =404;
}
```

Make sure you're not running any content as CGI or PHP, you only want to serve static files!

Urls look like: `https://archive.example.com/archive/1493350273/en.wikipedia.org/wiki/Dining_philosophers_problem.html`

---

## Security Concerns

Re-hosting other people's content has security implications for any other sites sharing your hosting domain.  Make sure you understand the dangers of hosting untrusted archived HTML/JS/CSS [on a shared domain](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy).
Due to the security risk of serving some malicious JS you archived by accident, it's best to put this on a domain or subdomain of its own to keep cookies separate and help limit the effectiveness of [CSRF attacks](https://en.wikipedia.org/wiki/Cross-site_request_forgery) and other nastiness.

More info:
- https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview
- https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview#publishing
- https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview#%EF%B8%8F-things-to-watch-out-for-%EF%B8%8F

## Copyright Concerns

> [!WARNING]
> Be aware that some sites you archive may not allow you to rehost their content publicly for copyright reasons, it's up to you to host responsibly and respond to takedown requests appropriately based on the laws in your jurisdiction.

Archiving for personal backups, research, and some other use-cases are covered by [fair use copyright exemptions](https://guides.library.oregonstate.edu/copyright/libraries) in the USA, but if your archive can deprive the original author of revenue (e.g. if you rehost it publicly), then your use case might no longer be covered and you have to respond to DMCA takedown notices.

**As a general rule of thumb:**

- Copies cannot be made for commercial purposes
- The copying cannot be systematic (e.g., to replace subscriptions)
- All copies made must include a notice stating that the materials may be protected under copyright.

Please modify the [`FOOTER_INFO`](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#footer_info) config variable to add your contact info to the footer of your index.

You may also want to blacklist your archive in `/robots.txt` if you don't want to be publicly associated with all the links you archive via search engine results.

#### Further Reading

*Keep in mind individuals, companies, schools, and libraries all have different copyright exemptions in different countries. Double check the specific laws for your situation in your own jurisdiction!*

- https://www.copyright.gov/title17/
- https://help.archive.org/help/rights/
- https://blog.archive.org/2024/03/01/fair-use-in-action-at-the-internet-archive/
- https://www.lib.ncsu.edu/workshops/understanding-copyright-and-fair-use-archival-research
- https://libguides.colorado.edu/c.php?g=1154758&p=8428124
- https://fairuse.stanford.edu/2003/11/10/digital_preservation_and_copyr/
- https://guides.library.oregonstate.edu/copyright/libraries
- https://www.clir.org/pubs/reports/pub112/body/
- https://github.com/pirate/internet-archiving-talk