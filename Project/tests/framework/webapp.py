
from data.config import settings 
from pages.global_functions import global_functions
from pages.login_page import LoginPage 

class WebApp:

    def __init__(self, driver):
        self.driver = driver
        self.global_function = global_functions(self.driver)
        self.login_page = LoginPage(self.driver)

    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get(settings['url'])
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
                
    def login(self):
        self.login_page.login()
        
    def login_dev(self):
        self.login_page.login_dev()
        
    def login_admin(self):
        self.login_page.login_admin()
