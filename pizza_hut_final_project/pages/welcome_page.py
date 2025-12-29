from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class WelcomePage():
    def __init__(self, driver):
        self.driver = driver

    def search_for_product(self, product):
        search = self.driver.find_element(By.ID, "search")
        search.clear()
        search.send_keys(product)
        search.send_keys(Keys.ENTER)

    def returning_to_welcome_page(self):
        self.driver.find_element(By.CLASS_NAME, "css-2b4rnz").click()

    def click_button_and_get_text(self, text):
        button = self.driver.find_element(By.LINK_TEXT, text)
        button_text = text
        return button_text
