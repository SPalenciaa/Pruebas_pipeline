from behave import given, when, then
from pages.menu_page import MenuPage
from framework.webapp import WebApp
from pages.company_balance_page import Company_Page_Balance
from pages.common_page import common
from steps.test_common_step import *



@given(u'I am on the Balance company page')
def test_step_impl(context):
    web_app = WebApp(context.driver)
    driver = web_app.get_driver()
    web_app.load_website()
    web_app.login()
    common_instance = common(driver)
    menu_page = MenuPage(driver)
    menu_page.select_option_balance()
    context.common = common(driver)
    context.company_filter = Company_Page_Balance(driver)


@when(u'Filter the {account} account')
def test_step_impl(context,account):
    context.company_filter.filter_account(account.strip('"'))
    
    
    
@then(u'I will see the card of the {card} account')
def test_step_impl(context,card):
    context.company_filter.card_account(card.strip('"'))
    
@when(u'I select "Assign Credit" button')
def test_step_impl(context):
    context.company_filter.asig_credit_button()


@then(u'I see the assign credits screen')
def test_step_impl(context):
    context.company_filter.asig_credit_screen()


@when(u'I click the "Allocate founds" button')
def test_step_impl(context):
    context.company_filter.allocate_founds_button()
    
@when(u'I select the {account} account')
def test_step_impl(context,account):
    context.company_filter.select_account(account.strip('"'))
    
@when(u'I enter a valor {balance} in the avaliable balanace')
def test_step_impl(context,balance):
    context.company_filter.input_balance_credit(balance.strip('"'))
