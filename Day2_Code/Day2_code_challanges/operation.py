"""
Code Challenge
  Name: 
    Operations Function
  Filename: 
    operation.py
  Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)

  Input: 
    5,2,6,2,3
  Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]  
"""

# int_num=[]
# def int_conversion(num):
#     for i in num:
#         int_num.append(int(i))
    
def Add(num):
    sum=0
    for i in num:
        sum+=int(i)
    print(sum)

def Multiply(num):
    sum=1
    for i in num:
        sum*=int(i)
    print(sum)


def Largest(num):
    max_num=0
    for i in num:
        if int(i)>max_num:
            max_num=int(i)
    print(max_num)

def Smallest(num):
    min_num=int(min_num[0])
    for i in num:
        if int(i)<min_num:
            min_num=int(i)
    print(min_num)  

def Sorting(num):
    # int_conversion(num)
    print(int_num.sort())

def remove_duplicates(num):
    no_duplicate=[]
    for i in num:
        if i not in no_duplicate:
            no_duplicate.append(i)
    print(no_duplicate)


def Print(num):
    Add(num)
    Multiply(num)
    # Smallest(num)
    # Largest(num)
    Sorting(num)
    remove_duplicates(num)

num=input("enter list of number seperated by space : ").split()
Print(num)
