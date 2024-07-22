"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""

str_=input("enter string : ").split()
digit=['1','2','3','4','5','6','7','8','9','0']
print(str_)
# list1=list(str_)
# print(list1)
digit_count=0
alpha_count=0
for name in str_:
    split_str=list(name)

    for i in split_str:
        if i not in digit:
            alpha_count+=1
        else:
            digit_count+=1

print(digit_count)
print(alpha_count)
