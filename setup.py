#!/usr/bin/env python

#
# Copyright John Reid 2011, 2012, 2013
#

from setuptools import setup, find_packages
import os


def read(*fnames):
    """
    Utility function to read the README file.
    Used for the long_description.  It's nice, because now 1) we have a top level
    README file and 2) it's easier to type in the README file than to put a raw
    string in below ...
    """
    return open(os.path.join(os.path.dirname(__file__), *fnames)).read()



#
# Call setup
#
setup(
    name             = 'cookbook',
    description      = 'Some useful Python code, mainly from the Python cookbook',
    long_description = read('python', 'cookbook', 'README'),
    version          = read('python', 'cookbook', 'VERSION').strip().split('-')[0],
    author           = 'John Reid',
    author_email     = 'john.reid@mrc-bsu.cam.ac.uk',
    url              = "http://sysbio.mrc-bsu.cam.ac.uk/johns/Cookbook/docs/build/html/",
    classifiers      = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries",
    ],

    packages         = find_packages(where='python'),
    package_dir      = { '' : 'python' },
    package_data     = { 'cookbook': ['README', 'LICENSE', 'VERSION'] },
    install_requires = ['distribute'],
)

