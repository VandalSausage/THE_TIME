''' functions to do the Truman time converstions '''
import time
import math as m
import collections

# turns time (string) into decimal representation of hours since midnght
# 08:30 -> 8.5
def time_conv(string):
    ''' time conv '''
    hour_f = float(string[:2])
    minute_f = float(string[3:5])
    second_f = float(string[6:8])
    decimated_time = float((hour_f)+(minute_f/60))+(second_f/(60**2))
    return decimated_time

# Does opposite of time_conv
def time_inv(number):
    ''' time inv '''
    t_1 = m.floor(number)
    h_2 = ((number-t_1)*(60))
    t_2 = m.floor(h_2)
    h_3 = h_2-t_2
    t_3 = int(h_3*60)
    output = [str(t_1), str(t_2), str(t_3)]
    for k in range(3):
        if len(output[k]) == 1:
            join = ['0', output[k]]
            output[k] = "".join(join)
    time_f = ":".join(output)
    return time_f

def truman_time_converter(work_week, timestamp, day):
    ''' displays the current day/time converted to the using Truman's code'''

    if day in work_week:
        start_time = work_week[day][0]
        end_time = work_week[day][1]
        # a to be replaced by start time (in hrs decimals)
        a = work_week[day][2]
        b = work_week[day][3]

        if time_conv(timestamp) < time_conv(start_time) or time_conv(timestamp) \
            > time_conv(end_time):
            time_f = 'You are off the clock right now - get it together'
        else:
            h = (time_conv(timestamp)-time_conv(start_time))

            # actual hours into the day
            h_actual = ((h/(time_conv(end_time)-time_conv(start_time)))*b)+a
            time_f = 'But the real time is {}'.format(time_inv(h_actual))

    else:
        time_f = 'Why are you checking this on the weekend, you maniac?'
    return time_f


def time_day():
    ''' returns the time formatted as Day-of-week hh:mm:ss '''

    # Current datetime
    t = time.localtime()

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
    today = week[t[6]]

    # Get time
    hour_second_min = [str(t[3]), str(t[4]), str(t[5])]

    for k in range(3):
        if len(hour_second_min[k]) == 1:
            join = ['0', hour_second_min[k]]
            hour_second_min[k] = "".join(join)

    # generate the timestamp
    timestamp = ("{}".format((":".join(hour_second_min))))

    # return timestamp and day
    return timestamp, today

def make_new_data(work_week_data):

    hrs_in_week = []
    dec_start_times_in_week = []
    actual_hours_in_day = []

    total_hours = 0
    total_start_hours = 0
    total_end_hours = 0

    # first loop to build list about the 'actual day'
    for key, value in work_week.items():

        # using the a and the b
        start_time = value[0]
        end_time = value[1]

        dec_start_time = time_conv(start_time)
        dec_end_time = time_conv(end_time)

        hours_in_day = dec_end_time - dec_start_time

        total_start_hours += dec_start_time
        total_end_hours += dec_end_time

        total_hours += hours_in_day

        # append things
        hrs_in_week.append(hours_in_day)
        dec_start_times_in_week.append(dec_start_time)
        actual_hours_in_day.append(hours_in_day)

    # calculate "average day"
    average_start = total_start_hours/5
    average_end = total_end_hours/5
    average_day = average_end - average_start

    # debug
    # second loop to put back into dictionary information about the day in the 'actual day'
    countup = 0
    for key,value in work_week_data.items():
        print(key)

        # get time through actaul 'day' you are
        time_through_actual_day = \
        sum([x for ind, x in enumerate(dec_start_times_in_week) if ind < countup])

        new_data = \
            (value[0], value[1], time_through_actual_day, actual_hours_in_day[countup])

        print(new_data)
        work_week_data[key] = new_data
        countup+=1

    return work_week_data

#########################################
## DEBUG:

work_week = collections.OrderedDict()
work_week['Monday'] = ('07:45:00', '15:07:56')
work_week['Tuesday'] = ('07:45:00', '19:07:56')
work_week['Wednesday'] = ('07:45:00', '18:07:56')
work_week['Thursday'] = ('07:45:00', '16:07:56')
work_week['Friday'] = ('07:45:00', '17:07:56')

# aisha_work_week = {
#     'Monday': ('07:45:00', '16:07:56'),
#     'Tuesday': ('05:32:45', '17:45:03'),
#     'Wednesday': ('05:38:43', '17:20:09'),
#     'Thursday': ('05:28:54', '18:05:23'),
#     'Friday': ('08:35:21', '17:01:09'),
#     }

# take is start and end times of work Day

# calclate decimals hours in each day

# calculate sum of decimal hours in each day

# calculate "average day"

t_timestamp, t_day = time_day()



new_time(work_week,t_day)
time_conv('07:45:00')
