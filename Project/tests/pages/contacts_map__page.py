import time
from pages.global_functions import global_functions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Map_Page_Contacts():
    
    def __init__(self,driver):
        self.driver = driver
        self.global_function = global_functions(self.driver)
        self.wait = WebDriverWait(self.driver, 15)
        
    def verify_list_groups_contacts(self):
        try:
            elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Contacts Preview']")))
        except TimeoutException as e:
            print("Error: Page listmap not found")
            self.global_function.attach_screenshot_to_report()
            
    def select_phone_number(self,MobileNumber):
        try:
            self.global_function.click("xpath", "//div[@class='ant-select ant-select-single ant-select-show-arrow']//div[@class='ant-select-selector']")###
            self.global_function.click("xpath",f"//div[@class='ant-select-item-option-content'][normalize-space()='{MobileNumber}']")
        except TimeoutException as e:
            print(f"Not found {MobileNumber}")
            self.global_function.attach_screenshot_to_report()
            
    def verify_campign_confirmation_page(self):
        try:
            elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
            self.global_function.element_present("xpath", "//p[normalize-space()='MobileNumber']")
        except Exception as e:
            self.global_function.attach_screenshot_to_report()
            raise e
        