### Installation
To install the repository, you need to clone it and run it inside a virtual environment. Running `main.py` generates a Code Property Graph of the simple addition script inside `examples/` and saves it to `output/`.
```
git clone https://github.com/markgacoka/codepropertygraph.git
cd codepropertygraph

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the Application
```
python main.py
```

## Testing
Run all tests
```
pytest tests
```

## Updating Library

1. Change the version number
```
--> VERSION="0.0.9"
DESCRIPTION="A Python implementation of a Code Property Graph."
LONG_DESCRIPTION="A tool for ..."

setup(
    name='codepropertygraph',
    version=VERSION,
```

2. Upload to Pypi
```
python setup.py sdist bdist_wheel
twine upload dist/*
```


For first time contributors, read the [CONTRIBUTING](https://github.com/markgacoka/codepropertygraph/blob/main/CONTRIBUTING.md) page.
