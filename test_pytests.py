import pytest
import collections
from aisha_time import time_day, timestamp_to_decimal, \
    decimal_time_to_timestamp, work_week_and_actual_day, the_actual_time
from THE_TIME import time_conv, time_inv, WT_parameter_calculation, \
    actual_time_conv, actual_time

################################################################################
## TEST DATA ###################################################################

WORK_WEEK = collections.OrderedDict()
WORK_WEEK['Monday'] = ('09:00:00', '17:30:00')
WORK_WEEK['Tuesday'] = ('09:30:00', '17:00:00')
WORK_WEEK['Wednesday'] = ('09:00:00', '17:00:00')
WORK_WEEK['Thursday'] = ('09:00:00', '17:30:00')
WORK_WEEK['Friday'] = ('09:30:00', '17:30:00')

NOW, DAY_OF_WEEK = time_day()
ACTUAL_TIME = the_actual_time(WORK_WEEK, NOW, DAY_OF_WEEK)

TEST_TIMESTAMP = "08:30:00"
TEST_TIME_DECIMAL = 8.5

################################################################################
## AISHA CODE TESTS ############################################################

def test_timestamp_to_decimal():
    ''' given a timestamp in the format hh:mm:ss
        when the input is valid
        then it is converted to a decimal representation of the time '''
    assert timestamp_to_decimal(TEST_TIMESTAMP) == TEST_TIME_DECIMAL

def test_decimal_time_to_timestamp():
    ''' given an decimal time input
        when the input is valid (between 0 and 24)
        then it is converted to a timestamp '''
    assert decimal_time_to_timestamp(TEST_TIME_DECIMAL) == TEST_TIMESTAMP

def weekend_error():
    ''' given an (input) which is not a WORK DAY
        then no ACTAUL TIME is shown
        and an error message is shown '''

def after_hours_error():
    ''' given a REAL TIME (input) which is outside of working hours
        then no ACTAUL TIME is shown
        and an error message is shown '''

################################################################################
## TRUMAN CODE TESTS ###########################################################

# def test_time_inv():
#     assert time_inv(TEST_TIMESTAMP) == TEST_TIME_DECIMAL
#
# def test_time_conv():
#     assert time_conv(TEST_TIME_DECIMAL) == TEST_TIMESTAMP
