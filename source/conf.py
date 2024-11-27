# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Visual Localization'
copyright = '2024, CyberAgent AI Lab'
author = 'CyberAgent AI Lab'
release = '2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

numfig_format = {
    'code-block': 'ブロック %s',
    'figure': '図 %s',
    'section': 'セクション %s',
    'table': '表 %s',
}

language = 'ja'
latex_engine = 'platex'
latex_docclass = {'manual': 'jsbook'}

math_eqref_format = '式 ({number})'

extensions = []

templates_path = ['_templates']
html_css_files = [
    'css/custom.css',
]

exclude_patterns = []


numfig = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
