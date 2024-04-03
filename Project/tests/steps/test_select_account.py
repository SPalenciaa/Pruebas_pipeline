
from behave import given, when, then
from pages.menu_page import MenuPage
from pages.admin_companies_page import companies_page
from pages.company_account_page import Company_Page_Account
from steps.test_common_step import *


@given(u'I login in yp platform')
def test_step_impl(context):
    web_app = WebApp(context.driver)
    web_app.load_website()
    web_app.login()
    driver = web_app.get_driver()
    common_instance = common(driver)
    context.menu_page = MenuPage(driver)
    context.company_page_account = Company_Page_Account(driver)
    common_instance.click_Company_home()

@then(u'I view Balance in "{company}" Account')
def step_impl(context, company):
    context.company_page_account.verify_company_change(company.strip('"'))



@when(u'I select a "{account}" Account')
def step_impl(context,account):
    context.company_page_account.click_specific_account(f"(//button[@type='button'])[{account}]")
    

@then(u'I am view account page')
def step_impl(context):
    context.company_page_account.verify_account_page()



@when(u'I select "{account}" of the menu lateral of the page')
def step_impl(context,account):
    context.menu_page.select_option_company(account.strip('"'))
    
