from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from pages.global_functions import global_functions
import time

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.action = global_functions(self.driver)
        self.wait = WebDriverWait(self.driver, 15)

    def _wait_for_spinner_to_disappear(self):
        try:
            self.wait.until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
        except TimeoutException:
            print("El elemento no se pudo encontrar en el tiempo límite de espera.")

    def click_button_campaign(self, locator_type, locator):
        try:
            self._wait_for_spinner_to_disappear()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "(//p[normalize-space()='Total Campaigns Sent'])[1]")))
            self.action.click(locator_type, f"(//a[@class='CompanyHome_dashboard-header-button__2_8LJ'][normalize-space()='{locator}'])[1]")
        except (TimeoutException, NoSuchElementException) as e:
            self.action.attach_screenshot_to_report(name=f"select_option_error_{locator}", wait_time=5)
            raise e

    def click_filters_channels(self, locator_type, channel):
         try:
             self._wait_for_spinner_to_disappear()
             self.wait.until(EC.presence_of_element_located((By.XPATH, "(//p[normalize-space()='Total Campaigns Sent'])[1]")))
             self.action.click(locator_type, f"(//div[contains(text(),'{channel}')])[1]")
         except (TimeoutException, NoSuchElementException) as e:
             self.action.attach_screenshot_to_report(name=f"select_option_error_{channel}", wait_time=5)
             raise e
         
    def verify_change_of_All_button(self):
        try:
            self._wait_for_spinner_to_disappear()
            self.action.click("xpath", "(//div[normalize-space()='All'])[1]")
            self.wait.until(EC.presence_of_element_located((By.XPATH, "(//p[normalize-space()='SMS Use'])[1]")))
            self.wait.until(EC.presence_of_element_located((By.XPATH, "(//p[normalize-space()='VOICE Use'])[1]")))
            self.wait.until(EC.presence_of_element_located((By.XPATH, "(//p[normalize-space()='Use by Account'])[1]")))
        except (TimeoutException, NoSuchElementException) as e:
             self.action.attach_screenshot_to_report(name=f"select_option_error_change_channels", wait_time=5)
             raise e
         
    def verify_change_of_SMS_button(self):
        try:
            self._wait_for_spinner_to_disappear()
            self.action.click("xpath", "(//div[normalize-space()='Sms'])[1]")
            self.wait.until(EC.presence_of_element_located((By.XPATH, "(//p[normalize-space()='SMS Use'])[1]")))
            self.wait.until(EC.invisibility_of_element_located((By. XPATH, "(//p[normalize-space()='VOICE Use'])[1]")))
            self.wait.until(EC.invisibility_of_element_located((By. XPATH, "(//p[normalize-space()='Use by Account'])[1]")))
        except (TimeoutException, NoSuchElementException) as e:
             self.action.attach_screenshot_to_report(name=f"select_option_error_change_channels", wait_time=5)
             raise e
         
    def verify_change_of_VOICE_button(self):
        try:
            self._wait_for_spinner_to_disappear()
            self.action.click("xpath", "(//div[normalize-space()='Voice'])[1]")
            self.wait.until(EC.presence_of_element_located((By.XPATH, "(//p[normalize-space()='VOICE Use'])[1]")))
            self.wait.until(EC.invisibility_of_element_located((By. XPATH, "(//p[normalize-space()='SMS Use'])[1]")))
            self.wait.until(EC.invisibility_of_element_located((By. XPATH, "(//p[normalize-space()='Use by Account'])[1]")))
        except (TimeoutException, NoSuchElementException) as e:
             self.action.attach_screenshot_to_report(name=f"select_option_error_change_channels", wait_time=5)
             raise e
