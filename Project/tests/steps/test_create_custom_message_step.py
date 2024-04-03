import time
from data.config import settings 
from behave import given, when, then
from pages.campaign_destination_page import upload_csv
from pages.campaign_settings_page import campaign_settings
from pages.menu_page import MenuPage
from framework.webapp import WebApp
from pages.common_page import common
from pages.campaign_content_page import custom_message
from steps.test_common_step import *


@given(u'I am on the message creation page {option_campaing} in {channel}')
def test_step_impl(context,option_campaing,channel):
    web_app = WebApp(context.driver)
    driver = web_app.get_driver()
    menu_page = MenuPage(driver)
    Campaign_Settings = campaign_settings(driver)
    common_instance = common(driver)
    Upload_csv = upload_csv(driver)
    context.custom_messages = custom_message(driver)
    context.common_instance = common(driver)
    web_app.load_website()
    web_app.login()
    menu_page.select_option_campaign(option_campaing.strip('""'),channel.strip('""'))
    menu_page.verify_campaign_settings_page()
    Campaign_Settings.company_name_test('PRUEBAS AUTOMATIZADAS',settings['company'])
    Campaign_Settings.send_option('1')
    common_instance.next_button()
    context.common_instance.csv_valid(settings['csv_path'])
    Upload_csv.select_phone_number("MobileNumber")
    context.common_instance.select_wildcards()
    common_instance.next_button()
    Upload_csv.verify_content_page()

@when(u'I enter a valid URL')
def test_step_impl(context):
    context.custom_messages.url_toshortlinks("www.identidadtech.com")

@when(u'I create a custom message with the wildcards')
def test_step_impl(context):
    context.custom_messages.create_message( click_shortlink=False)

@when(u'I create a custom message with the wildcards and shortlink')
def test_step_impl(context):
    context.custom_messages.create_message()
    
@when(u'I verify my message')
def test_step_impl(context):
    context.custom_messages.verify_message_dynamic()
    
@when(u'I preview the message')
def test_step_impl(context):
    context.custom_messages.verify_message_dynamic_VOICE()

@then(u'I am redirected to the message confirmation page')
def test_step_impl(context):
    context.custom_messages.verify_confirmation_page()

@when(u'I enter a valid campaign ID')
def test_step_impl(context):
    context.custom_messages.sender_id("123456")

@when(u'I write the number for the test')
def test_step_impl(context):
    context.custom_messages.number_for_test("573167628372")

@when(u'I am not write nothing')
def test_step_impl(context):
    time.sleep(3)

@when(u'I click on the "Verify Cost" button to continue')
def test_step_impl(context):
    context.custom_messages.verify_cost_button()
    

@when(u'I click on the "send" button and confirm to continue')
def test_step_impl(context):
    context.custom_messages.send_message_test()

### Bug yp, no se muestra el costo de la llamada de prueba al enviar la prueba. https://identidadtech-team.monday.com/boards/5081280383/pulses/5549334943
@when(u'I see the cost of the message')
def test_step_impl(context):
    context.custom_messages.message_cost()
    
@then(u'I am redirected to the summary page')
def test_step_impl(context):
    time.sleep(3)
    
