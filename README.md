# Appium UI Automation Framework – React Native Shopping App

## 📋 Overview

This framework is built to automate end-to-end user flows on a React Native shopping app using **Python**, **Appium**, and **Pytest**. It supports structured reporting, screenshots on failure, and easy extensibility.

---

## 🚀 Features

- Launch & navigate app on Android (via emulator or physical device)
- Automated test coverage of key user flows
- Screenshot capture on test failures
- Pytest + Allure integration
- Modular test structure for scalability

---

## 🧱 Project Structure

```
AppiumPythonFramework/
├── tests/             → All test case files
├── utilities/         → Logging and utilities
├── screenshots/       → Failure screenshots
├── drivers/           → Driver setup (if needed)
├── requirements.txt   → Python dependencies
└── README.md          → This file
```

---

## 🧪 Test Cases Covered

- ✅ Launch the app
- ✅ Navigate to Contact Form
- ✅ Enter data in Contact Form
- ✅ Login screen invalid login
- 🚧 (To be extended for Product Listing, Add to Cart, Checkout)

---

## ⚙️ Setup Instructions

### 1. 📦 Install Dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

pip install -r requirements.txt
```

### 2. 📱 Environment Requirements

- Appium (v2+):
  ```bash
  npm install -g appium
  appium driver install uiautomator2
  ```

- Node.js (LTS)
- Android SDK and Emulator or physical device
- Python 3.8+

---

## ▶️ Running Tests

### Run all tests:

```bash
pytest -v -s tests/ --alluredir=reports/allureReports
```

### View Allure Report:

```bash
allure generate reports/allureReports -o reports/allureResults --clean
allure open reports/allureResults
```

---

## 📸 Screenshots on Failure

Screenshots are saved automatically to the `/screenshots/` directory when any test fails.

---

## 📄 Author & Contact

Developed by: Manali Malkani  
Assignment: QA Automation Engineer Technical Task
