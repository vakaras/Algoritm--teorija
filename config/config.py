#!/usr/bin/python3
{
    # main.tex options
    'use_bibliography': False,
    'extra_packages': [
        ],
    'glossary': False,
    # style.sty options
    # other options
    'template_files': [
        'main.tex',
        'chapters.tex',
        'documentation.cls',
        'lithuanian.lbx',
        'title.sty',
        'global-config.tex',
        'bibliography.bib',
        #'pglossary.py',
        #'pglossary.sty',
        ],
    'concat_files': {
        'style.sty': [
            #'style/old.sty',
            'style/font.sty',
            'style/page.sty',
            'style/paragraph.sty',
            # TODO 'style/table.sty',
            'style/enumeration.sty',
            'style/footnotes.sty',
            'style/chapters.sty',
            'style/toc.sty',
            'style/figures.sty',
            'style/translations.sty',
            'style/bibliography.sty',
            'style/packages.sty',
            'style/math_operators.sty',
            'style/at_operators.sty',
            'style/commands.sty',
            'style/theorems.sty',
            ],
        },
    }
