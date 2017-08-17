#https://www.reddit.com/r/beginnerprojects/comments/4n9hne/project_idea_alarm_clock/
#Make a program that accepts command line arguments for what time to go off, and when it does it should launch a Youtube video in your browser that will start playing.
#The program should read in a text file that contains URLs to different Youtube videos and will randomly choose one and launch it. My command line args were in the form of --hour <hour> --minute <minute> --<pm/am> but you should do whatever you feel is easiest or most convenient for you.
#source help:  https://pymotw.com/3/datetime/index.html, https://github.com/Pmogi/Alarm-Clock/blob/master/alarm.py

import webbrowser
import datetime
import time

t = datetime.time(23, 2, 10) #h,m,s
print(t)
print(t.hour)
print(t.minute)
print(t.second)

setalarmclock = input("Enter alarm clock in 24 hour format 06:30: ")
currenttime = datetime.datetime.now()
print("{:%H:%M:%S}".format(currenttime))
currenttimealarmclock = time.strftime("%H:%M")
print(currenttimealarmclock)

if setalarmclock == currenttimealarmclock:
	print("test")
	#webbrowser.open("http://www.innovateinfinitely.com")
while setalarmclock != currenttimealarmclock:
	print("The time is " +currenttimealarmclock)
	time.sleep(10)
	#update currentalarmclock time to refresh the clock.  No infinite loop.
	currenttimealarmclock = time.strftime("%H:%M")
	if setalarmclock == currenttimealarmclock:
		print("test")
		break




today = datetime.date.today()
print(today)