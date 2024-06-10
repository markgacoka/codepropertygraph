'''
setup.py - a setup script
Copyright (C) 2024 CySuite

Author:
    Gacoka Mbui <markgacoka@gmail.com>
'''

from setuptools import setup, find_packages
import os

def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()

VERSION="0.0.9"
DESCRIPTION="A Python implementation of a Code Property Graph."
LONG_DESCRIPTION="A tool for representing code into a code property graph where the syntax, program and data flow can be queried."

setup(
    name='codepropertygraph',
    version=VERSION,
    license='Apache License 2.0',
    license_files=["LICENSE"],
    author='Gacoka Mbui',
    author_email='<markgacoka@gmail.com>',
    description=DESCRIPTION,
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url="https://github.com/markgacoka/codepropertygraph",
    download_url="https://github.com/markgacoka/codepropertygraph/releases",
    packages=find_packages('codepropertygraph'),
    install_requires=[''],
    build_requires=['python3-pbr'],
    setup_requires=['wheel'],
    py_modules=['codepropertygraph'],
    python_requires='>=3.9.0',
    keywords='cybersecurity, static analysis, code tokenization, property graph',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Security",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)