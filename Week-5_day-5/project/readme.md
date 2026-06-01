# Python Fundamentals Project

## Overview

This project demonstrates core Python concepts through five modules:

1. Types Module
2. Data Structures Module
3. OOP Module
4. File Handling Module
5. Generators Module

The project includes comprehensive unit tests using pytest and code coverage reporting.

---

## Project Structure

```text
project/
│
├── src/
│   ├── types_module.py
│   ├── data_structures.py
│   ├── oop_module.py
│   ├── file_handling.py
│   └── generators.py
│
├── tests/
│   ├── test_types.py
│   ├── test_data_structures.py
│   ├── test_oop.py
│   ├── test_file_handling.py
│   └── test_generators.py
│
├── requirements.txt
├── README.md
└── htmlcov/
```

---

## Features

### Types Module

* Add numbers from a list
* Find maximum value
* Safe division
* Value processing and type conversion

### Data Structures Module

* Stack implementation
* Queue implementation
* Push, Pop, Enqueue, Dequeue operations

### OOP Module

* User class
* AdminUser class
* Post class
* Comment class
* Inheritance and object relationships

### File Handling Module

* Write files
* Read files
* Append content to files

### Generators Module

* Count generator
* Fibonacci generator
* Square number generator

---

## Requirements

* Python 3.10+
* pytest
* pytest-cov

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running Tests

Run all tests:

```bash
pytest
```

Run tests with detailed output:

```bash
pytest -v
```

---

## Coverage Report

Generate coverage report:

```bash
pytest --cov=src --cov-report=html
```

After execution, open:

```text
htmlcov/index.html
```

in your browser to view the coverage report.

---

## Test Summary

The project contains:

* 20+ pytest test cases
* Unit tests for all modules
* Coverage reporting using pytest-cov
* Validation of expected outputs and edge cases

---

## Example Commands

Run tests:

```bash
pytest
```

Run coverage:

```bash
pytest --cov=src --cov-report=html
```

Run verbose tests:

```bash
pytest -v
```

---

## Author

Python Fundamentals Project

Created as part of Week 5 Python learning exercises covering:

* Core Python Types
* Data Structures
* Object-Oriented Programming
* File Handling
* Iterators and Generators
* Testing with pytest
