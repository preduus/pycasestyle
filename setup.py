#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='pycasestyle',
    version='{{VERSION_PLACEHOLDER}}',
    keywords=['pycasestyle', 'camelcase', 'snakecase', 'pascal case', 'kebab case', 'dict key case', 'string case'],
    description='A simple python lib to convert string and dict keys to camelcase, pascal case, kebab case and snake case.',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Pedro Rodrigues',
    author_email='pedrota.rodrigues@gmail.com',
    url='https://github.com/preduus/pycasestyle',
    py_modules=['pycasestyle'],
    license='Apache License 2.0',
    zip_safe=False,
    test_suite="tests",
    python_requires='>=3',
    install_requires=['Unidecode==1.3.8', 'pytest==8.0.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)