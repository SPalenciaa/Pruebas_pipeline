
from behave import given, when, then
from pages.campaign_destination_page import upload_csv
from pages.campaign_settings_page import campaign_settings
from pages.menu_page import MenuPage
from framework.webapp import WebApp
from pages.common_page import common
from steps.test_common_step import *


@given(u'I am on the content creation page {option_campaing} in {channel}')
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
    
    
@when(u'I select the {MobileNumber} column from the CSV file')
def test_step_impl(context,MobileNumber):
    context.upload_csv.select_phone_number(MobileNumber.strip('"'))



@then(u'I am redirected to the message content page')
def test_step_impl(context):
    context.upload_csv.verify_content_page()
    
@when(u'I am not upload csv file')
def test_step_impl(context):
    context.upload_csv.verify_creation_page()

@then(u'I click on the "remove file" button')
def test_step_impl(context):
    context.upload_csv.remove_file()
    

@when(u'I click to download CSV template')
def test_step_impl(context):
    context.upload_csv.dowload_button()
    
@when(u'I see an example of a file required for the platform has been downloaded')
def test_step_impl(context):
    context.upload_csv.validate_download("yp-bulk-campaign-template (14)")