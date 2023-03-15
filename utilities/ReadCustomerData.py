from pythonProject.SeleniumNopCommerceApplication.utilities import XLUtils


class CustomerData:
    path = "C:\\Users\\alex_\\PycharmProjects\\pythonProject\\SeleniumNopCommerceApplication\\TestData\\CustomerData" \
           ".xlsx"
    password = XLUtils.readData(path, 'customer', 2, 1)
    fname = XLUtils.readData(path, 'customer', 2, 2)
    lname = XLUtils.readData(path, 'customer', 2, 3)
    gender = XLUtils.readData(path, 'customer', 2, 4)
    dob = XLUtils.readData(path, 'customer', 2, 5)
    company = XLUtils.readData(path, 'customer', 2, 6)
    content = XLUtils.readData(path, 'customer', 2, 7)

