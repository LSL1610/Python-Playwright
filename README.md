# Python-Playwright
# Playwright Automation Testing with Python

This project is a basic web automation testing framework built using Python, Playwright, and PyTest.  
It is designed to automate common web test scenarios and demonstrate a clean and simple test structure.

## Tech Stack
- Python 3.x
- Playwright
- PyTest

## Project Structure
.
├── conftest.py # PyTest fixtures and test setup
├── locator.py # Web element locators
├── test_run.py # Test execution file
├── pytest.ini # PyTest configuration
├── requirement.txt # Project dependencies
├── init.py
├── .gitignore
└── README.md

## Description
- **conftest.py**: Contains reusable PyTest fixtures such as browser setup and teardown.
- **locator.py**: Stores page locators to separate UI elements from test logic.
- **test_run.py**: Includes test cases for validating web functionalities.
- **pytest.ini**: PyTest configuration (markers, test discovery, options).
- **requirement.txt**: List of required Python packages.

## Test Scope
- Basic web navigation
- UI element interaction
- Functional test scenarios
- Simple validation checks

## How to Run

### 1. Clone the repository
```bash
gh repo clone LSL1610/Python-Playwright
cd Python-Playwright

