from selenium.webdriver.common.by import By


class ProductPage():
    def __init__(self,driver):
        self.driver = driver

    def reading_store_location(self,adress):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'NC 27516-2539')
        self.driver.get(adress)










