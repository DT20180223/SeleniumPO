from pages.register_page import RegisterPage

class RegisterBusiness():
    def __init__(self,driver):
        self.driver = driver
        self.driver.get("http://www.5itest.cn/register")
        self.driver.maximize_window()
        self.register_p = RegisterPage(self.driver)

    def base_reg(self,email,name,password,code):
        try:
            self.register_p.get_email_element().send_keys(email)
            self.register_p.get_name_element().send_keys(name)
            self.register_p.get_password_element().send_keys(password)
            self.register_p.get_code_element().send_keys(code)
            self.register_p.get_register_button().click()
        except Exception:
            self.driver.save_screenshot('1.png')
            return None

    def reg_email_err(self,email,name,password,code):
        self.base_reg(email,name,password,code)
        if self.register_p.get_error_element("email_error"):
            text = self.register_p.get_error_element("email_error").text
        else:
            text = None
        print(text)
        return text

    def reg_name_err(self,email,name,password,code):
        self.base_reg(email,name,password,code)
        if self.register_p.get_error_element("name_error"):
            text = self.register_p.get_error_element("name_error").text
        else:
            text = None
        print(text)
        return text