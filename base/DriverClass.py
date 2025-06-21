import os

from appium.options.android import UiAutomator2Options
from appium import  webdriver



class Driver:

    def getDriverMethod(self):
        # Dynamically get the root path of the project
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

        # Build full path to the APK file
        app_path = os.path.join(root_dir, 'apps', 'Android_Demo_App.apk')

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['platformVersion'] = '14'
        desired_caps['deviceName'] = 'Test'
        desired_caps['app'] = app_path
        desired_caps['appPackage'] = 'com.code2lead.kwad'
        desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
        desired_caps['fullReset'] = True
        options = UiAutomator2Options().load_capabilities(desired_caps)
        driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

        return driver