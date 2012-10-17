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
    entry_points={
        "console_scripts": [
            "vies = pyvies:main",
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2 :: Only",
        "Topic :: Database :: Front-Ends",
        "Topic :: Office/Business :: Financial :: Accounting",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ]
)
