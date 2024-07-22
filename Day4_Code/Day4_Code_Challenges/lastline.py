"""
Code Challenge
  Name: 
    Last Line
  Filename: 
    lastline.py
  Problem Statement:
    Ask the user for the name of a text file. 
    Display the final line of that file.
    Think of ways in which you can solve this problem, 
    and how it might relate to your daily work with Python.
"""

file_name=input("enter file name to open : ")
print(file_name)

with open(file_name,"r") as file:
    l1=[]
    for line in file:
        # print(line)
        l1.append(line)
    # print(l1)
    print(l1[-1])
