'''
Created on Feb 25, 2016

@author: usreei
'''

## Sign up test 1 for Python - Multiply
def multiply(a, b):
    total = a * b
    return(total)


## Sign up test 2 for Pyhton - Broken Greetings
class Person:

    def __init__(self, name):
        self.name = name

    def greet(self, other_name):
        return "Hi {0}, my name is {1}".format(other_name, self.name)

## Return to Sanity Team Kata #1
def mystery():
    results = {'sanity': 'Hello'}
    return results

## Fix the Bugs(syntax) - My First Kata
def my_first_kata(a, b):
    if type(a) == int and type(b) == int:
        return (a % b) + (b % a)
    else:
        return False

## Stive Matching #1
candidate = {'min_salary': 120000}
job = {'max_salary': 140000}


def match(candidate, job):
    for key in candidate:
        needed_salary = (candidate[key] - (0.1 * candidate[key]))
    for key in job:
        able_salary = job[key]
    if needed_salary <= able_salary:
        return True
    elif needed_salary > able_salary:
        return False
    else:
        return "Error"

print(match(candidate, job))

## What's wrong with these Identifiers
Person = {
    "1stname": "John",
    "second-name": "Doe",
    "email@ddress": "john.doe@email.com",
    "male.female": "M"
}

#Last Kata Answer
def last(*x):
    try:
        return x[-1][-1]
    except:
        return x[-1]
