# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import recommonmark                                   # noqa: F401
from recommonmark.transform import AutoStructify

os.environ['USE_CHROME'] = 'False'

import archivebox
from archivebox.config.legacy import setup_django

setup_django()

VERSION = archivebox.VERSION

# -- Project information -----------------------------------------------------

project = 'ArchiveBox'
copyright = '2023 ©️ ArchiveBox ™️'
author = 'Nick Sweeting'
github_url = 'https://github.com/ArchiveBox/ArchiveBox'
github_doc_root = 'https://github.com/ArchiveBox/docs/tree/master/docs/'
language = 'en'

# The full version, including alpha/beta/rc tags
release = VERSION


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'recommonmark',
]

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
    'Thumbs.db',
    '.DS_Store',
    'data',
    'output',
    'templates',
    'tests',
    'migrations',
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
}
html_show_sphinx = False

texinfo_documents = [
    (master_doc, 'archivebox', 'archivebox Documentation',
     author, 'archivebox', 'The open-source self-hosted internet archive.',
     'Miscellaneous'),
]

autodoc_default_flags = ['members']
autodoc_member_order = 'bysource'
extensions += ['sphinx.ext.autosummary',]
autosummary_gerenerate = True

pygments_style = 'sphinx'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


man_pages = [
    (master_doc, 'archivebox', 'archivebox Documentation',
     [author], 1)
]




# At the bottom of conf.py
def setup(app):
    app.add_config_value('recommonmark_config', {
            # 'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Documentation',
            }, True)
    app.add_transform(AutoStructify)
