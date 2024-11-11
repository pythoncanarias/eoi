#!/usr/bin/env python3

import sys
import os

sys.path.insert(0, os.path.abspath('.'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.doctest',
    'sphinx.ext.graphviz',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinxcontrib.mermaid',
    'sphinx_copybutton',
    'myst_parser',
]

myst_enable_extensions = [
    "colon_fence",
    ]

language = 'es'

html_theme = 'furo'

# The name of the entry point, without the ".rst" extension.
# By convention this will be "index"
master_doc = "index"

exclude_patterns = [
    '.venv/**',
    'node_modules/**',
    '01-environment/**',
    '02-core/**',
    '03-version-control/**',
    # '04-patterns/**',
    '05-libs/**',
    '06-web/**',
    '07-sys-admin/**',
    '08-desktop-apps/**',
    '09-data-science/**',
    '10-iot/**',
    '11-videogames/**',
    ]

# This values are all used in the generated documentation.
# Usually, the release and version are the same,
# but sometimes we want to have the release have an "rc" tag.

project = "Curso EOI Python en entornos industriales"
copyright = "@ 2024 Python Canarias"
author = "Many"
version = release = "2024.09.17"
