'''
Created on Feb 26, 2016

@author: usreei
'''

## Prime Number
def is_prime(x):
    Prime = False
    if (x < 2):
        Prime = False
    elif (x == 2):
        Prime = True
    else:
        for n in range(2, x):
            if (x % n) == 0:
                Prime = False
                break
            else:
                Prime = True
    return Prime

## Factorial
def factorial(x):
    if x == 1 or x == 0:
        #print("1")
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(4))

## Sum of Digits
n = "1234"


def digit_sum(n):
    b = []
    n = str(n)
    for a in n:
        a = int(a)
        b.append(a)
    return sum(b)

print(digit_sum(n))

## Fibonacci Numbers
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b),
        a, b = b, a + b

def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

print(fib(5000000000000))

## Median Value of a String
def median(a):
    a = sorted(a)
    b = len(a)
    if b % 2 == 0:
        return (a[len(a) / 2] + a[(len(a) / 2) - 1]) / 2.0
    else:
        return a[(len(a) - 1) / 2]

## List Manipulations
square_even_numbers_in_range = [x**2 for x in range(1, 30) if x % 2 == 0]

print(square_even_numbers_in_range)
