# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
sys.path.append(str(Path(__file__).parent.parent / 'archivebox'))

# -- Project information -----------------------------------------------------

project = 'ArchiveBox'
copyright = '2024 ©️ ArchiveBox ™️'
author = 'Nick Sweeting'
github_url = 'https://github.com/ArchiveBox/ArchiveBox'
github_doc_root = 'https://github.com/ArchiveBox/docs/tree/master/'
github_view_style = 'blob'
vendor_dir = 'archivebox/pkgs'
language = 'en'

# The full version, including alpha/beta/rc tags
release = (Path(__file__).parent.parent / 'pyproject.toml').read_text().split('version = ', 1)[-1].split('\n', 1)[0].strip('"').strip("'")
tag = release

# 0.8.5 -> v0.8.5
if release[0].isdigit():
    tag = f"v{release}"    # .split('rc')[0]

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.linkcode',
    'sphinx.ext.autosummary',
    # 'sphinx.ext.graphviz',
    # 'sphinx.ext.inheritance_diagram'
    'myst_parser',                       # pip install myst-parser
    'autodoc2',
    # 'recommonmark',
]
autodoc2_packages = [
    {
        "path": "../archivebox",
        "module": "archivebox",
        "exclude_dirs": [
            '__pycache__',
            'migrations',
            'vendor',
            'typings',
            'templates',
            'static',
        ],
        "exclude_files": [
            'tests.py',  
        ],
    },
    # {
    #     "path": "../archivebox/pkgs/abx",
    #     "module": "archivebox.pkgs.abx",
    #     "exclude_dirs": [
    #         '__pycache__',
    #         'migrations',
    #     ],
    # },
]

# add all vendored plugin packages to autodoc2_packages
pkgs_dir = Path(__file__).parent.parent / vendor_dir
vendor_pkgs = {}
for pkg in pkgs_dir.glob("*"):
    if not pkg.is_dir():
        continue
    if not (pkg / 'pyproject.toml').exists():
        continue

    dunder_name = pkg.name.replace('-', '_')                          # abx_plugin_ldap_auth
    if (pkg / dunder_name / '__init__.py').exists():
        # archivebox/pkgs/abx-plugin-ldap-auth/abx_plugin_ldap_auth   (package is in a subdir called package_name)
        path = f'{vendor_dir}/{pkg.name}/{dunder_name}'
        submodule_to_path = lambda submodule, prefix=path: f'{prefix}/{(submodule or "__init__").replace(".", "/")}.py'
    elif (pkg / 'src' / '__init__.py').exists():
        # archivebox/pkgs/abx-plugin-htmltotext/src                   (package is in a subdir called src)
        path = f'{vendor_dir}/{pkg.name}/src'
        submodule_to_path = lambda submodule, prefix=path: f'{prefix}/{(submodule or "__init__").replace(".", "/")}.py'
    elif (pkg / f'{dunder_name}.py').exists():
        # archivebox/pkgs/abx/abx.py                                  (package is all in a single file in the root)
        path = f'{vendor_dir}/{pkg.name}/{dunder_name}.py'
        submodule_to_path = lambda submodule, prefix=path: prefix
    else:
        continue
    
    module_info = {
        "path": f'../{path}',            # ../archivebox/pkgs/abx-plugin-ldap-auth/abx_plugin_ldap_auth
        "module": dunder_name,           # abx_plugin_ldap_auth
        "exclude_dirs": [
            '__pycache__',
            'migrations',
        ],
        "exclude_files": [
            'tests.py',
        ],
    }
    vendor_pkgs[dunder_name] = submodule_to_path
    autodoc2_packages.append(module_info)


