'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

import datetime
from datetime import date

min = date(1901, 1, 1)
max = date(2000, 12, 31)
delta = max - min

date = datetime.date(1901, 1, 1)
numDays = 0

for i in range(delta.days + 1):
    if date.weekday() == 6 and date.day == 1:
        numDays += 1
    date += datetime.timedelta(days = 1)

print(numDays)
