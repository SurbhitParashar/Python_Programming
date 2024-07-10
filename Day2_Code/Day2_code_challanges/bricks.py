"""
Code Challenge
  Name: 
    Bricks
  Filename: 
    bricks.py
  Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target 
    by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, 
    middle element represents number of big bricks and 3rd element represents the target.
  Input: 
    2, 2, 11
  Output:
    True
"""

brick_num=input("enter no of bricks and target: ").split()
print(brick_num)

small_brick=brick_num[0]
big_brick=brick_num[1]
target=brick_num[2]

rem=int(target)//int(big_brick)

if rem<=int(small_brick):
    print(True)
else:
    print(False)
