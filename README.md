# Project Name: Sila.by Test Automation

## Overview

This is a test automation project for the **Sila.by** e-commerce website. The project uses **Selenium WebDriver** and **pytest** for automating tests of the website's main features, such as product search, adding products to the cart, and completing the order. It is structured to test a user journey for browsing products, selecting filters, adding items to the cart, and filling out the order form.

## Technologies Used
- **Python**: Programming language used for writing test scripts.
- **Selenium WebDriver**: Tool for automating web browsers and interacting with the pages.
- **pytest**: Testing framework for running and managing tests.
- **Page Object Model (POM)**: A design pattern used to model web pages as objects for better maintainability.

## Project Structure

```
sila.by [Test Automation Project]
├── .venv                  # Virtual environment
├── base_page              # Contains base classes for interacting with pages
│   └── base_page.py       # Base Page class for common actions
├── page                   # Contains specific page classes
│   ├── home_page.py       # Home page class
│   ├── making_order_page.py  # Page for the order form
│   ├── product_cart_page.py  # Cart page class
│   └── search_result_page.py # Search result page class
├── tests                  # Test cases
│   └── test_guest_can_to_order_product.py  # Test script for guest product ordering
├── .gitignore             # Git ignore file
├── conftest.py            # Pytest configuration
├── pytest.ini             # Pytest settings file
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

## Features

- **Page Object Model (POM)**: All pages are represented as classes, each responsible for interactions on a specific page.
- **Tests**: A variety of tests have been implemented to simulate user interactions such as:
  - Opening the homepage.
  - Navigating to the search page and applying filters.
  - Adding products to the cart.
  - Filling in the order form with test data.
- **Cookies acceptance**: Automated handling of cookies consent pop-ups.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hello3world/test_sila.by.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Make sure you have **Google Chrome** installed, or change the driver to **Firefox** or **Edge** if needed.

4. Run the tests:
   ```bash
   pytest --maxfail=1 --disable-warnings -v
   ```

## How It Works

### Page Object Model (POM)
Each page of the site is represented by a Python class with methods that define actions and interactions on that page. The base page (`base_page.py`) contains general functions like clicking buttons, filling forms, etc. Each specific page (such as `home_page.py`, `search_result_page.py`) inherits from the base page and extends it with more specific interactions.

### Key Steps in Test:
- **Homepage interaction**: Accept cookies and navigate to product categories.
- **Product selection**: Filter the products based on criteria and add them to the cart.
- **Order form**: Fill out the form with user data for checkout.