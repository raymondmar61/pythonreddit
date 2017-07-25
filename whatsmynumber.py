#https://www.reddit.com/r/beginnerprojects/comments/1dbena/challenge_whats_my_number/
#Between 1 and 1000, there is only 1 number that meets the following criteria. While it could be manually figured out with pen and paper, it would be much more efficient to write a program that would do this for you. With that being said, your goal is to find out which number meets these criteria. To find out if you have the correct number, click the link at the bottom of this main post.
#The number has two or more digits.
#The number is prime.
#The number does NOT contain a 1 or 7 in it.
#The sum of all of the digits is less than or equal to 10.
#The first two digits add up to be odd.
#The second to last digit is even.
#The last digit is equal to how many digits are in the number.
# for eachnumber in range(10,21,2):
# 	print(eachnumber)
#poster's answer is 523.  However zero is an even number.  I found four numbers:  323, 343, 503, 523.

import math
newa = []
def isprime(n):
	if n == 1:
		return False
	elif n < 4:
		return True #2 and 3 are prime numbers
	elif n % 2 == 0:
		return False #prime numbers except 2 are odd
	elif n < 9:
		return True #4, 6, and 8 are excluded
	elif n % 3 == 0:
		return False
	else:
		r = math.floor(n**.5)  #n^.05 rounded to the greatest integer r so r*r<=n
		f = 5
		while f<=r:
			if n % f == 0:
				False
				break
			elif n % (f+2) == 0:
				False
				break
			f = f + 6
		return True
counter = 1000
n = 10
while n <= counter:
	#print("Is",n, "a prime number? " +str(isprime(n)))
	if str(isprime(n)) == "True":
		newa.append(n)
	n += 1

newa = list(map(str, newa))
for x in range(len(newa)-1,-1,-1):
	if len(newa[x]) == 3:
		if newa[x][0] == "1" or newa[x][0] == "7" or newa[x][1] == "1" or newa[x][1] == "7" or newa[x][2] == "1" or newa[x][2] == "7":
			del newa[x]
	elif len(newa[x]) == 2:
		if newa[x][0] == "1" or newa[x][0] == "7" or newa[x][1] == "1" or newa[x][1] == "7":
			del newa[x]
for x in range(len(newa)-1,-1,-1):
	if len(newa[x]) == 3:
		if int(newa[x][0])+int(newa[x][1])+int(newa[x][2]) > 10:
			del newa[x]
	elif len(newa[x]) == 2:
		if int(newa[x][0])+int(newa[x][1]) > 10:
			del newa[x]
for x in range(len(newa)-1,-1,-1):
	if (int(newa[x][0])+int(newa[x][1])) % 2 == 0:
		del newa[x]
for x in range(len(newa)-1,-1,-1):
	if (int(newa[x][1])) % 2 != 0:
		del newa[x]
for x in range(len(newa)-1,-1,-1):
	if (int(newa[x][2])) != len((newa[x])):
		del newa[x]
print(newa)
newa = list(map(int, newa))
print(newa)

ok = str(146)
print(int(ok[0]+ok[1]+ok[2])) #print 146
print(int(ok[0])) #print 1
print(int(ok[1])) #print 4
print(int(ok[2])) #print 6
print(int(ok[0])+int(ok[1])+int(ok[2])) #print 11

lists = ["a","b","c"]
for h in range(len(lists)-1,-1,-1):
	print(lists[h]) #print c\n b\n a