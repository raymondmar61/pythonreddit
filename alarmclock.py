#https://www.reddit.com/r/beginnerprojects/comments/4n9hne/project_idea_alarm_clock/
#Make a program that accepts command line arguments for what time to go off, and when it does it should launch a Youtube video in your browser that will start playing.
#The program should read in a text file that contains URLs to different Youtube videos and will randomly choose one and launch it. My command line args were in the form of --hour <hour> --minute <minute> --<pm/am> but you should do whatever you feel is easiest or most convenient for you.
#source help:  https://pymotw.com/3/datetime/index.html, https://github.com/Pmogi/Alarm-Clock/blob/master/alarm.py
#created word file Python datetime.docx on 08/21/17
#Time module work with the clock time.  Calendar module work with dates.

import webbrowser
import datetime
import time
import random

#entire code for the alarm clock
# with open("alarmclockwebsites.txt","r") as fileobject:
# 	randomwebsitelist = fileobject.readlines()
# 	randomwebsite = random.choice(randomwebsitelist)
# currenttime = datetime.datetime.now()
# print("{:%H:%M:%S}".format(currenttime))
# setalarmclock = input("Enter alarm clock in 24 hour format 06:30: ")
# currenttimealarmclock = time.strftime("%H:%M")
# print(currenttimealarmclock)
# if setalarmclock == currenttimealarmclock:	
# 	webbrowser.open(randomwebsite)
# while setalarmclock != currenttimealarmclock:
# 	print("The time is " +currenttimealarmclock)
# 	time.sleep(10)
# 	#update currentalarmclock time to refresh the clock.  No infinite loop.
# 	currenttimealarmclock = time.strftime("%H:%M")
# 	if setalarmclock == currenttimealarmclock:
# 		webbrowser.open(randomwebsite)
# 		break

#self teaching date and time
today = datetime.date.today()
print(today) #print 2017-08-18
print(type(today)) #print <class 'datetime.date'>
print(today.ctime()) #print Fri Aug 18 00:00:00 2017 ctime is current time?
timetuplett = today.timetuple()
print(timetuplett.tm_year) #print 2017. year
print(timetuplett.tm_mon) #print 8. month jan is 1?
print(timetuplett.tm_mday) #print 18. month's day
print(timetuplett.tm_hour) #print 0
print(timetuplett.tm_min) #print 0
print(timetuplett.tm_sec) #print 0
print(timetuplett.tm_wday) #print 4. Mon is 0, Sun is 6. 
print(timetuplett.tm_yday) #print 230.  Day 230 of 365?
print(timetuplett.tm_isdst) #-1.  Daylight standard or savings time? -1 false?
print('ordinal:', today.toordinal()) #print 
print('Year   :', today.year) #print Year: 2017
print('Mon    :', today.month) #print Mon: 8
print('Day    :', today.day) #print Day 18

#assign a date
date1 = datetime.date(2008, 3, 29) #set the date .date(year,month,day)
print("date1",date1.ctime()) #print date1 Sat Mar 29 00:00:00 2008
date2 = date1.replace(year=2008)
print("date2",date2.ctime()) #print date1 Sat Mar 29 00:00:00 2009
print(type(date2)) #print <class 'datetime.date'>
#assign a time
t = datetime.time(23, 2, 10) #set the time .time(hour,minute,second)
print(t) #print 23:02:10 
print(type(t)) #print <class 'datetime.time'>
print(t.hour) #print 23
print(t.minute) #print 2
print(t.second) #print 10

