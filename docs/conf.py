# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

from recommonmark.parser import CommonMarkParser
from sphinx.builders.html import StandaloneHTMLBuilder
import subprocess, os, sys
import textwrap

# Check if we're running on Read the Docs' servers
read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'

# -- Project information -----------------------------------------------------

project = 'XENSIV TLx5012B Angle Sensor'
copyright = '2024, Infineon Technologies AG'
author = 'Infineon Technologies AG'
release = '2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [

    #'autoapi.extension',
    'sphinx.ext.autodoc',
    'versionwarning.extension',
    'sphinxemoji.sphinxemoji',
    'sphinx_tabs.tabs',
    'sphinx_copybutton',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx_sitemap',
    'sphinx.ext.graphviz',
    'sphinx.ext.inheritance_diagram',
    'myst_parser',
    'breathe',
    'exhale'
]

autosectionlabel_prefix_document = True
# source_parsers = {
#    '.md': 'recommonmark.parser.CommonMarkParser',
# }

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

suppress_warnings = ['autosectionlabel.*', 'epub.duplicated_toc_entry']

# Setup the exhale extension
exhale_args = {
    # These arguments are required
    "containmentFolder":     "./exhale-auto-docs",
    "rootFileName":          "api_list.rst",
    "rootFileTitle":         "API List",
    "doxygenStripFromPath":  "..",
    # Suggested optional arguments
    "createTreeView":        True,
    # TIP: if using the sphinx-bootstrap-theme, you need
    # "treeViewIsBootstrap": True,
    "exhaleExecutesDoxygen": True,
    # "exhaleUseDoxyfile" : True,
    "exhaleDoxygenStdin":    textwrap.dedent('''
        EXTRACT_ALL = YES
        SOURCE_BROWSER = YES
        EXTRACT_STATIC = YES
        OPTIMIZE_OUTPUT_FOR_C  = YES
        INPUT            = ../src
        GENERATE_LATEX   = NO
        GENERATE_HTML    = YES
        GENERATE_XML     = YES
        RECURSIVE        = YES
        VERBATIM_HEADERS = NO
        EXCLUDE          = ./../src/framework/arduino/examples ./../src/framework/arduino/README.md ./../src/framework/wiced-43xxx/README.md
    '''),

    # Configure what not to show in the API index page
    "unabridgedOrphanKinds": {"function", "define", "dir","file", "variable", "namespace"},
    "fullToctreeMaxDepth" : 4
    
}

#autoapi_dirs = ['./../src/']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
primary_domain = 'cpp'
highlight_language = 'c++'
html_logo = 'img/ifx_logo_white_green_s.png'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_templates']
breathe_projects = {
	"XENSIV TLx5012B Angle Sensor": "build/xml/"
}
breathe_default_project = "XENSIV TLx5012B Angle Sensor"
breathe_default_members = ('members', 'undoc-members')

html_css_files = ["custom.css"]