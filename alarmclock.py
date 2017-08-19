#https://www.reddit.com/r/beginnerprojects/comments/4n9hne/project_idea_alarm_clock/
#Make a program that accepts command line arguments for what time to go off, and when it does it should launch a Youtube video in your browser that will start playing.
#The program should read in a text file that contains URLs to different Youtube videos and will randomly choose one and launch it. My command line args were in the form of --hour <hour> --minute <minute> --<pm/am> but you should do whatever you feel is easiest or most convenient for you.
#source help:  https://pymotw.com/3/datetime/index.html, https://github.com/Pmogi/Alarm-Clock/blob/master/alarm.py

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

#start timedeltas



print('Earliest  :', datetime.time.min) #print Earliest  : 00:00:00
print('Latest    :', datetime.time.max) #print Latest    : 23:59:59.999999
print('Resolution:', datetime.time.resolution) #print Resolution: 0:00:00.000001
