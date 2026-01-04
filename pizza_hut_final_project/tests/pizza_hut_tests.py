import time
import unittest
from pizza_hut_final_project.globals import CONTACT_BUTTON, RESTURANTS_BUTTON, FAQS_BUTTON, GIFT_CARDS_BUTTON, \
    SITEMAP_BUTTON, FIND_STORE_BUTTON
from pizza_hut_final_project.pages.pizza_menu_page import PizzaMenuPage
from pizza_hut_final_project.pages.welcome_page import WelcomePage
from pizza_hut_final_project.pages.school_lunch_page import SchoolLunchPage
from pizza_hut_final_project.tests.pizza_hut_selenium_base import pizza_hut_selenium_base



class PizzaHutTests (unittest.TestCase):
    def setUp(self):
        self.base = pizza_hut_selenium_base()
        self.driver = self.base.selenium_start_with_url('https://www.pizzahut.com/?msockid=14690bc54ccc666626111db34d256734')
        self.welcome_page=WelcomePage(self.driver)
        self.school_lunch_page = SchoolLunchPage(self.driver)
        self.pizza_menu_page = PizzaMenuPage(self.driver)

    def tearDown(self):
        self.base.selenium_stop()


    def test_returning_to_welcome_page(self):
        self.school_lunch_page.clicking_on_school_lunch_button()
        self.welcome_page.returning_to_welcome_page()
        url= self.driver.current_url
        assert url=='https://www.pizzahut.com/', 'url is incorrect'



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
        counter=self.welcome_page.empty_shopping_cart()
        assert counter == 0, 'Shopping cart text is not as expected'



    def test_pizza_menu_button(self):
        time.sleep(3)
        pizza_menu_text=self.welcome_page.find_pizza_menu_button()
        assert pizza_menu_text == 'PIZZA MENU', 'Pizza menu button text is not as expected'



    def test_pizza_menu_url(self):
        self.pizza_menu_page.enter_pizza_menu_page()
        url = self.driver.current_url
        assert url == 'https://www.pizzahut.com/menu/pizza', 'pizza menu url is not as expected'



    def test_finding_store(self):
        time.sleep(3)
        correct_location_read=self.welcome_page.find_store()
        assert 'NEW YORK, NY 10011' in correct_location_read, 'location text is not as expected'


























