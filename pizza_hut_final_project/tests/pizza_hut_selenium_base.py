from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class pizza_hut_selenium_base():


    def selenium_start(self):
        print('Test started')
        # service =ChromeService(executable_path=ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(service=service)

    def selenium_start_with_url(self, url):
            print("test start")
            options = Options()
            options.add_argument("--incognito")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            # service = ChromeService(executable_path=ChromeDriverManager().install())
            # self.driver = webdriver.Chrome(service=service)
            self.driver = webdriver.Chrome(options=options)
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            self.driver.get(url)
            return self.driver

    def selenium_stop(self):
        print('Test ended')
        self.driver.close()


    def click_and_assert_on_element (self,element):
        print ("Clicking on element")
        is_selected = element.is_selected()
        if is_selected == False:
            element.click()
        after = element.is_selected()
        assert after == True , "After clicking on element is not as expected"
        return after
