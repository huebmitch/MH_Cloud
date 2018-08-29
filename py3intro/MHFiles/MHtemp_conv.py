import pprint


def main(temp):
    c2f(temp)
    f2c(temp)
    presentFC(temp)


def c2f(temp):
    Fahr = ((9 * float(temp)) / 5.0) + 32
    return Fahr


def f2c(temp):
    Cel = (float(temp) - 32) * (5.0 / 9)
    return Cel


def presentFC(temp):
    pprint.pprint(c2f(temp))
    pprint.pprint(f2c(temp))


if __name__ == '__main__':
    main(100)
