ArchiveBox supports several types of authentication for users logging in via the Admin Web UI or REST API.

> *💬 We offer [consulting services](https://docs.monadical.com/s/archivebox-consulting-services) to set up and secure ArchiveBox for corporate environments. If you or your organization want ongoing support and advanced development to capture difficult sites, we can provide it!*
> 
> We use this revenue (from mostly corporate clients who can afford to pay) to support open source development.

---

<br/>

## Set Up Admin Web UI Permissions

<img src="https://github.com/ArchiveBox/ArchiveBox/assets/511499/024913f0-ad2c-463c-aa4a-eb3d0ec8eb64" alt="Non-admin user permissions are only available to paying ArchiveBox clients" width="200px" align="right">

Use these three options to set up your desired permissions for non-admin guest users:
- [`PUBLIC_INDEX=True`](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#public_index--public_snapshots--public_add_view): Default *allows* non-logged-in users to see Snapshot list
- [`PUBLIC_SNAPSHOTS=True`](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#public_index--public_snapshots--public_add_view): Default *allows* non-logged-in users to see Snapshot content
- [`PUBLIC_ADD_VIEW=False`](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#public_index--public_snapshots--public_add_view): Default *doesn't allow* non-logged-in users to submit new URLs

> [!IMPORTANT]
> **Free ArchiveBox does not currently support setting up *non-admin* users** with more granular read-only permissions. We do offer this feature and more to [paying clients](https://docs.monadical.com/s/archivebox-consulting-services).

- [Wiki: Configuration (`PUBLIC_ADD_VIEW`, `PUBLIC_SNAPSHOTS`, `PUBLIC_INDEX`)]()
- [Wiki: Security Overview](https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview)

<br/>

## Admin Web UI Authentication Methods

> [!WARNING]
> Make sure you've **set up your [Web UI permissions](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#public_index--public_snapshots--public_add_view) first above** to restrict public access.  
> Configuring advanced auth methods below is pointless if your Web UI permissions allow unrestricted access to guests!

<br/>

### Username & Password (the default)

You need an admin account to access the Web UI, you can run the commands below to create/edit a user from the CLI:

```bash
archivebox manage createsuperuser
archivebox manage changepassword <username>

# equivalent: docker compose run archivebox manage [...]
# equivalent: docker run -v $PWD:/data archivebox/archivebox manage [...]
```

> [!TIP]
> If using Docker, you can set [`ADMIN_USERNAME` & `ADMIN_PASSWORD`](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#admin_username--admin_password) to auto-create an admin account on first run.

Existing users can be managed from the Admin UI here: `http://127.0.0.1:8000/admin/auth/user/`,  
and you can change your password in the UI here: `http://127.0.0.1:8000/admin/password_change/`.

<br/>

### Reverse Proxy Authentication

> Can be used with a reverse proxy auth provider like [oauth2-proxy](https://github.com/oauth2-proxy/oauth2-proxy), [Cloudflare Zero Trust](https://developers.cloudflare.com/cloudflare-one/tutorials/access-workers/#create-a-worker-with-custom-headers), [Authentik](https://docs.goauthentik.io/docs/providers/proxy/), and others.

Set these ArchiveBox configuration values to based on your reverse proxy setup and needs:
```bash
# REQUIRED: the header where your upstream reverse proxy will place the authenticated user's username/email
# EXAMPLE: Cf-Access-Authenticated-User-Email (if using Cloudflare)
REVERSE_PROXY_USER_HEADER=X-Remote-User

# REQUIRED: the IP/CIDR of your upstream reverse proxy server
# WARNING: make sure this range contains ONLY your reverse proxy server!
# ArchiveBox will completely trust any IP in this range for authentication
REVERSE_PROXY_WHITELIST=192.0.2.3/32

# OPTIONAL: redirect users to an external URL after they log out
LOGOUT_REDIRECT_URL=https://auth.yourcompany.example.com/after/logout
```

- https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#reverse_proxy_user_header
- https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#reverse_proxy_whitelist
- https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#logout_redirect_url
- https://github.com/ArchiveBox/ArchiveBox/pull/866

<br/>

### LDAP Authentication

> Can be used with an SSO provider like [Authentik](https://github.com/goauthentik/authentik), [Authelia](https://github.com/authelia/authelia), [Okta / Auth0](https://www.okta.com/), [Keycloak](https://www.keycloak.org/), and others.

First, `pip`-install the `ldap` add-on to use this feature (not needed if using Docker).
```bash
pip install archivebox[ldap]
```

Then set these configuration values to finish configuring LDAP:
```bash
LDAP=True
LDAP_SERVER_URI="ldap://ldap.example.com:3389"
LDAP_BIND_DN="ou=archivebox,ou=services,dc=ldap.example.com"
LDAP_BIND_PASSWORD="secret-bind-user-password"
LDAP_USER_BASE="ou=users,ou=archivebox,ou=services,dc=ldap.example.com"
LDAP_USER_FILTER="(objectClass=user)"

LDAP_USERNAME_ATTR="uid"
LDAP_FIRSTNAME_ATTR="givenName"
LDAP_LASTNAME_ATTR="sn"
LDAP_EMAIL_ATTR="mail"
```

- https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#ldap
- https://github.com/ArchiveBox/ArchiveBox/pull/1214
- https://github.com/django-auth-ldap/django-auth-ldap#example-configuration
- https://jumpcloud.com/blog/what-is-ldap-authentication

<br/>

### Not Yet Supported: SAML / OAuth2 / OpenID Authentication

> *We'd welcome PRs to add support for these using `django-allauth`!*

These methods are not natively supported by ArchiveBox at the moment. However it is still possible to use them with ArchiveBox by running your own [IdP (Identity Provider)](https://www.cloudflare.com/learning/access-management/what-is-an-identity-provider/) server to act as a bridge (e.g. [Authentik](https://docs.goauthentik.io/docs/providers/saml/), [Authelia](https://www.authelia.com/configuration/identity-providers/introduction/#openid-connect-10), [oauth2-proxy](https://github.com/oauth2-proxy/oauth2-proxy)).

The IdP server can act as a middleman gateway to authenticate users using an external SAML/OAuth/OpenID/etc. provider (e.g. Google, Microsoft, Github, Facebook, etc.), and then pass on the authenticated user's session info to ArchiveBox using LDAP or reverse proxy headers (as described above).

- https://www.cloudflare.com/learning/access-management/what-is-saml/
- https://docs.goauthentik.io/docs/providers/saml/
- https://docs.goauthentik.io/docs/providers/oauth2/
- https://www.authelia.com/configuration/identity-providers/introduction/#openid-connect-10
- https://github.com/oauth2-proxy/oauth2-proxy
- https://oauth2-proxy.github.io/oauth2-proxy/configuration/overview

<br/>

---

<br/>

## REST API

The REST API (available starting in v0.8.0) supports several methods of authentication for convenience.  
  
To see API docs, try endpoints interactively, and see how auth works, visit this URL on your ArchiveBox server:  
[`http://127.0.0.1:8000/api/v1/docs`](http://127.0.0.1:8000/api/v1/docs)

<img width="738" alt="Screenshot of django-ninja Swagger API docs page" src="https://github.com/ArchiveBox/ArchiveBox/assets/511499/ad914143-f48b-4d4e-aa8c-f89a2c70cee7">

To get started using the REST API, you can generate an API key for your user in the Admin Web UI:  
[`http://127.0.0.1:8000/admin/api/apitoken/add/`](http://127.0.0.1:8000/admin/api/apitoken/add/)  
  
or by calling the `http://127.0.0.1:8000/api/v1/auth/get_api_token` endpoint:
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

<br/>

> [!TIP]
> Bearer Tokens are the recommended method for the best balance of security and convenience.


### API Bearer Token Authentication

Pass `Authorization=Bearer YOURAPITOKENHERE` as a request header.

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/core/snapshots?limit=10' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer YOURAPITOKENHERE'
```

### API Request Header Authentication

Pass `X-API-Key=YOURAPITOKENHERE` as a request header.

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/core/snapshots?limit=10' \
  -H 'accept: application/json' \
  -H 'X-API-Key: YOURAPITOKENHERE'
```

<br/>

### API Query Parameter Authentication

> [!WARNING]
> This method is sometimes known as ["Capability URLs"](https://w3ctag.github.io/capability-urls/) because anyone in possession of the URL can perform API actions. It comes with several [important security caveats](https://security.stackexchange.com/questions/118975/is-it-safe-to-include-an-api-key-in-a-requests-url) and is not recommended unless you fully understand the risks.

Pass `api_key=YOURAPITOKENHERE` as a GET/POST query parameter.

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/core/snapshots?limit=10&api_key=YOURAPITOKENHERE' \
  -H 'accept: application/json'
```

<br/>

### API Session Cookie Authentication

> [!CAUTION]
> We recommend sticking to header-based authentication and not using this method unless you deeply understand the CSRF/CORS security risks.
> This method is mostly useful when testing API requests from the browser devtools, as it lets you skip having to pass an API key with every request.

> Browsers enforce that requests made to the ArchiveBox API from *other domains* will not include any session cookies by default. This is is an [important security principle](https://docs.djangoproject.com/en/5.0/ref/csrf/) that protects you from API requests being initiated from JS served to users on websites you don't control (aka CSRF/CORS attacks).
>
> You can tell browsers to allow incoming POST requests from specific domains you trust using the [`CSRF_TRUSTED_ORIGINS`](https://docs.djangoproject.com/en/5.0/ref/settings/#csrf-trusted-origins) option. but 

Log in via the Admin Web UI: `/admin/login/`, you can then re-use your login session id (stored in the `sessionid` cookie) for REST API requests. This makes it convenient to test API requests from a browser environment where you're already logged in.

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/core/snapshots?limit=10' \
  -H 'accept: application/json' \
  -H 'Cookie: sessionid=YOURSESSIONIDVALUEHERE'
```

<br/>

### API HTTP Basic Authentication

> [!CAUTION]
> This method is fairly uncommon and is only useful in a few niche situations where the other methods are not available.  
> **We will likely remove this method in a future ArchiveBox release if nobody uses it.**  
> *If you rely on this method and want us to keep it, please [open an issue](https://github.com/ArchiveBox/ArchiveBox/issues/new/choose) and explain your use-case!* 

Pass your ArchiveBox admin username & password via HTTP Basic Authentication.

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/core/snapshots?limit=10' \
  -u 'YOURUSERNAMEHERE:YOURPASSWORDHERE'
  -H 'accept: application/json'
```
