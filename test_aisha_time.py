import pytest
import collections
from aisha_time import time_day, timestamp_to_decimal, \
    decimal_time_to_timestamp, work_week_and_actual_day, the_actual_time

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
## TESTS #######################################################################

def test_timestamp_to_decimal():
    assert timestamp_to_decimal(TEST_TIMESTAMP) == TEST_TIME_DECIMAL

def test_decimal_time_to_timestamp():
    assert decimal_time_to_timestamp(TEST_TIME_DECIMAL) == TEST_TIMESTAMP
