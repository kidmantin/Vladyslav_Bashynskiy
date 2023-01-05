from behave import *


@when('we press "Global (EN)", then "{language}"')
def step_impl(context, language):
    pass


@then('site show us full page localized to "{language}"')
def step_impl(context, language):
    pass