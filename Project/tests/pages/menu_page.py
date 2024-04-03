from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from pages.global_functions import global_functions
import time

class MenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.action = global_functions(self.driver)
        self.wait = WebDriverWait(self.driver, 15)

    def _wait_for_element_to_disappear(self):
        try:
            self.wait.until(EC.invisibility_of_element_located((By. ID, "spinner_background")))
        except TimeoutException:
            print("El elemento no se pudo encontrar en el tiempo límite de espera.")

    def _click_element(self, locator_type, locator):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-layout-sider-children']")))
            self.action.click(locator_type, locator)
        except (TimeoutException, NoSuchElementException) as e:
            self.action.attach_screenshot_to_report(name=f"select_option_error_{locator}", wait_time=5)
            raise e

    def select_option_campaign(self, campaign, channel):
        try:
            self._wait_for_element_to_disappear()
            self._click_element("xpath", "//span[normalize-space()='Create Campaign']")
            self._click_element("xpath", f"//span[normalize-space()='{channel}']")
            self._click_element("xpath", f"//a[normalize-space()='{campaign}']")
        except Exception as e:
            self.action.attach_screenshot_to_report("select_option_campaign")
            raise e

    def select_option_developers(self, developers_option):
        try:
            self._wait_for_element_to_disappear()
            self._click_element("xpath", "(//div[@role='menuitem'])[1]")
            self._click_element("xpath", f"//a[normalize-space()='{developers_option}']")
        except Exception as e:
            self.action.attach_screenshot_to_report("select_option_developers")
            raise e

    def select_option_company(self, balance):
        try:
            self._wait_for_element_to_disappear()
            self._click_element("xpath", "//span[@class='-title-content'][normalize-space()='Company']")
            self._click_element("xpath", f"//a[normalize-space()='{balance}']")
        except Exception as e:
            self.action.attach_screenshot_to_report("select_option_company")
            raise e

    def select_option_balance(self):
        try:
            self._wait_for_element_to_disappear()
            self._click_element("xpath", "//span[normalize-space()='Company Home']")
            self._click_element("xpath", "//span[@class='ant-menu-title-content']//a[normalize-space()='Balance']")
        except Exception as e:
            self.action.attach_screenshot_to_report("select_option_balance")
            raise e

    def select_option_company_users(self):
        try:
            self._wait_for_element_to_disappear()
            self._click_element("xpath", "//span[normalize-space()='Company Home']")
            self._click_element("xpath", "//a[contains(text(),'Users')]")
        except Exception as e:
            self.action.attach_screenshot_to_report("select_option_company_users")
            raise e

    def select_option_contacts(self, contacts_option):
        try:
            self._wait_for_element_to_disappear()
            self._click_element("xpath", "//span[normalize-space()='Contacts']")
            self._click_element("xpath", f"//a[normalize-space()='{contacts_option}']")
        except Exception as e:
            self.action.attach_screenshot_to_report("select_option_contacts")
            raise e

    def select_option_templates(self, templates_option):
        try:
            self._wait_for_element_to_disappear()
            self._click_element("xpath", "//span[normalize-space()='Templates']")
            self._click_element("xpath", f"//a[normalize-space()='{templates_option}']")
        except Exception as e:
            self.action.attach_screenshot_to_report("select_option_templates")
            raise e

    def verify_campaign_settings_page(self):
        try:
            self._wait_for_element_to_disappear()
            self.action.element_present("xpath", "//div[contains(text(),'Campaign Name')]")
        except Exception as e:
            self.action.attach_screenshot_to_report("verify_campaign_settings_page_error")
            raise e

    def verify_menu_page(self):
        try:
            self._wait_for_element_to_disappear()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-layout-sider-children']")))
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//main[@class='ant-layout-content']")))
        except Exception as e:
            self.action.attach_screenshot_to_report("verify_menu_page_error")
            raise e

    def verify_rol_page(self, rol_esperado):
        try:
            self._wait_for_element_to_disappear()
            rol_actual = self.wait.until(EC.presence_of_element_located((By.ID, "rol_company"))).text
            if rol_esperado == rol_actual:
                return True
            self.action.attach_screenshot_to_report()
            raise AssertionError(f"The actual role '{rol_actual}' does not match the expected role '{rol_esperado}'.")
        except TimeoutException:
            print("El elemento no se pudo encontrar en el tiempo límite de espera.")
        except NoSuchElementException:
            print("No se encontró el elemento.")

    def verify_user(self, usuario_esperado):
        try:
            self._wait_for_element_to_disappear()
            usuario_actual = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/section/header/div/div[2]/div/p[1]"))).text
            if usuario_esperado == usuario_actual:
                return True
            self.action.attach_screenshot_to_report()
            raise AssertionError(f"The actual role '{usuario_actual}' does not match the expected role '{usuario_esperado}'.")
        except TimeoutException:
            print("El elemento no se pudo encontrar en el tiempo límite de espera.")
        except NoSuchElementException:
            print("No se encontró el elemento.")
