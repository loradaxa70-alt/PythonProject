import time
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



driver.get ('https://demo.guru99.com/test/newtours/index.php')



user= driver.find_element(By.ID,'userName')
user.click()
user.clear()
user.send_keys('Lora')
user.send_keys(Keys.ENTER)


driver.close()

