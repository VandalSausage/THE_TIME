''' all functions for the behave tests '''

################################################################################
## GIVEN #######################################################################

@given('the timestamp <timestamp>')
def get_timestamp(context, timestamp):
    context.timestamp = timestamp
    return context

@given('the decimal representation of the time <decimal_time>')
def get_decimal_time(context, decimal_time):
    context.decimal_time = decimal_time
    return context

@given('the input <work_week>')
def get_work_week(context, work_week):
    context.work_week = work_week
    return context

################################################################################
## WHEN #########################################################€##############

@when('the input is valid')
def valid_input(context):
    return context

@when('the input is not valid')
def invalid_input(context):
    return context

################################################################################
## THEN #########################################################€##############

@then('the error message \'<error>\' is shown')
def error_msg(context, error):
    assert error in context.error

@then('it is converted to a decimal representation of the time <decimal>')
def decimal_converstion_success(context, decimal):
    assert decimal in context.decimal_time

@then('it is converted to a timestamp <timestamp>')
def timestamp_converstion_success(context, timestamp):
    assert timestamp in context.timestamp
