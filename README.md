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

## Continuous Integration (CI)

This project uses **GitHub Actions** to automatically run the automation test suite whenever new code is pushed to the repository.

### CI Status

![CI](https://github.com/<your-username>/<your-repository>/actions/workflows/automation.yml/badge.svg)

The badge above indicates the current status of the automation pipeline.

* 🟢 **Passing** – All automated tests executed successfully
* 🔴 **Failing** – One or more tests failed during execution

### CI Workflow Overview

The CI pipeline performs the following steps automatically:

1. Checkout the repository source code
2. Setup Python environment
3. Install project dependencies
4. Install Playwright browsers
5. Execute automation tests using Pytest

### Workflow Configuration

The CI workflow configuration file is located at:

```id="y7w6p6"
.github/workflows/automation.yml
```

### Test Execution Command

The automation tests are executed using:

```id="mox23n"
pytest -v
```

### When CI Runs

The automation pipeline is triggered when:

* Code is pushed to the `main` branch
* A Pull Request is created or updated

### Purpose

This CI setup ensures that all UI automation tests for the supported platforms (Shopee, Lazada, DemoBlaze, and Food data scraping) are executed automatically to verify that the automation scripts are working correctly after each code change.

