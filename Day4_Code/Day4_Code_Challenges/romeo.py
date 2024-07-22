"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""

with open("romeo.txt","r") as file:
    dict1={}
    for line in file:
        line_words=line.split(" ")
        # print(line_words)
        # print(list(enumerate(line_words)))
        enu_list=enumerate(line_words)
        for item,value in enu_list:
            if value not in dict1:
                dict1[value]=1
            else:
                dict1[value]+=1

    print(dict1)


