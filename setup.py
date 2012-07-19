from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

import os
import koremutake

readme = file(os.path.join(os.path.dirname(__file__), 'README')).readlines()
short_desc = readme[0].strip()
long_desc = "".join(readme[2:])

setup(name='koremutake',
      version = koremutake.__version__,
      description = short_desc,
      packages = ['koremutake'],
      long_description = long_desc,
      keywords = 'koremutake kormutake koremutate kormutate shorl mers tinyurl',
      author = 'Patrick Schork',
      author_email = 'patrick@schork.com',
      maintainer = 'Patrick Schork',
      maintainer_email = 'patrick@schork.com',
      url = 'http://github.com/pschork/koremutake'
      license = 'BSD',
      test_suite = 'test',
    )
