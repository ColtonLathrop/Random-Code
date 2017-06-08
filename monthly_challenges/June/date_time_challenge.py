'''This is a script made for the 1st June coding challenge by study.py'''
from __future__ import print_function
import datetime
import sys

def get_difference(target, current):
    diff = target - current
    return str(diff)

def get_weeks(target, current):
    target_iso = target.isocalendar()
    current_iso = current.isocalendar()
    return str(target_iso[1] - current_iso[1]) + ' Weeks. '

def get_workdays(target, current):
    target_tuple = target.timetuple()
    current_tuple = current.timetuple()
    day_diff = target_tuple[7] - current_tuple[7]
    return str((day_diff - ((day_diff / 7)* 2)) + (day_diff % 7)) + ' Business Days.'

def compile_all():
    x = get_difference(target_date, current_date)
    y = get_weeks(target_date, current_date)
    z = get_workdays(target_date, current_date)
    return str(x) + str(y) + str(z)



while True:
    target_date = datetime.datetime(2017, 9, 22, 14, 11)
    current_date = datetime.datetime.today()
    print(compile_all(), end='\r')
    sys.stdout.flush()
