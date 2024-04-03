from data.config import settings 
from behave import given, when, then
from pages.campaign_destination_page import upload_csv
from pages.campaign_settings_page import campaign_settings
from pages.menu_page import MenuPage
from framework.webapp import WebApp
from pages.common_page import common
from pages.campaign_content_page import custom_message
from pages.common_page import *
from pages.campaign_summary_page import Reviewdata 



@given(u'I am on the "{option_campaing}" campaign summary page test in "{channel}"')
def test_step_impl(context,option_campaing,channel):
    web_app = WebApp(context.driver)
    web_app.load_website()
    web_app.login()
    driver = web_app.get_driver()
    menu_page = MenuPage(driver)
    context.common_instance = common(driver)
    menu_page.select_option_campaign(option_campaing,channel)
    menu_page.verify_campaign_settings_page()
    Campaign_Settings = campaign_settings(driver)
    Campaign_Settings.company_name_test('PRUEBAS AUTOMATIZADAS',settings['company'])
    Campaign_Settings.send_option('1')
    common_instance = common(driver)
    common_instance.next_button()
    Campaign_Settings.verify_desnitation_page()
    Upload_csv = upload_csv(driver)
    context.common_instance.csv_valid(settings['csv_path'])
    Upload_csv.select_phone_number("MobileNumber")
    common_instance.select_wildcards()
    common_instance.next_button()
    Upload_csv.verify_content_page()
    custom_messages = custom_message(driver)
    custom_messages.sender_id("18332604961")
    if option_campaing == "Shortlink":
        custom_messages.url_toshortlinks("www.identidadtech.com")
    custom_messages.create_message()
    if option_campaing == "Bulk Voice":
        custom_messages.select_voice("Male / Spanish")
    common_instance.next_button()
    context.Reviewdata = Reviewdata(driver)


@when(u'I review the {campaign_name} and data')
def test_step_impl(context, campaign_name):
    context.Reviewdata.data(campaign_name.strip('"'))


    

@then(u'I am redirected to the campaigns menu and see the confirmation alert')
def test_step_impl(context):
    context.Reviewdata.redirected_campaigns_menu()
    
