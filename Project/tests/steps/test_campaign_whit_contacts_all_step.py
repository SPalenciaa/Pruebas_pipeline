from data.config import settings 
import allure
from behave import given, when, then
from pages.campaign_destination_page import upload_csv
from pages.campaign_settings_page import campaign_settings
from pages.menu_page import MenuPage
from framework.webapp import WebApp
from pages.common_page import common
from pages.campaign_content_page import custom_message
from steps.test_common_step import *
from pages.campaign_summary_page import Reviewdata 


@given(u'I am on the content page {option_campaing} in {channel}')
def test_step_impl(context,option_campaing,channel):
    web_app = WebApp(context.driver)
    web_app.load_website()
    web_app.login()
    driver = web_app.get_driver()
    menu_page = MenuPage(driver)
    menu_page.select_option_campaign(option_campaing.strip('"'),channel.strip('"'))
    menu_page.verify_campaign_settings_page()
    Campaign_Settings = campaign_settings(driver)
    Campaign_Settings.company_name_test('PRUEBAS AUTOMATIZADAS',settings['company'])
    Campaign_Settings.send_option('1')
    common_instance = common(driver)
    common_instance.next_button()
    Campaign_Settings.verify_desnitation_page()
    context.upload_csv = upload_csv(driver)
    context.common_instance = common(driver)
    context.custom_messages = custom_message(driver)
    context.Reviewdata = Reviewdata(driver)
    
 
  
@when(u'I select the {group_contacts} contacts file')
def test_step_impl(context,group_contacts):
    context.upload_csv.select_group_contacts(group_contacts.strip('"'))
    
    

@when(u'I enter a valid campaign ID and URL')
def test_step_impl(context):
    context.custom_messages.sender_id("123456")
    context.custom_messages.url_toshortlinks("www.identidadtech.com")
    
    
    

@when(u'I create a valid message')
def test_step_impl(context):
    context.custom_messages.create_message()
    
    
    

@when(u'I enter a campaign ID')
def test_step_impl(context):
    context.custom_messages.sender_id("123456")
    
    
    
@when(u'I select the {voice} voice for the campaign')
def test_step_impl(context,voice):
    context.custom_messages.select_voice(voice.strip('"'))