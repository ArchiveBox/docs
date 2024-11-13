# {py:mod}`archivebox.machine.models`

```{py:module} archivebox.machine.models
```

```{autodoc2-docstring} archivebox.machine.models
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`MachineManager <archivebox.machine.models.MachineManager>`
  - ```{autodoc2-docstring} archivebox.machine.models.MachineManager
    :summary:
    ```
* - {py:obj}`Machine <archivebox.machine.models.Machine>`
  - ```{autodoc2-docstring} archivebox.machine.models.Machine
    :summary:
    ```
* - {py:obj}`NetworkInterfaceManager <archivebox.machine.models.NetworkInterfaceManager>`
  - ```{autodoc2-docstring} archivebox.machine.models.NetworkInterfaceManager
    :summary:
    ```
* - {py:obj}`NetworkInterface <archivebox.machine.models.NetworkInterface>`
  - ```{autodoc2-docstring} archivebox.machine.models.NetworkInterface
    :summary:
    ```
* - {py:obj}`InstalledBinaryManager <archivebox.machine.models.InstalledBinaryManager>`
  - ```{autodoc2-docstring} archivebox.machine.models.InstalledBinaryManager
    :summary:
    ```
* - {py:obj}`InstalledBinary <archivebox.machine.models.InstalledBinary>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_CURRENT_MACHINE <archivebox.machine.models._CURRENT_MACHINE>`
  - ```{autodoc2-docstring} archivebox.machine.models._CURRENT_MACHINE
    :summary:
    ```
* - {py:obj}`_CURRENT_INTERFACE <archivebox.machine.models._CURRENT_INTERFACE>`
  - ```{autodoc2-docstring} archivebox.machine.models._CURRENT_INTERFACE
    :summary:
    ```
* - {py:obj}`_CURRENT_BINARIES <archivebox.machine.models._CURRENT_BINARIES>`
  - ```{autodoc2-docstring} archivebox.machine.models._CURRENT_BINARIES
    :summary:
    ```
* - {py:obj}`MACHINE_RECHECK_INTERVAL <archivebox.machine.models.MACHINE_RECHECK_INTERVAL>`
  - ```{autodoc2-docstring} archivebox.machine.models.MACHINE_RECHECK_INTERVAL
    :summary:
    ```
* - {py:obj}`NETWORK_INTERFACE_RECHECK_INTERVAL <archivebox.machine.models.NETWORK_INTERFACE_RECHECK_INTERVAL>`
  - ```{autodoc2-docstring} archivebox.machine.models.NETWORK_INTERFACE_RECHECK_INTERVAL
    :summary:
    ```
* - {py:obj}`INSTALLED_BINARY_RECHECK_INTERVAL <archivebox.machine.models.INSTALLED_BINARY_RECHECK_INTERVAL>`
  - ```{autodoc2-docstring} archivebox.machine.models.INSTALLED_BINARY_RECHECK_INTERVAL
    :summary:
    ```
````

### API

````{py:data} _CURRENT_MACHINE
:canonical: archivebox.machine.models._CURRENT_MACHINE
:value: >
   None

```{autodoc2-docstring} archivebox.machine.models._CURRENT_MACHINE
```

````

````{py:data} _CURRENT_INTERFACE
:canonical: archivebox.machine.models._CURRENT_INTERFACE
:value: >
   None

```{autodoc2-docstring} archivebox.machine.models._CURRENT_INTERFACE
```

````

````{py:data} _CURRENT_BINARIES
:canonical: archivebox.machine.models._CURRENT_BINARIES
:value: >
   None

```{autodoc2-docstring} archivebox.machine.models._CURRENT_BINARIES
```

````

````{py:data} MACHINE_RECHECK_INTERVAL
:canonical: archivebox.machine.models.MACHINE_RECHECK_INTERVAL
:value: >
   None

```{autodoc2-docstring} archivebox.machine.models.MACHINE_RECHECK_INTERVAL
```

````

````{py:data} NETWORK_INTERFACE_RECHECK_INTERVAL
:canonical: archivebox.machine.models.NETWORK_INTERFACE_RECHECK_INTERVAL
:value: >
   None

```{autodoc2-docstring} archivebox.machine.models.NETWORK_INTERFACE_RECHECK_INTERVAL
```

````

````{py:data} INSTALLED_BINARY_RECHECK_INTERVAL
:canonical: archivebox.machine.models.INSTALLED_BINARY_RECHECK_INTERVAL
:value: >
   None

```{autodoc2-docstring} archivebox.machine.models.INSTALLED_BINARY_RECHECK_INTERVAL
```

````

`````{py:class} MachineManager
:canonical: archivebox.machine.models.MachineManager

