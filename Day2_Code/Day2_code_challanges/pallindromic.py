
"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      Shorter logic can be developed using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""

num=input("enter numbers seperated by space : ")
list1=num.split()
# print(list1)

tflist1=[]
# tflist2=[]
for number in list1:
    
    def pallin_chk(number):
        list_chk=list(number)
        # print(list_chk)
        for i in range(round(len(list_chk)/2)):
            if(list_chk[i]==(list_chk[len(list_chk)-i-1])):
                tflist1.append("true")
            else:
                tflist1.append("false")
    pallin_chk(number)

# for num in list1:
#     if int(num)>0:
#         tflist2.append("true")
#     else:
#         tflist2.append("false")


if( ("true" in tflist1)):
    print(True)
else:
    print(False)



