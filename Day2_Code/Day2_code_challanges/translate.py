"""
Code Challenge
  Name: 
    Translate Function
  Filename: 
    translate.py
  Problem Statement:
    Write a function translate() that will translate a text into "rövarspråket" 
    Swedish for "robber's language". 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User  
  Input: 
    This is fun
  Output:
    ToThohisos isos fofunon  
"""

l1=[]
def translate(inp_str):
    vowel=['a','e','i','o','u']
    for i in inp_str:
        if i==" ":
            print(" ",end='')
        if i not in vowel:
            print(f"{i}o{i}",end='')
    
inp_str=input("enter a string")
translate(inp_str)
