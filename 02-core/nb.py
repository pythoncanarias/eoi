#!/usr/bin/env python
'''
Inspired by https://goo.gl/SYWRbM and https://t.ly/8LAeY

Convert a jupyter notebook to slides (html) and apply some changes to default
settings (reveal.js, mathjax, ...)

Usage:
> nb.py <notebook.ipynb>
'''

import fileinput
import re
import shlex
import subprocess
import sys
from pathlib import Path

# list of modifications to be made after generating the html slides
# each tuple has the form: (pattern, replacement) as regex
SETTINGS = [
    (
        r"(Reveal.addEventListener\('slidechanged', setScrollingSlide\);)",
        # next slide with right cursor, previous slide with left cursor
        # source: https://github.com/hakimel/reveal.js#keyboard-bindings
        "Reveal.configure({ keyboard: {37:'prev', 39:'next',} });"
    ),
    (
        r'(MathJax.Hub.Config\({)',
        # show the equation numbers
        'TeX: { equationNumbers: {autoNumber: \"AMS\"} },'
    ),
    (
        r'(http[\S]+/reveal.js/)\d\.\d\.\d',
        # update version of reveal.js
        # https://cdnjs.com/libraries/reveal.js/3.7.0
        '3.7.0'
    )
]


def notebook_to_slides(ipynbfile_path):
    print(f'Converting {ipynbfile_path} to html...')
    notebook_path = Path(ipynbfile_path)
    html_path = notebook_path.parent.joinpath(notebook_path.stem +
                                              '.slides.html')
    cmd = shlex.split(f'jupyter nbconvert {notebook_path} --to slides')
    subprocess.run(cmd)
    return html_path


def change_settings(htmlfile_path):
    print(f'Changing settings of {htmlfile_path}...')
    with fileinput.input(files=htmlfile_path, inplace=True) as f:
        for line in f:
            for setting in SETTINGS:
                pattern, replace = setting
                if re.search(pattern, line):
                    new_line = re.sub(pattern, rf'\g<1>{replace}', line)
                    break
            else:
                new_line = line
            print(new_line, end='')


for file in sys.argv[1:]:
    rendered_html_file = notebook_to_slides(file)
    change_settings(rendered_html_file)
