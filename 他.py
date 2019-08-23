from selenium import webdriver
import time
import unittest

class Test(unittest.TestCase):

    def test1(self):
        driver =webdriver.Chrome()
        driver.get('https://www.imooc.com/')
        time.sleep(2)
        driver.maximize_window()
        driver.find_element_by_class_name('search-input').send_keys('自动化')
        time.sleep(1)
        driver.find_element_by_class_name('showhide-search').click()
        time.sleep(1)
        title = driver.title
        self.assertEqual(title,"自动化_搜索_慕课网")
        driver.quit()

if __name__=="__main__":
    unittest.main()