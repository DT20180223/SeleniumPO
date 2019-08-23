from pages.basePage import Page
from selenium.webdriver.common.by import By
class RegisterPage():
    def __init__(self,drive):
        self.driver =drive
        self.fd =Page(drive)
        self.register_email = (By.ID, 'register_email')
        self.register_password = (By.ID, 'register_password')
        self.register_nickname = (By.ID, 'register_nickname')
        self.captcha_code = (By.ID, 'captcha_code')
        self.email_error = (By.ID, 'register_email-error')
        self.nickname_error = (By.ID, 'register_nickname-error')
        self.password_error = (By.ID, 'register_password-error')
        self.code_error = (By.ID, 'captcha_code-error')
        self.register_btn = (By.ID,'register-btn')

    def get_email_element(self):
        try:
            return self.fd.get_element(self.register_email)
        except   Exception:
            self.driver.save_screenshot('1.png')
            return None

    def get_name_element(self):
        return self.fd.get_element(self.register_nickname)

    def get_password_element(self):
        return self.fd.get_element(self.register_password)

    def get_code_element(self):
        return self.fd.get_element(self.captcha_code)

    def get_register_button(self):
        return self.fd.get_element(self.register_btn)

    def get_error_element(self,info):
        if info =="email_error":
            text =self.fd.get_element(self.email_error)
            print(info,text)
            return text
        elif info == "name_error":
            text = self.fd.get_element(self.nickname_error)
            print(info, text)
            return text