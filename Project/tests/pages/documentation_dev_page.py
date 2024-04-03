import time
from pages.global_functions import global_functions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

class Documentation_Dev_Page():
    
    def __init__(self,driver):
        self.driver = driver
        self.global_function = global_functions(self.driver)
        self.wait = WebDriverWait(self.driver, 15)
        
    
    def verify_documentation_page(self):
        try:
            elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
            self.wait.until(EC.presence_of_element_located((By.XPATH, "(//h2[normalize-space()='Send messages with the SMS API'])[1]")))
        except TimeoutException as e:
            print("Error: Page listmap not found")
            self.global_function.attach_screenshot_to_report()
            raise e

    def verify_api_documents(self):
        BUTTON_MAPPINGS = {
            1: {
                'button_id': 'rc-tabs-0-tab-item-1',
                'panel_xpath': "(//div[@class='sc-gTRrQi epXxba'])[1]"
            },
            2: {
                'button_id': 'rc-tabs-0-tab-item-2',
                'panel_xpath': "(//div[@class='sc-gTRrQi epXxba'])[2]"
            },
            3: {
                'button_id': 'rc-tabs-0-tab-item-3',
                'panel_xpath': "(//div[@class='sc-gTRrQi epXxba'])[3]"
            },
            4: {
                'button_id': 'rc-tabs-0-tab-item-4',
                'panel_xpath': "(//div[@class='sc-gTRrQi epXxba'])[4]"
            },
            5: {
                'button_id': 'rc-tabs-0-tab-item-5',
                'panel_xpath': "(//div[@class='sc-gTRrQi epXxba'])[5]"
            }
        }

        for panel_number, mappings in BUTTON_MAPPINGS.items():
            button_id = mappings['button_id']
            panel_xpath = mappings['panel_xpath']

            try:
                self.global_function.click("id", button_id)
                self.global_function.element_present("xpath", panel_xpath)
                if self.panel_has_changed(panel_xpath):
                    print("El panel ha cambiado correctamente.")
                else:
                    print("Error: El panel no ha cambiado correctamente.")
                    self.global_function.attach_screenshot_to_report()
            except TimeoutException as e:
                print("Error: Page listmap not found")
                self.global_function.attach_screenshot_to_report()
                raise e

    def panel_has_changed(self, panel_xpath):
        try:
            self.global_function.element_present("xpath", panel_xpath)
            return True
        except NoSuchElementException:
            return False

