from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class SearchCustomer:
    # List of Web Elements on Customer page
    customerEmail_xpath = "//input[@id='SearchEmail']"
    searchButton_xpath = "//button[@id='search-customers']"
    customerEmailInTable_xpath = "//tbody/tr/td[2]"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Specify Customer Email
    def specifyCustomerEmail(self, email):
        self.driver.find_element(By.XPATH, self.customerEmail_xpath).send_keys(email)

    # Click Search Button
    def clickSearchButton(self):
        self.driver.find_element(By.XPATH, self.searchButton_xpath).click()

    # Customer search by email result
    def customerSearchByEmailResult(self, email):
        flag = False
        time.sleep(4)
        if self.driver.find_element(By.XPATH, self.customerEmailInTable_xpath).text == email:
            flag = True
        return flag

