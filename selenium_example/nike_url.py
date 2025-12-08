from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

print("Test start")
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://www.nike.com/il/')
find_a_store_link=driver.find_element(By.LINK_TEXT,"Find a Store")
find_a_store_link.click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Find a Store").click()

url = driver.current_url
print(url)

if (url == 'https://www.nike.com/il/retail'):
    print ("Test OK -URL as expected")

else:
    print ("#####Test FAILED -URL not as expected######")



driver.close()