#timedeltas
print('timedeltas microseconds:', datetime.timedelta(microseconds=1))
print('timedeltas milliseconds:', datetime.timedelta(milliseconds=1))
print('timedeltas seconds     :', datetime.timedelta(seconds=1))
print('timedeltas minutes     :', datetime.timedelta(minutes=1))
print('timedeltas hours       :', datetime.timedelta(hours=1))
print('timedeltas days        :', datetime.timedelta(days=1))
print('timedeltas weeks       :', datetime.timedelta(weeks=1))
"""
timedeltas microseconds: 0:00:00.000001
timedeltas milliseconds: 0:00:00.001000
timedeltas seconds     : 0:00:01
timedeltas minutes     : 0:01:00
timedeltas hours       : 1:00:00
timedeltas days        : 1 day, 0:00:00
timedeltas weeks       : 7 days, 0:00:00
"""
for delta in [datetime.timedelta(microseconds=1), datetime.timedelta(milliseconds=1), datetime.timedelta(seconds=1), datetime.timedelta(minutes=1), datetime.timedelta(hours=1), datetime.timedelta(days=1), datetime.timedelta(weeks=1)]:
    print('{:15} = {:8} seconds'.format(str(delta), delta.total_seconds()))
    """
    0:00:00.000001  =    1e-06 seconds
	0:00:00.001000  =    0.001 seconds
	0:00:01         =      1.0 seconds
	0:01:00         =     60.0 seconds
	1:00:00         =   3600.0 seconds
	1 day, 0:00:00  =  86400.0 seconds
	7 days, 0:00:00 = 604800.0 seconds
	"""
print("\n")

#date arithmetic
today = datetime.date.today()
print('Today    :', today)
one_day = datetime.timedelta(days=1)
print('One day  :', one_day)
yesterday = today - one_day
print('Yesterday:', yesterday)
tomorrow = today + one_day
print('Tomorrow :', tomorrow)
print('tomorrow - yesterday:', tomorrow - yesterday)
print('yesterday - tomorrow:', yesterday - tomorrow)
"""
Today    : 2017-08-21
One day  : 1 day, 0:00:00
Yesterday: 2017-08-20
Tomorrow : 2017-08-22
tomorrow - yesterday: 2 days, 0:00:00
yesterday - tomorrow: -2 days, 0:00:00
"""
one_day = datetime.timedelta(days=1)
print('One day  :', one_day)
print('5 days   :', one_day * 5)
print('1.5 days :', one_day * 1.5)
print('1/4 day  :', one_day / 4)
"""
One day  : 1 day, 0:00:00
5 days   : 5 days, 0:00:00
1.5 days : 1 day, 12:00:00
1/4 day  : 6:00:00
"""
work_day = datetime.timedelta(hours=7)
meeting_length = datetime.timedelta(hours=1)
print('meetings per day :', work_day / meeting_length) #print meetings per day : 7.0
print("\n")

#date and time values can be compared using the standard comparison operators to determine which is earlier or later
print('Times:')
t1 = datetime.time(12, 55, 0) #12:55:00
print('  t1:', t1)
t2 = datetime.time(13, 5, 0) #13:05:00
print('  t2:', t2)
print('  t1 < t2:', t1 < t2)
print('Dates:')
d1 = datetime.date.today()
print('  d1:', d1)
d2 = datetime.date.today() + datetime.timedelta(days=1)
print('  d2:', d2)
print('  d1 > d2:', d1 > d2)
"""
Times:
  t1: 12:55:00
  t2: 13:05:00
  t1 < t2: True

Dates:
  d1: 2017-07-30
  d2: 2017-07-31
  d1 > d2: False
"""
print("\n")

#Use the datetime class to hold values consisting of both date and time components
print('Now    :', datetime.datetime.now())
print('Today  :', datetime.datetime.today())
print('UTC Now:', datetime.datetime.utcnow())
"""
Now    : 2017-08-21 14:57:18.140436
Today  : 2017-08-21 14:57:18.140445
UTC Now: 2017-08-21 21:57:18.140450
"""
FIELDS = ['year', 'month', 'day','hour', 'minute', 'second','microsecond']
d = datetime.datetime.now()
for attr in FIELDS:
    print('{:15}: {}'.format(attr, getattr(d, attr)))
