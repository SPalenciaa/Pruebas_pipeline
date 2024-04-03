from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.global_functions import global_functions
from selenium.common.exceptions import TimeoutException




class Reports_Shortlinks_Page:
    
    def __init__(self, driver): 
        self.driver = driver
        self.global_function = global_functions(self.driver)
        self.wait = WebDriverWait(self.driver, 15)
                 
    def verify_reports_shortlinks_page(self):
        try:
            elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//th[normalize-space()='Link']")))
        except TimeoutException as e:
            print("Error: Page shortlinks_report not found")
            self.global_function.attach_screenshot_to_report()
            raise e
            
    def reports_shortlinks_info(self):
        try:
            elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
            self.wait.until(EC.presence_of_element_located((By.XPATH, "(//td[contains(text(),'PRUEBAS AUTOMATIZADAS')])[1]")))
        except TimeoutException as e:
            print("Error: info not found PRUEBAS AUTOMATIZADAS")
            self.global_function.attach_screenshot_to_report()
            raise e