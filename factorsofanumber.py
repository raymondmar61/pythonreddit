#https://www.reddit.com/r/beginnerprojects/comments/1a0d82/function_factors_of_a_number/
#Define a function that creates a list of all the numbers that are factors of the user's number. For example, if the function is called factor, factor(36) should return [1,2,3,4,6,9,12,18,36]. The numbers in your list should be from least to greatest, and 1 and the original number should be included.

#https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
#run on Python2.7
# def factors(n): 
#     return set(reduce(list.__add__, 
#                 ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
# print(factors(36)) #print set([1, 2, 3, 36, 6, 9, 12, 18, 4])

#https://stackoverflow.com/questions/9761562/how-many-factors-in-an-integer
#run on Python3.5
def factors(n):
    sqrt = int(n ** .5)
    half_factors = [i for i in range(1, sqrt + 1) if n % i == 0]
    return half_factors + [n // i for i in half_factors[n%sqrt == 0::-1]]
print(factors(36)) #print [1, 2, 3, 4, 6, 18, 36]