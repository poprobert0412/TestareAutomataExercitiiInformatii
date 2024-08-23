from behave import *


@given(u'I am on the login page')
def step_impl(context):
    print(u'STEP: Given I am on the login page')
    context.base_page.navigate_to_login_page()


@when(u'I send a valid username and password')
def step_impl(context):
    print(u'STEP: When I send a valid username and password')
    context.login_page.send_valid_username_and_password()

@when(u'I press on the login button')
def step_impl(context):
    print(u'STEP: When I press on the login button')
    context.login_page.press_on_the_login_button()

@then(u'I am redirected to secure area page')
def step_impl(context):
    print(u'STEP: Then I am redirected to secure area page')
    context.login_page.check_secure_area_page()

@then(u'I should see the banner: "You logged into a secure area!"')
def step_impl(context):
    print(u'STEP: Then I should see the banner: "You logged into a secure area!"')
    context.login_page.banner_logged_secure_area()

@then(u'I should see the Logout button')
def step_impl(context):
    print(u'STEP: Then I should see the Logout button')
    context.login_page.check_logout_button()

@when(u'I send a correct username and wrong password')
def step_impl(context):
    print(u'STEP: When I send a correct username and wrong password')
    context.login_page.correct_username_wrong_password()

@then(u'I should see the banner: "Your password is invalid!"')
def step_impl(context):
    print(u'STEP: Then I should see the banner: "Your password is invalid!"')
    context.login_page.pasword_invalid_banner()

@when(u'I send a wrong "{username}" and "{password}"')
def step_impl(context, username, password):
    print(u'STEP: When I send a wrong "{username}" and "{password}"')
    context.login_page.send_wrong_username_and_password(username, password)

@then(u'I should see the banner: "Your username is invalid!"')
def step_impl(context):
    print(u'STEP: Then I should see the banner: "Your username is invalid!"')
    context.login_page.username_invalid_banner()