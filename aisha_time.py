''' functions to do the Truman time converstions
a WORK DAY is a real day and the hours you work, as stated in your contract or in practice
e.g.: Monday, 08:30 to 17:00
an ACTAUL DAY is if the sum of your working days in one week were represented as one 'day'
the number of hours in your WORK WEEK == number of hours in your ACTUAL DAY

Process of calculating the time:
- Input of start and end times of work day
- Calclate decimal hours in each day
- Calculate sum of decimal hours in each day in order to Calculate "average day" i.e. the Actual Day
- Find how much of a proportion of the Actual day each work day is
- Convert work day time to actual time
- Output Actual Time
'''
from datetime import datetime
import math as m

DEBUG = False

################################################################################
## FUNCTIONS ###################################################################

def time_day():
    ''' returns the current time formatted as
    "Day-of-week hh:mm:ss" '''

    # Get day of week
    week = {
        0:"Monday",
        1:"Tuesday",
        2:"Wednesday",
        3:"Thursday",
        4:"Friday",
        5:"Saturday",
        6:"Sunday"
        }

    today = week[datetime.today().weekday()]

    if DEBUG:
        print(today)

    # Get timestamp
    timestamp = ("{}").format(datetime.now().strftime("%H:%M:%S"))

    if DEBUG:
        print(timestamp)

    # return timestamp and day
    return timestamp, today

def timestamp_to_decimal(timestamp):
    ''' turns timestamp string "hh:mm" into decimal representation of hours since midnight
        e.g.: 08:30 -> 8.5 '''

    invalid_data_error = "ERROR: timestamp supplied is not valid"

    # split timestamp
    split_timestamp = timestamp.split(':')

    # first validation check
    if len(split_timestamp) != 3:
        return invalid_data_error

    else:
        # second validation check
        for time_frag in split_timestamp:
            if len(time_frag) > 2:
                return invalid_data_error

        # split out the timestamp into hrs, mins, secs
        hours = float(split_timestamp[0])
        mins = float(split_timestamp[1])
        seconds = float(split_timestamp[2])

        # third validation check
        if hours < 0 or hours > 23 or mins < 0 or mins > 59 or seconds < 0 or seconds > 59:
            return invalid_data_error

        # turn the timestamp into a decimal number
        decimal_time = float((hours)+(mins/60))+(seconds/(60**2))

        return decimal_time

def decimal_time_to_timestamp(decimal_time):
    ''' does opposite of time `timestamp_to_decimal` function
        turns decimal representation of hours since midnght into a timestamp
        e.g.: 8.5 -> 08:30 '''

    invalid_data_error = "ERROR: decimal time supplied is not valid"

    # check data is valid
    if decimal_time < 0 or decimal_time >= 24:
        return invalid_data_error

    else:
        hours = m.floor(decimal_time)
        leftover_mins = (decimal_time - hours)*60
        mins = m.floor(leftover_mins)
        leftover_secs = leftover_mins-mins
        secs = int(leftover_secs * 60)

        output = [str(hours), str(mins), str(secs)]

        for k in range(3):
            if len(output[k]) == 1:
                join = ['0', output[k]]
                output[k] = "".join(join)
        timestamp = ":".join(output)

        return timestamp

def work_week_and_actual_day(work_week_data):
    ''' Takes in ordered dictionary of your actual days worked with start and end times
    adds to this data structure to include information of that work day's start time on the
    Actual Day and the proportion of the Actual Day it takes up '''

    # Error checking
    # define vaild work days
    valid_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # error text
    data_error = 'Something wrong with your work week'

    # number of days in work week
    week_length = len(work_week_data)

    # work out the start and end of your actual day from averages of your week days

    # list of hours worked in each work day
    # length will be equal to work days in work week
    daily_hrs_in_work_week = []

    # countups
    total_start_hours, total_end_hours = 0, 0

    # first loop to build information about the 'actual day'
    for key, value in work_week_data.items():

        if DEBUG:
            print(key)

        # first data validation check
        if key not in valid_week:
            return data_error

        else:

            # Find the start and end times for that day
            start_time = value[0]
            end_time = value[1]

            # turn these into decimal numbers
            dec_start_time = timestamp_to_decimal(start_time)
            dec_end_time = timestamp_to_decimal(end_time)

            # second data validation check that end time is after start time
            if dec_start_time > dec_end_time:
                if DEBUG:
                    print(dec_start_time, dec_end_time, dec_start_time > dec_end_time)
                return data_error

            # find the hours in each work day and add to list
            hrs_in_work_day = dec_end_time - dec_start_time
            daily_hrs_in_work_week.append(hrs_in_work_day)

            # possibly not needed
            total_start_hours += dec_start_time
            total_end_hours += dec_end_time

    # calculate "average work day"
    # - this is the how long your actual day will last and what time it starts and ends
    average_start = total_start_hours / week_length

    # second loop to put back into dictionary information about
    #work day's relationship to 'actual day'
    countup = 0
    for key, value in work_week_data.items():

        # get proportion of 'actual day' your work day is
        # endtime - starttime / total_end
        proportion_of_actual_day = daily_hrs_in_work_week[countup] / week_length

        # get time through actaul 'day' you are
        time_through_actual_day = average_start + proportion_of_actual_day * countup

        # make the new data structure
        new_data = (value[0], value[1], \
            time_through_actual_day, proportion_of_actual_day)

        # print(new_data)
        work_week_data[key] = new_data
        countup += 1

    if DEBUG:
        print(work_week_data)
    return work_week_data

def the_actual_time(work_week, timestamp, day):
    ''' displays the current day/time converted to the Actual Time
    outputs friendly text including time (if you are on the clock) '''

    # get extra information about the 'actual day' based on work week data
    work_week = work_week_and_actual_day(work_week)

    if day in work_week:

        # read data structure
        start_time = work_week[day][0]
        end_time = work_week[day][1]
        hrs_thru_actual_day = work_week[day][2]
        prop_of_actual_day = work_week[day][3]

        # if not in work day, you don't need to know the time!
        if timestamp_to_decimal(timestamp) < timestamp_to_decimal(start_time) \
        or timestamp_to_decimal(timestamp) > timestamp_to_decimal(end_time):
            actual_time_text = 'You are off the clock right now - get it together'

        # find what the actual time is
        else:
            time_through_day = \
                (timestamp_to_decimal(timestamp)-timestamp_to_decimal(start_time))

            # actual hours into the day
            h_actual = \
                ((time_through_day/(timestamp_to_decimal(end_time)- \
                timestamp_to_decimal(start_time))) * prop_of_actual_day) + hrs_thru_actual_day
            actual_time_text = 'But the real time is {}'.format(decimal_time_to_timestamp(h_actual))

    # the day you are looking up is not part of your work week
    else:
        actual_time_text = 'Why are you checking this on the weekend, you maniac?'

    return actual_time_text
