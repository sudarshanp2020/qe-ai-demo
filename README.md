# GreenKart Test Automation Framework

This repository contains automated test cases for the GreenKart web application (https://rahulshettyacademy.com/seleniumPractise/#/) using Python and Playwright.

## 🚀 Features

- **Page Object Model (POM)**: Clean and maintainable test structure
- **Comprehensive Test Coverage**: Search, Cart, Checkout, UI, and End-to-End tests
- **Pytest Framework**: Powerful testing framework with fixtures and markers
- **HTML Reports**: Detailed test execution reports
- **Multiple Test Categories**: Smoke, Regression, and UI tests

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/sudarshanp2020/qe-ai-demo.git
cd qe-ai-demo
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:
```bash
playwright install chromium
```

## 📁 Project Structure

```
qe-ai-demo/
├── tests/
│   ├── __init__.py
│   ├── conftest.py              # Pytest fixtures and configuration
│   ├── pages/
│   │   ├── __init__.py
│   │   └── greenkart_page.py    # Page Object Model for GreenKart
│   └── test_greenkart.py        # Test cases
├── reports/                      # Test execution reports (generated)
├── .gitignore
├── pytest.ini                    # Pytest configuration
├── requirements.txt              # Python dependencies
└── README.md
```

## 🧪 Test Categories

### 1. Search Tests (`TestGreenKartSearch`)
- ✅ Search product by name
- ✅ Search with no results
- ✅ Case-insensitive search
- ✅ Clear search functionality

### 2. Cart Tests (`TestGreenKartCart`)
- ✅ Add single product to cart
- ✅ Add multiple products to cart
- ✅ Add product by name
- ✅ Cart icon functionality

### 3. Checkout Tests (`TestGreenKartCheckout`)
- ✅ Proceed to checkout
- ✅ Apply invalid promo code
- ✅ Apply valid promo code
- ✅ Place order button visibility

### 4. UI Tests (`TestGreenKartUI`)
- ✅ Page title verification
- ✅ Search box visibility
- ✅ Product display with images
- ✅ Cart icon visibility
- ✅ Product card elements

### 5. End-to-End Tests (`TestGreenKartEndToEnd`)
- ✅ Complete shopping flow
- ✅ Shopping with promo code

## 🏃 Running Tests

### Run all tests:
```bash
pytest
```

### Run specific test categories:
```bash
# Run smoke tests only
pytest -m smoke

# Run regression tests only
pytest -m regression

# Run UI tests only
pytest -m ui
```

### Run specific test file:
```bash
pytest tests/test_greenkart.py
```

### Run specific test class:
```bash
pytest tests/test_greenkart.py::TestGreenKartSearch
```

### Run specific test method:
```bash
pytest tests/test_greenkart.py::TestGreenKartSearch::test_search_product_by_name
```

### Run with verbose output:
```bash
pytest -v
```

### Run with HTML report:
```bash
pytest --html=reports/report.html --self-contained-html
```

## 📊 Test Reports

After running tests, HTML reports are generated in the `reports/` directory. Open `reports/report.html` in a browser to view detailed test results.

## 🎯 Test Markers

- `@pytest.mark.smoke`: Critical tests that should always pass
- `@pytest.mark.regression`: Comprehensive tests for regression testing
- `@pytest.mark.ui`: UI-specific tests

## 🔧 Configuration

### Browser Configuration
Edit `tests/conftest.py` to modify browser settings:
- `headless=False`: Run with visible browser (set to `True` for headless mode)
- `slow_mo=500`: Slow down operations by 500ms for better visibility
- `viewport`: Set browser window size

### Base URL
The base URL is configured in `tests/conftest.py`:
```python
BASE_URL = "https://rahulshettyacademy.com/seleniumPractise/#/"
```

## 📝 Page Object Model

The `GreenKartPage` class provides methods for interacting with the application:

### Search Methods
- `search_product(product_name)`: Search for products
- `verify_product_displayed(product_name)`: Verify product in results

### Cart Methods
- `add_product_to_cart_by_index(index)`: Add product by index
- `add_product_to_cart_by_name(product_name)`: Add product by name
- `get_cart_count()`: Get number of items in cart
- `open_cart()`: Open cart preview

### Checkout Methods
- `proceed_to_checkout()`: Navigate to checkout
- `apply_promo_code(promo_code)`: Apply promo code
- `get_promo_message()`: Get promo validation message
- `place_order()`: Place the order

## 🐛 Troubleshooting

### Issue: Playwright not found
```bash
pip install playwright
playwright install chromium
```

### Issue: Tests failing due to timeout
Increase timeout in `tests/conftest.py` or individual test methods.

### Issue: Browser not launching
Ensure Playwright browsers are installed:
```bash
playwright install
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-test`)
3. Commit your changes (`git commit -am 'Add new test'`)
4. Push to the branch (`git push origin feature/new-test`)
5. Create a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

Sudarshan Prasad
- GitHub: [@sudarshanp2020](https://github.com/sudarshanp2020)

## 🙏 Acknowledgments

- Test application provided by [Rahul Shetty Academy](https://rahulshettyacademy.com/)
- Built with [Playwright](https://playwright.dev/) and [Pytest](https://pytest.org/)
