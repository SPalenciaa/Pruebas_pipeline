import time
from behave import given, when, then
from pages.contacts_create_page import Create_Page_Contacts
from pages.contacts_map__page import Map_Page_Contacts
from pages.contacts_confirmation_page import Confirmation_Page_Contacts
from pages.menu_page import MenuPage
from framework.webapp import WebApp
from steps.test_common_step import *



@when(u'I am on the confirmation contacts page')
def test_step_impl(context):
    web_app = WebApp(context.driver)
    driver = web_app.get_driver()
    context.common_instance = common(driver)
    context.confirmation_page_contacts = Confirmation_Page_Contacts(driver)
    context.Map_Page_Contact = Map_Page_Contacts(driver)
    menu_page = MenuPage(driver)
    web_app.load_website()
    web_app.login()
    menu_page.select_option_contacts("Create")
    create_page = Create_Page_Contacts(driver)
    create_page.validate_accounts_listGroupName("PRUEBAS CONTACTOS")
    create_page.accounts()
    context.common_instance.csv_valid(settings['csv_path_contacts'])
    context.common_instance.next_button()
    context.Map_Page_Contact.select_phone_number("MobileNumber")
    context.common_instance.select_wildcards()
    context.common_instance.next_button()
    context.Map_Page_Contact.verify_campign_confirmation_page()





@then(u'I am redirected to the list_gropus page')
def test_step_impl(context):
    context.confirmation_page_contacts.verify_list_gropus_page()
    
    
    