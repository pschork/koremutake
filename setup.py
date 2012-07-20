from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

version = '1.0.5'
short_desc = "Convert to and from Koremutake Memorable Random Strings"
long_desc = """Koremutake is a 128bit MeRS encoding algorithm that can convert any large, 
unsigned number into a memorable sequence of phonetically unique syllables.

For details see http://shorl.com/koremutake.php

To install, run 'sudo easy_install koremutake'

>>> import koremutake
>>> koremutake.encode(10610353957)
'koremutake'
>>> koremutake.decode('koremutake')
10610353957
"""

setup(
    name='koremutake',
    py_modules = ['koremutake'],
    version = version,
    description = short_desc,
    long_description = long_desc,
    keywords = 'koremutake kormutake koremutate kormutate shorl mers tinyurl',
    author = 'Patrick Schork',
    author_email = 'patrick@schork.com',
    maintainer = 'Patrick Schork',
    maintainer_email = 'patrick@schork.com',
    url = 'http://github.com/pschork/koremutake',
    license = 'BSD',
    test_suite = 'koremutake',
    )
