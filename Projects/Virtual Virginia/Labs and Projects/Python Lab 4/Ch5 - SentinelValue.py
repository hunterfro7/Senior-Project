#Input an integer to start
data = eval(input("Enter an integer (the input ends " +
                   "if it is 0: "))

#Keep reading data until the input is 0
sum = 0
while data !=0:
    #Add integer to sum
    sum += data
    
    #Reenter an integer and go back to the top of the loop
    data = eval(input("Enter an integer (the input ends " +
                       "if it is 0: "))

#Output the sum
print("The sum is", sum)
