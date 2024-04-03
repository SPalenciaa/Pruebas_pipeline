import time


from pages.global_functions import global_functions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




class List_Group_Page_Contacts():
    
    def __init__(self,driver):
        self.driver = driver
        self.global_function = global_functions(self.driver)
        self.wait = WebDriverWait(self.driver, 15)
    
    def verify_list_groups_page(self):
        try:
            elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
            self.global_function.element_present("xpath", "//p[normalize-space()='Groups']")
        except Exception as e:
            self.global_function.attach_screenshot_to_report("Error=verify_list_groups_page")
            raise e
        
    def search_list_group(self,idsearch):
        try:
            elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
            self.global_function.text("xpath", "//input[@placeholder='Search Group Name']", idsearch)
        except Exception as e:
            self.global_function.attach_screenshot_to_report("Error=search_list_group")
            raise e
        
    def verify_filter_search(self,card):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, "//td[normalize-space()='Pruebas Automatizadas']")))
            self.global_function.element_present("xpath", f"(//td[contains(text(),'{card}')])[1]")#####
        except Exception as e:
            self.global_function.attach_screenshot_to_report("accounts_filter_error")
            error_message = f"Error in cardr_account: In card account {str(e)}"
            raise AssertionError(error_message)
        
