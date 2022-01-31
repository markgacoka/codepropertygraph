---
name: Bug report
about: Create a report to help us improve
title: '[BUG] TypeError: can only concatenate str (not "int") to str'
labels: bug
assignees: markgacoka

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Activate conda environment with proposed requirements
   ```
   conda activate base
   pip install -r requirements.txt
   ```
2. Run the CPG library within my Python script
   ```
   #python cpg.py
   cpg = CPG(r'C:/Users/Dominik/code/')
   print(cpg)
   ```
3. Error is reproduced

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Desktop (please complete the following information):**
 - OS: [e.g. iOS]
 - Browser [e.g. chrome, safari]
 - Version [e.g. 22]

**Additional context**
Add any other context about the problem here.
