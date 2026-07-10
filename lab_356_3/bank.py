#!/usr/bin/env python3

""" 
bank.py  - Definition of the bank accounts 
An implementation of BankAccount, SavingsAccount, and custom exception classes.
"""
# ==========================================
# Task 3: Custom Exception Class
# ==========================================
class InsufficientFundsError(Exception):
    """Exception raised when a withdrawal exceeds the available account balance."""
    def __init__(self, account_number, attempt_amount, current_balance):
        self.account_number = account_number
        self.attempt_amount = attempt_amount
        self.current_balance = current_balance
        super().__init__(
            f"Insufficient funds: Cannot withdraw ${attempt_amount:.2f} "
            f"from account {account_number}. Available balance: ${current_balance:.2f}."
        )

# ==========================================
# Task 1: Defining the Base Class
# ==========================================

class BankAccount:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount):
        """Adds a positive amount to the account balance."""
        if amount <=0:
            raise ValueError(f"Deposit amount must be positive and greater than zero, {amount} is not valid")
        self.balance += amount
        return f"Deposited {amount}. New balance is {self.balance}"

    def withdraw(self, amount):
        """Subtracts a given amount if sufficient funds exist. Raises custom error otherwise."""
        if amount < 0:
            raise ValueError(f"Withdrawal amount must be positive and greater than zero, {amount} is not valid")
        
        if amount > self.balance:
            # Task 3 integration: raising custom exception instead of ValueError
            raise InsufficientFundsError(self.account_number, amount, self.balance)
            #raise ValueError(
            #    f"Insufficient funds or invalid withdrawal amount {amount}, \n  - Balance did not change and is still {self.balance}"
            #)
        self.balance -= amount
        return f"Withdrew {amount}. New balance is {self.balance}"

    def __str__(self):
        return f"Account {self.account_number} – Owner: {self.owner}, Balance: ${self.balance:.2f}"
    

# ==========================================
# Test Code Demonstration
# ==========================================
if __name__ == "__main__":
    print("=== TASK 1: TESTING BASE BANK ACCOUNT ===")
    # Create an instance of BankAccount
    account1 = BankAccount("123456", "Jimmy Lopez", 1000.0)
    print("New Bank Account - Initialized: ", account1)
    print("\n" + "-"*50 + "\n")

    # Demonstrate a successful deposit
    try:   
        print(account1.deposit(500.0))
        print("After $500 deposit:", account1)
        print("\n" + "-"*50 + "\n")


    except ValueError as error:
        # This prints the message created inside the f-string
        print(error)

    # Trying to deposit a negative amount
    try:        
        print(account1.deposit(-50.0))       

    except ValueError as error:
        # This prints the message created inside the f-string
        print(error)
        print("\n" + "-"*50 + "\n")

    # Demonstrate a successful withdrawal
    try:        
        print(account1.withdraw(200.0))
        print("After $200 withdrawal:", account1)
        print("\n" + "-"*50 + "\n")
    except ValueError as error:
        # This prints the message created inside the f-string
        print(error)

    # Attempt a withdrawal that exceeds balance to trigger/catch custom exception (error handling)
    print("\nAttempting to overdraw...")
    try:        
        print(account1.withdraw(2000.0))
    except InsufficientFundsError as e:
        # This prints the message created inside the f-string
        print(f"Caught Expected Error -> {e}")

    print("Final account balance - ", account1)

    print("\n" + "="*50 + "\n")
