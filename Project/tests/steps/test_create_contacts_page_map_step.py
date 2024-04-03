import time
from behave import given, when, then
from pages.contacts_create_page import Create_Page_Contacts
from pages.contacts_map__page import Map_Page_Contacts
from pages.menu_page import MenuPage
from framework.webapp import WebApp
from steps.test_common_step import *
from pages.common_page import common

@given(u'I am on the create contacts map page')
def test_step_impl(context):
    web_app = WebApp(context.driver)
    driver = web_app.get_driver()
    context.common_instance = common(driver)
    context.map_page = Map_Page_Contacts(driver)
    menu_page = MenuPage(driver)
    web_app.load_website()
    web_app.login()
    menu_page.select_option_contacts("Create")
    create_page = Create_Page_Contacts(driver)
    create_page.validate_accounts_listGroupName("PRUEBAS CONTACTOS")
    create_page.accounts()
    context.common_instance.csv_valid(settings['csv_path'])
    context.common_instance.next_button()
    context.map_page.verify_list_groups_contacts()
    
@when(u'I select {MobileNumber} of the csv')
def test_step_impl(context,MobileNumber):
    context.map_page.select_phone_number(MobileNumber.strip('"'))
    
@when(u'I redirect at the confirmation page')
def test_step_impl(context):
    context.map_page.verify_campign_confirmation_page()
    
