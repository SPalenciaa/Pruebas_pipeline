from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from pages.global_functions import global_functions
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


    
class admin_menu_page:
    
    def __init__(self, driver): 
        self.driver = driver
        self.global_function = global_functions(self.driver)
        self.wait = WebDriverWait(self.driver, 15)
    
            
    def select_option_admin(self,menu_option):
        try:
            elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By.ID,"spinner_background")))
            self.global_function.click("xpath",f"//a[normalize-space()='{menu_option}']")
        except Exception as e:
            self.global_function.attach_screenshot_to_report()
            raise e
  
    