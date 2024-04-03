import time
from selenium.common.exceptions import TimeoutException
from pages.global_functions import global_functions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.config import settings 

class add_balance_page:

    def __init__(self, driver):
        self.driver = driver
        self.global_function = global_functions(self.driver)
        self.wait = WebDriverWait(self.driver, 15)

    def _wait_for_spinner_to_disappear(self):
        try:
            WebDriverWait(self.driver, 360).until(
                EC.invisibility_of_element_located((By. ID, "spinner_background"))
            )
        except TimeoutException as e:
            self.global_function.attach_screenshot_to_report()
            raise e

    def add_balance_button(self):
        company = settings['company']
        try:
            self._wait_for_spinner_to_disappear()
            self.global_function.click("id", f"add_balance_buttom_{company}")
        except TimeoutException as e:
            self.global_function.attach_screenshot_to_report()
            raise e

    def modal_balance(self, modalBalance):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.ID, "form_in_modal")
                )
            )
            self.global_function.text("id", "form_in_modal_balance", modalBalance)
        except Exception as e:
            self.global_function.attach_screenshot_to_report("form_in_modal_balance_error")
            raise AssertionError(f"Error in form_in_modal_balance: {str(e)}")

    def accept_balance_button(self):
        try:
            self._wait_for_spinner_to_disappear()
            self.global_function.click(
                "css",
                "[data-testid='btnSave']"
            )
        except TimeoutException as e:
            self.global_function.attach_screenshot_to_report()
            raise e

    def confirm_balance_button(self):
        try:
            self.global_function.click("xpath", "//span[normalize-space()='yes']")
        except TimeoutException as e:
            self.global_function.attach_screenshot_to_report()
            raise e

    def confirm_balance_page(self):
        try:
            self._wait_for_spinner_to_disappear()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "(//p[normalize-space()='Company Balance'])[1]"))) 
        except TimeoutException as e:
            self.global_function.attach_screenshot_to_report()
            raise e