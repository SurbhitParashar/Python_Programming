"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic2.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      You need to develop using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:if input_num:
    True
"""

num_list=input("enter integer space seperated > ").split(" ")
print(num_list)
l1=[]
def pallindrome(num_sep):
    if num_sep==num_sep[::-1]:
        l1.append(True)
    else:
        l1.append(False)

for num in num_list:
    num_sep=list(num)
    # print(num_sep)
    pallindrome(num_sep)
print(any(l1))
