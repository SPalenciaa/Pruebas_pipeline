from behave import given, when, then
from pages.menu_page import MenuPage
from pages.contacts_map__page import Map_Page_Contacts
from pages.dashboard_page import DashboardPage
from framework.webapp import WebApp
from pages.add_balance_page import add_balance_page

@given(u'I am in the dashboard page')
def step_impl(context):
    web_app = WebApp(context.driver)
    web_app.load_website()
    web_app.login()
    driver = web_app.get_driver()
    context.dashboardpage = DashboardPage(driver)
    context.menupage = MenuPage(driver)
    context.balance_page = add_balance_page(driver)


@when(u'I click {campaign} button in dashboard')
def step_impl(context,campaign):
    context.dashboardpage.click_button_campaign("xpath",campaign.strip('"'))
    
@then(u'I am redirected to the firs step to create a SMS campaign')
def step_impl(context):
    context.menupage.verify_campaign_settings_page()
    
    
@then(u'I see the page of assign Balance')
def step_impl(context):
    context.balance_page.confirm_balance_page()

@when(u'I filter the channel for {channel_filter} in the dashboard')
def step_impl(context,channel_filter):
    context.dashboardpage.click_filters_channels("xpat",channel_filter.strip('"'))

@then(u'I see the voice and SMS consumption at the same time')
def step_impl(context):
    context.dashboardpage.verify_change_of_All_button()


@then(u'I see only the voice consumption')
def step_impl(context):
    context.dashboardpage.verify_change_of_VOICE_button()


@then(u'I filter only the consumption of sms')
def step_impl(context):
    context.dashboardpage.verify_change_of_SMS_button()
            
            
            
            
            
