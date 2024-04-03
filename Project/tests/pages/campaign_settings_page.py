import time
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.global_functions import global_functions
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import TimeoutException



class campaign_settings:
    
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

    def verify_campign_settings_page(self):
        try:
            self._wait_for_spinner_to_disappear()
            self.global_function.element_present("id", "validate_other_Account")
        except Exception as e:
            self.global_function.attach_screenshot_to_report("verify_campaign_settings_page_error")
            raise e
    def company_name_test(self, campaign_name, campaign_Account=None):
        try:
            self.global_function.click("xpath", "//div[@name='Account']//div[@class='ant-select-selector']")
    
            if campaign_Account is not None:
                self.global_function.click("xpath", f"//div[contains(text(), '{campaign_Account}')]")
            else:
                self.global_function.click("xpath", "//div[contains(text(),'QXTL')]")
    
            self.global_function.text("xpath", "//input[@placeholder='Choose a distinguishable name']", campaign_name)
        except Exception as e:
            self.global_function.attach_screenshot_to_report("lets_start_error")
            raise AssertionError(f"Error in company_name_test: {str(e)}")
    

            
    def next_button(self):
        try:
            self.global_function.click("xpath", "//button[contains(text(), 'Next')]")
        except Exception as e:
            self.global_function.attach_screenshot_to_report("next_button_error")
            raise AssertionError(f"Error in next_button: {str(e)}")

        
    def verify_desnitation_page(self):
        
        try:
            self._wait_for_spinner_to_disappear()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-col']")))
            self.global_function.element_present("xpath","//*[@id='root']/section/section/main/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/div/div")
        except Exception as e:
            self.global_function.attach_screenshot_to_report("verify_destination_page_error")
            raise AssertionError(f"Error in verify_destination_page: {str(e)}")
        
    def empty_campaing_name_account(self):
        try:
            self._wait_for_spinner_to_disappear()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Choose a distinguishable name']")))
        except Exception as e:
            self.global_function.attach_screenshot_to_report("empty_campaign_name_account_error")
            raise AssertionError(f"Error in empty_campaign_name_account: {str(e)}")
            
    def error_messages(self, error_message):
        time.sleep(2)
        xpath_list = [
            "/html/body/div[1]/section/section/main/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]",
            "/html/body/div[1]/section/section/main/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/div[1]/div/div[2]/div[2]/div/div/div[1]"
        ]
        for xpath in xpath_list:
            message = self.global_function.select_element_xpath(xpath).text
            if message == error_message:
                return True
        self.global_function.attach_screenshot_to_report()
        raise AssertionError("The message does not match")
    
    
    def send_option(self,option):
        try:
            self.global_function.click("xpath",(f"//input[@value='{option}']"))
        except Exception as e:
            raise AssertionError(f"Error in empty_campaign_name_account: {str(e)}")
        
    def add_phase(self):
        try:  
            self.global_function.click("xpath","//button[@class='ant-btn ant-btn-circle ant-btn-icon-only yp-button-optional']")
        except Exception as e:
            raise AssertionError(f"Error in empty_campaign_name_account: {str(e)}")

    
    def add_percentage(self,percentage):
        try:
            self.global_function.text("xpath", "(//input[@value='0%'])[1]",percentage )
        except Exception as e:
            raise AssertionError(f"Error in empty_campaign_name_account: {str(e)}")
        
    def date_today_phase(self, date_type):
        try:
            if date_type == "tomorrow":
                current_date = datetime.now().date() + timedelta(days=1)
                xpath = "(//input[@placeholder='Select'])[3]"
            else:
                current_date = datetime.now().date()
                xpath = "(//input[@placeholder='Select'])[1]"

            formatted_date = current_date.strftime("%Y-%m-%d")
            self.global_function.click("xpath", xpath)
            element = self.global_function.select_element_xpath(xpath)
            element.send_keys(formatted_date, Keys.ENTER)
        except Exception as e:
            raise AssertionError(f"Error in date_today_phase: {str(e)}")

    def hour_today_phase(self, time):
        try:
            current_time = datetime.now().strftime("%H:%M")
            if time == "tomorrow":
                xpath = "(//input[@placeholder='Select'])[4]"
            else:
                xpath = "(//input[@placeholder='Select'])[2]"
    
            self.global_function.click("xpath", xpath)
            element = self.global_function.select_element_xpath(xpath)
            element.send_keys(current_time, Keys.ENTER)
                
        except Exception as e:
            raise AssertionError(f"Error in hour_today_phase: {str(e)}")
    



