#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(name='picas',
      version='0.2.6',
      description='Python client using CouchDB as a token pool server.',
      author='Jan Bot',
      author_email='jan.bot@surfsara.nl',
      url='https://github.org/jjbot/picasclient/',
      packages=['picas'],
      install_requires=['couchdb'],
      extras_require={
          'test': ['flake8', 'nose'],
      },
     )