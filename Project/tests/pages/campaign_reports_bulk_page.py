import time
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.global_functions import global_functions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException




class Reports_Bulk_Page:
    
    def __init__(self, driver): 
        self.driver = driver
        self.global_function = global_functions(self.driver)
        self.wait = WebDriverWait(self.driver, 15)
        

    def verify_reports_bulk_page(self):
        try:
            elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
            self.wait.until(EC.presence_of_element_located((By.XPATH, "(//p[normalize-space()='Report Name'])[1]")))
        except TimeoutException as e:
            print("Error: Page reports_bulk not found")
            self.global_function.attach_screenshot_to_report()
            raise e