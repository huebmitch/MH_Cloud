fruit = []

with open('DATA/fruit.txt') as fruit_in:
    for raw_line in fruit_in:
        line = raw_line.strip()
        fruit.append(line)

nameCaseSensitive = sorted(fruit)
nameCaseInsensitive = sorted(fruit, key=str.lower)
LengthName = sorted(fruit, key=lambda x: (len(x), x.lower()))
LengthName2 = sorted(fruit, key=lambda x: (len(x)))
SecondLetterFirstLetter = sorted(fruit, key=lambda x: (x[1], x[0]))
SecondLetterFirstLetter2 = sorted(fruit, key=lambda x: (x[1].lower(), x[0].lower()))


print("")
print("Sorted by Name Case-Sensitively", nameCaseSensitive, '\n')
print("Sorted by Name Case-Insensitively", nameCaseInsensitive, '\n')
print("Sorted by Length, Name Case-Sensitively", LengthName, '\n')
print("Sorted by Length, Name Case-Insensitively", LengthName2, '\n')
print("Sorted by 2nd Letter, 1st Letter Case-Sensitively", SecondLetterFirstLetter, '\n')
print("Sorted by 2nd Letter, 1st Letter Case-Insensitively", SecondLetterFirstLetter2, '\n')
