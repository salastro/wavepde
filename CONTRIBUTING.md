# Contributing to wavepde

Thank you for your interest in contributing to wavepde! This document outlines
the guidelines for contributing to this project, including code style, code
structure, and general best practices.

## Code Style

To ensure consistency and readability across the codebase, please adhere to the following code style guidelines:

### General Guidelines

1. **Follow PEP 8**: The project follows the PEP 8 style guide for Python code.
   Use an automatic linter like `flake8` or `pylint` to check your code.
2. **Use Type Annotations**: Provide type annotations for function signatures
   and class attributes to improve code clarity and assist with static
analysis.
3. **Docstrings**: Write clear and concise docstrings for all public modules,
   classes, methods, and functions using the [Google style
guide](http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).

## Code Structure

The project employs Object-Oriented Programming (OOP) principles to encapsulate
data and behavior within classes, promoting modularity, reusability, and
maintainability.

### Class Design

- **Encapsulation**: Bundle data (attributes) and methods (functions) within
classes. Keep attributes private unless they need to be accessed directly.
- **Inheritance and Polymorphism**: Use inheritance to create subclasses that
extend the functionality of base classes. Implement polymorphism to allow
subclasses to be used interchangeably with their base classes.
- **Composition**: Construct classes that are composed of other classes,
fostering a "has-a" relationship.
- **Modularity**: Organize the code into modules and packages, each focusing on
a specific aspect of the project.

### Directory Structure

Organize your project files to enhance clarity and maintainability.

```
src/wavepde/
├── __init__.py
├── wave.py  # Contains Wave1D and Wave2D classes
├── plot.py  # Contains animation classes
└── utils.py  # Utility functions, if any
```

### Documentation and Testing

- **Documentation**: Write comprehensive docstrings for all classes and methods.
- **Testing**: Implement unit tests to ensure that your classes and methods
function correctly.

## Contribution Process

1. **Fork the Repository**: Fork the project repository to your own GitHub
   account.
2. **Clone Your Fork**: Clone your forked repository to your local machine.
3. **Create a New Branch**: Create a new branch for your feature or bugfix.
4. **Make Changes**: Implement your changes, adhering to the code style and
   structure guidelines.
5. **Run Tests**: Ensure all tests pass and add new tests as needed.
6. **Commit Changes**: Commit your changes with a clear and concise commit
   message.
7. **Push to GitHub**: Push your branch to your forked repository on GitHub.
8. **Create a Pull Request**: Open a pull request against the main project
   repository.

Thank you for contributing to wavepde! Your efforts help improve the project
for everyone.

---
