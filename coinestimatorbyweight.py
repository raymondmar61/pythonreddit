#https://www.reddit.com/r/beginnerprojects/comments/1idqw1/project_coin_estimator_by_weight/
#Create a program that allows the user to input the total weight of each type of coin they have (pennies, nickels, dimes, and quarters), and then print out how many of each type of wrapper they would need, how many coins they have, and the estimated total value of all of their money.
#For example, if you weigh all of your dimes and see that you have 1276.9g of them, you can estimate that you have about 563 dimes (since each one is 2.268g) and you would be able to fill 11 dime wrappers.  One dime wrap is 113.4g.  1276.9/563=2.268.  1276.9/113.4 = 11.26.
#Round all numbers printed out to the nearest whole number.
#Allow the user to select whether they want to submit the weight in either grams or pounds.

import math

def numberofwrappersg(cointype, coinweight):
	if cointype == "cent":
		return math.ceil(coinweight / 125)
	elif cointype == "nickle":
		return math.ceil(coinweight / 200)
	elif cointype == "dime":
		return math.ceil(coinweight / 113.4)
	elif cointype == "quarter":
		return math.ceil(coinweight / 226.8)
	else:
		return("Uncommon coin.  Information unavailable.")
def numberofwrapperslb(cointype, coinweight):
	if cointype == "cent":
		return math.ceil(coinweight / 0.275578)
	elif cointype == "nickle":
		return math.ceil(coinweight / 0.440925)
	elif cointype == "dime":
		return math.ceil(coinweight / 0.250004)
	elif cointype == "quarter":
		return math.ceil(coinweight / 0.500008)
	else:
		return("Uncommon coin.  Information unavailable.")
userinput = input("Enter cointype cent, nickle, dime, or quarter, follow by a space, weight of coins, followed by a space, and lb for pounds or g for grams. ")
userinput = userinput.split(" ")
if userinput[2] == "lb":
	print(numberofwrapperslb(userinput[0],float(userinput[1])))
elif userinput[2] == "g":
	print(numberofwrappersg(userinput[0],float(userinput[1])))
else:
	print("Invalid input.")

# def numberofwrappers(cointype, coinweight):
# 	if cointype == "cent":
# 		return math.ceil(coinweight / 125)
# 	elif cointype == "nickle":
# 		return math.ceil(coinweight / 200)
# 	elif cointype == "dime":
# 		return math.ceil(coinweight / 113.4)
# 	elif cointype == "quarter":
# 		return math.ceil(coinweight / 226.8)
# 	else:
# 		return("Uncommon coin.  Information unavailable.")
# userinput = input("Enter cointype cent, nickle, dime, or quarter, follow by a space, and weight of coins. ")
# userinput = userinput.split(" ")
# print(numberofwrappers(userinput[0],float(userinput[1])))