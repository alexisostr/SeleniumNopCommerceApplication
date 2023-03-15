import random
import string
import time
import pytest

from pythonProject.SeleniumNopCommerceApplication.pageObjects.LoginPage import LoginPage
from pythonProject.SeleniumNopCommerceApplication.utilities.readProperties import ReadConfig
from pythonProject.SeleniumNopCommerceApplication.utilities.customLogger import LogGen
from pythonProject.SeleniumNopCommerceApplication.pageObjects.AddCustomerPage import AddCustomer
from pythonProject.SeleniumNopCommerceApplication.utilities.ReadCustomerData import CustomerData


class Test_003_AddCustomer:
    # Declare variables
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getuserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("********* Test_003_ Add Customer ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        # Create LoginPage instance and login to home page
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login successfully ********")

        # Create AddCustomerPage instance and start add new Customer
        self.logger.info("****** Starting Add Customer test ******")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickOnAddNewButton()

        # Set customer info
        self.logger.info("****** Providing customer info ******")
        self.email = self.random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword(CustomerData.password)
        self.addcust.setFirstName(CustomerData.fname)
        self.addcust.setLastName(CustomerData.lname)
        self.addcust.setGender(CustomerData.gender)
        self.addcust.setDob(CustomerData.dob)  # Format dd/mm/yyyy
        self.addcust.setCompanyName(CustomerData.company)
        self.addcust.setAdminContent(CustomerData.content)
        time.sleep(3)
        self.addcust.clickOnSaveButton()
        # Verify that Customer is added successfully
        page_content = self.driver.page_source
        if page_content.find("The new customer has been added successfully.") != -1:
            self.logger.info("******* New Customer added successfully ********")
            assert True
        else:
            self.driver.save_screenshot(
                "C:\\Users\\alex_\\PycharmProjects\\pythonProject\\SeleniumNopCommerceApplication"
                "\\Screenshots\\test_Add_Customer.png")
            self.logger.info("******* New Customer is not added  ********")
            assert False

        self.logger.info("******* Saving Customer Info ********")

    def random_generator(self, size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))
