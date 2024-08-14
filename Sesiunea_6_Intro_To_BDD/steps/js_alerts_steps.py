from behave import *

@when(u'I press on the jsalert button')
def step_impl(context):
    print(u'STEP: When I press on the jsalert button')
    context.js_alerts_page.click_jsalert_button()


@when(u'I press on the OK button from the alert pop-up')
def step_impl(context):
    print(u'STEP: When I press on the OK button from the alert pop-up')
    context.js_alerts_page.click_ok_button()

@then(u'I should see the following message: "You successfully clicked an alert"')
def step_impl(context):
    print(u'STEP: Then I should see the following message: "You successfully clicked an alert"')
    context.js_alerts_page.you_successfully_clicked_an_alert()

@when(u'I press on the jsconfirm button')
def step_impl(context):
    print(u'STEP: When I press on the jsconfirm button')
    context.js_alerts_page.click_jsconfirm_button()

@then(u'I should see the following message: "You clicked: Ok"')
def step_impl(context):
    print(u'STEP: Then I should see the following message: "You clicked: Ok"')
    context.js_alerts_page.you_clicked_ok()

@when(u'I press on the Cancel button from the alert pop-up')
def step_impl(context):
    print(u'STEP: When I press on the Cancel button from the alert pop-up')
    context.js_alerts_page.click_on_the_cancel_button()

@then(u'I should see the following message: "You clicked: Cancel"')
def step_impl(context):
    print(u'STEP: Then I should see the following message: "You clicked: Cancel"')
    context.js_alerts_page.you_clicked_cancel()

@when(u'I press on the jsprompt button')
def step_impl(context):
    print(u'STEP: When I press on the jsprompt button')
    context.js_alerts_page.click_on_the_jsprompt_button()

@when(u'I input "{text}"')
def step_impl(context, text):
    print(u'STEP: When I input "{text}"')
    context.js_alerts_page.send_text_to_alert(text)

@then(u'I should see the following message: "You entered: "{name}""')
def step_impl(context, name):
    print(u'STEP: Then I should see the following message: "You entered: "{name}""')
    context.js_alerts_page.verify_result_name(name)

@then(u'I should see the following message: "You entered: null"')
def step_impl(context):
    print(u'STEP: Then I should see the following message: "You entered: null"')
    context.js_alerts_page.you_entered_null()
