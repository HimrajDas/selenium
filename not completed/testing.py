from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


logging.basicConfig(filename="testing.log", level=logging.INFO)

try:
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(service=Service(PATH))
    driver.get("https://www.techwithtim.net")
    logging.info(driver.title)
    search = driver.find_element(By.CLASS_NAME, "search-field")
    search.send_keys("test")
    search.send_keys(Keys.RETURN)

    wait = WebDriverWait(driver, 15)

    try:
        main = wait.until(EC.visibility_of_element_located((By.ID, "main")))
        articles = main.find_elements(By.TAG_NAME, "article")
        for article in articles:
            header = article.find_element(By.CLASS_NAME, "entry-summary")
            logging.info(header.text)

        logging.info(main.text)

    except Exception as e:
        logging.info(e)



except Exception as e:
    logging.info(e)




