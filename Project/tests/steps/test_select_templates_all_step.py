from behave import given, when, then
from pages.menu_page import MenuPage
from framework.webapp import WebApp
from pages.templates_history_page import Templates_History_Page


@given(u'I am on the yp dashboard')
def test_step_impl(context):
    context.web_app = WebApp(context.driver)
    context.web_app.load_website()
    context.web_app.login()
    context.menu_page = MenuPage(context.web_app.get_driver())
    context.templates_history_page = Templates_History_Page(context.web_app.get_driver())


@when(u'I select "{template_option}" from the Templates menu')
def test_step_impl(context, template_option):
    context.menu_page.select_option_templates(template_option.strip('"'))


@then(u'I am redirected to the History Templates page step')
def test_step_impl(context):
    context.templates_history_page.verify_history_page_templates()


@when(u'I see the templates "{templateName}"')
def test_step_impl(context, templateName):
    context.templates_history_page.verify_info_template(templateName.strip('"'))


@when(u'I filter "{template}"')
def test_step_impl(context, template):
    context.templates_history_page.filter_templates(template.strip('"'))


@when(u'I see the template "{templateName}"')
def test_step_impl(context, templateName):
    context.templates_history_page.verify_info_filter(templateName.strip('"'))
