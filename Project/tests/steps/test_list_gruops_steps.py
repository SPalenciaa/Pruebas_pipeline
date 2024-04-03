import time
from behave import given, when, then
from pages.contacts_list_groups_page import List_Group_Page_Contacts
from pages.menu_page import MenuPage
from framework.webapp import WebApp
from steps.test_common_step import *

@given(u'I am on the "Groups" page')
def test_step_impl(context):
    web_app = WebApp(context.driver)
    driver = web_app.get_driver()
    menu_page = MenuPage(driver)
    web_app.load_website()
    web_app.login()
    menu_page.select_option_contacts('Groups')
    context.common_instance = common(driver)
    context.list_page = List_Group_Page_Contacts(driver)

@when(u'I filter the contacts "{idsearch}"')
def test_step_impl(context, idsearch):
    context.list_page.search_list_group(idsearch.strip('"'))


@when(u'I see the group of contacts with the name "{card}" and their data')
def test_step_impl(context,card):
    context.list_page.verify_filter_search(card.strip('"'))
    
    