#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
#import markdown
import importlib
import collections
import os
import pkg_resources

ROOT = os.path.abspath(os.path.dirname(__file__))


setup(
    name = 'reservoirpy',
    packages = find_packages(),
    include_package_data=True,
    version = '1.3.8',  # Ideally should be same as your GitHub release tag varsion
    description = 'reservoirpy - A collection of Reservoir Engineering Utilities',
    author = 'Kshitij Soni',
    author_email = 'kshitijsoni@iipe.ac.in',
    url = 'https://github.com/kshitijsoni/reservoirpy',
    keywords = ['restoolbox', 'petroleum', 'reservoir'],
    classifiers = [],
    install_requires=[
        'requests',
        'numpy',
        'scipy',
        'pandas',
        'tabulate',
        'gwr_inversion',
        'mpmath',
        'openpyxl'
    ]
)