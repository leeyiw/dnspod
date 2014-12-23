#!/usr/bin/env python
#-*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='dnspod',
    version='0.1',
    description='a Python library for DNSPod OpenAPI',
    author='Yiwei Li',
    author_email='leeyiw@gmail.com',
    url='https://github.com/leeyiw/dnspod',
    packages=['dnspod'],
    requires=['requests (>=2.0.0)'],
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
