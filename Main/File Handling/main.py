## Question: Write a Python program that reads the contents of a text file named "example.txt" (assuming the file exists) and prints each line with line numbers. For example:
#1: This is the first line.
#2: This is the second line.
#3: This is the third line.

#Answer
with open("example.txt") as file:
    line = file.readlines()
    count = 1
    for i in line:
        print(str(count) + ": " + i)
        count=count+1
