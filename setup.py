#!/usr/bin/python
from setuptools import setup

description = "Set of random avatars with generator scripts."
docs_file = 'docs.txt'

setup(name='Random Avatar',
    version = '0.01',
    description = description,
    long_description = description,
    author = 'Samuel Colvin',
    license = 'MIT',
    author_email = 'S@muelColvin.com',
    url = 'https://github.com/samuelcolvin/random-avatar',
    install_requires=[
        'avatar-generator==0.0.13',
    ],
)