autodoc2_output_dir = 'apidocs'
autodoc2_render_plugin = "myst"
autodoc2_skip_module_regexes = [
    r'.*migrations.*',
    r'.*vendor.*',
]
# autodoc2_hidden_objects = ['inherited', 'dunder']
autodoc2_hidden_regexes = [
    r'.*__package__',
]
myst_enable_extensions = ['linkify']     # pip install linkify-it-py

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
master_doc = 'index'
napoleon_google_docstring = True
napoleon_use_param = True
napoleon_use_ivar = False
napoleon_use_rtype = True
napoleon_include_special_with_doc = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    '**/Thumbs.db',
    '**/.DS_Store',
    'data*',
    '**/requirements.txt',
    '**/tests/**',
    '**/templates/**',
    '**/migrations/**',
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_logo = 'logo.png'
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 5,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'version_selector': False,
    'language_selector': False,
    'style_external_links': True,
}
html_context = {
    "display_github": True,
    "github_user": "ArchiveBox",
    "github_repo": "docs",
    "github_version": "master",
    "conf_py_path": "/",
}
html_show_sphinx = False

texinfo_documents = [
    (master_doc, 'archivebox', 'archivebox Documentation', author, 'archivebox', 'The open-source self-hosted internet archive.', 'Miscellaneous'),
]

autodoc_default_flags = ['members']
autodoc_member_order = 'bysource'
autosummary_generate = True

pygments_style = 'sphinx'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

man_pages = [
    (master_doc, 'archivebox', 'archivebox Documentation', [author], 1)
]

def linkcode_resolve(domain, info):
    """
    Calculate link to source code on Github
    Docs: https://www.sphinx-doc.org/en/master/usage/extensions/linkcode.html
    """
    module_name = str(info['module'] or '').replace('archivebox.pkgs.', '')          # abx.binaries
    package_name = module_name.split('.', 1)[0]                                      # abx
    submodule_name = module_name.split(f'{package_name}', 1)[-1].strip('.')          # binaries
    symbol_name = str(info['fullname'] or '')                                        # SomeBinary.INSTALLER_BIN_ABSPATH
    full_name = f'{package_name}.{submodule_name}.{symbol_name}'.replace('..', '.')  # abx.binaries.SomeBinary.INSTALLER_BIN_ABSPATH
    fallback_url = f'https://github.com/search?type=code&q=repo%3AArchiveBox%2FArchiveBox%20{full_name.replace(".", "%20")}'
    
    # 'core.models.Crawl' -> archviebox/core/models.py
    # 'abx.get_all_plugins' -> archivebox/pkgs/abx/abx.py
    # 'abx_plugin_htmltotext.find_plugins_in_dir' -> archivebox/pkgs/abx-plugin-htmltotext/abx_plugin_htmltotext/__init__.py
    # 'abx_plugin_htmltotext.binproviders.PlaywrightBinProvider' -> archivebox/pkgs/abx-plugin-htmltotext/abx_plugin_htmltotext/binproviders.py
    
    if package_name in vendor_pkgs:
        file_path = vendor_pkgs[package_name](submodule_name)                 # archivebox/pkgs/abx/abx.py
    else:
        file_path = f'{package_name}/{submodule_name.replace(".", "/")}.py'   # archivebox/core/models.py
    
    # correct for any extra / or .py
    file_path = file_path.strip('/').strip('.py') + '.py'
    
    # fallback to using Github search instead if URL doesn't look like a valid file path
    if not file_path.startswith('archivebox/'):
        return fallback_url
    if '//' in file_path:
        return fallback_url
    if file_path.count('.py') > 1:
        return fallback_url
    
    # correct for archivebox/cli.py -> archivebox/cli/__init__.py
    init_path = f'{package_name}/{submodule_name.replace(".", "/")}/__init__.py'
    if not Path(f'../{file_path}').is_file():
        if Path(f'../{init_path}').is_file():
            file_path = init_path
        else:
            return fallback_url

    # https://github.com/ArchiveBox/ArchiveBox/blob/v0.8.5/archivebox/core/models.py#archivebox.core.models.Crawl.abid_ts_src#:~:text=abid_ts_src
    return f"{github_url}/{github_view_style}/{tag}/{file_path}#{full_name}#:~:text={symbol_name.rsplit('.', 1)[-1]}"
