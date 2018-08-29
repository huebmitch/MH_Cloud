import sys

Raw_Cel = sys.argv[1]
Cel = int(Raw_Cel)
Fahr = ((9 * Cel) / 5) + 32

print("Celcius", str(Cel), "is Fahrenheit", Fahr)