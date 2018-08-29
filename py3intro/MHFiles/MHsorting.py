import pprint as pp

fruit = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi",
         "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG", "pear", "banana",
         "Tamarind", "persimmon", "elderberry", "peach", "BLUEberry", "lychee",
         "grape"]

f1 = sorted(fruit)

pp.pprint(f1)

nums = [800, 80, 1000, 32, 255, 12]

f2 = sorted(nums)

pp.pprint(f2)

def ignore_case(f):
    return f.lower()

f2 = sorted(fruit, key=ignore_case)
print("f2:", f2, '\n')

f3 = sorted(fruit, key=len)
print("f3:", f3, '\n')

f4 = sorted(fruit, key=len)[:5]
print("f4:", f4, '\n')

def len_and_name(wombat):
    return len(wombat), wombat.lower()

f5 = sorted(fruit, key=len_and_name)
print("f5:", f5, '\n')

def wacky(f):
    return f[1], f[-1]

f6 = sorted(fruit, key=wacky)
print("f6:", f6, '\n')
