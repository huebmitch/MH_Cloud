import sys
import pprint

# Raw_Cel = input("What is the Celcius Temperature: ")
# Cel = int(Raw_Cel)
# Fahr = ((9 * Cel) / 5) + 32
#
# print("Celcius", str(Cel), "is Fahrenheit", Fahr)
#
# print("")

DATA = [100, 0, 37, -40, 72.4, 50]


def main():
    c2f(DATA)
    present()


def c2f(data):
    CeliusTemps = DATA
    FarhenheitTemps = []
    for x in data:
        Fahr = float(((9 * x) / 5) + 32)
        FarhenheitTemps.append(Fahr)
    zipped = zip(FarhenheitTemps, CeliusTemps)
    return list(zipped)


def present():
    pprint.pprint(c2f(DATA))


if __name__ == '__main__':
    main()
