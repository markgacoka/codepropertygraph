'''
setup.py - a setup script
Copyright (C) 2022 CySuite
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Author:
    Gacoka Mbui <markgacoka@gmail.com>
'''

from setuptools import setup, find_packages
import codecs
import os

path = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(path, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'A Python implementation of a Code Property Graph.'
LONG_DESCRIPTION = 'A tool for representing code into a code property graph where the syntax, program and data flow can be queried.'

setup(
    name="codepropertygraph",
    version=VERSION,
    license='Apache License 2.0',
    author="Gacoka Mbui",
    author_email="<markgacoka@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[''],
    keywords=['cybersecurity', 'static analysis', 'code tokenization', 'property graph'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ]
)