from behave import given, when, then
import time
from pages.campaign_settings_page import campaign_settings
from pages.menu_page import MenuPage
from framework.webapp import WebApp
from pages.common_page import common
from steps.test_common_step import *
from data.config import settings


@given(u'I am on the campaign settings page {option_campaing} in {channel}')
def test_step_impl(context,option_campaing,channel):
    web_app = WebApp(context.driver)
    driver = web_app.get_driver()
    menu_page = MenuPage(driver)
    context.campaign_settings_page = campaign_settings(driver)
    context.common_instance = common(driver)
    web_app.load_website()
    web_app.login()
    menu_page.select_option_campaign(option_campaing.strip('"'),channel.strip('"'))
    menu_page.verify_campaign_settings_page()


@given(u'I select a company, and a name for the test {campaign_name}')
def test_step_impl(context,campaign_name):
    context.campaign_settings_page.company_name_test(campaign_name,settings['company'])


@then(u'I am redirected to the destination creation page')
def test_step_impl(context):
    context.campaign_settings_page.verify_desnitation_page()


@given(u'I select a company and a campaign name empty or invalid')
def test_step_impl(context):
    context.campaign_settings_page.empty_campaing_name_account()


@when(u'I select Send now/schedule option {option}')
def test_step_impl(context,option):
    context.campaign_settings_page.send_option(option.strip('"'))
    


@when(u'I click the add phase')
def test_step_impl(context):
    context.campaign_settings_page.add_phase()



@when(u'I enter a percentage "{percentage}" in the phase')
def test_step_impl(context,percentage):
    context.campaign_settings_page.add_percentage(percentage)


@when(u'I enter the {date_type} date in the phase')
def test_step_impl(context,date_type):
    context.campaign_settings_page.date_today_phase(date_type.strip('"'))
    
@when(u'I enter the {time} hour')
def test_step_impl(context,time):
    context.campaign_settings_page.hour_today_phase(time.strip('"'))