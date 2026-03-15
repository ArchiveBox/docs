# {py:mod}`archivebox.tests.test_auth_ldap`

```{py:module} archivebox.tests.test_auth_ldap
```

```{autodoc2-docstring} archivebox.tests.test_auth_ldap
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestLDAPConfig <archivebox.tests.test_auth_ldap.TestLDAPConfig>`
  - ```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPConfig
    :summary:
    ```
* - {py:obj}`TestLDAPIntegration <archivebox.tests.test_auth_ldap.TestLDAPIntegration>`
  - ```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPIntegration
    :summary:
    ```
* - {py:obj}`TestLDAPAuthBackend <archivebox.tests.test_auth_ldap.TestLDAPAuthBackend>`
  - ```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPAuthBackend
    :summary:
    ```
* - {py:obj}`TestArchiveBoxWithLDAP <archivebox.tests.test_auth_ldap.TestArchiveBoxWithLDAP>`
  - ```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestArchiveBoxWithLDAP
    :summary:
    ```
* - {py:obj}`TestLDAPConfigValidationInArchiveBox <archivebox.tests.test_auth_ldap.TestLDAPConfigValidationInArchiveBox>`
  - ```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPConfigValidationInArchiveBox
    :summary:
    ```
````

### API

`````{py:class} TestLDAPConfig(methodName='runTest')
:canonical: archivebox.tests.test_auth_ldap.TestLDAPConfig

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPConfig
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPConfig.__init__
```

````{py:method} test_ldap_config_defaults()
:canonical: archivebox.tests.test_auth_ldap.TestLDAPConfig.test_ldap_config_defaults

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPConfig.test_ldap_config_defaults
```

````

````{py:method} test_ldap_config_validation_disabled()
:canonical: archivebox.tests.test_auth_ldap.TestLDAPConfig.test_ldap_config_validation_disabled

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPConfig.test_ldap_config_validation_disabled
```

````

````{py:method} test_ldap_config_validation_missing_fields()
:canonical: archivebox.tests.test_auth_ldap.TestLDAPConfig.test_ldap_config_validation_missing_fields

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPConfig.test_ldap_config_validation_missing_fields
```

````

````{py:method} test_ldap_config_validation_complete()
:canonical: archivebox.tests.test_auth_ldap.TestLDAPConfig.test_ldap_config_validation_complete

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPConfig.test_ldap_config_validation_complete
```

````

````{py:method} test_ldap_config_in_get_config()
:canonical: archivebox.tests.test_auth_ldap.TestLDAPConfig.test_ldap_config_in_get_config

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPConfig.test_ldap_config_in_get_config
```

````

`````

`````{py:class} TestLDAPIntegration(methodName='runTest')
:canonical: archivebox.tests.test_auth_ldap.TestLDAPIntegration

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPIntegration
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPIntegration.__init__
```

````{py:method} test_django_settings_without_ldap_enabled()
:canonical: archivebox.tests.test_auth_ldap.TestLDAPIntegration.test_django_settings_without_ldap_enabled

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPIntegration.test_django_settings_without_ldap_enabled
```

````

````{py:method} test_django_settings_with_ldap_library_check()
:canonical: archivebox.tests.test_auth_ldap.TestLDAPIntegration.test_django_settings_with_ldap_library_check

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPIntegration.test_django_settings_with_ldap_library_check
```

````

`````

`````{py:class} TestLDAPAuthBackend(methodName='runTest')
:canonical: archivebox.tests.test_auth_ldap.TestLDAPAuthBackend

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPAuthBackend
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPAuthBackend.__init__
```

````{py:method} test_ldap_backend_class_exists()
:canonical: archivebox.tests.test_auth_ldap.TestLDAPAuthBackend.test_ldap_backend_class_exists

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPAuthBackend.test_ldap_backend_class_exists
```

````

````{py:method} test_ldap_backend_inherits_correctly()
:canonical: archivebox.tests.test_auth_ldap.TestLDAPAuthBackend.test_ldap_backend_inherits_correctly

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPAuthBackend.test_ldap_backend_inherits_correctly
```

````

`````

`````{py:class} TestArchiveBoxWithLDAP(methodName='runTest')
:canonical: archivebox.tests.test_auth_ldap.TestArchiveBoxWithLDAP

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestArchiveBoxWithLDAP
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestArchiveBoxWithLDAP.__init__
```

````{py:method} setUp()
:canonical: archivebox.tests.test_auth_ldap.TestArchiveBoxWithLDAP.setUp

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestArchiveBoxWithLDAP.setUp
```

````

````{py:method} test_archivebox_init_without_ldap()
:canonical: archivebox.tests.test_auth_ldap.TestArchiveBoxWithLDAP.test_archivebox_init_without_ldap

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestArchiveBoxWithLDAP.test_archivebox_init_without_ldap
```

````

````{py:method} test_archivebox_version_with_ldap_config()
:canonical: archivebox.tests.test_auth_ldap.TestArchiveBoxWithLDAP.test_archivebox_version_with_ldap_config

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestArchiveBoxWithLDAP.test_archivebox_version_with_ldap_config
```

````

`````

`````{py:class} TestLDAPConfigValidationInArchiveBox(methodName='runTest')
:canonical: archivebox.tests.test_auth_ldap.TestLDAPConfigValidationInArchiveBox

Bases: {py:obj}`unittest.TestCase`

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPConfigValidationInArchiveBox
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPConfigValidationInArchiveBox.__init__
```

````{py:method} setUp()
:canonical: archivebox.tests.test_auth_ldap.TestLDAPConfigValidationInArchiveBox.setUp

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPConfigValidationInArchiveBox.setUp
```

````

````{py:method} test_archivebox_init_with_incomplete_ldap_config()
:canonical: archivebox.tests.test_auth_ldap.TestLDAPConfigValidationInArchiveBox.test_archivebox_init_with_incomplete_ldap_config

```{autodoc2-docstring} archivebox.tests.test_auth_ldap.TestLDAPConfigValidationInArchiveBox.test_archivebox_init_with_incomplete_ldap_config
```

````

`````
