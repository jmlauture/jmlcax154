# Lab : User Interaction and Input 
# Author: Jean Lauture
# To see the outputs of this code, 
# run it in a Python environment (like VS Code, Jupyter Notebook, PyCharm, 
# or the command line) 
# python3 secret_password.py  
#


counter = 0
    
while True:
    password = input("Enter the secret password: ")
    if password == "python123":
        print("Access granted!")
        break
    else:
        print("Incorrect password. Please try again.")
        counter += 1
        if counter >= 3:
            print("Too many failed attempts. Access denied.")
            break   


