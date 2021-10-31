"""
pip install pep8

pep8 - Python style guide checker
pep8 is a tool to check your Python code against some of the style conventions
in PEP 8.

Features
Plugin architecture: Adding new checks is easy.
Parseable output: Jump to error location in your editor.
Small: Just one Python file, requires only stdlib. You can use just the pep8.py file for this purpose.
Comes with a comprehensive test suite.


Installation
You can install, upgrade, uninstall pep8.py with these commands:

$ pip install pep8
$ pip install --upgrade pep8
$ pip uninstall pep8



There’s also a package for Debian/Ubuntu, but it’s not always the
latest version.

Example usage and output
$ pep8 --first optparse.py
optparse.py:69:11: E401 multiple imports on one line
optparse.py:77:1: E302 expected 2 blank lines, found 1
optparse.py:88:5: E301 expected 1 blank line, found 0
optparse.py:222:34: W602 deprecated form of raising exception
optparse.py:347:31: E211 whitespace before '('
optparse.py:357:17: E201 whitespace after '{'
optparse.py:472:29: E221 multiple spaces before operator
optparse.py:544:21: W601 .has_key() is deprecated, use 'in'

You can also make pep8.py show the source code for each error,
and even the relevant text from PEP 8:

"""