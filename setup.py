from setuptools import setup

description = \
"""
This package is used to create individual Dublin Core and Macrepo xml records from a given tsv file.
"""

setup (
    name = 'tsv-convert',
    version = '0.1.0',
    url = 'https://github.com/mmccollow/TSV-Convert',
    author = 'Matt McCollow, Nick Ruest',
    author_email = 'mccollo@mcmaster.ca',
    py_modules = ['dublincore'],
    scripts = ['tsv-convert.py'],
    description = description,
    platforms = ['POSIX'],
    test_suite = 'test',
    classifiers = [
      'License :: GPLv2',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'Topic :: System :: Filesystems',
    ],
)  
