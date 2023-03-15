from pythonProject.SeleniumNopCommerceApplication.pageObjects.LoginPage import LoginPage
from pythonProject.SeleniumNopCommerceApplication.utilities.readProperties import ReadConfig
from pythonProject.SeleniumNopCommerceApplication.utilities.customLogger import LogGen
import pytest

class Test_001_Login:
    # Declare variables
    baseURL = ReadConfig.getApplicationURL()  # "https://admin-demo.nopcommerce.com/login"
    username = ReadConfig.getuserEmail()  # "admin@Yourstore.com"
    password = ReadConfig.getPassword()  # "admin"
    logger = LogGen.loggen()  # get logger object

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("********* Test_001_Login ***********")
        self.logger.info("********* verifying test_homePageTitle ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title = self.driver.title  # get title of the page
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*********** test_homePageTitle passed **********")
        else:
            self.driver.save_screenshot(
                "C:\\Users\\alex_\\PycharmProjects\\pythonProject\\SeleniumNopCommerceApplication"
                "\\Screenshots\\test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*********** test_homePageTitle failed **********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("********* verifying test_login  ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        ac_title = self.driver.title
        if ac_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*********** test_login passed **********")
        else:
            self.driver.close()
            self.logger.error("*********** test_login failed **********")
            assert False
