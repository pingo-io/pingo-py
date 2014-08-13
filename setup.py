#!/usr/bin/env python
# -*- coding: utf-8 -*-
# MIT Licensed. See LICENSE for more information.
""" Pingo setup module """

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import os
import sys

pkgname = 'pingo'
version = '0.2.0'


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['pingo', '-vrsx']
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


install_requires = [
    '',
]

tests_require = [
    'pytest',
]

metadata = {
    "name": pkgname,
    "version": version,
    "author": "Pingo Team @ Garoa Hacker Clube",
    "author_email": "luciano at sign ramalho within the dot org tld",
    "url": "http://github.com/garoa/pingo",
    "description": "Generic API to control boards with programmable IO pins.",
    "license": "MIT",
    "include_package_data": True,
    "install_requires": install_requires,
    "tests_require": tests_require,
    "cmdclass": {'test': PyTest},
}

readme_path = os.path.join(os.path.dirname(__file__), 'README.rst')

try:
    with io.open(readme_path, encoding='utf-8') as readme:
        metadata["long_description"] = readme.read()
except IOError: # FIXME: how to reliably read the README.rst file in root installs?
    metadata["long_description"] = 'See README.rst'

metadata["classifiers"] = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Console',
    "Environment :: Handhelds/PDA's",
    'Environment :: Other Environment',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: End Users/Desktop',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Manufacturing',
    'Intended Audience :: Other Audience',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Telecommunications Industry',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 2 :: Only',
    'Programming Language :: Python :: Implementation :: CPython',
    'Topic :: Education',
    'Topic :: Home Automation',
    'Topic :: Internet',
    'Topic :: Other/Nonlisted Topic',
    'Topic :: Software Development',
    'Topic :: Software Development :: Embedded Systems',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

metadata["packages"] = find_packages(where='.')

setup(**metadata)

# Upload to PyPI:
# python setup.py sdist upload -r PyPI
