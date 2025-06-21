from base.DriverClass import Driver
import utilities.CustomLogger as cl
from base.BasePage import BasePage


import unittest
import pytest
from pages.ContactUsFormPage import ContactForm
import utilities.CustomLogger as cl

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class Test_ContactUsForm(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)

    @pytest.mark.order(2)
    def test_enterDataInForm(self):
        self. cf.enterName()
        self.cf.enterEmail()
        self.cf.enterAddress()
        self.cf.enterMNumber()
        self.cf.clickSubmitButton()

    @pytest.mark.order(1)
    def test_opencontactForm(self):
        self.cf.clickContactFormButton()
        self.cf.verifyContactPage()
