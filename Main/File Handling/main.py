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

#Question: Write a Python program that reads the contents of a text file named "data.txt" 
#(assuming the file exists) and counts the frequency of each word in the file. Then, print out each unique word and its corresponding frequency.

#Answer
with open("data.txt","r") as f:
    a = f.readlines()
    lst = []
    for i in a:
        for k in i.split():
            lst.append(k.lower())
    for j in set(lst):
        print(j +" Occur " +  str(lst.count(j)) + " Times")


#Question: Write a Python program that reads the contents of a text file named "input.txt" (assuming the file exists) and writes the same content to 
#another text file named "output.txt." Additionally, add a line at the end of the "output.txt" file that says "File copied successfully."

#Answer
with open("input.txt","r") as f:
    a = f.readlines()
    a.append("\nFile copied successfully.")
with open("output.txt","w") as n:
    n.writelines(a)


#Question: Write a Python program that reads a CSV file named "data.csv" (assuming the file exists). Each line of the CSV file contains 
#information about a student in the following format: Name,Score. Your task is to calculate and print the average score of all the students.

#Answer
import csv
import statistics
with open("data.csv","r",newline='\r\n') as f:
    read = csv.reader(f)
    count = 0
    lst = []
    for rec in read:
        for item in rec:
            if count%2==0:
                pass
            else:
                lst.append(item)
            count += 1
lst2=[]
for i in lst:
    lst2.append(int(i))
print(statistics.mean(lst2))
