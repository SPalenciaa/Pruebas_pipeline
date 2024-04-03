from behave import given, when, then
from pages.common_page import common
from data.config import settings 
from framework.webapp import WebApp
from pages.admin_menu_page import admin_menu_page
from pages.admin_companies_page import companies_page
from pages.change_rates_page import change_rates_page
from pages.company_rates_page import Company_Page_Rates
from steps.test_common_step import *

@given(u'I am on the change rates page')
def step_impl(context):
    web_app = WebApp(context.driver)
    web_app.load_website()
    web_app.login_admin()
    driver = web_app.get_driver()
    common_instance = common(driver)
    context.admin_menu_page = admin_menu_page(driver)
    context.companies_page = companies_page(driver)
    context.cost_page = Company_Page_Rates(driver)
    context.change_rates = change_rates_page(driver)
    context.admin_menu_page.select_option_admin("Companies")
    context.companies_page.verify_companies_page()
    

@when(u'I select "Chage-rates" of the company Identidad')
def step_impl(context):
    context.companies_page.change_rates_buttom()


@when(u'I click the "save" button')
def step_impl(context):
    context.change_rates.save_buttom()


@when(u'I confirm the update of rates')
def step_impl(context):
    context.change_rates.confirm_uptdate_button()


@when(u'I click download csv of "{Rate_Template}"')
def step_impl(context,Rate_Template):
    context.change_rates.template_rates(Rate_Template)


@when(u'I see a file downloaded "{namearchive}"')
def step_impl(context,namearchive):
    context.change_rates.review_download(namearchive)



@when(u'I click the view current rates "sms" button')
def step_impl(context):
    context.change_rates.viewer_button_smstemplate_rates()


@then(u'I see a current rates "{rate}"')
def step_impl(context,rate):
    context.cost_page.verify_rates_page()

@when(u'I upload the rate "{id_rate}" archive "{rate}"')
def step_impl(context,rate,id_rate):
    context.change_rates.csv_rates(f"/csv/{rate}",id_rate.strip('"'))


@when(u'I see the efective rate now')
def step_impl(context):
    context.change_rates.efective_rate()

@when(u'I click the view current rates "Voice" button')
def step_impl(context):
    context.change_rates.viewer_button_voicetemplate_rates()


@when(u'I upload the voice_and__sms-rates archive "{ratesms}", "{ratevoice}"')
def step_impl(context,ratesms,ratevoice):
    context.change_rates.csv_rates(f"/csv/{ratesms}",("draggerSms"))
    context.change_rates.csv_rates(f"/csv/{ratevoice}",("draggerVoice"))