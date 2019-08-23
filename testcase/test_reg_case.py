from busines.register_business import RegisterBusiness
from selenium import webdriver
import unittest

class TestSearchPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.register = RegisterBusiness(self.driver)

    def test_reg_email_err(self):
        text = self.register.reg_email_err('34',"user111","1111","33333")
        self.assertEqual(text,'请输入有效的电子邮件地址')


    def test_reg_name_len_err(self):
        text = self.register.reg_name_err('34444@qq.com',"111","111111","33333")
        self.assertEqual(text,'字符长度必须大于等于4，一个中文字算2个字符')

    # def test_reg_name_tpye_err(self):
    #     text = self.register.reg_name_err('34444@qq.com',"_","111111","33333")
    #     self.assertEqual(text,'只支持中文字、英文字母、数字及_ . ·')
    #
    # def test_reg_password_null(self):
    #     text = self.register.reg_email_err('34444@qq.com',"_","","33333")
    #     self.assertEqual(text,'请输入密码')
    def tearDown(self):
        self.driver.quit()