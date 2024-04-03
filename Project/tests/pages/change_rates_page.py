
import time
import os
import datetime
from selenium.common.exceptions import TimeoutException
from pages.global_functions import global_functions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



    
class change_rates_page:
    
    def __init__(self, driver): 
        self.driver = driver
        self.global_function = global_functions(self.driver)
        self.wait = WebDriverWait(self.driver, 15)
        
    def wait_for_file_to_download(self,file_path, timeout=30):
        start_time = time.time()
        while not os.path.isfile(file_path):
            if time.time() - start_time > timeout:
                raise TimeoutException(f"El archivo {file_path} no se descargó en el tiempo especificado.")
            time.sleep(1)
        
    def save_buttom(self):
        try:
            self.global_function.click("xpath", "//span[normalize-space()='Save']")
        except TimeoutException as e:
            self.global_function.attach_screenshot_to_report()
            raise e
        
    def confirm_uptdate_button(self):
        try:
            self.global_function.click("xpath", "(//button[@class='ant-btn ant-btn-primary ant-btn-sm'])[1]")
        except TimeoutException as e:
            self.global_function.attach_screenshot_to_report()
            raise e
        
    def template_rates(self,Rate_Template):
        try:
            self.global_function.click("xpath", f"//span[normalize-space()='{Rate_Template}']")
        except TimeoutException as e:
            self.global_function.attach_screenshot_to_report()
            raise e
    
    def viewer_button_smstemplate_rates(self):
        # Click the button to see the SMS rates in the template
        smstemplate_rates_button_xpath = "//div[@class='ant-drawer-wrapper-body']//div[1]//div[1]//div[1]//div[1]//button[2]"
        try:
            self.global_function.click("xpath", smstemplate_rates_button_xpath)
        except TimeoutException as e:
            self.global_function.attach_screenshot_to_report()
            raise TimeoutException("The button to view SMS rates in the template could not be clicked.") from e
        
    def viewer_button_voicetemplate_rates(self):
        # Click the button to see the VOICE rates in the template
        voice_template_rates_button_xpath = "//div[@class='ant-drawer-body']//div[2]//div[1]//div[1]//div[1]//button[2]//span[1]//*[name()='svg']"
        try:
            self.global_function.click("xpath", voice_template_rates_button_xpath)
        except TimeoutException as e:
            self.global_function.attach_screenshot_to_report()
            raise TimeoutException("The button to view VOICE rates in the template could not be clicked.") from e
        
    def csv_rates(self, csv, id_rate):
        try:
            elements = WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
            wait = WebDriverWait(self.driver, 10)
            time.sleep(2)

            # JavaScript para mostrar el elemento oculto
            script = "arguments[0].style.display = 'block';"
            input_field = self.driver.find_element(By.ID, id_rate)
            self.driver.execute_script(script, input_field)

            input_field.send_keys(csv)

            self.driver.switch_to.window(self.driver.window_handles[0])
        except TimeoutException as e:
            self.global_function.attach_screenshot_to_report()
            raise e
    
    def efective_rate(self):
        try:
            # Now date'MM/DD/YY'
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            xpath = f"//td[contains(text(),'{current_date}')]"
            element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException as e:
            print(current_date)
            raise TimeoutException("Date not found.") from e







        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    def review_download(self, file_name):
        try:
            download_dir = '/home/seluser/Downloads'
            file_path = os.path.join(download_dir, file_name)
            self.wait_for_file_to_download(file_path, timeout=60)
            assert os.path.isfile(file_path), f"El archivo {file_name} no se descargó en {download_dir}"
        except TimeoutException:
            raise Exception("La descarga no se completó a tiempo.")
        except Exception as e:
            print(f"Error al validar la descarga del archivo {file_name}: {str(e)}")
            raise e
        
    
        

