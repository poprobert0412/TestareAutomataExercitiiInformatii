from pages.base_page import BasePage
from browser import Browser
from pages.js_alerts_page import JsAlertsPage


def before_all(context):
    context.browser = Browser()
    context.js_alerts_page = JsAlertsPage()
    context.base_page = BasePage()

def after_all(context):
    context.browser.close()

