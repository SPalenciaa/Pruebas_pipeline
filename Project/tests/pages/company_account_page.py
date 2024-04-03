import time


from pages.global_functions import global_functions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




class Company_Page_Account():
        
    def __init__(self,driver):
        self.driver = driver
        self.global_function = global_functions(self.driver)
        self.wait = WebDriverWait(self.driver, 15)
        
    def verify_account_page(self):
        try:
            elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
            self.wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Company Accounts')])[1]")))     
        except TimeoutException as e:
            print("Error: Page contacts create not found")
            self.global_function.attach_screenshot_to_report(name="redirected_campaigns_menu_error")
            raise e
        
    def click_specific_account(self,account):
        try:
            elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
            self.global_function.click("xpath",account)    
        except TimeoutException as e:
            print("Error: Page contacts create not found")
            self.global_function.attach_screenshot_to_report(name="redirected_campaigns_menu_error")
            raise e 
        
    def verify_company_change(self,company):
        try:
            elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
            self.wait.until(EC.presence_of_element_located((By.XPATH, f"//p[normalize-space()='Balance in {company} Account'][1]")))
        except (TimeoutException) as e:
             self.action.attach_screenshot_to_report(name=f"select_option_error_change_channels", wait_time=5)
             raise e