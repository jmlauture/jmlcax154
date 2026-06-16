# Using a for loop for iterations
def sum_even_numbers():
    start = 1
    
    # If you want to get any end number from the user before starting the loop
    # end_num = int(input("Enter the end number for your range: "))
    end_num = 50

    # Iterating through the range with a for loop
    total_sum = 0
    for num in range(start+1,end_num+2,2):    
        total_sum += num

    X = total_sum
    print(f"The sum of even numbers in your range {start} to {end_num} is: {X}")

# Iterating through the range with while loop
def sum_even_numbers_while():  
    # Initialize the sum variable and the starting number
    total_sum = 0
    number = 1

    # Loop through all numbers from 1 to 50
    while number <= 50:
        # Check if the number is even
        if number % 2 == 0:
            total_sum += number
        # Increment the number to avoid an infinite loop
        number += 1

    # Print the final result in the requested format
    X= total_sum
    print(f"The sum of even numbers in your range 1 to 50 is: {X}")

# Alternative (More Efficient) Approach
def sum_even_numbers_efficient():
    total_sum = 0
    number = 2  # Start at the first even number

    while number <= 50:
        total_sum += number
        number += 2  # Skip directly to the next even number
        X = total_sum
    print(f"The sum of even numbers in your range 1 to 50 is: {X}")


print("Results with for loop: \n------------------------------")
sum_even_numbers()
print("\nResults with while loop: \n------------------------------")
sum_even_numbers_while()
print("\nResults with while looop efficient approach: \n------------------------------")
sum_even_numbers_efficient()


# Output Example: 

#Results with for loop:
#------------------------------
#The sum of even numbers in your range 1 to 50 is: 650

#Results with while loop:
#------------------------------
#The sum of even numbers in your range 1 to 50 is: 650

#Results with efficient approach with while loop:
#------------------------------
#The sum of even numbers in your range 1 to 50 is: 650

# Comparison of while loop and for loop approaches:
#
# Yes, both the for loop and while loop approaches produce the exact same result: 650. 
# The for loop iterates through the range of numbers and checks for even numbers, 
# while the while loop does the same but with a different structure. 
# The efficient approach with the while loop directly iterates through even numbers, 
# which is more efficient and also yields the same result.   

# The for loop approach is considered clearer, more elegant and avoids infinite loops.

# The biggest disadvantage of a while loop is human error. 
# If you accidentally forget to include the increment step at the bottom of a while loop, 
# the code will run forever, freezing your computer or crashing your terminal.