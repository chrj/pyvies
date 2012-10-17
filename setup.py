#!/usr/bin/env python

from distutils.core import setup

setup(
    name='pyvies',
    version='0.1',
    description='A quick Python API for the VIES VAT number validation',
    author='Christian Joergensen',
    author_email='christian@technobabble.dk',
    url='https://bitbucket.org/chrj/pyvies',
    py_modules=["pyvies"],
    install_requires=file("requirements.txt").read(),
)
