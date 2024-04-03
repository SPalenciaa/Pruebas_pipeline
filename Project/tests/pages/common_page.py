import time
from colorama import Fore
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from pages.global_functions import global_functions

class common:

    def __init__(self, driver):
        self.driver = driver
        self.global_function = global_functions(self.driver)

    def _wait_for_spinner_to_disappear(self):
        try:
            WebDriverWait(self.driver, 360).until(
                EC.invisibility_of_element_located((By. ID, "spinner_background"))
            )
        except TimeoutException as e:
            self.global_function.attach_screenshot_to_report()
            raise e

    def next_button(self):
        self._wait_for_spinner_to_disappear()
        self.global_function.click("xpath", "(//span[normalize-space()='Next'])[1]")

    def error_message_matches(self, expected_message, xpath):
        try:
            self._wait_for_spinner_to_disappear()
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            message = element.text
            if message == expected_message:
                return True
            else:
                self.global_function.attach_screenshot_to_report()
                raise AssertionError(f"The message does not match. Expected: '{expected_message}', Actual: '{message}'")
        except TimeoutException as e:
            self.global_function.attach_screenshot_to_report()
            raise e
    
    def click_done_button(self):
        self._wait_for_spinner_to_disappear()
        self.global_function.click("xpath", "//span[normalize-space()='Done']")

    def csv_valid(self, csv):
        try:
            self._wait_for_spinner_to_disappear()
            wait = WebDriverWait(self.driver, 10)
            time.sleep(2)

            # Ejecutar un script de JavaScript para mostrar el elemento oculto
            script = "arguments[0].style.display = 'block';"
            input_field = self.driver.find_element(By.XPATH, "//input[@type='file']")
            self.driver.execute_script(script, input_field)

            # Enviar la ruta del archivo al campo de carga
            input_field.send_keys(csv)

            self.driver.switch_to.window(self.driver.window_handles[0])
        except TimeoutException as e:
            self.global_function.attach_screenshot_to_report()
            raise e

    def select_wildcards(self):
        try:
            self._wait_for_spinner_to_disappear()
            wildcards_list = ['Custom1', 'Custom2']
            self.global_function.click("xpath", "//div[@class='ant-select-selection-overflow']")
            for wildcard in wildcards_list:
                try:
                    self.global_function.click("xpath", f"(//div[@class='ant-select-item-option-content'][normalize-space()='{wildcard}'])[2]")
                except:
                    continue
        except TimeoutException as e:
            self.global_function.attach_screenshot_to_report()
            raise e

    def confirm_campaign(self):
        self.global_function.click("xpath", "//span[normalize-space()='Generate']")

    def click_Company_home(self):
        self._wait_for_spinner_to_disappear()
        self.global_function.click("xpath", "//span[normalize-space()='Company Home']")
