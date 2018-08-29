fruit1 = set()
fruit2 = set()

with open("DATA/fruit1.txt") as fruit1_in:
    for f in fruit1_in:
        fruit1.add(f.strip().lower())

with open("DATA/fruit2.txt") as fruit2_in:
    for f in fruit2_in:
        fruit2.add(f.strip().lower())

print(fruit1)
print("")
print(fruit2)

print(fruit1 & fruit2)