Bases: {py:obj}`django.db.models.Manager`

```{autodoc2-docstring} archivebox.machine.models.MachineManager
```

````{py:method} current() -> archivebox.machine.models.Machine
:canonical: archivebox.machine.models.MachineManager.current

```{autodoc2-docstring} archivebox.machine.models.MachineManager.current
```

````

`````

`````{py:class} Machine(*args: typing.Any, **kwargs: typing.Any)
:canonical: archivebox.machine.models.Machine

Bases: {py:obj}`archivebox.abid_utils.models.ABIDModel`, {py:obj}`archivebox.abid_utils.models.ModelWithHealthStats`

```{autodoc2-docstring} archivebox.machine.models.Machine
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.machine.models.Machine.__init__
```

````{py:attribute} abid_prefix
:canonical: archivebox.machine.models.Machine.abid_prefix
:value: >
   'mxn_'

```{autodoc2-docstring} archivebox.machine.models.Machine.abid_prefix
```

````

````{py:attribute} abid_ts_src
:canonical: archivebox.machine.models.Machine.abid_ts_src
:value: >
   'self.created_at'

```{autodoc2-docstring} archivebox.machine.models.Machine.abid_ts_src
```

````

````{py:attribute} abid_uri_src
:canonical: archivebox.machine.models.Machine.abid_uri_src
:value: >
   'self.guid'

```{autodoc2-docstring} archivebox.machine.models.Machine.abid_uri_src
```

````

````{py:attribute} abid_subtype_src
:canonical: archivebox.machine.models.Machine.abid_subtype_src
:value: >
   '"01"'

```{autodoc2-docstring} archivebox.machine.models.Machine.abid_subtype_src
```

````

````{py:attribute} abid_rand_src
:canonical: archivebox.machine.models.Machine.abid_rand_src
:value: >
   'self.id'

```{autodoc2-docstring} archivebox.machine.models.Machine.abid_rand_src
```

````

````{py:attribute} abid_drift_allowed
:canonical: archivebox.machine.models.Machine.abid_drift_allowed
:value: >
   False

```{autodoc2-docstring} archivebox.machine.models.Machine.abid_drift_allowed
```

````

````{py:attribute} id
:canonical: archivebox.machine.models.Machine.id
:value: >
   'UUIDField(...)'

```{autodoc2-docstring} archivebox.machine.models.Machine.id
```

````

````{py:attribute} abid
:canonical: archivebox.machine.models.Machine.abid
:value: >
   'ABIDField(...)'

```{autodoc2-docstring} archivebox.machine.models.Machine.abid
```

````

````{py:attribute} created_at
:canonical: archivebox.machine.models.Machine.created_at
:value: >
   'AutoDateTimeField(...)'

```{autodoc2-docstring} archivebox.machine.models.Machine.created_at
```

````

````{py:attribute} modified_at
:canonical: archivebox.machine.models.Machine.modified_at
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.machine.models.Machine.modified_at
```

````

````{py:attribute} guid
:canonical: archivebox.machine.models.Machine.guid
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.machine.models.Machine.guid
```

````

````{py:attribute} hostname
:canonical: archivebox.machine.models.Machine.hostname
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.machine.models.Machine.hostname
```

````

````{py:attribute} hw_in_docker
:canonical: archivebox.machine.models.Machine.hw_in_docker
:value: >
   'BooleanField(...)'

```{autodoc2-docstring} archivebox.machine.models.Machine.hw_in_docker
```

````

````{py:attribute} hw_in_vm
:canonical: archivebox.machine.models.Machine.hw_in_vm
:value: >
   'BooleanField(...)'

```{autodoc2-docstring} archivebox.machine.models.Machine.hw_in_vm
```

````

````{py:attribute} hw_manufacturer
:canonical: archivebox.machine.models.Machine.hw_manufacturer
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.machine.models.Machine.hw_manufacturer
```

