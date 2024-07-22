"""
Code Challenge
  Name: 
    Anagram
  Filename: 
    anagram.py
  Problem Statement:
   Two words are anagrams if you can rearrange the letters of one to spell the second.  
   For example, the following words are anagrams:
   ['abets', 'baste', 'bates', 'beast', 'beats', 'betas', 'tabes']
  
   create a function which takes two arguments and return whether they are angram or no ( True or False)
  Hint: 
   How can you tell quickly if two words are anagrams?  
   Dictionaries allow you to find a key quickly.  

"""

str_=input("enter anagram string : ").split()
str_1=(str_[0])
str_2=(list(str_[1]))
l1=[]
# if str_1.difference(str_2)
for i in str_1:
    if i in str_2:
        str_2.remove(i)

if len(str_2)==0:
    print("anagram")
else:
    print("not")
