#pytest -v -s AppiumFramework/tests/Login.py --alluredir=../AppiumFramework/reports/allureReports
#allure generate ../AppiumFramework/reports/allureReports -o ../AppiumFramework/reports/allureResults --clean
#allure open ../AppiumFramework/reports/allureResults
#allure serve ../AppiumFramework/reports/allureReports
import unittest
import pytest
import utilities.CustomLogger as cl
from base.BasePage import BasePage
from pages.LoginPage import LoginPageTest


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class Test_login(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.gt = LoginPageTest(self.driver)
        self.bp = BasePage(self.driver)

    @pytest.mark.order(5)
    def test_enterDataInEditBox(self):
        self.gt.enterText()
        self.gt.clickOnSubmit()

    @pytest.mark.order(4)
    def test_openLoginScreen(self):
        self.bp.keyCode(4)
        self.gt.clickLoginBotton()
        self.gt.enterEmail()
        self.gt.enterPassword()
        self.gt.clickOnLoginB()
        self.gt.verifyAdminScreen()

    @pytest.mark.order(3)
    def test_loginFailMethod(self):
        cl.allureLogs("App Opened")
        self.gt.clickLoginBotton()
        self.gt.enterEmail()
        self.gt.enterPassword2()
        self.gt.clickOnLoginB()
        self.gt.verifyAdminScreen()
