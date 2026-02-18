from behave import given, when, then
import requests

from resolution import context

BASE_URL = ""

@given("Base API URL is configured")
def step_base_url(context):
        context.base_url = BASE_URL

@when('I send a "{method}" request to "{endpoint}"')
def step_send_request(context, method, endpoint):

    url = context.base_url + endpoint
    context.response = requests.request(method, url)

@then("I should receive a valid response")
def step_validate(context):
    assert context.response.status_code < 500