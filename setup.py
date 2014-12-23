#!/usr/bin/env python
#-*- coding: utf-8 -*-

from distutils.util import convert_path
from setuptools import setup

execfile(convert_path('dnspod/version.py'))

setup(
    name='dnspod',
    version=__version__,
    description='a Python library for DNSPod OpenAPI',
    author='Yiwei Li',
    author_email='leeyiw@gmail.com',
    license='Apache',
    url='https://github.com/leeyiw/dnspod',
    packages=['dnspod'],
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
    ],
)
