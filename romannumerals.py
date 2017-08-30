#https://www.reddit.com/r/beginnerprojects/comments/3x52ie/project_roman_numeral_integer_converter/
#Sources https://en.wikipedia.org/wiki/Roman_numerals, http://artlung.com/smorgasborg/roman-numerals/, http://romannumerals.babuo.com/roman-numerals-1-5000
#Symbol I V X L C D M
#Value 1 5 10 50 100 500 1,000
#Number 4 9 40 90 400 900
#Notation IV IX XL XC CD CM

numbers1to10 = ["","I","II","III","IV","V","VI","VII","VIII","IX","X"]
#map or a dictionary.  A colon separates each key for its value
sports = {1 : "I", 4 : "IV", 5: "V", 9: "IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
n = 340
if n >= 0 and n <= 9:
	print(n,numbers1to10[n])	
elif n >= 10 and n <= 99:
	n = str(n)
	n0 = n[0]
	n1 = n[1]
	n0 = int(n0)
	n1 = int(n1)
	if n0 >= 1 and n0 <= 3:
		print(n,sports[10]*n0+numbers1to10[n1])
	elif n0 == 4:
		print(n,sports[40]+numbers1to10[n1])
	elif n0 >= 5 and n0 <= 8:
		print(n,sports[50]+(sports[10]*(n0-5))+numbers1to10[n1])
	elif n0 == 9:
		print(n,sports[90]+numbers1to10[n1])
elif n >= 100 and n <= 999:
	n = str(n)
	n0 = n[0]
	n1 = n[1]
	n2 = n[2]
	n0 = int(n0)
	n1 = int(n1)
	n2 = int(n2)
	if (n0 ==1 and n1 ==0) or (n0 ==2 and n1 ==0) or (n0 ==3 and n1 ==0):
		print(n,sports[100]*n0+numbers1to10[n2])
	elif (n0 >=1 and n0 <=3) and (n1 >= 1 and n1 <= 3):
		print(n,sports[100]*n0+sports[10]*n1+numbers1to10[n2])
	elif (n0 >=1 and n0 <=3) and n1 == 4:
		print(n,sports[100]*n0+sports[40]+numbers1to10[n2])
	elif (n0 >=1 and n0 <=3) and (n1 >= 5 and n1 <= 8):
		print(n,sports[100]*n0+sports[50]+(sports[10]*(n1-5))+numbers1to10[n2])
	elif (n0 >=1 and n0 <=3) and n1 == 9:
		print(n,sports[100]*n0+sports[90]+numbers1to10[n2])
	elif (n0 == 4) and (n1 >= 1 and n1 <= 3):
		print(n,sports[400]+sports[10]*n1+numbers1to10[n2])
	elif (n0 == 4) and (n1 == 0):
		print(n,sports[400]+sports[40]*n1+numbers1to10[n2])
	elif (n0 == 4) and n1 == 4:
		print(n,sports[400]+sports[40]+numbers1to10[n2])
	elif (n0 == 4) and (n1 >= 5 and n1 <= 8):
		print(n,sports[400]+sports[50]+(sports[10]*(n1-5))+numbers1to10[n2])
	elif (n0 == 4) and n1 == 9:
		print(n,sports[400]+sports[90]+numbers1to10[n2])
	elif n0 ==5 and n1 ==0:
		print(n,sports[500]+numbers1to10[n2])
	elif (n0 == 6 and n1 ==0) or (n0 ==7 and n1 ==0) or (n0 ==8 and n1 ==0):
		print(n,sports[500]+sports[100]*(n0-5)+numbers1to10[n2])
	elif (n0 >=5 and n0 <=8) and (n1 >= 1 and n1 <= 3):
		print(n,sports[500]+sports[100]*(n0-5)+sports[10]*n1+numbers1to10[n2])
	elif (n0 >=5 and n0 <=8) and n1 == 4:
		print(n,sports[500]+sports[100]*(n0-5)+sports[40]+numbers1to10[n2])
	elif (n0 >=5 and n0 <=8) and (n1 >= 5 and n1 <= 8):
		print(n,sports[500]+sports[100]*(n0-5)+sports[50]+(sports[10]*(n1-5))+numbers1to10[n2])
	elif (n0 >=5 and n0 <=8) and n1 == 9:
		print(n,sports[500]+sports[100]*(n0-5)+sports[90]+numbers1to10[n2])
	elif (n0 == 9) and (n1 == 0):
		print(n,sports[900]+sports[90]*n1+numbers1to10[n2])
	elif (n0 == 9) and (n1 >= 1 and n1 <= 3):
		print(n,sports[900]+sports[10]*n1+numbers1to10[n2])
	elif (n0 == 9) and n1 == 4:
		print(n,sports[900]+sports[40]+numbers1to10[n2])
	elif (n0 == 9) and (n1 >= 5 and n1 <= 8):
		print(n,sports[900]+sports[50]+(sports[10]*(n1-5))+numbers1to10[n2])
	elif (n0 == 9) and n1 == 9:
		print(n,sports[900]+sports[90]+numbers1to10[n2])
elif n >= 1000 and n <= 3999:
	n = str(n)
	n0 = n[0]
	n1 = n[1]
	n2 = n[2]
	n3 = n[3]
	n0 = int(n0)
	n1 = int(n1)
	n2 = int(n2)
	n3 = int(n3)
	if (n0 ==1 and n1 ==0 and n2==0) or (n0 ==2 and n1 ==0 and n2==0) or (n0 ==3 and n1 ==0 and n2==0):
		print(n,sports[1000]*n0+numbers1to10[n3])
	elif (n0 >=1 and n0 <=3) and n1==0 and (n2 >= 1 and n2 <= 3):
		print(n,sports[1000]*n0+sports[10]*n2+numbers1to10[n3])
	elif (n0 >=1 and n0 <=3) and n1== 0 and n2 == 4:
		print(n,sports[1000]*n0+sports[40]+numbers1to10[n3])
	elif (n0 >=1 and n0 <=3) and n1==0 and (n2 >= 5 and n2 <= 8):
		print(n,sports[1000]*n0+sports[50]+(sports[10]*(n2-5))+numbers1to10[n3])
	elif (n0 >=1 and n0 <=3) and n1==0 and n2 == 9:
		print(n,sports[1000]*n0+sports[90]+numbers1to10[n3])
	elif (n0 >=1 and n0 <=3) and (n1 >= 1 and n1 <= 3) and (n2 >= 0 and n2 <= 3):
		print(n,sports[1000]*n0+sports[100]*n1+sports[10]*n2+numbers1to10[n3])
	elif (n0 >=1 and n0 <=3) and (n1 >= 1 and n1 <= 3) and n2 == 4:
		print(n,sports[1000]*n0+sports[100]*n1+sports[40]+numbers1to10[n3])
	elif (n0 >=1 and n0 <=3) and (n1 >= 1 and n1 <= 3) and (n2 >= 5 and n2 <= 8):
		print(n,sports[1000]*n0+sports[100]*n1+sports[50]+(sports[10]*(n2-5))+numbers1to10[n3])
	elif (n0 >=1 and n0 <=3) and (n1 >= 1 and n1 <= 3) and n2 == 9:
		print(n,sports[1000]*n0+sports[100]*n1+sports[90]+numbers1to10[n3])
	elif (n0 >=1 and n0 <=3) and n1 == 4 and (n2 >= 0 and n2 <= 3):
		print(n,sports[1000]*n0+sports[400]+sports[10]*n2+numbers1to10[n3])
	elif (n0 >=1 and n0 <=3) and n1 == 4 and n2 == 4:
		print(n,sports[1000]*n0+sports[400]+sports[40]+numbers1to10[n3])
	elif (n0 >=1 and n0 <=3) and n1 == 4 and (n2 >= 5 and n2 <= 8):
		print(n,sports[1000]*n0+sports[400]+sports[50]+(sports[10]*(n2-5))+numbers1to10[n3])
	elif (n0 >=1 and n0 <=3) and n1 == 4 and n2 == 9:
		print(n,sports[1000]*n0+sports[400]+sports[90]+numbers1to10[n3])
	elif (n0 >=1 and n0 <=3) and (n1 >= 5 and n1 <= 8) and (n2 >= 0 and n2 <= 3):
		print(n,sports[1000]*n0+sports[500]+sports[100]*(n1-5)+sports[10]*n2+numbers1to10[n3])
	elif (n0 >=1 and n0 <=3) and (n1 >= 5 and n1 <= 8) and n2 == 4:
		print(n,sports[1000]*n0+sports[500]+sports[100]*(n1-5)+sports[40]+numbers1to10[n3])
	elif (n0 >=1 and n0 <=3) and (n1 >= 5 and n1 <= 8) and (n2 >= 5 and n2 <= 8):
		print(n,sports[1000]*n0+sports[500]+sports[100]*(n1-5)+sports[50]+(sports[10]*(n2-5))+numbers1to10[n3])
	elif (n0 >=1 and n0 <=3) and (n1 >= 5 and n1 <= 8) and n2 == 9:
		print(n,sports[1000]*n0+sports[500]+sports[100]*(n1-5)+sports[90]+numbers1to10[n3])
	elif (n0 >=1 and n0 <=3) and n1 == 9 and (n2 >= 0 and n2 <= 3):
		print(n,sports[1000]*n0+sports[900]+sports[10]*n2+numbers1to10[n3])
	elif (n0 >=1 and n0 <=3) and n1 == 9 and n2 == 4:
		print(n,sports[1000]*n0+sports[900]+sports[40]+numbers1to10[n3])
	elif (n0 >=1 and n0 <=3) and n1 == 9 and (n2 >= 5 and n2 <= 8):
		print(n,sports[1000]*n0+sports[900]+sports[50]+(sports[10]*(n2-5))+numbers1to10[n3])
	elif (n0 >=1 and n0 <=3) and n1 == 9 and n2 == 9:
		print(n,sports[1000]*n0+sports[900]+sports[90]+numbers1to10[n3])
else:
	print("Sorry, can't convert the number.  3,999 is the maximum.")