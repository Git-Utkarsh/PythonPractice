#Question: Write a Python function that takes a dictionary as input, where the keys are student names, and the values are their corresponding scores. The function should return the name of the student with the highest score.

def max_marks(dictionary):
    for i in dictionary:
        lst = list(dictionary.values())
        if dictionary[i]==max(lst):
            return i 
        
