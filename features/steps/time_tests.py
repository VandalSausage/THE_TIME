''' all functions for the behave tests '''
from behave import given, when, then, step
import collections
from aisha_time import time_day, timestamp_to_decimal, \
    decimal_time_to_timestamp, work_week_and_actual_day, the_actual_time
from THE_TIME import time_conv, time_inv, WT_parameter_calculation, \
    actual_time_conv, actual_time

################################################################################
## GIVEN #######################################################################

@given('the timestamp {timestamp} and day {day}')
def get_timestamp_and_day(context, timestamp, day):
    context.timestamp = timestamp
    context.day = day
    return context

@given('the timestamp {timestamp}')
def get_timestamp(context, timestamp):
    context.timestamp = timestamp
    return context

@given('the decimal representation of the time {decimal_time}')
def get_decimal_time(context, decimal_time):
    context.decimal_time = float(decimal_time)
    return context

@given('a valid work week')
def get_work_week(context):
    context.work_week = VALID_WORK_WEEK
    return context

@given('an invalid work week {work_week}')
def get_work_week(context, work_week):
    context.work_week = TEST_WORK_WEEKS[work_week]
    return context

################################################################################
## WHEN #########################################################€##############

@when('the input is valid')
def valid_input(context):
    if hasattr(context, 'decimal_time'):
        context.valid_decimal = validate_decimal_time(context.decimal_time)
        if not context.valid_decimal:
            raise AssertionError("data is not valid")

    if hasattr(context, 'timestamp'):
        context.valid_timestamp = validate_timestamp(context.timestamp)
        if not context.valid_timestamp:
            raise AssertionError("data is not valid")

    if hasattr(context, 'work_week'):
        context.valid_work_week = validate_work_week(context.work_week)
        if not context.valid_work_week:
            raise AssertionError("data is not valid")

    return context

@when('the input is not valid')
def invalid_input(context):
    if hasattr(context, 'decimal_time'):
        context.valid_decimal = validate_decimal_time(context.decimal_time)
        if context.valid_decimal:
            raise AssertionError("data is valid will not show error")

    if hasattr(context, 'timestamp'):
        context.valid_timestamp = validate_timestamp(context.timestamp)
        if context.valid_timestamp:
            raise AssertionError("data is valid will not show error")

    if hasattr(context, 'work_week'):
        context.valid_work_week = validate_work_week(context.work_week)
        if context.valid_work_week:
            raise AssertionError("data is valid will not show error")

    return context

# you request the actual time
@when('you request the actual time from aisha')
def time_check(context):
    context.aisha_actual_time = the_actual_time(VALID_WORK_WEEK, context.timestamp, context.day)
    print(context.aisha_actual_time)
    return context

@when('you request the actual time from truman')
def time_check(context):
    context.truman_actual_time = actual_time()
    print(context.truman_actual_time)
    return context
################################################################################
## THEN #########################################################€##############

@then('the error message \'{error}\' is shown')
def error_msg(context, error):

    if hasattr(context, 'decimal_time'):
        context.error = decimal_time_to_timestamp(context.decimal_time)

    if hasattr(context, 'timestamp'):
        context.error = timestamp_to_decimal(context.timestamp)

    if hasattr(context, 'work_week'):
        context.error = work_week_and_actual_day(context.work_week)

    if hasattr(context, 'aisha_actual_time'):
        context.error = context.aisha_actual_time

    if hasattr(context, 'truman_actual_time'):
        context.error = context.truman_actual_time

    print(context.error)
    assert error == context.error

@then('it is converted to a decimal representation of the time {decimal}')
def decimal_converstion_success(context, decimal):
    context.decimal_time = timestamp_to_decimal(context.timestamp)
    assert float(decimal) == context.decimal_time

@then('it is converted to a timestamp {timestamp}')
def timestamp_converstion_success(context, timestamp):
    context.timestamp = decimal_time_to_timestamp(context.decimal_time)
    assert timestamp in context.timestamp

@then('the actual time is {actual_time}')
def timestamp_converstion_success(context, actual_time):
    if hasattr(context, 'aisha_actual_time'):
        context.actual_time = context.aisha_actual_time
    elif hasattr(context, 'truman_actual_time'):
        context.actual_time = context.truman_actual_time

    assert actual_time in context.actual_time

@then('the two actual times are equal')
def two_method_check(context):
    assert context.aisha_actual_time == context.aisha_actual_time

################################################################################
## VALIDATION FUNCTIONS ########################################################

def validate_decimal_time(decimal_time):
    if decimal_time < 0 or decimal_time >= 24:
        return False
    else:
        return True

def validate_timestamp(timestamp):

    # split timestamp
    split_timestamp = timestamp.split(':')

    # first validation check
    if len(split_timestamp) != 3:
        return False

    else:

        # second validation check
        for time_frag in split_timestamp:
            if len(time_frag) > 2:
                return False

        # split out the timestamp into hrs, mins, secs
        hours = float(split_timestamp[0])
        mins = float(split_timestamp[1])
        seconds = float(split_timestamp[2])

        # third validation check
        if hours < 0 or hours > 23 or mins < 0 or mins > 59 or seconds < 0 or seconds > 59:
            return False

        else:
            return True

def validate_work_week(work_week):
    if len(work_week) < 8:
        return False
    else:
        return True

################################################################################
## TEST DATA ###################################################################

INVALID_WORK_WEEK_1 = collections.OrderedDict()
INVALID_WORK_WEEK_1['Monday'] = ('09:00:00', '17:30:00')
INVALID_WORK_WEEK_1['Zhenjsday'] = ('09:30:00', '17:00:00')
INVALID_WORK_WEEK_1['Wednesday'] = ('09:00:00', '17:00:00')
INVALID_WORK_WEEK_1['Thursday'] = ('09:00:00', '17:30:00')
INVALID_WORK_WEEK_1['Friday'] = ('09:30:00', '17:30:00')

INVALID_WORK_WEEK_2 = collections.OrderedDict()
INVALID_WORK_WEEK_2['Monday'] = ('09:00:00', '17:30:00')
INVALID_WORK_WEEK_2['Tuesday'] = ('09:30:00', '17:00:00')
INVALID_WORK_WEEK_2['Wednesday'] = ('09:00:00', '08:30:00')
INVALID_WORK_WEEK_2['Thursday'] = ('09:00:00', '17:30:00')
INVALID_WORK_WEEK_2['Friday'] = ('09:30:00', '17:30:00')

VALID_WORK_WEEK = collections.OrderedDict()
VALID_WORK_WEEK['Monday'] = ('07:45:00', '17:45:00')
VALID_WORK_WEEK['Tuesday'] = ('07:45:00', '17:45:00')
VALID_WORK_WEEK['Wednesday'] = ('07:45:00', '17:45:00')
VALID_WORK_WEEK['Thursday'] = ('07:45:00', '17:45:00')
VALID_WORK_WEEK['Friday'] = ('07:45:00', '17:45:00')

TEST_WORK_WEEKS = {'1':INVALID_WORK_WEEK_1, '2':INVALID_WORK_WEEK_2}
