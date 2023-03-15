from pythonProject.SeleniumNopCommerceApplication.pageObjects.LoginPage import LoginPage
from pythonProject.SeleniumNopCommerceApplication.utilities.readProperties import ReadConfig
from pythonProject.SeleniumNopCommerceApplication.utilities.customLogger import LogGen
from pythonProject.SeleniumNopCommerceApplication.utilities import XLUtils
import time
import pytest


class Test_002_TDD_Login:
    # Declare variables
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # get logger object
    # path to data file
    path = "C:\\Users\\alex_\\PycharmProjects\\pythonProject\\SeleniumNopCommerceApplication\\TestData\\LoginData.xlsx"
    # list of the test result pass/failed. All test cases must passed
    lst_status = []

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("********* verifying test_login_ddt  ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        # Start work with Excel file. Read number of rows in Excel file
        self.rows = XLUtils.getRowCount(self.path, 'users')
        print("Number of rows", self.rows)

        # Read data from xlsx file row by  row and execute steps for each user

        for r in range(2, self.rows + 1):
            self.username = XLUtils.readData(self.path, 'users', r, 1)
            self.password = XLUtils.readData(self.path, 'users', r, 2)
            self.exp = XLUtils.readData(self.path, 'users', r, 3)

            self.driver.get(self.baseURL)
            self.lp.setUserName(self.username)
            self.lp.setUserPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            # Check point. Verify if test pass or failed
            act_title = self.driver.title  # Get home  page title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Passed ***")
                    self.lp.clickLogout()
                    self.lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*** Failed ***")
                    self.lp.clickLogout()
                    self.lst_status.append("Fail")
            else:
                if self.exp == "Pass":
                    self.logger.info("*** Failed ***")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*** Passed ***")
                    self.lst_status.append("Pass")

        # Verify result of the test
        if "Fail" not in self.lst_status:
            self.logger.info("Login DDT test passed successfully")
            self.driver.close()

            assert True
        else:
            self.logger.info("Login DDT test failed")
            self.driver.close()
            assert False

        self.logger.info("***** test_login_ddt completed *******")
