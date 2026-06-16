# Simple discount calculator
def calculate_price(original_price, discount_rate):
    discount_amount = (original_price * discount_rate * 1/100)
    discounted_price = original_price - discount_amount
    return discounted_price

# Example usage
# original_price = 100.0  # Original price in dollars
original_price = float(input ("What is the original price ? "))
# discount_rate = 0.1  # Discount rate (10%)
discount_rate = float(input("What is the percent discount ? (Enter in percentage format): "))
discounted_price = calculate_price(original_price, discount_rate)
print(f"Original Price: ${original_price}") 
# print(f"Discount Rate: {discount_rate * 100}%")
print (f"Discount Rate: {discount_rate}")
print(f"Final Price: ${discounted_price}")

