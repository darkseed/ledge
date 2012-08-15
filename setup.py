#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='ledge',
    version='0.1.0',
    description='Simple serialized persistence for Python dictionaries',
    author='Jamie Matthews',
    author_email='jamie.matthews@gmail.com',
    url='https://github.com/j4mie/ledge',
    license = 'BSD',
    packages=find_packages(),
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
