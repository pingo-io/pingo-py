#!/usr/bin/env python
# -*- coding: utf-8 -*-
# MIT Licensed. See LICENSE for more information.
""" Pingo setup module """

from setuptools import setup
import io

metadata = {
    "name": "pingo",
    "version": "0.1",
    "author": "Pingo Team @ Garoa Hacker Clube",
    "author_email": "luciano at sign ramalho within the dot org tld",
    "url": "http://github.com/garoa/pingo",
    "description": "Generic API to control boards with programmable IO pins.",
    "license": "MIT",
}

with io.open('README.rst', encoding='utf-8') as readme:
    metadata["long_description"] = readme.read()

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

metadata["packages"] = [metadata["name"]]

setup(**metadata)
