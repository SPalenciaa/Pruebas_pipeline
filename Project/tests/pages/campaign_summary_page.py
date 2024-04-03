import time


from pages.global_functions import global_functions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




class Reviewdata():
    
    def __init__(self,driver):
        self.driver = driver
        self.global_function = global_functions(self.driver)
        self.wait = WebDriverWait(self.driver, 15)
        
    def verify_summary_page(self):
        try:
            elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-col']")))
        except TimeoutException as e:
            print("Error: Page sumary not found")
            self.global_function.attach_screenshot_to_report(name="redirected_campaigns_menu_error")


    def data(self, campaign_name):
        elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
        data_campaign = self.global_function.select_element_xpath("(//p[normalize-space()='PRUEBAS AUTOMATIZADAS'])[1]").text
        if data_campaign != campaign_name:
            print("Error: Data NOT EQUAL")
            self.global_function.attach_screenshot_to_report(name="redirected_campaigns_menu_error")


    def redirected_campaigns_menu(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-notification-notice-message']")))
        except TimeoutException:
            self.global_function.attach_screenshot_to_report()
            raise Exception("Error: Campaigns menu page not found")


