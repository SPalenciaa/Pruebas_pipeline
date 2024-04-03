from behave import given, when, then
from pages.menu_page import MenuPage
from framework.webapp import WebApp
from pages.company_account_page import Company_Page_Account
from pages.company_users_page import Company_Page_Users
from pages.company_rates_page import Company_Page_Rates
from pages.company_History_Balance_page import Company_Page_History_Balance
from steps.test_common_step import *




@given(u'I am on the initial menu and click in "Company Home"')
def test_step_impl(context):
    web_app = WebApp(context.driver)
    web_app.load_website()
    web_app.login()
    driver = web_app.get_driver()
    common_instance = common(driver)
    context.menu_page = MenuPage(driver)
    context.company_account = Company_Page_Account(driver)
    context.company_users = Company_Page_Users(driver)
    context.company_rates = Company_Page_Rates(driver)
    context.company_history = Company_Page_History_Balance(driver)
    common_instance.click_Company_home()


@when(u'I select {company} from the company-Home menu')
def test_step_impl(context,company):
    context.menu_page.select_option_company(company.strip('"'))
    

@then(u'I am redirected to the campaign Account page')
def test_step_impl(context):
    context.company_account.verify_account_page()


@then(u'I am redirected to the campaign Users page')
def test_step_impl(context):
    context.company_users.verify_users_page()
    
@then(u'I am redirected to the campaign Rates page')
def test_step_impl(context):
    context.company_rates.verify_rates_page()
    
@then(u'I am redirected to the campaign History Balance page')
def test_step_impl(context):
    context.company_history.verify_history_balance_page()