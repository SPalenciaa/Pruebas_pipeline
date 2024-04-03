from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.global_functions import global_functions 
from data.config import settings 
import time




class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.global_function = global_functions(self.driver)
        self.wait = WebDriverWait(self.driver, 15)

    def enter_email(self, email):
        email_input = self.wait.until(EC.presence_of_element_located((By.ID, "email")))
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
        password_input.send_keys(password)


    def init_session_button(self):
        self.global_function.click("id", "next")
        
    def login(self):
        time.sleep(3)
        self.global_function.text("id", "email", settings['user'])
        self.global_function.text("id", "password",settings['password'])
        self.global_function.click("id", "next")
        elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/section/section/header/div/div[1]/div/img")))
        except TimeoutException:
            raise TimeoutException("Element not found")
        
    def login_dev(self):
        time.sleep(3)
        self.global_function.text("id", "email", settings['user_dev'])
        self.global_function.text("id", "password",settings['password_dev'])
        self.global_function.click("id", "next")
        elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/section/section/header/div/div[1]/div/img")))
        except TimeoutException:
            raise TimeoutException("Element not found")
    
    def login_admin(self):
        time.sleep(3)
        self.global_function.text("id", "email", settings['user_admin'])
        self.global_function.text("id", "password",settings['password_admin'])
        self.global_function.click("id", "next")
        elements= WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/section/section/header/div/div[1]/div/img")))
        except TimeoutException:
            raise TimeoutException("Element not found")
        

