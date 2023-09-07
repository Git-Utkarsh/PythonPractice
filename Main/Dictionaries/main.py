#Question: Write a Python function that takes a dictionary as input, where the keys are student names, and the values are their corresponding scores. The function should return the name of the student with the highest score.

def max_marks(dictionary):
    for i in dictionary:
        lst = list(dictionary.values())
        if dictionary[i]==max(lst):
            return i 
        
#Question: Write a Python function that takes a list of dictionaries as input, where each dictionary represents a student and their scores in different subjects. The dictionaries have the following 
#format: {"Name": "StudentName", "Math": Score, "Science": Score, "History": Score}. 
#The function should calculate the average score for each student and return a new list of dictionaries, where each dictionary includes the student's name and their average score.

def average(lst):
    lst1 = []
    for item in lst:
        dict = {item["Name"]:str((item["Math"] + item["Science"] + item["History"])/3)}
        lst1.append(dict)
    return lst1

#Question: Write a Python function that takes a list of dictionaries as input, where each dictionary represents a product with attributes like "name," "price," and "quantity." 
    #The function should calculate the total value of all products in the list, considering the price and quantity of each product. It should return the total value.

def total(lst):
    lst1 = []
    for item in lst:
        dict = {item["name"]:str(item["price"]*item["quantity"])}
        lst1.append(dict)
    return lst1
