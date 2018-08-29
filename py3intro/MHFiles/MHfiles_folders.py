import os
from datetime import datetime

folder = '..\DATA'
file = 'mary.txt'

file_path = os.path.join(folder,file)

print(file_path)

file_size = os.path.getsize(file_path)
print(file_size)

raw_timestamp = os.path.getatime(file_path)
print("raw timestamp:", raw_timestamp)

timestamp = datetime.fromtimestamp(raw_timestamp)
print("timestamp:", timestamp)

print(type(timestamp))

print(timestamp.ctime(), timestamp.year, timestamp.weekday())

print(os.path.dirname(file_path))
print(os.path.basename(file_path))
print(os.path.abspath(file_path))


