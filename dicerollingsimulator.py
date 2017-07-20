#https://www.reddit.com/r/beginnerprojects/comments/1j50e7/project_dice_rolling_simulator/
#By using the random module, python can do things like pseudo-random number generation. So in this program, allow the user to input the amount of sides on a dice and how many times it should be rolled. From there, your program should simulate dice rolls and keep track of how many times each number comes up (this does not have to be displayed). After that, print out how many times each number came up.
#Adjust your program so that if the user does not type in a number when they need to, the program will keep prompting them to type in a real number until they do so.
#Put the program into a loop so that the user can continue to simulate dice rolls without having to restart the entire program.
#In addition to printing out how many times each side appeared, also print out the percentage it appeared. If you can, round the percentage to 4 digits total OR two decimal places.

import random

def integercheck(message):
	while True:		
		try:
			userinput = int(input(message))			
			if userinput > 0:
				return userinput
				break
			else:
				print("Error.  Need a positive integer.")
				continue
		except ValueError:
			print("Error.  Need an integer.")
			continue
		else:
			return userinput
			break
go = "y"
while go != "q":
	dicesides = integercheck("How many sides are on a dice? ")
	dicerolls = integercheck("How many times I roll the dice? ")
	diceresultlist = []
	for eachroll in range(1,dicerolls+1):
		diceresult = random.randrange(1,dicesides+1)
		diceresultlist.append(diceresult)
	print(diceresultlist)
	for eachside in range(1,dicesides+1):
		dicerolltracker = diceresultlist.count(eachside)
		print(eachside,"appeared",dicerolltracker,"times.","Percentage", round(100*(dicerolltracker/dicerolls),4))
	go = input("Type 'y' to continue  or type 'q' to quit ")

# #How to make sure the user enters a number (integer) - www.101computing.net
# def inputNumber(message):
#   while True:
#     try:
#        userInput = int(input(message))       
#     except ValueError:
#        print("Not an integer! Try again.")
#        continue
#     else:
#        return userInput 
#        break
# #MAIN PROGRAM STARTS HERE:
# age = inputNumber("How old are you?")
# if (age>=18):
#   print("You are old enough to vote.")
# else:
#   print("You will be able to vote in " + str(18-age) + " year(s).")


# dicesides = int(input("How many sides are on a dice? "))
# dicerolls = int(input("How many times I roll the dice "))
# diceresultlist = []
# for eachroll in range(1,dicerolls+1):
# 	diceresult = random.randrange(1,dicesides+1)
# 	diceresultlist.append(diceresult)
# print(diceresultlist)
# for eachside in range(1,dicesides+1):
# 	dicerolltracker = diceresultlist.count(eachside)
# 	print(eachside,"appeared",dicerolltracker,"times")