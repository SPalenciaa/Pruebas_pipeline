from behave import given, when, then
from pages.common_page import common
from data.config import settings 
from pages.campaign_settings_page import campaign_settings
from pages.menu_page import MenuPage
from framework.webapp import WebApp




@when(u'I click on the "next" button to continue')
def test_step_impl(context):
    context.common_instance = common(context.driver)
    context.common_instance.next_button()

    
@then(u'I see the error message "{expected_message}" in "{xpath}"')
def test_step_impl(context, expected_message, xpath):
    context.common_instance = common(context.driver)
    context.common_instance.error_message_matches(expected_message, xpath)
    
    
@when(u'I am see the confirmation alert, "{alert_confirmation}" in "{xpath}"')
def test_step_impl(context,alert_confirmation,xpath):
    context.common_instance = common(context.driver)
    context.common_instance.error_message_matches(alert_confirmation, xpath)
    


@when(u'I click the "done" button to finish the campaign creation process')
def test_step_impl(context):
    context.common_instance = common(context.driver)
    context.common_instance.click_done_button()
    
@when(u'I upload a valid CSV file with phone numbers')
def test_step_impl(context):
    context.common_instance = common(context.driver)
    context.common_instance.csv_valid(settings['csv_path'])
    
@when(u'I select the wildcards to use')
def test_step_impl(context):
    context.common_instance = common(context.driver)
    context.common_instance.select_wildcards()
    
@when(u'I click the confirm campaign')
def test_step_impl(context):
    context.common_instance = common(context.driver)
    context.common_instance.confirm_campaign()




