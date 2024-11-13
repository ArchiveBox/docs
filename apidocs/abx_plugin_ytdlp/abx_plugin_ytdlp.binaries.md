# {py:mod}`abx_plugin_ytdlp.binaries`

```{py:module} abx_plugin_ytdlp.binaries
```

```{autodoc2-docstring} abx_plugin_ytdlp.binaries
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`YtdlpBinary <abx_plugin_ytdlp.binaries.YtdlpBinary>`
  -
* - {py:obj}`FfmpegBinary <abx_plugin_ytdlp.binaries.FfmpegBinary>`
  -
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__package__ <abx_plugin_ytdlp.binaries.__package__>`
  - ```{autodoc2-docstring} abx_plugin_ytdlp.binaries.__package__
    :summary:
    ```
* - {py:obj}`YTDLP_BINARY <abx_plugin_ytdlp.binaries.YTDLP_BINARY>`
  - ```{autodoc2-docstring} abx_plugin_ytdlp.binaries.YTDLP_BINARY
    :summary:
    ```
* - {py:obj}`FFMPEG_BINARY <abx_plugin_ytdlp.binaries.FFMPEG_BINARY>`
  - ```{autodoc2-docstring} abx_plugin_ytdlp.binaries.FFMPEG_BINARY
    :summary:
    ```
````

### API

````{py:data} __package__
:canonical: abx_plugin_ytdlp.binaries.__package__
:value: >
   'abx_plugin_ytdlp'

```{autodoc2-docstring} abx_plugin_ytdlp.binaries.__package__
```

````

`````{py:class} YtdlpBinary(/, **data: typing.Any)
:canonical: abx_plugin_ytdlp.binaries.YtdlpBinary

Bases: {py:obj}`pydantic_pkgr.Binary`

````{py:attribute} name
:canonical: abx_plugin_ytdlp.binaries.YtdlpBinary.name
:type: pydantic_pkgr.BinName
:value: >
   None

```{autodoc2-docstring} abx_plugin_ytdlp.binaries.YtdlpBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: abx_plugin_ytdlp.binaries.YtdlpBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} abx_plugin_ytdlp.binaries.YtdlpBinary.binproviders_supported
```

````

`````

````{py:data} YTDLP_BINARY
:canonical: abx_plugin_ytdlp.binaries.YTDLP_BINARY
:value: >
   'YtdlpBinary(...)'

```{autodoc2-docstring} abx_plugin_ytdlp.binaries.YTDLP_BINARY
```

````

`````{py:class} FfmpegBinary(/, **data: typing.Any)
:canonical: abx_plugin_ytdlp.binaries.FfmpegBinary

Bases: {py:obj}`pydantic_pkgr.Binary`

````{py:attribute} name
:canonical: abx_plugin_ytdlp.binaries.FfmpegBinary.name
:type: pydantic_pkgr.BinName
:value: >
   'ffmpeg'

```{autodoc2-docstring} abx_plugin_ytdlp.binaries.FfmpegBinary.name
```

````

````{py:attribute} binproviders_supported
:canonical: abx_plugin_ytdlp.binaries.FfmpegBinary.binproviders_supported
:type: typing.List[pydantic.InstanceOf[pydantic_pkgr.BinProvider]]
:value: >
   None

```{autodoc2-docstring} abx_plugin_ytdlp.binaries.FfmpegBinary.binproviders_supported
```

````

````{py:attribute} overrides
:canonical: abx_plugin_ytdlp.binaries.FfmpegBinary.overrides
:type: pydantic_pkgr.BinaryOverrides
:value: >
   None

```{autodoc2-docstring} abx_plugin_ytdlp.binaries.FfmpegBinary.overrides
```

````

`````

````{py:data} FFMPEG_BINARY
:canonical: abx_plugin_ytdlp.binaries.FFMPEG_BINARY
:value: >
   'FfmpegBinary(...)'

```{autodoc2-docstring} abx_plugin_ytdlp.binaries.FFMPEG_BINARY
```

````
