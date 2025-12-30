from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pizza_hut_final_project.locators import WelcomePageLocators


class WelcomePage():
    def __init__(self, driver):
        self.driver = driver

    def search_for_product(self, product):
        search = self.driver.find_element(*WelcomePageLocators.SEARCH)
        search.clear()
        search.send_keys(product)
        search.send_keys(Keys.ENTER)


    def returning_to_welcome_page(self):
        self.driver.find_element(WelcomePageLocators.RETURN_TO_WELCOME_PAGE).click()



    def click_button_and_get_text(self, text):
        button = self.driver.find_element(By.LINK_TEXT, text)
        button_text = text
        return button_text
