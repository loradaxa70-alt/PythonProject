

from selenium.webdriver.common.by import By



class SchoolLunchPage():
    def __init__(self, driver):
        self.driver = driver

    def clicking_on_school_lunch_button(self):
        self.driver.find_element(By.LINK_TEXT, "School lunch").click()
