# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

import sphinx_material

sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------

project = 'clumio-python-sdk'
copyright = '2021. Clumio, Inc.'
author = 'support@clumio.com'

# The full version, including alpha/beta/rc tags
release = '0.1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    # sphinx_autodoc_typehints must be loaded after sphinx.ext.napoleon.
    'sphinx_autodoc_typehints',
    'sphinx.ext.autosummary',
    'sphinx_material',
]

autodoc_default_flags = ['members']
autosummary_generate = True
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_show_sourcelink = False
html_sidebars = {
    '**': ['logo-text.html', 'globaltoc.html', 'localtoc.html', 'searchbox.html'],
}
html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()
html_theme = 'sphinx_material'
html_theme_options = {
    'repo_url': 'https://github.com/clumio/clumio-python-sdk',
    'repo_name': 'Clumio Python SDK',
    'repo_type': 'github',
    # Set the name of the project to appear in the navigation.
    'nav_title': 'Clumio Python SDK',
    # Set the color and the accent color
    'color_primary': 'blue',
    'color_accent': 'cyan',
    'theme_color': '#2196f3',
    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 3,
    # If False, expand all TOC entries
    'globaltoc_collapse': False,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False,
    'master_doc': False,
    'version_dropdown': True,
    'version_json': '_static/versions.json',
    'table_classes': ['plain'],
    'html_minify': False,
    'html_prettify': True,
}

# html_style = 'css/clumiotheme.css'
html_favicon = 'images/favicon.ico'
html_logo = 'images/clumio-logo-light-on-dark.svg'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
napoleon_google_docstring = True
napoleon_use_param = False
napoleon_use_ivar = False
