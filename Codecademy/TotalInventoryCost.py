'''
Created on Feb 15, 2016

@author: usreei
'''

prices = {"banana": 4,
          "apple": 2,
          "orange": 1.5,
          "pear": 3}

stock = {"banana": 6,
         "apple": 4,
         "orange": 32,
         "pear": 15}

for key in prices:
    print(key)
    print("price: %s" % prices[key])
    print("stock: %s" % stock[key])
    print()

total = 0

for key in prices:
    total = ((prices[key]) * (stock[key])) + total

print("The total inventory would cost", total)
