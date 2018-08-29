nums = [7, 9.7, 6.3, 0, 5.4, 2.37]

x = 2

for n in nums:
    try:
        result = x / n
    except ZeroDivisionError as err:
        print(err)
    else:
        print("Result is:", result)
    finally:
        print("Wombat")  # close resources either way
