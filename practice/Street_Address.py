def address(street, city, state, zip_code):
    address = f"{street}, {city}, {state} {zip_code}"
    print(address)
    return address
   
    

s = input("Enter street: ")
c = input("Enter city: ")
st = input("Enter state: ")
z = input("Enter zip code: ")

print("Your adress is :" +  address(s, c, st, z))
print()
print("Your adress is: " )
address(s, c, st, z)
