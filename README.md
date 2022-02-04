## Code Property Graph
<p align="center">
  <a href="https://github.com/markgacoka/codepropertygraph/blob/main/LICENSE" alt="License"><img align="center" alt="Apache license badge" src="https://img.shields.io/github/license/markgacoka/codepropertygraph?style=flat-square"></a>
  <a href="https://github.com/markgacoka/codepropertygraph/pulse" alt="Stars"><img align="center" alt="Github Stars badge" src="https://img.shields.io/github/stars/markgacoka/codepropertygraph?style=flat-square"></a>
  <a href="https://github.com/markgacoka/codepropertygraph/releases" alt="Release"><img align="center" alt="GitHub release (latest SemVer) badge" src="https://img.shields.io/github/v/release/markgacoka/codepropertygraph?style=flat-square"></a>
  <a href="https://github.com/markgacoka/codepropertygraph/graphs/contributors" alt="Maintained"><img align="center" alt="Maintenance badge" src="https://img.shields.io/maintenance/yes/2022?style=flat-square"></a>
  <a href="https://github.com/markgacoka/codepropertygraph/blob/main/CONTRIBUTING.md" alt="Contributions Welcome"><img align="center" alt="Contributions badge" src="https://img.shields.io/badge/contributions-welcome-blue?style=flat-square"></a>
</p>

<p align="center"><img align="center" alt="Code Property Graph Logo" src="https://raw.githubusercontent.com/markgacoka/codepropertygraph/main/media/cpg.png"></p>

This library is an implementation of a Code Property Graph as seen in the paper published by [Fabian Yamaguchi](https://fabianyamaguchi.com/) on *Modeling and Discovering Vulnerabilities with [Code Property Graphs](https://www.sec.cs.tu-bs.de/pubs/2014-ieeesp.pdf)*

A code property graph is a highly efficient data structure designed to mine large codebases for similar programming patterns. The data structure can be loaded into a graph database where properties of code can be queried. Code property graphs are intended to be code-agnostic and highly scalable making it one of the best choices for code representation.

![Code Property Graph Demo](https://raw.githubusercontent.com/markgacoka/codepropertygraph/main/media/cpg_arrow.png)

## Installation
```
pip install codepropertygraph
```

## Usage
```
from codepropertygraph import CPG

code_cpg = CPG('C:\Users\Gacoka\Projects\portfolio')
code_cpg.files.count
code_cpg.files.l
```

For first time contributors, read the [CONTRIBUTING](https://github.com/markgacoka/codepropertygraph/blob/main/CONTRIBUTING.md) page.
