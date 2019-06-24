#!/usr/bin/env python

from setuptools import setup, find_packages

version = '0.1'

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='VideoTime',
    version=version,
    install_requires=requirements,
    author='Cherie Lu',
    author_email='mailto:luqh1022@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='Semantic media search and recommendation',
    entry_points={
        'console_scripts': [
            'videotime = videotime.main:main',
        ]
    }
)