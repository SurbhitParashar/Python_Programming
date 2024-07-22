"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""

my_dict={}
str_=list(input("enter a string : "))
print(str_)
for item,value in enumerate(str_):
    if value not in my_dict:
        my_dict[value]=1
    else:
        my_dict[value]+=1
print(my_dict)

