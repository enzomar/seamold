# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='{{cookiecutter.project}}',
    version='0.0.1',
    description='{{cookiecutter.description}}',
    long_description=readme,
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.author_email}}',
    license=license,
    packages=find_packages()
)