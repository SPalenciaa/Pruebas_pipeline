from selenium.common.exceptions import NoSuchElementException
from behave import given, when, then
from framework.webapp import WebApp
from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from pages.validate_users import Validate_Users

@given(u'I am on the login page')
def test_step_impl(context):
    web_app = WebApp(context.driver)
    web_app.load_website()
    driver = web_app.get_driver()
    context.login_page = LoginPage(driver)
    context.menu_page = MenuPage(driver)
    context.validate_users = Validate_Users(driver)
    


@when(u'I enter {usuario} and {password}')
def test_step_impl(context,usuario,password):
    context.login_page.enter_email(usuario)
    context.login_page.enter_password(password)


@when(u'I click the "Next" button')
def test_step_impl(context):
    context.login_page.init_session_button()


@when(u'I should be logged in successfully')
def test_step_impl(context):
    context.menu_page.verify_menu_page()


@when(u'I should see my {usuario_esperado} and {rol_esperado} displayed on the screen')
def test_step_impl(context,usuario_esperado,rol_esperado):
    context.menu_page.verify_user(usuario_esperado)
    context.menu_page.verify_rol_page(rol_esperado)

