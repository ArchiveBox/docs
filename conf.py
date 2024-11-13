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
language = 'en'

# The full version, including alpha/beta/rc tags
release = (Path(__file__).parent.parent / 'pyproject.toml').read_text().split('version = ', 1)[-1].split('\n', 1)[0].strip('"').strip("'")
tag = release

# 0.8.5 -> v0.8.5
if release[0].isdigit():
    tag = f"v{release}".split('rc')[0]

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
]
autodoc2_output_dir = 'apidocs'
autodoc2_render_plugin = "myst"
autodoc2_skip_module_regexes = [
    r'.*migrations.*',
    r'.*vendor.*',
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
    fallback_url = f'https://github.com/search?q=repo%3AArchiveBox%2FArchiveBox%20{info["fullname"]}&type=code'
    if domain != 'py' or not info['module']:
        return fallback_url
    
    # archivebox.crawls.models
    # -> https://github.com/ArchiveBox/ArchiveBox/blob/dev/archivebox/crawls/models.py
    file_path = info['module'].replace('.', '/')
    
    if not file_path.startswith('archivebox/'):
        return fallback_url
    
    # add hotlink to symbol within page content
    symbol_name = str(info['fullname'] or '').rsplit('.', 1)[-1]  # e.g. #:~:text=ArchiveResult

    return f"{github_url}/blob/{tag}/{file_path}.py#:~:text={symbol_name}"
