import time
import unittest

import self
from cffi.cffi_opcode import CLASS_NAME
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pizza_hut_final_project.pages.welcome_page import WelcomePage
from pizza_hut_final_project.tests.pizza_hut_selenium_base import pizza_hut_selenium_base


class PizzaHutTests (unittest.TestCase):
    def setUp(self):
        self.base = pizza_hut_selenium_base()
        self.driver = self.base.selenium_start_with_url('https://www.pizzahut.com/?msockid=14690bc54ccc666626111db34d256734')
        self.welcome_page=WelcomePage(self.driver)

    def tearDown(self):
        self.base.selenium_stop()



    def test_returning_to_welcome_page(self):
        self.driver.find_element(By.LINK_TEXT,"School lunch").click()
        self.welcome_page.returning_to_welcome_page()
        print('back to welcome page successfully')



    def test_customerservice_buttons_exist(self):
        button_text=self.welcome_page.click_button_and_get_text('Contact us')
        assert button_text == 'Contact us', 'Contact us button text is not as expected'
        print('Contact us button excsits')

        button_text = self.welcome_page.click_button_and_get_text('Restaurants by state')
        assert button_text == 'Restaurants by state', 'Restaurants by state button text is not as expected'
        print('Restaurants by state button excsits')

        button_text = self.welcome_page.click_button_and_get_text('FAQs')
        assert button_text == 'FAQs', 'FAQs button text is not as expected'
        print('FAQs button excsits')

        button_text = self.welcome_page.click_button_and_get_text('Gift cards')
        assert button_text == 'Gift cards', 'Gift cards button text is not as expected'
        print('Gift cards button excsits')

        button_text = self.welcome_page.click_button_and_get_text('Sitemap')
        assert button_text == 'Sitemap', 'Sitemap button text is not as expected'
        print('Sitemap button excsits')

        button_text = self.welcome_page.click_button_and_get_text('Pizza Hut Store Finder')
        assert button_text == 'Pizza Hut Store Finder', 'Pizza Hut Store Finder button text is not as expected'
        print('Pizza Hut Store Finder button excsits')



    def test_empty_shopping_cart(self):
        shopping_cart=self.driver.find_element(By.CLASS_NAME,"css-1h8ch3n")
        text = shopping_cart.text
        counter = text.count("[0]")
        print('Shopping cart is empty')
        assert counter ==0 , "Shopping Cart did not include 0 "



    def test_pizza_menu_button(self):
        time.sleep(3)
        pizza_menu_button=self.driver.find_elements(By.CSS_SELECTOR, 'div >div.css-ug2o6l > a')[1]
        pizza_menu_button_read =pizza_menu_button.text
        assert pizza_menu_button_read=='PIZZA MENU', 'Pizza menu button text is not as expected'
        print('Pizza menu button exsists')



    def test_pizza_menu_url(self):
        self.driver.get('https://www.pizzahut.com/menu/pizza')
        print('correct url to pizza menu')



    def test_finding_store(self):
        carry_out_button=self.driver.find_element(By.CLASS_NAME,'css-1qy7znf')
        time.sleep(4)
        carry_out_button.click()
        location_field=self.driver.find_element(By.ID,"carryout-city-state-zip")
        location_field.send_keys('10001')
        search_button=self.driver.find_elements(By.CSS_SELECTOR,'button[class="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-fullWidth MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-fullWidth css-aoy6ko"]')[0]
        search_button.click()
        right_location=self.driver.find_element(By.CSS_SELECTOR,'div["MuiGrid-root MuiGrid-item css-1wxaqej"]')
        right_location_reading=right_location.text
        assert 'NEW YORK, NY 10011' in right_location_reading, 'location text is not as expected'
        print('location text is as expected')


























