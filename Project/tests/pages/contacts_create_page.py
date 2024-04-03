import time


from pages.global_functions import global_functions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from data.config import settings




class Create_Page_Contacts():
    
    def __init__(self,driver):
        self.driver = driver
        self.global_function = global_functions(self.driver)
        self.wait = WebDriverWait(self.driver, 15)
        
    def verify_create_contacts(self):
        try:
            elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Create List / Group']")))
        except TimeoutException as e:
            print("Error: Page contacts create not found")
            self.global_function.attach_screenshot_to_report(name="redirected_campaigns_menu_error")
    
    def validate_accounts_listGroupName(self,listname):
        try:
            self.global_function.text("id","validate_accounts_listGroupName", listname)
        except Exception as e:
            self.global_function.attach_screenshot_to_report("validate_accounts_listGroupName_error")
            raise AssertionError(f"Error in validate_accounts_listGroupName: {str(e)}")
        
    def accounts(self):
        company = settings['company']
        try:
            self.global_function.click("xpath","//div[@class='ant-select-selection-overflow']")###
            self.global_function.click("xpath",f"//div[contains(text(),'{company}')]")
        except Exception as e:
            self.global_function.attach_screenshot_to_report("accounts_listGroupName_error")
            raise AssertionError(f"Error in accounts_listGroupName: {str(e)}")
        
    def verify_campign_map_page(self):
        try:
            elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
            self.global_function.element_present("xpath", "//p[normalize-space()='Contact Preview']")
        except Exception as e:
            self.global_function.attach_screenshot_to_report("verify_campaign_settings_page_error")
            raise e
        