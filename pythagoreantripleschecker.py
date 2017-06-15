#https://www.reddit.com/r/beginnerprojects/comments/19jwi6/project_pythagorean_triples_checker/
#Create a program that allows the user to input the sides of any triangle, and then return whether the triangle is a Pythagorean Triple or not.  The hypotenuse (c) is always the longest side.

inputsides = ""
while inputsides != "q":
	inputsides = input("Enter the three triangle sides positive integers separated by commas no spaces.  Type q to quit ")
	if inputsides == "q":
		break
	splitsides = inputsides.split(",")
	print(splitsides) #split() creates a list each value separated by the split
	#splitsides = [int(i) for i in splitsides] #list comprehension
	splitsides = list(map(int, splitsides)) #convert list string to list integers
	splitsides.sort()
	print(splitsides)
	asides = splitsides[0]
	bsides = splitsides[1]
	csides = splitsides[2]
	a = int(asides)
	b = int(bsides)
	c = int(csides)
	if (a**2) + (b**2) == (c**2):
		print("Triangle is a Pythagorean Triple.\n")
	else:
		print("Triangle is a not a Pythagorean Triple.\n")

# #trianglesides = []
# inputsides = input("Enter adjacent,adjacent,hypotenuse or leg,leg,hypotenuse triangle positive integers separated by commas no spaces ")
# splitsides = inputsides.split(",")
# # trianglesides.append(inputsides)
# # print(trianglesides)
# # print(trianglesides[0])
# asides = splitsides[0]
# bsides = splitsides[1]
# csides = splitsides[2]
# print(asides)
# print(bsides)
# print(csides)
# a = int(asides)
# b = int(bsides)
# c = int(csides)
# if (a**2) + (b**2) == (c**2):
# 	print("yes")