import time
from pages.global_functions import global_functions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Templates_History_Page():
    
    def __init__(self,driver):
        self.driver = driver
        self.global_function = global_functions(self.driver)
        self.wait = WebDriverWait(self.driver, 15)
        
    def verify_history_page_templates(self):
        try:
            elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
            self.wait.until(EC.presence_of_element_located((By.XPATH, "(//p[normalize-space()='Template'])[1]")))
        except TimeoutException as e:
            print("Error: Page history_page_template not found")
            self.global_function.attach_screenshot_to_report()
            raise e
        
    def verify_info_template(self,templateName):
        try:
            elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
            self.wait.until(EC.presence_of_element_located((By.XPATH, f"//td[normalize-space()='{templateName}']")))
        except TimeoutException as e:
            print("Error: Page history_page_info_template not found")
            self.global_function.attach_screenshot_to_report()
            raise e
        
    def filter_templates(self,template):
        try:
            elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
            self.global_function.text("xpath", "//input[@placeholder='Template name']", template)
        except Exception as e:
            self.global_function.attach_screenshot_to_report("filter_template_error")
            error_message = f"Error in filter_account:Error in filter {str(e)}"
            raise AssertionError(error_message)
        
    def verify_info_filter(self,templateName):
        try:
            elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
            notcard= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By.XPATH, "//p[normalize-space()='Campanas a los CEOs y Chief']")))
            self.wait.until(EC.presence_of_element_located((By.XPATH, f"//td[normalize-space()='{templateName}']")))     
        except TimeoutException as e:
            print("Error: Page contacts create not found")
            self.global_function.attach_screenshot_to_report(name="redirected_campaigns_menu_error")
            raise e