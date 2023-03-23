from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
logging.basicConfig(filename="scrapper2.log", level=logging.INFO)


PATH = "C:\Program Files (x86)\chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)
driver.get("https://techwithtim.net")

wait = WebDriverWait(driver, 15)


try:
    link = driver.find_element(By.LINK_TEXT, "Python Programming")
    link.click()
    element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials")))
    element.click()
    driver.back()
    driver.back()
    driver.back()
    # driver.forward()

except Exception as e:
    logging.info(e)
    driver.quit()
