
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import os
import numpy as np
import scipy as sp
from scipy.interpolate import interp1d
import math as m
#matplotlib.use('Agg')
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.gridspec as gridspec
import sys
import numpy.polynomial.polynomial as poly
import time


# In[10]:


def time_conv(string):
    hour_f=int(string[:2])
    minute_f=int(string[3:5])
    second_f=int(string[6:8])
    h_f=((hour_f)+(minute_f/60))+(second_f/(60**2))
    print(h_f)
    return h_f


# In[3]:


def time_inv(number):
    t_1=m.floor(number)
    h_2=((number-t_1)*(60))
    t_2=m.floor(h_2)
    h_3=h_2-t_2
    t_3=int(h_3*60)
    output=[str(t_1),str(t_2),str(t_3)]
    for k in range(3):
        if len(output[k]) == 1:
            join=['0',output[k]]
            output[k]="".join(join)
        
    time_f=":".join(output)
    return time_f


# In[4]:


def actual_time_conv(input):
    day=input[10:] 
    hour=int(input[:2])
    minute=int(input[3:5])
    second=int(input[6:8])
    boolean=1
    #print(day)

    if day != 'Monday':
        if day != 'Tuesday':
            if day != 'Wednesday':
                if day != 'Thursday':
                    if day != 'Friday':
                        boolean=0
                    else:
                        start_time='08:35:21'
                        end_time= '17:01:09'
                        a=15
                        b=1
                else:
                    start_time='05:28:54'
                    end_time= '18:05:23'
                    a=13
                    b=2
            else:
                start_time= '05:38:43'
                end_time= '17:20:09'
                a=11
                b=2
        else:
            start_time= '05:32:45'
            end_time= '17:45:03'
            a=9
            b=2
    else:    
        start_time='07:45:00'
        end_time= '16:07:56'
        a=8
        b=1
     
    
    if boolean != 0:
        if time_conv(input) < time_conv(start_time) or time_conv(input) > time_conv(end_time):
            time_f='You are off the clock right now - get it together'
        else:
            h=(time_conv(input)-time_conv(start_time))
    
            #actual hours into the day
            h_a=((h/(time_conv(end_time)-time_conv(start_time)))*b)+a
            time_f = time_inv(h_a)
    else:
        if day == 'Saturday' or day == 'Sunday':
            time_f = 'Why are you checking this on the weekend, you maniac?'
        else:
            time_f = 'Learn to type, jesus'
    return time_f
    


# In[5]:


def actual_time():
    t = time.localtime()
    
    if t[6] == 5 or t[6]==6:
        time_f= 'Why are you checking this on the weekend, you maniac?'
    else:
        if t[6] == 0:
            day='Monday'
        if t[6] == 1:
            day='Tuesday'
        if t[6] == 2:
            day='Wednesday'
        if t[6] == 3:
            day='Thursday'
        if t[6] == 4:
            day='Friday'
        
        output=[str(t[3]),str(t[4]),str(t[5])]
        for k in range(3):
            if len(output[k]) == 1:
                join=['0',output[k]]
                output[k]="".join(join)
       
        formatter=(":".join(output),day)
        #print((", ".join(formatter)))
        time_f= actual_time_conv(", ".join(formatter))
    return time_f


# In[6]:


print(actual_time())


# In[7]:


print(actual_time_conv('13:10:29, Wednesday'))


# In[8]:


name = input("Give me your name: ")
print("Your name is " + name)


# In[11]:


time_conv('07:45:00')

