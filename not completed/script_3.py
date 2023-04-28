from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
logging.basicConfig(filename="scrapper3.log", level=logging.INFO)


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(service=Service(PATH))
driver.get("https://orteil.dashnet.org/cookieclicker/")
try:
    driver.save_screenshot("homepage.png")
    actions = ActionChains(driver)
    driver.implicitly_wait(20)
    lang_eng = driver.find_element(By.ID, "langSelect-EN")
    lang_eng.click()
    # cookie = driver.find_element(By.ID, "bigCookie")
    wait = WebDriverWait(driver, 15)
    cookie = wait.until(EC.element_to_be_clickable((By.ID, "bigCookie")))
    cookie_count = driver.find_element(By.ID, "cookies")
    items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1, -1, -1)]

    actions.click(cookie)
    for i in range(500):
        actions.perform()
        time.sleep(2)

except Exception as e:
    logging.info(e)

finally:
    time.sleep(5)
    driver.quit()






