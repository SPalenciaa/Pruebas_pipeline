from selenium.webdriver.common.keys import Keys
from pages.global_functions import global_functions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from data.config import settings

class Company_Page_Balance:
        
    def __init__(self, driver):
        self.driver = driver
        self.global_function = global_functions(self.driver)
        self.wait = WebDriverWait(self.driver, 15)
        
    def _wait_for_spinner_to_disappear(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
        except TimeoutException as e:
            print("Error: Page contacts create not found")
            self.global_function.attach_screenshot_to_report(name="redirected_campaigns_menu_error")
            raise e

    def verify_balance_page(self):
        try:
            self._wait_for_spinner_to_disappear()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Buy Credits'])[1]")))     
        except TimeoutException as e:
            print("Error: Page contacts create not found")
            self.global_function.attach_screenshot_to_report(name="redirected_campaigns_menu_error")
            raise e

    def filter_account(self, account):
        try:
            self._wait_for_spinner_to_disappear()
            self.global_function.text("xpath", "//input[@placeholder='Main account']", account)
        except Exception as e:
            self.global_function.attach_screenshot_to_report(context= self.evidence_path)
            error_message = f"Error in filter_account: Error in filter {str(e)}"
            raise AssertionError(error_message)
        
    def card_account(self, card,context):
        company = settings['company']
        try:
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, f"//p[@class='yp-title'][normalize-space()='{company}']")))
            self.global_function.element_present("xpath", f"//p[normalize-space()='{card}']")    
        except Exception as e:
            self.global_function.attach_screenshot_to_report(context=context.evidence_path)
            error_message = f"Error in card_account: In card account {str(e)}"
            raise AssertionError(error_message)
        
    def asig_credit_button(self):
        try:
            self._wait_for_spinner_to_disappear()
            self.global_function.click("xpath", "//span[normalize-space()='Assign Credit']")
        except Exception as e:
            self.global_function.attach_screenshot_to_report("accounts_filter_error")
            error_message = f"Error in credit_button: In card account {str(e)}"
            raise AssertionError(error_message)
    
    def asig_credit_screen(self):
        try:
            self.global_function.element_present("xpath","(//div[@class='ant-drawer-body'])[1]")
        except Exception as e:
            self.global_function.attach_screenshot_to_report("accounts_filter_error")
            error_message = f"Error in credit_screen: {str(e)}"
            raise AssertionError(error_message)
    
    def allocate_founds_button(self):
        try:
            self._wait_for_spinner_to_disappear()
            self.global_function.click("css","[data-testid='btnSave']")
        except Exception as e:
            self.global_function.attach_screenshot_to_report("accounts_filter_error")
            error_message = f"Error in credit_button: In card account {str(e)}"
            raise AssertionError(error_message)
        
    def select_account(self, account):
        try:
            self.global_function.click("xpath", "(//span[@title='Selected'])[1]")
            self.global_function.click("xpath", f"//div[contains(text(),'{account}')]")
        except Exception as e:
            self.global_function.attach_screenshot_to_report("accounts_filter_error")
            error_message = f"Error in select account: In card account {str(e)}"
            raise AssertionError(error_message)
        
    def input_balance_credit(self, balance):
        try:
            input_element = self.global_function.select_element_xpath("//input[@value='0']")
            input_element.send_keys(Keys.BACKSPACE)
            input_element.send_keys(balance)
        except Exception as e:
            self.global_function.attach_screenshot_to_report("accounts_filter_error")
            error_message = f"Error in select account: In card account {str(e)}"
            raise AssertionError(error_message)
