"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop1.py
  Problem Statement:
    Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:
        
    Order Number  Book Title  Author Quantity  Price per Item
    34587 Learning Python, Mark Lutz  4 40.95
    98762 Programming Python, Mark Lutz 5 56.80
    77226 Head First Python, Paul Barry 3 32.95
    88112 Einführung in Python3, Bernd Klein  3 24.99    
    
    
    Write a Python program, You need to write a solution without using lambda,map,list comprehension first and then with lambda,map,reduce
    
    A) which returns Order Summary as a list with 2-tuples. 
       Each tuple consists of the order number and the product of the price per items 
       and the quantity. 
    
       The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.

  Hint: 
    Write a Python program using lambda and map.

  Input:
    orders = [["34587", "Learning Python, Mark Lutz", 4, 40.95], 
              ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
              ["77226", "Head First Python, Paul Barry", 3,32.95],
              ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
             ]
  Output:
      [('34587', 163.8), ('98762', 284.0), ('77226', 108.85), ('88112', 84.97)]
      

"""

orders = [["34587", "Learning Python, Mark Lutz", 4, 40.95], 
              ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
              ["77226", "Head First Python, Paul Barry", 3,32.95],
              ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
             ]
dict1={}

total_price=list(map(lambda a: a[-1]*a[-2],orders))
print(total_price)
for item in total_price:
    if int(item)<100:
        a=total_price.index(item)
        item+=10
        total_price[a]=item
print(total_price)

# for line in order:
#     total_price=line[-1]*line[-2]
    # if total_price<=100:
    #     dict1[line[0]]=total_price+10
    # else:
    #     dict1[line[0]]=total_price

# print(dict1.items())
