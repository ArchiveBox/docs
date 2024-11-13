# {py:mod}`archivebox.machine.admin`

```{py:module} archivebox.machine.admin
```

```{autodoc2-docstring} archivebox.machine.admin
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`MachineAdmin <archivebox.machine.admin.MachineAdmin>`
  -
* - {py:obj}`NetworkInterfaceAdmin <archivebox.machine.admin.NetworkInterfaceAdmin>`
  -
* - {py:obj}`InstalledBinaryAdmin <archivebox.machine.admin.InstalledBinaryAdmin>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`register_admin <archivebox.machine.admin.register_admin>`
  - ```{autodoc2-docstring} archivebox.machine.admin.register_admin
    :summary:
    ```
````

### API

`````{py:class} MachineAdmin(model, admin_site)
:canonical: archivebox.machine.admin.MachineAdmin

Bases: {py:obj}`abid_utils.admin.ABIDModelAdmin`

````{py:attribute} list_display
:canonical: archivebox.machine.admin.MachineAdmin.list_display
:value: >
   ('abid', 'created_at', 'hostname', 'ips', 'os_platform', 'hw_in_docker', 'hw_in_vm', 'hw_manufacture...

```{autodoc2-docstring} archivebox.machine.admin.MachineAdmin.list_display
```

````

````{py:attribute} sort_fields
:canonical: archivebox.machine.admin.MachineAdmin.sort_fields
:value: >
   ('abid', 'created_at', 'hostname', 'ips', 'os_platform', 'hw_in_docker', 'hw_in_vm', 'hw_manufacture...

```{autodoc2-docstring} archivebox.machine.admin.MachineAdmin.sort_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.machine.admin.MachineAdmin.readonly_fields
:value: >
   ('guid', 'created_at', 'modified_at', 'abid_info', 'ips')

```{autodoc2-docstring} archivebox.machine.admin.MachineAdmin.readonly_fields
```

````

````{py:attribute} fields
:canonical: archivebox.machine.admin.MachineAdmin.fields
:value: >
   ()

```{autodoc2-docstring} archivebox.machine.admin.MachineAdmin.fields
```

````

````{py:attribute} list_filter
:canonical: archivebox.machine.admin.MachineAdmin.list_filter
:value: >
   ('hw_in_docker', 'hw_in_vm', 'os_arch', 'os_family', 'os_platform')

```{autodoc2-docstring} archivebox.machine.admin.MachineAdmin.list_filter
```

````

````{py:attribute} ordering
:canonical: archivebox.machine.admin.MachineAdmin.ordering
:value: >
   ['-created_at']

```{autodoc2-docstring} archivebox.machine.admin.MachineAdmin.ordering
```

````

````{py:attribute} list_per_page
:canonical: archivebox.machine.admin.MachineAdmin.list_per_page
:value: >
   100

```{autodoc2-docstring} archivebox.machine.admin.MachineAdmin.list_per_page
```

````

````{py:attribute} actions
:canonical: archivebox.machine.admin.MachineAdmin.actions
:value: >
   ['delete_selected']

```{autodoc2-docstring} archivebox.machine.admin.MachineAdmin.actions
```

````

````{py:method} ips(machine)
:canonical: archivebox.machine.admin.MachineAdmin.ips

```{autodoc2-docstring} archivebox.machine.admin.MachineAdmin.ips
```

````

`````

`````{py:class} NetworkInterfaceAdmin(model, admin_site)
:canonical: archivebox.machine.admin.NetworkInterfaceAdmin

Bases: {py:obj}`abid_utils.admin.ABIDModelAdmin`

