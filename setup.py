#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from typing import Dict

from setuptools import setup  # type: ignore

here = os.path.abspath(os.path.dirname(__file__))

# To update the package version number, edit nanoutils/__version__.py
version: Dict[str, str] = {}
version_path = os.path.join(here, 'nanoutils', '__version__.py')
with open(version_path, encoding='utf-8') as f:
    exec(f.read(), version)

with open('README.rst') as readme_file:
    readme = readme_file.read()

# Requirements for building the documentation
docs_require = [
    'sphinx>=2.1',
    'sphinx_rtd_theme'
]

# Requirements for running tests
tests_require = [
    'assertionlib',
    'pytest>=4.1.0',
    'pytest-cov',
    'pytest-flake8>=1.0.5',
    'pytest-pydocstyle>=2.1',
    'typing-extensions>=3.7.4; python_version<"3.8"',
    'pytest-mypy>=0.6.2'
]

setup(
    name='Nano-Utils',
    version=version['__version__'],
    description='Utility functions used throughout the various nlesc-nano repositories.',
    long_description=f'{readme}\n\n',
    long_description_content_type='text/x-rst',
    author=['B. F. van Beek'],
    author_email='b.f.van.beek@vu.nl',
    url='https://github.com/nlesc-nano/Nano-Utils',
    packages=['nanoutils'],
    package_dir={'nanoutils': 'nanoutils'},
    package_data={'nanoutils': ['*.rst', '*.pyi', 'py.typed']},
    include_package_data=True,
    license='Apache Software License',
    zip_safe=False,
    keywords=[
        'python-3',
        'python-3-6',
        'python-3-7',
        'python-3-8'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
        'Typing :: Typed'
    ],
    python_requires='>=3.6',
    setup_requires=['pytest-runner'],
    tests_require=tests_require,
    extras_require={'doc': docs_require, 'test': tests_require}
)
