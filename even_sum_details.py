# Using a for loop for iterations
def sum_even_numbers():
    even_numbers = []
    start = 2
    
    # If you want to get any end number from the user before starting the loop
    # end_num = int(input("Enter the end number for your range: "))
    end_num = 50

    # Iterating through the range with a for loop
    for num in range(start,end_num+2,2):    
        if num % 2 == 0:
            # Append the even number to the list - New even number list
            even_numbers.append(num)

            # Or swap the list
            # even_numbers.insert(0, num)

            # Print the current list of even numbers
            # print("Current list of even numbers:", even_numbers)

            current_sum = sum(even_numbers)
            
            # Print the current sum of even numbers
            # print("Current sum of even numbers:", current_sum)

     
    # X = sum(even_numbers)

    X = current_sum
    print(f"The sum of even numbers in your range {start} to {end_num} is: {X}")

# Iterating through the range with while loop
def sum_even_numbers_while():  
    even_numbers = []
    thenumber = 1
    # If you want to get any end number from the user before starting the loop
    # end_num = int(input("Enter the end number for your range: "))
    end_num = 50
    while thenumber <= end_num:
        if thenumber % 2 == 0:
            even_numbers.append(thenumber)
        thenumber += 1

    X = sum(even_numbers)
    print(f"The sum of even numbers in your range 1 to {end_num} is: {X}")

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


# Output: 

#Results with for loop:
#------------------------------
#The sum of even numbers in your range 1 to 50 is: 600

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
