from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from pages.global_functions import global_functions
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from data.config import settings

    
class companies_page:
    
    def __init__(self, driver): 
        self.driver = driver
        self.global_function = global_functions(self.driver)
        self.wait = WebDriverWait(self.driver, 15)
        
    def verify_companies_page(self):
        try:
            elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
            self.wait.until(EC.presence_of_element_located((By.ID, "button_create"))) 
        except TimeoutException:
            print("Page of companies not found")
            self.global_function.attach_screenshot_to_report()
            
            
    def change_rates_buttom(self):
        company = settings['company']
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, f"//p[normalize-space()='{company}']")))
            self.global_function.click("id", f"change_rates__{company}")
        except TimeoutException as e:
            self.global_function.attach_screenshot_to_report()
            raise e
            
    
    
            