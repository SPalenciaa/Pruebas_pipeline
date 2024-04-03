import time


from pages.global_functions import global_functions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




class Confirmation_Page_Contacts():
        
    def __init__(self,driver):
        self.driver = driver
        self.global_function = global_functions(self.driver)
        self.wait = WebDriverWait(self.driver, 15)
        
    def verify_list_gropus_page(self):
        try:
            elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Groups/Lists']")))
        except TimeoutException as e:
            print("Error: Page contacts create not found")
            self.global_function.attach_screenshot_to_report(name="redirected_campaigns_menu_error")
            
