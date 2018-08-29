import sys
import os

print(sys.prefix)
print(sys.executable)
print()
print(sys.version)
print(sys.version_info)
print()
for path in sys.path:
    print(path)
print()
print(sys.platform)
print()
print(sys.maxsize)
print()
sys.stdout.write("Hello World\n")
print()
os.system('netstat -an')