````{py:attribute} list_display
:canonical: archivebox.machine.admin.NetworkInterfaceAdmin.list_display
:value: >
   ('abid', 'created_at', 'machine_info', 'ip_public', 'dns_server', 'isp', 'country', 'region', 'city'...

```{autodoc2-docstring} archivebox.machine.admin.NetworkInterfaceAdmin.list_display
```

````

````{py:attribute} sort_fields
:canonical: archivebox.machine.admin.NetworkInterfaceAdmin.sort_fields
:value: >
   ('abid', 'created_at', 'machine_info', 'ip_public', 'dns_server', 'isp', 'country', 'region', 'city'...

```{autodoc2-docstring} archivebox.machine.admin.NetworkInterfaceAdmin.sort_fields
```

````

````{py:attribute} search_fields
:canonical: archivebox.machine.admin.NetworkInterfaceAdmin.search_fields
:value: >
   ('abid', 'machine__abid', 'iface', 'ip_public', 'ip_local', 'mac_address', 'dns_server', 'hostname',...

```{autodoc2-docstring} archivebox.machine.admin.NetworkInterfaceAdmin.search_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.machine.admin.NetworkInterfaceAdmin.readonly_fields
:value: >
   ('machine', 'created_at', 'modified_at', 'abid_info', 'mac_address', 'ip_public', 'ip_local', 'dns_s...

```{autodoc2-docstring} archivebox.machine.admin.NetworkInterfaceAdmin.readonly_fields
```

````

````{py:attribute} fields
:canonical: archivebox.machine.admin.NetworkInterfaceAdmin.fields
:value: >
   ()

```{autodoc2-docstring} archivebox.machine.admin.NetworkInterfaceAdmin.fields
```

````

````{py:attribute} list_filter
:canonical: archivebox.machine.admin.NetworkInterfaceAdmin.list_filter
:value: >
   ('isp', 'country', 'region')

```{autodoc2-docstring} archivebox.machine.admin.NetworkInterfaceAdmin.list_filter
```

````

````{py:attribute} ordering
:canonical: archivebox.machine.admin.NetworkInterfaceAdmin.ordering
:value: >
   ['-created_at']

```{autodoc2-docstring} archivebox.machine.admin.NetworkInterfaceAdmin.ordering
```

````

````{py:attribute} list_per_page
:canonical: archivebox.machine.admin.NetworkInterfaceAdmin.list_per_page
:value: >
   100

```{autodoc2-docstring} archivebox.machine.admin.NetworkInterfaceAdmin.list_per_page
```

````

````{py:attribute} actions
:canonical: archivebox.machine.admin.NetworkInterfaceAdmin.actions
:value: >
   ['delete_selected']

```{autodoc2-docstring} archivebox.machine.admin.NetworkInterfaceAdmin.actions
```

````

````{py:method} machine_info(iface)
:canonical: archivebox.machine.admin.NetworkInterfaceAdmin.machine_info

```{autodoc2-docstring} archivebox.machine.admin.NetworkInterfaceAdmin.machine_info
```

````

`````

`````{py:class} InstalledBinaryAdmin(model, admin_site)
:canonical: archivebox.machine.admin.InstalledBinaryAdmin

Bases: {py:obj}`abid_utils.admin.ABIDModelAdmin`

````{py:attribute} list_display
:canonical: archivebox.machine.admin.InstalledBinaryAdmin.list_display
:value: >
   ('abid', 'created_at', 'machine_info', 'name', 'binprovider', 'version', 'abspath', 'sha256', 'healt...

```{autodoc2-docstring} archivebox.machine.admin.InstalledBinaryAdmin.list_display
```

````

````{py:attribute} sort_fields
:canonical: archivebox.machine.admin.InstalledBinaryAdmin.sort_fields
:value: >
   ('abid', 'created_at', 'machine_info', 'name', 'binprovider', 'version', 'abspath', 'sha256')

```{autodoc2-docstring} archivebox.machine.admin.InstalledBinaryAdmin.sort_fields
```

````

````{py:attribute} search_fields
:canonical: archivebox.machine.admin.InstalledBinaryAdmin.search_fields
:value: >
   ('abid', 'machine__abid', 'name', 'binprovider', 'version', 'abspath', 'sha256')

```{autodoc2-docstring} archivebox.machine.admin.InstalledBinaryAdmin.search_fields
```

````

````{py:attribute} readonly_fields
:canonical: archivebox.machine.admin.InstalledBinaryAdmin.readonly_fields
:value: >
   ('created_at', 'modified_at', 'abid_info')

```{autodoc2-docstring} archivebox.machine.admin.InstalledBinaryAdmin.readonly_fields
```

````

````{py:attribute} fields
:canonical: archivebox.machine.admin.InstalledBinaryAdmin.fields
:value: >
   ('machine', 'name', 'binprovider', 'abspath', 'version', 'sha256')

```{autodoc2-docstring} archivebox.machine.admin.InstalledBinaryAdmin.fields
```

````

````{py:attribute} list_filter
:canonical: archivebox.machine.admin.InstalledBinaryAdmin.list_filter
:value: >
   ('name', 'binprovider', 'machine_id')

```{autodoc2-docstring} archivebox.machine.admin.InstalledBinaryAdmin.list_filter
```

````

````{py:attribute} ordering
:canonical: archivebox.machine.admin.InstalledBinaryAdmin.ordering
:value: >
   ['-created_at']

```{autodoc2-docstring} archivebox.machine.admin.InstalledBinaryAdmin.ordering
```

````

````{py:attribute} list_per_page
:canonical: archivebox.machine.admin.InstalledBinaryAdmin.list_per_page
:value: >
   100

```{autodoc2-docstring} archivebox.machine.admin.InstalledBinaryAdmin.list_per_page
```

````

````{py:attribute} actions
:canonical: archivebox.machine.admin.InstalledBinaryAdmin.actions
:value: >
   ['delete_selected']

```{autodoc2-docstring} archivebox.machine.admin.InstalledBinaryAdmin.actions
```

````

````{py:method} machine_info(installed_binary)
:canonical: archivebox.machine.admin.InstalledBinaryAdmin.machine_info

```{autodoc2-docstring} archivebox.machine.admin.InstalledBinaryAdmin.machine_info
```

````

`````

````{py:function} register_admin(admin_site)
:canonical: archivebox.machine.admin.register_admin

```{autodoc2-docstring} archivebox.machine.admin.register_admin
```
````
