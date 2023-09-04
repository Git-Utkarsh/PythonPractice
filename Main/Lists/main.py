#Question: Write a Python function that takes a list of numbers as input and returns the sum of all the even numbers in the list.

def even_add(lst):
    l = []
    for i in lst:
        if i%2==0:
            l.append(i)
    return sum(l)
