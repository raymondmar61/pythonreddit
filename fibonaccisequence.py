#https://www.reddit.com/r/beginnerprojects/comments/19r3qg/functionfibonacci_sequence/
#Define a function that allows the user to find the value of the nth term in the sequence. To make sure you've written your function correctly, test the first 10 numbers of the sequence. Remember, the 0th term is 0 and the first and second term are both 1.

project2evenfibonaccilist = []
fibonacci_cache = {}
print(fibonacci_cache)
def fibonaccicache(n):
	#if we have cached the value, then return it
	if n in fibonacci_cache:
		return fibonacci_cache[n]
	# Compute the Nth term
	if n == 1:
		value = 1
	elif n == 2:
		value = 2
	elif n > 2:
		value = fibonaccicache(n-1) + fibonaccicache(n-2)
	#Cache the value in fibonacci_cache dictionary and return it
	fibonacci_cache[n] = value
	return value
userinput = int(input("Enter the nth term of the Fibonacci Sequence "))
for n in range(1,userinput+1):
	print(n, ":", fibonaccicache(n), "going faster use memorization.")
	project2evenfibonaccilist.append(fibonaccicache(n))	
print(project2evenfibonaccilist)
print(sum(project2evenfibonaccilist))