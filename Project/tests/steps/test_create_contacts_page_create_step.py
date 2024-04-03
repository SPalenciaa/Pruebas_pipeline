import time
from behave import given, when, then
from pages.contacts_create_page import Create_Page_Contacts
from pages.menu_page import MenuPage
from framework.webapp import WebApp
from steps.test_common_step import *





@given(u'I am on the contacts {option_contacts} page')
def test_step_impl(context,option_contacts):
    web_app = WebApp(context.driver)
    driver = web_app.get_driver()
    menu_page = MenuPage(driver)
    web_app.load_website()
    web_app.login()
    menu_page.select_option_contacts(option_contacts.strip('"'))
    context.page_contacts = Create_Page_Contacts(driver)
    context.common_instance = common(driver)
    


@when(u'I am not write the list name')
def test_step_impl(context):
    time.sleep(2)

@when(u'I write the name for the list name {name_list}')
def test_step_impl(context,name_list):
    context.page_contacts.validate_accounts_listGroupName(name_list)
    
@when(u'I select the account {account}')
def test_step_impl(context,account):
    context.page_contacts.accounts()
    

@when(u'I redirect at the map page')
def test_step_impl(context):
    context.page_contacts.verify_campign_map_page()