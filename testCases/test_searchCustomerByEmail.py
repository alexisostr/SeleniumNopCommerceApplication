import random
import string
import time

from pythonProject.SeleniumNopCommerceApplication.pageObjects.LoginPage import LoginPage
from pythonProject.SeleniumNopCommerceApplication.pageObjects.SearchCustomerPage import SearchCustomer
from pythonProject.SeleniumNopCommerceApplication.pageObjects.AddCustomerPage import AddCustomer
from pythonProject.SeleniumNopCommerceApplication.utilities.readProperties import ReadConfig
from pythonProject.SeleniumNopCommerceApplication.utilities.customLogger import LogGen
import pytest


class Test_004_SearchCustomerByEmail:
    # Declare variables
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getuserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("********* Test_004_Search Customer By Email ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        # Create LoginPage instance and login to home page
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login successfully ********")
        # Create AddCustomerPage and SearchCustomerPage instances and search customer by email
        self.logger.info("***** Go to  Customer page  ********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        time.sleep(4)
        self.logger.info("***** Start search customer by email  ********")
        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.specifyCustomerEmail("admin@yourStore.com")
        self.searchcust.clickSearchButton()
        self.logger.info("***** Customer search by email finished ********")
        status = self.searchcust.customerSearchByEmailResult("admin@yourStore.com")
        assert True == status

        self.driver.close()
