import time
import os
import time
import tempfile
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from colorama import  Fore
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from allure_commons.types import AttachmentType




class global_functions:


    def __init__(self, driver):
        self.driver = driver

    def time(self, time):
        time = time.sleep(time)
        return time
        
    def select_element_xpath(self, element, timeout=5):
        element_xpath = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, element)))
        element_xpath = self.driver.execute_script("arguments[0].scrollIntoView()", element_xpath)
        element_xpath = self.driver.find_element(By.XPATH, element)
        return element_xpath

    def select_element_id(self, element, timeout=5):
        element_id = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, element)))
        element_id = self.driver.execute_script("arguments[0].scrollIntoView()", element_id)
        element_id = self.driver.find_element(By.ID, element)
        return element_id      
    
    def select_element_css(self, element, timeout=5):
        element_css = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
        element_css = self.driver.execute_script("arguments[0].scrollIntoView()", element_css)
        element_css = self.driver.find_element(By.CSS_SELECTOR, element)
        return element_css
  
                
    def text(self, selector_type, selector_name, input_text, timeout=10):
        selectors = {
            "xpath": self.select_element_xpath,
            "id": self.select_element_id
        }

        selector_method = selectors.get(selector_type)
        if selector_method:
            try:
                element = selector_method(selector_name, timeout)
                if element:
                    element.clear()
                    time.sleep(1)
                    element.send_keys(input_text)
                    print(f"-----Writing text {input_text} to field {selector_name}")
                else:
                    raise NoSuchElementException(f"Could not find element {selector_name} ({selector_type})")
            except TimeoutException as ex:
                raise TimeoutException(f"Timed out waiting for element {selector_name} ({selector_type}) to be present") from ex
            except NoSuchElementException as ex:
                raise NoSuchElementException(f"Could not find element {selector_name} ({selector_type}): {str(ex)}") from ex
        else:
            raise ValueError(f"Invalid selector type: {selector_type}")


    def click(self, selector_type, selector_name, timeout=10):
        selectors = {
            "xpath": self.select_element_xpath,
            "id": self.select_element_id,
            "css": self.select_element_css
        }
    
        selector_method = selectors.get(selector_type)
        if selector_method:
            try:
                element = selector_method(selector_name)
                time.sleep(1)
                element.click()
                print(f"-----Clicked on element {selector_name}")
            except (TimeoutException, NoSuchElementException) as ex:
                print(Fore.RED+ f"-----Could not find element {selector_name} ({selector_type}): {str(ex)}" + Fore.RESET)
            except Exception as ex:
                print(Fore.RED+ f"-----Error clicking on element {selector_name}: {str(ex)}" + Fore.RESET)
        else:
            print(Fore.RED+ f"-----Invalid selector type: {selector_type}" + Fore.RESET)



    def select(self, selector_type, selector_name, select_type, select_value, time_wait=4):
        selectors = {
            "xpath": self.select_element_xpath,
            "id": self.select_element_id
        }

        select_method = selectors.get(selector_type)
        if select_method:
            try:
                element = select_method(selector_name, time_wait)
                select = Select(element)
                if select_type == "text":
                    select.select_by_visible_text(select_value)
                elif select_type == "value":
                    select.select_by_value(select_value)
                elif select_type == "index":
                    select.select_by_index(select_value)
                else:
                    print(Fore.RED + "-----Invalid select type: {select_type}" + Fore.RESET)
                    return

                print(f"-----Selecting '{select_value}' in field '{selector_name}'")
                time.sleep(time_wait)
            except (TimeoutException, NoSuchElementException) as ex:
                print(Fore.RED + f"-----Could not find element {selector_name} ({selector_type}): {str(ex)}" + Fore.RESET)
            except Exception as ex:
                print(Fore.RED + f"-----Error selecting '{select_value}' in field '{selector_name}': {str(ex)}" + Fore.RESET)
        else:
            print(Fore.RED + f"-----Invalid selector type: {selector_type}" + Fore.RESET)


    def upload_file(self, selector_type, selector_name, file_path, wait_time):
        try:
            element = self.select_element_xpath(selector_name)
            element.send_keys(file_path)
            print(f"File {file_path} uploaded to element {selector_name} ({selector_type})")
            time.sleep(wait_time)
        except TimeoutException as ex:
            print(f"Could not find element {selector_name} ({selector_type}): {str(ex)}")

                

    def wait_for_element(self, locator, selector, timeout=10):
        if locator == "id":
            try:
                element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, selector)))
                element = self.driver.execute_script("arguments[0].scrollIntoView()", element)
                element = self.driver.find_element(By.ID, selector)
                print("-----Element found: {}".format(selector))
                time.sleep(timeout)
            except TimeoutException as ex:
                print(Fore.RED + "-----Element not found: " + selector + Fore.RESET)

        elif locator == "xpath":
            try:
                element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, selector)))
                element = self.driver.execute_script("arguments[0].scrollIntoView()", element)
                element = self.driver.find_element(By.XPATH, selector)
                print("-----Element found: {}".format(selector))
                time.sleep(timeout)
            except TimeoutException as ex:
                print(Fore.RED + "-----Element not found: " + selector + Fore.RESET)
                

    def click_checkboxes_by_xpath(self, time, *xpaths):
        try:
            for xpath in xpaths:
                checkbox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
                checkbox = self.driver.execute_script("arguments[0].scrollIntoView()", checkbox)
                checkbox.click()
                print("-----Checkbox clicked: {}".format(xpath))
                time.sleep(time)
        except TimeoutException:
            for xpath in xpaths:
                print(Fore.RED + "-----Element not found: {}".format(xpath) + Fore.RESET)

                    
    def element_present(self, locator_type, selector, timeout=13):
        try:
            locator = getattr(By, locator_type.upper())
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((locator, selector)))
            element = self.driver.execute_script("arguments[0].scrollIntoView()", element)
            print(f"Element {selector} found using {locator_type}")
            return "Exists"
        except TimeoutException:
            raise AssertionError

    def attach_screenshot_to_report(self, name="screenshot"):
        screenshot_path = os.path.join(self.evidence_path, f"{name}.png")
        # Guarda la captura de pantalla en la ruta especificada
        allure.attach.file(screenshot_path, name=name, attachment_type=AttachmentType.PNG)
            
            




