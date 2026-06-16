def is_even(num):
    """
    Define a function is_even(num) that returns True if num is even or False otherwise.
    """
    while True:
        try:
            num = input("Enter a number ")
        except ValueError:
            print("Invalid input, you need to enter a valid number")
            continue

        if int(num) % 2 == 0:
            result = True
        else:
            result = False
            
    print(result)

    is_even(num)

