from behave import when, given, then

from features.page_objects.base_page import BasePage
from features.page_objects.login_page import LoginPage
from features.page_objects.logout_page import LogoutPage


@given('User is on drive page')
def login_successful(context):
    page = LoginPage(context.driver)
    page.login_to_pah_website()
    page.login_successful()
    assert context.driver.execute_script("return window.localStorage.jwt") is not None


@when('User logs out via menu Logout button')
def logout_via_button(context):
    page = LogoutPage(context.driver)
    page.logout_via_logout_button()


@then('User is on logout view with removed session details')
def logged_out_user_state(context):
    page = LogoutPage(context.driver)
    page.logged_out_user_state()
    assert context.driver.execute_script("return window.localStorage.jwt") is None
    assert "drive" not in page.get_current_url()


@when('User enters logout page')
def enter_logout_url(context):
    page = BasePage(context.driver)
    page.visit_logout_view()


@then('User logs in via logout view')
def login_via_logout_view(context):
    page_logout = LogoutPage(context.driver)
    page_logout.navigate_to_login_via_logout()
    page_login = LoginPage(context.driver)
    page_login.login_to_pah_website()
    page_login.login_successful()
