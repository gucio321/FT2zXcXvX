# DISCLAIMER - THIS IS NOT AN OFFICIAL AGH TEMPLATE

I use it for my personal projects but feel free to try it out.

# AGH Sphinx Template

Sphinx project template for Akademia Górniczo-Hutnicza im. Stanisława Staszica documents.

## Usage

1. Clone this repository or create your own from the template.
2. Edit conf.py and/or other files (I'll put list here). The variables you may want to use are on top of `conf.py` (title/author, e.t.c.)
3. (Only first time) Generate virtual enviroument `python3 -m virtualenv venv` and activate it `source venv/bin/activate`
4. Edit `index.md` and/or other files
5. Use makefile to generate project (`make html` / `make latxpdf`)

<details><summary>Pre requirements on Fedora</summary>

On fedora you need to install this:

```sh
dnf install -y latexmk texlive-cmap texlive-collection-fontsrecommended texlive-fncychap texlive-wrapfig texlive-capt-of texlive-framed texlive-upquote texlive-needspace texlive-tabulary texlive-parskip texlive-oberdiek texlive-cancel texlive-hyphen-polish texlive-pict2e texlive-ellipse.noarch
```

I'm not sure about other OS - Let me know if you find it out!

</details>

Available technologies:
- Markdown files support
- Latex formulas
- Plots [check here for more info](https://pypi.org/project/sphinxcontrib-plot/)

## Resources

- [AGH - WFIiS Title Pag template](https://www.overleaf.com/latex/templates/praca-dyplomowa/kbwcrcmczypy)

<details><summary>Investigation about latex customization</summary>

- `latex_logo` could set logo
- `latex_additional_files` works similar to `html_static_path`
- thsi is about figures naming: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-numfig_format

</details>
