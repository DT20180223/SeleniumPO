from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class Page():
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,loc):
        # 隐形等待10s
        print(loc)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
        element = self.driver.find_element(*loc)
        return element

    def input_text(self,loc,text):
        self.get_element(*loc).send_keys(text)

    def click(self,loc):
        self.get_element(*loc).click()

    def get_title(self):
        return self.driver.title

    def get_element_text(self,loc):
        return  self.get_element(*loc).text

