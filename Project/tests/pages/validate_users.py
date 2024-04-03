from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from pages.global_functions import global_functions
from selenium.webdriver.support.ui import WebDriverWait


class Validate_Users:
    
    def __init__(self, driver): 
        self.driver = driver
        self.global_function = global_functions(self.driver)

        
    def account_Admin(self):
        try:
            self.global_function.select_element_xpath("//a[normalize-space()='Performance']")
            self.global_function.select_element_xpath("//a[normalize-space()='Companies']")
            self.global_function.select_element_xpath("//a[normalize-space()='A-Z Base rates']")
            self.global_function.select_element_xpath("//a[normalize-space()='History Balance']")
            self.global_function.select_element_xpath("//a[normalize-space()='Users']")
            print("Los elementos están presentes para el rol 'admin'")
        except NoSuchElementException:
            raise AssertionError("No se encontraron todos los elementos para el rol 'admin'")
            
    def account_CompanyAdmin(self):
        try:
            self.global_function.select_element_xpath("//a[normalize-space()='Performance']")
            self.global_function.select_element_xpath("//span[@class='-title-content'][normalize-space()='Company']")
            self.global_function.select_element_xpath("//span[normalize-space()='Campaigns']")
            self.global_function.select_element_xpath("//span[normalize-space()='Contacts']")
            self.global_function.select_element_xpath("//span[normalize-space()='Templates']")
            print("Los elementos están presentes para el rol 'companyAdmin'")
        except NoSuchElementException:
            raise AssertionError("No se encontraron todos los elementos para el rol 'companyAdmin'")
            
    def account_user(self):
        try:
            self.global_function.select_element_xpath("//a[normalize-space()='Performance']")
            self.global_function.select_element_xpath("/html/body/div/section/aside/div[1]/ul/li[2]/div/span[2]")
            print("Los elementos están presentes para el rol 'user'")
        except NoSuchElementException:
            raise AssertionError("No se encontraron todos los elementos para el rol 'user'")
