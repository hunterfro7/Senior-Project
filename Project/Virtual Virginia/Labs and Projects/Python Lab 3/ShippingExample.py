#Enter the shipping destination
print("You will choose a shipping location based on the following choices:")
print("  1 for the continental US, 2 for Alaska and Hawaii, and 3 for outside the US")

location = eval(input("\nEnter the number for the shipping destination: "))

# decisions to determine what price is associated with the different 
# shipping locations
# if (location = continental US) then display $5.00
# if (location = Alaska or Hawaii) then display $10.00
# else then display $20.00
if(location == 1):
    print("Shipping is $5.00")
elif(location == 2):
    print("Shipping is $10.00")
elif(location == 3):
    print("Shipping is $20.00")
else:
    print("Invalid entry")
