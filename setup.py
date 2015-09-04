#!/usr/bin/env python
# encoding: utf-8

"""
    Flask-Token
    ~~~~~~~~~~~

        快速生成API认证令牌
"""
from setuptools import setup


setup(
    name='Flask-Token',
    version='1.0',
    url='https://github.com/neo1218/flask-token',
    license='MIT',
    author='neo1218',
    author_email='neo1218@yeah.net',
    description='快速生成API认证令牌',
    long_description=__doc__,
    py_modules=['flask_token'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'itsdangerous'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