````

````{py:attribute} hw_product
:canonical: archivebox.machine.models.Machine.hw_product
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.machine.models.Machine.hw_product
```

````

````{py:attribute} hw_uuid
:canonical: archivebox.machine.models.Machine.hw_uuid
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.machine.models.Machine.hw_uuid
```

````

````{py:attribute} os_arch
:canonical: archivebox.machine.models.Machine.os_arch
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.machine.models.Machine.os_arch
```

````

````{py:attribute} os_family
:canonical: archivebox.machine.models.Machine.os_family
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.machine.models.Machine.os_family
```

````

````{py:attribute} os_platform
:canonical: archivebox.machine.models.Machine.os_platform
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.machine.models.Machine.os_platform
```

````

````{py:attribute} os_release
:canonical: archivebox.machine.models.Machine.os_release
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.machine.models.Machine.os_release
```

````

````{py:attribute} os_kernel
:canonical: archivebox.machine.models.Machine.os_kernel
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.machine.models.Machine.os_kernel
```

````

````{py:attribute} stats
:canonical: archivebox.machine.models.Machine.stats
:value: >
   'JSONField(...)'

```{autodoc2-docstring} archivebox.machine.models.Machine.stats
```

````

````{py:attribute} objects
:canonical: archivebox.machine.models.Machine.objects
:type: archivebox.machine.models.MachineManager
:value: >
   'MachineManager(...)'

```{autodoc2-docstring} archivebox.machine.models.Machine.objects
```

````

````{py:attribute} networkinterface_set
:canonical: archivebox.machine.models.Machine.networkinterface_set
:type: django.db.models.Manager[NetworkInterface]
:value: >
   None

```{autodoc2-docstring} archivebox.machine.models.Machine.networkinterface_set
```

````

`````

`````{py:class} NetworkInterfaceManager
:canonical: archivebox.machine.models.NetworkInterfaceManager

Bases: {py:obj}`django.db.models.Manager`

```{autodoc2-docstring} archivebox.machine.models.NetworkInterfaceManager
```

````{py:method} current() -> archivebox.machine.models.NetworkInterface
:canonical: archivebox.machine.models.NetworkInterfaceManager.current

```{autodoc2-docstring} archivebox.machine.models.NetworkInterfaceManager.current
```

````

`````

``````{py:class} NetworkInterface(*args: typing.Any, **kwargs: typing.Any)
:canonical: archivebox.machine.models.NetworkInterface

Bases: {py:obj}`archivebox.abid_utils.models.ABIDModel`, {py:obj}`archivebox.abid_utils.models.ModelWithHealthStats`

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface
```

```{rubric} Initialization
```

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.__init__
```

````{py:attribute} abid_prefix
:canonical: archivebox.machine.models.NetworkInterface.abid_prefix
:value: >
   'ixf_'

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.abid_prefix
```

````

````{py:attribute} abid_ts_src
:canonical: archivebox.machine.models.NetworkInterface.abid_ts_src
:value: >
   'self.machine.created_at'

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.abid_ts_src
```

````

````{py:attribute} abid_uri_src
:canonical: archivebox.machine.models.NetworkInterface.abid_uri_src
:value: >
   'self.machine.guid'

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.abid_uri_src
```

````

````{py:attribute} abid_subtype_src
:canonical: archivebox.machine.models.NetworkInterface.abid_subtype_src
:value: >
   'self.iface'

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.abid_subtype_src
```

````

````{py:attribute} abid_rand_src
:canonical: archivebox.machine.models.NetworkInterface.abid_rand_src
:value: >
   'self.id'

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.abid_rand_src
```

````

````{py:attribute} abid_drift_allowed
:canonical: archivebox.machine.models.NetworkInterface.abid_drift_allowed
:value: >
   False

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.abid_drift_allowed
```

````

