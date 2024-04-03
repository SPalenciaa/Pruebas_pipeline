import traceback
import time


from pages.global_functions import global_functions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




class custom_message():
    
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
        
    def verify_message_page(self):
        self._wait_for_spinner_to_disappear()
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/section/section/main/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[1]/form/div/div[1]/label")))### Sender ID button to validate the message page
            time.sleep(3)
        except TimeoutException:
            print("Page not found ")
            print(traceback.format_exc())
            self.global_function.attach_screenshot_to_report("error_verify_message_page")

        
    def sender_id(self,sender_id):
        self._wait_for_spinner_to_disappear()
        self.global_function.text("xpath", "//input[@placeholder='Sender Id']", sender_id)
        
    def url_toshortlinks(self,url_shortlinks):
        self._wait_for_spinner_to_disappear()
        self.global_function.text("xpath", "//input[@placeholder='Url']", url_shortlinks)
            
    def create_message(self, click_shortlink=True):
        self._wait_for_spinner_to_disappear()
        self.global_function.select_element_xpath("//div[@id='message-area']")
        textbox = self.global_function.select_element_id("message-area")
    
        message_parts = [
            "Hello ", 
            "//span[normalize-space()='Custom1']", 
            ", your lucky number is ", 
            "//span[normalize-space()='Custom2']", 
            " and your mood is "
        ]
    
        for part in message_parts:
            if "//span" in part:
                try:
                    wildcard = self.global_function.select_element_xpath(part)
                    wildcard.click()
                except:
                    continue
            else:
                textbox.send_keys(part)
        if click_shortlink:
            try:
                self.global_function.click("id","wildcard_shortlinks")
            except:
                pass
        time.sleep(10)

    def verify_message_dynamic(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, "message_dinamic_0")))
        except TimeoutException:
            print("Message not found")
            print(traceback.format_exc())
            self.global_function.attach_screenshot_to_report("error_verify_message_dynamic")
    
    def verify_message_dynamic_VOICE(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Preview']")))
        except TimeoutException:
            print("Message not found")
            print(traceback.format_exc())
            self.global_function.attach_screenshot_to_report("error_verify_message_dynamic")


    def verify_confirmation_page(self):
        try:
            self._wait_for_spinner_to_disappear()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-col']")))
        except TimeoutException:
            print("Page not found")
            print(traceback.format_exc())
            self.global_function.attach_screenshot_to_report("error_verify_confirmation_page")
    
    def number_for_test(self,number):
        try:
            self.global_function.text("id","mobileNumber",number)
        except TimeoutException:
            print("Page not found")
            print(traceback.format_exc())
            self.global_function.attach_screenshot_to_report("error_verify_confirmation_page")
            
    def verify_cost_button(self):
            self._wait_for_spinner_to_disappear()
            self.global_function.click("xpath","//span[normalize-space()='Verify Cost']")
            time.sleep(3)
            
    def send_message_test(self):
        self.global_function.click("xpath","//span[normalize-space()='Send']")
        time.sleep(1)
        self.global_function.click("xpath","(//span[normalize-space()='Yes'])[1]")

              
    def message_cost(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "(//p[normalize-space()='Test SMS Cost'])[1]")))
            self.wait.until(EC.presence_of_element_located((By.XPATH, "(//p[normalize-space()='Test SMS Destination'])[1]")))
        except TimeoutException:
            print("Message cost not found")
            print(traceback.format_exc())
            self.global_function.attach_screenshot_to_report("error_verify_message_dynamic")

    def select_voice(self,voice):
        try:
            self.global_function.click("xpath", "(//span[@class='ant-select-selection-search'])[2]")
            self.global_function.click("xpath", f"//div[contains(text(),'{voice}')]")
        except Exception as e:                  
            self.global_function.attach_screenshot_to_report("select_voice")
            error_message = f"Error in select_voice: In select_voice_bulk {str(e)}"
            raise AssertionError(error_message)
        