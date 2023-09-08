#Question: Write a Python program that calculates the factorial of a given positive integer. The factorial of a number "n" is
#the product of all positive integers from 1 to "n." For example, the factorial of 5 (written as 5!) is 5 x 4 x 3 x 2 x 1 = 120.

# Answer
def factorial(n):
    if n == 1 or n == 0:
        return 1 
    return n * factorial(n-1)


#Question: Write a Python function that takes a list of integers as input and returns a new list containing only the even numbers from the original list.

#Answer
def even(lst):
    lst1 = []
    for item in lst:
        if item%2==0:
            lst1.append(item)
    return lst1
print(even([1,2,3,4,5,6]))
