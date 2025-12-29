import unittest

import self
from cffi.cffi_opcode import CLASS_NAME
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


    def test_pizza_menu(self):
        menu_button=self.driver.find_element(By.LINK_TEXT,"PIZZA MENU")
        menu_button.click()
        cheese_pizza=self.driver.find_element(By.CLASS_NAME,"MuiTypography-root MuiTypography-body1 jss1970 css-dfadvx").text()
        peperoni_pizza=self.driver.find_element(By,CLASS_NAME,"MuiTypography-root MuiTypography-body1 jss3283 css-dfadvx").text()
        if cheese_pizza=='Cheese Pizza' and peperoni_pizza=='Pepperoni Pizza':
            print('pizza menu is valid')


    def test_finding_store(self):
        self.driver.find_element(By.CSS_SELECTOR,"span[class='css-1sji35f']").click()







    # def test_product_search(self):
    #
    #
    #
    # def test_returning_to_welcome_page(self):
    #     self.driver.find_element(By.ID,"utilityNav-registries").click()
    #     self.welcome_page.returning_to_welcome_page()
    #     print('back to welcome page successfully')
    #
    #
    # def test_six_buttons_exsist(self):
    #     button_text=self.welcome_page.click_button_and_get_text('Weekly Ad')
    #     assert button_text == 'Weekly Ad', 'Weekly ad button text is not as expected'
    #     print('Weekly ad button excsits')
    #
    #     button_text = self.welcome_page.click_button_and_get_text('Find Stores')
    #     assert button_text == 'Find Stores', 'Find Stores button text is not as expected'
    #     print('Find Stores button excsits')
    #
    #     button_text = self.welcome_page.click_button_and_get_text('Registry & Wish List')
    #     assert button_text == 'Registry & Wish List', 'Registry & Wish List button text is not as expected'
    #     print('Registry & Wish List button excsits')
    #
    #     button_text = self.welcome_page.click_button_and_get_text('Target Circle 360™')
    #     assert button_text == 'Target Circle 360™', 'Target Circle 360™ button text is not as expected'
    #     print('Target Circle 360™ button excsits')
    #
    #     button_text = self.welcome_page.click_button_and_get_text('Target Circle™ Card')
    #     assert button_text == 'Target Circle™ Card', 'Target Circle™ Card button text is not as expected'
    #     print('Target Circle™ Card button excsits')
    #
    #     button_text = self.welcome_page.click_button_and_get_text('Target Circle™')
    #     assert button_text == 'Target Circle™', 'Target Circle™ button text is not as expected'
    #     print('Target Circle™ button excsits')
    #
    #
    # def test_finding_store(self):
    #     self.driver.find_element(By.ID, "utilityNav-findStores").click()
    #     self.driver.find_element(By.CSS_SELECTOR,"button[class='styles_ndsBaseButton__4Gp2_ styles_md__Lvk4a styles_ndsButton__XOOOH styles_md__Yc3tr styles_outlined__2a7ys']").click()
    #
    #     entering_city_name=self.driver.find_element(By.ID,"city")
    #     entering_city_name.send_keys('NYC')
    #
    #     choose_state=self.driver.find_element(By.ID,'state')
    #     choose_state_as_drop_down = Select(choose_state)
    #     choose_state_as_drop_down.select_by_visible_text('NC')
    #     time.sleep(3)
    #     self.driver.find_element(By.CSS_SELECTOR,'div[class="styles_ndsCol__Bq1x9"]').click()
    #
    #
    #
    #
    # def test_asking_for_help(self):
    #
    #





















