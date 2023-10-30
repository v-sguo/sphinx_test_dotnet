# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ReadTheDocs'
copyright = '2021, v-sguo'
author = 'v-sguo'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx_multiversion',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = [
    "_templates",
]

# html_sidebars = {
#     '**': [
#         'versioning.html',
#     ],
# }

# -- Options for HTML output

# html_theme = 'sphinx_rtd_theme'

html_theme_options = {
  "display_version": False,
  "logo_only": True,
  "style_nav_header_background": "#151033",
}

html_context = {
    'Tags':'Tags'
}