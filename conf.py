# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
import sys
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import time

sys.path.insert(0, os.path.abspath("."))

# -- Project information -----------------------------------------------------

project = "FT2zXcXvX"
author = "[AUTORZY]"
titlepage = {
    "faculty": "Fizyki i Informatyki Stosowanej",
    "year": "auto",
    "groupID": "[NR GRUPY]",
    "team": "[NR DRUŻYNY]",
    "title": "[TEMAT ĆWICZENIA]",
    "number": "[NUMER ĆWICZENIA]",
    "taskDate": "auto",  # [DATA LABORATORIUM]
    "creationDate": "auto",  # [DATA POWSTANIA SPRAWOZDANIA]
    # [DATA POPRAWKI] - I hope You'll not need that :-)
    "correctionDate": "",
    # nothing to change here
    "author": author,
}

if titlepage["taskDate"] == "auto":
    t = time.localtime()
    titlepage["taskDate"] = (
        str(t.tm_year)
        + "-"
        + "{:02d}".format(t.tm_mon)
        + "-"
        + "{:02d}".format(t.tm_mday)
    )

if titlepage["creationDate"] == "auto":
    t = time.localtime()
    titlepage["creationDate"] = (
        str(t.tm_year)
        + "-"
        + "{:02d}".format(t.tm_mon)
        + "-"
        + "{:02d}".format(t.tm_mday)
    )

if titlepage["year"] == "auto":
    titlepage["year"] = str(time.localtime().tm_year)


# for cloud_sptheme.ext.issue_tracker
issue_tracker_url = "gh:gucio321/fizyka"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.githubpages",
    "sphinxcontrib.images",  # https://github.com/sphinx-contrib/images
    "sphinxcontrib.plot",
    # "cloud_sptheme.ext.issue_tracker",
    "myst_parser",  # ref: https://www.sphinx-doc.org/en/master/usage/markdown.html
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "pl"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "docs",
    "Thumbs.db",
    ".DS_Store",
    "_build",
    "venv",
    "README.md",
    "assets/README.md",
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# more themes: https://sphinx-themes.org/#theme-groundwork-sphinx-theme
html_theme = "cloud"
html_theme_options = {
    "sidebar_localtoc_title": "Spis treści:",
    "sidebar_prev_title": "Poprzednia strona",
    "sidebar_next_title": "Następna strona",
}
html_css_files = ["css/custom.css"]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_logo = "./assets/logo.png"
html_favicon = "./assets/icon.ico"
# TODO: add something better
# html_permalinks_icon=
html_copy_source = False

# for myst_parser (markdown)
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# just helper :-P


def defineLatexVar(varName: str, var: str) -> str:
    if var == None or var == "":
        return ""

    return r"\newcommand{" + varName + r"}{" + var + "}"


latex_additional_files = ["resources/titlepage.cls", "resources/logo_AGH.jpg"]
latex_elements = {
    "papersize": "a4paper",
    "pointsize": "10pt",
    "preamble": r"""
        \newcolumntype{L}{>{\raggedright\arraybackslash}X}
        \ChRuleWidth{0pt}
        \ChNumVar{}
        \let\endtitlepage\relax
        \usepackage{cancel}
        \usepackage{tabularx}
        \usepackage[utf8]{inputenc}
        \usepackage{etoolbox}
        %%\usepackage[margin=3.5cm]{geometry}
        \usepackage{graphicx}
        \usepackage{makecell}
        \usepackage{caption}

        \DeclareCaptionLabelFormat{custom}{#1~\thechapter.#2}
        \captionsetup{labelformat=custom}

        \let\oldsphinxattablestart\sphinxattablestart
        \renewcommand{\sphinxattablestart}{\begin{minipage}{\textwidth}\oldsphinxattablestart}
        \let\oldsphinxattableend\sphinxattableend
        \renewcommand{\sphinxattableend}{\oldsphinxattableend\end{minipage}}

        \newcommand{\sphinxDocumentTitle}{"""
    + titlepage["title"]
    + r"""}
        \newcommand{\sphinxDocumentAuthor}{"""
    + titlepage["author"]
    + r"""}
        \newcommand{\sphinxDocumentGroupID}{"""
    + titlepage["groupID"]
    + r"""}
        \newcommand{\sphinxDocumentFaculty}{"""
    + titlepage["faculty"]
    + r"""}
        \newcommand{\sphinxDocumentTaskDate}{"""
    + titlepage["taskDate"]
    + r"""}
        \newcommand{\sphinxDocumentCreationDate}{"""
    + titlepage["creationDate"]
    + r"""}
        \newcommand{\sphinxDocumentCorrectionDate}{"""
    + titlepage["correctionDate"]
    + r"""}
        """
    + defineLatexVar("\sphinxDocumentTeam", titlepage["team"])
    + r"""
        """
    + defineLatexVar("\sphinxDocumentNumber", titlepage["number"])
    + r"""
        """
    + defineLatexVar("\sphinxDocumentYear", titlepage["year"])
    + r"""


\titlespacing*{\chapter}{-10pt}{10pt}{0pt} % Adjust the values as needed
\titlespacing*{\section}{0pt}{5pt}{0pt} % Adjust the values as needed
        """,
    "maketitle": r"""\input{titlepage.cls}

\titleformat{\chapter}[hang]
  {\normalfont\large\bfseries}{\llap{\thechapter\hskip 8pt}}{0pt}{\large}
\titleformat{\section}
  {\normalfont\large\bfseries}{\thesection\space}{0pt}{\large}
\makeatletter
\patchcmd{\chapter}{\if@openright\cleardoublepage\else\clearpage\fi}{}{}{}
\makeatother

        """,
    "tableofcontents": "",
    "extraclassoptions": "openany,oneside",
}
