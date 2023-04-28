import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import logging

logging.basicConfig(filename="unittest.log", level=logging.INFO)

PATH = "C:\Program Files (x86)\chromedriver.exe"
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(PATH))


    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.python.org")
        self.assertIn("Python", driver.title)
        element = driver.find_element(By.NAME, "q")
        element.send_keys("pycon")
        element.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)

    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
