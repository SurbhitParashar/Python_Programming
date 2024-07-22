"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""

with open("absentee.txt","w") as file:
    while True:
        i=0
        str_name=input("enter name of student : ")
        file.write(str_name)
        file.write("\n")
        if not (str_name or i>25):
            break
        i+=1

with open("absentee.txt","r") as f:
    # for line in f:
    #     print(line)
    print(f.readlines())
