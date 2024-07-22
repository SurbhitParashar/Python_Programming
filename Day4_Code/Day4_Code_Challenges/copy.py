"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""

with open("words.txt","r") as f:
    with open("words2.txt","a") as copy_file:
        # line=f.readline()
        # print(line)
        for line in f:
            copy_file.write(line)
