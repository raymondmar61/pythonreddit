#https://www.reddit.com/r/beginnerprojects/comments/1bytu5/projectmenu_calculator/
#Imagine you have started up a small restaurant and are trying to make it easier to take and calculate orders. Since your restaurant only sells 9 different items, you assign each one to a number, as shown below.
#1 Chicken Strips - $3.50
#2 French Fries - $2.50
#3 Hamburger - $4.00
#4 Hotdog - $3.50
#5 Large Drink - $1.75
#6 Medium Drink - $1.50
#7 Milk Shake - $2.25
#8 Salad - $3.75
#9 Small Drink - $1.25
#To quickly take orders, your program should allow the user to type in a string of numbers and then it should calculate the cost of the order. For example, if one large drink, two small drinks, two hamburgers, one hotdog, and a salad are ordered, the user should type in 5993348, and the program should say that it costs $19.50. Also, make sure that the program loops so the user can take multiple orders without having to restart the program each time.
#If you decide to, print out the items and prices every time before the user types in an order.
#Once the user has entered an order, print out how many of each item have been ordered, as well as the total price. If an item was not ordered at all, then it should not show up.

import csv
restaurantitemslist = []
# with open("tempbook1.csv") as csvfile:
# 	readcsv = csv.reader(csvfile, delimiter=",")
# 	print(readcsv) #print <_csv.reader object at 0x7f3ae4f3aba8>
# 	for eachreadcsv in readcsv:
# 		print(eachreadcsv) #print ['1', 'Chicken Strips', '3.50']\n ['2', 'French Fries', '2.50']\n ['3', 'Hamburger', '4.00']\n ['4', 'Hotdog', '3.50']\n ['5', 'Large Drink', '1.75']\n ['6', 'Medium Drink', '1.50']\n ['7', 'Milk Shake', '2.25']\n ['8', 'Salad', '3.75']\n ['9', 'Small Drink', '1.25']
with open("tempbook1.csv") as csvfile:
	readcsv = csv.reader(csvfile, delimiter=",")
	for eachreadcsv in readcsv:
		restaurantitemslist.append(eachreadcsv)
#print(restaurantitemslist) #print [['1', 'Chicken Strips', '3.50'], ['2', 'French Fries', '2.50'], ['3', 'Hamburger', '4.00'], ['4', 'Hotdog', '3.50'], ['5', 'Large Drink', '1.75'], ['6', 'Medium Drink', '1.50'], ['7', 'Milk Shake', '2.25'], ['8', 'Salad', '3.75'], ['9', 'Small Drink', '1.25']]

for eachrestaurantitemslist in restaurantitemslist:
	print(eachrestaurantitemslist)
totalcost = 0
customerorder = 0
totalorders = []
while customerorder != "q":
	customerorder = input("Enter your order by the numbers no spaces ")
	if customerorder == "q":
		break
	customerorders = list(customerorder)
	print(customerorders)
	for eachcustomerorders in customerorders:
		eachcustomerorders = int(eachcustomerorders)
		print(restaurantitemslist[eachcustomerorders-1][1]+": "+str(restaurantitemslist[eachcustomerorders-1][2]))
		totalorders.append(restaurantitemslist[eachcustomerorders-1][1]+": "+str(restaurantitemslist[eachcustomerorders-1][2]))
		totalcost = float(restaurantitemslist[eachcustomerorders-1][2]) + totalcost
	print(totalorders)
	print("%.2f" % totalcost)
	customerorder = input("Is the customer done ordering?  If yes, type q ")
	if customerorder == "q":
		break
	else:
		continue
print(totalcost * 1.0875) #tax 8.75%
a = totalcost * 1.0875
print("%.2f" % round(a,2))