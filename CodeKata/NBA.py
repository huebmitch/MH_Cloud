'''
Created on Jan 20, 2017

@author: usreei
'''
ppg = 23
mpg = 55

def nba_extrap(ppg, mpg):
    AvgPerMin = ppg / mpg
    ppg = AvgPerMin * 48
    print(ppg)
    return round(ppg, 2)

print(nba_extrap(ppg, mpg))
