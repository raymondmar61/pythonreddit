#Source https://en.wikipedia.org/wiki/Roman_numerals
#Symbol I V X L C D M
#Value 1 5 10 50 100 500 1,000
#Number 4 9 40 90 400 900
#Notation IV IX XL XC CD CM

import math

numbers1to10 = ["","I","II","III","IV","V","VI","VII","VIII","IX","X"]
print(numbers1to10[10])

#map or a dictionary.  A colon separates each key for its value
sports = {1 : "I", 4 : "IV", 5: "V", 9: "IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
print(sports)
print(list(sports))
print(sports[1])
print(sports[1]*3)
n = 59
n = str(n)
print(n)
n0 = n[0]
n1 = n[1]
n0 = int(n0)
n1 = int(n1)
if n0 >= 1 and n0 <= 3:
	print(sports[10]*n0+numbers1to10[n1])
elif n0 == 4:
	print(sports[40]+numbers1to10[n1])
elif n0 >= 5 and n0 <= 8:
	print(sports[50]+(sports[10]*(n0-5))+numbers1to10[n1])
elif n0 == 9:
	print(sports[90]+numbers1to10[n1])

for n in range(10,100):
	n = str(n)
	print(n)
	n0 = n[0]
	n1 = n[1]
	n0 = int(n0)
	n1 = int(n1)
	if n0 >= 1 and n0 <= 3:
		print(sports[10]*n0+numbers1to10[n1])
	elif n0 == 4:
		print(sports[40]+numbers1to10[n1])
	elif n0 >= 5 and n0 <= 8:
		print(sports[50]+(sports[10]*(n0-5))+numbers1to10[n1])
	elif n0 == 9:
		print(sports[90]+numbers1to10[n1])


# n = 19
# if n >=11 and n<=39:
# 	n = str(n)
# 	n0 = n[0]
# 	n1 = n[1]
# 	n0 = int(n0)
# 	n1 = int(n1)
# 	print(sports[10]*n0)
# elif n>=40 and n<=49:
# 	n = str(n)
# 	n0 = n[0]
# 	n1 = n[1]
# 	n0 = int(n0)
# 	n1 = int(n1)
# 	print(sports[40]+""+numbers1to10[n1])


# if n >=50 and n<=89:
# 	n = str(n)
# 	n0 = n[0]
# 	n1 = n[1]
# 	n0 = int(n0)
# 	n1 = int(n1)
# 	print(sports[10]*n0)
# elif n>=40 and n<=49:
# 	n = str(n)
# 	n0 = n[0]
# 	n1 = n[1]
# 	n0 = int(n0)
# 	n1 = int(n1)
# 	print(sports[40]+""+numbers1to10[n1])


# n10 = n/10
# number_dec = str(n10-int(n10))[1:]
# print(n10)
# print(number_dec)
# print(favorite_sports[10]*2)




# whole, decimal = math.modf(25/10)
# print(whole)
# print(decimal)