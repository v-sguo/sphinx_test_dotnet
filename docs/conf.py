# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ReadTheDocs'
copyright = '2021, v-sguo'
author = 'v-sguo'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
  "sphinx.ext.viewcode",
  "sphinx.ext.autodoc",
  "sphinx.ext.napoleon",
  "sphinx_autodoc_typehints",
  "sphinx.ext.todo",
  "sphinx_fontawesome",
  "sphinx_click.ext",
  # 'sphinx.ext.coverage',
  "sphinx.ext.mathjax",
  "sphinx_multiversion",
  "sphinx_tabs.tabs",
  "sphinx-prompt",
  "sphinx_substitution_extensions",
  "sphinx_togglebutton",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = [
    "_templates",
]

html_sidebars = {
  "**": [
    "about.html",
    "navigation.html",
    "relations.html",  # needs 'show_related': True theme option to display
    "searchbox.html",
    "donate.html",
  ]
}

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# html_theme_options = {
#   "display_version": False,
#   "logo_only": True,
#   "style_nav_header_background": "#151033",
# }

html_context = {
    'Tags':'Tags'
}