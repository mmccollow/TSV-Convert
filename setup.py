#bootstrap easy_install
import ez_setup
ez_setup.use_setuptools()

  from setuptools import setup, find_packages

description = \
"""
This package is used to create individual Dublin Core and Macrepo xml records from a given tsv file.
"""

install_requires = []
try:
    import DublinCore
    except ImportError:
        install_requires.append('dublincore>=1.0')

setup (
    name = 'tsv-convert',
    version = '0.1.0',
    url = 'https://github.com/mmccollow/TSV-Convert',
    author = 'Matt McCollow, Nick Ruest',
    author_email = 'mccollo@mcmaster.ca',
    py_modules = ['DublinCore', 'ez_setup'],
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
