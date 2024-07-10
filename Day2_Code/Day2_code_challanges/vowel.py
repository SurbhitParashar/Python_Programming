"""
Code Challenge
  Name: 
    Vowels Finder
  Filename: 
    vowels.py
  Problem Statement:
    Remove all the vowels from the list of states  
  Hint: 
    Use nested for loops and in membership Operator
  Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
  Output:
    ['lbm', 'Clfrn', 'klhm', 'Flrd']
    
"""

inp_list=[]
while(True):
    name=input("enter the string : ")
    inp_list.append(name)
    if not name:
        break
print(inp_list)

final_str=[]
for name in inp_list:
    new_str=[]
    split_name=list(name)
    print(split_name)
    vowel=['a','e','i','o','u']
    for i in split_name:
        if i not in vowel:
            new_str.append(i)

    final_str.append("".join(new_str))
print(final_str)
