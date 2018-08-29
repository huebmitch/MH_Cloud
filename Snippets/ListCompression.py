
#https://www.makeuseof.com/tag/python-list-comprehension-guide/

letters = ['a','b','c','d']
print(letters)

upper_letters = []

for letter in letters:
    result = letter.upper()
    upper_letters.append(result)

print(upper_letters)


LCletters = ['a','b','c','d']
print(LCletters)

LCupper_letters = [x.upper() for x in LCletters]

print(LCupper_letters)

ages = [1, 34, 5, 7, 3, 57, 356]
print(ages)

old_ages = [x for x in ages if x > 10]
print(old_ages)
