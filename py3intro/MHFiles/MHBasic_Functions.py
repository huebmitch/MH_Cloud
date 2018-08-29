def main():
    print_message()


def get_message():
    return "Hello, TDS World"


def print_message():
    message = get_message()
    print(message)


if __name__ == '__main__':
    main()

