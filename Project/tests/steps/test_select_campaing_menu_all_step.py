from behave import given, when, then
from pages.menu_page import MenuPage
from framework.webapp import WebApp
from pages.campaign_reports_bulk_page import Reports_Bulk_Page
from pages.campaign_reports_shortlinks_page import Reports_Shortlinks_Page
    
@given(u'I am on the menu page')
def test_step_impl(context):
    web_app = WebApp(context.driver)
    web_app.load_website()
    web_app.login()
    driver = web_app.get_driver()
    context.menu_page = MenuPage(driver)
    context.reports_bulk = Reports_Bulk_Page(driver)
    context.reports_shortlinks = Reports_Shortlinks_Page(driver)


@when(u'I select "{campaign}" from the campaigns menu "{channel}"')
def test_step_impl(context,campaign,channel):
    menu_page = context.menu_page
    menu_page.select_option_campaign(campaign,channel)

@then(u'I am redirected to the campaign settings page')
def test_step_impl(context):
    menu_page = context.menu_page
    menu_page.verify_campaign_settings_page()
    

@then(u'I am redirected to the Shortlinks page init')
def test_step_impl(context):
    context.reports_shortlinks.verify_reports_shortlinks_page()

    