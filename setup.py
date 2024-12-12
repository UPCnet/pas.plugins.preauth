# -*- coding: utf-8 -*-
"""
This module contains the setup configuration for the pas.plugins.preauth package.
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    """Utility function to read files"""
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

# Version of the plugin
version = '1.3.dev0'

# Long description from README and HISTORY
long_description = read("README.rst") + "\n" + read(os.path.join("docs", "HISTORY.txt"))

# Test requirements
tests_require = ['zope.testing', 'plone.testing']

setup(
    name='pas.plugins.preauth',
    version=version,
    description="Pre-authentication plugin for Plone PAS",
    long_description=long_description,
    classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='plone pas preauth authentication',
    author='UPCnet Plone Team',
    author_email='plone.team@upcnet.es',
    url='https://github.com/UPCnet/pas.plugins.preauth',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['pas', 'pas.plugins'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.api', 
        'Products.CMFCore',  
        'zope.interface', 
    ],
    tests_require=tests_require,
    extras_require=dict(tests=tests_require),
    test_suite='pas.plugins.preauth.tests.test_docs.test_suite',
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
