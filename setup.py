#!/usr/bin/env python
from setuptools import setup

VERSION = '0.0.1'


test_requirements = [
    'nose>=1.3.7',
    'responses>=0.5.1'
]

install_requires = test_requirements + [
    'requests>=2.4.3',
]

setup(
    name="mondo",
    version=VERSION,
    description="Mondo Banking API Client",
    author=', '.join((
        'Tito Miguel Costa',
        'Simon Vans-Colina <simon@simon.vc>',
    )),
    url="https://github.com/simonvc/mxondo-python",
    packages=["mondo"],
    tests_require=test_requirements,
    install_requires=install_requires,
    license="MIT",
)
