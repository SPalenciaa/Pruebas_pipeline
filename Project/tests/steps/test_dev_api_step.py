from selenium.common.exceptions import NoSuchElementException
from behave import given, when, then
from framework.webapp import WebApp
from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from pages.Sms_api_page import Sms_Api_Page
from pages.documentation_dev_page import Documentation_Dev_Page

@given(u'I am on the login page of the dev')
def test_step_impl(context):
    web_app = WebApp(context.driver)
    web_app.load_website()
    web_app.login_dev()
    driver = web_app.get_driver()
    context.menu_page = MenuPage(driver)
    context.sms_page = Sms_Api_Page(driver)
    context.documentation_page = Documentation_Dev_Page(driver)


@when(u'I select {developers_option} from the Developers menu')
def test_step_impl(context, developers_option):
    context.menu_page.select_option_developers(developers_option.strip('"'))


@then(u'I am redirected to SMS API Key page')
def test_step_impl(context):
    context.sms_page.verify_api_page()
    
@when(u'I see the apis')
def test_step_impl(context):
    context.sms_page.api_info()
    
    
@then(u'I am redirected to Documentation page')
def test_step_impl(context):
    context.documentation_page.verify_documentation_page()


@when(u'I see the Documentation Api')
def test_step_impl(context):
    context.documentation_page.verify_api_documents()
