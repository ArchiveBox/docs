# Publishing Your Archive

There are two ways to publish your archive: using the `archivebox server` or by exporting and hosting it as static HTML.

<br/>

## 1. Use the built-in web server

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
and there is a commented-out example nginx config with SSL set up as well. If hosting publicly, it's essential to place an SSL termination server in front of ArchiveBox (e.g. [`traefik`](https://github.com/traefik/traefik), [`caddy`](https://caddyserver.com/docs/automatic-https#activation), or [`cloudflared`](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/)), 

> [!TIP]
> Advanced: You can use nginx to serve the static `/archive/` dir directly from the filesystem to increase performance.

<br/>

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

Urls look like: `https://demo.archivebox.io/archive/1493350273/en.wikipedia.org/wiki/Dining_philosophers_problem.html`

<br/>

---

<br/>

## Security Concerns

> [!CAUTION]
> Re-hosting untrusted archived content on a domain can potentially compromise *all apps on that domain*!  
> (including other subdomains)

Make sure you thoroughly understand the dangers of [hosting untrusted HTML/JS/CSS that may be captured during archiving](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy), and how viewing it can enable [CSRF attacks](https://en.wikipedia.org/wiki/Cross-site_request_forgery) across all apps on the same domain. If a logged-in user happens to visit an archived page with malicious Javascript embedded, it would allow the JS to hijack any cookies on the domain and pretend to be them, potentially exfiltrating or modifying other Snapshots/data on your server.

(This is why we don't support serving ArchiveBox from a subdirectory like `myapps.example.com/archivebox/`, it's too dangerous to share domains)

The industry standard approach is to use a separate domain for untrusted content, for example Github uses `githubusercontent.com` and Google uses `googleusercontent.com` for all user-uploaded files. If hosting ArchiveBox publicly, do the same and keep it on an isolated domain in order to mitigate potential damage of leaked cookies, CORS, and CSRF attack.  

To protect the Admin dashboard, it's also recommended to serve all content under `/archive/` on a separate domain from `/admin/`. We do this on our servers using a simple redirect rule in nginx/cloudflare like so:

- https://demo.archivebox.io: only serves `/`, redirects `/archive/*` to `demo-static.`
- https://demo-static.archivebox.io: only serves `/archive/`, redirects everything else to `demo.`

More info:
- https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview
- https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview#publishing
- https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview#%EF%B8%8F-things-to-watch-out-for-%EF%B8%8F

<br/>

---

<br/>

## Copyright Concerns

> [!WARNING]
> Be aware that some sites you archive may not allow you to rehost their content publicly for copyright reasons, it's up to you to host responsibly and respond to takedown requests appropriately based on the laws in your jurisdiction.

Archiving for personal backups, research, and some other use-cases are covered by [fair use copyright exemptions](https://guides.library.oregonstate.edu/copyright/libraries) in the USA, but if your archive can deprive the original author of revenue (e.g. if you rehost it for profit), then your use case might no longer be covered and you have to respond to DMCA takedown notices.

**As a general rule of thumb:**

- Copies cannot be made for commercial purposes
- The copying cannot be systematic (e.g., to replace subscriptions)
- All copies made must include a notice stating that the materials may be protected under copyright.

Please modify the [`FOOTER_INFO`](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#footer_info) config variable to add your contact info to the footer of your index.

Note: ArchiveBox prevents search engines from indexing your archives using [`/robots.txt`](https://github.com/ArchiveBox/ArchiveBox/blob/dev/archivebox/templates/static/robots.txt#L2) by default. It's not recommended to [disable](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#custom_templates_dir) this as it often leads to a flood of automated takedown requests and abuse reports to your hosting provider (from anti-piracy bots that scan for cloned copyrighted content via search engines).

*Keep in mind individuals, companies, schools, and libraries all have different copyright exemptions in different countries. Double check the specific laws for your situation in your own jurisdiction!*

#### Further Reading: USA Copyright Law & Fair Use Exemptions

- https://www.copyright.gov/title17/
- https://help.archive.org/help/rights/
- https://blog.archive.org/2024/03/01/fair-use-in-action-at-the-internet-archive/
- https://www.lib.ncsu.edu/workshops/understanding-copyright-and-fair-use-archival-research
- https://libguides.colorado.edu/c.php?g=1154758&p=8428124
- https://fairuse.stanford.edu/2003/11/10/digital_preservation_and_copyr/
- https://guides.library.oregonstate.edu/copyright/libraries
- https://www.clir.org/pubs/reports/pub112/body/
- https://github.com/pirate/internet-archiving-talk