"""
year           : 2017
month          : 8
day            : 21
hour           : 14
minute         : 58
second         : 38
microsecond    : 968829
"""
print("month", datetime.datetime.now().month) #print month 8
print("year", datetime.datetime.now().year) #print month 2017
print("today is", datetime.datetime.now().month,"/",datetime.datetime.now().day) #print today is 8 / 21
print("\n")

#start Formatting and Parsing page 12 word file
#The default string representation of a datetime object uses the ISO-8601 format (YYYY-MM-DDTHH:MM:SS.mmmmmm). Alternate formats can be generated using strftime().
today = datetime.datetime.today()
print("default datetime today",today) #print default datetime today; 2017-08-23 12:47:32.981897
format = "%a %b %d %H:%M:%S %Y"
s = today.strftime(format)
print("""strftime format %a %b %d %H:%M:%S %Y""",s) #print strftime format %a %b %d %H:%M:%S %Y Wed Aug 23 12:49:45 2017
#Use datetime.strptime() to convert formatted strings to datetime instances.
d = datetime.datetime.strptime(s, format)
print('strptime:', d.strftime(format)) #print strptime: Wed Aug 23 12:50:54 2017
print('ISO     :', today) #print ISO     : 2017-08-23 12:53:36.677435
print('format(%a %b %d %H:%M:%S %Y): {:%a %b %d %H:%M:%S %Y}'.format(today)) #print format(%a %b %d %H:%M:%S %Y): Wed Aug 23 12:54:04 2017.  Each datetime format code must still be prefixed with %, and subsequent colons are treated as literal characters to include in the output.
"""
Formatting codes for 5:00 PM January 13, 2016 in the US/Eastern time zone.
%a  Abbreviated weekday name:  'Wed'
%A  Full weekday name: 'Wednesday'
%w  Weekday number – 0 (Sunday) through 6 (Saturday):  '3'
%d  Day of the month (zero padded):  '13'
%b  Abbreviated month name:  'Jan'
%B  Full month name: 'January'
%m  Month of the year: '01'
%y  Year without century:  '16'
%Y  Year with century: '2016'
%H  Hour from 24-hour clock: '17'
%I  Hour from 12-hour clock: '05'
%p  AM/PM: 'PM'
%M  Minutes: '00'
%S  Seconds: '00'
%f  Microseconds:  '000000'
%z  UTC offset for time zone-aware objects:  '-0500'
%Z  Time Zone name:  'EST'
%j  Day of the year: '013'
%W  Week of the year:  '02'
%c  Date and time representation for the current locale: 'Wed Jan 13 17:00:00 2016'
%x  Date representation for the current locale:  '01/13/16'
%X  Time representation for the current locale:  '17:00:00'
%%  A literal % character: '%'
"""
format = "%a %b %d, %Y"
mytoday = today.strftime(format)
print("Today is",mytoday) #Today is Wed Aug 23, 2017
print("\n")

#timezones
min6 = datetime.timezone(datetime.timedelta(hours=-6))
plus6 = datetime.timezone(datetime.timedelta(hours=6))
d = datetime.datetime.now(min6)
print(min6, ':',d)
print(datetime.timezone.utc, ':',d.astimezone(datetime.timezone.utc))
print(plus6, ':',d.astimezone(plus6))
# convert to the current system timezone
d_system = d.astimezone()
print(d_system.tzinfo, '      :', d_system)
"""
UTC-06:00 : 2017-08-23 14:06:36.166516-06:00
UTC+00:00 : 2017-08-23 20:06:36.166516+00:00
UTC+06:00 : 2017-08-24 02:06:36.166516+06:00
PDT       : 2017-08-23 13:06:36.166516-07:00
"""
#The third party module pytz is a better implementation for time zones. It supports named time zones, and the offset database is kept up to date as changes are made by political bodies around the world.

#Time module work with the clock time.  Calendar module work with dates.

print('Earliest  :', datetime.time.min) #print Earliest  : 00:00:00
print('Latest    :', datetime.time.max) #print Latest    : 23:59:59.999999
print('Resolution:', datetime.time.resolution) #print Resolution: 0:00:00.000001
