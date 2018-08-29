import re

filePath ="C:\\Users\\usreei\\PycharmProjects\\MH_Local\\py3intro_1.0\\py3intro\\DATA\\parrot.txt"

with open(filePath, 'r') as parrot_in:
    data = parrot_in.read(). replace('\n', '')


print(data)

RegExPattern = r'\b[a-z]{8,}\b'

rx_code = re.compile(RegExPattern, re.I)

if rx_code.search(data):
    print("Found Pattern")
print()

for m in rx_code.finditer(data):
    print(m.group())
print()


