import pprint

knight_info = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.strip()
        name, title, color, quest, comment = line.split(':')
        print(name, title, color, quest, comment)
        knight_info[name] = [title, color, quest, comment]

print(knight_info['Arthur'])
print(knight_info['Robin'][2])

for name, data in knight_info.items():
    print(data[0], name)

pprint.pprint(knight_info)