````{py:attribute} id
:canonical: archivebox.machine.models.NetworkInterface.id
:value: >
   'UUIDField(...)'

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.id
```

````

````{py:attribute} abid
:canonical: archivebox.machine.models.NetworkInterface.abid
:value: >
   'ABIDField(...)'

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.abid
```

````

````{py:attribute} created_at
:canonical: archivebox.machine.models.NetworkInterface.created_at
:value: >
   'AutoDateTimeField(...)'

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.created_at
```

````

````{py:attribute} modified_at
:canonical: archivebox.machine.models.NetworkInterface.modified_at
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.modified_at
```

````

````{py:attribute} machine
:canonical: archivebox.machine.models.NetworkInterface.machine
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.machine
```

````

````{py:attribute} mac_address
:canonical: archivebox.machine.models.NetworkInterface.mac_address
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.mac_address
```

````

````{py:attribute} ip_public
:canonical: archivebox.machine.models.NetworkInterface.ip_public
:value: >
   'GenericIPAddressField(...)'

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.ip_public
```

````

````{py:attribute} ip_local
:canonical: archivebox.machine.models.NetworkInterface.ip_local
:value: >
   'GenericIPAddressField(...)'

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.ip_local
```

````

````{py:attribute} dns_server
:canonical: archivebox.machine.models.NetworkInterface.dns_server
:value: >
   'GenericIPAddressField(...)'

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.dns_server
```

````

````{py:attribute} hostname
:canonical: archivebox.machine.models.NetworkInterface.hostname
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.hostname
```

````

````{py:attribute} iface
:canonical: archivebox.machine.models.NetworkInterface.iface
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.iface
```

````

````{py:attribute} isp
:canonical: archivebox.machine.models.NetworkInterface.isp
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.isp
```

````

````{py:attribute} city
:canonical: archivebox.machine.models.NetworkInterface.city
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.city
```

````

````{py:attribute} region
:canonical: archivebox.machine.models.NetworkInterface.region
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.region
```

````

````{py:attribute} country
:canonical: archivebox.machine.models.NetworkInterface.country
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.country
```

````

````{py:attribute} objects
:canonical: archivebox.machine.models.NetworkInterface.objects
:type: archivebox.machine.models.NetworkInterfaceManager
:value: >
   'NetworkInterfaceManager(...)'

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.objects
```

````

`````{py:class} Meta
:canonical: archivebox.machine.models.NetworkInterface.Meta

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.Meta
```

````{py:attribute} unique_together
:canonical: archivebox.machine.models.NetworkInterface.Meta.unique_together
:value: >
   (('machine', 'ip_public', 'ip_local', 'mac_address', 'dns_server'),)

```{autodoc2-docstring} archivebox.machine.models.NetworkInterface.Meta.unique_together
```

````

`````

``````

`````{py:class} InstalledBinaryManager
:canonical: archivebox.machine.models.InstalledBinaryManager

Bases: {py:obj}`django.db.models.Manager`

```{autodoc2-docstring} archivebox.machine.models.InstalledBinaryManager
```

````{py:method} get_from_db_or_cache(binary: pydantic_pkgr.Binary) -> archivebox.machine.models.InstalledBinary
:canonical: archivebox.machine.models.InstalledBinaryManager.get_from_db_or_cache

```{autodoc2-docstring} archivebox.machine.models.InstalledBinaryManager.get_from_db_or_cache
```

````

`````

``````{py:class} InstalledBinary(*args: typing.Any, **kwargs: typing.Any)
:canonical: archivebox.machine.models.InstalledBinary

Bases: {py:obj}`archivebox.abid_utils.models.ABIDModel`, {py:obj}`archivebox.abid_utils.models.ModelWithHealthStats`

````{py:attribute} abid_prefix
:canonical: archivebox.machine.models.InstalledBinary.abid_prefix
:value: >
   'bin_'

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.abid_prefix
```

````

````{py:attribute} abid_ts_src
:canonical: archivebox.machine.models.InstalledBinary.abid_ts_src
:value: >
   'self.machine.created_at'

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.abid_ts_src
```

````

````{py:attribute} abid_uri_src
:canonical: archivebox.machine.models.InstalledBinary.abid_uri_src
:value: >
   'self.machine.guid'

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.abid_uri_src
```

