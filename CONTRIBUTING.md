# Contributing

When contributing to this repository, please **first discuss the change you wish to make via an issue, email, or any other method with the owners** of this repository before making a change.

### Discussions
You are welcome to suggest improvements via the `Discussions` section and introduce yourself to the community.
To open a new discussion, go to the [Discussions page.](https://github.com/markgacoka/codepropertygraph/discussions)

### Issue
To propose a feature, report a bug or update our documentation, start by opening a new [issue](https://github.com/markgacoka/codepropertygraph/issues).

### Email
To reach out to the main contributors, send an email to:
- **Project Author**: [Gacoka Mbui](mailto:markgacoka@gmail.com)

Additionally, remember that we have a **code of conduct** highlighted below. Please be sure to keep these guidelines in mind.

## Guidelines for contributing
We strive to write idiomatic code that is readable to everyone. Hence, we use the PEP8 standard for spacing, naming conventions,  variable names, comments and so forth. For more information, visit the Official Python docs on [PEP8 standards.](https://www.python.org/dev/peps/pep-0008/)

#### Importation
```python
# Importation - each on its own line
import os
import sys

# Alternative - specific import
from subprocess import Popen, PIPE
```
#### Spacing and Indentation
```python
# Adapted from https://www.python.org/dev/peps/pep-0008/
# Avoid whitespace in between expressions and statements
spam(ham[1], {eggs: 2})

# Hanging indents - also applies to variable definition
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

# Indentation uses four spaces
for i in range(10):
    #[xxxx]do something
    print(i)
```

#### Commenting
```python
# Inline comments - only when necessary
x = x + 1 # Compensate for border

# One-liner docstrings
"""Return the length of the list."""

# Multiline docstring - Google docstrings
# Adapted from https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings

# Script or Module
"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an overall description of the module or program.  Optionally, it may also contain a brief description of exported classes and functions and/or usage examples.

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""

# Class
class SampleClass:
    """Summary of class here.

    Full class description.

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam: bool = False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""

# Function
def sample_function(
    arg_1: file_list,
    arg_2: bool = True) -> List[str]:
    """Summary of function here.

    Full function description.

    Args:
      arg_1:
        A list of file names in the directory.
      arg_2:
        If true, returns all the list elements.

    Returns:
      A list of filenames in the current directory. Each element is represented as a string. For example:

      ['C:/User/Project/a.txt', 'C:/User/Project/b.txt']

    Raises:
      FileNotFoundError: The specified file is not found in the working directory.
    """
```

#### Naming Conventions
1. Non-public methods and instance variables - `_snake_case`
2. Function and variable names - `snake_case`
3. Class names - `CapWords` 
4. Constants - `MAX_OVERFLOW`
5. Always use `self` for the first argument to instance methods.
6. Always use `cls` for the first argument to class methods.
7. A clash with a reserved keyword e.g. `class` should be suffixed with an underscore i.e. `class_`.
8. Use comparison in-built methods i.e. `__eq__, __ne__, __lt__, __le__, __gt__, __ge__`

#### Miscalleneous
1. Shorten code:
    ```python
    # Correct:
    if foo is not None:
    # Wrong:
    if not foo is None:
    ```
2. Mention specific exceptions whenever possible instead of using a bare except: clause: e.g. `except ImportError`
    - Add an `else` statement after and exception to catch all other cases.
3. Use the most appropriate Python method if it exists e.g.
    ```python
    isinstance(obj, int) # if type(obj) is type(1)
    if is_present # if is_present == True
    ```
4. Use type annotations when defining functions e.g. 
    ```python
    def func(a: int) -> List[int]:
        # function code takes in integer, returns integer
    ```

#### Ideal Example
```python
def integer_addition(x: int, y: int) -> int:
	"""Returns the result of two integers added together.
	
    Adds two integers together and returns the sum.

	Args:
		x: an integer to be summed
		y: an integer to be summed
	Returns:
		The integer result after summation.
	Raises:
		TypeError: If both numbers are not integers.
	
	"""
	# try-catch was not used since floating points are accepted.
	if not(isinstance(x, int) and isinstance(y, int)):
		raise TypeError('Both inputs should be integers.')
	else:
		result = x + y
	return result

if __name__ == '__main__':
	a = 1
	b = 2
	result = integer_addition(a, b)
	print(result)
```

## Pull Requests

1. Ensure any install or build dependencies are removed before the end of the layer when doing a build. This is done automatically from the `.gitignore` file, but beware of OS dependent files that should be ignored in the pull request.
2. Update the README.md and version number (if approporiate) with details of changes to the interface, this includes new environment variables, exposed ports, useful file locations and container parameters.
3. Increase the version numbers in any examples files and the README.md to the new version that this 'Pull Request' would represent. The versioning scheme we use is Semantic Versioning. Check out [Semantic Versioning](https://semver.org/) here.
4. You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

### Opening a New Pull Request
For image reference, check the official [Github Docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

```bash
# Clone the Repository to your local machine
git clone https://github.com/markgacoka/codepropertygraph.git

cd codepropertygraph

# Create a new branch. 
    Format: issue_001_description or feature_001_description

    The branch should describe the biggest change.
    The branch should be related to an open tagged issue.

    Example: feature_525_blue-button

git checkout -b new_branch

# Make the changes
# [file] should be the files you wish to change. To add all changes to the staging area, run `git add .`

git status

git add [file]

git commit -m "Explain what the change was (start with a capitalized verb)"

git push origin new_branch
```
Go to the `codepropertygraph` GitHub repository and click on the `Compare & Pull Request` button that pops up and a reviewer will merge the code if appropriate.

## Issues

For image reference, check the official [Github Docs](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue)

The labels we use follow the Github [label](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels) recommendations:
1. `bug`: Indicates an unexpected problem or unintended behavior.
2. `documentation`: Indicates a need for improvements or additions to documentation.
3. `duplicate`:	Indicates similar issues, pull requests, or discussions
4. `enhancement`: Indicates new feature requests
5. `good first issue`: Indicates a good issue for first-time contributors
6. `help wanted`: Indicates that a maintainer wants help on an issue or pull request
7. `invalid`: Indicates that an issue, pull request, or discussion is no longer relevant
8. `question`: Indicates that an issue, pull request, or discussion needs more information
9. `wontfix`: Indicates that work won't continue on an issue, pull request, or discussion

## Code of Conduct
Read our [Code of Conduct](https://github.com/markgacoka/codepropertygraph/blob/main/CODE_OF_CONDUCT.md) before contributing to the project.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant: Version 1.4](http://contributor-covenant.org/version/1/4)
