from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class AddCustomer:
    driver = None
    # List of Web Elements on Customer page
    linkCustomer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    linkCustomers_menuitem_xpath = "(//p[contains(text(),'Customers')])[2]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    selectVendor_xpath = "//select[@id='VendorId']"
    txtAdminComment_xpath = "//textarea[@id='AdminComment']"
    listboxNewsLettes_xpath = "(//div[@role='listbox'])[1]"
    listItemNewsLetters_xpath = "//li[contains(text(), 'Test Store 2')]"
    listboxCustomerRoles_xpath = "(//div[@role='listbox'])[2]"
    listItemAdministrator_xpath = "//li[contains(text(), 'Administrators')]"
    btnSave_xpath = "//button[@name='save']"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Open Customer Menu
    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.linkCustomer_menu_xpath).click()
        time.sleep(3)

    # Click on Customer menu item
    def clickOnCustomerMenuItem(self):
        list_item = self.driver.find_element(By.XPATH, self.linkCustomers_menuitem_xpath)
        self.driver.execute_script("arguments[0].click();", list_item)

    # Click on 'Add New' button
    def clickOnAddNewButton(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    # Set Email
    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    # Set Password
    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    # Set First Name
    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    # Set Last Name
    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    # Set Gender
    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdFemaleGender_id).click()

    # Set Date of Birth
    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    # Set Company name
    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)

    # Select vendor
    def selectVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.selectVendor_xpath))
        drp.select_by_visible_text(value)

    # Select News Letters
    def selectNewsLetters(self):
        self.driver.find_element(By.XPATH, self.listboxNewsLettes_xpath)
        list_item = self.driver.find_element(By.XPATH, self.listItemNewsLetters_xpath)
        time.sleep(3)
        # list_item.click() does not work here
        # Java Script action
        self.driver.execute_script("arguments[0].click();", list_item)

    # Set Admin Content
    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminComment_xpath).send_keys(content)

    # Save Button click
    def clickOnSaveButton(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()
