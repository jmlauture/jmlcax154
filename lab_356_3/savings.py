#!/usr/bin/env python3

""" savings.py  - Definition of the savings account 
An implementation of SavingsAccount class that inherits from BankAccount.
"""

# ==========================================
# Task 2: Subclassing and Inheritance
# ==========================================
#from lab_356_3.bank import BankAccount
from bank import BankAccount

class SavingsAccount(BankAccount):
	def __init__(self, BankAccount, interest_rate=0.0):
		"""Initializes a SavingsAccount, calling the super class initializer."""
		super().__init__(BankAccount.account_number, BankAccount.owner, BankAccount.balance)
		#self.interest_rate = interest_rate
		self.interest_rate = float(interest_rate)  # interest rate as a percentage (e.g., 5.0 for 5%)
		
	
	def apply_interest(self):
		"""Calculates interest based on current balance and adds it to the balance."""
		interest_earned = self.balance * self.interest_rate / 100  # Convert percentage to decimal
		self.balance += interest_earned
		return f"Interest added: ${interest_earned:.2f}. New balance is ${self.balance:.2f}"


	def __str__(self):
		"""Create a string representation of the SavingsAccount object, including the interest rate
		Use f-string formatting to display the interest rate as a percentage with two decimal places
		Use the account number, owner, and balance from the parent BankAccount class
		Use string slicing to format the Savings Account number with the interest rate
		"""
		result = str(self.interest_rate)[0] # Get the first character of the interest rate string
		return f"Savings Account {self.account_number}-Sav{result} – Owner: {self.owner}, Balance: ${self.balance}, Interest Rate: {self.interest_rate:.2f}%"

# ==========================================
# Test Code Demonstration
# ==========================================
if __name__ == "__main__":
	print("=== TASK 2: TESTING SAVINGS ACCOUNT ===")
	# Create an instance of SavingsAccount (1000 balance, 5.0% interest)	
	savingsacct = SavingsAccount(BankAccount("123456", "Jimmy Lopez", 1000.0), interest_rate=5.0)
	print("\n" + "-"*50 + "\n")
	
	# Demonstrate the inherited deposit and withdraw functionalities  
	#savingsacct1.deposit(1000)
	#print(savingsacct1)
	print(savingsacct.deposit(1000.0))
	print("After $500 deposit (inherited):", savingsacct) 
	print("\n" + "-"*50 + "\n")
	

	#savingsacct1.withdraw(500)  
	#print(savingsacct1)
	print(savingsacct.withdraw(500.0))
	print("After $200 withdrawal (inherited):", savingsacct)
	print("\n" + "-"*50 + "\n")
	
	# Call apply_interest and print to verify balance and representation updates
	print("\nApplying annual interest...")

	#savingsacct1.apply_interest()
	print(savingsacct.apply_interest())
	
	# Print the account details
	print("After applying interest:", savingsacct)
	print("\n" + "="*50 + "\n")
	