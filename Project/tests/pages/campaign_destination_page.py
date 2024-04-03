
import time
import os

from pages.global_functions import global_functions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




class upload_csv():
    
    def __init__(self, driver): 
        self.driver = driver
        self.global_function = global_functions(self.driver)
        self.wait = WebDriverWait(self.driver, 15)
        
    def verify_creation_page(self):
        try:
            elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
        except TimeoutException:
            print("Page of creation not found")
            self.global_function.attach_screenshot_to_report()

    def select_phone_number(self, MobileNumber):
        try:

            self.global_function.click("xpath", "/html/body/div/section/section/main/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div/div[1]/div")###
            self.global_function.click("xpath", f"(//div[@class='ant-select-item-option-content'][normalize-space()='{MobileNumber}'])[1]")
        except TimeoutException:    
            print(f"Not found {MobileNumber}")
            self.global_function.attach_screenshot_to_report()



    def verify_content_page(self):
        elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Sender Id']")))
        except TimeoutException:
            print("Page of creation not found")
            self.global_function.attach_screenshot_to_report()
        
        
    def remove_file(self):
        try:
            self.global_function.click("xpath", "//button[@title='Remove file']")
        except TimeoutException:
            print("Button not found")
            self.global_function.attach_screenshot_to_report("verify content page")
            
            
    def select_group_contacts(self,gruop_contacts):
        try:
            self.global_function.click("xpath","//div[@class='ant-select ant-select-single ant-select-show-arrow']//div[@class='ant-select-selector']")###
            self.global_function.click("xpath",f"//div[contains(text(),'{gruop_contacts}')]")
            elements= WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
        except TimeoutException:
            print(f"Not found {gruop_contacts}")
            self.global_function.attach_screenshot_to_report()
            

    def validate_download(self,file_name):
        download_dir = "Downloads"

        try:
            file_path = os.path.join(download_dir, file_name)
            if os.path.isfile(file_path) and os.path.isfile(file_path):
                print(f"El archivo {file_name} se ha descargado correctamente.")
                return True
            else:
                raise Exception(f"El archivo {file_name} fallo")
        except Exception as e:
            print(f"Error al validar la descarga del archivo {file_name}: {str(e)}")
            raise e
        
    def dowload_button(self):
        try:
            elements = WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
            self.global_function.click("xpath", "//span[normalize-space()='Download .csv template']")
        except Exception as e:
            self.global_function.attach_screenshot_to_report("done_button_error")
            error_message = f"Error in click_done_button: {str(e)}"
            raise AssertionError(error_message)

