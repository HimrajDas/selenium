from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import logging
import time

logging.basicConfig(filename="script_1.log", level=logging.INFO)

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(service=Service(PATH))
driver.get("https://www.python.org")

try:
    assert "Python" in driver.title
except AssertionError:
    logging.info("Doesn't found Python in title")

element = driver.find_element(By.NAME, "q")
element.clear()
element.send_keys("pycon")
element.send_keys(Keys.RETURN)

try:
    assert "No results found." not in driver.page_source
except AssertionError:
    logging.info("something is wrong!")


time.sleep(5)
driver.quit()




