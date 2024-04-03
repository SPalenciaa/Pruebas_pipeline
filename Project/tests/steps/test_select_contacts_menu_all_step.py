from behave import given, when, then
from pages.contacts_create_page import Create_Page_Contacts
from pages.contacts_map__page import Map_Page_Contacts
from pages.menu_page import MenuPage
from framework.webapp import WebApp


    
@given(u'I am in the dashboard')
def test_step_impl(context):
    web_app = WebApp(context.driver)
    web_app.load_website()
    web_app.login()
    driver = web_app.get_driver()
    context.menu_page = MenuPage(driver)
    context.contacts_page = Create_Page_Contacts(driver)
    context.map_page_contacts = Map_Page_Contacts(driver)
    


@then(u'I am redirected to the contacts create page step')
def test_step_impl(context):
    contacts_page = context.contacts_page
    contacts_page.verify_create_contacts()
    
@when(u'I select "{option_contacts}" from the contacts menu')
def test_step_impl(context,option_contacts):
    menu_page = context.menu_page
    menu_page.select_option_contacts(option_contacts)

@then(u'I am redirected to the contacts Groups/Lists page')
def test_step_impl(context):
    map_page_contacts = context.map_page_contacts
    map_page_contacts.verify_list_groups_contacts()