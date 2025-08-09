#!/usr/bin/env python
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

try:
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()
        long_desc_type = 'text/markdown'
except FileNotFoundError:
    long_description = ''
    long_desc_type = None

setup(
    name='p2_collab_compet',
    version='0.1.0',
    description='Udacity collab compet reinforcement‑learning project',
    long_description=long_description,
    long_description_content_type=long_desc_type,
    url='https://github.com/coder52/p2_collab-compet',
    packages=find_packages(),
    install_requires=install_requires,
    python_requires='~=3.6',
)
