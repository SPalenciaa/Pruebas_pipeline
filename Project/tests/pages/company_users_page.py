import time
from pages.global_functions import global_functions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Company_Page_Users:
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


    def verify_users_page(self):
        try:
            self._wait_for_spinner_to_disappear()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div")))
        except TimeoutException as e:
            self.handle_error("Page contacts create not found", "redirected_campaigns_menu_error", e)

    def filter_user(self, username):
        try:
            self._wait_for_spinner_to_disappear()
            self.global_function.text("xpath", "//input[@placeholder='User Name']", username)
        except Exception as e:
            self.handle_error("Error in filter_account", "accounts_filter_error", e)

    def card_user(self, card):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, "//p[normalize-space()='Dayro Moreno Moreno']")))
            self.global_function.element_present("xpath", f"//p[normalize-space()='{card}']")
        except Exception as e:
            self.handle_error("Error in card_account", "accounts_filter_error", e)

    def button_create_user(self):
        try:
            self._wait_for_spinner_to_disappear()
            self.global_function.click("xpath", "//span[normalize-space()='Create']")
        except Exception as e:
            self.handle_error("Error in create_user_button", "accounts_filter_error", e)

    # -------------Formulary------------------ #

    def create_user_screen(self):
        try:
            self.global_function.element_present("id", "form_in_modal")
        except Exception as e:
            self.handle_error("Error in credit_screen", "accounts_filter_error", e)

    def create_user_button(self):#+
        try:
            self._wait_for_spinner_to_disappear()
            self.global_function.click("id", "button_create")
        except Exception as e:
            self.handle_error("Error in user_button", "accounts_filter_error", e)

    def confirm_create(self):
        try:
            self.global_function.click("xpath", "//span[normalize-space()='yes']")
        except Exception as e:
            self.handle_error("Error in credit_button", "accounts_filter_error", e)

    def write_input(self, id, datatext):
        try:
            self.global_function.text("id", id, datatext)
        except Exception as e:
            self.handle_error("Error in write input", "accounts_filter_error", e)

    def select_input(self, selectId, nameselect):
        try:
            self.global_function.click("id", selectId)
            self.global_function.click("xpath", f"//div[contains(text(),'{nameselect}')]")
        except Exception as e:
            self.handle_error("Error in select input", "accounts_filter_error", e)

    def handle_error(self, message, screenshot_name, exception):
        self.global_function.attach_screenshot_to_report(name=screenshot_name)
        error_message = f"Error: {message} - {str(exception)}"
        print(error_message)
        raise AssertionError(error_message)
