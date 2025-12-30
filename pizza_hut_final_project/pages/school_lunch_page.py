

from selenium.webdriver.common.by import By

from pizza_hut_final_project.locators import SchoolLunchPageLocators


class SchoolLunchPage():
    def __init__(self, driver):
        self.driver = driver

    def clicking_on_school_lunch_button(self):
        self.driver.find_element(*SchoolLunchPageLocators.CLICK_ON_SCHOOL_LUNCH).click()
