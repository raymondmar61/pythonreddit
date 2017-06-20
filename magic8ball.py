#https://www.reddit.com/r/beginnerprojects/comments/29aqox/project_magic_8_ball/
#Goal I'm sure you've used a magic 8 ball at one point in your life. You ask it a question, turn it right side up and it gives an answer by way of a floating die with responses written on it. You can create one in python. You must:
#Allow the user to enter their question
#Display an in progress message( i.e. "thinking")
#Create 20 responses, and show a random response
#Allow the user to ask another question or quit
#Bonus Using whatever module you like, add a gui. Your gui must have:
#A box for users to enter the question
#At least 4 buttons: Ask , clear(the text box), play again and quit(this must close the window)
#Time delay in python: https://stackoverflow.com/questions/510348/how-can-i-make-a-time-delay-in-python
#fortune telling ball sayings: http://www.ginifab.com/gift/magic_8_ball_sayings.html

import random, time

def magicanswer():
	fortuneresponses = ["Screw you","Forget it kid","It's going to happen","Outcome is hazy","I see it happeneing in your next life","Hell must freeze first","Be patient","As I See It Yes","Ask Again Later","Better Not Tell You Now","Cannot Predict Now","Concentrate and Ask Again","Don't Count On It","It Is Certain","It Is Decidedly So","Most Likely","My Reply Is No","My Sources Say No","Outlook Good","Outlook Not So Good","Reply Hazy Try Again","Signs Point to Yes","Very Doubtful","Without A Doubt","Yes","Yes - Definitely","You May Rely On It","Absolutely","Answer Unclear Ask Later","Cannot Foretell Now","Can't Say Now","Chances Aren't Good","Consult Me Later","Don't Bet On It","Focus And Ask Again","Indications Say Yes","Looks Like Yes","No","No Doubt About It","Positively","Prospect Good","So It Shall Be","The Stars Say No","Unlikely","Very Likely","Yes","You Can Count On It"]
	highest = len(fortuneresponses)
	fortune = random.randrange(0,highest-1)
	# if fortune == 1:
	# 	return "Screw you"
	# elif fortune == 2:
	# 	return "Forget it kid"
	# elif fortune == 3:
	# 	return "It's going to happen"
	# elif fortune == 4:
	# 	return "Outcome is hazy"
	# elif fortune == 5:
	# 	return "I see it happeneing in your next life"
	# elif fortune == 6:
	# 	return "Hell must freeze first"
	# elif fortune == 7:
	# 	return "Be patient"
	return fortuneresponses[fortune]

def progressmessage():
	seconds = 1
	while seconds < 6:
		print("Thinking!")
		time.sleep(1)  #delay for 1 second
		seconds += 1

while True:
	userquestion = "\nI predict your fortune.  Type q to quit."
	userquestion += "\nWhat is your question? "
	userinput = input(userquestion)
	if userinput == "q":
		break	
	#print("Thinking!")
	#time.sleep(5) #delay for 5 seconds
	progressmessage()
	print(magicanswer())