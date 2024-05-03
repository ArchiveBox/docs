ArchiveBox supports 4 types of authentication currently.

> [!WARNING]
> This page is a work in progress, follow the links to learn more about each authentication setup below.
> *To help make this page better, submit a pull request here: [`ArchiveBox/docs/Setting-Up-Authentication.md`](https://github.com/ArchiveBox/docs/blob/master/Setting-up-Authentication.md).

If you encounter any issues or need help feel free to ask questions in our public forum: https://zulip.archivebox.io

---

### Username & Password (the default)

```bash
archivebox manage createsuperuser

archivebox manage changepassword
```

- https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#admin_username--admin_password

### Reverse Proxy Authentication (e.g. Authelia)

- https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#reverse_proxy_user_header
- https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#reverse_proxy_whitelist
- https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#logout_redirect_url
- https://github.com/ArchiveBox/ArchiveBox/pull/866

### LDAP Authentication

- https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#ldap
- https://github.com/ArchiveBox/ArchiveBox/pull/1214
- https://github.com/django-auth-ldap/django-auth-ldap#example-configuration
- https://jumpcloud.com/blog/what-is-ldap-authentication

### API Token Authentication

The new REST API released in v0.8.0 supports several methods of authentication using an API token.

First, generate your API key in your Admin UI: `[/admin/api/apitoken/add/`](http://127.0.0.1:8000/admin/api/apitoken/add/).
You can read the API docs and test the authentication methods here: [`/api/v1/docs`](http://127.0.0.1:8000/api/v1/docs).

- passing Bearer=xyz as a bearer token request header
- passing `X-API-Key=xyz` as a request header
- passing `api_key=xyz` as a GET/POST query parameter
- fallback: passing username & password via HTTP Basic Authentication (not recommended)

<img width="738" alt="Screenshot 2024-05-03 at 4 40 22 PM" src="https://github.com/ArchiveBox/ArchiveBox/assets/511499/ad914143-f48b-4d4e-aa8c-f89a2c70cee7">

---

## Web Server UI Permissions

Make sure to set up your Web UI permissions to allow or prevent guest access to content according to your needs. See the links below for more information.

- https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#public_index--public_snapshots--public_add_view
- https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview