
from behave import given, when, then
from pages.common_page import common
from data.config import settings 
from framework.webapp import WebApp
from pages.admin_menu_page import admin_menu_page
from pages.admin_companies_page import companies_page
from pages.add_balance_page import add_balance_page
from steps.test_common_step import *


@given(u'I go to the exchange rate to add balance to the company Identity')
def step_impl(context):
    web_app = WebApp(context.driver)
    web_app.load_website()
    web_app.login_admin()
    driver = web_app.get_driver()
    context.common_instance = common(driver)
    context.admin_menu_page = admin_menu_page(driver)
    context.companies_page = companies_page(driver)
    context.add_balance = add_balance_page(driver)
    context.admin_menu_page.select_option_admin("Companies")
    context.companies_page.verify_companies_page()

@when(u'I click the add balance button')
def step_impl(context):
    context.add_balance.add_balance_button()
    


@when(u'I write "{balance}" usd add balance')
def step_impl(context,balance):
    context.add_balance.modal_balance(balance.strip('"'))


@when(u'I confirm the add balance')
def step_impl(context):
    context.add_balance.accept_balance_button()
    context.add_balance.confirm_balance_button()
    


@when(u'I see the alert error "{alert}"')
def step_impl(context,alert):
    context.common_instance.error_message_matches(alert,"//div[@role='alert']")
