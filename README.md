# rosalind-python

Solve the http://rosalind.info/problems/locations/ problems and learn about software, testing, collaboration. The problems are difficult. Let's work together to solve them!

## Goal

The goal is to solve all of the ROSALIND problems. We need to write the code to solve the tasks. We also need to write unit tests to make sure the code is functioning correctly.

## Collaboration

The person who writes unit tests for a problem cannot be the same as the person who codes the solution to the problem. Further, the unit tests must be written first! We are practicing [test-driven development](https://en.wikipedia.org/wiki/Test-driven_development).

## Organization

```
problems/
    CountingDnaNucleotides/
        code.py
        prompt.md
        test_code.py
    .../
```

This project is organized so that ROSALIND problems are placed under the problems/ directory. Each problem is named in [CamelCase](https://simple.wikipedia.org/wiki/CamelCase) after the title of the problem on ROSALIND, e.g. CountingDnaNucleotides. Sometimes, the names will be shortened for our convenience.

There are 3 files under each problem directory. prompt.md contains a link to problem on ROSALIND. code.py contains the Python code to solve the problem. test_code.py contains the unit tests to make sure the problem is solved correctly.

## Testing

Unit tests can be run from  the root of the project (the top-level directory for the project) using the following command (install the Python package for pytest and pytest-cov if not already installed):

```bash
# Intallation
# python -m pip install pytest pytest-cov

# Command
python -m pytest
```
