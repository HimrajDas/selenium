from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
import logging
import time

logging.basicConfig(filename="scrap3.log", level=logging.INFO)

PATH = "C:\Program Files (x86)\chromedriver.exe"

service = Service(PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(10)

try:

    cookie = driver.find_element(by=By.ID, value="bigCookie")
    cookie_count = driver.find_element(By.ID, "cookies")
    select_english = driver.find_element(By.ID, "langSelect-EN")
    items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1, -1, -1)]

    AC(driver).move_to_element(select_english).click(select_english).perform()

    for i in range(301):
        AC(driver).move_to_element(cookie).click(cookie).perform()

except Exception as e:
    logging.info(e)
finally:
    driver.quit()



# menu = driver.find_element(By.CSS_SELECTOR, ".nav")
# hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav #submenu1")

# ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()

