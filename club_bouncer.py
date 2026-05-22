user_input =  input("How old are you? ")

try:
    # user_input = int(age)
    # if not isinstance(user_input, (int, float)):
    #    print("Your input age is not a number!"); exit()
    # if not user_input.isdigit():
    #    print("Your input age is not a valid whole number."); exit()
    # elif user_input < 0:
    #    print("Your input age cannot be negative!"); exit()
    # else:
    
    age = int(user_input)

except ValueError:
    print("Error: Input is not an integer. \n - Please enter a valid age.")
    exit()

if age < 18:
    print("Access denied. Too young!")
elif age > 18 and age <= 20:
    print("You can come in, but no drinking!")
else:
    print("Welcome in! Enjoy your night")


