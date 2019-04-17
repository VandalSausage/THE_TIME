
# coding: utf-8

# In[1]:


import os
import numpy as np
import math as m
import sys
import numpy.polynomial.polynomial as poly
import time


# In[2]:


#define input data
#input 1: all working days with start and end times
#input 2: timestamp (time.local_time) - to be called in function

#input 1
#format: [['day of the week, 0=Monday etc...', start_time, end_time]......
working_times=[]
working_times.append([2,'07:45:00','17:45:00'])
working_times.append([3,'07:45:00','17:45:00'])
working_times.append([4,'07:45:00','17:45:00'])
working_times.append([0,'07:45:00','17:45:00'])
working_times.append([1,'07:45:00','17:45:00'])

#days can be added in any order and will then be sorted into acsending order 
#(say if you wanted to iteratively create a list of working times from an un-ordered dictionary)
def take_first_element(List):
    return List[0]

working_times.sort(key=take_first_element)


# In[36]:


#converts a string in form 00:00:00 to hours since midnight (00:00:00 = 0, 07:45:00 = 7.75)
def time_conv(string):
    hours=int(string[:2])
    minutes=int(string[3:5])
    seconds=int(string[6:8])
    decimated_hours=((hours)+(minutes/60))+(seconds/(60**2))
    return decimated_hours


# In[57]:


#converts decimated hours to a string in form 00:00:00 (0 = 00:00:00, 7.75 = 07:45:00)
#inverse of time_conv

def time_inv(number):
    round_number_of_hours=m.floor(number)
    total_number_of_minutes=(number-round_number_of_hours)*60
    round_number_of_minutes=m.floor(total_number_of_minutes)
    total_number_of_seconds=(total_number_of_minutes-round_number_of_minutes)*60
    round_number_of_seconds=int(total_number_of_seconds)
    output=[str(round_number_of_hours),str(round_number_of_minutes),str(round_number_of_seconds)]
    for k in range(3):
        if len(output[k]) == 1:
            join=['0',output[k]]
            output[k]="".join(join)
        
    time_formatted=":".join(output)
    return time_formatted


# In[58]:


print(time_inv(7.36))


# In[59]:


#from the working times need to work out:
# a start time of the average day, an endtime oh the average day and the 'a' and 'b' value per day

def WT_parameter_calculation(working_times):
    #create a set of working days
    working_days=[]
    for i in range(len(working_times)):
        working_days.append(working_times[i][0])


    #find start times in hours from midnight of that day (07:45 = 7.75)
    decimated_start_times=[]
    for i in range(len(working_times)):
        decimated_start_times.append(time_conv(working_times[i][1]))


    #calculate mean for average day start time (still decimated)
    actual_day_start_time=(sum(decimated_start_times)/len(decimated_start_times))


    #calculate the length of each working day in decimated hours
    day_lengths=[]
    for i in range(len(working_times)):
        day_lengths.append(time_conv(working_times[i][2])-time_conv(working_times[i][1]))


    #calculate mean for average day length (still decimated)
    actual_day_length=(sum(day_lengths)/len(day_lengths))


    #calculate the length of each day relative to the actual day (i.e b values)
    b_values=[]
    for i in range(len(decimated_start_times)):
        b_values.append((((day_lengths[i])/sum(day_lengths))*actual_day_length))
   
    #starttimes converted to decimal hours through the 'actual day' (i.e. a values)
    a_values=[]
    for i in range(len(decimated_start_times)):
        a_values.append(actual_day_start_time + ((sum(day_lengths[:i])/sum(day_lengths))*actual_day_length))   
    
    
    return working_days,a_values,b_values


# In[60]:


def actual_time_conv(input):
    day=input[1] 
    hour=int(input[0][:2])
    minute=int(input[0][3:5])
    second=int(input[0][6:8])
    not_a_real_boolean=0
    
    for i in range(len(working_days)):
        if day == working_days[i]:
            start_time  = working_times[i][1]
            end_time    = working_times[i][2]
            a           = WT_parameter_calculation(working_times)[1][i]
            b           = WT_parameter_calculation(working_times)[2][i]
            not_a_real_boolean=1 
    
    if not_a_real_boolean == 1:
        if time_conv(input[0]) < time_conv(start_time) or time_conv(input[0]) > time_conv(end_time):
            time_f='You are off the clock right now - get it together'
        else:
            h=(time_conv(input[0])-time_conv(start_time))
    
            #actual hours into the day
            h_a=((h/(time_conv(end_time)-time_conv(start_time)))*b)+a
            time_f = time_inv(h_a)
    else:
        if day not in WT_parameter_calculation(working_times)[0]:
            time_f = 'Why are you checking this? Its not a work day! You maniac!'
        else:
            time_f = 'Learn to type, jesus'
    return time_f
    


# In[61]:


def actual_time():
    t = time.localtime()
    
    output=[str(t[3]),str(t[4]),str(t[5])]
    for k in range(3):
        if len(output[k]) == 1:
            join=['0',output[k]]
            output[k]="".join(join)
       
    formatter=(":".join(output))
    
    time_f= actual_time_conv([formatter,t[6]])
    return time_f


# In[62]:


print(actual_time())


# In[63]:


print(actual_time_conv(['13:10:56', 0]))

