'''
Created on Feb 12, 2016

@author: usreei
'''

city = input("Enter Tampa, Pittsburg, or Los Angeles: ")
days = int(input("Enter number of days: "))
spending_money = int(input("Enter extra spending money: "))

def hotel_cost(days):
    return 140 * days

def plane_ride_cost(city):
    if city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    total = 40 * days
    if days >= 7:
        total -= 50
    elif days >= 3:
        total -= 20
    return total

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
print(trip_cost(city, days, spending_money))
