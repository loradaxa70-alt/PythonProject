import time
import unittest

import self
from cffi.cffi_opcode import CLASS_NAME
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pizza_hut_final_project.globals import CONTACT_BUTTON, RESTURANTS_BUTTON, FAQS_BUTTON, GIFT_CARDS_BUTTON, \
    SITEMAP_BUTTON, FIND_STORE_BUTTON
from pizza_hut_final_project.locators import PizzaHutTestsLocators
from pizza_hut_final_project.pages.welcome_page import WelcomePage
from pizza_hut_final_project.pages.school_lunch_page import SchoolLunchPage
from pizza_hut_final_project.tests.pizza_hut_selenium_base import pizza_hut_selenium_base



class PizzaHutTests (unittest.TestCase):
    def setUp(self):
        self.base = pizza_hut_selenium_base()
        self.driver = self.base.selenium_start_with_url('https://www.pizzahut.com/?msockid=14690bc54ccc666626111db34d256734')
        self.welcome_page=WelcomePage(self.driver)
        self.school_lunch_page = SchoolLunchPage(self.driver)

    def tearDown(self):
        self.base.selenium_stop()



    def test_returning_to_welcome_page(self):
        self.school_lunch_page.clicking_on_school_lunch_button()
        time.sleep(3)
        self.welcome_page.returning_to_welcome_page()
        print('back to welcome page successfully')



    def test_customerservice_buttons_exist(self):
        button_text=self.welcome_page.click_button_and_get_text(CONTACT_BUTTON)
        assert button_text == 'Contact us', 'Contact us button text is not as expected'
        print('Contact us button exists')

        button_text = self.welcome_page.click_button_and_get_text(RESTURANTS_BUTTON)
        assert button_text == 'Restaurants by state', 'Restaurants by state button text is not as expected'
        print('Restaurants by state button exists')

        button_text = self.welcome_page.click_button_and_get_text(FAQS_BUTTON)
        assert button_text == 'FAQs', 'FAQs button text is not as expected'
        print('FAQs button exists')

        button_text = self.welcome_page.click_button_and_get_text(GIFT_CARDS_BUTTON)
        assert button_text == 'Gift cards', 'Gift cards button text is not as expected'
        print('Gift cards button exists')

        button_text = self.welcome_page.click_button_and_get_text(SITEMAP_BUTTON)
        assert button_text == 'Sitemap', 'Sitemap button text is not as expected'
        print('Sitemap button exists')

        button_text = self.welcome_page.click_button_and_get_text(FIND_STORE_BUTTON)
        assert button_text == 'Pizza Hut Store Finder', 'Pizza Hut Store Finder button text is not as expected'
        print('Pizza Hut Store Finder button exists')



    def test_empty_shopping_cart(self):
        shopping_cart=self.driver.find_element(PizzaHutTestsLocators.SHOPPING_CART)
        text = shopping_cart.text
        counter = text.count("[0]")
        print('Shopping cart is empty')
        assert counter ==0 , "Shopping Cart did not include 0 "



    def test_pizza_menu_button(self):
        time.sleep(3)
        pizza_menu_button=self.driver.find_elements(PizzaHutTestsLocators.PIZZA_MENU)[1]
        pizza_menu_button_read =pizza_menu_button.text
        assert pizza_menu_button_read=='PIZZA MENU', 'Pizza menu button text is not as expected'
        print('Pizza menu button exsists')



    def test_pizza_menu_url(self):
        self.driver.get('https://www.pizzahut.com/menu/pizza')
        print('correct url to pizza menu')



    def test_finding_store(self):
        time.sleep(3)
        carry_out_button=self.driver.find_element(PizzaHutTestsLocators.CARRY_OUT_BUTTON)
        time.sleep(4)
        carry_out_button.click()
        location_field=self.driver.find_element(PizzaHutTestsLocators.LOCATION_FIELD)
        location_field.send_keys('10001')
        search_button=self.driver.find_elements(PizzaHutTestsLocators.SEARCH_BUTTON)[0]
        search_button.click()
        right_location=self.driver.find_element(PizzaHutTestsLocators.RIGHT_LOCATION)
        right_location_reading=right_location.text
        assert 'NEW YORK, NY 10011' in right_location_reading, 'location text is not as expected'
        print('location text is as expected')


























