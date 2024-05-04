ArchiveBox supports several types of authentication for users logging in via the Admin Web UI or REST API.

> [!WARNING]
> *This page is a work in progress, follow the links to learn more about each authentication setup below.*  
> To help make this page better, submit a pull request here: [`ArchiveBox/docs/Setting-Up-Authentication.md`](https://github.com/ArchiveBox/docs/blob/master/Setting-up-Authentication.md).

💬 If you encounter any issues or need help feel free to ask questions in our public forum: https://zulip.archivebox.io

---

<br/>

## Set Up Admin Web UI Permissions

> [!IMPORTANT]
> Make sure to **set up your Web UI permissions first** to allow/restrict public access according to your needs.  
> Configuring advanced auth methods below wont help you if your archive is set up to be visible to the public!

- https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#public_index--public_snapshots--public_add_view
- https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview

<br/>

## Admin Web UI Authentication Methods

### Username & Password (the default)

Make sure you have an admin User created first, you can run the commands below to create/edit a user from the command line:

```bash
archivebox manage createsuperuser
archivebox manage changepassword <username>

# equivalent: docker compose run archivebox manage [...]
# equivalent: docker run -v $PWD:/data archivebox/archivebox manage [...]
```

If using Docker or Docker Compose, you can alternatively configure [`ADMIN_USERNAME` & `ADMIN_PASSWORD`](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#admin_username--admin_password) to create an admin user automatically on first run.

Existing users can be managed from the Admin UI here: `/admin/auth/user/`, and you can change your password in the UI here: `/admin/password_change/`.

<br/>

### Reverse Proxy Authentication

> Can be used with reverse proxy auth provider like [oauth2-proxy](https://github.com/oauth2-proxy/oauth2-proxy), [Cloudflare Zero Trust](https://developers.cloudflare.com/cloudflare-one/tutorials/access-workers/#create-a-worker-with-custom-headers), [Authentik](https://docs.goauthentik.io/docs/providers/proxy/), and others.

- https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#reverse_proxy_user_header
- https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#reverse_proxy_whitelist
- https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#logout_redirect_url
- https://github.com/ArchiveBox/ArchiveBox/pull/866

### LDAP Authentication

> Can be used with an SSO provider like [Authentik](https://github.com/goauthentik/authentik), [Authelia](https://github.com/authelia/authelia), [Okta / Auth0](https://www.okta.com/), [Keycloak](https://www.keycloak.org/), and others.

- https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#ldap
- https://github.com/ArchiveBox/ArchiveBox/pull/1214
- https://github.com/django-auth-ldap/django-auth-ldap#example-configuration
- https://jumpcloud.com/blog/what-is-ldap-authentication

<br/>

### Not Yet Supported: SAML / OAuth2 / OpenID Authentication

These methods are not natively supported by ArchiveBox at the moment. However it is still possible to use them with ArchiveBox by running your own [IdP (Identity Provider)](https://www.cloudflare.com/learning/access-management/what-is-an-identity-provider/) server (e.g. [Authentik](https://docs.goauthentik.io/docs/providers/saml/), [Authelia](https://www.authelia.com/configuration/identity-providers/introduction/#openid-connect-10), etc.).

The IdP server can act as a middleman gateway to authenticate users using an external SAML/OAuth/OpenID/etc. provider (e.g. Google, Microsoft, Github, Facebook, etc.), and then pass on the authenticated user's session info to ArchiveBox using LDAP or reverse proxy headers (as described above).

- https://www.cloudflare.com/learning/access-management/what-is-saml/
- https://docs.goauthentik.io/docs/providers/saml/
- https://docs.goauthentik.io/docs/providers/oauth2/
- https://www.authelia.com/configuration/identity-providers/introduction/#openid-connect-10

> *We'd welcome PRs to add support for more providers using `django-allauth`!*

<br/>

---

<br/>

## REST API

The new REST API released in v0.8.0 supports several methods of authentication using an API token (or username & password).
You can read the API docs and test the authentication methods here: [`/api/v1/docs`](http://127.0.0.1:8000/api/v1/docs).

<img width="738" alt="Screenshot 2024-05-03 at 4 40 22 PM" src="https://github.com/ArchiveBox/ArchiveBox/assets/511499/ad914143-f48b-4d4e-aa8c-f89a2c70cee7">

To get started using the REST API, generate an API key for your user through the Admin Web UI: `[/admin/api/apitoken/add/`](http://127.0.0.1:8000/admin/api/apitoken/add/) or by calling the `/api/v1/auth/get_api_token` endpoint:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/auth/get_api_token' \
  -H 'Content-Type: application/json'
  -d '{"username": "YOURUSERNAMEHERE", "password": "YOURPASSWORDHERE"}'
```

#### Further Reading

- https://github.com/ArchiveBox/ArchiveBox/blob/dev/archivebox/api/auth.py#:~:text=API_AUTH_METHODS
- https://github.com/ArchiveBox/ArchiveBox/blob/dev/archivebox/api/v1_auth.py
- https://django-ninja.dev/guides/authentication/
- https://swagger.io/docs/specification/authentication/

### Bearer Token Authentication

Pass `Bearer=YOURAPITOKENHERE` as a bearer token request header.

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/core/snapshots?limit=10' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer YOURAPITOKENHERE'
```

### Request Header Authentication

Pass `X-API-Key=YOURAPITOKENHERE` as a request header.

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/core/snapshots?limit=10' \
  -H 'accept: application/json' \
  -H 'X-API-Key: YOURAPITOKENHERE'
```

### Query Parameter Authentication

Pass `api_key=YOURAPITOKENHERE` as a GET/POST query parameter.

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/core/snapshots?limit=10&api_key=YOURAPITOKENHERE' \
  -H 'accept: application/json'
```

### HTTP Basic Authentication

Pass your user's username & password via HTTP Basic Authentication (not recommended).

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/core/snapshots?limit=10' \
  -u 'YOURUSERNAMEHERE:YOURPASSWORDHERE'
  -H 'accept: application/json'
```