#https://www.reddit.com/r/beginnerprojects/comments/1eqt8i/function_mean_median_and_mode/
#In a set of numbers, the mean is the average, the mode is the number that occurs the most, and if you rearrange all the numbers numerically, the median is the number in the middle.
#Create three functions that allow the user to find the mean, median, and mode of a list of numbers. If you have access or know of functions that already complete these tasks, do not use them.
#In the mean function, give the user a way to select how many decimal places they want the answer to be rounded to.
#If there is an even number of numbers in the list, return both numbers that could be considered the median.
#If there are multiple modes, return all of them.

from statistics import mean, median, mode, StatisticsError

def meanmedianmode(numberslist):
	meanx = mean(numberslist)
	print(meanx) #prints 9.1875
	medianx = median(numberslist)
	print(medianx) #prints 5.5
	while True:
		try:
			modex = mode(numberslist)
			print(modex) #prints 2
			break
		except StatisticsError:
			modex = 0
			break
	# modex = mode(numberslist)
	# print(modex) #prints 2
	return ("mean", meanx, "median", medianx, "mode", modex)

numberslist = [4, 6, 2, 6, 7, 8, 2, 5, 6, 78, 4, 6, 7, 2, 2, 2]
print(numberslist) #print [4, 6, 2, 6, 7, 8, 2, 5, 6, 78, 4, 6, 7, 2, 2, 2]
print(meanmedianmode(numberslist)) #print ('mean', 9.1875, 'median', 5.5, 'mode', 2)
inputnumbers = input("Enter a list of numbers separated by a comma ")
inputnumbers = inputnumbers.split(",")
inputnumbers = list(map(int, inputnumbers))
print(inputnumbers)
print(meanmedianmode(inputnumbers))

# inputnumbers = input("Enter a list of numbers separated by a comma ")
# inputnumbers = inputnumbers.split(",")
# print(inputnumbers)
# calculatestats = []
# for x in inputnumbers:
# 	x = int(x)
# 	print(x)
# 	calculatestats.append(x)
# print(calculatestats)
# print(meanmedianmode(calculatestats))

# numberslist = [4, 6, 2, 6, 7, 8, 2, 5, 6, 78, 4, 6, 7, 2, 2, 2]
# print(sum(numberslist))
# print(len(numberslist))
# print(sum(numberslist)/len(numberslist))
# print(len(numberslist)//2)
# median = len(numberslist)//2
# print(median)
# numberslist.sort()
# if median % 2 == 0:
# 	print(numberslist[median])
# else:
# 	print()

# from math import ceil
# numberslist = [1, 2, 3, 4]
# median = ceil(len(numberslist)/2)
# print(median)
# if median % 2 == 0:
# 	print(median)
# 	print(numberslist[median-1])
# 	print(numberslist[median-1] + numberslist[median])
# 	print((numberslist[median-1] + numberslist[median])/2)
# else:
# 	print(numberslist[median-1])