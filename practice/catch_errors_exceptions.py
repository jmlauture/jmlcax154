
while True:
    try:
        good_number = int(input("Enter a number to check if it's divisible by 2: "))
                            
        if good_number % 2 == 0:
            print("This is a good number", good_number)
            break    
        else:
            print("This is not a good number", good_number)

    except ValueError:
        print("This is an invalid number, try again")
        continue
    except KeyboardInterrupt:
        print("Program interrupted by user")
        break
    except:
        print("An error occurred, try again")
        continue
