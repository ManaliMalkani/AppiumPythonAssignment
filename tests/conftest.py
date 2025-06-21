import pytest
import time
import sys
import os
from appium.webdriver.appium_service import AppiumService

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from base.DriverClass import Driver

# Start Appium once for the whole session
@pytest.fixture(scope='session', autouse=True)
def appium_server():
    appium_service = AppiumService()
    appium_service.start()
    print(appium_service.is_running)
    print(appium_service.is_listening)
    if not appium_service.is_running:
        raise RuntimeError("Appium failed to start.")
    yield
    appium_service.stop()
    print(appium_service.is_running)
    print(appium_service.is_listening)

@pytest.fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')

@pytest.fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')