````

````{py:attribute} abid_subtype_src
:canonical: archivebox.machine.models.InstalledBinary.abid_subtype_src
:value: >
   'self.binprovider'

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.abid_subtype_src
```

````

````{py:attribute} abid_rand_src
:canonical: archivebox.machine.models.InstalledBinary.abid_rand_src
:value: >
   'self.id'

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.abid_rand_src
```

````

````{py:attribute} abid_drift_allowed
:canonical: archivebox.machine.models.InstalledBinary.abid_drift_allowed
:value: >
   False

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.abid_drift_allowed
```

````

````{py:attribute} id
:canonical: archivebox.machine.models.InstalledBinary.id
:value: >
   'UUIDField(...)'

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.id
```

````

````{py:attribute} abid
:canonical: archivebox.machine.models.InstalledBinary.abid
:value: >
   'ABIDField(...)'

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.abid
```

````

````{py:attribute} created_at
:canonical: archivebox.machine.models.InstalledBinary.created_at
:value: >
   'AutoDateTimeField(...)'

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.created_at
```

````

````{py:attribute} modified_at
:canonical: archivebox.machine.models.InstalledBinary.modified_at
:value: >
   'DateTimeField(...)'

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.modified_at
```

````

````{py:attribute} machine
:canonical: archivebox.machine.models.InstalledBinary.machine
:value: >
   'ForeignKey(...)'

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.machine
```

````

````{py:attribute} name
:canonical: archivebox.machine.models.InstalledBinary.name
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.name
```

````

````{py:attribute} binprovider
:canonical: archivebox.machine.models.InstalledBinary.binprovider
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.binprovider
```

````

````{py:attribute} abspath
:canonical: archivebox.machine.models.InstalledBinary.abspath
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.abspath
```

````

````{py:attribute} version
:canonical: archivebox.machine.models.InstalledBinary.version
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.version
```

````

````{py:attribute} sha256
:canonical: archivebox.machine.models.InstalledBinary.sha256
:value: >
   'CharField(...)'

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.sha256
```

````

````{py:attribute} objects
:canonical: archivebox.machine.models.InstalledBinary.objects
:type: archivebox.machine.models.InstalledBinaryManager
:value: >
   'InstalledBinaryManager(...)'

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.objects
```

````

`````{py:class} Meta
:canonical: archivebox.machine.models.InstalledBinary.Meta

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.Meta
```

````{py:attribute} verbose_name
:canonical: archivebox.machine.models.InstalledBinary.Meta.verbose_name
:value: >
   'Installed Binary'

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.Meta.verbose_name
```

````

````{py:attribute} verbose_name_plural
:canonical: archivebox.machine.models.InstalledBinary.Meta.verbose_name_plural
:value: >
   'Installed Binaries'

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.Meta.verbose_name_plural
```

````

````{py:attribute} unique_together
:canonical: archivebox.machine.models.InstalledBinary.Meta.unique_together
:value: >
   (('machine', 'name', 'binprovider', 'abspath', 'version', 'sha256'),)

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.Meta.unique_together
```

````

`````

````{py:method} __str__() -> str
:canonical: archivebox.machine.models.InstalledBinary.__str__

````

````{py:method} clean(*args, **kwargs) -> None
:canonical: archivebox.machine.models.InstalledBinary.clean

````

````{py:method} BINARY() -> pydantic_pkgr.Binary
:canonical: archivebox.machine.models.InstalledBinary.BINARY

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.BINARY
```

````

````{py:method} BINPROVIDER() -> pydantic_pkgr.BinProvider
:canonical: archivebox.machine.models.InstalledBinary.BINPROVIDER

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.BINPROVIDER
```

````

````{py:method} load_from_db() -> pydantic_pkgr.Binary
:canonical: archivebox.machine.models.InstalledBinary.load_from_db

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.load_from_db
```

````

````{py:method} load_fresh() -> pydantic_pkgr.Binary
:canonical: archivebox.machine.models.InstalledBinary.load_fresh

```{autodoc2-docstring} archivebox.machine.models.InstalledBinary.load_fresh
```

````

``````
