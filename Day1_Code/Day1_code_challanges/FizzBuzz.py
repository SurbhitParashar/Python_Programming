"""

Code Challenge
  Name: 
    Fizz Buzz
  Filename: 
    fizzbuzz.py
  Problem Statement:
    Write a Python program which iterates the integers from 1 to 100(included). 
    For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
    For numbers which are multiples of both three and five print "FizzBuzz". 
  User Input 
    Not required  
  Output:
    1
    2
    Fizz
    4 
    Buzz  
"""

for i in range(101):
    if((i%3==0) & (i%5==0)):
        print("fizzvuzz")
    elif(i%3==0):
        print("fizz")
    elif(i%5==0):
        print("vuzz")
    else:
        print(i)
