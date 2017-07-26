# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

setup(
    name='abako',
    version='0.1.0',
    description='Simple reporting tool for your AWS account.',
    author='jakub.jarosz@postpro.net',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'click',
        'jinja2',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        abako-raw=abako.cli:raw_report
    ''',
    zip_safe=False
)

