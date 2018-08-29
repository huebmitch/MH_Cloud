'''
Created on Jun 2, 2016

@author: usreei
'''

Base = 9.75
Weather = -0.90
Village = 3.77
Upgrades = 0.80
Buildings = 1.17
Paragon = 1.41
Demand = -31.61

#Should = 8.96

TotalCatnip = (Base * (1 + Weather) + (Village * (1 + Upgrades)) + (1 + Buildings) + (Base * Paragon)) - Demand
totalattempt = (Base * (1 + Weather) + (Base + Village) + (Base * (1 + Upgrades)) + (Base * Buildings) + (Base * Paragon)) + Demand

print("{:.2f}".format(TotalCatnip))
print("{:.2f}".format(totalattempt))
