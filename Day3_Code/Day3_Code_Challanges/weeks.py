"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""

week_days=input("enter week days : ").split()
print(set(week_days))
total_week_days={'monday','tuesday','wednesday','thrusday','friday','saturday','sunday'}
rem_week_days=set(total_week_days).difference(set(week_days))
print(rem_week_days)
print(set(list(week_days)+list(rem_week_days)))
