from behave import given, when, then
from pages.menu_page import MenuPage
from framework.webapp import WebApp
from pages.company_users_page import Company_Page_Users
from pages.common_page import common
from steps.test_common_step import *


@given(u'I am on the users company page')
def test_step_impl(context):
    web_app = WebApp(context.driver)
    driver = web_app.get_driver()
    web_app.load_website()
    web_app.login()
    common_instance = common(driver)
    menu_page = MenuPage(driver)
    menu_page.select_option_company_users()
    context.company_user = Company_Page_Users(driver)
    


@when(u'Filter the {username} usersname')
def test_step_impl(context,username):
    context.company_user.filter_user(username.strip('"'))


@then(u'I will see the card of the {card} user email')
def test_step_impl(context,card):
    context.company_user.card_user(card.strip('"'))
    
@when(u'I click button for the create user')
def test_step_impl(context):
    context.company_user.create_user_button()


@when(u'I see the create user screen')
def test_step_impl(context):
    context.company_user.create_user_screen()


@when(u'I confirm the create user')
def test_step_impl(context):
    context.company_user.confirm_create()
    
@when(u'I click the create user button')
def test_step_impl(context):
    context.company_user.button_create_user()
    
    
#-----------Formulary-----------#
    
@when(u'I write the {datatext} in {id}')
def test_step_impl(context,id,datatext):
    context.company_user.write_input(id.strip('"'),datatext.strip('"'))

@when(u'I select {nameselect} in {selectId}')
def test_step_impl(context,selectId,nameselect):
    context.company_user.select_input(selectId.strip('"'),nameselect.strip('"'))
