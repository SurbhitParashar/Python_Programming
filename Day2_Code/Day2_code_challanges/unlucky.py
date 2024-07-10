"""
Code Challenge
  Name: 
    Unlucky 13
  Filename: 
    unlucky.py
  Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that 
    come immediately after a 13 also do not count
    Take input from user  
  Input: 
    13, 1, 2, 13, 2, 1, 13
  Output:
    3
"""

num_list=input("enter list of numbers seperated by space : ").split()

user_list=[]
for i in num_list:
    user_list.append(int(i))

# print(user_list)

for i in user_list:
    sum=0
    skip_nxt=0

    if i==13:
        # indx=user_list.index(13)
        # user_list.pop(indx)
        # user_list.pop(indx+1)
        skip_nxt=True
    elif skip_nxt:
        skip_nxt=False
    else:
        sum+=i
        
    print(sum)

        
