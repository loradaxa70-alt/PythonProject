import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pizza_hut_final_project.locators import WelcomePageLocators, PizzaHutTestsLocators


class WelcomePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def search_for_product(self, product):
        search = self.driver.find_element(*WelcomePageLocators.SEARCH)
        search.clear()
        search.send_keys(product)
        search.send_keys(Keys.ENTER)


    def returning_to_welcome_page(self):
        find_button=self.driver.find_element(*WelcomePageLocators.RETURN_TO_WELCOME_PAGE)
        find_button.click()
        time.sleep(2)
        print('back to welcome page successfully')
        url = self.driver.current_url
        assert url == 'https://www.pizzahut.com/', 'url is incorrect'
        return url




    def click_button_and_get_text(self, text):
        button = self.driver.find_element(By.LINK_TEXT, text)
        button_text = button.text
        return button_text


    def find_pizza_menu_button(self):
        pizza_menu_button=self.driver.find_elements(*PizzaHutTestsLocators.PIZZA_MENU)[1]
        pizza_menu_button_read=pizza_menu_button.text
        print('pizza menu button exists')
        assert pizza_menu_button_read == 'PIZZA MENU', 'Pizza menu button text is not as expected'
        return pizza_menu_button_read


    def find_store(self):
        carry_out_button = self.driver.find_element(*PizzaHutTestsLocators.CARRY_OUT_BUTTON)
        time.sleep(4)
        carry_out_button.click()
        location_field = self.driver.find_element(*PizzaHutTestsLocators.LOCATION_FIELD)
        location_field.send_keys('10001')
        search_button = self.driver.find_elements(*PizzaHutTestsLocators.SEARCH_BUTTON)[0]
        search_button.click()
        correct_location = self.driver.find_element(*PizzaHutTestsLocators.RIGHT_LOCATION)
        correct_location_read = correct_location.text
        print('location text is as expected')
        assert 'NEW YORK, NY 10011' in correct_location_read , 'location text is not as expected'
        return correct_location_read



    def empty_shopping_cart(self):
        shopping_cart = self.driver.find_element(*PizzaHutTestsLocators.SHOPPING_CART)
        text = shopping_cart.text
        counter = text.count("[0]")
        print(f'Shopping cart has {counter} items')
        assert counter == 0, 'Shopping cart text is not as expected'
        return counter


