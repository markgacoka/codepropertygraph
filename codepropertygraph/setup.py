from setuptools import setup, find_packages
import os

def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()

VERSION = "0.1.0"
DESCRIPTION = "A Python implementation of a Code Property Graph."
LONG_DESCRIPTION = read_file('README.md')

setup(
    name='codepropertygraph',
    version=VERSION,
    license='Apache License 2.0',
    license_files=["LICENSE"],
    author='Gacoka Mbui',
    author_email='markgacoka@gmail.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url="https://github.com/markgacoka/codepropertygraph",
    download_url="https://github.com/markgacoka/codepropertygraph/releases",
    packages=find_packages(),
    install_requires=[
        "neo4j",
        "python-dotenv",
        "pytest"
    ],
    setup_requires=['wheel'],
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
