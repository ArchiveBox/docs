# {py:mod}`archivebox.api.auth`

```{py:module} archivebox.api.auth
```

```{autodoc2-docstring} archivebox.api.auth
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`APITokenAuthCheck <archivebox.api.auth.APITokenAuthCheck>`
  - ```{autodoc2-docstring} archivebox.api.auth.APITokenAuthCheck
    :summary:
    ```
* - {py:obj}`UserPassAuthCheck <archivebox.api.auth.UserPassAuthCheck>`
  - ```{autodoc2-docstring} archivebox.api.auth.UserPassAuthCheck
    :summary:
    ```
* - {py:obj}`HeaderTokenAuth <archivebox.api.auth.HeaderTokenAuth>`
  - ```{autodoc2-docstring} archivebox.api.auth.HeaderTokenAuth
    :summary:
    ```
* - {py:obj}`BearerTokenAuth <archivebox.api.auth.BearerTokenAuth>`
  - ```{autodoc2-docstring} archivebox.api.auth.BearerTokenAuth
    :summary:
    ```
* - {py:obj}`QueryParamTokenAuth <archivebox.api.auth.QueryParamTokenAuth>`
  - ```{autodoc2-docstring} archivebox.api.auth.QueryParamTokenAuth
    :summary:
    ```
* - {py:obj}`UsernameAndPasswordAuth <archivebox.api.auth.UsernameAndPasswordAuth>`
  - ```{autodoc2-docstring} archivebox.api.auth.UsernameAndPasswordAuth
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_or_create_api_token <archivebox.api.auth.get_or_create_api_token>`
  - ```{autodoc2-docstring} archivebox.api.auth.get_or_create_api_token
    :summary:
    ```
* - {py:obj}`auth_using_token <archivebox.api.auth.auth_using_token>`
  - ```{autodoc2-docstring} archivebox.api.auth.auth_using_token
    :summary:
    ```
* - {py:obj}`auth_using_password <archivebox.api.auth.auth_using_password>`
  - ```{autodoc2-docstring} archivebox.api.auth.auth_using_password
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`API_AUTH_METHODS <archivebox.api.auth.API_AUTH_METHODS>`
  - ```{autodoc2-docstring} archivebox.api.auth.API_AUTH_METHODS
    :summary:
    ```
````

### API

````{py:function} get_or_create_api_token(user)
:canonical: archivebox.api.auth.get_or_create_api_token

```{autodoc2-docstring} archivebox.api.auth.get_or_create_api_token
```
````

````{py:function} auth_using_token(token, request: typing.Optional[django.http.HttpRequest] = None) -> typing.Optional[django.contrib.auth.models.AbstractBaseUser]
:canonical: archivebox.api.auth.auth_using_token

```{autodoc2-docstring} archivebox.api.auth.auth_using_token
```
````

````{py:function} auth_using_password(username, password, request: typing.Optional[django.http.HttpRequest] = None) -> typing.Optional[django.contrib.auth.models.AbstractBaseUser]
:canonical: archivebox.api.auth.auth_using_password

```{autodoc2-docstring} archivebox.api.auth.auth_using_password
```
````

`````{py:class} APITokenAuthCheck
:canonical: archivebox.api.auth.APITokenAuthCheck

```{autodoc2-docstring} archivebox.api.auth.APITokenAuthCheck
```

````{py:method} authenticate(request: django.http.HttpRequest, key: typing.Optional[str] = None) -> typing.Optional[django.contrib.auth.models.AbstractBaseUser]
:canonical: archivebox.api.auth.APITokenAuthCheck.authenticate

```{autodoc2-docstring} archivebox.api.auth.APITokenAuthCheck.authenticate
```

````

`````

`````{py:class} UserPassAuthCheck
:canonical: archivebox.api.auth.UserPassAuthCheck

```{autodoc2-docstring} archivebox.api.auth.UserPassAuthCheck
```

````{py:method} authenticate(request: django.http.HttpRequest, username: typing.Optional[str] = None, password: typing.Optional[str] = None) -> typing.Optional[django.contrib.auth.models.AbstractBaseUser]
:canonical: archivebox.api.auth.UserPassAuthCheck.authenticate

```{autodoc2-docstring} archivebox.api.auth.UserPassAuthCheck.authenticate
```

````

`````

`````{py:class} HeaderTokenAuth()
:canonical: archivebox.api.auth.HeaderTokenAuth

Bases: {py:obj}`archivebox.api.auth.APITokenAuthCheck`, {py:obj}`ninja.security.APIKeyHeader`

```{autodoc2-docstring} archivebox.api.auth.HeaderTokenAuth
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.api.auth.HeaderTokenAuth.__init__
```

````{py:attribute} param_name
:canonical: archivebox.api.auth.HeaderTokenAuth.param_name
:value: >
   'X-ArchiveBox-API-Key'

```{autodoc2-docstring} archivebox.api.auth.HeaderTokenAuth.param_name
```

````

`````

````{py:class} BearerTokenAuth()
:canonical: archivebox.api.auth.BearerTokenAuth

Bases: {py:obj}`archivebox.api.auth.APITokenAuthCheck`, {py:obj}`ninja.security.HttpBearer`

```{autodoc2-docstring} archivebox.api.auth.BearerTokenAuth
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.api.auth.BearerTokenAuth.__init__
```

````

`````{py:class} QueryParamTokenAuth()
:canonical: archivebox.api.auth.QueryParamTokenAuth

Bases: {py:obj}`archivebox.api.auth.APITokenAuthCheck`, {py:obj}`ninja.security.APIKeyQuery`

```{autodoc2-docstring} archivebox.api.auth.QueryParamTokenAuth
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.api.auth.QueryParamTokenAuth.__init__
```

````{py:attribute} param_name
:canonical: archivebox.api.auth.QueryParamTokenAuth.param_name
:value: >
   'api_key'

```{autodoc2-docstring} archivebox.api.auth.QueryParamTokenAuth.param_name
```

````

`````

````{py:class} UsernameAndPasswordAuth()
:canonical: archivebox.api.auth.UsernameAndPasswordAuth

Bases: {py:obj}`archivebox.api.auth.UserPassAuthCheck`, {py:obj}`ninja.security.HttpBasicAuth`

```{autodoc2-docstring} archivebox.api.auth.UsernameAndPasswordAuth
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.api.auth.UsernameAndPasswordAuth.__init__
```

````

````{py:data} API_AUTH_METHODS
:canonical: archivebox.api.auth.API_AUTH_METHODS
:value: >
   None

```{autodoc2-docstring} archivebox.api.auth.API_AUTH_METHODS
```

````
