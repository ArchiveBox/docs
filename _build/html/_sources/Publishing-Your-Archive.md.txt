# Publishing Your Archive

The archive produced by `./archive` is suitable for serving on any provider that can host static html (e.g. github pages!).

You can also serve it from a home server or VPS by uploading the outputted `output` folder to your web directory, e.g. `/var/www/ArchiveBox` and configuring your webserver.  If you're using docker-compose, an Nginx server serving the archive via HTTP is provided right out of the box! See the [[Docker]] page for details.

Here's a sample nginx configuration that works to serve archive folders:

```nginx
location / {
    alias       /path/to/ArchiveBox/output/;
    index       index.html;
    autoindex   on;               # see directory listing upon clicking "The Files" links
    try_files   $uri $uri/ =404;
}
```

Make sure you're not running any content as CGI or PHP, you only want to serve static files!

Urls look like: `https://archive.example.com/archive/1493350273/en.wikipedia.org/wiki/Dining_philosophers_problem.html`

## Security Concerns

Re-hosting other people's content has security implications for any other sites sharing your hosting domain.  Make sure you understand the dangers of hosting unknown archived CSS & JS files [on your shared domain](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy).
Due to the security risk of serving some malicious JS you archived by accident, it's best to put this on a domain or subdomain of its own to keep cookies separate and slightly mitigate [CSRF attacks](https://en.wikipedia.org/wiki/Cross-site_request_forgery) and other nastiness.

## Copyright Concerns

Be aware that some sites you archive may not allow you to rehost their content publicly for copyright reasons, it's up to you to host responsibly and respond to takedown requests appropriately.

You may also want to blacklist your archive in `/robots.txt` if you don't want to be publicly assosciated with all the links you archive via search engine results.

Please modify the `FOOTER_INFO` config variable to add your contact info to the footer of your index.
