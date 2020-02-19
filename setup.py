#!/usr/bin/env python

from setuptools import setup, find_packages

version = '0.1'

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='VideoTime',
    version=version,
    install_requires=requirements,
    author='CLu',
    author_email='mailto:',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='Semantic media search and recommendation',
    test_suite = 'nose.collector',
    entry_points={
        'console_scripts': [
            'videotime = videotime.main:main',
        ]
    }
)

