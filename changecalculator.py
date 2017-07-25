#https://www.reddit.com/r/beginnerprojects/comments/19jkn8/project_change_calculator/
#Imagine that your friend is a cashier, but has a hard time counting back change to customers. Create a program that allows him to input a certain amount of change, and then print how how many quarters, dimes, nickels, and pennies are needed to make up the amount needed.  For example, if he inputs 1.47, the program will tell that he needs 5 quarters, 2 dimes, 0 nickels, and 2 pennies.
#So your friend doesn't have to calculate how much change is needed, allow him to type in the amount of money given to him and the price of the item. The program should then tell him the amount of each coin he needs like usual.
#To make the program even easier to use, loop the program back to the top so your friend can continue to use the program without having to close and open it every time he needs to count change.

from math import floor

# change = 9.86
# quarters = change / 0.25
# quarters = floor(quarters)
# print("quarters",quarters)
# change = change - (quarters * 0.25)
# change = round(change,2)
# print(change)
# dimes = change / 0.10
# dimes = floor(dimes)
# print("dimes",dimes)
# change = change -(dimes * 0.10)
# change = round(change,2)
# print(change)
# nickles = change / 0.05
# nickles = floor(nickles)
# print("nickles",nickles)
# change = change -(nickles * 0.05)
# change = round(change,2)
# print(change)
# pennies = change / 0.01
# pennies = floor(pennies)
# print("pennies",pennies)
# change = change -(pennies * 0.01)
# change = round(change,2)
# print(change)

def coinschange(change):
	quarters = change / 0.25
	quarters = floor(quarters)
	print("quarters",quarters)
	change = change - (quarters * 0.25)
	change = round(change,2)
	print(change)
	dimes = change / 0.10
	dimes = floor(dimes)
	print("dimes",dimes)
	change = change -(dimes * 0.10)
	change = round(change,2)
	print(change)
	nickles = change / 0.05
	nickles = floor(nickles)
	print("nickles",nickles)
	change = change -(nickles * 0.05)
	change = round(change,2)
	print(change)
	pennies = change / 0.01
	pennies = floor(pennies)
	print("pennies",pennies)
	change = change -(pennies * 0.01)
	change = round(change,2)
	print(change)

totalandpaid = 0
while totalandpaid != "q":
	totalandpaid = input("Enter the total and customer paid separated by a comma.  Type q to quit. ")
	if totalandpaid == "q":
		break
	calculatechange = totalandpaid.split(",")
	total = float(calculatechange[0])
	paid = float(calculatechange[1])
	print(total)
	print(paid)
	change = paid - total
	change = round(change,2)
	coinschange(change)

